# OpenAI Resource Cleanup Script

A Python script for managing and deleting OpenAI resources, including assistants, files, threads, and vector stores. The script supports both batch deletion of all resources and selective deletion of specific resource types.

## Features

- Delete multiple types of OpenAI resources:
  - Assistants
  - Files
  - Threads
  - Vector Stores
- Parallel deletion for improved performance
- Command-line interface with selective deletion options
- Safety confirmations before deletion
- Pagination support for handling large numbers of resources

## Prerequisites

- Python 3.6+
- `requests` library
- An OpenAI API key ([Find your API key here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key))

### Important Notice on Threads API

The `list_threads` function is not part of the official OpenAI API. To retrieve threads, you need to extract your session ID while logged into [OpenAI's platform](https://platform.openai.com/threads).

#### How to Get Your Session ID

1. Log in to [OpenAI's platform](https://platform.openai.com/threads).
2. Open the browser developer tools (F12 or right-click and select 'Inspect').
3. Go to the 'Network' tab and filter for `fetch` or `XHR` requests.
4. Refresh the page and look for a request related to threads.
5. Find the `Authorization` or session-related key in the request headers.
6. Copy the session ID, which typically looks like:
   ```
   sess-qOvvKH6Nvn6QKpqtpkjedSKqwzMeBj0FFqnKHe5S
   ```
7. Use this session ID in the script to authenticate `list_threads` requests.

- Python 3.6+
- `requests` library

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies:
   ```bash
   pip install requests
   ```
3. Configure your OpenAI API credentials in the script:
   ```python
   OPENAI_API_KEY = "your-api-key"
   OPENAI_SESSION_KEY = "your-session-key"
   OPENAI_ORG_ID = "your-org-id"
   OPENAI_PROJECT_ID = "your-project-id"
   ```

## Usage

### Basic Command Structure

```bash
python main.py [OPTIONS]
```

### Available Options

- `--all` : Delete all resource types
- `--assistants` : Delete only assistants
- `--files` : Delete only files
- `--threads` : Delete only threads
- `--vector-stores` : Delete only vector stores
- `-h, --help` : Show help message

### Examples

1. Delete all resources:
   ```bash
   python main.py --all
   ```

2. Delete only files and threads:
   ```bash
   python main.py --files --threads
   ```

3. Delete only assistants:
   ```bash
   python main.py --assistants
   ```

4. Show help message:
   ```bash
   python main.py --help
   ```


## Configuration

The script includes several configurable constants:

- `MAX_WORKERS` : Number of parallel deletion workers (default: 10)
- `TIMEOUT` : API request timeout in seconds (default: 30)


## Limitations

- API rate limits may apply
- Large deletions may take significant time
- Some operations require specific API permissions
- The `list_threads` function is not part of the official OpenAI API. To retrieve threads, you need to extract your session ID while logged into [OpenAI's platform](https://platform.openai.com/threads).
