import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import argparse

# Configuration constants
OPENAI_API_KEY = ""
OPENAI_SESSION_KEY = ""
OPENAI_ORG_ID = ""
OPENAI_PROJECT_ID = ""

HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "OpenAI-Beta": "assistants=v2"
}

SESSION_HEADERS = {
    "Authorization": f"Bearer {OPENAI_SESSION_KEY}",
    "OpenAI-Beta": "assistants=v2",
    "OpenAI-Organization": OPENAI_ORG_ID,
    "OpenAI-Project": OPENAI_PROJECT_ID,
    "Origin": "https://platform.openai.com",
    "Referer": "https://platform.openai.com/"
}

MAX_WORKERS = 10  # Adjust this based on your needs
TIMEOUT = 30

def list_files(limit=100, after=None):
    """Get a list of files from OpenAI API with pagination."""
    all_files = []
    has_more = True
    
    while has_more:
        url = "https://api.openai.com/v1/files"
        params = {"limit": limit}
        if after:
            params["after"] = after
        
        response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            files = data.get("data", [])
            all_files.extend(files)
            
            # Check if there are more results
            has_more = data.get("has_more", False)
            if has_more and files:
                after = files[-1]["id"]
            else:
                break
        else:
            print(f"Failed to list files: {response.status_code}, {response.text}")
            break
    
    return all_files


