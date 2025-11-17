# 2025/06/11 サイバーセキュリティニュース

## 主要ポイント
- **Microsoftのゼロデイ脆弱性修正**: 2025年6月のPatch Tuesdayで、悪用されたゼロデイ脆弱性を含む66件の脆弱性が修正された。
- **損保ジャパンの大規模データ漏洩の可能性**: 4月のサイバー攻撃により、最大約1,748万件の個人情報が漏洩した可能性がある。
- **日本初の取引先セキュリティ評価サービス**: 新サービス「Assured企業評価」が取引先経由のサイバー被害防止を目指して開始された。

## ニュース紹介

### 1. Microsoft、66件の脆弱性を修正、ゼロデイ脆弱性CVE-2025-33053を含む
2025年6月11日、Microsoftは66件の新たな脆弱性を修正し、その中に野放しで悪用されたゼロデイ脆弱性CVE-2025-33053が含まれている。この脆弱性は、WebDAVを利用した遠隔コード実行を可能にするもので、Stealth Falconと呼ばれる攻撃者グループによってトルコの防衛組織を標的に悪用された。フィッシングメールを通じて偽装されたファイルが使用され、悪意のあるコードが実行された。この修正は、WindowsおよびWindows Serverの最新バージョンと一部のレガシーシステムに適用される。

