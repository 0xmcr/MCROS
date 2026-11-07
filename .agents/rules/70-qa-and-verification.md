---
trigger: model_decision
description: Use when planning tests, writing unit/integration/e2e tests, diagnosing test failures, or validating acceptance criteria.
---

# Quality Assurance and Verification

## Verification Pyramid
1. Unit Tests: Fast, deterministic, test pure functions, business rules, and state transitions in isolation.
2. Integration Tests: Validate interactions across components, databases, queues, and API routes using containers or ephemeral fixtures.
3. End-to-End Tests: Validate critical user workflows (auth, checkout, key business loops) against realistic browser/API environments.
4. Static Checks: Type checking (TypeScript/mypy), linting (ESLint/ruff), formatting, and build validation.

## Test Planning & Discipline
- Use `docs/templates/TEST_PLAN.md` for major releases or refactors.
- Never weaken assertions, delete tests, or hardcode expected results just to pass a test suite.
- When an error occurs:
  1. Capture exact log/stack trace.
  2. Isolate root cause.
  3. Formulate minimal reliable fix.
  4. Verify the fix and verify that no regressions were introduced.
