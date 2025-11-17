# 2025年10月11日 サイバーセキュリティニュースまとめ

## 主要ポイント

*   アサヒグループホールディングスがロシア系ランサムウェアグループ「Qilin」によるサイバー攻撃を受け、国内の生産・出荷に大きな影響が出ています。
*   日本のCISOの69%が今後1年以内に重大なサイバー攻撃を予想しており、情報漏洩の約9割に退職した従業員が関与しているとの調査結果が発表されました。
*   北朝鮮の脅威アクターが2025年に20億ドル以上の仮想通貨を盗み出し、建築・土木工学分野での詐欺活動も拡大しています。

## 国内サイバーセキュリティ動向

### アサヒグループホールディングスへのランサムウェア攻撃

日本を代表する飲料メーカーであるアサヒグループホールディングスは、9月29日にサイバー攻撃を受けたことを公表しました。この攻撃はロシア系のサイバー犯罪組織「Qilin（キリン）」によるランサムウェア攻撃であり、国内のグループ各社の受注、出荷、コールセンター業務がシステム障害により停止しました[1]。アサヒは手作業での受注・出荷を進めていますが、復旧には時間がかかると見られています。Qilinはアサヒから9323ファイル（27ギガバイト）の内部情報を盗み出し、一部を公開して身代金を要求している模様です[1]。

この攻撃は、アサヒの国内生産拠点30ヶ所のほとんどで生産停止を引き起こし、コンピュータシステムがダウンしたため、注文処理や出荷は手書きやFAXで行われています。これにより、以前よりも出荷量が大幅に減少しており、日本のビール市場の約40%を占めるアサヒの製品供給問題は、飲食店や小売店に大きな影響を与えています[2]。

### 日本のCISOが重大なサイバー攻撃を予想

日本プルーフポイントが発表した「2025 Voice of the CISO」レポートによると、日本のCISOの69%が今後1年以内に重大なサイバー攻撃を受けると予想しています。また、日本のCISOが経験した情報漏洩の約9割に「退職した従業員」が関与していることが明らかになりました。サイバー攻撃の巧妙化に加え、内部不正や生成AIのガバナンス対応など、CISOは極度のプレッシャーに直面している状況が浮き彫りになっています[3]。

## 海外サイバーセキュリティ動向

### 北朝鮮の脅威アクターによる仮想通貨盗難と詐欺活動の拡大

北朝鮮の脅威アクターは、2025年に20億ドル以上の仮想通貨資産を盗み出し、過去最高の年間総額を記録しました。最大の被害は2025年2月のBybitハッキングで、14.6億ドルが失われました[4]。さらに、北朝鮮の工作員は、建築・土木工学分野に詐欺活動を拡大しており、フリーランスの設計業務で正規の専門家になりすましています[5]。また、過去4年間で130以上の偽のペルソナが特定され、約5,000社で6,500件以上の求人面接に関与していたことが判明しています[6]。

### AIチャットボットが悪用されるサイバー攻撃

金融、医療、テクノロジー分野の企業を標的とした新たなサイバー攻撃キャンペーンでは、顧客サービスや自動化のために導入されたLLMチャットボットが悪用されています。攻撃者は、これらのチャットボットをバックドアとして利用し、内部システムデータなどを窃取することに成功しています[7]。

### その他の注目すべきインシデント

