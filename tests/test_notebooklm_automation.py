import sys
import asyncio
import os
from unittest.mock import AsyncMock, MagicMock, patch

# Mocking the notebooklm dependency before import
sys.modules['notebooklm'] = MagicMock()
from notebooklm_automation import NotebookLMAutomation

async def test_output_path_handling():
    print("--- Testing Output Path Handling ---")
    
    mock_client = AsyncMock()
    mock_client.__aenter__.return_value = mock_client
    
    # Mock Research
    mock_research = AsyncMock()
    mock_research.poll.return_value = MagicMock(state=6)
    mock_research.results = [MagicMock(markdown='Research Result')]
    mock_client.research.start.return_value = mock_research
    
    # Mock Notebooks
    mock_nb = MagicMock(id='nb-123', title='Daily Security News Automation')
    mock_client.notebooks.list.return_value = [mock_nb]
    
    # Mock Chat
    mock_client.chat.ask.return_value = MagicMock(text='Summary Output')
    
    # Target output path
    test_output = "tmp_test_news.md"
    automation = NotebookLMAutomation(dry_run=False, output_path=test_output)
    
    async def mock_from_storage(): return mock_client
    
    # We will actually test if 'open' is called with the correct path
    with patch.object(NotebookLMAutomation, 'load_prompt_template', return_value='Template'), \
         patch('notebooklm_automation.NotebookLMClient.from_storage', side_effect=mock_from_storage), \
         patch('os.makedirs', MagicMock()), \
         patch('builtins.open', MagicMock()) as mock_open:
        
        await automation.run()
        
        # Verify if open was called with the specific output path
        mock_open.assert_called_with(test_output, "w", encoding="utf-8")
        print(f"✅ Success: Script correctly attempted to write to {test_output}")

async def test_dynamic_path_creation():
    print("--- Testing Dynamic Directory Creation ---")
    test_output = "some/nested/dir/news.md"
    automation = NotebookLMAutomation(dry_run=False, output_path=test_output)
    
    mock_client = AsyncMock()
    mock_client.__aenter__.return_value = mock_client
    async def mock_from_storage(): return mock_client
    
    # Setup mocks to reach the file saving part
    mock_research = AsyncMock()
    mock_research.poll.return_value = MagicMock(state=6)
    mock_research.results = [MagicMock(markdown='R')]
    mock_client.research.start.return_value = mock_research
    mock_client.notebooks.list.return_value = [MagicMock(id='1', title='Daily Security News Automation')]
    mock_client.chat.ask.return_value = MagicMock(text='S')

    with patch.object(NotebookLMAutomation, 'load_prompt_template', return_value='T'), \
         patch('notebooklm_automation.NotebookLMClient.from_storage', side_effect=mock_from_storage), \
         patch('os.makedirs') as mock_makedirs, \
         patch('builtins.open', MagicMock()):
        
        await automation.run()
        
        # Verify if os.makedirs was called with the correct directory
        mock_makedirs.assert_called_with("some/nested/dir", exist_ok=True)
        print(f"✅ Success: Script correctly attempted to create directory 'some/nested/dir'")

async def run_all_tests():
    try:
        await test_output_path_handling()
        await test_dynamic_path_creation()
        print("\n🎉 All logic tests passed.")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(run_all_tests())
