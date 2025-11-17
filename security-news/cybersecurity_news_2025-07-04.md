# 2025-07-04 サイバーセキュリティニュースまとめ

## 主要ポイント

*   欧州NIS2指令が日本企業にも適用される可能性があり、高額な制裁金リスクがあるため、適切な対応が不可欠です。
*   ランサムウェア攻撃の巧妙化と要求額の増大、ディープフェイクを用いた脅迫など、サイバー攻撃の脅威が多様化しています。
*   デバイスコードフィッシングは、多要素認証をバイパスする強力な攻撃手法であり、Microsoft Entra ID/Microsoft 365を標的とした事例が報告されています。

## 国内ニュース

### 欧州NIS2指令に向けた日本企業の備え

2023年に施行された欧州NIS2指令は、EU域内の重要インフラやデジタル事業者に対し、サイバーセキュリティ対策の強化を義務付ける包括的な法制度です。この指令はEU域内企業だけでなく、域外から事業展開する日本企業にも適用される可能性があります。特にEU子会社を持つ企業では、グループ全体の売上高に基づく高額な制裁金リスクがあるため、適切な対応が不可欠です。NIS2指令の主な変更点として、適用対象となる業種や企業規模の拡大、違反時の罰則強化、当局への報告義務の厳格化が挙げられます。日本企業がEU域内にグループ会社を持ち、該当する事業を現地で行っている場合、日本本社が対応を求められるケースがあります。違反時の制裁金は、主要事業体の場合、全世界売上高の2％または1,000万ユーロのいずれか高い方が上限となり、重要事業体は売上高の1.4％または700万ユーロのいずれか高い方が適用されます。また、企業評価の低下や経営陣への刑事責任の可能性も指摘されており、対応は重要な経営課題となっています。

### 偽造した顔で就職面接？ 増額するランサムウェア要求額、偽データを用いた脅迫……2024年の実例に見る｢脅威動向｣と３つの被害主因まとめ

2024年、サイバー攻撃を受けた企業の25％は、侵害からデータ流出までの時間が5時間を下回っていました。パロアルトネットワークスの調査によると、攻撃の検知にかかる時間は短縮されているものの、攻撃の速度には及んでいません。ランサムウェア攻撃では、当初の「暗号化」に加え、偽データを用いた脅迫など、攻撃手法が多様化しています。リアルタイムのディープフェイクは、市販のツールと安価なハードウェアでわずか1時間ほどで作成可能であり、就職面接での悪用事例も報告されています。サイバー被害の主な原因として、セキュリティの複雑化による効果低下、サプライチェーン攻撃、そしてランサムウェア攻撃が挙げられます。

### デバイスコードフィッシング - セキュリティブログ - NEC Corporation

デバイスコードフィッシングは、正規の認証認可方法であるデバイスコードフローを悪用したフィッシング攻撃です。この攻撃は、被害者に多要素認証（MFA）やパスワードレス認証が設定されていても、アクセストークンやリフレッシュトークンを入手し、被害者の環境にアクセスすることを可能にします。Microsoft社は2024年8月からデバイスコードフィッシングが活性化していると2025年2月に公表しています。攻撃者は、GraphSpyなどのツールを利用してデバイスコードを生成し、正規のMicrosoftのURLを悪用したフィッシングメールを送信します。被害者がメール内のURLにアクセスし、コードを入力することで、攻撃者はアクセストークンやリフレッシュトークンを取得し、メールの閲覧や送信、さらにはTeamsメッセージの閲覧や送信が可能になります。特に、高権限のアカウントを標的としたデバイスコードフィッシングは、永続化を可能にする強力な攻撃手法です。

## 海外の重大事例

### NightEagle APT Exploits Microsoft Exchange Flaw to Target China’s Military and Tech Sectors

NightEagle（別名APT-Q-95）と呼ばれる未確認の脅威アクターが、中国の政府、防衛、技術分野を標的とするゼロデイエクスプロイトチェーンの一部として、Microsoft Exchangeサーバーを悪用していることが明らかになりました。QiAnXinのRedDripチームによると、この脅威アクターは2023年から活動しており、非常に速いペースでネットワークインフラを切り替えています。攻撃は、ハイテク、チップ半導体、量子技術、人工知能、軍事分野の企業を特に標的としています。

### SaaS Security Made Simple

SaaSプラットフォームの普及に伴い、データ保護の課題が浮上しています。多くのSaaSプロバイダーは共有責任モデルを採用しており、稼働時間とアプリケーションのセキュリティは保証するものの、データ保護はユーザー側の責任となります。ハイブリッドアーキテクチャ、グローバルチーム、絶え間ないサイバー脅威が存在する現代において、この責任を管理することはこれまで以上に困難になっています。組織は、ハイブリッドおよびマルチクラウド環境での分散データ、IaaS、SaaS、レガシーシステム間の複雑な統合レイヤー、規制強化、ランサムウェアの脅威、内部脅威など、多岐にわたる課題に直面しています。

