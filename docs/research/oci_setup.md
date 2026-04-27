# OCI Always Free Tierを活用した高スペック開発環境構築ガイド：Ubuntu, n8n, OpenHands, Difyサーバーの統合

## I. はじめに

Oracle Cloud Infrastructure (OCI) のAlways Free Tierは、開発者や小規模ビジネスオーナーにとって、費用を気にすることなくクラウドインフラストラクチャを探索し、アプリケーションをデプロイするための魅力的な機会を提供します ^^。このティアは、無期限で利用可能なサービスと、30日間または300ドルのクレジットが利用できる「Free Trial」サービスで構成されており、後者はすべてのOCIサービスを試用するために利用できますが、本レポートの目的は、この「Always Free」枠を最大限に活用し、継続的な無料利用を実現することに焦点を当てます ^^。**   **

Always Freeサービスには、Computeインスタンス、ストレージ（ブロックボリューム、オブジェクトストレージ）、ネットワーキング、ロードバランサー、データベースなど、アプリケーションを構築・テストするために不可欠なコアコンポーネントが含まれています ^^。これらのリソースは、エンタープライズグレードの仮想ネットワーク上で提供され、プロトタイプ開発からデータパイプライン構築まで、幅広いユースケースに対応可能です ^^。**   **

本レポートは、OCIを初めて利用する方を対象に、継続して無料で利用可能な範囲で、Ubuntu開発環境、n8nサーバー、OpenHandsサーバー、Difyサーバーといった複数のオープンソースアプリケーションを「高スペック」かつ「快適に動作」する環境として構築するための詳細なステップバイステップガイドを提供します。特に、OCI Always Free Tierの制約内で最大限のパフォーマンスを引き出すため、ArmベースのAmpere A1 Flexインスタンスを単一のVMとして活用し、その上でDockerとDocker Composeを用いて複数のアプリケーションを効率的に統合する戦略を詳述します。これにより、利用者は複雑なクラウドデプロイメントの概念を理解し、実践的なスキルを習得しながら、費用をかけずに自身のプロジェクトを立ち上げることができます。

## II. OCI Always Free Tierの理解と最適なリソース選択

OCI Always Free Tierを効果的に活用するためには、提供されるリソースの特性と制限を深く理解することが不可欠です。特にComputeインスタンスの選択は、構築する環境の性能と安定性を大きく左右します。

### Always Free Computeインスタンスの詳細

OCI Always Free Tierでは、Computeインスタンスとして主に2種類のプロセッサアーキテクチャが提供されています ^^。**   **

* **AMDベースのVM (VM.Standard.E2.1.Micro):** 各インスタンスは1/8 OCPUと1 GBのメモリを提供し、最大2つのVMを無料枠で利用できます ^^。これは非常に小規模なワークロードやテスト環境に適していますが、本レポートで要求される「高スペック」な開発環境や複数のアプリケーションの同時実行には不十分です。例えば、n8nは最低2vCPUと4-8GB RAMを推奨し ^^、OpenHandsは最低4GB RAMとモダンなプロセッサを推奨し ^^、Difyは最低2コアCPUと4GB RAMを必要とします ^^。AMDインスタンスのスペックでは、これらのアプリケーションのいずれか一つを単独で動作させることすら困難であり、ましてや複数アプリケーションの「高スペック」かつ「快適な動作」は実現不可能です。**   **
* **ArmベースのAmpere A1 Computeインスタンス (VM.Standard.A1.Flex):** こちらは月あたり3,000 OCPU時間と18,000 GB時間の無料枠が提供され、これは実質的に4 OCPUと24 GBのメモリに相当します ^^。このリソースは1つの高性能VMとして、または最大4つのより小さなVMに分割して使用することが可能です ^^。利用者の目標が「高スペック」な環境と、各アプリケーションが「快適に動作」することである場合、このAmpere A1 Flexインスタンスが唯一の現実的な選択肢となります。このインスタンスは、上記のすべてのアプリケーションの最低要件を十分に満たし、さらに複数のアプリケーションを統合して動作させるための十分な余裕を提供します。したがって、単一の高性能Armインスタンスにすべてのサービスを統合するというデプロイメント戦略が、無料枠の制約下で最も最適であるという結論が導き出されます。**   **

上記の分析に基づき、本レポートでは**ArmベースのAmpere A1 Flexインスタンス** を推奨し、その無料枠の最大リソース（4 OCPU, 24 GBメモリ）を単一のVMに割り当てる構成を前提として、以降の手順を解説します。

### ストレージ（ブロックボリューム、オブジェクトストレージ）の制限

OCI Always Free Tierでは、全テナンシーで合計200 GBのAlways Freeブロックボリュームストレージが提供されます ^^。この容量は、Computeインスタンスのブートボリュームと、追加で作成するブロックボリュームの合計に適用されます。各Computeインスタンスのブートボリュームはデフォルトで50 GBを消費します ^^。もし利用者がブートボリュームのサイズを最大200GBにカスタマイズした場合、無料枠のブロックボリュームストレージをすべて消費することになり、追加のブロックボリュームを作成する余地がなくなります ^^。**   **

無料枠のストレージとバックアップには重要な制約があります。ボリュームバックアップは最大5つまでしか作成できません ^^。この5つのバックアップ制限は、頻繁なバックアップや長期的な履歴保持には不十分である可能性があります。特に、ブロックボリュームのバックアップは書き込み済みブロック全体を対象とするため、ボリュームサイズが大きいほどバックアップサイズも大きくなります ^^。例えば、50GBのブートボリュームのフルバックアップを複数回取るだけでも、すぐに5つのバックアップ制限に達してしまう可能性があります。このストレージとバックアップの制約は、無料枠での運用において非常に重要な考慮事項となります。利用者は、ブートボリュームのサイズをデフォルトの50GBに抑え、アプリケーションのデータ（特に頻繁に更新されるもの）は、別のブロックボリュームに分離するか、あるいは無料枠のオブジェクトストレージ（20GB）や外部のバックアップソリューションへのエクスポートを検討する必要があります。これにより、限られた無料枠内で効率的なデータ管理と災害復旧計画を立てることが可能となります。**   **

