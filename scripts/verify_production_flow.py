import os
import sys
import asyncio
import uuid
from notebooklm import NotebookLMClient

async def verify_production_flow():
    print("=== Production Flow Verification Starting ===")
    
    test_title = f"Verification Test - {uuid.uuid4().hex[:8]}"
    client = await NotebookLMClient.from_storage()
    
    async with client:
        print(f"Connected: {client.is_connected}")
        
        # 1. Create a temporary notebook
        print(f"Creating notebook: {test_title}")
        nb = await client.notebooks.create(test_title)
        nb_id = nb.id
        print(f"Created Notebook ID: {nb_id}")
        
        try:
            # 2. Add a source (Text)
            print("Adding a text source...")
            source_title = "Test Context"
            source_text = "This is a verification source. NotebookLM should use this to generate a report."
            source = await client.sources.add_text(nb_id, source_title, source_text)
            print(f"Added source: {source.title} (ID: {source.id})")
            
            # 3. Wait for source processing
            print("Waiting for source processing...")
            await client.sources.wait_until_ready(nb_id, source.id)
            print("Source processed.")
            
            # 4. Generate an artifact (Report)
            print("Generating a report artifact...")
            status = await client.artifacts.generate_report(nb_id)
            print(f"Initial Status: {status}")
            
            task_id = getattr(status, 'task_id', None)
            if not task_id and hasattr(status, 'metadata') and status.metadata:
                task_id = status.metadata.get('task_id')
            
            if not task_id:
                if status.is_complete:
                     print("Task already complete.")
                else:
                    raise Exception(f"Could not determine task_id from status: {status}")

            # 5. Wait for artifact
            if task_id:
                print(f"Waiting for task completion (Task ID: {task_id})...")
                final_status = await client.artifacts.wait_for_completion(nb_id, task_id)
                print(f"Final Status: {final_status}")
            
            # 6. List and Download latest report
            print("Listing reports to find the artifact ID...")
            reports = await client.artifacts.list_reports(nb_id)
            if not reports:
                raise Exception("No reports found after generation.")
            
            latest_report = reports[0]
            report_id = latest_report.id
            print(f"Found report: {latest_report.title} (ID: {report_id})")

            output_path = f"verify_report_{nb_id[:8]}.md"
            print(f"Downloading report to {output_path}...")
            # CORRECT ORDER: (notebook_id, output_path, artifact_id)
            await client.artifacts.download_report(nb_id, output_path, report_id)
            
            if os.path.exists(output_path):
                print(f"Download complete: {output_path}")
                with open(output_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    print(f"Report Length: {len(content)} characters")
                    print(f"Preview: {content[:100]}...")
                
                os.remove(output_path)
                print("Cleaned up local report file.")
            else:
                print("Error: Report file not found after download.")

        except Exception as e:
            print(f"Error during flow: {e}")
            raise e
        finally:
            # 7. Cleanup (Delete notebook)
            print(f"Cleaning up: Deleting notebook {nb_id}")
            await client.notebooks.delete(nb_id)
            print("Notebook deleted.")

    print("=== Production Flow Verification Completed Successfully ===")

async def main():
    try:
        await verify_production_flow()
    except Exception as e:
        print(f"Verification Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
