#  2026年9月23日  サイバーセキュリティニュースまとめ

## 主要ポイント
*  **Microsoftが2026年9月の月例更新で過去最多となる973件の脆弱性を修正し、うち2件がゼロデイ攻撃として悪用済み**。
*  **北朝鮮Lazarusグループが「Operation Dream Job」においてWinSockのカーネル脆弱性（CVE-2026-68820）を悪用し、CISAが連邦機関へ修正命令**。
*  **中国系AI企業による米フロンティアモデルへの大規模モデル蒸留（蒸留攻撃）およびSalesloft/CareCloud等での非人間アイデンティティ（NHI）侵害が深刻化**。

##  脆弱性・パッチ管理とコアOSの脅威
Microsoftは2026年9月のPatch Tuesdayにおいて、単月として史上最多となる973件の脆弱性修正を公表しました。このうちWindows Updateスタック（CVE-2026-81963）およびWindowsメッセージングシステム（CVE-2026-85880）の特権昇格脆弱性2件は、既に実際のサイバー攻撃（野生）で悪用されていることがCISAにより確認されています。AIによる静的コード解析や自動ファジングの普及に伴い年間公開脆弱性数が2,600件を超過しており、発見速度に対してパッチ適用が追いつかない「パッチ疲れ」が顕著になっています。

##  国家主導型サイバー攻撃（APT）とカーネル層侵入
北朝鮮のLazarusグループは防衛・航空宇宙産業のエンジニアを標的とした求人詐欺手口「Operation Dream Job」を展開し、WinSock（afd.sys）のUse-After-Free脆弱性（CVE-2026-68820）を突いてSYSTEM権限を獲得しました。侵入後はカーネルモードルートキット「FudModule」を用いてEDR機能を無効化しています。また、ロシア系アクターによるZimbraのフィッシングやルーターインフラの奪取、さらにはウクライナ・ロシア間の相互的なDDoS攻撃やインフラ攻撃が継続しています。

##  クラウドサプライチェーン・非人間アイデンティティ（NHI）侵害
営業・AI支援企業のSalesloftでは、GitHubアカウントの不正アクセスを通じてDriftのAWS環境に保持されていたOAuthトークンやAPIキーが強奪され、CloudflareやZscalerを含む700以上の組織へ影響が波及しました。また、電子電子カルテ（EHR）のCareCloudではAWS環境の不備により375万人以上の医療・個人情報が漏洩しました。MFAが導入される人間のアカウントではなく、APIトークンやサービスアカウントといった「非人間アイデンティティ（NHI）」の管理不備がサプライチェーン攻撃の最大の死角となっています。

---

#  2026年9月23日  サイバーセキュリティニュース詳細

## ニュース紹介

