# 2026年3月25日 サイバーセキュリティニュースまとめ

## 主要ポイント

* **ソフトウェアサプライチェーンへの組織的波及攻撃:** 脅威アクター「TeamPCP」がLiteLLM、Trivy、KICSなどの主要な開発・セキュリティツールを侵害し、1,000以上の企業SaaS環境に影響を及ぼす大規模なサプライチェーン攻撃を展開しています。
* **重要インフラ管理プラットフォームを狙うゼロデイ悪用:** インフラ管理の核心であるCisco Secure FMCの脆弱性（CVE-2026-20131）が、公表の36日前からInterlockランサムウェアグループによってゼロデイ攻撃として悪用されていたことが判明しました。
* **「マルウェアレス」およびSaaS依存型侵害の深刻化:** 日本経済新聞（日経）のSlack侵害や、医療機器大手StrykerへのIntune悪用ワイパー攻撃など、正規ツールや認証情報を武器化して「環境寄生」する攻撃が目立っています。

## ソフトウェアサプライチェーンの脆弱性

開発エコシステムの信頼性が根本から揺らいでいます。**TeamPCP**による攻撃は、GitHub Actions、Docker Hub、NPM、PyPIなど複数のプラットフォームを跨いでおり、特にAI開発に不可欠なライブラリ「**LiteLLM**」の汚染は深刻です。攻撃者は正規のメンテナアカウントやCI/CDシークレットを奪取して悪意あるコードを注入しており、開発者がツールを導入・更新するだけで認証情報が窃取され、Kubernetes環境へ横展開されるリスクが生じています。

## インフラ脆弱性とパッチ管理

2026年3月のパッチサイクルでは、最大深刻度の脆弱性が相次いで修正されました。**Cisco Secure FMC**のJavaコード実行脆弱性（CVSS 10.0）に加え、**Oracle Identity Manager**の認証不要RCE（CVSS 9.8）、**Microsoft Devices Pricing Program**（CVSS 9.8）など、企業のアイデンティティや管理の基盤を揺るがす欠陥が標的となっています。また、**Google Chrome**でもグラフィックスライブラリSkiaやV8エンジンにおけるゼロデイ脆弱性が修正されており、ブラウザ経由のコード実行リスクも継続しています。

## 日本国内の情勢とハードウェアリスク

国内では、**日本経済新聞（日経）**において従業員のPC感染からSlackの認証情報が盗まれ、約1.7万人分のチャット履歴や個人情報が漏洩する事象が発生しました。また、**シャープ製ルーター**における認証不備（CVE-2026-32326）がJVNより報告されており、初期パスワードの推測からデバイスが完全に乗っ取られる恐れがあるとして、大手キャリア各社が注意を呼びかけています。

---

# 2026年3月25日 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. TeamPCPによるLiteLLMおよび開発ツールの広域侵害
脅威アクターTeamPCPは、Pythonパッケージ「LiteLLM」のバージョン1.82.7および1.82.8に、認証情報を窃取するバックドアを注入しました。特に1.82.8に含まれる`.pth`ファイルは、パッケージがインポートされずともPythonが起動するだけでペイロードを実行する極めて攻撃的な手法を採用しています。この攻撃はAqua SecurityのTrivyやCheckmarxのKICSの侵害から得たシークレットを再利用して拡大しており、CI/CDパイプライン全体が汚染される事態となっています。

