---
name: security-audit
description: Perform a comprehensive, authorized defensive security audit of code, dependencies, API contracts, trust boundaries, and configuration hygiene.
---

# Defensive Security Audit Skill

Use this skill when auditing a codebase for vulnerabilities, reviewing secrets management, inspecting OWASP Top 10 risks, or preparing a security assessment.

## Protocol

1. Scope Validation: Ensure analysis is defensive and restricted strictly to workspace code and configurations.
2. Static Code Analysis (SAST):
   - Trace untrusted inputs to sinks (SQL queries, system commands, DOM manipulation).
   - Verify authentication and authorization checks on all routes.
   - Inspect CORS, Content-Security-Policy, and cookie security flags.
3. Dependency Vulnerability Audit (SCA):
   - Check package manifests and lockfiles for known CVEs.
   - Run dependency audit tools (`npm audit`, `pip-audit`, `cargo audit`) when installed.
4. Secrets Hygiene:
   - Check for hardcoded API keys, bearer tokens, private keys, or passwords.
   - Confirm only sample `.env.example` templates exist with dummy values.
5. Report Generation:
   - File all findings in `docs/SECURITY_REPORT.md` using the standard format.
