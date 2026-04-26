# Design: Repository Cleanup for Pure Content Repo (Issue 15)

## Goal
Transform the `my-docs` repository into a pure content (document) repository by removing unnecessary scripts and archives.

## Scope
- Remove:
  - `archive/`
  - `tools/`
  - `study-materials/test/`
- Preserve:
  - `prompts/`
  - `templates/`
  - All other content-related directories (`knowledge/`, `research/`, `security-news/`, etc.)

## Strategy
1. **Research**: Scan the repository for any internal references to the directories slated for deletion to avoid broken links or scripts.
2. **Branching**: Create a dedicated cleanup branch.
3. **Execution**: Delete the specified directories.
4. **Verification**: 
   - Confirm directories are gone.
   - Confirm preserved directories remain intact.
   - (Note) Verification of the external `private-ops` pipeline will rely on user confirmation or specific instructions if available.

## Success Criteria
- [ ] `archive/` is completely removed.
- [ ] `tools/` is completely removed.
- [ ] `study-materials/test/` is completely removed.
- [ ] `prompts/` and `templates/` are maintained.
- [ ] No internal broken references to deleted paths.
