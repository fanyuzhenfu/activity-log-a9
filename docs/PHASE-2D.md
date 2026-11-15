# Phase 2D CodeQL Status

## Configuration

This project uses GitHub CodeQL Advanced Setup for Python. The workflow uses
the official `github/codeql-action/init@v3` and `analyze@v3` actions. It runs on
push to `main`, pull requests, and a weekly schedule.

The workflow grants only the permissions needed by the job:

- `contents: read` for checkout
- `actions: read` for workflow-related access
- `security-events: write` to upload CodeQL results

No Default Setup was enabled, so the repository will not run duplicate CodeQL
configurations.

## Verification status

Before this workflow is pushed, the repository API reports no CodeQL analysis.
The final O-Level status must wait for a completed run and a readable Code
Scanning result. A green YAML file alone is not evidence of a successful scan.
