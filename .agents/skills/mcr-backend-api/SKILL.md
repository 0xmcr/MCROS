---
name: mcr-backend-api
description: Design and implement enterprise REST, GraphQL, or gRPC APIs with strict schema validation, consistent error models, rate limiting, and pagination.
---

# MCR Backend API Engineering Skill

Use this skill when building backend services, designing RESTful or RPC endpoints, implementing input validation, or establishing robust error handling.

## API Architecture Principles

### 1. Schema Validation at Perimeter
- Validate 100% of incoming payloads (body, query params, headers) using schema validators (Zod, Pydantic, Joi).
- Reject extraneous or malformed fields early before hitting service layers or database queries.

### 2. Standardized Response & Error Envelope
- Success Response:
  ```json
  {
    "success": true,
    "data": { ... },
    "meta": { "page": 1, "limit": 20, "total": 140 }
  }
  ```
- Error Response:
  ```json
  {
    "success": false,
    "error": {
      "code": "VALIDATION_FAILED",
      "message": "Human-readable explanation of error.",
      "details": [{ "field": "email", "issue": "Invalid email address format" }],
      "requestId": "req_abc123"
    }
  }
  ```

### 3. API Hygiene & Resilience
- Rate Limiting: Protect all public and authenticated endpoints with token bucket / sliding window limits (Redis-backed).
- Pagination: Enforce cursor-based or limit-offset pagination on all collection endpoints (default limit: 20, max limit: 100).
- Idempotency: Support `Idempotency-Key` headers for financial, checkout, or state-mutating POST requests.
- Versioning: Prefix routes with API versioning (`/api/v1/resource`).
