# Project AI Git

A small Python package for an AI assistant agent using the Google ADK LLM agent interface.

## Project structure

- `project_ai_git/`
  - `agent.py` - defines the main root AI agent using `google.adk.agents.llm_agent.Agent`.
  - `tools.py` - utility functions for file reading and word counting.
  - `__init__.py` - package initializer.
- `temporyagent/` - temporary workspace files.

## Setup

1. Create and activate a Python virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install any required packages.

```powershell
pip install google-adk
```

> Adjust package installation if your project uses a different dependency manager or package source.

## Usage

Import the package and use the defined `root_agent` or utility functions:

```python
from project_ai_git.agent import root_agent
from project_ai_git.tools import read_file, words_count

# Example usage
print(root_agent.name)
print(read_file("example.txt")['output'])
print(words_count("Hello world")['output'])
```

## Notes

- `agent.py` currently configures a `gemini-2.5-flash` model.
- `tools.py` exposes basic helper functions for file I/O and word counting.
- Add a `requirements.txt` or update dependencies as the project grows.
