import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from private_ops.tools.notebooklm_automation import NotebookLMAutomation

@pytest.mark.asyncio
async def test_automation_dry_run():
    automation = NotebookLMAutomation(dry_run=True)
    # This should run without error and not call any APIs
    await automation.run()

@pytest.mark.asyncio
async def test_automation_logic_with_mocks():
    # Mock the NotebookLMClient
    mock_client = AsyncMock()
    mock_client.__aenter__.return_value = mock_client
    
    # Mock Research
    mock_research_session = AsyncMock()
    mock_research_session.poll.return_value = MagicMock(state=6)
    mock_research_session.results = [MagicMock(markdown="Sample Research Result")]
    mock_client.research.start.return_value = mock_research_session
    
    # Mock Notebooks
    mock_notebook = MagicMock(id="nb-123")
    mock_client.notebooks.list.return_value = [mock_notebook]
    
    # Mock Chat
    mock_client.chat.ask.return_value = MagicMock(text="Sample Summary Output")
    
    automation = NotebookLMAutomation(dry_run=False)
    
    # Mock the template loading to avoid file dependency
    with patch.object(NotebookLMAutomation, 'load_prompt_template', return_value="Template Content"):
        with patch('private_ops.tools.notebooklm_automation.NotebookLMClient.from_storage', return_value=mock_client):
            # Also mock file writing
            with patch('builtins.open', MagicMock()):
                with patch('os.makedirs', MagicMock()):
                    await automation.run()
    
    # Verify the calls
    mock_client.research.start.assert_called_once()
    mock_client.chat.ask.assert_called_once_with("nb-123", "Template Content")
    print("Logic verification with mocks successful.")

if __name__ == "__main__":
    asyncio.run(test_automation_logic_with_mocks())
