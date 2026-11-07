---
trigger: model_decision
description: Use when performing defensive security reviews, threat modeling, vulnerability assessments, secrets auditing, or OWASP compliance checks.
---

# Defensive Security and Threat Modeling

## Scope & Compliance
- Operate exclusively within authorized workspace and defensive engineering bounds.
- Reference OWASP Top 10, OWASP API Security Top 10, ASVS, and CWE taxonomies.
- Never extract, print, or commit real API keys, passwords, private certificates, or production secrets.

## Threat Modeling & Review Protocol
- Model threats using STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
- Record models using `docs/templates/THREAT_MODEL.md`.
- Inspect perimeter trust boundaries, data in transit (TLS 1.3), and data at rest (AES-256 / KMS).
- Review CORS configurations, Content Security Policy (CSP), cookie security flags (`HttpOnly`, `Secure`, `SameSite=Lax/Strict`).

## Vulnerability Reporting
For any security finding, populate `docs/SECURITY_REPORT.md` with:
- ID, Severity (CVSS v3/v4), Affected Component, Evidence, Impact, Remediation, and Retest status.
- Avoid vague claims; substantiate every finding with concrete code references or scan output.
