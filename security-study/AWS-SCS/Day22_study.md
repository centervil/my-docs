## 📚 今日の学習テーマ：Systems Manager (SSM) によるセキュアな運用

### 📝 学習の目標

* Session Managerを活用し、SSH不要かつ監査ログ取得可能なセキュアなリモートアクセス環境を構築できる。
* Patch Managerを用いたOSパッチ管理の自動化と、コンプライアンス評価の手法を理解する。
* Parameter Storeを利用した機密情報や設定値の安全な管理方法を習得する。

### 🔍 カバーする範囲

AWS Systems Manager (SSM) の主要機能であるSession Manager、Patch Manager、Parameter Storeを中心に、インフラストラクチャの運用効率化とセキュリティ強化の手法を学習します。

## 📖 解説パート

### Session Managerによるセキュアな管理

Session Managerは、SSHキーの管理や踏み台サーバー（Bastion Host）を必要とせずに、ブラウザやAWS CLIからEC2インスタンスへ安全に接続できる機能です。従来、SSH接続には「22番ポートの開放」や「秘密鍵の配布・管理」といったセキュリティリスクが伴いましたが、Session Managerを利用することで、これらを排除できます。

接続はIAM権限によって制御されるため、最小権限の原則に基づいたアクセス管理が可能です。また、操作ログをS3バケットやCloudWatch Logsへ自動的に転送できるため、誰がいつどのような操作を行ったかという監査証跡を確実に保存できます。これにより、インシデント発生時の調査やコンプライアンス要件の充足が容易になります。

### Patch ManagerとParameter Storeの活用

Patch Managerは、OSのパッチ適用を自動化する機能です。パッチベースラインを定義することで、承認済みのパッチのみを対象に自動適用を実行し、コンプライアンス評価を行うことができます。手動操作によるミスを減らし、脆弱性への対応時間を大幅に短縮可能です。

一方、Parameter Storeは、設定値や機密情報（APIキーやDBパスワードなど）を階層構造で管理するサービスです。KMS（Key Management Service）と連携して値を暗号化できるため、環境変数やコード内に機密情報をハードコードするリスクを防ぎます。アプリケーション側は、SSMのAPI経由で値を呼び出すだけで済むため、安全かつ柔軟な構成管理が実現します。

#### 重要ポイント

* Session Managerはインバウンドポート（22番）の開放が不要であり、攻撃対象領域を最小化できる。
* Patch Managerの活用により、パッチ適用状況の可視化と自動的なコンプライアンス維持が可能になる。
* Parameter StoreはKMSと連携することで、機密情報の安全な保管と動的な参照を実現する。

## 🏢 ケースステディ

### ケース：踏み台サーバーの廃止とSession Managerへの移行

多くの企業では、プライベートサブネット内のEC2に接続するために踏み台サーバーを運用していますが、そのメンテナンスやセキュリティパッチ適用が運用負荷となっています。また、踏み台サーバー自体が攻撃の標的となり得るリスクを抱えています。

#### 問題点

* 踏み台サーバーのOSパッチ管理やセキュリティ更新に多大なコストがかかる。
* SSH鍵の紛失や盗難、あるいは鍵のローテーション漏れによる不正アクセスのリスク。
* 踏み台を経由した操作ログの追跡が複雑で、監査が困難な場合がある。

#### 対応策

* 踏み台サーバーのインスタンスを停止・削除し、SSMエージェントを導入した対象インスタンスへ直接接続する構成へ切り替える。
* IAMポリシーでSession Managerへのアクセスを制限し、MFA（多要素認証）を必須化する。
* 操作ログをS3またはCloudWatch Logsへ転送し、定期的な監査を行う設定を有効化する。

#### ケースから学ぶ教訓

* マネージドサービスを活用することで、インフラ運用に伴う「管理対象」そのものを減らすことが最大のセキュリティ対策となる。
* 認証の仕組みを個別のサーバーからIAMへ集約することで、権限管理を一元化し、セキュリティレベルを向上させることができる。

## 📋 今日のまとめ

* Session Managerにより、SSH不要のセキュアなリモートアクセスと詳細な操作ログ取得を実現する。
* Patch Managerを用いて、パッチ適用の自動化とコンプライアンス維持を効率化する。
* Parameter StoreとKMSを組み合わせ、機密情報を安全に管理する運用体制を構築する。

### 次回予告

明日は「データ保護と暗号化（KMS、ACMなど）」について学習します。

## 📚 参考資料・リソース

* [AWS Systems Manager ユーザーガイド](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/)
* [AWS Systems Manager Session Manager の概要](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/session-manager.html)
* [AWS Systems Manager Patch Manager を使用したパッチ適用](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/systems-manager-patch.html)