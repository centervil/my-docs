# 設計文書: 日次配信のメタデータ SSOT の作成 (Issue #28)

## 1. 背景と目的
日次配信（学習編・ニュース編）の現在状態（Day 番号や対象日、Spotify シーズン/エピソード番号、配信進捗状況など）が各所に散らばっており、毎回の実行で手動逆算やクリップボードからのテンプレート貼り付けを行っていた。これを解消し、日次実行エージェントや人間が単一の情報源（SSOT: Single Source of Truth）を参照・更新できるようにする。

## 2. SSOT の配置と形式
- **配置**: リポジトリ直下の `config/` または専用場所、または `docs/` 配下、あるいはリポジトリルートに `podcast-ssot.yaml` として配置する。
  - *決定*: 日次実行エージェントや人間が最も迷わず見つけられ、参照しやすいリポジトリ直下に `podcast-ssot.yaml` として配置する。また、近傍に読み方・書き戻し方を記した `README.md` を置く（または `podcast-ssot.yaml` 内にセクションを記載、あるいは `config/` 配下にする？指示では「SSOT と同じ場所」に短い README/セクション）。今回はリポジトリルートに `podcast-ssot.yaml` を配置し、同ファイルのコメントまたは専用の `podcast-ssot-readme.md`（または同一ディレクトリ）とするか、あるいは `config/podcast-ssot.yaml` に置くか。指示: 「SSOT と同じ場所にし、README か design.md から参照できるようにすること」「SSOT の読み方・書き戻し方を説明する短い README/セクション（SSOT と同じ場所）」。
  - *具体配置*: `config/podcast-ssot.yaml` および `config/README.md`（またはルートに `podcast-ssot.yaml` と `PODCAST_SSOT_README.md`）。ルート直下に `podcast-ssot.yaml` と `podcast-ssot-readme.md` を置くのが最もシンプル。ルートに `podcast-ssot.yaml` を置き、その説明を `podcast-ssot-readme.md` に書くか、あるいは `config/podcast-ssot.yaml` と `config/README.md` にする。指示では「SSOT の読み方・書き戻し方を説明する短い README/セクション（SSOT と同じ場所）」とあるので、`config/podcast-ssot.yaml` と `config/README.md` の構成が綺麗。あるいは `podcast-ssot.yaml` の中に詳細なコメント（セクション）を書きつつ `README.md` からリンクする。ここでは `config/podcast-ssot.yaml` と `config/README.md` を採用する。
- **形式**: 機械可読で人が直接編集しやすい **YAML** 形式を採用する。

## 3. 初期値と Provenance（2026-11-15 時点の検証済み事実）
- **学習系 (30日間で学ぶ資格勉強)**:
  - theme: `security-study/CRISC/`
  - material_day: 13 (provenance: 実測 - origin/main に Day13_study.md あり, commit 4b7d622)
  - note_day: 12 (provenance: 実測)
  - spotify_day: 12 (provenance: 実測 - Day12 は 2026-11-15 に公開済み)
  - spotify_season: 19 (provenance: 手順正本 my-life `domains/habits/daily-podcast-runbook.md` §4 の規則)
- **ニュース系 (AI CyberSecurity News Digest)**:
  - report_date: `2026-11-14` (provenance: 実測 - origin/main に cybersecurity_news_2026-11-14.md あり, commit 30e7bd9)
  - note_date: `2026-11-14` (provenance: 実測)
  - spotify_date: `2026-11-14` (provenance: 実測 - 2026-11-15 に公開済み)
  - spotify_season: 1 (provenance: 固定)
  - spotify_last_episode: 557 (provenance: 導出 - 2026-11-13 分がシーズン1 エピソード556 + 前回+1 規則)

## 4. 特記事項・注意書き
- `security-study/current_day.txt` は教材生成側の先行カウンタであり、配信 Day ではない（2026-11-15 時点で値は 13 だが配信完了は Day12）。SSOT 内にこの区別を明記する。
- 書き戻し運用: 各段階の担当は完了時に自分のキーだけを更新し、あわせて `updated_at`（JST）を更新する。ポーリングはしない。
