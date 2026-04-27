# Design: Repository Cleanup for Pure Content Repo (Issue 15)

## Goal
Transform the `my-docs` repository into a pure content (document) repository by removing unnecessary scripts and archives.

## Scope
- Remove:
  - `archive/`
  - `tools/`
  - `study-materials/test/`
- Reorganize:
  - `research/` -> `docs/research/`
  - `knowledge/specs/` -> `docs/specs/`
  - Remove empty `knowledge/` directory.
- Preserve:
  - `prompts/`
  - `templates/`
  - All other content-related directories.

## Strategy
1. **Research**: Scan the repository for any internal references to the directories slated for deletion or relocation.
2. **Branching**: Create a dedicated cleanup branch (already created: `issue-15-cleanup`).
3. **Execution**: 
   - Delete specified directories.
   - Move content to new locations under `docs/`.
4. **Verification**: 
   - Confirm directories are gone/moved.
   - Confirm preserved directories remain intact.
   - Update internal references if necessary.
   - (Note) Verification of the external `private-ops` pipeline will rely on user confirmation or specific instructions if available.

## Success Criteria
- [ ] `archive/` is completely removed.
- [ ] `tools/` is completely removed.
- [ ] `study-materials/test/` is completely removed.
- [ ] `prompts/` and `templates/` are maintained.
- [ ] No internal broken references to deleted paths.
