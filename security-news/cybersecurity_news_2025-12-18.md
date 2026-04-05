# 2025年12月18日 サイバーセキュリティニュースまとめ

## 主要ポイント
*   **SonicWall SMA 1000**および**Cisco AsyncOS**において、中国系APTやサイバー犯罪者によって活発に悪用されるクリティカルなゼロデイ脆弱性が連鎖的に発見され、ネットワーク境界防御機器が危機に瀕している,,。
*   ESET Researchは、Windowsの**Group Policyを悪用**して日本を含む政府機関を長期的に監視する、新たな中国関連APTグループ**「LongNosedGoblin」**を発見した,,,。
*   アスクル株式会社は、ランサムウェア攻撃による**74万件超のデータ流出**を確定し、初期侵入が**MFA未適用の業務委託先アカウント**経由であったこと、バックアップの暗号化が復旧遅延の主因であったことを明らかにした,,,。

## ゼロデイ攻撃とネットワーク境界の危機
リモートアクセスアプライアンスを提供するSonicWallは、SMA 1000製品に存在するゼロデイ脆弱性（CVE-2025-40602）が actively exploited（活発に悪用されている）と警告した,。この欠陥は、認証済みユーザーの権限昇格を可能にするものであり、今年初めにパッチが適用された別の脆弱性（CVE-2025-23006）と連鎖させることで、**認証不要でルート権限によるリモートコード実行（RCE）**が可能になるという特に悪質な組み合わせとなっている,,,。
また、Ciscoは、Secure Email GatewayおよびSecure Email and Web ManagerアプライアンスのAsyncOSソフトウェアに、**CVSSスコア10.0**のクリティカルなゼロデイ脆弱性（CVE-2025-20393）が悪用されていると警告した,。攻撃は、**中国関連のAPTアクター（UAT-9686）**によるもので、脆弱性が悪用されると、基盤となるOS上でルート権限で任意のコマンドが実行される危険性がある,,。CISAは両社の脆弱性を既知の悪用済み脆弱性（KEV）カタログに追加し、緊急の対処を義務付けている,。さらに、Apple製品（iOS、macOSなど）のWebKitにも、Google Chromeと同一のWebKit関連のゼロデイ脆弱性（CVE-2025-14174）が修正された,,。

## 国家APTとサイバースパイ技術の高度化
ESET Researchは、東南アジアおよび**日本**の政府機関を標的とする、これまで文書化されていなかった中国関連のAPTグループ**「LongNosedGoblin」**を発見した,。このグループは、Windows環境で設定管理に使用される**Group Policy（グループポリシー）を悪用**し、マルウェアを大規模に展開し、目立たない横移動を行う,。C&C通信には、Microsoft OneDriveやGoogle Driveなどの**クラウドサービス**を利用しており、正規のトラフィックに悪意ある通信を紛れ込ませる手法を採用している,。同グループは、ブラウザ履歴を収集するNosyHistorianや、ファイル窃取・シェル実行を行うNosyDoorバックドアなど、長期的な監視とデータ窃取に特化したツールセットを使用している,,,。

## 国内大規模データ侵害と犯罪インフラのテイクダウン
アスクル株式会社は、2025年10月19日に検出されたランサムウェア攻撃（RansomHouseによる）に関する調査結果を公表し、約2カ月間の復旧作業を経て、12月17日に法人向け物流システム（一部）の出荷業務を再開した,。同社は、攻撃によりビジネス顧客や個人顧客を含む**74万件超のレコードが流出**したことを確定した,,。
詳細分析の結果、攻撃者は、**多要素認証（MFA）が適用されていなかった業務委託先アカウント**の認証情報を窃取し、初期侵入に成功していたことが判明した,。攻撃者はネットワークに潜伏した後、セキュリティシステムを無効化し、**バックアップファイルを含むシステムデータを暗号化**したため、復旧が大幅に遅延した,。
一方、サイバー犯罪対策の分野では、米司法省（DOJ）が国際的な協力のもと、ランサムウェア収益など**7,000万ドル以上**の不正資金洗浄に関与したとされる仮想通貨取引所「E-Note」のインフラを解体し、ロシア国籍の運営者を起訴した,,。

---

# 2025年12月18日 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. SonicWall SMA 1000にゼロデイ脆弱性、認証不要RCEにつながる連鎖攻撃を確認
SonicWall Secure Mobile Access (SMA) 1000リモートアクセスアプライアンスの管理コンソールに、権限昇格を許すゼロデイ脆弱性（CVE-2025-40602）が発見され、活発に悪用されている,。この脆弱性は、今年初めに修正された別の脆弱性（CVE-2025-23006）と連鎖させることで、**認証なしでルート権限によるRCE**を可能にする「特に悪質な組み合わせ」として武器化されている,。SonicWallは、直ちにホットフィックスバージョンへのアップデートを行うことと、アプライアンス管理コンソール（AMC）へのアクセスを信頼できるネットワークに限定する緩和策を推奨している,。
[出典: Another bad week for SonicWall as SMA 1000 zero-day under active exploit, Exploitation of CVE-2025-40602 chained with CVE-2025-23006 | Tenable®,,]

### 2. Cisco AsyncOSのCVSS 10.0ゼロデイが中国系APTに悪用される
Ciscoは、Secure Email GatewayおよびSecure Email and Web ManagerアプライアンスのAsyncOSソフトウェアに、クリティカルなゼロデイ脆弱性（CVE-2025-20393, CVSS 10.0）が悪用されていると警告した,。この脆弱性は不適切な入力検証に起因し、攻撃者は基盤となるOS上でルート権限での任意コマンド実行が可能となる,。Cisco Talosは、攻撃を**中国関連のAPTアクター「UAT-9686」**によるものとみており、AquaShell、AquaPurge、AquaTunnelといったカスタムバックドアやトンネリングツールを使用して、長期間にわたりアクセスを維持しようとしている,,。
[出典: China-Linked Hackers Exploiting Zero-Day in Cisco Security Gear - SecurityWeek, Cisco Warns of Active Attacks Exploiting Unpatched 0-Day in AsyncOS Email Security Appliances,,]

