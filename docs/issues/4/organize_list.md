# Organize List (Refined): 移行・統合対象ディレクトリの整理

## 1. 移行元ディレクトリのステータス (ユーザーフィードバック反映後)

### 1.1 `Docs` リポジトリ (アーカイブ化)
| 元ディレクトリ | my-docs での配置 | 備考 |
| :--- | :--- | :--- |
| `dev-records/` | `archive/docs-dev-records/` | 過去の日記ファイル。全移行しアーカイブ。 |
| `dev-records_old/` | `archive/docs-dev-records/` | 同上。フォルダを統合してアーカイブ。 |
| `prompts/` | 移行対象外 | 使用していないため除外。 |
| `templates/` | 移行対象外 | 使用していないため除外。 |
| `tools/` | 移行対象外 | 使用していないため除外。 |
| `books/` | 移行対象外 | 中身がないため除外。 |

### 1.2 `Docs-Study` リポジトリ (継続利用・最優先)
| 元ディレクトリ | my-docs での配置 | 備考 |
| :--- | :--- | :--- |
| `security-news/` | `security-news/` | 既存の `my-docs/security-news/` とマージ。 |
| `security-study/` | `security-study/` | 学習進捗管理。全移行。 |
| `dev-docs/` | `research/` | 調査資料。既存の `my-docs/research/` とマージ。 |
| `specification-draft/` | `knowledge/specs/` | 仕様書ドラフト。全移行。 |
| `prompts/` | `prompts/` | **Pipeline 継続利用のため必須。** |
| `templates/` | `templates/` | **Pipeline 継続利用のため必須。** |
| `Docs-common/tools/` | `tools/` | **Pipeline 継続利用のため必須。** |

## 2. 統合・整理の基本方針 (Safe-First)

1. **Docs-Study 優先**: 現在稼働中の `Docs-Study` の環境をそのまま `my-docs` 上で再現することを最優先する。
2. **Docs の最小移行**: `Docs` からは日記ファイルのみを `archive/` 以下に「読み物」として退避させる。
3. **Pipeline 互換性の維持**: Issue #3 で `private-ops` に移管した Pipeline が正常に動作するよう、`prompts/`, `templates/`, `tools/` は `Docs-Study` のものを正しく配置する。
4. **既存コンテンツの保護**: `my-docs` に既に存在する `research/` や `security-news/` のファイルが、上書きや削除で失われないよう慎重にマージする。

## 3. 次のステップ (Issue #5 移行フェーズ)

- [ ] `archive/docs-dev-records/` ディレクトリの作成とコピー。
- [ ] `Docs-Study` から各ディレクトリを最優先でコピー。
- [ ] `my-docs` ルートの `research/`, `security-news/` へのマージ作業。
- [ ] `private-ops` の Pipeline から参照されるファイルの整合性確認。
