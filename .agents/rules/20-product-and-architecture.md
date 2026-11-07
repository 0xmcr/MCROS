---
trigger: model_decision
description: Use when authoring PRDs, system architecture designs, domain modeling, or Architecture Decision Records (ADRs).
---

# Product Requirements and System Architecture

## Product Requirements Framework
- Every product feature must address a real user problem with verifiable demand.
- Document requirements in `docs/templates/PRD.md` format.
- Define explicit Functional Requirements (FR) with priority (P0/P1/P2) and testable acceptance criteria.
- Define Non-Functional Requirements (NFR) covering latency, throughput, security, accessibility (WCAG AA), and availability.

## Architecture & System Design
- Separation of concerns: Enforce clean domain boundaries and decoupled services.
- Data contracts: Every external and internal service boundary must use strongly typed schemas (TypeScript, Pydantic, protobuf, OpenAPI).
- Complexity budget: Choose the simplest architecture (monolith or modular monolith) that reliably satisfies scaling and operational constraints. Avoid premature distributed microservices.
- Architecture Decision Records: Log non-trivial decisions using `docs/templates/ADR.md`.