### 3. 中国APT「LongNosedGoblin」がGroup Policyを悪用し日本を含む政府機関を標的に
ESET Researchは、東南アジアおよび日本の政府機関を標的とする、新たな中国関連APTグループ「LongNosedGoblin」を発見した,。このグループは、Windows環境で広く使用される**Group Policy（グループポリシー）を悪用**してマルウェアを大規模に展開し、ネットワーク内を横移動する,。これは、通常の管理トラフィックに紛れ込むことで、従来の検出技術を回避する,。同グループのツールセットには、ブラウザ履歴や認証情報を窃取するNosyHistorianやNosyStealer、およびオーディオ/ビデオ録画ツールが含まれ、長期的なサイバースパイ活動を目的としている,。
[出典: Group Policy abuse reveals China-aligned espionage group targeting governments - Help Net Security, New Chinese group LongNosedGoblin deploys cyberespionage,,]

## 深掘り
### ネットワーク境界機器の危機とMFA欠如の決定的な影響
SonicWallやCiscoといったネットワーク境界防御機器が、国家APTの主要な標的となり、認証不要RCEにつながるゼロデイ脆弱性の連鎖的な悪用が常態化している,。これらの機器が侵害されると、攻撃者は内部ネットワークへの支配権を確立する。

#### サブトピック1: ゼロデイ連鎖攻撃によるRCEの簡素化
SonicWall SMA 1000の連鎖攻撃（CVE-2025-40602 + CVE-2025-23006）は、攻撃者が複数の脆弱性を組み合わせることで、**認証済みユーザーを装う必要すらなく（unauthenticated）**、リモートから最高権限（root privileges）でシステムを完全に掌握できることを示している,。CiscoのAsyncOSゼロデイも同様にルート権限を標的としており、リモートアクセスやゲートウェイ機器のセキュリティが、組織のセキュリティ姿勢全体の決定的な弱点となっていることが強調される,。

#### サブトピック2: アスクル事例から学ぶMFAとバックアップの構造的欠陥
アスクルの大規模データ侵害（74万件超の流出）は、初期侵入が**多要素認証（MFA）を例外的に適用していなかった業務委託先アカウント**の認証情報漏洩によるものであったことから、サプライチェーンにおけるID/アクセス管理の脆弱性が決定的な破綻を招いた教訓となる,。さらに、攻撃者がバックアップファイルを削除し、オンラインバックアップも暗号化したという事実は、**ランサムウェア攻撃を想定したAir Gap（ネットワーク隔離）**など、強固なバックアップ体制の欠如が、復旧の長期化を招く構造的な欠陥であったことを示唆している,,。

### 関連知識

#### 用語解説
*   **CVE-2025-40602/CVE-2025-23006:** SonicWall SMA 1000の脆弱性。特権昇格と信頼できないデータのデシリアライゼーションを連鎖させ、認証不要RCEを可能にする,。
*   **UAT-9686:** Cisco AsyncOSのゼロデイ（CVE-2025-20393）を悪用している中国関連のAPTアクター。AquaShellやAquaTunnelなどのカスタムツールを使用し、ルート権限でのコマンド実行を狙う,,。
*   **Group Policy Abuse:** LongNosedGoblinが用いる手法。Active Directoryの管理ツールであるGroup Policyを利用して、正規の管理トラフィックに紛れ込ませながらマルウェアをドメイン全体に展開する,。

#### 今後の展望
ネットワーク境界防御機器に対するゼロデイの常態化は、パッチ適用までの間にWAFによる仮想パッチ適用や、アプライアンス管理コンソール（AMC）へのアクセス制限など、**即時的な緩和策**が必須となる,。また、アスクルの事例が示すように、サプライチェーン全体でのMFAの強制適用と、攻撃者によるバックアップ破壊に耐えうる**イミュータブル（不変）なバックアップ体制**の確立が、事業継続計画（BCP）の核となる,,。

## 結論
2025年12月18日現在のサイバー脅威環境は、中国国家APTやサイバー犯罪者によるネットワーク境界機器のゼロデイ攻撃（Cisco, SonicWall）の活発化、および国内企業におけるMFA欠如（アスクル）を起点とした大規模侵害の長期化という、二重の緊急課題に直面している,。組織は、SonicWallやCiscoの緊急パッチ適用を最優先事項としつつ、アスクルの教訓に基づき、**多要素認証の例外なき徹底**と、攻撃者による破壊に耐えうる**隔離されたバックアップ体制の再構築**へ、経営資源を集中投下する必要がある,,。

## 主要引用
*   「The bug, tracked as CVE-2025-40602... has been chained with another SMA 1000 flaw patched earlier this year (CVE-2025-23006) to enable **unauthenticated remote code execution with root rights** – a particularly nasty combo when weaponized in the wild.」
*   「The vulnerability, tracked as CVE-2025-20393 and classified as having critical severity, impacts appliances running Cisco AsyncOS software... **The exploitation of CVE-2025-20393 was discovered by Cisco’s own Talos security experts.**,」
*   「Askul’s investigation concluded that attackers likely gained initial access using stolen authentication credentials tied to an **outsourced partner’s administrative account that lacked multi-factor authentication.**」
*   「The group, tracked as LongNosedGoblin, has targeted government institutions in Southeast Asia and **Japan** with a toolset built for long-term surveillance.」
*   「Askul Restarts Logistics as Ransomware Attack Exposes **740,000 Records**」