オブジェクトストレージに関しては、Always Freeアカウントでは、Standard、Infrequent Access、Archiveの各ティアで合計20 GBのデータストレージが利用可能です。これに加えて、月あたり50,000回のAPIリクエストが無料枠に含まれます ^^。**   **

### ネットワーク帯域幅とデータ転送

OCI Always Free Tierは、月あたり10 TBという非常に寛大なアウトバウンドデータ転送量を無料で提供しています。インバウンドデータ転送は一般的に無料です ^^。このデータ転送量は、他の主要なクラウドプロバイダーと比較しても非常に高い水準であり、多くの開発プロジェクトや軽量なビジネスアプリケーションのニーズを十分に満たします ^^。**   **

Computeインスタンス自体のネットワーク帯域幅は、Ampere A1 Flexシェイプで1 Gbpsとされています ^^。これは一般的な用途には十分な速度です。しかし、10TBの無料データ転送量は非常に魅力的ですが、これはデータ転送の「量」に関するものであり、「速度」とは異なる概念です。利用者は複数のWebアプリケーション（n8n、OpenHands、Dify）をこの単一のVM上で動作させる計画であり、これらのアプリケーションがすべて同じ1Gbpsのネットワーク帯域幅を共有することになります。OpenHandsやDifyはLLMとの連携を伴うため、将来的には大量のデータ（例：LLMの応答、Webアセット、APIトラフィック）がネットワークを介して転送される可能性があります。単一インスタンスでの共有帯域幅（1Gbps）が、特にトラフィックが増加した場合や、複数のアプリケーションが同時に高負荷のネットワーク通信を行った場合に、パフォーマンスの潜在的なボトルネックとなる可能性があります。利用者は、無料枠の範囲内で「高スペック」を追求する上でのこのトレードオフを理解しておくべきです。これは、単に「無料枠で10TB使える」という表面的な情報だけでは見過ごされがちな、より深いパフォーマンスの考慮事項です。**   **

### 「Out of Host Capacity」問題とその対策

Ampere A1インスタンスは非常に人気が高いため、特に需要の高いリージョンや時間帯では、「Out of Host Capacity」（ホスト容量不足）というエラーに遭遇し、インスタンスをすぐに作成できないことがあります ^^。これは、無料枠のインスタンスが物理的なハードウェアリソースに依存するため、供給が追いつかない場合に発生します。手動で何度もインスタンス作成を試みるのは、非常に時間と労力がかかり、利用者が直面する可能性のある具体的な初期障害です。**   **

この問題に対処するためには、OCIコンソールでの手動作成を何度も繰り返すのではなく、Terraform設定を保存し、OCI Cloud Shellを活用した自動化スクリプトによるインスタンス作成の再試行が非常に効果的です ^^。このスクリプトは、利用可能な容量が見つかり次第、自動的にインスタンスのプロビジョニングを停止するため、利用者は他の作業に集中できます。この問題は、単に「運が悪かった」で済まされるものではなく、無料枠の特性として認識し、戦略的に対処すべき課題です。自動化スクリプトを利用することで、利用者はインスタンスのプロビジョニングをより確実に、かつ効率的に行うことができ、この初期の障壁を乗り越えてスムーズに次の環境構築ステップに進むことが可能になります。**   **

### 推奨されるインスタンス構成

上記の詳細な検討に基づき、利用者の「高スペック」かつ「継続して無料」という要件を満たすための最適なOCI Always Freeインスタンス構成を以下に示します。この表は、OCI Always Free Tierの複雑な仕様と利用者の具体的な要求（高スペック、無料、複数アプリのデプロイ）を統合し、最も効率的で効果的なインスタンス構成を「一目で理解できる」形で提供します。これにより、利用者は自信を持って初期設定を進め、無料枠の範囲内で最大限の価値を引き出すことが可能となります。

**Table 1: 推奨OCI Always Freeインスタンス構成**


| 項目                       | 設定値                             | 備考                                                                                                                                                                      | 参照 |
| ---------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **インスタンスタイプ**     | VM.Standard.A1.Flex                | ArmベースのAmpere A1インスタンス。OCI無料枠で最も高性能な選択肢であり、複数のアプリケーションの統合に適しています。                                                       | ^^   |
| **OCPU**                   | 4 OCPU                             | 無料枠で利用可能な最大OCPU数。n8n、OpenHands、Difyの各アプリケーションの最低要件を十分に満たし、快適な動作を可能にします。                                                | ^^   |
| **メモリ**                 | 24 GB                              | 無料枠で利用可能な最大メモリ量。複数のアプリケーションが同時に稼働する際の安定性とパフォーマンスを確保します。                                                            | ^^   |
| **ブートボリュームサイズ** | 50 GB                              | デフォルトのブートボリュームサイズ。これにより、200GBの無料ストレージ枠を有効活用し、必要に応じて追加のブロックボリュームやバックアップに容量を割り当てることができます。 | ^^   |
| **OSイメージ**             | Ubuntu 22.04 LTS (または最新のLTS) | 開発環境として広く利用されており、Dockerのサポートも充実しています。安定性と長期サポートが魅力です。                                                                      | ^^   |
| **パブリックIP**           | 1 (自動割り当て)                   | 単一のComputeインスタンスに割り当てられるパブリックIPは通常1つです。Nginx Reverse Proxyを導入することで、この単一IPを通じて複数のサービスにアクセス可能にします。         | ^^   |
| **ネットワーク帯域幅**     | 1 Gbps                             | インスタンスあたりの最大ネットワーク帯域幅。一般的なWebアプリケーションや開発ワークロードには十分な速度です。                                                             | ^^   |
| **データ転送**             | 10 TB/月 (アウトバウンド)          | 無料枠の範囲内で提供されるデータ転送量。非常に寛大であり、ほとんどのユースケースで追加費用を心配する必要はありません。                                                    | ^^   |

## III. 環境構築のステップバイステップガイド

