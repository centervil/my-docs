# Design for Issue #21: Structure Study Plan and Isolate Daily Content

## 1. 概要
`00_plan.md` を構造化データとして扱い、CI パイプライン内で特定日のデータのみをフィルタリングして LLM に渡す。

## 2. 構造設計

### 2.1. プランファイル形式 (`00_plan.md`)
```markdown
<course_context>
# 全体概要
...
</course_context>

<day_plans>
<day n="1">
テーマ: ...
内容: ...
</day>
...
</day_plans>
```

### 2.2. パイプライン抽出ロジック (GitHub Actions)
`sed` コマンドを使用して、特定のタグに囲まれた範囲を抽出する。

- **Common Context**: `<course_context>` 〜 `</course_context>`
- **Daily Content**: `<day n="X">` 〜 `</day>`

抽出した内容を `isolated_input.txt` に結合し、これを `content-converter` のインプット（`--input`）として渡す。

## 3. 変更箇所
1.  `templates/plan_template.md`: 新規作成。
2.  `security-study/00_plan.md`: 新フォーマットへ移行。
3.  `private-ops/.github/workflows/generate_study_material.yml`: 抽出ステップの追加と `content-converter` の引数変更。
4.  `prompts/study_day_content_prompt_template.md`: 入力構造の変化に合わせた指示の微調整。