def delete_file(file_id):
    """Delete a file by its file ID."""
    url = f"https://api.openai.com/v1/files/{file_id}"
    response = requests.delete(url, headers=HEADERS, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json().get("deleted", False)
    else:
        print(
            f"Failed to delete file {file_id}: {response.status_code}, {response.text}"
        )
        return False


def delete_all_files():
    """List all files and delete them one by one."""
    files = list_files()
    print(f"Found {len(files)} files to delete")
    if files:
        for file in files:
            file_id = file.get("id")
            if file_id:
                deleted = delete_file(file_id)
                if deleted:
                    print(f"Deleted file: {file_id}")
                else:
                    print(f"Failed to delete file: {file_id}")
    else:
        print("No files to delete.")


def list_assistants(limit=100, after=None):
    """Get a list of assistants from OpenAI API with pagination."""
    all_assistants = []
    has_more = True
    
    while has_more:
        url = "https://api.openai.com/v1/assistants"
        params = {"limit": limit}
        if after:
            params["after"] = after
        
        response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            assistants = data.get("data", [])
            all_assistants.extend(assistants)
            
            # Check if there are more results
            has_more = data.get("has_more", False)
            if has_more and assistants:
                after = assistants[-1]["id"]
            else:
                break
        else:
            print(f"Failed to list assistants: {response.status_code}, {response.text}")
            break
    
    return all_assistants


def delete_assistant(assistant_id):
    """Delete an assistant by its ID."""
    url = f"https://api.openai.com/v1/assistants/{assistant_id}"
    response = requests.delete(url, headers=HEADERS, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json().get("deleted", False)
    else:
        print(
            f"Failed to delete assistant {assistant_id}: {response.status_code}, {response.text}"
        )
        return False


def delete_all_assistants():
    """List all assistants and delete them one by one."""
    assistants = list_assistants()
    print(f"Found {len(assistants)} assistants to delete")
    if assistants:
        for assistant in assistants:
            assistant_id = assistant.get("id")
            if assistant_id:
                deleted = delete_assistant(assistant_id)
                if deleted:
                    print(f"Deleted assistant: {assistant_id}")
                else:
                    print(f"Failed to delete assistant: {assistant_id}")
    else:
        print("No assistants to delete.")


def list_threads(limit=100, after=None):
    """Get a list of threads from OpenAI API with pagination."""
    all_threads = []
    has_more = True
    
    while has_more:
        url = "https://api.openai.com/v1/threads"
        params = {"limit": limit}
        if after:
            params["after"] = after
        
        # Use SESSION_HEADERS instead of HEADERS for thread operations
        response = requests.get(url, headers=SESSION_HEADERS, params=params, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            threads = data.get("data", [])
            all_threads.extend(threads)
            
            # Check if there are more results
            has_more = data.get("has_more", False)
            if has_more and threads:
                after = threads[-1]["id"]
            else:
                break
        else:
            print(f"Failed to list threads: {response.status_code}, {response.text}")
            break
    
    return all_threads


def delete_thread(thread_id):
    """Delete a thread by its ID."""
    url = f"https://api.openai.com/v1/threads/{thread_id}"
    # Use SESSION_HEADERS for delete operation as well
    response = requests.delete(url, headers=SESSION_HEADERS, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json().get("deleted", False)
    else:
        print(
            f"Failed to delete thread {thread_id}: {response.status_code}, {response.text}"
        )
        return False


def delete_all_threads():
    """List all threads and delete them one by one."""
    threads = list_threads()
    if threads:
        for thread in threads:
            thread_id = thread.get("id")
            if thread_id:
                deleted = delete_thread(thread_id)
                if deleted:
                    print(f"Deleted thread: {thread_id}")
                else:
                    print(f"Failed to delete thread: {thread_id}")
    else:
        print("No threads to delete.")


def list_vector_stores(limit=100, after=None):
    """Get a list of vector stores from OpenAI API with pagination."""
    all_stores = []
    has_more = True
    
    while has_more:
        url = "https://api.openai.com/v1/vector_stores"
        params = {"limit": limit}
        if after:
            params["after"] = after
        
        response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            stores = data.get("data", [])
            all_stores.extend(stores)
            
            # Check if there are more results
            has_more = data.get("has_more", False)
            if has_more and stores:
                after = stores[-1]["id"]
            else:
                break
        else:
            print(f"Failed to list vector stores: {response.status_code}, {response.text}")
            break
    
    return all_stores


def list_vector_store_files(vector_store_id, limit=100):
    """Get a list of files from a vector store."""
    url = f"https://api.openai.com/v1/vector_stores/{vector_store_id}/files"
    params = {"limit": limit}
    response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Failed to list vector store files: {response.status_code}, {response.text}")
        return []


def delete_vector_store(vector_store_id):
    """Delete a vector store by its ID."""
    url = f"https://api.openai.com/v1/vector_stores/{vector_store_id}"
    response = requests.delete(url, headers=HEADERS, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json().get("deleted", False)
    else:
        print(
            f"Failed to delete vector store {vector_store_id}: {response.status_code}, {response.text}"
        )
        return False


def delete_all_vector_stores():
    """List all vector stores and delete them one by one."""
    vector_stores = list_vector_stores()
    print(f"Found {len(vector_stores)} vector stores to delete")
    if vector_stores:
        for store in vector_stores:
            store_id = store.get("id")
            if store_id:
                # First, list and log files in the vector store
                files = list_vector_store_files(store_id)
                if files:
                    print(f"Vector store {store_id} contains {len(files)} files")
                
                # Then delete the vector store
                deleted = delete_vector_store(store_id)
                if deleted:
                    print(f"Deleted vector store: {store_id}")
                else:
                    print(f"Failed to delete vector store: {store_id}")
    else:
        print("No vector stores to delete.")


def parallel_delete_all_files():
    """Delete all files in parallel."""
    files = list_files()
    print(f"Found {len(files)} files to delete")
    if not files:
        print("No files to delete.")
        return

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_file = {
            executor.submit(delete_file, file["id"]): file["id"]
            for file in files if file.get("id")
        }
        
        for future in as_completed(future_to_file):
            file_id = future_to_file[future]
            try:
                deleted = future.result()
                if deleted:
                    print(f"Deleted file: {file_id}")
                else:
                    print(f"Failed to delete file: {file_id}")
            except Exception as e:
                print(f"Exception deleting file {file_id}: {str(e)}")


def parallel_delete_all_assistants():
    """Delete all assistants in parallel."""
    assistants = list_assistants()
    print(f"Found {len(assistants)} assistants to delete")
    if not assistants:
        print("No assistants to delete.")
        return

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_assistant = {
            executor.submit(delete_assistant, asst["id"]): asst["id"]
            for asst in assistants if asst.get("id")
        }
        
        for future in as_completed(future_to_assistant):
            asst_id = future_to_assistant[future]
            try:
                deleted = future.result()
                if deleted:
                    print(f"Deleted assistant: {asst_id}")
                else:
                    print(f"Failed to delete assistant: {asst_id}")
            except Exception as e:
                print(f"Exception deleting assistant {asst_id}: {str(e)}")


def list_runs(thread_id, limit=100):
    """Get a list of runs from a thread."""
    url = f"https://api.openai.com/v1/threads/{thread_id}/runs"
    params = {"limit": limit}
    response = requests.get(url, headers=HEADERS, params=params, timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Failed to list runs: {response.status_code}, {response.text}")
        return []


def get_thread_ids_from_runs():
    """Get unique thread IDs from all runs."""
    thread_ids = set()
    
    # First get all assistants to find their threads
    assistants = list_assistants()
    for assistant in assistants:
        assistant_id = assistant.get("id")
        if assistant_id:
            # Get runs for this assistant's threads
            threads_response = requests.get(
                f"https://api.openai.com/v1/assistants/{assistant_id}/threads",
                headers=HEADERS,
                timeout=TIMEOUT
            )
            if threads_response.status_code == 200:
                threads = threads_response.json().get("data", [])
                for thread in threads:
                    thread_ids.add(thread.get("id"))

    return list(thread_ids)


def parallel_delete_all_threads():
    """Delete all threads in parallel."""
    threads = list_threads()
    print(f"Found {len(threads)} threads to delete")
    if not threads:
        print("No threads to delete.")
        return

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_thread = {
            executor.submit(delete_thread, thread["id"]): thread["id"]
            for thread in threads if thread.get("id")
        }
        
        for future in as_completed(future_to_thread):
            thread_id = future_to_thread[future]
            try:
                deleted = future.result()
                if deleted:
                    print(f"Deleted thread: {thread_id}")
                else:
                    print(f"Failed to delete thread: {thread_id}")
            except Exception as e:
                print(f"Exception deleting thread {thread_id}: {str(e)}")


def parallel_delete_all_vector_stores():
    """Delete all vector stores in parallel."""
    vector_stores = list_vector_stores()
    print(f"Found {len(vector_stores)} vector stores to delete")
    if not vector_stores:
        print("No vector stores to delete.")
        return

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # First list all files in parallel
        for store in vector_stores:
            store_id = store.get("id")
            if store_id:
                files = list_vector_store_files(store_id)
                if files:
                    print(f"Vector store {store_id} contains {len(files)} files")

        # Then delete stores in parallel
        future_to_store = {
            executor.submit(delete_vector_store, store["id"]): store["id"]
            for store in vector_stores if store.get("id")
        }
        
        for future in as_completed(future_to_store):
            store_id = future_to_store[future]
            try:
                deleted = future.result()
                if deleted:
                    print(f"Deleted vector store: {store_id}")
                else:
                    print(f"Failed to delete vector store: {store_id}")
            except Exception as e:
                print(f"Exception deleting vector store {store_id}: {str(e)}")


def confirm_deletion(resource_type):
    """Ask for user confirmation before deletion."""
    response = input(f"\nAre you sure you want to delete all {resource_type}? (y/N): ").lower().strip()
    return response == 'y'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Delete OpenAI resources')
    parser.add_argument('--all', action='store_true', help='Delete all resources')
    parser.add_argument('--assistants', action='store_true', help='Delete assistants')
    parser.add_argument('--files', action='store_true', help='Delete files')
    parser.add_argument('--threads', action='store_true', help='Delete threads')
    parser.add_argument('--vector-stores', action='store_true', help='Delete vector stores')
    
    args = parser.parse_args()
    start_time = time.time()
    
    # If no specific arguments are provided and --all is not set, show help
    if not any(vars(args).values()):
        parser.print_help()
        exit(1)
    
    if args.all:
        if confirm_deletion("resources (assistants, vector stores, files, and threads)"):
            print("\nDeleting all assistants...")
            parallel_delete_all_assistants()
            print("\nDeleting all vector stores...")
            parallel_delete_all_vector_stores()
            print("\nDeleting all files...")
            parallel_delete_all_files()
            print("\nDeleting all threads...")
            parallel_delete_all_threads()
    else:
        if args.assistants and confirm_deletion("assistants"):
            print("\nDeleting all assistants...")
            parallel_delete_all_assistants()
        
        if args.vector_stores and confirm_deletion("vector stores"):
            print("\nDeleting all vector stores...")
            parallel_delete_all_vector_stores()
        
        if args.files and confirm_deletion("files"):
            print("\nDeleting all files...")
            parallel_delete_all_files()
        
        if args.threads and confirm_deletion("threads"):
            print("\nDeleting all threads...")
            parallel_delete_all_threads()
    
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
