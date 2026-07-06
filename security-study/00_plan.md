# AWS-SCS (AWS Certified Security - Specialty) 30日間学習計画
## ～AWSセキュリティの実務スペシャリストとして、クラウドを守る思考と技術を30日で体得する～

本計画は、AWS Certified Security - Specialty（SCS-C02）試験の出題ドメイン（脅威の検出と対応、セキュリティロギングとモニタリング、インフラストラクチャのセキュリティ、IAMと権限管理、データ保護と暗号化）を網羅します。単なるサービス知識の暗記ではなく、「攻撃者の思考を理解したうえで防御設計する」という実務視点を重視します。

<course_context>
AWS-SCSの学習は、以下の5つのドメインを軸に構成されています。
1. 脅威の検出と対応 (Threat Detection and Incident Response): GuardDuty, Security Hub, Detective, Macieによる脅威の自動検出と、インシデント対応プレイブックの設計。
2. セキュリティロギングとモニタリング (Security Logging and Monitoring): CloudTrail, CloudWatch, AWS Config, VPC Flow Logsによる可視性の確保と監査証跡の管理。
3. インフラストラクチャのセキュリティ (Infrastructure Security): VPC設計、Security Groups/NACLs、AWS WAF/Shield/Firewall Manager、Systems Managerによる多層防御。
4. IAMと権限管理 (Identity and Access Management): IAM Policy、SCPs、Permission Boundaries、IAM Identity Center、Resource-based Policyによる最小権限の実現。
5. データ保護と暗号化 (Data Protection): KMS、CloudHSM、Secrets Manager、ACM、S3暗号化によるデータの機密性・完全性保証。
</course_context>

<day_plans>
<day n="1">
テーマ: AWS責任共有モデルとセキュリティの全体像
内容:
- AWSとユーザーの責任範囲の境界を理解する。IaaS/PaaS/SaaSでの責任の変化。
- Well-Architected Framework「セキュリティの柱」の7つの設計原則を精読する。
- 思考タスク: 自組織のAWS環境を「誰が何を守る責任があるか」のマトリクスで整理する。
</day>

<day n="2">
テーマ: IAMの基礎 - ポリシーの構造と評価論理
内容:
- IAMポリシーのJSON構造（Effect, Action, Resource, Condition）を深く理解する。
- ポリシー評価ロジック（明示的Deny → SCP → Resource-based → Identity-based の優先順位）を習得する。
- 実践: IAM Policy Simulatorで意図した権限が付与されているか既存ロールを検証する。
</day>

<day n="3">
テーマ: IAMの応用 - 最小権限と危険なポリシーパターン
内容:
- `*:*`リソースの危険性、PassRole、AssumeRole、iam:Createのリスク。
- Permission Boundaries（アクセス許可境界）でデリゲートされた管理の安全なパターン。
- 思考タスク: 自組織の開発者ロールに付与されている権限を監査し、削除できるアクションを5つ特定する。
</day>

<day n="4">
テーマ: AWS Organizations とサービスコントロールポリシー (SCP)
内容:
- 組織単位（OU）の設計とアカウント分離戦略（本番/開発/セキュリティアカウント）。
- SCPによるガードレール設定（例: 特定リージョンのみ許可、S3パブリック公開禁止）。
- 実践: 「東京リージョン以外へのリソース作成を禁止するSCP」をJSONで設計する。
</day>

<day n="5">
テーマ: IAM Identity Center (旧SSO) とフェデレーション
内容:
- IdP（Okta, Active Directory）連携、SAML 2.0/OIDC フェデレーション。
- IAM Identity Centerでの権限セットと多アカウント一元管理のアーキテクチャ。
- 思考タスク: パスワード管理の手間を最小化しつつ、最小権限を維持するSSOアーキテクチャを設計する。
</day>

<day n="6">
テーマ: VPCセキュリティ設計の基礎
内容:
- Public/Private/Isolated サブネット設計。Security GroupsとNACLsの使い分け。
- VPCエンドポイント（ゲートウェイ型、インターフェース型）によるプライベート通信の実現。
- 実践: 「パブリックに公開しないS3バケットへのEC2からのアクセス」をVPCエンドポイントで実現する構成図を描く。
</day>

<day n="7">
テーマ: ネットワーク境界防御 - WAF・Shield・Firewall Manager
内容:
- AWS WAF: WebACL、マネージドルールグループ（Core rule set、SQLi、XSS）、カスタムルールの設計。
- AWS Shield Standard vs. Advanced: DDoS保護のレベルと使いどき。
- 思考タスク: SQLインジェクションとLog4Shell攻撃をWAFで防ぐためのルール優先度を設計する。
</day>

<day n="8">
テーマ: AWS Network Firewall と多層防御アーキテクチャ
内容:
- Network Firewall: ステートフルルールとステートレスルール、Suricata互換のシグネチャ。
- Egress（アウトバウンド）制御の重要性とドメインベースのフィルタリング。
- 実践: 「マルウェアに感染したEC2が外部C&Cサーバーへ通信しようとする」シナリオで、Network Firewallでの遮断ルールを設計する。
</day>

