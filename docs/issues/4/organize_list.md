# Organize List: 移行・統合対象ディレクトリの整理

## 1. 移行元ディレクトリのステータス

| 元ディレクトリ (Docs) | my-docs での配置 | 備考 |
| :--- | :--- | :--- |
| `dev-records/` | `dev-records/` | 日記等の開発記録。全移行。 |
| `dev-records_old/` | `archive/dev-records_old/` | 過去の記録。アーカイブとして移行。 |
| `prompts/` | `prompts/` | Zenn記事生成プロンプト。統合。 |
| `templates/` | `templates/` | Zenn記事テンプレート。統合。 |
| `tools/` | `tools/` | 各種スクリプト。統合（重複は整理）。 |
| `books/` | `knowledge/books/` | 書籍メモ。整理して移行。 |

| 元ディレクトリ (Docs-Study) | my-docs での配置 | 備考 |
| :--- | :--- | :--- |
| `security-news/` | `security-news/` | 既存の `my-docs/security-news/` と統合。 |
| `security-study/` | `security-study/` | 学習進捗管理。全移行。 |
| `dev-docs/` | `research/` | 調査資料。既存の `my-docs/research/` と統合。 |
| `specification-draft/` | `knowledge/specs/` | 仕様書ドラフト。整理して移行。 |
| `prompts/` | `prompts/` | 学習コンテンツ生成プロンプト。統合。 |
| `templates/` | `templates/` | 学習コンテンツテンプレート。統合。 |
| `Docs-common/tools/` | `tools/` | 重複する `document_processor.py` 等の整理。 |

## 2. 統合・整理方針のポイント

1. **重複排除**: `document_processor.py` は、学習用と日記用で差異があるため、`tools/document_processor_study.py` と `tools/document_processor_diary.py` のようにリネームして配置、または共通化を検討する。
2. **アーカイブ**: `dev-records_old/` 等の古いデータは、ルートディレクトリを汚さないよう `archive/` 以下にまとめる。
3. **新規カテゴリ**: `knowledge/` ディレクトリを新設し、静的な資料（書籍、仕様、調査資料の恒久版）を整理して配置する。
4. **既存 my-docs コンテンツ**: `research/` や `security-news/` は、既存のファイルを壊さないようマージする。

## 3. 次のステップ (Issue #5 移行フェーズ)

- [ ] `my-docs` に新規ディレクトリ (`knowledge/`, `archive/`, `tools/` 等) を作成。
- [ ] 各ディレクトリへのファイルコピー。
- [ ] 相対パス参照が含まれるドキュメント（あれば）の修正。
- [ ] 最終的なディレクトリ構成の整合性チェック。
