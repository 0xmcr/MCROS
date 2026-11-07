# Workflow: 03 Release Readiness

## Purpose
Pre-deployment verification gate assessing build integrity, automated test results, data migration safety, secrets scrubbing, rollback procedures, and documentation.

## Steps

### Step 1: Build & Type Integrity
- Run production build commands in standard isolation.
- Ensure 0 compilation, type-check, or bundling errors.

### Step 2: Test Verification
- Run complete automated test suite (unit, integration, e2e).
- Capture test summaries and verify 100% pass rates for release candidates.

### Step 3: Migration & Rollback Review
- Verify forward and backward migration scripts.
- Document and test automated rollback procedures.

### Step 4: Observability & Health Checks
- Verify health check endpoints (`/healthz`, `/readyz`).
- Confirm structured logging and tracing hooks are operational.

### Step 5: Final Decision & Documentation
- Update `docs/RELEASE_READINESS.md` with release decision (GO / NO-GO).
- Present blockers, evidence, and sign-off prerequisites to the user.
