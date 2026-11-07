---
trigger: manual
---

# DevOps, CI/CD, and Release Readiness Checklist

## Release Verification Gates
Prior to approving any release or deployment:
- [ ] Automated Builds: Clean build with zero type-check or linter errors.
- [ ] Test Suite: 100% passing tests with verified test run logs.
- [ ] Dependency Hygiene: Zero high or critical vulnerabilities in software composition analysis (`npm audit`, `pip-audit`, `cargo audit`).
- [ ] Secrets Scrubbing: Codebase and commit history verified free of plaintext API keys, passwords, or tokens.
- [ ] Database Migrations: Tested up and down migrations; zero backward-incompatible column deletions without deprecation grace period.
- [ ] Observability: Structured logging, metrics collection, distributed tracing, and health check endpoints (`/healthz`, `/readyz`).
- [ ] Rollback Plan: Fully automated, deterministic rollback procedure documented and verified.
- [ ] Release Report: Record status in `docs/RELEASE_READINESS.md`.
