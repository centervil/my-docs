# Project Context (my-docs)

このファイルは、本リポジトリにおける AI エージェントの動作原則を定義します。

## コア・プリンシパル
1. **SSOT (Single Source of Truth)**: GitHub Issue の本文および `docs/issues/[ID]/` 配下のドキュメントを「唯一の真実」として扱う。
2. **IDD (Issue-Driven Development)**: すべての変更は Issue に基づき、`Start -> Task -> Review -> End` のサイクルで実施する。
3. **ロジックの分離**: 本リポジトリはドキュメントを主とし、実行ロジック（スクリプト等）が必要な場合は `private-ops` サブモジュール側での管理を検討する。

## 運用ルール
- **作業開始**: 
  - 作業前に必ず `gh issue list` で対象 Issue を確認する。
  - 要件が不足している場合は、実装前に `requirements` プロセスを通じて SSOT を確立する。
- **ブランチ戦略**: 
  - 常に Issue 単位のトピックブランチを作成し、`main` への直接コミットは最小限とする。
  - 作業完了後は、自律的にブランチを削除し、環境をクリーンに保つ。
- **ドキュメント更新**:
  - 作業進捗は必ず `docs/issues/[ID]/tasks.md` に反映し、トレーサビリティを確保する。

## 安全性への配慮
- `security-news/` や `security-study/` 配下の自動生成コンテンツの構造を破壊しない。
- サブモジュール (`private-ops`) の更新を伴う場合は、本体リポジトリとの同期を確実に行う。