<day n="9">
テーマ: Amazon GuardDuty - 脅威の自動検出
内容:
- GuardDutyのデータソース（CloudTrail、VPC Flow Logs、DNS Logs、EKS、S3、Malware Protection）。
- Finding タイプ（Reconnaissance、Backdoor、CryptoCurrency、UnauthorizedAccess）の読み方。
- 実践: GuardDutyのFindingをEventBridgeでトリガーし、Slackに通知するアーキテクチャを設計する。
</day>

<day n="10">
テーマ: AWS Security Hub - セキュリティ状態の統合管理
内容:
- Security HubのStandard（AWS Foundational Security Best Practices, CIS AWS Benchmark）。
- Findingの集約と自動修復パターン（Lambda連携）。
- 思考タスク: Security HubのFindingを重要度でトリアージし、どのチームがどのFindingに対応するかのRACIを定義する。
</day>

<day n="11">
テーマ: Amazon Detective と Inspector
内容:
- Amazon Detective: GuardDutyのFindingを深掘り調査するための振る舞い分析ツール。
- Amazon Inspector v2: EC2とコンテナのCVE脆弱性スキャン、ECRイメージスキャン。
- 実践: 「不審なAPIコールが検出された」シナリオでDetectiveを使った調査フローをステップバイステップで書き出す。
</day>

<day n="12">
テーマ: Amazon Macie - S3データ保護
内容:
- Macieによる機密データ（PII、個人情報、クレジットカード番号）の自動検出。
- Macieの誤検知への対処と、S3バケットのパブリック公開リスク評価。
- 思考タスク: GDPR・個人情報保護法の観点から、Macieを使って「いつ誰が何のデータを処理しているか」を説明できる仕組みを設計する。
</day>

<day n="13">
テーマ: CloudTrail - 監査証跡の設計
内容:
- Management Events vs. Data Events vs. Insights Events の違いと取得コスト。
- CloudTrail Lake によるクエリと長期保存戦略。証跡への改ざん防止（Log File Validation）。
- 実践: 「S3バケットのオブジェクトを誰がいつ削除したか」をCloudTrail Lakeで特定するAthenaクエリを書く。
</day>

<day n="14">
テーマ: Amazon CloudWatch と VPC Flow Logs によるモニタリング
内容:
- CloudWatch Logs Insights で異常なAPIコールパターンを検出するクエリ設計。
- VPC Flow Logsの読み方（ACCEPT/REJECT、srcaddr、dstport）とセキュリティ分析への活用。
- 思考タスク: 「SSH総当たり攻撃（Brute Force）を受けているEC2」をVPC Flow Logsで検出するためのフィルターを設計する。
</day>

<day n="15">
テーマ: AWS Config - コンプライアンスの継続的評価
内容:
- Config Rules（マネージドルール vs. カスタムルール）による設定の自動チェック。
- Conformance PacksによるCIS/PCI-DSSなどのコンプライアンス基準の一括適用。
- 実践: 「S3バケットのパブリック公開が有効になったら即座にBlockする」自動修復ルールをConfig+Lambda+SSMで設計する。
</day>

<day n="16">
テーマ: AWS KMS - 鍵管理の基礎
内容:
- CMK（AWS managed key vs. Customer managed key）の違いと鍵ポリシー。
- 対称鍵・非対称鍵・HMACキーのユースケース。キーローテーションのベストプラクティス。
- 思考タスク: 「KMSキーの誤削除」を防ぐためのキーポリシー設計と待機削除（Pending deletion）の運用フローを定義する。
</day>

<day n="17">
テーマ: AWS KMS - 高度な暗号化パターン
内容:
- Envelope Encryption（封筒暗号化）の仕組みとData Key Caching。
- Cross-Account KMSキーの共有、Grant による一時的な権限委譲。
- 実践: 「A社アカウントのKMSキーでB社アカウントのS3オブジェクトを暗号化する」クロスアカウント設計を完成させる。
</day>

<day n="18">
テーマ: AWS CloudHSM と Secrets Manager
内容:
- CloudHSM: FIPS 140-2 Level 3準拠の専用HSMが必要なユースケース（金融系署名、PKIルートCA）。
- Secrets Manager: DBパスワードの自動ローテーション、Lambda連携パターン、クロスアカウント共有。
- 思考タスク: ハードコードされたDB接続情報をSecrets Managerに移行する際の「移行計画とリスク」を箇条書きで整理する。
</day>

<day n="19">
テーマ: S3のセキュリティ設計
内容:
- S3バケットポリシー、ACL、Block Public Access設定の優先順位。
- S3サーバー側暗号化（SSE-S3, SSE-KMS, SSE-C）とクライアント側暗号化の選択基準。
- MFA Deleteと Object Lockによるランサムウェア対策。
- 実践: 「本番データが入ったS3バケット」のランサムウェア対策設計を、Object Lock + バージョニング + アクセスログで構成する。
</day>

