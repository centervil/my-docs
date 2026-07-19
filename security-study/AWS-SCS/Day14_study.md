## 📚 今日の学習テーマ：Amazon CloudWatch と VPC Flow Logs によるモニタリング

### 📝 学習の目標

* CloudWatch Logs Insights を活用し、ログから異常なAPIコールパターンを効率的に抽出・分析できる。
* VPC Flow Logs の構造を理解し、トラフィックの拒否・許可のログからセキュリティ上の脅威を特定できる。
* セキュリティインシデント（SSH総当たり攻撃など）を想定したログ分析フィルターを設計できる。

### 🔍 カバーする範囲

本日は、AWS環境における可視性の確保に焦点を当てます。CloudWatch Logs Insights を用いたログ分析の手法と、VPC Flow Logs を活用したネットワークトラフィックの監視・分析手法について学習します。

## 📖 解説パート

### CloudWatch Logs Insights による異常検知

CloudWatch Logs Insights は、CloudWatch Logs に集約されたログデータに対して高速かつ柔軟なクエリを実行できる強力な分析ツールです。特に、AWS CloudTrail のログと組み合わせることで、特定のAPIコールパターンから不正アクセスや設定変更の兆候を早期に発見することが可能です。

分析を行う際は、まず「どのような条件で異常を定義するか」を明確にします。例えば、特定のIAMユーザーによる短時間での大量のアクセス拒否（AccessDenied）や、通常利用されないリージョンからの API 呼び出しを抽出するクエリを設計します。`filter` コマンドで対象を絞り込み、`stats` コマンドで集計を行うことで、異常なパターンを可視化します。これにより、インシデント対応の初動を迅速化し、セキュリティの継続的な監視体制を構築できます。

### VPC Flow Logs によるネットワーク分析

VPC Flow Logs は、VPC 内のネットワークインターフェイスを通過する IP トラフィックをキャプチャする機能です。セキュリティ分析においては、各ログレコードに含まれる `srcaddr`（送信元IP）、`dstport`（送信先ポート）、`protocol`、そして `action`（ACCEPT/REJECT）が重要な判断材料となります。

特に `REJECT` されたトラフィックは、セキュリティグループやネットワーク ACL によってブロックされた通信を指し、攻撃者による偵察活動（ポートスキャンなど）の証拠となることが多々あります。また、`ACCEPT` されたトラフィックであっても、通常想定されない時間帯や異常な通信量がある場合は注意が必要です。VPC Flow Logs を CloudWatch Logs や S3 に転送し、Athena 等で分析することで、広範囲のネットワーク脅威を可視化できます。

#### 重要ポイント

* CloudWatch Logs Insights は、大規模なログデータから特定のイベントを高速に抽出・集計するために必須のツールである。
* VPC Flow Logs の `action` フィールド（REJECT）を監視することで、未承認のアクセス試行を早期に発見できる。
* ログの分析には、時間軸に基づいたフィルタリングと、送信元・送信先IPの相関分析が非常に有効である。

## 🏢 ケーススタディ

### ケース：EC2に対するSSH総当たり攻撃（Brute Force）

ある夜間、パブリックサブネットに配置されたEC2インスタンスに対し、未知のIPアドレス群から短時間に大量のSSH接続試行が行われました。セキュリティグループの設定により、多くの試行が拒否されていましたが、システムログには膨大な認証失敗が記録されており、攻撃者がポートの開放を狙っていることが判明しました。

#### 問題点

* SSHポート（22番）が広範囲のIPに対して公開されており、攻撃の標的になりやすい。
* 認証失敗が多発しても、リアルタイムでアラートが通知される仕組みが構築されていなかった。
* 攻撃者のIPアドレスを特定し、自動的にブロックする動的な防御が機能していなかった。

#### 対応策

* SSH接続を特定のIPアドレス範囲からのみに制限する（または踏み台サーバー経由に変更する）。
* VPC Flow Logs を有効化し、`dstport=22` かつ `action=REJECT` のログを監視する。
* Amazon GuardDuty を有効にし、SSH総当たり攻撃を自動検知してアラートを飛ばす設定を行う。
* AWS WAF や AWS Network Firewall を活用し、悪意のあるIPを自動的にブロックする。

#### ケースから学ぶ教訓

* ネットワークの「拒否」ログは、攻撃の前兆を把握するための重要なシグナルである。
* 境界防御だけでなく、ログによる監視とアラートの自動化を組み合わせることで、多層防御を完成させる。
* 「いつ、どこから、どのような通信が拒否されたか」を常に追跡できる状態を維持する。

## 📋 今日のまとめ

* CloudWatch Logs Insights を用いて、膨大なログから特定の異常APIパターンをクエリで抽出する方法を学んだ。
* VPC Flow Logs の各フィールド（アクション、ポート、IP）がセキュリティ分析にどのように役立つかを理解した。
* SSH総当たり攻撃などの脅威に対し、ログのフィルタリングと監視が有効な防御策であることを確認した。

### 次回予告

明日は「AWS Systems Manager によるインフラの自動管理とパッチ適用」について学習します。

## 📚 参考資料・リソース

* [CloudWatch Logs Insights クエリ構文のガイド](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)
* [VPC Flow Logs のログレコードの形式](https://docs.aws.amazon.com/ja_jp/vpc/latest/userguide/flow-logs.html#flow-logs-records)
* [AWS セキュリティモニタリングのベストプラクティス](https://docs.aws.amazon.com/ja_jp/whitepapers/latest/aws-security-incident-response-guide/monitoring-and-logging.html)