本セクションでは、OCI Always Free Tier上で推奨されるAmpere A1 Flexインスタンスを利用し、Ubuntu開発環境、n8n、OpenHands、Difyサーバーを構築するための具体的な手順を詳述します。

### ステップ1: OCIアカウントの準備とSSHキーペアの生成

OCIのComputeインスタンスをプロビジョニングする前に、OCIアカウントの準備と、インスタンスへのセキュアなアクセスに必要なSSHキーペアの生成を行います。

#### OCIアカウントのサインアップ

まず、Oracle Cloudの公式ウェブサイトから無料ティアアカウントにサインアップします ^^。サインアップには有効なクレジットカード情報が必要ですが、これは本人確認と不正利用防止のためであり、Always Freeサービスを利用する限りは請求が発生することはありません ^^。Oracle Cloud Free Tierの規約により、一人につき一つの無料アカウントのみが許可されており、複数のアカウントを作成しようとすると、アカウントの停止や終了につながる可能性があるため注意が必要です ^^。**   **

#### SSHキーペアの生成方法

OCIのLinuxインスタンスへのセキュアな接続には、パスワード認証ではなくSSHキーペア（公開鍵と秘密鍵のセット）が使用されます ^^。秘密鍵は利用者の手元に安全に保管し、公開鍵はインスタンス作成時にOCIに提供します。**   **

* **Windowsユーザーの場合:**
  * Windows 10/Server 2019以降のシステムでは、OpenSSHクライアントがデフォルトでインストールされているため、PowerShellまたはGit Bashのターミナルから`ssh-keygen`コマンドを使用するのが最も簡単です ^^。**   **
  * `ssh-keygen`コマンドを実行し、キーペアの保存場所とパスフレーズを設定します（パスフレーズはオプションですが、セキュリティを高めるために推奨されます）。デフォルトでは、ユーザーのホームディレクトリの`.ssh`フォルダに`id_rsa`（秘密鍵）と`id_rsa.pub`（公開鍵）が生成されます ^^。**   **
  * もしPuTTYを使用したい場合は、PuTTY Key Generator (`puttygen.exe`) をダウンロードして使用します。SSH-2 RSAタイプ、2048ビットのキーを生成し、秘密鍵（.ppk形式）と公開鍵（テキストファイルにコピー＆ペーストして.pub形式で保存）を生成します ^^。秘密鍵はPuTTY専用形式であるため、OpenSSHで利用する場合は別途変換が必要になる場合があります。**   **
* **Linux/macOSユーザーの場合:**
  * ターミナルを開き、`ssh-keygen`コマンドを実行します。
  * デフォルトのファイルパスとファイル名（`~/.ssh/id_rsa`および`~/.ssh/id_rsa.pub`）を受け入れ、パスフレーズは任意で設定します ^^。**   **
  * 生成された`id_rsa.pub`が公開鍵、`id_rsa`が秘密鍵です。秘密鍵は絶対に他者に共有せず、安全に保管してください。

### ステップ2: 仮想クラウドネットワーク (VCN) の設定

VCNは、OCI上でインスタンスが通信するためのプライベートネットワークです。OCIの無料ティアアカウントでは、デフォルトでVCNが作成される場合がありますが、ここでは基本的な作成手順を説明します。

* **VCNの作成:**
  1. OCIコンソールにログインします。
  2. ナビゲーションメニューを開き、「ネットワーキング」から「仮想クラウド・ネットワーク」を選択します ^^。**   **
  3. 「リスト・スコープ」で、インスタンスを作成するコンパートメントを選択します。
  4. 「VCNの作成」をクリックします ^^。**   **
  5. 「VCNと関連リソースの作成」オプションを選択すると、インターネットゲートウェイ、ルートテーブル、サブネットが自動的に作成され、設定が簡素化されます ^^。**   **
  6. VCNの名前を入力します（例: `MyFreeTierVCN`）。
  7. IPv4 CIDRブロックを指定します（例: `10.0.0.0/16`）。
  8. 「このVCNでDNSホスト名を使用」オプションを有効にし、DNSラベルを指定します ^^。**   **
  9. 「VCNの作成」をクリックし、VCNがプロビジョニングされるのを待ちます。

#### セキュリティリストとネットワークセキュリティグループ (NSG) の設定

OCIでは、インスタンスへのトラフィックを制御するためにセキュリティリストとネットワークセキュリティグループ (NSG) の2つの主要なツールが提供されます ^^。セキュリティリストはサブネット全体に適用されるファイアウォールルールであるのに対し、NSGは個々の仮想ネットワークインターフェースカード (VNIC) や特定のグループに適用されるため、よりきめ細やかな制御が可能です ^^。Oracleは、将来的な機能強化の優先度やマイクロセグメンテーション戦略の観点から、NSGの使用を推奨しています ^^。**   **

推奨されるアプローチは、すべてのセキュリティリストおよびNSGルールにおいてホワイトリスト方式を採用し、アプリケーションやワークロードに必要な特定のソース、プロトコル、ポートのみを許可することです ^^。**   **

* **推奨されるネットワーク設定（NSGベース）:**
  * **SSH (ポート22):** 任意のソースIPアドレス (`0.0.0.0/0`) からのTCPトラフィックを許可します。これはインスタンスへの管理アクセスに必要です。
  * **HTTP (ポート80):** 任意のソースIPアドレス (`0.0.0.0/0`) からのTCPトラフィックを許可します。Nginx Reverse Proxy経由でWebサービスにアクセスするために必要です。
  * **HTTPS (ポート443):** 任意のソースIPアドレス (`0.0.0.0/0`) からのTCPトラフィックを許可します。Nginx Reverse Proxy経由でセキュアなWebサービスにアクセスするために必要です。
  * **内部Dockerコンテナ通信:** Dockerコンテナ間の通信や、Nginx Reverse Proxyから各アプリケーションコンテナへの通信を許可するために、必要に応じて内部ネットワークのポート（例: n8nの5678、OpenHandsの3000、Difyの3000など）を許可するルールを設定します。ただし、これらのポートは通常、Nginxによって内部的にプロキシされるため、外部への直接公開は不要です。

