# Assignment 9 - DevSecOps Fundamentals

This repository is an independent A9 project for B11309044. It uses a small
Flask application to demonstrate linting, dependency security checks, and
CodeQL static analysis.

## Local setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-dev.txt
```

## Checks

```powershell
.\.venv\Scripts\python.exe -m flake8 src tests
.\.venv\Scripts\python.exe -m pytest -q
```

GitHub Actions runs the same lint and test checks for pushes and pull requests.
Dependabot and CodeQL configuration will be verified with real GitHub evidence
before the final report is written.
