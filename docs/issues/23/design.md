# Design: [Feature] Automate Daily Security News Collection using NotebookLM CLI

## 1. Overview
Automate the manual process of collecting security news (Deep Research) and summarizing them (Chat) using NotebookLM via a CLI tool.

## 2. Technical Approach

### 2.1 CLI Tool Research
- **Selected Tool:** `notebooklm-py` (https://github.com/teng-lin/notebooklm-py)
- **Rationale:** 
    - Reverse-engineered API (httpx/Protobuf) is faster and more stable for pipelines than browser automation.
    - Supports programmatic creation of notebooks, adding sources (URLs), and querying via `ask()`.
    - Handle authentication via stored session cookies (`storage_state.json`).
- **Alternative:** `notebooklm-mcp-cli` (useful for interactive CLI usage, but `notebooklm-py` is better for Python scripting).

### 2.2 Automation Script (`private-ops/tools/notebooklm_automation.py`)
- **Library:** `notebooklm-py`
- **Workflow:**
    1. **Initialization:** Load authentication state from `storage_state.json`.
    2. **Notebook Setup:** Create or find a "Daily Security News" notebook.
    3. **Source Injection:** Add the "Deep Research" trigger. (Note: In NotebookLM, this is often done by adding a web source or querying with a search-enabled prompt).
    4. **Summarization:** Use `notebook.ask()` with the prompt from `prompts/study_day_content_prompt_template.md`.
    5. **Export:** Save the response to `security-news/cybersecurity_news_YYYY-MM-DD.md` in the `my-docs` repo.

### 2.3 Pipeline (`private-ops/.github/workflows/daily_news.yml`)
- Scheduled GitHub Action (cron).
- Steps:
    1. Checkout `my-docs` and `private-ops`.
    2. Setup environment (Python/CLI).
    3. Run automation script.
    4. Commit and push generated news to `my-docs`.

## 3. Risks & Mitigations
- **NotebookLM API Stability:** If no official API exists, browser automation might be brittle. Mitigation: Use robust selectors and error handling.
- **Authentication:** Keeping session cookies/tokens valid. Mitigation: Use GitHub Secrets for credentials and implement token refresh if possible.

## 4. Success Criteria
- [ ] Research phase identifies a viable CLI method.
- [ ] Prototype script successfully generates a summary.
- [ ] `private-ops` contains the finalized script and workflow.
- [ ] First automated news file appears in `security-news/`.
