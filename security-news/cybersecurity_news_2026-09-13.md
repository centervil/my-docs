#  2026年9月13日  サイバーセキュリティニュースまとめ

## 主要ポイント
*  **パスキー設定更新を装うソーシャルエンジニアリングとクラウド環境侵害の急増**：ITヘルプデスクを騙るVishingやAitMフィッシングにより、Microsoft 365クラウドの権限や多要素認証（MFA）が迂回され、Graph API経由での大量データ窃取が発生しています。
*  **ChromeとWindowsのゼロデイを連鎖させる「BlueMoon」エクスプロイトキットの拡散**：Chrome V8エンジンの2つのゼロデイ（CVE-2026-85046, CVE-2026-87491）とWindows ALPCの特権昇格ゼロデイ（CVE-2026-85880）を組み合わせ、SYSTEM権限でのバックドア展開を行う攻撃が東アジア背景の複数の脅威アクターへ急速に広がっています。
*  **GitLabにおけるCVSS 10.0の致命的パストラバーサル脆弱性（CVE-2026-85706）の野生悪用**：リポジトリのcommits APIにおける不備を突き、未認証で任意のファイルや設定・認証情報を読み取れる脆弱性が公開直後からアクティブに探索・悪用され、米CISAがKEVカタログに追加しました。

##  クラウドアイデンティティとソーシャルエンジニアリング脅威
ITヘルプデスクを偽装した電話やSMSを起点に、パスキーやSSOの設定更新を口実として偽サイトへ誘導し、AitM（Adversary-in-the-Middle）やデバイスコード認証フローを悪用してMicrosoftクラウドのアクセス権限を強奪するキャンペーンが猛威を振るっています。攻撃者は侵入後、攻撃者管理の電話番号や認証アプリを新たなMFA手法として追加登録することで持続的なアクセス（永続化）を確立し、Graph APIやSharePoint、OneDrive、Exchange Onlineから機密データを長期にわたり抽出します。

##  ブラウザ・OSゼロデイの連鎖と高度サイバースパイ活動
Google ChromeのV8エンジンに存在する2つの未パッチゼロデイ脆弱性（CVE-2026-85046, CVE-2026-87491）でブラウザサンドボックスを回避し、Windows ALPCの特権昇格ゼロデイ（CVE-2026-85880）を連続実行してSYSTEM特権を獲得する「BlueMoon」エクスプロイトキットが確認されました。中国背景の「Violet Typhoon」（APT31）をはじめ、UNK_LateNight、UNK_DoubleCheck、UNK_QuietRacketなどの複数のスパイグループが航空宇宙、製造、金融、政府機関を標的に短期間で広範囲に投入しています。

##  ソフトウェアサプライチェーンおよび開発プラットフォームの脆弱性
GitLab Community/Enterprise Editionのリポジトリcommits APIに存在する、パス閉じ込め不備および認証不備の脆弱性（CVE-2026-85706、CVSS 10.0）が公表されました。攻撃者は未認証の状態で任意のシステムファイルやログ、環境設定ファイルを読み取ることが可能であり、公開後数時間で世界的な探索・攻撃活動が開始され、CISAも連邦機関に対して迅速な修正を命じています。

---

#  2026年9月14日  サイバーセキュリティニュース詳細

## ニュース紹介
### 1.  パスキー誘導フィッシングとMicrosoftクラウド環境への不正侵入・データ強奪
Microsoftは、第三者のメールインフラやパスキーをテーマとしたソーシャルエンジニアリングを悪用し、企業クラウド環境へ侵入してデータを窃取する2つの大規模キャンペーンの詳細を公開しました。
*   **事象と手口**：攻撃者はターゲット企業のITヘルプデスクを装って個人の携帯電話に連絡（Vishing）し、アクセス中断を防ぐためにパスキーやSSO、MFAの設定を即時更新するよう誘導します。被害者が誘導された偽ポータル（`secure-passkey.com`など）でデバイスコード認証やAitMフローを実行させられると、アカウントの制御権が奪取されます。
*   **侵入後の影響**：攻撃者は侵入後、自管理の電話番号や認証アプリを新たなMFA手法として登録して永続化（Persistence）を確立します。その後、Graph APIを利用してテナント内のユーザーやアクセス権限を偵察し、SharePoint Online、OneDrive for Business、Exchange Onlineから数時間から数日間にわたり大量の機密ファイルを流出させます。本活動にはStorm-3032（UNC6671/Helix）やStorm-3121（ShinyHunters）などのグループの関与が確認されています。
$$出典: The Hacker News - Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data$$ (https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html)

