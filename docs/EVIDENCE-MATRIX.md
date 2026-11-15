# Assignment 9 Evidence Matrix

| Requirement | Evidence | Status | Explanation |
|---|---|---|---|
| A: Flake8 configuration | `setup.cfg` | PARTIAL | Configuration is present locally and staged in the initial commit; final lint output is recorded by CI below. |
| A: Initial F841 finding | `evidence/phase2a-results-reported.txt` | PARTIAL | Result was supplied from Windows CMD; original terminal capture is still required for formal evidence. |
| A: F841 fix diff | `evidence/phase2b-flake8-fix.diff` | PARTIAL | The change is recorded locally; final rerun output is still required. |
| A: Final Flake8 | [A9 CI success run](https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43695476661) | PASS | The lint step completed successfully in the real GitHub Actions run. |
| A: pytest | [A9 CI success run](https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43695476661) | PASS | The pytest step completed successfully in the same run. |
| A: CI workflow | [A9 CI workflow](https://github.com/fanyuzhenfu/activity-log-a9/actions/workflows/ci.yml) | PASS | Push and pull_request triggers, Python 3.12, lint, and pytest are configured. |
| A: CI failure evidence | [A9 CI failed run](https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43695494617) | PASS | Dependency installation failed and lint/test steps were skipped, so the job failed closed. |
| E: Dependabot configuration | `.github/dependabot.yml` | PASS | pip and github-actions ecosystems use the root directory and weekly schedules. |
| E: Dependabot alerts | [Security alerts](https://github.com/fanyuzhenfu/activity-log-a9/security/dependabot) | PASS | API inspection returned 0 alerts at inspection time. This does not prove zero future risk. |
| E: Dependabot PR and CI | [Dependabot PR #1](https://github.com/fanyuzhenfu/activity-log-a9/pull/1), [PR check](https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43695472535) | PASS | Dependabot updated actions/checkout 4 to 7; lint-and-test passed. PR remains open. |
| O: CodeQL workflow | `.github/workflows/codeql.yml` | PASS | Advanced Setup uses official `github/codeql-action/init@v3` and `analyze@v3`, Python analysis, push/PR/weekly triggers, and minimal permissions. |
| O: CodeQL Actions run | [CodeQL run 43696363084](https://github.com/fanyuzhenfu/activity-log-a9/actions/runs/43696363084) | PASS | `Analyze Python` completed successfully for commit `4752564af0a5e37d799d73fd2c531164bdc31bfb`. |
| O: Code scanning analysis | [Code Scanning](https://github.com/fanyuzhenfu/activity-log-a9/security/code-scanning) | PASS | GitHub analysis record exists with `results_count=0`; the alerts API returned 0 CodeQL alerts. |
| E: Current Dependabot alerts | [Security alerts](https://github.com/fanyuzhenfu/activity-log-a9/security/dependabot) | PASS | Four current alerts were returned: two medium OpenTelemetry API issues, one low Flask issue, and one medium pytest issue. Patched versions were recorded in Phase 2D notes. |