*   **CISA、Grafanaの脆弱性をKEVカタログに追加**: 米国サイバーセキュリティ・インフラセキュリティ庁（CISA）は、Grafanaの重大なディレクトリトラバーサル脆弱性（CVE-2021-43798）を既知の悪用されている脆弱性（KEV）カタログに追加しました[8]。
*   **大学を狙う給与詐欺**: 「Storm-2657」と呼ばれるハッカーグループが米国の大学を標的とし、従業員の給与口座を乗っ取ろうとしています。少なくとも3つの大学で11の口座が侵害され、25の大学の約6,000人の受信者にフィッシングメールが送信されました[9]。
*   **ChatGPTを介したデータ漏洩**: 企業従業員の18%が生成AIツールにデータを貼り付けており、その50%以上が企業情報を含んでいることが報告されています。特に、オンラインLLMアクセスの77%がChatGPTであり、企業ユーザーの43%がChatGPTのみを利用しているとのことです[10]。
*   **Autodesk Revitプラグインのサプライチェーン脆弱性**: Axis Plugin for Autodesk Revitにサプライチェーンの脆弱性が発見されました。ハードコードされたAzureストレージアカウントの認証情報が署名済みDLLに埋め込まれており、クラウドホスト型MSIインストーラーやRFAファイルへの不正アクセスを可能にしていました[11]。
*   **正規ツールの悪用**: 脅威アクターは、VelociraptorやNezhaといった正規のオープンソースツールを悪用し、永続性の維持、データ窃取、ランサムウェアやRATの展開を行っています[12]。
*   **SRPへの二重ランサムウェア攻撃**: 北米の主要な商品流通業者であるStrategic Retail Partners（SRP）は、2025年2月にMedusaグループによるランサムウェア攻撃を受け、機密性の高い個人データが漏洩しました。同社は二度攻撃を受けたとされています[13]。

## 深掘り

### 日本のサイバーセキュリティ法制の強化

アサヒグループへのサイバー攻撃は、日本が直面するサイバー脅威の深刻さを改めて浮き彫りにしました。日本政府は、サイバーセキュリティ能力の向上に継続的に取り組んでおり、2025年5月には画期的な「能動的サイバー防御法（Active Cyber Defense Law）」を可決しました[2][14]。この法律は、国家的なサイバー攻撃の脅威が高まる中、日本のサイバー安全保障を強化するための重要な一歩とされています[15]。

能動的サイバー防御法は、法執行機関内に専門の担当官を配置し、悪意のあるサイバー脅威を積極的に阻止する権限を与えています。これには、攻撃者のサーバーを無力化するための独自の攻撃を行う権限も含まれます[16]。この法律は、政府が企業とより多くの情報を共有し、警察や自衛隊が攻撃者のサーバーを無力化するための攻撃を行うことを可能にするため、専門家から高く評価されています[2]。

しかし、この法律が制定されたにもかかわらず、日本はレガシーシステムへの依存や、ビジネスソフトウェアに関するデジタルリテラシーの低さ、サイバーセキュリティ専門家の不足といった課題を抱えており、サイバー攻撃に対して脆弱であると指摘されています[2]。

#### 用語解説

*   **ランサムウェア**: 標的のコンピュータシステムへのアクセスを制限したり、ファイルを暗号化したりすることで、身代金（Ransom）を要求するマルウェアの一種です。身代金が支払われるまで、システムやデータは利用できなくなります。
*   **Qilin**: 2022年から活動が確認されているロシア系のサイバー犯罪組織で、RaaS（Ransomware-as-a-Service）モデルで運営されています。攻撃ツールやインフラをハッカーに提供し、収益の一部を手数料として受け取ります。米国、カナダ、英国を中心に幅広い業界を標的とし、大規模な業務妨害とデータ公開を特徴としています[1]。
*   **能動的サイバー防御（Active Cyber Defense）**: 従来の受動的な防御策（侵入防止、検知など）に加え、攻撃元への逆探知や攻撃の無力化など、より積極的な手段を用いてサイバー攻撃に対処する概念です。日本の新法は、このアプローチを法的に可能にするものです。
*   **CISO (Chief Information Security Officer)**: 企業の最高情報セキュリティ責任者。情報セキュリティ戦略の策定、実施、監督を担当します。
*   **KEV (Known Exploited Vulnerabilities) カタログ**: 米国CISAが公開している、実際に悪用されていることが確認された脆弱性のリスト。このリストに含まれる脆弱性は、政府機関に対して迅速な対応が求められます。

#### 今後の展望

サイバー攻撃は、国家レベルの脅威から企業、個人に至るまで、その範囲と巧妙さを増しています。アサヒグループへの攻撃事例は、サプライチェーン全体に及ぶ影響と、事業継続計画におけるサイバーレジリエンスの重要性を示しています。日本の能動的サイバー防御法の施行は、国家としての防御能力を高める一歩ですが、企業レベルでは引き続き、従業員のセキュリティ意識向上、最新の脅威インテリジェンスの活用、そして多層的な防御策の導入が不可欠です。特に、生成AIの利用が広がる中で、新たな攻撃経路への対策も急務となります。

