# 2026年11月23日 サイバーセキュリティニュースまとめ

## 主要ポイント

* CISAが悪用が確認されたProject MONAIおよびN-able Mail Assureの脆弱性をKEVカタログに追加し、連邦機関に迅速な対応を要求。
* Cisco Expresswayに存在する深刻なリモートコード実行（RCE）の脆弱性が悪用対象としてCISAに指定され、連邦機関に3日以内の対処が命じられる。
* ペルーを拠点に米国在住のヒスパニック系住民3万人以上から1,500万ドルを騙し取った詐欺グループのコールセンター運営者に対し禁錮8年の判決。

## 脆弱性・セキュリティアラート

CISAは、現在進行形で悪用が確認された脆弱性として、Project MONAIのパストラバーサル（CVE-2026-133968）およびN-able Mail AssureのSSRF（CVE-2026-134624）をKEVカタログに追加しました。また、Cisco Expresswayのクラスター環境においてroot権限で任意コードが実行される脆弱性（CVE-2026-76466）についても悪用が警告され、緊急パッチ適用が呼びかけられています。

## サイバー犯罪・法執行

米国司法省および裁判所は、米国の政府高官や弁護士になりすまし、3万人以上のスペイン語話者から計1,500万ドルを脅し取った国際詐欺・恐喝スキームに関与したペルー人コールセンター運営者に対し、禁錮8年の実刑判決を下しました。

## システム・パッチ影響

Microsoftは、Windows 11の2026年11月ホットパッチ（KB5132043）適用後にForcepoint DLP Endpoint Agentとの競合により印刷機能（Print Spooler）が停止する不具合を公表しました。併せて、Bluetooth LE Audioにおいてマイク使用時に発生していた音声品質低下の修正テストを進めています。

---

# 2026年11月23日 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. CISAがMONAIおよびN-ableの脆弱性を悪用確認済みカタログに追加

米サイバーセキュリティ・インフラセキュリティ庁（CISA）は、実際に悪用が確認されたとして2件の脆弱性を「悪用が確認された脆弱性（KEV）カタログ」に追加しました。対象は、Project MONAIの「MONAI Label」におけるパストラバーサルの脆弱性（CVE-2026-133968）と、N-able Mail Assure（旧SpamExperts）におけるサーバーサイド・リクエスト・フォージェリ（SSRF）の脆弱性（CVE-2026-134624）です。これらは攻撃者による足がかりや不正アクセスの頻出経路となっており、拘束的運用指令（BOD 26-04）に基づき連邦文民行政府（FCEB）機関へ迅速な対応が求められています。

[出典: CISA - CISA Adds Two Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog)

### 2. Cisco Expresswayの重大なRCE脆弱性が悪用中とCISAが警告

CISAは、Cisco Expresswayシリーズのエンタープライズコラボレーションゲートウェイに存在する深刻な脆弱性（CVE-2026-76466）が野生環境（in the wild）で悪用されているとして警告を発しました。本脆弱性は、ハードコードされた認証情報の使用やクライアント証明書の検証不備に起因し、認証されていない遠隔の攻撃者がroot権限で任意のOSコマンドを実行できるものです。シスコ側のPSIRTは悪用を公に確認していなかったものの、CISAが能動的な攻撃を検知しKEVカタログに追加、連邦機関に対して3日以内の是正措置を義務付けました。

[出典: BleepingComputer - CISA flags critical Cisco RCE flaw as actively exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-flags-critical-cisco-expressway-rce-flaw-as-actively-exploited/)

### 3. 米国人3万人を標的にした詐欺コールセンター運営者に禁錮8年の判決

ペルー・リマ在住のCarla Magaly Alcedo Mendoza（45歳）は、米国在住のスペイン語を話す住民3万人以上から1,500万ドル（約23億円相当）以上を騙し取った政府機関なりすまし詐欺・恐喝スキームにおいて、郵便・電信詐欺の共謀罪で禁錮8年の判決を受けました。2013年から2018年にかけて運営されたコールセンターでは、当初は無料サービスの案内を装い、その後は政府関係者や弁護士を名乗って「逮捕や法的措置、移民資格の剥奪」などをチラつかせて被害者を脅迫し、巨額の現金を支払わせていました。

