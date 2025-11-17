# 2025-09-12 サイバーセキュリティニュースまとめ

## 主要ポイント

*   日本国内では、一般財団法人日本熊森協会とCBC株式会社が不正アクセスによる被害を受け、情報漏洩や業務障害が発生しました。
*   海外では、Google Pixel 10がAI生成メディアの認証機能を強化し、Microsoftは80の脆弱性を修正しました。
*   米上院議員がMicrosoftのサイバーセキュリティ過失に関するFTC調査を要求し、中国のAPTグループがフィリピン軍事システムにファイルレスマルウェアを展開した事例も報告されています。

## 国内ニュース

### 日本熊森協会への不正アクセスと情報漏洩

一般財団法人日本熊森協会は2025年9月、管理するサーバーが不正アクセスを受け、協会ホームページやメールが改ざんされる事態に至ったと発表しました。この不正アクセスにより、一時的にホームページの管理画面やメールシステムが利用不能となり、メールサーバーに保存されていた一部のデータ（氏名、メールアドレス、住所、電話番号、クレジットカード名義）が2013年10月25日以降の履歴で外部に流出した可能性が判明しました。ただし、クレジットカード番号そのものの流出は確認されておらず、現時点での不正利用の報告もありません。協会はサーバー会社や外部専門家と協力し、セキュリティ対策の強化を進めており、ホームページの復旧作業を行っています。

