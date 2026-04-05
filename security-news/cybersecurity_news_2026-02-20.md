# 2026年2月20日 サイバーセキュリティニュースまとめ

## 主要ポイント
* **日本の半導体大手アドバンテストへのランサムウェア攻撃:** 2月15日に検知され、国内事業所の電話システムが一時停止するなど、世界の半導体サプライチェーンへの影響が懸念されています。
* **BeyondTrust製品の脆弱性がランサムウェア攻撃で悪用:** CISAはBeyondTrustのRCE脆弱性（CVE-2026-1731）が実際に悪用されているとして、連邦機関に3日以内の修正を命じました。
* **AI技術を武器化した新型攻撃の出現:** 実行時に生成AI（Google Gemini）を利用して永続化を試みるAndroidマルウェア「PromptSpy」や、AI開発ツールを標的にしたサプライチェーン攻撃が報告されています。

## 産業・インフラへの脅威
日本の半導体試験装置大手**アドバンテスト**がランサムウェア攻撃を受け、ネットワークの一部が侵害されました。この影響で2月16日には国内事業所の電話システムが不通となりましたが、現在は復旧しており、機密データの流出については調査が継続されています。また、米国のミシシッピ大学医療センター（UMMC）もランサムウェア攻撃により全クリニックの閉鎖を余儀なくされるなど、医療インフラへの実害も続いています。

## ソフトウェア・サプライチェーンとAIの悪用
AI搭載のコーディングアシスタント「**Cline CLI**」が、侵害されたトークンを悪用したサプライチェーン攻撃を受け、約4,000名の開発者に無断でAIエージェント「OpenClaw」がインストールされました。また、Microsoft Outlookの正規アドインのドメインが乗っ取られ、4,000件以上の認証情報が盗まれる「**AgreeToSteal**」という新たな手口も判明しました。さらに、AIを利用して動的に挙動を変えるマルウェア「**PromptSpy**」の出現は、防御側にとって極めて困難な課題を突きつけています。

## 重要脆弱性とデータ侵害
Windowsの標準アプリ「**メモ帳（Notepad）**」において、新たに追加されたMarkdown機能に起因するリモートコード実行（RCE）の脆弱性（CVE-2026-20841）が発見・修正されました。一方、データ侵害の規模も拡大しており、フランスの銀行登録機関で120万アカウント、PayPalではソフトエラーにより6ヶ月間にわたり社会保障番号を含む情報が露出していたことが公表されました。

---