[出典: BleepingComputer - Call center operator gets 8 years for helping scam 30,000 Americans](https://www.bleepingcomputer.com/news/security/call-center-operator-gets-8-years-for-helping-scam-30-000-americans/)

## 深掘り

### 境界ゲートウェイと公開資産を狙うエクスプロイトの脅威

エンタープライズネットワークの境界に位置するアプライアンスやコラボレーション機器は、外部からのアクセスを受け付ける特性上、認証不備やコマンド実行の脆弱性が発見された際の危険度が極めて高くなります。

#### ハードコードされた認証情報と証明書検証の脆弱性（CVE-2026-76466）

Cisco Expresswayの脆弱性では、クラスタリング構成における内部通信やRPCコマンドの処理において、ハードコードされた認証情報および不完全なクライアント証明書検証が存在していました。攻撃者はクッキー情報を取得・偽造してデータベースサービスに接続し、リモートプロシージャコール（RPC）を呼び出すことで、認証を経ることなくroot権限でのOSコマンド実行に至ります。ゲートウェイ機器が侵害された場合、社内ネットワーク全体への侵入拡大の足がかりとなるリスクがあります。

#### BOD 26-04による優先順位付けと是正の短期化

米国の拘束的運用指令「BOD 26-04」は、公開資産かつ悪用後に完全な制御権を奪われる高リスクなCVEに対して迅速な是正を義務付けています。今回のCisco脆弱性のように「3日以内」といった極めて短い期限が設定されるケースでは、管理者はパッチ適用に加えて「パッチ適用前に侵害されていなかったか」のフォレンジック調査を実施することが求められます。

### 関連知識

脆弱性管理体制の強化と、運用管理における周辺ソフトウェア（セキュリティエージェントやホットパッチ）との整合性管理についての技術的背景です。

#### 用語解説

* **KEV Catalog（Known Exploited Vulnerabilities Catalog）**: CISAが管理する、実際に攻撃者による悪用が確認された脆弱性の公的データベース。
* **BOD 26-04**: 米国連邦文民行政府（FCEB）機関を対象に、リスクベースで脆弱性修復の優先度を定義した拘束的運用指令。
* **Windows ホットパッチ（Hotpatch）**: 再起動を伴わずにインメモリでプロセスコードを更新する更新プログラム。Windows Autopatch等を通じて配布されるが、セキュリティ製品のエンドポイントエージェントと競合を起こすケースがある。

#### 今後の展望

CISAによるKEVの即時更新に見られるように、ベンダーがPoCや攻撃を公認する前であっても、公的機関が実被害をトリガーに緊急指定を行う動きが常態化しています。組織は単にCVSSスコアに依存するだけでなく、KEVカタログ等の脅威インテリジェンスを取り入れたリスクベースの優先順位付けと、迅速なパッチ適用プロセスの自動化・検証環境の整備を進める必要があります。

## 結論

外部境界を守るネットワーク機器やコラボレーション製品、Web連携機能を持つソフトウェアの脆弱性は、依然として標的型攻撃および無差別スキャンの主たる侵入経路です。公的機関の勧告を迅速に監視し、重要インフラおよびエンタープライズ管理者は、外部公開資産の把握と短期間でのパッチ適用体制を再点検することが不可欠です。同時に、ソーシャルエンジニアリングや恐怖心につけ込む恐喝詐欺などの人的リスクに対しても、法執行機関との連携や継続的な警戒が必要です。

## 主要引用

* CISA: 「These types of vulnerabilities are a frequent attack vector for malicious cyber actors and pose significant risks to the federal enterprise.（これらの種類の脆弱性は悪意あるサイバー攻撃者の頻出攻撃ベクトルであり、連邦組織に重大なリスクをもたらす）」
* Yara Lorenzo Klukas 米連邦検事代行: 「These criminals preyed on hardworking Americans, using fear and intimidation to steal millions of dollars. They deliberately targeted Spanish-speaking communities...（これらの犯罪者は恐怖と脅迫を用いて勤勉な米国人を食い物にし、数百万ドルを奪った。彼らは意図的にスペイン語圏コミュニティを標的にした）」
* Cisco: 「An attacker with possession of the cookies could exploit this vulnerability by connecting to the database service and invoking specific remote procedure call (RPC) commands,（クッキーを所持する攻撃者は、データベースサービスに接続し特定のRPCコマンドを呼び出すことで、この脆弱性を悪用できる）」