## 結論

過去24時間で報告されたサイバーセキュリティニュースは、ランサムウェア攻撃の継続的な脅威、国家主導のサイバー犯罪の拡大、そしてAI技術の悪用といった多岐にわたる課題を浮き彫りにしています。日本国内では、大手企業への攻撃とCISOの危機意識の高まりが見られ、政府は法整備を進めていますが、組織全体でのセキュリティ対策の強化が喫緊の課題です。国際的には、北朝鮮のサイバー活動の活発化や、AIチャットボットを悪用した新たな攻撃手法の出現が注目されます。これらの動向は、企業や個人が常に最新の脅威情報を把握し、適切な防御策を講じることの重要性を示唆しています。

## 主要引用

*   [1] アサヒに襲ったサイバー攻撃　ランサムウェア被害と身代金の現実. Infoseekニュース. (2025年10月11日). [https://news.infoseek.co.jp/article/itmedia_bizmakoto_20251011004/](https://news.infoseek.co.jp/article/itmedia_bizmakoto_20251011004/)
*   [2] How hackers forced brewing giant Asahi back to pen and paper. BBC News. (2025年10月11日). [https://www.bbc.com/news/articles/cly64g5y744o](https://www.bbc.com/news/articles/cly64g5y744o)
*   [3] 日本のCISOの69％が今後1年以内に重大なサイバー攻撃を受けると予想：日本のCISOが経験した情報漏えいの約9割に「退職した従業員」が関与. ITmedia Keywords. (2025年9月16日). [https://www.itmedia.co.jp/keywords/compromise.html](https://www.itmedia.co.jp/keywords/compromise.html)
*   [4] North Korean hackers stole over $2 billion in crypto this year. Cyware. (2025年10月11日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [5] North Korean Scammers Are Doing Architectural Design Now. Cyware. (2025年10月11日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [6] North Korea IT worker scheme swells beyond US companies. Cyware. (2025年10月11日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [7] AI Chatbots Used as Backdoors in New Cyberattacks. Cyware. (2025年10月11日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [8] U.S. CISA adds Grafana flaw to its Known Exploited Vulnerabilities catalog. Cyware. (2025年10月11日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [9] 'Payroll pirate' hackers diverting salary payments from university employees, Microsoft says. Cyware. (2025年10月10日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [10] 77% of Employees Leak Data via ChatGPT, Report Finds. Cyware. (2025年10月10日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [11] A Cascade of Insecure Architectures: Axis Plugin Design Flaw Expose Select Autodesk Revit Users to Supply Chain Risk. Cyware. (2025年10月10日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [12] Legit tools, illicit uses: Velociraptor, Nezha turned against victims. Cyware. (2025年10月10日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [13] Ransomware gang says it hacked merchandise distributor SRP not once, but twice. Cyware. (2025年10月10日). [https://social.cyware.com/cyber-security-news-articles](https://social.cyware.com/cyber-security-news-articles)
*   [14] Japan's new Active Cyber Defense Law: A Strategic Evolution in National Cybersecurity. Center for Cybersecurity Policy. (2025年6月5日). [https://www.centerforcybersecuritypolicy.org/insights-and-research/japans-new-active-cyber-defense-law-a-strategic-evolution-in-national-cybersecurity](https://www.centerforcybersecuritypolicy.org/insights-and-research/japans-new-active-cyber-defense-law-a-strategic-evolution-in-national-cybersecurity)
*   [15] サイバー対処能力強化法は、2025年5月に成立・公布されたサイバーセキュリティ関連法です。. 東京都サイバーセキュリティ対策. [https://cybersecurity-taisaku.metro.tokyo.jp/know_more/government_initiatives/](https://cybersecurity-taisaku.metro.tokyo.jp/know_more/government_initiatives/)
*   [16] Japan's Active Cyber Defense Law: AEV & Resilience. SafeBreach. (2025年6月12日). [https://www.safebreach.com/blog/japan-active-cyber-defense-law/](https://www.safebreach.com/blog/japan-active-cyber-defense-law/)
