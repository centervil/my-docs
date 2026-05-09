import os
import sys
import asyncio
from notebooklm import NotebookLMClient

async def main():
    print("--- Starting NotebookLM Verification ---")
    
    try:
        print("Initializing NotebookLMClient from storage...")
        # Await the coroutine to get the client instance
        client = await NotebookLMClient.from_storage()
        
        async with client:
            print(f"Connected: {client.is_connected}")
            
            print("Fetching notebook list...")
            notebooks = await client.notebooks.list()
            print(f"Found {len(notebooks)} notebooks.")
            
            for nb in notebooks[:5]:
                try:
                    # Looking at dir(Notebook) earlier, it had __dataclass_fields__ 
                    # Let's see if it has 'title' or 'id'
                    title = getattr(nb, 'title', 'No Title')
                    nb_id = getattr(nb, 'id', 'No ID')
                    print(f"- {title} (ID: {nb_id})")
                except Exception as e:
                    print(f"- [Error reading notebook info: {e}]")
        
    except Exception as e:
        print(f"Error during verification: {e}")
        print("\nNote: You might need to authenticate first using:")
        print("python -m notebooklm auth login")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