### Your AI Agents Might Be Leaking Data — Watch this Webinar to Learn How to Stop It

生成AIはビジネスの働き方を変革していますが、同時に機密性の高い企業データが漏洩する新たな隠れた経路を生み出しています。AIエージェントやカスタムGenAIワークフローは、SharePoint、Google Drive、S3バケット、内部ツールなどからデータを引き出す際に、意図せず機密情報を不適切なユーザーやインターネットに公開してしまう可能性があります。厳格なアクセス制御、ガバナンスポリシー、監視がなければ、AIが誤って内部の給与データや未公開の製品デザインを漏洩させるリスクがあります。

### Massive Android Fraud Operations Uncovered: IconAds, Kaleidoscope, SMS Malware, NFC Scams

HUMANの新しいレポートによると、352のAndroidアプリで構成されるIconAdsと呼ばれるモバイル広告詐欺操作が阻止されました。これらのアプリは、ユーザーの画面に文脈に合わない広告をロードし、デバイスのホーム画面ランチャーからアイコンを隠すように設計されており、被害者が削除しにくくなっていました。これらのアプリはGoogle Playストアから削除されています。この広告詐欺スキームは、活動のピーク時には1日あたり12億件の入札要求を占めていました。IconAdsに関連するトラフィックの大部分は、ブラジル、メキシコ、米国から発生していました。

### Over 40 Malicious Firefox Extensions Target Cryptocurrency Wallets, Stealing User Assets

サイバーセキュリティ研究者らは、Mozilla Firefox向けに40以上の悪意のあるブラウザ拡張機能を発見しました。これらは、仮想通貨ウォレットの秘密を盗み、ユーザーのデジタル資産を危険にさらすように設計されています。これらの拡張機能は、Coinbase、MetaMask、Trust Wallet、Phantom、Exodus、OKX、Keplr、MyMonero、Bitget、Leap、Ethereum Wallet、Filfoxなどの広く使用されているプラットフォームの正規のウォレットツールを偽装しています。この大規模なキャンペーンは、少なくとも2025年4月から継続しており、先週も新しい拡張機能がFirefoxアドオンストアにアップロードされていました。これらの拡張機能は、人気を人為的に水増しし、何百もの5つ星レビューを追加することで、信頼性を偽装していました。

### Chinese Hackers Exploit Ivanti CSA Zero-Days in Attacks on French Government, Telecoms

フランスのサイバーセキュリティ機関は、中国のハッキンググループがIvanti Cloud Services Appliance（CSA）デバイスの複数のゼロデイ脆弱性を悪用し、フランスの政府、電気通信、メディア、金融、運輸部門にわたる多数の組織に影響を与えたことを明らかにしました。2024年9月初旬に検出されたこのキャンペーンは、Houkenというコードネームの特定の侵入セットに起因するとされており、Google MandiantがUNC5174（別名UteusまたはUetus）として追跡している脅威クラスターと一部重複していると評価されています。攻撃者はゼロデイ脆弱性と高度なルートキットを使用していますが、中国語圏の開発者によって作成された多数のオープンソースツールも活用しています。

## 深掘り

### サイバー攻撃の多様化と対策の重要性

近年のサイバー攻撃は、ランサムウェア、フィッシング、ゼロデイ脆弱性の悪用、モバイル詐欺、AIエージェントからのデータ漏洩など、その手口が多様化・巧妙化しています。攻撃者は常に新しい技術や手法を開発し、企業のセキュリティ対策の隙を狙っています。特に、多要素認証をバイパスするデバイスコードフィッシングや、ディープフェイクを用いた詐欺は、従来のセキュリティ対策だけでは防ぎきれない新たな脅威となっています。また、欧州NIS2指令のように、サイバーセキュリティ対策が法的に義務付けられ、違反に対する罰則が強化される動きも加速しており、企業は法規制への対応と同時に、実効性のあるセキュリティ対策を講じる必要があります。

#### ゼロデイ脆弱性

ゼロデイ脆弱性とは、ソフトウェアやハードウェアに存在する、まだ一般に知られていない、または修正プログラムが提供されていない脆弱性のことです。攻撃者はこの脆弱性を悪用して、セキュリティパッチが適用されていないシステムに侵入し、マルウェアの実行、データの窃取、システム制御の奪取などを行います。ゼロデイ攻撃は、防御側が対策を講じる時間がないため、非常に危険な攻撃とされています。

#### 多要素認証（MFA）

多要素認証（Multi-Factor Authentication, MFA）とは、ユーザー認証において、知識情報（パスワードなど）、所持情報（スマートフォン、ICカードなど）、生体情報（指紋、顔など）のうち、2つ以上の異なる要素を組み合わせて認証を行うセキュリティ手法です。これにより、たとえパスワードが漏洩しても、他の要素がなければ不正アクセスを防ぐことができ、セキュリティを大幅に向上させることができます。しかし、デバイスコードフィッシングのように、MFAをバイパスする巧妙な攻撃も存在するため、MFAの導入だけでなく、ユーザーへの教育や最新の脅威情報の把握が重要です。

