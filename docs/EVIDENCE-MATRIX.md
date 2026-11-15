# Assignment 9 Evidence Matrix

| Requirement | Evidence | Status | Explanation |
|---|---|---|---|
| A: Flake8 configuration | `setup.cfg` | NOT VERIFIED | Configuration is present locally; final lint output must be retained after staging. |
| A: Initial F841 finding | `evidence/phase2a-results-reported.txt` | PARTIAL | Result was supplied from Windows CMD; original terminal capture is still required for formal evidence. |
| A: F841 fix diff | `evidence/phase2b-flake8-fix.diff` | PARTIAL | The change is recorded locally; final rerun output is still required. |
| A: Final Flake8 | Windows CMD output | NOT VERIFIED | Not executed by the current Codex environment. |
| A: pytest | Windows CMD output | PARTIAL | Student reported `2 passed in 1.45s`; raw output should be preserved. |
| A: CI workflow | `.github/workflows/ci.yml` | NOT VERIFIED | Workflow is prepared locally; no GitHub Actions run exists yet. |
| E: Dependabot configuration | `.github/dependabot.yml` | NOT VERIFIED | Configuration is prepared locally; GitHub settings are not yet checked. |
| E: Dependabot alerts | GitHub Security page | NOT VERIFIED | Requires remote repository and read-only inspection. |
| E: Dependabot PR and CI | GitHub PR URL and checks | NOT VERIFIED | No remote repository or Dependabot PR exists yet. |
| O: CodeQL | To be added in Phase 2D | NOT STARTED | Not part of this phase. |