<day n="20">
テーマ: ACM (AWS Certificate Manager) と PKI
内容:
- パブリック証明書とプライベート証明書の発行・管理・更新の自動化。
- ACM Private CA: プライベートPKIの構築、証明書の失効管理（CRL/OCSP）。
- 思考タスク: マイクロサービス間のmTLS（相互TLS認証）をACM Private CAで実現するアーキテクチャを設計する。
</day>

<day n="21">
テーマ: Amazon Cognito - アプリケーション認証
内容:
- User Pools（認証）vs. Identity Pools（認可）の役割と連携パターン。
- MFAの強制、パスワードポリシー、Advanced Security Features（アダプティブ認証）。
- 実践: 「外部のウェブアプリケーション経由でAWSリソースにアクセスさせる」際のCognito + IAMロールの最小権限設計を行う。
</day>

<day n="22">
テーマ: Systems Manager (SSM) によるセキュアな運用
内容:
- Session Manager: SSH不要のEC2管理、操作ログのS3/CloudWatch送信。
- Patch Manager: OSパッチの自動適用とコンプライアンス評価。SSM Parameter Store: 設定値の安全な管理。
- 思考タスク: 「踏み台サーバー（Bastion Host）を廃止してSession Managerに移行する」際の移行障壁とリスク軽減策を整理する。
</day>

<day n="23">
テーマ: コンテナセキュリティ (ECS/EKS)
内容:
- ECRイメージスキャン（Inspector連携）、Dockerfile のセキュリティベストプラクティス。
- ECSタスクロール vs. EKS IRSAによる最小権限のPod/Task設計。
- 実践: EKSクラスターへの攻撃シナリオ（特権コンテナからのホスト侵害）を分析し、EKS Pod Security Standards での対策を設計する。
</day>

<day n="24">
テーマ: サーバーレスセキュリティ (Lambda/API Gateway)
内容:
- Lambda実行ロールの最小権限、環境変数の暗号化（KMS）、VPC内Lambda のネットワーク設計。
- API GatewayのWAF連携、リソースポリシー、Lambda Authorizerによる認証。
- 思考タスク: 「Lambda関数のコードにAWSアクセスキーがハードコードされていた」インシデントの影響範囲と修復手順をIR計画として書く。
</day>

<day n="25">
テーマ: インシデントレスポンス計画の設計
内容:
- AWSにおけるIR（Incident Response）フレームワーク: 準備→検出→封じ込め→根絶→復旧→教訓。
- EC2の隔離（Security Groupの変更）、スナップショット取得、フォレンジックアカウントへの転送。
- 実践: 「GuardDutyが`Backdoor:EC2/C&CActivity.B`を検出した」シナリオのIRプレイブックを30分以内に対応できる形式で作成する。
</day>

<day n="26">
テーマ: データ流出（Data Exfiltration）対策
内容:
- 典型的なデータ流出経路（S3パブリック公開、ECRイメージへの埋め込み、Lambda環境変数）の理解。
- Macieによる機密データ検出、GuardDutyのS3 Protectionによる異常な大量ダウンロード検出。
- 思考タスク: 「悪意ある内部犯行者（Insider Threat）」がS3からデータを持ち出そうとするシナリオを想定し、検出と防止のコントロールを10個設計する。
</day>

<day n="27">
テーマ: ランサムウェア対策とバックアップ戦略
内容:
- AWS Backup: クロスリージョン・クロスアカウントのバックアップによるランサムウェア耐性。
- Vault Lockによるバックアップへの不変性の付与（WORM: Write Once Read Many）。
- 実践: 「RDSデータベースがランサムウェアで暗号化された」シナリオにおける復旧手順（RTO/RPOを満たす形式）を設計する。
</day>

<day n="28">
テーマ: ペネトレーションテストとセキュリティ評価
内容:
- AWSのペネトレーションテストポリシー（許可されているサービスと事前承認が必要なテスト）。
- AWS Trusted Advisor、Prowler、ScoutSuiteなどのツールを使ったセキュリティ評価の自動化。
- 思考タスク: 四半期ごとのセキュリティレビューで確認すべき「Top 10 AWSセキュリティチェックリスト」を独自に作成する。
</day>

<day n="29">
テーマ: 試験対策 - ドメイン横断のアーキテクチャ問題演習
内容:
- 複数サービスを組み合わせた設計問題（例: 「金融系企業のマルチアカウント・セキュリティアーキテクチャ設計」）への解法パターンを習得する。
- 「最もコスト効率が高い」「最も運用負荷が低い」「最も安全な」選択肢の見極め方を練習する。
- 実践: 過去問または模擬試験を1セット（65問）解き、ミスした設問のサービスをドキュメントで再確認する。
</day>

<day n="30">
テーマ: AWS-SCSスペシャリストとしての実務への還元
内容:
- 30日間の学習を振り返り、自組織のAWS環境に存在する「最大のセキュリティリスクTop 3」を特定する。
- 実践: リスクに対する改善提案を「経営層向けの1ページサマリー」として作成し、コスト・優先度・期待効果を明記する。
</day>
</day_plans>
