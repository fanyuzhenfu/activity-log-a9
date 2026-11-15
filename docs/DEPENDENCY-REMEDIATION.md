# Dependency Remediation

## Scope and status

This document records a local-only remediation attempt for the four open
Dependabot alerts inspected on 2026-11-15. No commit, push, pull request, or
remote alert dismissal was performed in this phase.

## Version plan

| Dependency | Before | Proposed local version | Related advisory | Status |
|---|---:|---:|---|---|
| `opentelemetry-api` | 1.39.0 | 1.45.2+ | GHSA-mf5v-w3w3-f6cg; GHSA-xcq7-p3pf-p88h | BLOCKED |
| `opentelemetry-sdk` | 1.39.0 | must be coordinated | SDK currently pins `opentelemetry-api==1.39.0` | BLOCKED |
| OTLP exporter/proto | 1.39.0 | must be coordinated | exporter currently requires the 1.39.0 SDK/proto set | BLOCKED |
| Flask instrumentation | 0.60b0 | unchanged locally | compatibility depends on the OTel release family | NOT VERIFIED |
| Flask | 3.1.2 | 3.1.3 | GHSA-68rp-wp8r-4726 | MODIFIED LOCALLY |
| pytest | 8.3.5 | 9.0.3 | GHSA-6w46-j5rx-g56g | MODIFIED LOCALLY |

## OpenTelemetry compatibility finding

The installed metadata shows that the current `opentelemetry-sdk==1.39.0`
requires `opentelemetry-api==1.39.0`, while the OTLP gRPC exporter requires
the 1.39.0 SDK and proto packages. The installed Flask instrumentation
(`0.60b0`) also depends on the matching `0.60b0` semantic-conventions set,
which currently pins the 1.39.0 API.

Therefore, changing only `opentelemetry-api` to 1.45.2 would create a resolver
conflict. The correct fix requires identifying a mutually compatible newer
OpenTelemetry release family for API, SDK, exporter/proto, instrumentation, and
semantic conventions. That lookup and installation could not be completed in
the current restricted execution environment, so the OpenTelemetry alerts are
not claimed as fixed.

## Local changes made

Only these two version pins were changed locally:

- `Flask==3.1.2` → `Flask==3.1.3`
- `pytest==8.3.5` → `pytest==9.0.3`

The OpenTelemetry pins were intentionally left unchanged until a compatible
release family can be resolved. No production code, instrumentation setup, or
tests were changed.

## Verification status

| Check | Result | Reason |
|---|---|---|
| Dependency install | PASS | User verified installation in Windows PowerShell after the two version changes. |
| `pip check` | PASS | User reported `No broken requirements found`. |
| Flake8 | PASS | User reported no lint errors after the changes. |
| pytest | PASS | User reported `2 passed in 0.53s`. |
| OTLP warning check | PASS | User reported no OTLP Collector connection errors during pytest. |

These results were executed and reported by the user in Windows PowerShell;
they were not re-executed by the Agent. No native terminal screenshot is yet
attached to this document.

## Recommended next step

Run the exact PowerShell commands from the handoff using the Windows Python
environment. If the two small upgrades pass, they can be proposed for a
separate security branch. OpenTelemetry should be upgraded only as a tested,
coordinated release set; otherwise retain the current pins and report the
remaining alerts as unresolved.