### 2.  ChromeとWindowsのゼロデイを連鎖させる「BlueMoon」エクスプロイトキットの拡散
複数のサイバースパイグループが、Google ChromeおよびWindowsの未パッチゼロデイ脆弱性を3つ連鎖させた新しいエクスプロイトキット「BlueMoon」を急速に配備・悪用していることが判明しました。
*   **技術的メカニズム**：攻撃はまず、Google ChromeのV8エンジンにおける2つのゼロデイ脆弱性（CVE-2026-85046、CVE-2026-87491）を悪用してブラウザのサンドボックスを脱出し、ホスト環境を識別します。続いて、Windows Advanced Local Procedure Call (ALPC) の特権昇格ゼロデイ（CVE-2026-85880）を実行してSYSTEM特権を獲得し、親のChromeブローカープロセスにスタブを注入して`curl`コマンド等で外部から実行ファイルをダウンロード・実行させます。
*   **標的と背景**：2026年8月28日に中国背景の「Violet Typhoon」（APT31）が米国NGOや商品取引企業に対して最初に使用したのを皮切りに、数日内にUNK_LateNight（米国航空宇宙企業標的）、UNK_DoubleCheck（ベトナム製造業標的）、UNK_QuietRacket（インドネシア・シンガポール政府・金融標的）などの独立したグループへ急速に拡散しました。開発物からは生成AIを用いて攻撃コードやローディング機構が構築された可能性も指摘されています。
$$出典: SecurityWeek - BlueMoon Exploit Kit Chains Recent Chrome, Windows Zero-Days$$ (https://www.securityweek.com/bluemoon-exploit-kit-chains-recent-chrome-windows-zero-days/)

### 3.  GitLabにおけるCVSS 10.0最高深刻度のファイル読み取り脆弱性（CVE-2026-85706）と野生での攻撃
GitLabは、Community Edition（CE）およびEnterprise Edition（EE）において、最高深刻度（CVSS 10.0）のパストラバーサル脆弱性「CVE-2026-85706」を含む複数の不備を修正する緊急パッチ（19.3.2、19.2.6、19.1.8）を公開しました。
*   **影響と危険性**：本脆弱性は、リポジトリのcommits APIにおける適切なパス閉じ込め不備および認証強制の欠如に起因します。パブリックプロジェクトが少なくとも1つ存在する環境において、未認証の外部アクターがGitLabサーバー上のログファイルや設定ファイル、CI/CDシークレット、認証情報を任意に読み取ることが可能になります。
*   **野生での悪用状況**：公開からわずか数時間（2026年9月11日 06:00 UTC頃）で実際の攻撃や探索活動が観測されており、米CISAも即座にKEV（悪用が確認された脆弱性）カタログに追加して連邦機関に対策を指示しました。
$$出典: The Hacker News - GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure$$ (https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html)

## 深掘り
###  パスワードレス移行期を突く「アイデンティティ侵害」とMFA永続化の手法

####  1. Vishingとデバイスコード認証・AitMによる認証突破の機序
組織がパスワードレス認証やパスキー（Passkey）への移行を進める中、攻撃者はパスワードそのものを盗むのではなく、人間の心理的隙（ソーシャルエンジニアリング）と認証プロセスの隙を突く方向へと手法を変化させています。
*   **ソーシャルエンジニアリングと事前調査（OSINT）**：
    UNC6671等のグループは、LinkedInなどの公開プロファイリングプラットフォームを通じて標的組織のエグゼクティブや従業員、組織構造を念入りに事前調査（OSINT）します。その後、個人の携帯電話番号に直接電話をかけ、ITヘルプデスクを名乗って「SSOやパスキーの設定更新が必要」と偽り、`secure-passkey.com` や `oktasession.com` といったターゲット組織名を組み込んだ偽ポータルへ誘導します。
*   **デバイスコード認証およびAitMの悪用**：
    攻撃者はパスワードを入力させる代わりに、デバイスコード認証（Device Code Phishing）やAdversary-in-the-Middle（AitM）プロキシを稼働させます。これにより、被害者が自身の正規デバイス上で表示されたコードを承認したり、セッションを確立したりすると、攻撃者は被害者の認証済みトークンやアクセス権限を丸ごと横取りすることができます。

####  2. 攻撃者制御のMFA追加による「永続化（Persistence）」とGraph APIの悪用
初期侵入を果たした攻撃者が最も優先するのは、一時的な侵入状態を持続的なアクセス権限（永続化）へと変換することです。
*   **MFA手法の不正追加**：
    攻撃者は被害者本人の介在なしにサインインを継続するため、即座に自らが制御する電話番号、認証アプリ（Authenticator）、またはソフトウェアベースのOTPトークンをターゲットアカウントの新しいMFA認証手法として追加登録します。これにより、正規ユーザーのセッションが切断された場合でも、自らのMFA手法を用いて何度でも企業アカウントへ直接ログインが可能となります。
*   **Microsoft Graph APIを用いた不可視の内部偵察と一括抽出**：
    一単体のAPI呼出としては正規の動作に見える Microsoft Graph API を悪用し、テナント内の全ユーザー、グループ、アクセス権限、所有コンテンツを一括で列挙（偵察）します。さらに、セキュリティ検知を回避するために認証用、偵察用、データ抽出用で別々のIPアドレスや住宅用プロキシ（Residential Proxy）を使い分け、数時間から数日間にわたってSharePointやOneDrive、Exchange Onlineから静かに大量の機密データを強奪します。

###  関連知識
####  用語解説
*   **デバイスコード認証フィッシング (Device Code Phishing)**：
    OAuth 2.0のデバイス認可フロー（Device Authorization Grant）を悪用した攻撃手法。スマートTVなど入力画面が限られたデバイス用の認可手順を逆用し、攻撃者が発行したデバイスコードを被害者に自身のPC/スマホの正規ログイン画面で入力・承認させることで、被害者のセッション資格情報を奪取する。
*   **Microsoft Graph API**：
    Microsoft 365の各種サービス（ユーザー、メール、OneDrive、SharePoint、Teams等）のデータや機能にプログラムから単一のエンドポイントでアクセスするためのRESTful Web API。単一のAPI呼出は正常な業務通信と区別がつきにくいため、攻撃者による広範囲な内部偵察やデータ一括ダウンロードに悪用される。
*   **AMTD (Automated Moving Target Defense / 自動移動目標防御)**：
    システムやブラウザのエントリポイント、メモリ配置、ネットワークルーティング、API構造を動的かつ自動的に変更し続ける技術。BlueMoonのような高度なゼロデイ連鎖攻撃に対して、攻撃者が標的のメモリ位置や脆弱性を特定することを困難にする次世代防御アプローチ。

####  今後の展望
*   **Graph API通信の動作相関（Cross-Event Correlation）による監視強化**：
    Microsoftが指摘する通り、単一のGraph API要求単体では不審な動作として検知できません。今後は、サインインイベント、MFA手法の新規追加、および短時間での大量データ取得アクションを統合・高度に相関分析する行動分析エンジン（SIEM/XDR）の配備が不可欠となります。
*   **ハードウェアバインド型MFA（FIDO2 / パスキー）の厳格な実装と端末制限**：
    電話番号やOTPアプリによるMFAは攻撃者によって容易に追加登録・迂回されるリスクが示されたため、今後はMFA認証情報そのものを端末の物理セキュリティチップ（TPM）にバインドするFIDO2/パスキーの導入、および未管理デバイスからのアクセスを厳格にブロックする条件付きアクセスポリシーの全面適用が求められます。

## 結論
2026年9月現在に顕在化したサイバー脅威は、企業の正面防壁を突破する攻撃だけでなく、ITヘルプデスクを装った精巧なソーシャルエンジニアリング（パスキー・MFAテーマ）による「アイデンティティの強奪」や、公開後数時間で悪用されるゼロデイ連鎖（BlueMoon）や開発基盤のクリティカル脆弱性（GitLab）など、多層的な「信頼の死角」を突く攻撃が常態化している実態を示しています。
企業や行政組織は、単一のパスワードや従来のMFAに頼る防御モデルから脱却し、侵入を前提（Assume Breach）とした厳格なネットワークセグメンテーション、未管理端末の排除、MFA追加やGraph API利用に対するリアルタイムな動的監視、および不変（Immutable）バックアップによるレジリエンス体制の確立を急ぐことが極めて決定的な教訓となります。

## 主要引用
*  **「Rather than relying solely on stolen credentials, the actor enrolled an MFA method under their control, typically by registering a new phone number, authenticator application, or software-based one-time password (OTP) token.」** — Microsoft Security Research Team（パスキー・MFA誘導フィッシングに関する分析報告より）
*  **「BlueMoon was developed, deployed rapidly, and shared across multiple threat actors within days in a manner that had high detection signals. This may reflect a reduced cost and barrier to entry for this class of capability, as AI agents increasingly enable threat actor exploit development.」** — Proofpoint 脅威インテリジェンスチーム（BlueMoonエクスプロイトキットに関する分析報告より）
*  **「The appeal to attackers of GitLab is obvious, as unauthorized access allows an attacker to gain access to source code, CI/CD secrets, credentials, and the ability to inject code into build pipelines, gaining access or poisoning anything downstream of it...」** — Jake Knott (watchTowr Head of Threat Intelligence, on GitLab CVE-2026-85706)