これらのルールは、Computeインスタンス作成時にNSGとして設定するか、インスタンス作成後に既存のNSGに追加します。

### ステップ3: Computeインスタンスのプロビジョニング

いよいよ、推奨されるAmpere A1 Flexインスタンスをプロビジョニングします。

1. **OCIコンソールにログイン:**
   * ナビゲーションメニューから「コンピュート」を選択し、「インスタンス」をクリックします ^^。**   **
2. **インスタンスの作成:**
   * 「インスタンスの作成」をクリックします ^^。**   **
   * **名前とコンパートメント:** インスタンスの名前を入力し、使用するコンパートメントを選択します ^^。**   **
   * **配置設定:** デフォルトの可用性ドメイン (AD-1など) を使用します。無料ティアでは「Always Free Eligible」オプションが自動的に選択されることを確認します ^^。**   **
   * **イメージとシェイプ設定:** 「イメージとシェイプ」の横にある「編集」をクリックします ^^。**   **

     * **イメージ:** 「イメージの変更」をクリックし、「Ubuntu」を選択し、推奨される「Ubuntu 22.04 LTS」または最新のLTSバージョンを選択します ^^。**   **
     * **シェイプ:** 「シェイプの変更」をクリックします。
       * 「仮想マシン」を選択し、「Ampere」シリーズを選択します ^^。**   **
       * 「VM.Standard.A1.Flex」シェイプを選択し、OCPUスライダーを「4」、メモリを「24 GB」に設定します ^^。これが無料枠で利用可能な最大リソースであり、今回の要件を満たすために不可欠です。**   **
       * 「シェイプの選択」をクリックします。
   * **ネットワーキング設定:**

     * ステップ2で作成したVCNとパブリックサブネットを選択します ^^。**   **
     * 「パブリックIPv4アドレスの割り当て」が「はい」になっていることを確認します ^^。**   **
     * 「ネットワーク・セキュリティ・グループを使用してトラフィックを制御」オプションを選択し、ステップ2で設定したNSGを選択または新規作成して適用します。
   * **SSHキーの追加設定:**

     * 「SSHキーの生成」セクションで、「公開キーの貼り付け」を選択し、ステップ1で生成した公開鍵（`id_rsa.pub`の内容）をテキストエリアに貼り付けます ^^。または、「公開キー・ファイルのアップロード」を選択して公開鍵ファイルを指定することもできます。**   **
   * **ブート・ボリューム設定:**

     * デフォルトの50 GBのブートボリュームサイズを維持します ^^。これにより、200GBの無料ストレージ枠を有効活用し、必要に応じて追加のブロックボリュームやバックアップに容量を割り当てることができます。**   **
   * **インスタンスの作成:**

     * すべての設定を確認し、「作成」をクリックします ^^。**   **

#### 「Out of Host Capacity」エラーへの対応

インスタンスの作成中に「Out of Host Capacity」エラーが発生した場合、これはAmpere A1インスタンスの人気によるものです ^^。手動で何度も再試行する代わりに、以下の自動化スクリプトを利用することをお勧めします。**   **

1. インスタンス作成画面でエラーが出た場合でも、「スタックとして保存」オプションを使用してVMの仕様設定を保存します ^^。**   **
2. 保存したスタックを開き、「プランの作成」を実行します。成功したら、Terraform ConfigurationとPlanをダウンロードします ^^。**   **
3. OCI Cloud Shellを開き、ダウンロードしたTerraform設定ファイル（`main.tf`など）と、以下の自動化スクリプトをアップロードまたは作成します ^^。**   **

   **Bash**

   ```
   #!/bin/bash
   # Define the availability domains (UPDATE with your region's ADs)
   AVAILABILITY_DOMAINS=("AD-1" "AD-2" "AD-3") # 例: 東京リージョンならAP-TOKYO-1-AD-1など
   COMPARTMENT_OCID="ocid1.compartment.oc1..xxxxxx" # あなたのコンパートメントOCID
   INSTANCE_NAME="MyAmpereInstance" # 作成するインスタンス名
   IMAGE_OCID="ocid1.image.oc1.ap-tokyo-1.xxxxxx" # Ubuntu 22.04 LTSのイメージOCID
   SHAPE="VM.Standard.A1.Flex"
   OCPUS=4
   MEMORY_GB=24
   SUBNET_OCID="ocid1.subnet.oc1.ap-tokyo-1.xxxxxx" # あなたのサブネットOCID
   SSH_PUBLIC_KEY_FILE="~/.ssh/id_rsa.pub" # あなたの公開鍵ファイルパス

   # Function to create instance
   create_instance() {
       local ad=$1
       echo "Attempting to create instance in Availability Domain: $ad"
       oci compute instance launch \
           --availability-domain "$ad" \
           --compartment-id "$COMPARTMENT_OCID" \
           --display-name "$INSTANCE_NAME" \
           --image-id "$IMAGE_OCID" \
           --shape "$SHAPE" \
           --assign-public-ip true \
           --subnet-id "$SUBNET_OCID" \
           --ssh-authorized-keys-file "$SSH_PUBLIC_KEY_FILE" \
           --metadata '{"ssh_authorized_keys": "'"$(cat "$SSH_PUBLIC_KEY_FILE")"'"}' \
           --shape-config "ocpus=$OCPUS,memory_in_gbs=$MEMORY_GB" \
           --wait-for-state RUNNING
   }

   # Loop through availability domains until instance is created
   for ad in "${AVAILABILITY_DOMAINS[@]}"; do
       if create_instance "$ad"; then
           echo "Instance created successfully in $ad."
           exit 0 # Exit the script after successful execution.
       else
           echo "Failed to launch instance in $ad. Trying the next one..."
           sleep 3 # Wait 3 seconds before trying the next domain.
       fi
   done

   echo "Failed to create instance in all available domains."
   exit 1
   ```

   * **注意:** 上記スクリプトの`AVAILABILITY_DOMAINS`、`COMPARTMENT_OCID`、`IMAGE_OCID`、`SUBNET_OCID`は、利用者の環境に合わせて正確なOCIDと値を更新する必要があります。`IMAGE_OCID`は、OCIコンソールでUbuntuイメージの詳細から取得できます。