出典: [不正アクセスでホームページ改ざんに個人情報や一部クレカ情報漏えいか│日本熊森協会｜サイバーセキュリティ.com](https://cybersecurity-jp.com/news/110823)

### CBC株式会社への不正アクセスと業務障害

CBC株式会社は2025年9月5日までに、同社サーバーが外部の第三者による不正アクセスを受けたことを明らかにしました。事象確認後、直ちにネットワークを遮断するなどの被害拡大防止措置が講じられましたが、この不正アクセスの影響により一部の業務に支障が出ています。現在も復旧作業が続いており、完全な復旧には時間を要する見込みです。同社は被害範囲の特定、原因、侵入経路の調査を進めています。

出典: [不正アクセスで障害発生か│CBC株式会社｜サイバーセキュリティ.com](https://cybersecurity-jp.com/news/110821)

## 海外ニュース

### Google Pixel 10におけるAI生成メディアの認証機能強化

Googleは、新しいGoogle Pixel 10スマートフォンで、AI生成メディアの出所と履歴を検証するためのC2PA（Coalition for Content Provenance and Authenticity）標準をサポートすると発表しました。PixelカメラアプリとGoogleフォトアプリにC2PAのコンテンツクレデンシャルが追加され、改ざん防止機能付きの暗号署名されたデジタルマニフェストが提供されます。この機能は、Google Tensor G5、Titan M2セキュリティチップ、およびAndroidオペレーティングシステムに組み込まれたハードウェアベースのセキュリティ機能の組み合わせによって実現されており、デジタルメディアの透明性を高め、AIによるコンテンツの信頼性を確保することを目的としています。

出典: [Google Pixel 10 Adds C2PA Support to Verify AI-Generated Media Authenticity](https://thehackernews.com/2025/09/google-pixel-10-adds-c2pa-support-to.html)

### 米上院議員がMicrosoftのサイバーセキュリティ過失に関するFTC調査を要求

米上院議員ロン・ワイデンは、Microsoftの「重大なサイバーセキュリティ過失」が米国の重要インフラ（医療ネットワークを含む）へのランサムウェア攻撃を可能にしたとして、連邦取引委員会（FTC）にMicrosoftの調査を要求しました。この要求は、医療システムAscensionへのランサムウェア攻撃で約560万人の個人情報と医療情報が盗まれた事件に関連しています。攻撃者はMicrosoftのソフトウェアの「危険なほど安全でないデフォルト設定」を利用し、Kerberoastingという技術を用いて特権アクセスを取得したとされています。ワイデン議員は、MicrosoftがRC4暗号化技術のサポートを継続していることや、特権アカウントのパスワード長を強制しないことが、攻撃者に悪用されていると指摘しています。

出典: [Senator Wyden Urges FTC to Probe Microsoft for Ransomware-Linked Cybersecurity Negligence](https://thehackernews.com/2025/09/senator-wyden-urges-ftc-to-probe.html)

### 中国のAPTグループがフィリピン軍事システムにファイルレスマルウェア「EggStreme」を展開

中国のAPT（Advanced Persistent Threat）グループが、フィリピンの軍事関連企業を標的とし、これまで文書化されていなかったファイルレスマルウェアフレームワーク「EggStreme」を使用して侵害したと報告されました。EggStremeは、メモリに悪意のあるコードを直接注入し、DLLサイドローディングを利用してペイロードを実行することで、永続的で目立たないスパイ活動を実現します。その中心となるコンポーネントであるEggStremeAgentは、システム偵察、ラテラルムーブメント、キーロガーによるデータ窃取を可能にするフル機能のバックドアです。このマルウェアは、ファイルレスの性質、DLLサイドローディングの多用、洗練された多段階の実行フローにより、検出が困難であるとされています。

出典: [Chinese APT Deploys EggStreme Fileless Malware to Breach Philippine Military Systems](https://thehackernews.com/2025/09/chinese-apt-deploys-eggstreme-fileless.html)

### Microsoftが80の脆弱性を修正（SMB PrivEscとAzure CVSS 10.0のバグを含む）

Microsoftは、80のセキュリティ脆弱性（8件がCritical、72件がImportant）を修正するパッチを公開しました。これには、Windows SMBの特権昇格の脆弱性（CVE-2025-55234）や、Azure NetworkingのCVSSスコア10.0の重大な脆弱性（CVE-2025-54914）が含まれています。主な修正は、特権昇格（38件）、リモートコード実行（22件）、情報漏洩（14件）、サービス拒否（3件）に関する脆弱性です。また、BitLockerの4つの脆弱性（CVE-2025-54911、CVE-2025-54912など）も修正され、物理アクセスを持つ攻撃者がBitLocker保護をバイパスし、暗号化されたデータにアクセスできる可能性が排除されました。

出典: [Microsoft Fixes 80 Flaws — Including SMB PrivEsc and Azure CVSS 10.0 Bugs](https://thehackernews.com/2025/09/microsoft-fixes-80-flaws-including-smb.html)

### CiscoがIOS XRの重大な脆弱性を修正

Ciscoは、IOS XRソフトウェアの3つの脆弱性に対するパッチをリリースしました。これには、ISOイメージ検証のバイパス（CVE-2025-20248）とサービス拒否（DoS）状態を引き起こす可能性のあるARP実装のバグ（CVE-2025-20340）が含まれます。ISOイメージ検証のバイパスにより、署名されていないファイルがISOイメージに追加され、デバイスにインストールされる可能性があり、ARP実装のバグは、隣接する認証されていない攻撃者によってDoS状態を引き起こす可能性があります。Ciscoは、これらの脆弱性が悪用されたという報告はないとしているものの、早期のパッチ適用を推奨しています。

出典: [Cisco Patches High-Severity IOS XR Vulnerabilities](https://www.securityweek.com/cisco-patches-high-severity-ios-xr-vulnerabilities/)

### GoogleがChromeの重大な脆弱性を修正

Googleは、Chrome 124のアップデートを公開し、重大なセキュリティホールを含む4つの脆弱性を修正しました。最も重大な脆弱性（CVE-2024-4058）は、ANGLEグラフィックスレイヤーエンジンにおけるタイプ混同のバグで、リモートからの任意のコード実行やサンドボックスエスケープにつながる可能性がありました。この脆弱性を報告したQrious Secureの2名には16,000ドルの報奨金が授与されました。

出典: [Google Patches Critical Chrome Vulnerability](https://www.securityweek.com/google-patches-critical-chrome-vulnerability/)

### Jaguar Land Roverがサイバー攻撃によるデータ侵害を認める

Jaguar Land Rover (JLR) は、最近のサイバー攻撃により工場が停止しただけでなく、データ侵害も発生したことを認めました。この攻撃により、工場の一時停止や一部システムの切断が発生しました。盗まれたデータの種類については詳細を明らかにしていないものの、関連規制当局に通知し、影響を受けた個人には追って連絡するとしています。この攻撃には、悪名高いサイバー犯罪グループ「Scattered Spider」が関与したとされています。

出典: [Jaguar Land Rover Admits Data Breach Caused by Recent Cyberattack](https://www.securityweek.com/jaguar-land-rover-admits-data-breach-caused-by-recent-cyberattack/)

## 深掘り

### AI生成メディアの信頼性確保とサイバーセキュリティ

Google Pixel 10におけるC2PA標準のサポートは、AI技術の進化に伴うフェイクニュースやディープフェイクといった問題への重要な対策となります。C2PAは、デジタルコンテンツの作成元と履歴を検証するための技術であり、改ざん防止機能付きのデジタルマニフェストを提供します。これにより、画像や動画、音声ファイルがどのように作成され、編集されたかといった情報が「デジタル栄養表示」のように提供され、コンテンツの信頼性を高めることが期待されます。サイバーセキュリティの観点からは、AI生成コンテンツの悪用を防ぐための重要な一歩であり、情報の信頼性を確保するための技術的な基盤となります。今後、このような認証技術が広く普及することで、デジタルコンテンツの健全性が保たれることが期待されます。

### Microsoftのセキュリティ対策とKerberoastingの脅威

米上院議員によるMicrosoftへのFTC調査要求は、企業が提供するソフトウェアのデフォルト設定がサイバーセキュリティに与える影響の大きさを浮き彫りにしています。特に、Kerberoastingのような認証プロトコルを悪用する攻撃は、デフォルトで有効になっているRC4暗号化技術の脆弱性を突くものです。RC4は1987年に開発された古い暗号化技術であり、2015年にはTLSでの使用が禁止されるなど、その脆弱性は広く認識されています。Microsoftはパッチをリリースし、将来的にRC4のサポートを廃止する計画を示していますが、依然として多くのシステムでデフォルトで有効になっている現状は、攻撃者にとっての足がかりとなり得ます。企業は、提供されるソフトウェアのセキュリティ設定を適切に見直し、最新のセキュリティベストプラクティスに従うことが不可欠です。また、パスワードポリシーの強化や多要素認証の導入など、多層的な防御策を講じる必要があります。

#### 用語解説

*   **C2PA (Coalition for Content Provenance and Authenticity)**: デジタルコンテンツの出所と履歴を検証するための技術標準を開発する団体。コンテンツの信頼性を高めることを目的としている。
*   **Kerberoasting**: Kerberos認証プロトコルを悪用し、サービスアカウントの暗号化された資格情報をActive Directoryから抽出する攻撃手法。特にRC4のような脆弱な暗号化アルゴリズムを使用している場合に悪用されやすい。
*   **APT (Advanced Persistent Threat)**: 高度で持続的な脅威。特定の組織や国家を標的とし、長期にわたってネットワークに潜伏し、機密情報を窃取したり、システムを破壊したりする攻撃。
*   **ファイルレスマルウェア**: 実行ファイルとしてディスクに保存されず、メモリ上で直接実行されるマルウェア。検出が困難であり、フォレンジック調査も複雑になる。
*   **DLLサイドローディング**: 正規のアプリケーションが読み込むべきDLLの代わりに、悪意のあるDLLを読み込ませる攻撃手法。正規のプロセスとして実行されるため、検出が難しい。
*   **CVSS (Common Vulnerability Scoring System)**: ソフトウェアの脆弱性の深刻度を評価するための共通の基準。スコアが高いほど深刻度が高い。

#### 今後の展望

サイバーセキュリティの脅威は日々進化しており、AI技術の悪用やサプライチェーン攻撃など、新たな攻撃手法が台頭しています。GoogleのC2PAのような認証技術の導入は、AI生成コンテンツの信頼性確保に貢献する一方で、Microsoftの事例が示すように、既存システムの脆弱性やデフォルト設定の甘さが依然として大きなリスク要因となっています。企業や組織は、最新の脅威動向を常に把握し、多層的なセキュリティ対策を講じるとともに、従業員のセキュリティ意識向上も不可欠です。また、国際的な連携を通じて、サイバー攻撃に対する情報共有と共同対策を強化していくことが、今後のサイバーセキュリティ対策において重要となるでしょう。

## 結論

2025年9月12日現在、サイバーセキュリティの脅威は国内・海外を問わず多岐にわたっています。不正アクセスによる情報漏洩や業務障害、AI生成コンテンツの信頼性問題、既存システムの脆弱性を悪用した攻撃など、様々な課題が浮上しています。これらの事例から、技術的な対策だけでなく、組織全体のセキュリティ意識の向上、そして国際的な協力体制の構築が、サイバー空間の安全を確保するために不可欠であることが再確認されます。常に最新の情報を収集し、適切な対策を講じることが、個人および組織のデジタル資産を守る上で極めて重要です。

## 主要引用

*   [不正アクセスでホームページ改ざんに個人情報や一部クレカ情報漏えいか│日本熊森協会｜サイバーセキュリティ.com](https://cybersecurity-jp.com/news/110823)
*   [不正アクセスで障害発生か│CBC株式会社｜サイバーセキュリティ.com](https://cybersecurity-jp.com/news/110821)
*   [Google Pixel 10 Adds C2PA Support to Verify AI-Generated Media Authenticity](https://thehackernews.com/2025/09/google-pixel-10-adds-c2pa-support-to.html)
*   [Senator Wyden Urges FTC to Probe Microsoft for Ransomware-Linked Cybersecurity Negligence](https://thehackernews.com/2025/09/senator-wyden-urges-ftc-to-probe.html)
*   [Chinese APT Deploys EggStreme Fileless Malware to Breach Philippine Military Systems](https://thehackernews.com/2025/09/chinese-apt-deploys-eggstreme-fileless.html)
*   [Microsoft Fixes 80 Flaws — Including SMB PrivEsc and Azure CVSS 10.0 Bugs](https://thehackernews.com/2025/09/microsoft-fixes-80-flaws-including-smb.html)
*   [Cisco Patches High-Severity IOS XR Vulnerabilities](https://www.securityweek.com/cisco-patches-high-severity-ios-xr-vulnerabilities/)
*   [Google Patches Critical Chrome Vulnerability](https://www.securityweek.com/google-patches-critical-chrome-vulnerability/)
*   [Jaguar Land Rover Admits Data Breach Caused by Recent Cyberattack](https://www.securityweek.com/jaguar-land-rover-admits-data-breach-caused-by-recent-cyberattack/)

