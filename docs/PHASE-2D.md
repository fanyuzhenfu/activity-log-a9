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

## Verification result

CodeQL run: https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43696363084

- Commit: `4752564af0a5e37d799d73fd2c531164bdc31bfb`
- Job: `Analyze Python`
- Conclusion: success
- GitHub analysis record: category `/language:python`, tool `CodeQL`,
  `results_count=0`
- CodeQL alerts: 0

This means CodeQL found no alert in this analysis. It does not prove that the
application has no vulnerabilities, because CodeQL only covers the queries and
paths it can analyze.

## Current Dependabot findings

The later repository inspection returned four Dependabot alerts:

- `opentelemetry-api`, medium, patched in 1.45.2
- `opentelemetry-api`, medium, patched in 1.45.1
- `flask`, low, patched in 3.1.3
- `pytest`, medium, patched in 9.0.3

The API response did not provide CVSS scores or EPSS values for these records.
No dependency was downgraded to manufacture an alert, and no Dependabot PR was
merged during this phase.
