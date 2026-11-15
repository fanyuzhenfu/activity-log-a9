# Dependabot Findings

Inspection time: 2026-11-15 (GitHub API response created at approximately
08:41 UTC). All four alerts were open at inspection time. The current declared
versions come directly from `requirements.txt` and `requirements-dev.txt`.

## Alert 4: OpenTelemetry traceparent parsing

- Alert number: 4
- Advisory: GHSA-mf5v-w3w3-f6cg
- CVE: CVE-2026-126360
- Package: `opentelemetry-api`
- Ecosystem: pip
- Dependency scope: runtime, direct declaration in `requirements.txt`
- Declared version: 1.39.0
- Vulnerable range: `<= 1.45.1`
- Patched version: 1.45.2
- Severity: medium
- CVSS: 5.3
- CVSS vector: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L`
- EPSS: 0.00519 (percentile 0.44643)
- Advisory: https://github.com/open-telemetry/opentelemetry-python/security/advisories/GHSA-mf5v-w3w3-f6cg

The advisory describes quadratic-time parsing of a specially crafted
`traceparent` value. This matters to the application because Flask
instrumentation can extract inbound trace context. The practical exposure
depends on the HTTP server, carrier, and header-size limits. The current demo
does not expose a public service, but the dependency is part of the runtime
path, so this is the highest priority finding.

Recommended fix: upgrade `opentelemetry-api` to 1.45.2 or later, then rerun
the dependency installation, `pip check`, Flake8, pytest, and CI. Not applied
in this phase.

## Alert 3: OpenTelemetry tracestate parsing

- Alert number: 3
- Advisory: GHSA-xcq7-p3pf-p88h
- CVE: CVE-2026-114603
- Package: `opentelemetry-api`
- Ecosystem: pip
- Dependency scope: runtime, direct declaration in `requirements.txt`
- Declared version: 1.39.0
- Vulnerable range: `<= 1.45.0`
- Patched version: 1.45.1
- Severity: medium
- CVSS: 5.3
- CVSS vector: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L`
- EPSS: 0.00487 (percentile 0.42525)
- Advisory: https://github.com/open-telemetry/opentelemetry-python/security/advisories/GHSA-xcq7-p3pf-p88h

The advisory describes unbounded `tracestate` parsing that can consume
excessive CPU. It is relevant to the same inbound propagation path as Alert 4,
but it is a separate advisory and should not be merged with Alert 4. Updating
to 1.45.2 addresses both reported OpenTelemetry API findings.

Recommended fix: upgrade `opentelemetry-api` to 1.45.2 or later and verify
compatibility with the other OpenTelemetry packages. Not applied in this
phase.

## Alert 2: Flask cache variation header

- Alert number: 2
- Advisory: GHSA-68rp-wp8r-4726
- CVE: CVE-2026-27205
- Package: `flask`
- Ecosystem: pip
- Dependency scope: runtime, direct declaration in `requirements.txt`
- Declared version: 3.1.2
- Vulnerable range: `< 3.1.3`
- Patched version: 3.1.3
- Severity: low
- CVSS: GitHub returned 0 with no vector string
- EPSS: 0.00400 (percentile 0.34536)
- Advisory: https://github.com/pallets/flask/security/advisories/GHSA-68rp-wp8r-4726

The issue concerns a missing `Vary: Cookie` header in a specific session access
pattern. The A9 demo does not access Flask sessions and does not use a caching
proxy, so the demonstrated application path is not directly affected. The
runtime dependency should still move to 3.1.3 in a normal maintenance update.

Recommended fix: upgrade Flask to 3.1.3 and rerun the application tests. Not
applied in this phase.

## Alert 1: pytest temporary directory handling

- Alert number: 1
- Advisory: GHSA-6w46-j5rx-g56g
- CVE: CVE-2025-71176
- Package: `pytest`
- Ecosystem: pip
- Dependency scope: development, direct declaration in `requirements-dev.txt`
- Declared version: 8.3.5
- Vulnerable range: `< 9.0.3`
- Patched version: 9.0.3
- Severity: medium
- CVSS: 6.8
- CVSS vector: `CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:L`
- EPSS: 0.00154 (percentile 0.04517)
- Advisory: https://github.com/advisories/GHSA-6w46-j5rx-g56g

This is a development-tool issue involving local temporary-directory handling
on UNIX. It is not part of the Flask runtime deployment. It still matters for
developer and CI environments, but it has lower production impact than the two
runtime OpenTelemetry findings.

Recommended fix: upgrade pytest to 9.0.3 or later and rerun the test suite.
Not applied in this phase.

## Priority and status

1. Upgrade `opentelemetry-api` to 1.45.2 or later. This addresses Alerts 3 and
   4 together while keeping the change narrow.
2. Upgrade Flask to 3.1.3 after confirming the existing routes and
   instrumentation tests.
3. Upgrade pytest to 9.0.3 as a development dependency.

These are proposed changes only. No dependency version was changed in Phase
2E, so the four GitHub alerts remain open. CVSS and EPSS are different: CVSS
describes technical severity, while EPSS estimates exploitation probability.
Neither value alone proves that this small demo is exploitable in its current
deployment.