4. スクリプトファイルを実行可能にし（`chmod +x your_script.sh`）、実行します。スクリプトはインスタンスが正常にプロビジョニングされるまで、利用可能なアベイラビリティドメインを巡回しながら自動的に再試行します ^^。**   **

#### インスタンスへのSSH接続

インスタンスのステータスが「RUNNING」になったら、SSHを使用して接続できます。

* **Windows (OpenSSH/Git Bash) / Linux / macOS:**
  `ssh -i ~/.ssh/id_rsa ubuntu@<インスタンスのパブリックIPアドレス>`
  * `~/.ssh/id_rsa`はステップ1で生成した秘密鍵のパスに置き換えます。
  * `<インスタンスのパブリックIPアドレス>`は、OCIコンソールでインスタンスの詳細画面から確認できる「パブリックIPv4アドレス」に置き換えます ^^。**   **
  * デフォルトのユーザー名は`ubuntu`です ^^。**   **
* **Windows (PuTTY):**
  1. PuTTYを起動します。
  2. 「Host Name (or IP address)」にインスタンスのパブリックIPアドレスを入力します ^^。**   **
  3. 「Category」ツリーで「Connection」->「Data」を選択し、「Auto-login username」に`ubuntu`と入力します ^^。**   **
  4. 「Category」ツリーで「Connection」->「SSH」->「Auth」を選択し、「Private key file for authentication」の「Browse」をクリックして、ステップ1で生成した秘密鍵（.ppk形式）を選択します ^^。**   **
  5. 「Open」をクリックして接続します。初回接続時にはセキュリティアラートが表示される場合がありますが、「はい」をクリックして続行します ^^。**   **

### ステップ4: DockerとDocker Composeのインストール

ComputeインスタンスにSSH接続した後、DockerとDocker Composeをインストールし、コンテナ化されたアプリケーションの実行環境を準備します。

#### UbuntuへのDocker EngineとDocker Composeプラグインのインストール

Docker EngineとDocker Composeプラグインは、Ubuntuの公式リポジトリからインストールすることが推奨されます ^^。**   **

1. **既存のDockerパッケージのアンインストール (もしあれば):**
   **Bash**

   ```
   sudo apt-get remove docker docker-engine docker.io containerd runc docker-compose docker-compose-v2
   ```
2. **Dockerの公式GPGキーとリポジトリの追加:**
   **Bash**

   ```
   sudo apt-get update
   sudo apt-get install ca-certificates curl gnupg -y
   sudo install -m 0755 -d /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   sudo chmod a+r /etc/apt/keyrings/docker.gpg
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   ```
3. **Dockerパッケージのインストール:**
   **Bash**

   ```
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
   ```
4. **Dockerの動作確認:**
   **Bash**

   ```
   sudo docker run hello-world
   ```

   このコマンドはテストイメージをダウンロードして実行し、成功メッセージが表示されればインストールは完了です ^^。**   **
5. **現在のユーザーをdockerグループに追加 (sudoなしでDockerコマンドを実行するため):**
   **Bash**

   ```
   sudo usermod -aG docker $USER
   newgrp docker
   ```

   `newgrp docker`を実行するか、SSHセッションを一度終了して再接続することで、変更が適用されます。

#### UFW (Uncomplicated Firewall) の設定

UFWはUbuntuのデフォルトファイアウォールですが、Dockerは独自の`iptables`ルールを管理するため、UFWとDockerが競合し、意図しないポートが公開される可能性があります ^^。これを解決するために、**   **

`ufw-docker`スクリプトを使用してUFWとDockerを適切に連携させることが推奨されます。

1. **`ufw-docker`スクリプトのダウンロードとインストール:**
   **Bash**

   ```
   sudo wget -O /usr/local/bin/ufw-docker https://github.com/chaifeng/ufw-docker/raw/master/ufw-docker
   sudo chmod +x /usr/local/bin/ufw-docker
   ```
2. **`ufw-docker`のインストールとUFWルールの適用:**
   **Bash**

   ```
   sudo ufw-docker install
   ```

   このコマンドは、`ufw`がDockerコンテナのトラフィックを適切に処理するためのルールを`/etc/ufw/after.rules`に追加します ^^。**   **
3. **UFWの再起動またはリロード:**
   **Bash**

   ```
   sudo systemctl restart ufw
   # または
   sudo ufw reload
   ```
4. **必要なポートの許可:**

   * **SSH (22/tcp):**
     **Bash**

     ```
     sudo ufw allow 22/tcp
     ```
   * **HTTP (80/tcp) および HTTPS (443/tcp):**
     **Bash**

     ```
     sudo ufw allow 80/tcp
     sudo ufw allow 443/tcp
     ```
   * **Dockerコンテナへの内部アクセス (Nginx Reverse Proxy用):**

     * Nginx Reverse ProxyがDockerホスト上で動作し、各アプリケーションコンテナと通信する場合、UFWは通常、Dockerの内部ネットワークトラフィックをブロックしません。しかし、明示的に許可したい場合は、`ufw-docker`コマンドでコンテナ名とポートを指定できます。例えば、n8nの5678ポートを許可する場合：
       **Bash**

       ```
       sudo ufw-docker allow n8n 5678
       ```

       ただし、Nginx Reverse Proxyを使用する場合、これらのポートは外部に直接公開する必要がないため、通常はUFWで明示的に許可する必要はありません。Nginxが外部からのトラフィックを受け取り、内部のDockerネットワークにルーティングします。
5. **UFWの有効化:**
   **Bash**

   ```
   sudo ufw enable
   ```

   警告が表示されたら「y」を入力して続行します。

### ステップ5: 各アプリケーションのDocker Composeデプロイ

