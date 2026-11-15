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

Verification time: 2026-11-15, after the latest main push.

CodeQL run: https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43696363084

- Commit: `4752564af0a5e37d799d73fd2c531164bdc31bfb`
- Job: `Analyze Python`
- Conclusion: success
- GitHub analysis record: category `/language:python`, tool `CodeQL`,
  `results_count=0`
- CodeQL alerts: 0

A later documentation-only push also produced a successful analysis for commit
`8b064cd93b6af8a96b46822f430ef3fbfd1d9319`; its analysis record also reports
`results_count=0`.

This means CodeQL found no alert in this analysis. It does not prove that the
application has no vulnerabilities, because CodeQL only covers the queries and
paths it can analyze.

## Current Dependabot findings

The repository inspection returned four open Dependabot alerts. Their exact
advisory identifiers, CVSS, EPSS, scope, and remediation proposals are in
`docs/DEPENDABOT-FINDINGS.md`.

- `opentelemetry-api`, medium, patched in 1.45.2
- `opentelemetry-api`, medium, patched in 1.45.1
- `flask`, low, patched in 3.1.3
- `pytest`, medium, patched in 9.0.3

The alert records and linked advisory pages were separately inspected for the
four current alerts. The detailed values are recorded in
`docs/DEPENDABOT-FINDINGS.md`; where GitHub did not expose a field directly,
that document marks the value as unavailable rather than estimating it. No
dependency was downgraded to manufacture an alert, and no Dependabot PR was
merged during this phase.

The current agent session could not repeat the GitHub API request because its
network sandbox rejected the HTTPS socket, so the results above retain the
explicit inspection time rather than claiming a newer verification.
