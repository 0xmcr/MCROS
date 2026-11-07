---
name: release-readiness
description: Verify production release readiness across builds, test suites, database migrations, secrets scrubbing, observability, and rollback safety.
---

# Release Readiness Verification Skill

Use this skill when preparing to deploy, cut a release tag, or verify that a project meets production-grade quality criteria.

## Verification Checklist

1. Build & Compilation:
   - Run production build command (`npm run build`, `cargo build --release`, `go build`, etc.).
   - Confirm zero type-checking errors and clean artifact generation.
2. Automated Test Execution:
   - Run full unit, integration, and E2E test suites.
   - Verify 100% test passing evidence.
3. Database Migration & Rollback Review:
   - Inspect pending migrations.
   - Verify backward compatibility and existence of an automated rollback path.
4. Secrets & Environment Scrubbing:
   - Verify zero plaintext secrets in tracked files or build artifacts.
5. Observability & Health Checks:
   - Verify health check endpoints (`/healthz`, `/readyz`).
   - Check error reporting and metric instrumentation.
6. Documentation & Go/No-Go Decision:
   - Complete `docs/RELEASE_READINESS.md` and report release decision.
