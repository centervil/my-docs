# my-docs

セキュリティドキュメント管理、調査、およびプロジェクト管理のための中心リポジトリ。
AIエージェント主導の開発プロセス（IDD）と、`private-ops` サブモジュールによる自動化パイプラインを統合しています。

## 🚀 プロジェクトの目的
- **セキュリティ情報の集約**: 日々のニュース (`security-news/`) や体系的な学習資料 (`security-study/`) の管理。
- **調査・仕様の蓄積**: 技術調査 (`docs/research/`) およびシステム設計 (`docs/specs/`) の永続化。
- **AI主導開発の推進**: Issue駆動開発 (IDD) に基づく自律的なドキュメント・システム運用。

## 📂 ディレクトリ構造
- `.gemini/`: Gemini CLI 設定および独自スキル (`skills/`)。
- `docs/`: コアドキュメント群。
    - `issues/`: Issueごとのワークスペース。設計、タスク管理、作業ログ。
    - `research/`: 技術調査資料、開発ガイドライン (`development_process_guide.md` 等)。
    - `specs/`: プロジェクト・システムの仕様書。
- `private-ops/`: (Submodule) 自動化スクリプト、CI/CD 構成、プライベートツール群。
- `security-news/`: 自動収集されたサイバーセキュリティニュースのアーカイブ。
- `security-study/`: 構造化されたセキュリティ学習ノート。
- `prompts/`: AIエージェント用の指示テンプレート。
- `templates/`: ドキュメント作成用の標準テンプレート。

## 🛠 運用プロトコル
本リポジトリでは、以下のガイドラインに従って開発・運用を行います。

| カテゴリ | ガイドラインファイル | 概要 |
| :--- | :--- | :--- |
| **開発プロセス** | `docs/research/development_process_guide.md` | AI主導のIDD/TDDサイクルとPMレビュー。 |
| **セキュリティ** | `docs/research/devsecops_guide.md` | 安全なコーディングと運用の原則。 |
| **プロジェクト管理** | `docs/research/project_management_guide.md` | Issue/PRの管理基準。 |
| **エージェント原則** | `AGENTS.md` | 本リポジトリにおけるAIエージェントの基本憲章。 |

## 🏁 はじめに
1. `gh issue list` で現在のタスクを確認する。
2. `/help` を実行して、利用可能なスラッシュコマンドやスキルを確認する。
3. `docs/research/development_process_guide.md` を読み、開発フローを理解する。
