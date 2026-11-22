# 2026-11-22 サイバーセキュリティニュースまとめ

## 主要ポイント

* Rackspace Spotにおいて漏洩認証情報を利用した不正アクセスが発生し、攻撃者によりKubernetesシークレットの窃取や不正ポッドのデプロイが実施された。
* Microsoft Entra Connect HealthのAPI脆弱性が悪用され、管理者メールアドレスやテナント設定情報などのメタデータが閲覧された。
* Android TVや低価格デバイスを標的とするBADBOXボットネットが「BADBOX 3.0」として復活し、1日あたり400億件という過去最大規模の不正広告リクエストを記録した。

## クラウド・IDインフラの侵害

クラウドホスティングやID管理基盤を標的とした重大なセキュリティインシデントが相次いで報告されています。RackspaceのマネージドKubernetes環境「Rackspace Spot」では、流出した認証情報を突かれて顧客のKubernetes SecretsやAPIトークンが読み取られる被害が発生しました。また、Microsoft Entra Connect HealthサービスではAPIの不具合を突かれ、管理者の連絡先やテナント設定などのメタデータが第三者に漏洩しました。

## ボットネット・不正広告の大規模化

廉価なAndroidデバイスを足がかりにした大規模不正広告ネットワークが勢力を拡大しています。かつてテイクダウンを受けたBADBOXボットネットは「BADBOX 3.0」へと再構築され、バックグラウンドでの動画広告再生や正規ストリーミングアプリの偽装により、コネクテッドTV（CTV）トラフィックの4%以上を占める前例のない規模のアドフラウドを引き起こしています。

## AIインフラとサーバサイド脆弱性

AI推論サービスを提供するプロバイダにおいて、Zero Data Retention（データ非保持）設定のプロンプトを含むリクエストが数か月にわたり不正取得されていた事案が発覚し、OpenRouterが提携プロバイダ3社を停止しました。さらに、PDFや画像の変換処理に広く使われるGhostscriptにおいてサンドボックスを回避してリモートコード実行（RCE）を可能にする脆弱性が確認されるなど、基盤層のセキュリティリスクが浮き彫りになっています。

---

# 2026-11-22 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. Rackspace Spot breach let hackers access customer Kubernetes secrets

クラウドコンテナ管理プラットフォーム「Rackspace Spot」において、流出した認証情報を用いた不正アクセスが発生しました。攻撃者は2026年11月17日のおよそ22時間にわたり一部顧客組織のアカウントとして振る舞い、Kubernetesクラスタ内での不正ポッドの作成、ノードやボリュームの列挙、およびKubernetes Secretsの読み取りを行いました。Secretsにはパスワード、APIキー、認証トークンが含まれており、影響を受けた顧客には各種APIトークンやクラスタシークレットの再発行およびローテーションが呼びかけられています。

