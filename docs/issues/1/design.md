# Design: Issue #1 リポジトリの初期設定を行うためのIssue群を作成する

## Background
- `centervil/Docs` と `centervil/Doc-Study` を統合し、`centervil/my-docs` を立ち上げる。
- ナレッジの集約とメンテナンスの効率化を図る。
- Issue #1 は、この統合プロジェクトを推進するための詳細なタスクを、それぞれ独立した Issue として定義・作成することを目的とする。

## Goals
- 統合プロジェクトに必要な各工程を詳細な Issue に分割し、追跡可能な状態にする。
- 各 Issue に適切なタイトル、Success Criteria、Action Items を設定する。

## Proposed Approach
- Issue #1 の「実施項目 (Action Items)」および「成功条件 (Success Criteria)」を分解し、新規 Issue を作成する。
- 作成する Issue 群:
    1. 【分析】移行元リポジトリ (`Docs`, `Doc-Study`, `private-ops`) のクローンと現状分析
    2. 【移管】ドキュメント自動作成用 Pipeline コードの `private-ops` への配置検討と移管
    3. 【整理】既存ディレクトリの整理・不要ディレクトリの特定
    4. 【移行】各ドキュメント・ファイルの `my-docs` への全移行
    5. 【検証】移管先での自動化パイプライン正常稼働確認
- 各 Issue 作成後、それらを Issue #1 のチェックリストとリンクさせる。

## Success Criteria (for Issue #1)
- [ ] 上記 5 つのサブ Issue が `centervil/my-docs` に作成されていること
- [ ] 各 Issue に背景、成功条件、実施項目が記述されていること
- [ ] Issue #1 のチェックリストが更新され、各項目がサブ Issue へのリンクになっていること
