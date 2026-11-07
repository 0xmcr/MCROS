---
trigger: model_decision
description: Use when designing or implementing backend services, REST/GraphQL APIs, background workers, authentication, authorization, or error handling.
---

# Backend Engineering Guidelines

## API Design & Standards
- RESTful or typed RPC/GraphQL endpoints with explicit OpenAPI / JSON Schema specifications.
- Consistent envelope / error model: include machine-readable error codes, human-readable messages, and correlation/request IDs.
- Rate limiting, throttling, and pagination on all list/search queries.

## Input Validation & Trust Boundaries
- Validate all incoming payloads strictly at the perimeter (e.g. Zod, Pydantic, class-validator).
- Reject unrecognized fields in strict schemas where appropriate.
- Sanitize inputs against injection attacks (SQLi, command injection, path traversal, XSS).

## Security & Auth
- Enforce authentication on all private routes via industry standards (JWT with short lifetimes, OAuth 2.0 / OIDC, or secure session cookies).
- Fine-grained authorization: Role-Based (RBAC) or Attribute-Based (ABAC) access control checked at controller/service layers.
- Password hashing using modern standards (Argon2id or bcrypt with appropriate cost factors).

## Reliability & Resiliency
- Idempotency keys on all state-mutating requests (POST/PUT).
- Graceful shutdown, connection pooling, backpressure handling, circuit breakers for upstream dependencies.
