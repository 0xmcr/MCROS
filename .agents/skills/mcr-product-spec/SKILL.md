---
name: mcr-product-spec
description: Author comprehensive Product Requirements Documents (PRD), map user journeys, define functional and non-functional requirements, and establish acceptance criteria.
---

# MCR Product Specification & PRD Skill

Use this skill when defining product requirements, creating a new feature specification, or scoping an MVP. It translates business vision and user needs into testable technical specifications.

## PRD Authoring Protocol

### 1. Problem & User Discovery
- Formulate the core user problem and evidence of market demand.
- Define target user personas, their workflows, and operational pain points.

### 2. Goals & Non-Goals
- Primary Goals: Measurable business or technical outcomes (e.g. "Sub-100ms search latency", "Self-service onboarding in <2 minutes").
- Explicit Non-Goals: Features deliberately excluded from the current scope to maintain focus.

### 3. Functional Requirements (FR) & Acceptance Criteria
For every feature, define:
- Feature ID & Name
- Priority: P0 (Must have for MVP), P1 (Should have), P2 (Nice to have)
- User Story: "As a [role], I want to [action] so that [benefit]."
- Acceptance Criteria (Given / When / Then format):
  - *Given* an authenticated user with role Admin
  - *When* they click "Revoke Access"
  - *Then* the target session is immediately terminated and an audit log event is recorded.

### 4. Non-Functional Requirements (NFR)
- Performance (p95 latency < 300ms)
- Security (OWASP Top 10 compliance, encrypted data at rest)
- Accessibility (WCAG 2.1 AA compliant)
- Reliability (99.9% uptime target)

Document output in `docs/templates/PRD.md`.
