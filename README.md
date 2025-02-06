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
python deletefiles.py [OPTIONS]
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
   python deletefiles.py --all
   ```

2. Delete only files and threads:
   ```bash
   python deletefiles.py --files --threads
   ```

3. Delete only assistants:
   ```bash
   python deletefiles.py --assistants
   ```

4. Show help message:
   ```bash
   python deletefiles.py --help
   ```

## Safety Features

- Confirmation prompts before deletion
- Default 'No' option for safety
- Resource counting before deletion
- Detailed success/failure logging

## Configuration

The script includes several configurable constants:

- `MAX_WORKERS` : Number of parallel deletion workers (default: 10)
- `TIMEOUT` : API request timeout in seconds (default: 30)

## Output

The script provides detailed output, including:
- Number of resources found
- Deletion progress
- Success/failure status for each operation
- Total execution time

## Error Handling

- API errors are caught and logged
- Network timeouts are handled gracefully
- Invalid responses are reported

## Security Notes

- Keep your API keys secure
- Don't commit the script with real API keys
- Consider using environment variables for sensitive credentials

## Limitations

- API rate limits may apply
- Large deletions may take significant time
- Some operations require specific API permissions
- The `list_threads` function is not part of the official OpenAI API. To retrieve threads, you need to extract your session ID while logged into [OpenAI's platform](https://platform.openai.com/threads).

### How to Get Your Session ID

1. Log in to [OpenAI's platform](https://platform.openai.com/threads).
2. Open the browser developer tools (F12 or right-click and select 'Inspect').
3. Go to the 'Network' tab and filter for `fetch` or `XHR` requests.
4. Refresh the page and look for a request related to threads.
5. Find the `Authorization` or session-related key in the request headers.
6. Copy the session ID, which typically looks like:
   ```
   sess-qOvvkhlby7865ekhhbklbfjkj
   ```
7. Use this session ID in the script to authenticate `list_threads` requests.


- API rate limits may apply
- Large deletions may take significant time
- Some operations require specific API permissions

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

MIT License

## Disclaimer

Use this script carefully as deletions are permanent and cannot be undone. Always ensure you have backups of important data before running deletion operations.