# 2026年2月20日 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. アドバンテストへのサイバー攻撃とサプライチェーンのリスク
2026年2月15日、アドバンテストは社内ネットワークでの異常な動きを検知し、一部システムでランサムウェアが展開された可能性があると発表しました。同社は半導体試験装置で世界シェアを誇るため、インシデントによる出荷遅延や独自技術の流出は、世界のチップ供給網全体にボトルネックを生じさせるリスクがあります。
[出典: Bleeping Computer - Japanese tech giant Advantest hit by ransomware attack](https://www.bleepingcomputer.com/news/security/japanese-tech-giant-advantest-hit-by-ransomware-attack/)
[出典: ITmedia NEWS - アドバンテストに不正アクセス、ランサムウェア被害の可能性](https://www.itmedia.co.jp/news/articles/2602/19/news100.html)

### 2. BeyondTrustの特権管理ツールを狙う高速な武器化
BeyondTrustのRemote Support製品に存在する、認証不要でOSコマンド実行が可能な脆弱性（CVE-2026-1731）が、PoC公開直後からランサムウェア攻撃に利用されています。CISAはこの脆弱性を「既知の悪用された脆弱性（KEV）」カタログに追加し、連邦機関に対し緊急のパッチ適用、または製品の使用停止を命じる異例の対応をとりました。
[出典: Bleeping Computer - CISA: BeyondTrust RCE flaw now exploited in ransomware attacks](https://www.bleepingcomputer.com/news/security/cisa-beyondtrust-rce-flaw-now-exploited-in-ransomware-attacks/)
[出典: The Hacker News - BeyondTrust Flaw Used for Web Shells, Backdoors, and Data Exfiltration](https://thehackernews.com/2026/02/beyondtrust-flaw-used-for-web-shells.html)

### 3. 初のAI実行時利用マルウェア「PromptSpy」
ESETの研究者は、Android向けマルウェア「PromptSpy」がGoogleのGemini AIをAPI経由で呼び出し、感染したデバイスのOSバージョンやレイアウトに合わせた最適な永続化（潜伏）手法をリアルタイムでAIに生成させていることを確認しました。これにより、攻撃者は静的な解析や従来のシグネチャベースの検知を容易に回避することが可能になります。
[出典: Bleeping Computer - PromptSpy is the first known Android malware to use generative AI at runtime](https://www.bleepingcomputer.com/news/security/promptspy-is-the-first-known-android-malware-to-use-generative-ai-at-runtime/)
[出典: The Hacker News - PromptSpy Android Malware Abuses Gemini AI to Automate Recent-Apps Persistence](https://thehackernews.com/2026/02/promptspy-android-malware-abuses-google.html)

## 深掘り

### 標準ツールとAIの「高機能化」が招く新たな攻撃面
2026年2月の動向は、シンプルであったはずの標準アプリケーションや開発ツールが、高機能化（Markdown対応やAI統合）によって予期せぬ攻撃経路（アタックサーフェス）となっている現状を浮き彫りにしています。

#### 開発環境へのAIサプライチェーン攻撃
AIコーディングアシスタント「Cline CLI」への攻撃（Clinejection）は、GitHubのリポジトリキャッシュを汚染し、ビルドパイプラインを操作して悪意ある更新を配信するものでした。これは、AIエージェントに広範な権限（Issueの自動処理など）を与えすぎたことが原因であり、AIを「特権アクター」として管理・統制する必要性を明確に示しています。

#### Windowsメモ帳（Notepad）の変容
30年以上にわたり安全とされてきた「メモ帳」の脆弱性は、追加されたMarkdownのHTMLプレビュー機能において、不適切なURIフィルタリングがあったために発生しました。これにより、単なるテキストファイル（.txt / .md）を開き、中のリンクをクリックするだけでリモートコード実行が可能になるという、従来の「テキストファイルは安全」という前提を覆す事態となりました。

### [関連知識]

#### [用語解説]
*   **PromptSpy:** 実行時に生成AIモデルと通信し、感染環境に合わせて行動を最適化する「自律型」マルウェア。
*   **AgreeToSteal:** 放置されたアドインのドメインを再取得して、正規のMicrosoftストアからフィッシングページを配信するサプライチェーン攻撃。
*   **Vibe Hacking:** 従来のルールベースの検知をAIの適応能力で回避しようとする、AI駆動型攻撃の総称。

#### [今後の展望]
2026年は「信頼の境界線」が完全に崩壊した年として記憶されるでしょう。管理ツール、開発ライブラリ、標準エディタなど、これまで「安全」と信じられていた資産が攻撃の起点となっています。今後は、AIエージェントのアイデンティティ管理（Agentic Zero Trust）の導入と、ソフトウェアの依存関係（SBOM）だけでなく、動的なリモート依存関係の継続的な監視が不可欠になります。

## 結論
本日の報告は、サイバー攻撃が物理的な重要インフラ（半導体製造や医療）を直接脅かす段階にあり、その手段としてAI技術やサプライチェーンの「信頼の空白」が巧妙に悪用されていることを示しています。パッチ適用の迅速化（数日単位）という戦術的対応に加え、インフラ設計そのものをゼロトラストモデルへと根本的に再定義する戦略的転換が、あらゆる組織に求められています。

## 主要引用
*   「AIはサイバー犯罪を『工業化』した。かつて熟練者が時間を要した作業が、今や自動化され、世界規模で拡張可能になっている」 — 2026年サイバー脅威展望
*   「攻撃の発見から武器化までのサイクルが24時間を切った現状では、従来のパッチ管理モデルはもはや存続できない」 — セキュリティ研究者によるBeyondTrust脆弱性分析
*   「信頼できないソースから入手したMarkdownファイルをメモ帳で開くことは、今やブラウザで怪しいURLをクリックするのと同等のリスクを伴う」 — XenoSpectrum 解説
