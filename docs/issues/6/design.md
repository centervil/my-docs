# Design: Issue #6 【検証】移管先での自動化パイプライン正常稼働確認

## Background
- 移管・統合が完了した環境で、`private-ops` から `my-docs` のコンテンツを使用した学習資料の自動生成が正常に行えるかを確認する。

## Goals
- `private-ops` 上の `generate_study_material.yml` がエラーなく実行されること。
- 生成されたコンテンツが `my-docs` に正しく Push されること。
- `my-docs` 側の構成（`prompts/`, `templates/`, `tools/` 等のパス）に不整合がないことを実証する。

## Proposed Approach
1. **Pipeline のテスト実行**:
    - `private-ops` リポジトリで `workflow_dispatch` を使用して手動トリガーする。
    - 入力パラメータ `output_folder` にテスト用のディレクトリ（例: `study-materials/test/`）を指定する。
2. **ログの監視**:
    - GitHub Actions の実行ログを確認し、各ステップ（Checkout, Python Setup, Content-Converter 実行, Post-process, Commit/Push）の成功を確認する。
3. **成果物の確認**:
    - `my-docs` リポジトリに、Pipeline によって生成された新しいファイルおよび `current_day.txt` の更新が反映されていることを確認する。
4. **クリーニング (Optional)**:
    - テストで生成された不要なファイルがあれば削除する。

## Success Criteria
- [ ] `private-ops` の Workflow が正常に完了（Green）する。
- [ ] `my-docs` に新しい学習資料が、正しいテンプレート・プロンプトを使用して生成・Push されている。
- [ ] 全体の正常動作が確認でき次第、統合プロジェクトを完了状態とする。
