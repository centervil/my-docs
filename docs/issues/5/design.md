# Design: Issue #5 【移行】各ドキュメント・ファイルの my-docs への全移行

## Background
- 整理計画（Issue #4）に基づき、`Docs` および `Docs-Study` から `my-docs` へのファイル移行を実行する。
- ユーザーの要望通り、`Docs-Study` の環境をそのまま再現し、`Docs` からは日記のみをアーカイブする。

## Goals
- `my-docs` に必要なディレクトリ（`archive/`, `knowledge/`, `tools/`, `prompts/`, `templates/` 等）を作成し、移行対象ファイルを配置する。
- 既存の `research/`, `security-news/` と `Docs-Study` の同名ディレクトリを安全にマージする。

## Proposed Approach
1. **ディレクトリの作成**:
    - `archive/docs-dev-records/`, `knowledge/specs/`, `tools/`, `prompts/`, `templates/`, `security-study/` を作成。
2. **Docs からのアーカイブ移行**:
    - `Docs/dev-records/` および `Docs/dev-records_old/` 内の `.md` ファイルをすべて `archive/docs-dev-records/` にコピーする。
3. **Docs-Study からの移行 (最優先)**:
    - `security-news/`, `security-study/`, `dev-docs/` (as `research/`), `specification-draft/` (as `knowledge/specs/`), `prompts/`, `templates/`, `Docs-common/tools/` (as `tools/`) をコピーする。
    - **重要**: `cp -n` (no-clobber) を基本としつつ、既存の `my-docs` 側のファイル（日付ベースのニュース等）を保護しながらマージする。
4. **検証**:
    - 全ファイルが移行されているか、ディレクトリ構造が整理されているか、パスに矛盾がないかを確認する。

## Success Criteria
- [ ] `archive/docs-dev-records/` に `Docs` の日記が統合されている。
- [ ] `Docs-Study` の学習環境（Study, News, Prompts, Templates, Tools）が `my-docs` 上に再現されている。
- [ ] `my-docs` の既存コンテンツ（`research/`, `security-news/`）が正しく維持されている。