[出典: [Help Net Security - Microsoft fixes zero-day exploited for cyber espionage](https://www.helpnetsecurity.com/2025/06/11/microsoft-fixes-zero-day-exploited-for-cyber-espionage-cve-2025-33053/)] 

### 2. 損保ジャパン、サイバー攻撃により最大約1,748万件の情報漏洩の可能性
2025年6月11日、損害保険ジャパン株式会社は、4月17日から21日にかけての不正アクセスにより、最大約1,748万件の顧客および代理店関連データが漏洩した可能性があると発表した。影響を受けたデータには、氏名、連絡先、保険証券番号などが含まれるが、マイナンバーやクレジットカード情報は含まれていない。現在、実際の漏洩や悪用は確認されていないが、警察への相談やシステムの強化が行われている。

[出典: [損保ジャパン公式発表](https://www.sompo-japan.co.jp/announce/2025/202504_01/)] 

### 3. 日本初の新サービス「Assured企業評価」提供開始、取引先経由のサイバー被害を防止
2025年6月11日、Visionalグループのアシュアードは、取引先経由のサイバー被害を防ぐ日本初のサービス「Assured企業評価」を開始した。このサービスは、取引先のセキュリティ対策をISO27001やNIST SP800-171などの基準に基づいて評価し、サプライチェーン攻撃のリスクを軽減する。セキュリティ専門家による評価とデータベース化された情報により、企業は取引先のセキュリティ状況を迅速かつ正確に把握できる。

[出典: [PR Times - 取引先経由のサイバー被害を未然に防ぐ日本初の新サービス](https://prtimes.jp/main/html/rd/p/000000714.000034075.html)] 

### 4. 日本を標的にしたメール攻撃が世界の84％に急増
2025年6月11日、米Proofpointの報告によると、サイバー攻撃を目的としたメールが世界的に増加し、特に日本を標的とした攻撃が全体の84％を占めるまでに急増した。2025年5月には新種の攻撃メールが約7億7000万通に達し、過去最大を記録した。この状況は、フィッシングやマルウェア配布のリスクが高まっていることを示している。

[出典: [日経XTECH - 日本を標的にしたメール攻撃の割合が世界の84％に急増](https://xtech.nikkei.com/atcl/nxt/news/24/02597/)] 

### 5. 世界的なセキュリティカメラの露出急増
2025年6月11日、Bitsightの調査により、製造業や医療分野で露出した無防備なセキュリティカメラが世界的に急増していることが明らかになった。これらのデバイスは、適切なセキュリティ設定が施されていない場合、サイバー攻撃の入り口となる可能性がある。特に、IoTデバイスの管理不足が問題となっている。

[出典: [Industrial Cyber - Bitsight reveals global surge in exposed security cameras](https://industrialcyber.co/threats-attacks/bitsight-reveals-global-surge-in-exposed-unsecured-security-cameras-in-manufacturing-healthcare/)] 

## 深掘り

### Microsoftのゼロデイ脆弱性CVE-2025-33053

#### WebDAVとは
WebDAV（Web Distributed Authoring and Versioning）は、HTTPプロトコルを拡張した技術で、ファイルの共同編集やバージョン管理を可能にする。リモートサーバー上のファイルをローカルファイルのように操作できるが、2023年に非推奨となり、デフォルトでは無効化されている。

#### 脆弱性の概要
CVE-2025-33053は、WebDAVを悪用した遠隔コード実行（RCE）脆弱性である。攻撃者は、.urlファイルを通じて作業ディレクトリを自身のWebDAVサーバーに設定し、Windowsの正規プロセス（例：iediagcmd.exe）が悪意のあるファイルを実行するよう仕向ける。この手法は、システムのファイル検索順序を悪用し、検知を回避する。

#### 悪用の手口
攻撃は、フィッシングメールに偽装された.urlファイル（例：PDFに見せかけたファイル）から始まる。このファイルは、作業ディレクトリを攻撃者のWebDAVサーバーに設定し、iediagcmd.exeを起動。iediagcmd.exeはroute.exeなどのプロセスを呼び出すが、作業ディレクトリがWebDAVサーバーにあるため、悪意のあるroute.exe（Horus Loader）が実行される。Horus LoaderはさらにHorus Agentを展開し、C2（コマンド＆コントロール）サーバーと通信してスパイ活動を行う。

#### 影響と対策
この脆弱性は、2025年6月のPatch Tuesdayで修正された。ユーザーは速やかにWindows Updateを適用し、WebDAVを無効化することが推奨される。また、フィッシングメールに対する警戒と、セキュリティ意識の向上が重要である。

[出典: [Check Point Research - Stealth Falcon Zero-Day](https://research.checkpoint.com/2025/stealth-falcon-zero-day/)] 

### サプライチェーン攻撃とその対策

#### サプライチェーン攻撃とは
サプライチェーン攻撃は、取引先やパートナー企業を介して主要な組織を攻撃する手法である。セキュリティが脆弱な取引先を踏み台として、マルウェアの配布やデータ窃取が行われる。近年、この種の攻撃が増加しており、73％の企業が取引先のセキュリティに懸念を抱いていると報告されている。

#### 代表的な事例
- **SolarWinds事件（2020年）**: ソフトウェア更新を通じてマルウェアが配布され、複数の政府機関や企業が被害を受けた。
- **NotPetya（2017年）**: ウクライナの会計ソフトウェアを介してマルウェアが拡散し、世界的な被害を引き起こした。

#### 対策
- **取引先のセキュリティ評価**: 「Assured企業評価」のようなサービスを活用し、取引先のセキュリティ対策を定期的に評価する。
- **ゼロトラストアーキテクチャ**: 内部ネットワークでもすべてのアクセスを検証し、信頼を前提としない。
- **セキュリティ教育**: 従業員や取引先に対するフィッシング対策やセキュリティ意識の向上を図る。

[出典: [Assured企業評価サービス](https://assured.jp/tp?utm_source=servise_site&utm_medium=social&utm_campaign=other&utm_content=250611)] 

## 結論
2025年6月11日のサイバーセキュリティニュースは、ゼロデイ脆弱性の悪用、大規模なデータ漏洩の可能性、そしてサプライチェーン攻撃への新たな対策という、現代のサイバー脅威の多様性を示している。Microsoftの迅速なパッチ適用や、損保ジャパンの対応強化、アシュアードの新サービスは、サイバーセキュリティの重要性を強調する。企業は、最新のセキュリティ更新、取引先の評価、従業員教育を通じて、進化する脅威に対抗する必要がある。

## 主要引用
- 「Microsoftは、2025年6月のPatch Tuesdayで66件の脆弱性を修正し、ゼロデイ脆弱性CVE-2025-33053を封じた。」([Help Net Security](https://www.helpnetsecurity.com/2025/06/11/microsoft-fixes-zero-day-exploited-for-cyber-espionage-cve-2025-33053/)) 
- 「損保ジャパンは、4月の不正アクセスにより最大約1,748万件のデータ漏洩の可能性を報告。」([損保ジャパン公式発表](https://www.sompo-japan.co.jp/announce/2025/202504_01/)) 
- 「アシュアードの新サービスは、取引先のセキュリティ評価を通じてサプライチェーン攻撃を防止。」([PR Times](https://prtimes.jp/main/html/rd/p/000000714.000034075.html)) 

## Key Citations
- [Microsoft fixes zero-day exploited for cyber espionage](https://www.helpnetsecurity.com/2025/06/11/microsoft-fixes-zero-day-exploited-for-cyber-espionage-cve-2025-33053/)
- [損保ジャパン公式発表 - 4月の不正アクセスによる情報漏洩の可能性](https://www.sompo-japan.co.jp/announce/2025/202504_01/)
- [PR Times - 取引先経由のサイバー被害を未然に防ぐ日本初の新サービス](https://prtimes.jp/main/html/rd/p/000000714.000034075.html)
- [日経XTECH - 日本を標的にしたメール攻撃の割合が世界の84％に急増](https://xtech.nikkei.com/atcl/nxt/news/24/02597/)
- [Industrial Cyber - Bitsight reveals global surge in exposed security cameras](https://industrialcyber.co/threats-attacks/bitsight-reveals-global-surge-in-exposed-unsecured-security-cameras-in-manufacturing-healthcare/)
- [Check Point Research - Stealth Falcon Zero-Day](https://research.checkpoint.com/2025/stealth-falcon-zero-day/)
- [Assured企業評価サービス - サプライチェーン攻撃防止](https://assured.jp/tp?utm_source=servise_site&utm_medium=social&utm_campaign=other&utm_content=250611)