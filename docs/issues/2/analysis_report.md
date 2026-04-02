# Analysis Report: 統合元リポジトリの現状分析

## 1. 移行元リポジトリの構成分析

### 1.1 `Docs` リポジトリ
- **主要ディレクトリ**:
    - `dev-records/`: 日記等の入力ドキュメント。
    - `prompts/`: Zenn記事生成用プロンプト (`zenn_article_prompt.txt`)。
    - `templates/`: Zenn記事テンプレート (`zenn_template.md`)。
    - `tools/`: 自動化スクリプト群。
        - `replace_template_placeholders.sh`
        - `document_processor.py` (Diary用後処理)
        - `find-latest-diary.sh`
        - `diary-filename-processor.sh`
        - `find-prev-article.sh`
- **主要 Pipeline**:
    - `.github/workflows/diary-convert.yml`: 日記からZenn記事を自動生成する。
    - `.github/workflows/claude.yml`, `openhands_resolver.yml` (詳細未確認)

### 1.2 `Docs-Study` リポジトリ
- **主要ディレクトリ**:
    - `security-study/`: 学習用ドキュメント、進捗管理 (`current_day.txt`, `current_theme.txt`, `00_plan.md`)。
    - `prompts/`: 学習コンテンツ生成用プロンプト (`study_day_content_prompt_template.md`)。
    - `templates/`: 学習フォーマットテンプレート (`study_format.md`)。
    - `security-news/`: セキュリティ関連ニュース。
    - `Docs-common/tools/`: 共通ツール (`document_processor.py` - 学習用後処理)。
    - `dev-docs/`, `specification-draft/`: その他ドキュメント。
- **主要 Pipeline**:
    - `.github/workflows/generate_study_material.yml`: 学習コンテンツを自動生成する。

## 2. 移管先リポジトリの構成分析

### 2.1 `private-ops` リポジトリ
- **主要ディレクトリ**:
    - `configs/spotify/`: Spotify関連の設定。
- **主要 Pipeline**:
    - `.github/workflows/spotify-automation.yml`, `reusable-spotify-upload.yml` 等。

## 3. Pipeline の詳細と依存関係

### 3.1 `generate_study_material.yml` (移管対象)
- **フロー**:
    1. Python 環境セットアップ & `content-converter` インストール。
    2. `security-study/current_day.txt` から現在の日数を読込。
    3. `prompts/study_day_content_prompt_template.md` を使用してプロンプト生成。
    4. `content-converter` を実行し、`00_plan.md` を元に学習コンテンツを生成。
    5. `Docs-common/tools/document_processor.py` で後処理。
    6. 日数をインクリメントし、生成されたコンテンツと共にリポジトリへ Push。
- **依存関係 (Secrets)**:
    - `GOOGLE_API_KEY`: Gemini API 使用のため。
    - `LLM_MODEL`: 使用するモデル名 (例: `gemini-pro`)。
    - `GITHUB_TOKEN`: リポジトリへの Push 用。

### 3.2 `diary-convert.yml` (my-docs 統合対象)
- **フロー**:
    - 日記ファイルを検知し、Zenn記事へ変換・Push する。
- **依存関係 (Secrets)**:
    - `GOOGLE_API_KEY`, `LLM_MODEL`

## 4. 統合・移管に向けた課題と提案

- **`document_processor.py` の重複**: `Docs` と `Docs-Study` で微妙に異なる同名ファイルが存在するため、統合時に共通化または明示的な使い分けが必要。
- **移管後のリポジトリ間連携**: `private-ops` に Pipeline を移管する場合、`my-docs` のコンテンツを取得・更新するために、適切な権限を持つ `PAT` が必要になる。
- **パスの解決**: `private-ops` 側で `my-docs` をチェックアウトして実行する場合、Pipeline 内のパス参照（`templates/`, `security-study/` 等）を `my-docs/` 配下として解決するように修正が必要。
