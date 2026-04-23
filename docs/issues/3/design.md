# Design: Issue #3 【移管】ドキュメント自動作成用 Pipeline コードの private-ops への配置検討と移管

## Background
- `Docs-Study` に含まれていた「学習コンテンツ自動作成 Pipeline」を `private-ops` リポジトリへ移管し、コンテンツ (my-docs) とロジック (private-ops) を分離する。

## Goals
- `generate_study_material.yml` を `private-ops` へ移管し、正常にトリガーできるようにする。
- `document_processor.py` (学習用) を `private-ops` のツールディレクトリへ移管する。
- 移管先でのパス構成を確定し、動作可能な設定を行う。

## Proposed Approach
1. **配置先の選定**:
    - Workflow: `private-ops/.github/workflows/generate_study_material.yml`
    - Tool: `private-ops/tools/study-material/document_processor.py`
    - （一時的に `my-docs` 側のリポジトリ情報を取得するための PAT 使用設定を含める）
2. **コードの移管**:
    - 分析時にクローンした一時ディレクトリからコードをコピーする。
3. **Pipeline の調整**:
    - `actions/checkout` で `my-docs` をチェックアウトするよう設定変更。
    - 取得した `my-docs` のコンテンツ（`security-study/`, `templates/`, `prompts/`）を正しく参照できるよう、パス変数を調整。
    - 後処理ツール (`document_processor.py`) の実行パスを移管後のパスに修正。
4. **設定の外部化**:
    - `current_day.txt` などの状態管理ファイルが `my-docs` 側にあることを前提とした動作を確認する。

## Success Criteria
- [ ] Pipeline コードが `private-ops` へ配置されている。
- [ ] `private-ops` で Workflow が正しく認識されている。
- [ ] 依存関係のあるツールが適切な場所に配置されている。