[出典: BleepingComputer - Rackspace Spot breach let hackers access customer Kubernetes secrets](https://www.bleepingcomputer.com/news/security/rackspace-spot-breach-let-hackers-access-customer-kubernetes-secrets/)

### 2. Microsoft Entra Connect Health flaw exploited to steal tenant data

Microsoftは、オンプレミスID基盤の監視を行う「Microsoft Entra Connect Health」サービスのAPI脆弱性が悪用され、顧客テナントのメタデータが不正に閲覧されたことを公表しました。流出したデータには、技術担当者や管理者のメールアドレス、テナントID、ドメイン名、ディレクトリ同期ステータス、ライセンス情報、さらに過去に登録用で利用されていた失効済み証明書などが含まれます。調査の結果、設定変更等の改ざんは確認されず、読み取り専用アクセスに留まったと報告されています。

[出典: BleepingComputer - Microsoft Entra Connect Health flaw exploited to steal tenant data](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)

### 3. BADBOX botnet returns with record-breaking 40 billion daily ad requests

安価なAndroid TVボックスやAOSP搭載端末を感染源とするBADBOXマルウェアが再浮上しました。HUMANのSatoriリサーチチームによると、新たに確認された「BADBOX 3.0」は1日あたり約400億件の不正広告入札リクエストを生成しており、従来の記録保持ボットネット（VASTFLUX）の3倍以上、観測されたCTVトラフィックの4%超に達しています。感染端末はバックグラウンドの非表示ウィンドウで広告動画を再生し、正規アプリに偽装して広告詐欺を行っています。

[出典: BleepingComputer - BADBOX botnet returns with record-breaking 40 billion daily ad requests](https://www.bleepingcomputer.com/news/security/badbox-30-botnet-returns-with-record-breaking-40-billion-daily-ad-requests/)

## 深掘り

### クラウド・サプライチェーンと基盤層における権限掌握リスク

今回のニュースでは、クラスタオーケストレーション基盤、ID連携監視基盤、AI推論ホスティング基盤など、システム運用のコアとなるレイヤーへの攻撃が顕著に見られます。

#### Kubernetesにおけるシークレット侵害と水平展開

Rackspace Spotの事例では、漏洩した資格情報によって攻撃者が正当なユーザー権限を取得し、Kubernetes API経由でSecretsを読み取ることが可能となりました。Kubernetes Secretsにはデータベース接続情報や外部クラウドアカウントの認証キーが集約されているため、単一クラスタの侵入が組織全体の基幹システムや別クラウド環境への横展開（ラテラルムーブメント）につながる深刻なリスクを内包しています。

#### サードパーティ・監視サービスのAPI脆弱性と情報窃取

Microsoft Entra Connect Healthのインシデントでは、サービス側のAPI実装不具合によりテナントの管理者情報や同期状態が外部から閲覧可能な状態となっていました。管理者メールアドレスやテナント構成情報は、高度な標的型フィッシングやサプライチェーン攻撃を仕掛けるための偵察活動において極めて有用な情報となります。

### 関連知識

#### 用語解説

* **Kubernetes Secrets**: パスワード、OAuthトークン、SSHキーなどの機密情報をPodに直接ハードコードせず安全に注入・管理するためのKubernetesオブジェクト。
* **アドフラウド（Ad Fraud）**: ボットネットや不正スクリプトを用いて広告インプレッションやクリックを偽装し、広告主から不正に広告費を詐取するサイバー犯罪手法。
* **Zero Data Retention (ZDR)**: AIプロバイダなどにおいて、プライバシー保護や機密保持を目的に、送信されたプロンプトや生成結果をサーバ側に保存・ログ記録しない保証設定。

#### 今後の展望

クラウドサービスプロバイダやAIホスティング企業におけるインフラ管理・APIエンドポイントの堅牢化が急務です。利用者側においても、万一のプラットフォーム侵害を前提としたシークレットの定期ローテーション、最小特権アクセスの徹底、および外部連携APIの監視強化が求められます。また、IoT・安価なAndroid端末を踏み台にするボットネットに対しては、サプライチェーン段階でのファームウェア検証やエコシステム全体での連携遮断が不可欠です。

## 結論

クラウド基盤やID管理、AI推論などの外部マネージドサービスは利便性を提供する一方で、ひとたび認証情報やAPIの脆弱性が突かれると広範な顧客データや内部シークレットが脅威に晒されるリスクがあります。組織は自社管理外のプラットフォームにおいてもインシデントを想定したゼロトラストな鍵管理・ローテーション態勢を整備し、インフラ監視の強化を継続する必要があります。

## 主要引用

* Rackspace通知文: 「2026年11月17日（00:20〜22:00 UTC頃）、権限のない第三者が流出した認証情報を使用してRackspace Spotの一部にアクセスした」
* Microsoftセキュリティ通知: 「2026年11月20日に調査を完了し、お客様の組織に関連するテナントレベルのメタデータへの権限のない読み取り専用アクセスが発生したことを確認した」
* HUMAN（Satoriリサーチ）: 「BADBOX 3.0は最盛期に1日あたり約400億件の入札リクエストを占め、Human Defense Platformが観測した全CTVトラフィックの4%以上を占めた」
