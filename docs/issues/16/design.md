# Design: Issue #16 古いリポジトリのアーカイブ (`Docs`, `Docs-Study`)

## Background
`my-docs` へのドキュメント統合および `private-ops` へのロジック移管が完了したため、役割を終えた古いリポジトリを整理する。検証は既に完了しており、速やかにアクセス制限と凍結を行う。

## Goals
- `Docs` および `Docs-Study` リポジトリの無効化とアーカイブを完遂する。
- 外部からのアクセスを遮断し、読み取り専用の状態にする。

## Proposed Approach
1. **GitHub Actions の無効化**: 不要な自動更新や通知を止めるため、リポジトリ単位で Actions を無効化する。
2. **非公開化 (Private)**: リポジトリを非公開に設定し、アクセスを制限する。
3. **アーカイブ (Archive)**: リポジトリをアーカイブ設定にし、不慮の更新を防ぐ。

## Tools
- `gh repo edit`: リポジトリの視認性変更およびアーカイブ設定に使用。
- `gh workflow disable`: ワークフローの停止に使用。

## Success Criteria
- [x] `Docs` リポジトリの Actions が無効化されていること。
- [x] `Docs` リポジトリが Private になっていること。
- [x] `Docs` リポジトリが Archive されていること。
- [x] `Docs-Study` リポジトリの Actions が無効化されていること。
- [x] `Docs-Study` リポジトリが Private になっていること。
- [x] `Docs-Study` リポジトリが Archive されていること。
