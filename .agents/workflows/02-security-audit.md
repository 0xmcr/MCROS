# Workflow: 02 Security Audit

## Purpose
Authorized defensive security audit across code, dependencies, configurations, authentication boundaries, and storage layer.

## Steps

### Step 1: Scope & Boundaries
- Confirm audit scope is strictly within workspace boundaries.
- Inspect codebase for sensitive assets, perimeter gateways, and external API calls.

### Step 2: Static Analysis & Code Review
- Inspect source code against OWASP Top 10 and CWE standards.
- Check authentication and authorization enforcement on all routes.
- Verify input sanitization, parameterized queries, and output encoding.

### Step 3: Software Composition Analysis (SCA)
- Scan package lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, `requirements.txt`, `Cargo.lock`) for known vulnerabilities (CVEs).
- Verify dependency licenses and audit results.

### Step 4: Secrets & Configuration Hygiene
- Audit environment templates, configuration files, and git history for accidentally committed credentials.
- Ensure only environment variable names (never raw secrets) are documented.

### Step 5: Threat Modeling & Remediation
- Map trust boundaries using `docs/templates/THREAT_MODEL.md`.
- File all concrete findings with remediation steps in `docs/SECURITY_REPORT.md`.