DockerとDocker Composeがインストールされ、ファイアウォールが適切に設定されたら、いよいよ各アプリケーションをデプロイします。すべてのアプリケーションを単一のインスタンス上で快適に動作させるため、Docker Composeを用いて各サービスをコンテナ化し、Nginx Reverse Proxy (NPMなど) を導入して単一のパブリックIPアドレスを通じて複数のサービスにアクセスできるようにします ^^。**   **

#### 共通の考慮事項

* **Docker Composeの利点:** Docker Composeは、複数のDockerコンテナで構成されるアプリケーションの定義と実行を管理するためのツールです。これにより、各アプリケーションの依存関係、ネットワーク設定、環境変数などを一元的に管理でき、デプロイメントの複雑さを大幅に軽減します。コンテナ化された環境は、アプリケーション間の分離を提供し、依存関係の競合を防ぎ、移植性を高めます。
* **Nginx Reverse Proxyの導入:** OCIのComputeインスタンスには通常1つのパブリックIPアドレスしか割り当てられません ^^。複数のWebアプリケーション（n8n, OpenHands, Dify）を同じIPアドレスで公開するには、Nginx Reverse Proxyのようなツールが不可欠です。Nginxは、受信したHTTP/HTTPSリクエストを、リクエストのホスト名やパスに基づいて適切なDockerコンテナにルーティングします ^^。Nginx Proxy Manager (NPM) は、GUIで簡単にリバースプロキシ設定を行えるため、初心者には特におすすめです。**   **

#### n8nサーバーのデプロイ

n8nはワークフロー自動化ツールであり、Docker Composeで簡単にデプロイできます。

1. **システム要件の確認:** n8nは、低トラフィックのプロダクション環境であれば2 vCPUs、4-8 GB RAMで動作可能とされています ^^。推奨されるAmpere A1 Flexインスタンス（4 OCPU, 24 GB RAM）は、この要件を十分に満たします。**   **
2. **作業ディレクトリの作成:**
   **Bash**

   ```
   mkdir n8n && cd n8n
   ```
3. **Docker Composeファイルの作成 (`docker-compose.yml`):**
   n8nのデータ永続化とPostgreSQLデータベースの利用を考慮した`docker-compose.yml`を作成します。
   **YAML**

   ```
   version: '3.8'

   services:
     n8n:
       image: n8nio/n8n
       container_name: n8n
       restart: unless-stopped
       ports:
         - "5678:5678" # Nginx Reverse Proxyを使用するため、外部公開は必須ではないが、テスト用に残す
       environment:
         - N8N_BASIC_AUTH_ACTIVE=true
         - N8N_BASIC_AUTH_USER=${N8N_USER}
         - N8N_BASIC_AUTH_PASSWORD=${N8N_PASSWORD}
         - DB_TYPE=postgresdb
         - DB_POSTGRESDB_HOST=db
         - DB_POSTGRESDB_PORT=5432
         - DB_POSTGRESDB_DATABASE=${POSTGRES_DB}
         - DB_POSTGRESDB_USER=${POSTGRES_USER}
         - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}
         - N8N_HOST=${N8N_SUBDOMAIN}.${DOMAIN_NAME} # Nginx Reverse Proxyのホスト名
         - N8N_PORT=443
         - N8N_PROTOCOL=https
         - WEBHOOK_URL=https://${N8N_SUBDOMAIN}.${DOMAIN_NAME}/
         - GENERIC_TIMEZONE=Asia/Tokyo # タイムゾーン設定
       volumes:
         - n8n_data:/home/node/.n8n
       depends_on:
         - db
       networks:
         - app_network

     db:
       image: postgres:12
       container_name: n8n_db
       restart: unless-stopped
       environment:
         - POSTGRES_DB=${POSTGRES_DB}
         - POSTGRES_USER=${POSTGRES_USER}
         - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
       volumes:
         - db_data:/var/lib/postgresql/data
       networks:
         - app_network

   volumes:
     n8n_data:
     db_data:

   networks:
     app_network:
       external: true # Nginx Reverse Proxyと同じネットワークを使用
   ```
4. **環境変数ファイル (`.env`) の作成:**
   `docker-compose.yml`と同じディレクトリに`.env`ファイルを作成し、以下の変数を設定します。
   **コード スニペット**

   ```
   N8N_USER=your_n8n_username
   N8N_PASSWORD=your_n8n_password
   POSTGRES_DB=n8n_database
   POSTGRES_USER=n8n_user
   POSTGRES_PASSWORD=your_db_password
   DOMAIN_NAME=your_domain.com # あなたのドメイン名
   N8N_SUBDOMAIN=n8n # n8nのサブドメイン (例: n8n.your_domain.com)
   ```
5. **Nginx Reverse Proxy用ネットワークの作成:**
   まだ作成していない場合は、Nginx Reverse Proxyが共有するDockerネットワークを作成します。
   **Bash**

   ```
   docker network create app_network
   ```
6. **デプロイ:**
   **Bash**

   ```
   docker compose up -d
   ```

   n8nのDockerイメージは、Arm64アーキテクチャをサポートしています ^^。これにより、Ampere A1インスタンス上で問題なく動作します。**   **
7. **アクセス:**
   Nginx Reverse Proxyの設定後、`https://n8n.your_domain.com` (または設定したサブドメイン) からn8nにアクセスできるようになります。

#### OpenHandsサーバーのデプロイ

OpenHandsはAIエージェントの実行環境であり、Docker DesktopまたはLinux上のDockerで動作します ^^。**   **

1. **システム要件の確認:** OpenHandsは最低4GB RAMとモダンなプロセッサを推奨しています ^^。Ampere A1 Flexインスタンス（4 OCPU, 24 GB RAM）はこれを満たします。OpenHandsはLLMとの連携を前提としており、ローカルLLMを使用する場合はGPU（16GB VRAM以上）またはApple Silicon Mac（32GB RAM以上）が強く推奨されます ^^。OCI Always Free TierにはGPUは含まれないため、クラウドベースのLLMプロバイダー（OpenAI, Anthropicなど）のAPIキーを利用するか、CPUで動作する軽量なローカルLLMモデルを検討する必要があります。**   **
2. **作業ディレクトリの作成:**
   **Bash**

   ```
   mkdir openhands && cd openhands
   ```