[出典: Arctic Wolf - TeamPCP Supply Chain Attack Campaign Targets Trivy, Checkmarx (KICS), and LiteLLM](https://arcticwolf.com/resources/blog/teampcp-supply-chain-attack-campaign-targets-trivy-checkmarx-kics-and-litellm-potential-downstream-impact-to-additional-projects/)

### 2. InterlockランサムウェアによるCisco Secure FMCゼロデイ攻撃
Amazonの脅威インテリジェンスチームの調査により、InterlockランサムウェアがCisco Secure Firewall Management Center (FMC) の脆弱性（CVE-2026-20131）を、2026年1月26日から（公開の5週間以上前から）悪用していたことが明らかになりました。攻撃者はroot権限でのJavaコード実行を可能にするこの欠陥を使い、教育、製造、公共セクターを標的に、偵察スクリプトや独自のRATを展開して組織内での永続性を確保していました。

[出典: AWS Security Blog - Amazon threat intelligence teams identify Interlock ransomware campaign targeting enterprise firewalls](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-teams-identify-interlock-ransomware-campaign-targeting-enterprise-firewalls/)

### 3. 日経、Slack認証情報窃取により約1.7万人の情報漏洩
日本経済新聞社は、従業員のPCがウイルスに感染したことでSlackの認証情報が盗まれ、社内メッセージプラットフォームに不正アクセスを受けたと発表しました。これにより、従業員や取引先など17,368人分の氏名、メールアドレス、およびSlack上でのチャット履歴が流出した可能性があります。攻撃者は有効な認証情報を用いて「正規ユーザー」として振る舞う「Living Off The Land」戦術を用いており、検知を回避していました。

[出典: Bleeping Computer - Media giant Nikkei reports data breach impacting 17,000 people](https://www.bleepingcomputer.com/news/security/media-giant-nikkei-reports-data-breach-impacting-17-000-people/)

## 深掘り

### 信頼の連鎖を武器化するサプライチェーン攻撃の新段階

2026年3月のTeamPCPの活動は、サプライチェーン攻撃が単なる「一つのパッケージへの混入」から、**「セキュリティツール自体の特権を利用した全方位的な自動侵害」**へと進化したことを示しています。

#### セキュリティツールのパラドックス
TrivyやKICSといった脆弱性スキャナーは、その性質上、CI/CDパイプライン内で高い権限（シークレットへのアクセス権等）を持って動作します。TeamPCPはこれら「信頼されたツール」を侵害することで、防御側が自らマルウェアを実行し、自組織の鍵（クラウドトークン、SSHキー等）を差し出す状況を作り出しました。

#### 高度な永続化と隠蔽工作
TeamPCPのペイロードは、Kubernetes環境において特権ポッド（node-setup-）を全ノードに展開し、ホストのルートディレクトリをマウントして「System Telemetry Service」を装うバックドアを設置します。また、Interlockの事例では、HAProxyを用いたリバースプロキシの構築や5分おきのログ消去ルーチンにより、通信経路と足跡を徹底的に隠蔽する高度なOpSec（作戦保安）が確認されています。

### [関連知識]

#### 用語解説
*   **Living Off The Land (LotL):** 攻撃者が独自のマルウェアを持ち込まず、OSの標準機能（PowerShell等）や正規の管理ツール（Slack, Intune）を悪用して目的を達成する手法。
*   **Zero-day Window (ゼロデイ・ウィンドウ):** 脆弱性が公表される前に、攻撃者がそれを利用可能な期間。Interlockは36日間のウィンドウを保持していました。
*   **Agentic SOC:** AIエージェントが自律的に脅威検知や修復を行う次世代のセキュリティ運用モデル。人間が対応しきれない「マシン・スピード」の攻撃への対抗策として期待されています。

#### 今後の展望
AIコーディングエージェント（Claude Code, OpenClaw等）の普及に伴い、これら自律型ツールを標的にした「間接的プロンプト注入」や、AIが作成したコードへの脆弱性混入が新たな脅威となります。また、攻撃からAD支配までの時間が数時間に短縮されている現状を鑑み、ID管理を核とした「Identity-centric Security」への移行と、フィッシング耐性のあるハードウェアキー（FIDO2等）の標準化が急務です。

## 結論
最新の情勢は、従来の「境界を守る」防御モデルが、**「信頼された開発プロセス」と「正規の管理権限」の侵害**によって無効化されていることを浮き彫りにしました。TrivyやLiteLLMの侵害、StrykerのIntune悪用事例は、システム管理の利便性そのものが致命的な攻撃ベクトルになり得ることを示しています。組織は「侵害を前提（Assume Breach）」としたレジリエンス構築を最優先し、特権アカウントの厳格な監視、シークレットの即時回転、そしてサプライチェーン全体の継続的な整合性検証を組み込んだ運用へと刷新する必要があります。

## 主要引用
* 「TeamPCPはGitHub Actions、Docker Hub、NPM、OpenVSX、PyPIという5つのエコシステムを跨ぐ意図的なキャンペーンを展開している」 — **Endor Labs テクニカル分析**
* 「Interlockは単なる脆弱性悪用ではなく、ゼロデイを保持することで、防御側が探すべき対象を知る前に1週間のリードを得ていた」 — **CJ Moses (Amazon CISO)**
* 「日経の事例は、侵害されたエンドポイントから高価値のSaaSアプリケーションへと直接ピボットする、現代の攻撃ライフサイクルの典型例である」 — **Mayank Kumar (DeepTempo)**
