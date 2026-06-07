---
name: study-theme-switcher
description: security-studyセクションの学習テーマを変更します。新しいディレクトリの作成、current_theme.txtやcurrent_day.txtの更新、および00_plan.mdへの30日間学習計画の生成を自動化します。
---

# study-theme-switcher

このスキルは、`security-study/` 配下の学習テーマを切り替えるための標準的なワークフローを提供します。

## ワークフロー

1.  **ディレクトリの準備**: `security-study/[テーマ名]/` ディレクトリを作成し、`.gitkeep` を配置します。
2.  **設定ファイルの更新**:
    *   `security-study/current_theme.txt` を `security-study/[テーマ名]/` に書き換えます。
    *   `security-study/current_day.txt` を `1` にリセットします。
3.  **学習計画の生成**:
    *   既存の `security-study/00_plan.md` のフォーマット（`<course_context>` と `<day_plans>` タグを使用する構造）を厳格に維持します。
    *   30日間のカリキュラムを生成し、`00_plan.md` を上書きします。
    *   計画は「実務への適用」を重視し、毎日「思考タスク」または「実践」を含めるようにします。

## 計画のフォーマット定義

`00_plan.md` は以下の構造でなければなりません：

```markdown
# [テーマ名] 30日間学習計画
## ～[サブタイトル]～

[概要文]

<course_context>
[学習の全体像や軸となる概念の解説]
</course_context>

<day_plans>
<day n="1">
テーマ: [今日のテーマ]
内容:
- [箇条書きの学習項目]
- [思考タスクまたは実践内容]
</day>
... (Day 30まで続く)
</day_plans>
```

## 注意事項

- 既存の学習ログ（`DayX_study.md`など）は削除せず、新しいディレクトリに切り替えることで履歴を分離します。
- テーマ名は、ディレクトリ名として適切な形式（例: PMP, CISSP, AWS-SAA）にする必要があります。
