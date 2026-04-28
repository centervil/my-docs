# Tasks for Issue #21: Structure Study Plan and Isolate Daily Content

- [x] **Task 1: プランテンプレートの作成**
    - `templates/plan_template.md` を作成する
- [x] **Task 2: 既存プランの構造化移行**
    - `security-study/00_plan.md` を新しいタグ形式に変換する
- [x] **Task 3: ワークフローの抽出ロジック実装**
    - `private-ops/.github/workflows/generate_study_material.yml` に抽出ステップを追加
    - `content-converter` の `--input` を抽出済みファイルに変更
- [x] **Task 4: プロンプトの最適化**
    - `prompts/study_day_content_prompt_template.md` の指示を更新
- [x] **Task 5: 動作検証**
    - `Day 1` の抽出が正しく行われるかローカル（またはモック）で確認
