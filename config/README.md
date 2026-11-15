# Podcast メタデータ SSOT (Single Source of Truth)

本ファイルは、日次配信パイプライン（学習編・ニュース編）の進行状況、番組設定、タイトル・概要規則、テンプレートを一元管理する SSOT です。

## 運用ルール
1. **書き戻し運用**: 各パイプラインの各段階（素材作成・note公開・Spotify公開）の担当者は、処理完了時に該当するキー（`material_day`, `note_day`, `spotify_day`, `report_date`, `note_date`, `spotify_date`, `spotify_last_episode` など）および `updated_at`（JST）を更新してください。ポーリングは行いません。
2. **先行カウンタとの区別**: `security-study/current_day.txt` は教材生成側の先行カウンタであり、配信完了済みの `spotify_day` や `note_day` とは異なります。
3. **テンプレート利用**: 自動生成・手動投稿の際に本ファイルのテンプレートおよび導出規則を参照してください。