#### ランサムウェア

ランサムウェアは、マルウェアの一種で、感染したコンピュータのファイルを暗号化したり、システムをロックしたりして、身代金（ランサム）を要求するサイバー攻撃です。身代金が支払われない場合、ファイルは復元されなかったり、窃取した機密情報が公開されたりする可能性があります。近年では、データの暗号化だけでなく、窃取したデータを公開すると脅迫する「二重脅迫」の手口が増加しており、被害はより深刻化しています。

## 結論

今日のサイバーセキュリティ環境は、日々進化する脅威と新たな規制によって複雑さを増しています。日本企業は、欧州NIS2指令のような国際的な規制への対応に加え、ランサムウェア、フィッシング、AI関連のデータ漏洩といった多様な攻撃手法に対する包括的な防御策を講じる必要があります。技術的な対策だけでなく、従業員へのセキュリティ意識向上トレーニング、インシデント対応計画の策定、そして最新の脅威情報の継続的な収集と分析が、企業をサイバー攻撃から守る上で不可欠です。サイバーセキュリティは、もはやIT部門だけの問題ではなく、経営層が主導して取り組むべき経営課題として認識し、組織全体で強固なセキュリティ体制を構築することが求められます。

## 主要引用

*   PwC Japanグループ: [欧州NIS2指令に向けた日本企業の備え](https://www.pwc.com/jp/ja/knowledge/column/awareness-cyber-security/digital-governance-forum-explanation2.html)
*   東洋経済オンライン: [偽造した顔で就職面接？ 増額するランサムウェア要求額、偽データを用いた脅迫……2024年の実例に見る｢脅威動向｣と３つの被害主因まとめ](https://toyokeizai.net/articles/-/888410?display=b)
*   NEC Corporation: [デバイスコードフィッシング - セキュリティブログ](https://jpn.nec.com/cybersecurity/blog/250704/index.html)
*   The Hacker News: [NightEagle APT Exploits Microsoft Exchange Flaw to Target China’s Military and Tech Sectors](https://thehackernews.com/2025/07/nighteagle-apt-exploits-microsoft.html)
*   Cyware: [City of Coppell, TX notifies 17K residents of data breach following ransomware attack](https://social.cyware.com/cyber-security-news-articles/city-of-coppell-tx-notifies-17k-residents-of-data-breach-following-ransomware-attack)
*   Cyware: [Taiwan Flags Chinese Apps Over Data Security Violations](https://social.cyware.com/cyber-security-news-articles/taiwan-flags-chinese-apps-over-data-security-violations)
*   Cyware: [Researchers Defeat Content Security Policy Protections via HTML Injection](https://social.cyware.com/cyber-security-news-articles/researchers-defeat-content-security-policy-protections-via-html-injection)
*   Cyware: [IdeaLab confirms data stolen in ransomware attack last year](https://social.cyware.com/cyber-security-news-articles/idealab-confirms-data-stolen-in-ransomware-attack-last-year)
*   Cyware: [Virginia county says April ransomware attack exposed employee SSNs](https://social.cyware.com/cyber-security-news-articles/virginia-county-says-april-ransomware-attack-exposed-employee-ssns)
*   Cyware: [Over 40 Malicious Firefox Extensions Target Cryptocurrency Wallets, Stealing User Assets](https://social.cyware.com/cyber-security-news-articles/over-40-malicious-firefox-extensions-target-cryptocurrency-wallets-stealing-user-assets)
*   Cyware: [Chinese Hackers Exploit Ivanti CSA Zero-Days in Attacks on French Government, Telecoms](https://social.cyware.com/cyber-security-news-articles/chinese-hackers-exploit-ivanti-csa-zero-days-in-attacks-on-french-government-telecoms)
*   Cyware: [The Hidden Risks of SaaS: Why Built-In Protections Aren't Enough for Modern Data Resilience](https://social.cyware.com/cyber-security-news-articles/the-hidden-risks-of-saas-why-built-in-protections-arent-enough-for-modern-data-resilience)
*   Cyware: [Your AI Agents Might Be Leaking Data — Watch this Webinar to Learn How to Stop It](https://social.cyware.com/cyber-security-news-articles/your-ai-agents-might-be-leaking-data-watch-this-webinar-to-learn-how-to-stop-it)
*   Cyware: [Massive Android Fraud Operations Uncovered: IconAds, Kaleidoscope, SMS Malware, NFC Scams](https://social.cyware.com/cyber-security-news-articles/massive-android-fraud-operations-uncovered-iconads-kaleidoscope-sms-malware-nfc-scams)


