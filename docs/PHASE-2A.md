# Phase 2A Status

## Completed locally

- Created an independent `A9/activity-log-a9` project directory.
- Copied only the Flask application and runtime requirements from A8.
- Added isolated tests, development requirements, lint configuration, CI, and Dependabot configuration.
- No A8 files were edited.
- No commit, push, pull request, merge, or GitHub setting change was performed.

## Blocked verification

The Python executable exists on Windows, but the current Codex execution
environment cannot start it and reports `Unable to create process`. Therefore
Python installation, lint, and pytest results are not claimed as passed yet.

Run the following in Windows PowerShell from this directory:

```powershell
cd "C:\Users\Yorn90104\Desktop\B11309044\1151\軟體開發與維運\A9\activity-log-a9"
py -3.12 --version
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-dev.txt
.\.venv\Scripts\python.exe -m flake8 src tests
.\.venv\Scripts\python.exe -m pytest -q
```

The output should be saved under `evidence/` after execution. A9 must not be
reported as passed until these commands produce real results.
