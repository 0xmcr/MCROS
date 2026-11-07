---
name: mcr-backend-api
description: Design and implement enterprise REST, GraphQL, or gRPC APIs with strict schema validation, consistent error models, rate limiting, and pagination.
---

# MCR Enterprise Backend API Engineering Skill

Use this skill when architecting, implementing, or auditing backend services, API controllers, input validation layers, and serialization pipelines.

## Supporting Resources & Submodules
- Executable Validator: [validate_api.py](./scripts/validate_api.py)
- Reference Implementation: [express-clean-api.ts](./examples/express-clean-api.ts)
- Comprehensive Standards: [api-guidelines.md](./references/api-guidelines.md)

---

## 1. Architectural Principles & Invariants

1. **Zero Trust at Perimeter**: Every inbound parameter (Body, Query, Path, Header) must pass through a strict type-checked schema validator (Zod in TypeScript, Pydantic in Python) before reaching business services.
2. **Deterministic Response Envelopes**: Every API response must adhere to a predictable wrapper containing `success: true/false`, `data` or `error`, and `meta.requestId` for correlation.
3. **No Leaked Stack Traces**: Production error responses must never expose internal database queries, file paths, or language stack traces to clients.
4. **Resilient Rate Limiting**: All public and authenticated endpoints must be bounded by sliding-window or token-bucket rate limiters.

---

## 2. Step-by-Step Implementation Workflow

### Step 1: Define Strongly Typed Contracts
Before writing database queries or controllers:
- Define request DTOs using strict schemas. See [express-clean-api.ts](./examples/express-clean-api.ts).
- Define output response interfaces.
- Specify HTTP status codes and error taxonomies using [api-guidelines.md](./references/api-guidelines.md).

### Step 2: Implement Input Validation & Sanitization
- Ingest untrusted payloads and parse with `.safeParse()`.
- Reject unrecognized fields to prevent mass-assignment vulnerabilities.
- Format granular validation error messages indicating field name and specific constraint violated.

### Step 3: Implement Business Logic & Idempotency
- For state-mutating requests (`POST /api/v1/orders`), extract `Idempotency-Key` headers.
- Coordinate with database transaction boundaries (`BEGIN ... COMMIT`).
- Enforce business invariants in application service layers.

### Step 4: Verification & Automated Testing
- Validate output schema envelopes using `./scripts/validate_api.py`.
- Write automated integration tests verifying status codes:
  - Valid payload -> `200 OK` or `201 Created`
  - Missing field -> `400 Bad Request` with structured details
  - Unauthorized token -> `401 Unauthorized`
  - Unprivileged caller -> `403 Forbidden`
