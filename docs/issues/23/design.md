# Design: [Feature] Automate Daily Security News Collection using NotebookLM CLI (Revised)

## 1. Overview
Automate the manual process of collecting security news (Deep Research) and summarizing them (Chat) using NotebookLM. This revision focuses on robust implementation using the `notebooklm-py` library with a verified async flow and secure authentication.

## 2. Technical Approach

### 2.1 Library & Authentication
- **Library:** `notebooklm-py` (v0.1.0+ recommended)
- **Auth:** Using `NOTEBOOKLM_AUTH_JSON` environment variable.
- **Setup Flow:**
    1. User runs `notebooklm login` locally to generate `storage_state.json`.
    2. User copies JSON content to GitHub Secret `NOTEBOOKLM_AUTH_JSON`.
    3. Workflow injects secret as environment variable.

### 2.2 Automation Workflow (Async Python)
1. **Initialize Client:** Use `NotebookLMClient.from_storage()` which automatically checks `NOTEBOOKLM_AUTH_JSON`.
2. **Deep Research:**
    - Call `client.research.start(query, mode="deep")`.
    - Poll for status `6` (Completed).
    - Extract report markdown from the result.
3. **Notebook Management:**
    - Find/Create notebook "Daily Security News".
    - Import the Deep Research report as a source.
4. **Summarization:**
    - Call `client.chat.ask(notebook_id, prompt)` using the template from `prompts/study_day_content_prompt_template.md`.
5. **Output:**
    - Save to `security-news/cybersecurity_news_YYYY-MM-DD.md`.

### 2.3 Verification & Testing Strategy
- **Environment Check:** `verify_setup.py` to ensure `notebooklm-py` is installed and the auth variable is present.
- **Unit Testing:** `pytest` with `unittest.mock` to simulate `NotebookLMClient` responses (e.g., mocking the research polling and chat responses).
- **Dry Run Mode:** Implementation of a `--dry-run` flag in the automation script to validate logic without calling the API.

## 3. Security Considerations
- **Credential Rotation:** Cookies expire. The design must handle auth errors gracefully and notify the user to rotate the secret.
- **Sensitive Data:** `storage_state.json` contains full session access. It must **never** be logged or printed.

## 4. Implementation Details
- **Script Location:** `private-ops/tools/notebooklm_automation.py`
- **Dependency File:** `private-ops/tools/requirements.txt`
- **Workflow:** `private-ops/.github/workflows/daily_news.yml`
