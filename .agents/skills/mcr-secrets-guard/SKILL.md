---
name: mcr-secrets-guard
description: Prevent credential leaks, scan code and commits for hardcoded secrets, enforce environment variable hygiene, and maintain safe .env.example files.
---

# MCR Secrets Guard Skill

Use this skill to audit codebases for hardcoded credentials, verify environment variable configurations, and ensure compliance with secret management best practices.

## Secrets Security Protocol

### 1. Hardcoded Secret Detection
Scan code and configuration files for patterns matching:
- AWS Access Keys (`AKIA...`), Google Cloud Service Account keys, GitHub Personal Access Tokens (`ghp_...`).
- Database connection strings containing passwords (`postgres://user:password@host...`).
- JWT signing secrets, private RSA/ECDSA keys, API bearer tokens.

### 2. Environment Variable Hygiene
- All sensitive configurations must be ingested via environment variables (e.g. `process.env.DATABASE_URL`, `os.environ["API_KEY"]`).
- Tracked files (`.gitignore`): Ensure `.env`, `.env.local`, `.env.production` are strictly ignored.
- Public template: Maintain `.env.example` with descriptive variable names and sanitized placeholders (never real secrets).

### 3. Immediate Leak Remediation
If a secret is ever detected in source control or workspace files:
1. Immediately notify the user.
2. Recommend immediate revocation/rotation of the exposed credential.
3. Replace the secret in code with an environment variable reference.
4. Remove the credential from git history if committed.
