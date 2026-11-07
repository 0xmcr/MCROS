---
name: mcr-project-planning
description: Plan project milestones, define work breakdown structure (WBS), task dependencies, timeline estimates, and risk management strategies.
---

# MCR Project Planning & Work Breakdown Skill

Use this skill at the initiation of any software project or major feature epic to transform high-level requirements into an actionable, dependency-mapped execution plan.

## Planning Protocol

### Step 1: Scope & Milestone Definition
- Define MVP (Minimum Viable Product): Focus strictly on P0 critical-path features that deliver the core value proposition.
- Define Phase 2 (Enhancements): P1 features (performance optimizations, secondary user roles, advanced analytics).
- Define Phase 3 (Scale & Polish): P2 features (integrations, customization, multi-region).

### Step 2: Work Breakdown Structure (WBS)
Decompose each epic into isolated, verifiable engineering tasks:
1. Architecture & Scaffold (directory setup, configs, linting, git hooks).
2. Data Layer (database schema, models, migrations, seed data).
3. Core Backend Services & APIs (business logic, controllers, input validation).
4. Auth & Security (tokens, middleware, route guards).
5. Frontend UI/UX (pages, layout, responsive components, state management).
6. Integration & End-to-End Wiring (client-server data flows, optimistic UI).
7. QA & Testing (unit tests, integration test fixtures, E2E user flows).
8. DevOps & Deployment (Docker, CI/CD pipelines, production readiness).

### Step 3: Dependency Mapping & Risk Register
- Identify blockers (e.g. frontend cannot test authenticated routes until auth middleware is ready).
- Formulate risk mitigation strategies for third-party APIs, database limits, and rate limits.
- Record tasks and track progress in `docs/PROJECT_CONTEXT.md`.
