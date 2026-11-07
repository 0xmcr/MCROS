---
name: mcr-test-automation
description: Author and run automated unit, integration, and end-to-end (E2E) test suites with high code coverage and deterministic test fixtures.
---

# MCR Test Automation Skill

Use this skill when implementing automated testing, writing test cases for new features, setting up test runners, or validating pull requests.

## Test Pyramid & Standards

### 1. Unit Tests (Base Layer)
- Scope: Pure functions, utilities, domain entities, schema validators, state reducers.
- Speed: Fast, in-memory execution (<1ms per test). Zero network or database dependencies.
- Tools: Vitest, Jest, Pytest.

### 2. Integration Tests (Middle Layer)
- Scope: API route handlers, database queries, service layers, cache interactions.
- Isolation: Use ephemeral test databases (Docker Testcontainers, SQLite in-memory, or transactions rolled back after each test).
- Validation: Ensure HTTP status codes, response payloads, database state transitions, and audit logs match expectations.

### 3. End-to-End (E2E) Tests (Top Layer)
- Scope: Critical user journeys (Signup -> Onboard -> Create Project -> Checkout -> Logout).
- Execution: Headless browser automation (Playwright).
- Resilience: Avoid brittle XPath or CSS selectors; query elements by user-facing roles and text (`getByRole('button', { name: 'Submit' })`).

## Execution & Output
- Run tests via standard workspace test commands (`npm test`, `pytest`, `cargo test`).
- Verify tests pass with 100% success before approving any task completion.
- Never weaken assertions or mock internal logic simply to make tests turn green.