3. **Docker Composeファイルの作成 (`docker-compose.yml`):**
   OpenHandsのDockerイメージは、`docker.all-hands.dev/all-hands-ai/openhands`および`docker.all-hands.dev/all-hands-ai/runtime`を使用します。ただし、これらのイメージのArm64サポートには注意が必要です。現在のところ、公式のランタイムイメージは主にAMD64アーキテクチャをサポートしており、Arm64環境での安定した接続に問題が発生する可能性が報告されています ^^。将来的なマルチアーキテクチャサポートが期待されますが ^^、現状ではArm64環境での動作に課題があることを理解しておく必要があります。**   **

   **YAML**

   ```
   version: "3.8"
   services:
     openhands-app:
       image: docker.all-hands.dev/all-hands-ai/openhands:0.45 # 最新バージョンを確認
       container_name: openhands-app
       environment:
         SANDBOX_RUNTIME_CONTAINER_IMAGE: docker.all-hands.dev/all-hands-ai/runtime:0.45-nikolaik # 最新バージョンを確認
         LOG_ALL_EVENTS: "true"
         # LLM連携のための環境変数（例：OpenAIの場合）
         # LLM_API_KEY: "your_openai_api_key"
         # LLM_BASE_URL: "https://api.openai.com/v1"
         # LLM_MODEL: "gpt-4o"
         # ローカルLLMを使用する場合の例（LM Studioなど）
         # LLM_API_KEY: "local-llm" # 任意のプレースホルダー
         # LLM_BASE_URL: "http://host.docker.internal:1234/v1" # ホストのLM Studioへのパス
         # LLM_MODEL: "lm_studio/qwen2.5-coder-14b-instruct" # LM Studioでロードしたモデル名
       ports:
         - "3000:3000" # Nginx Reverse Proxyを使用するため、外部公開は必須ではない
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock # Dockerソケットへのアクセス
         - ~/.openhands:/root/.openhands # 永続化のためのボリューム
       networks:
         - app_network

   networks:
     app_network:
       external: true # Nginx Reverse Proxyと同じネットワークを使用
   ```
4. **環境変数ファイル (`.env`) の作成:**
   LLMのAPIキーなどを設定します。
   **コード スニペット**

   ```
   # OPENHANDS_SUBDOMAIN=openhands # OpenHandsのサブドメイン (例: openhands.your_domain.com)
   # DOMAIN_NAME=your_domain.com # あなたのドメイン名
   # LLM_API_KEY=your_llm_api_key
   # LLM_BASE_URL=https://api.openai.com/v1
   # LLM_MODEL=gpt-4o
   ```
5. **デプロイ:**
   **Bash**

   ```
   docker compose up -d
   ```
6. **アクセス:**
   Nginx Reverse Proxyの設定後、`https://openhands.your_domain.com` (または設定したサブドメイン) からOpenHandsにアクセスできるようになります。初回アクセス時にLLMプロバイダーとAPIキーの設定が求められます ^^。**   **

#### Difyサーバーのデプロイ

DifyはLLMアプリケーション開発プラットフォームであり、Docker Composeでのデプロイが推奨されています ^^。**   **

1. **システム要件の確認:** Difyは最低2コアCPU、4GB RAMを必要とします ^^。Ampere A1 Flexインスタンス（4 OCPU, 24 GB RAM）はこれを満たします。DifyもLLMとの連携を前提としていますが、GPU要件はLLMモデルに依存します ^^。**   **
2. **Difyリポジトリのクローン:**
   **Bash**

   ```
   git clone https://github.com/langgenius/dify.git
   cd dify/docker
   ```
3. **環境変数ファイル (`.env`) の作成:**
   `docker`ディレクトリ内で、`.env.example`をコピーして`.env`ファイルを作成します ^^。**   **

   **Bash**

   ```
   cp.env.example.env
   ```

   `SECRET_KEY`などの重要な変数を設定します。必要に応じて、`VECTOR_STORE`（Weaviate, Milvusなど）を設定します ^^。**   **
4. **Docker Composeファイルの編集:**
   Difyは通常、`docker-compose.yaml`と`docker-compose.middleware.yaml`の2つのファイルを使用します ^^。すべてのサービスを単一の**   **

   `docker-compose.yml`に統合するか、または`docker-compose.middleware.yaml`でミドルウェアを起動し、別途DifyのAPI/Worker/Webサービスを起動する手順に従います ^^。ここでは、**   **

   `docker-compose.yaml`をベースに説明します。
   `docker-compose.yaml`を編集し、`app_network`を各サービスに追加します。
   **YAML**

   ```
   #... (既存のdocker-compose.yamlの内容)
   services:
     #...
     api:
       #...
       networks:
         - app_network
     worker:
       #...
       networks:
         - app_network
     web:
       #...
       networks:
         - app_network
     #... (db, redis, vector store services)
     db:
       #...
       networks:
         - app_network
     redis:
       #...
       networks:
         - app_network
     #... (他のミドルウェアサービスも同様にapp_networkに追加)

   networks:
     app_network:
       external: true # Nginx Reverse Proxyと同じネットワークを使用
   ```

   DifyのDockerイメージは、Arm64アーキテクチャのサポートを強化しています。`dify-plugin-daemon`などの一部のコンポーネントにはArm64イメージが提供されており ^^、マルチプラットフォームビルドのサポートも進められています ^^。ただし、大規模なビルド時間や、すべてのコンポーネントが完全にArm64に最適化されているかについては、継続的な確認が必要です ^^。**   **
5. **デプロイ:**
   `dify/docker`ディレクトリ内で実行します。
   **Bash**

   ```
   docker compose up -d
   ```
6. **アクセス:**
   Nginx Reverse Proxyの設定後、`https://dify.your_domain.com` (または設定したサブドメイン) からDifyにアクセスできるようになります。

#### Nginx Reverse Proxyの設定 (Nginx Proxy Managerの利用)