### 1.  Microsoft、2026年9月Patch Tuesdayで973件の脆弱性を修正（2件のゼロデイ悪用）
Microsoftは2026年9月8日、史上最大規模となる973件のセキュリティ脆弱性を修正する月例パッチを公開しました。
* **発生した事象と影響**：CISAは、Windows Updateスタックの脆弱性（CVE-2026-81963）とWindows Messaging Systemの脆弱性（CVE-2026-85880）の2件が野外でアクティブに悪用されていることを確認しました。これらはフィッシング等で初期侵入を果たした攻撃者が権限昇格を行い、セキュリティソフトによる追放を免れて端末を完全制御する手口に悪用されています。CISAは米連邦機関に対し9月22日までの適用を指示しました。
$$出典: The Record from Recorded Future News - Microsoft posts nearly 1,000 bugs for Patch Tuesday as CISA warns two being exploited$$ (https://therecord.media/microsoft-patch-tuesday-september-2026)

### 2.  北朝鮮Lazarusグループ、「Operation Dream Job」でWinSockゼロデイ（CVE-2026-68820）を悪用
北朝鮮の偵察総局傘下のLazarusグループが、防衛・宇宙航空・監視機器関連企業の人材を狙った「Operation Dream Job」キャンペーンにおいて新種のゼロデイ脆弱性を悪用していることが判明しました。
* **発生した事象と影響**：攻撃者はLinkedIn等でLockheed Martinなどの採用担当者になりすまして偽の求人PDFを送付し、バックドアを導入した上でWinSock（afd.sys）のRace Condition脆弱性（CVE-2026-68820）を実行します。これによりSYSTEM権限を獲得し、ルートキット「FudModule」をデプロイしてEDRを無効化・カーネルメモリを改ざんします。
$$出典: The Record from Recorded Future News - CISA gives federal agencies two weeks to patch Microsoft bug exploited in DPRK campaign$$ (https://therecord.media/cisa-gives-federal-agencies-two-weeks-to-patch-dprk-microsoft-bug)

### 3.  Salesloft Drift不正アクセスによりOAuthトークン流出、700超の顧客組織に波及
AI・営業支援プラットフォームを提供するSalesloftは、同社のGitHubアカウントが第三者に不正アクセスされ、買収したDriftのAWS環境から顧客連携用のOAuthトークンや認証情報が窃取されたと発表しました。
* **発生した事象と影響**：攻撃者は3月〜6月にかけて潜伏し、Driftと連携するSalesforce等の顧客データ領域の偵察を実施しました。Cloudflare、Zscaler、Palo Alto Networks、Nutanix、Elasticなど700以上の企業が影響を受け、サポートチケットや連絡先、認証情報の漏洩対応を余儀なくされました。
$$出典: The Record from Recorded Future News - Salesloft: Hacker broke into systems in March through GitHub account$$ (https://therecord.media/salesloft-hacker-broke-into-github)

## 深掘り

###  フロンティアAIモデルに対する大規模「モデル蒸留（Distillation）攻撃」とAI脅威の進化

####  中国系AI事業者による米国フロンティアモデルの能力強奪（CISA Advisory AA26-251A）
CISAが公開した合同注意報AA26-251Aによると、StepFun、Z.AI、MiniMaxといった中国を拠点とするAI商業事業者が、米国の最先端フロンティアAIモデル（Claude Opus 4.1/4.5/4.8、Claude Sonnet 4.5、GPT-5シリーズ等）に対して産業規模の「モデル蒸留（Distillation）キャンペーン」を展開していたことが判明しました。
これらの事業者は、自動化されたAPIクエリ、プロンプトインジェクションによる安全ガードレールの迂回、および自律エージェントの対話機能を悪用し、高度なコーディング能力や思考プロセス（Chain-of-Thought reasoning）を体系的に抽出・取得しました。強奪された推論能力や知識ロジックは、Step 4などの中国国産AIモデルへ転送・複製されています。

####  AIツールによる脆弱性発見の自動化と攻撃スピードの極限化
2026年の脅威情勢において、AIアシスタントや高度なコード監査ツールの普及は防御側の脆弱性発見率を劇的に向上させた一方で、攻撃側によるエクスプロイトコード作成や未知の欠陥探査もミリ秒単位で自動化させました。
公開された脆弱性に対して修正パッチを検証・配信するスピードよりも、攻撃者が自動スキャンおよびゼロデイ/Nデイ攻撃を構築して実行するタイムラインの方が短縮されており、境界型防御や従来の脆弱性管理の仕組みが限界を迎えていることを示しています。

###  関連知識

####  用語解説
*  **非人間アイデンティティ（Non-Human Identities: NHIs）**：APIキー、OAuthトークン、サービスアカウント、CI/CDアクセスキーなど、人間を介さずシステム間やクラウド間でデータ連携を行うための認証情報。MFAが適用されにくく、暗号化・定期ローテーションが行われない場合に長期潜入の侵入口となる。
*  **FudModule**：Lazarusグループが使用するカーネルモードの高度なルートキット。OSの最も深いカーネル層で動作し、EDR（Endpoint Detection and Response）セキュリティエージェントのプロセスを直接停止・隠蔽する。

####  今後の展望
*  **ブラウザ・ネイティブ防衛（BDR）とゼロトラストNHIガバナンスの必須化**：
    SaaSおよびWebブラウザ内での業務・AI利用が一般化する中、ネットワーク境界だけでなく、 encrypted ブラウザセッション内部のデータ移動を動的監視する「Browser Detection and Response (BDR)」の導入が進みます。また、APIキーやトークンの自動インベントリ・短期間ローテーションを義務付ける「NHIガバナンス」の導入が急務となります。

## 結論
2026年9月時点のサイバー空間は、月間900件超という前例のないペースでの脆弱性公開、カーネル層を狙うゼロデイ攻撃、さらにはAPIトークン（NHI）侵害を通じた広範なサードパーティサプライチェーン破綻 が同時進行する極めて過酷な環境となっています。
組織は「侵害されることを前提（Assume Breach）」とし、ネットワークから切り離された物理的・不変（Immutable）バックアップの保持、カーネル保護機能を備えたEDRの運用、および外部連携APIトークンの徹底的な権限最小化・自動ローテーションを即座に実行する必要があります。

## 主要引用
*  **“An attacker who owns the update stack owns the thing you'd use to evict them.”** — Serena DiPenti（Automox エンジニア、CVE-2026-81963 に関するコメント）
*  **“This incident highlights a significant systemic blind spot in how organizations manage 'Non-Human Identities' like API tokens, which are used for communication between platforms.”** — Rom Carmel（Apono CEO、Salesloft/Drift侵害事件に関するコメント）
*  **“China-based artificial intelligence commercial entities... conducted industrial-scale model distillation campaigns targeting leading U.S. frontier AI models.”** — 米CISA（合同セキュリティ勧告 AA26-251A より）
