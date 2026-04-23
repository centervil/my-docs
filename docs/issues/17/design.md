# Design: Issue #17 【最終同期】Docs-Study からの最新コンテンツの再同期

## Background
- 同期漏れ（1日分の遅延）を解消するため、`Docs-Study` から最新のセキュリティニュースと学習資料を再取得する。

## Goals
- `security-news/` および `security-study/` の最新状態を完全に反映する。
- `current_day.txt` を最新の値に更新する。

## Proposed Approach
1. `Docs-Study` を `git pull` して最新化。
2. `cp -u` (または `cp -a`) で差分を `my-docs` に適用。
3. 差分を確認し、コミット・PR作成。

## Success Criteria
- [ ] `my-docs` が `Docs-Study` の最新コンテンツと一致している。