複数のDockerコンテナを単一のパブリックIPで公開するために、Nginx Proxy Manager (NPM) を使用します。

1. **NPMのDocker Composeファイル作成:**
   別のディレクトリ（例: `~/nginx-proxy-manager`）で`docker-compose.yml`を作成します。
   **YAML**

   ```
   version: '3.8'

   services:
     app:
       image: 'jc21/nginx-proxy-manager:latest'
       container_name: nginx-proxy-manager
       restart: unless-stopped
       ports:
         - '80:80'
         - '443:443'
         - '81:81' # NPM管理画面用ポート
       volumes:
         -./data:/data
         -./letsencrypt:/etc/letsencrypt
       networks:
         - app_network # 共有ネットワーク

   networks:
     app_network:
       name: app_network # 既存のネットワーク名と一致させる
       external: true
   ```
2. **NPMのデプロイ:**
   **Bash**

   ```
   cd ~/nginx-proxy-manager
   docker compose up -d
   ```
3. **NPM管理画面へのアクセス:**
   ブラウザで`http://<インスタンスのパブリックIPアドレス>:81`にアクセスします。
   初期ログイン情報: `admin@example.com` / `changeme`。ログイン後、パスワードを変更します。
4. **プロキシホストの追加:**
   NPM管理画面で「Proxy Hosts」->「Add Proxy Host」をクリックし、以下の設定を行います。

   * **n8n用:**
     * `Domain Names`: `n8n.your_domain.com` (設定したサブドメイン)
     * `Scheme`: `http`
     * `Forward Hostname / IP`: `n8n` (Docker Composeファイルで指定したn8nサービス名)
     * `Forward Port`: `5678` (n8nコンテナの内部ポート)
     * `SSL`: Let's EncryptでSSL証明書を取得・適用します。
   * **OpenHands用:**
     * `Domain Names`: `openhands.your_domain.com` (設定したサブドメイン)
     * `Scheme`: `http`
     * `Forward Hostname / IP`: `openhands-app` (Docker Composeファイルで指定したOpenHandsサービス名)
     * `Forward Port`: `3000` (OpenHandsコンテナの内部ポート)
     * `SSL`: Let's EncryptでSSL証明書を取得・適用します。
   * **Dify用:**
     * `Domain Names`: `dify.your_domain.com` (設定したサブドメイン)
     * `Scheme`: `http`
     * `Forward Hostname / IP`: `web` (Difyのwebサービス名)
     * `Forward Port`: `3000` (Dify webコンテナの内部ポート)
     * `SSL`: Let's EncryptでSSL証明書を取得・適用します。

各プロキシホストを設定したら、DNSプロバイダーで`n8n.your_domain.com`、`openhands.your_domain.com`、`dify.your_domain.com`がOCIインスタンスのパブリックIPアドレスを指すようにAレコードを設定します。

## IV. 結論と推奨事項

本レポートは、OCI Always Free Tierの制約内で、Ubuntu開発環境、n8n、OpenHands、Difyサーバーを「高スペック」かつ「継続して無料」で運用するための包括的なガイドを提供しました。Ampere A1 Flexインスタンスの4 OCPUと24 GBメモリを単一VMに割り当てる戦略は、無料枠で利用可能な最大のComputeリソースを確保し、複数のアプリケーションの要件を満たす上で最も効果的であることが示されました。

主要な推奨事項は以下の通りです。

1. **ArmベースのAmpere A1 Flexインスタンスの活用:** ユーザーの「高スペック」および「快適な動作」という要求を満たす唯一の選択肢であり、無料枠の範囲内で最大限の性能を引き出すために、4 OCPUと24 GBメモリを単一VMに割り当てる構成を強く推奨します。
2. **「Out of Host Capacity」問題への戦略的対応:** Ampere A1インスタンスのプロビジョニング時に発生しうる容量不足エラーに対しては、OCI Cloud Shellを用いた自動化スクリプトによる再試行が、効率的かつ確実な解決策となります。
3. **ストレージの最適化とバックアップ戦略:** 無料枠の200GBブロックボリュームストレージと5つのボリュームバックアップという制限を理解し、ブートボリュームサイズをデフォルトの50GBに抑えることを推奨します。重要なアプリケーションデータは、追加のブロックボリュームに分離するか、オブジェクトストレージや外部バックアップソリューションへのエクスポートを検討することで、限られたリソース内でデータ管理と災害復旧計画を最適化できます。
4. **DockerとDocker Composeによるアプリケーション統合:** 複数のアプリケーションを効率的にデプロイし、管理するための標準的な方法としてDockerとDocker Composeを導入します。これにより、環境の一貫性が保たれ、依存関係の競合が回避されます。
5. **Nginx Reverse Proxyによるサービス公開:** 単一のパブリックIPアドレスで複数のWebアプリケーションにアクセス可能にするため、Nginx Proxy Managerのようなリバースプロキシの導入が不可欠です。これにより、各サービスをサブドメイン経由で公開し、SSL証明書の一元管理も可能になります。
6. **ファイアウォール（UFW）とDockerの適切な連携:** UFWとDockerの`iptables`ルール間の競合を解消するため、`ufw-docker`スクリプトを導入し、必要なポートのみを安全に公開するように設定することが重要です。
7. **OpenHandsのArm64サポートに関する注意:** OpenHandsの公式DockerイメージのArm64サポートには現在課題が報告されており、安定した動作には追加の調査やコミュニティの進展を注視する必要があります。

本レポートで示されたステップと考慮事項を実践することで、OCI初心者でも、継続して無料で利用可能な範囲で、要求される「高スペック」なUbuntu開発環境、n8nサーバー、OpenHandsサーバー、Difyサーバーを構築し、自身のプロジェクトを成功裏に立ち上げることが可能となるでしょう。継続的な運用においては、OCIのAlways Freeティアで提供される基本的な監視とアラート機能を活用しつつ ^^、アプリケーションレベルでのログ監視やヘルスチェックを定期的に実施し、リソース使用状況を把握することが重要です。**   **
