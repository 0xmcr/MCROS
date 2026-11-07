---
name: mcr-security-audit
description: Perform a comprehensive, authorized defensive security audit of code, dependencies, API contracts, trust boundaries, and configuration hygiene.
---

# MCR Defensive Security Audit Skill

Use this skill when auditing a codebase for vulnerabilities, reviewing secrets management, inspecting OWASP Top 10 risks, or preparing a security assessment report.

## Supporting Resources & Submodules
- Secrets Scanner Script: [scan_secrets.sh](./scripts/scan_secrets.sh)
- Defensive Headers Middleware: [secure-headers.ts](./examples/secure-headers.ts)
- Comprehensive Threat Runbook: [owasp-top-10-runbook.md](./references/owasp-top-10-runbook.md)

---

## 1. Defensive Audit Protocol

### Step 1: Automated Secrets Hygiene Scan
- Execute `./scripts/scan_secrets.sh`.
- Confirm zero exposed AWS tokens, private keys, database passwords, or personal access tokens exist in tracked files.

### Step 2: Code Review against OWASP Top 10
- Consult [owasp-top-10-runbook.md](./references/owasp-top-10-runbook.md).
- Verify all database queries use parameterized inputs.
- Inspect route handlers for Broken Object Level Authorization (BOLA/IDOR).
- Audit authentication cookie flags (`HttpOnly`, `Secure`, `SameSite`).

### Step 3: Security Headers & CORS Inspection
- Compare HTTP response headers against [secure-headers.ts](./examples/secure-headers.ts).
- Verify Content-Security-Policy (CSP) and HSTS enforcement.
- Ensure CORS configurations do not wildcard (`Access-Control-Allow-Origin: *`) on routes returning private user data.

### Step 4: Documentation & Reporting
- File all concrete findings into `docs/SECURITY_REPORT.md` including ID, Severity, Affected Component, Evidence, Impact, and verified Remediation steps.
