# MCR Enterprise Backend API Guidelines & Standards

---

## 1. HTTP Status Code Decision Matrix

Never return `200 OK` for an error state. Use standard RFC-compliant HTTP status codes:

| Code | Status | Meaning & Exact Usage |
|---|---|---|
| **200** | `OK` | Standard successful response for `GET`, `PUT`, or `PATCH`. |
| **201** | `Created` | Successful entity creation via `POST`. Must return `Location` header or created object. |
| **204** | `No Content` | Successful deletion via `DELETE` where no response body is needed. |
| **400** | `Bad Request` | Malformed JSON or request payload failing validation schema checks. |
| **401** | `Unauthorized` | Missing or invalid authentication token (JWT / Session). |
| **403** | `Forbidden` | Authenticated caller lacks permission or RBAC role to access resource. |
| **404** | `Not Found` | Target resource URI or ID does not exist. |
| **409** | `Conflict` | State conflict (e.g. duplicate email, unique constraint violation). |
| **422** | `Unprocessable Entity` | Valid syntax, but semantic business rules violated. |
| **429** | `Too Many Requests` | Rate limit exceeded. Must include `Retry-After` header. |
| **500** | `Internal Server Error` | Unhandled runtime exception or crash. Strip internal stack traces from client! |
| **503** | `Service Unavailable` | Downstream dependency or database maintenance. |

---

## 2. Idempotency Key Architecture
All state-mutating payment, checkout, or batch operations must require an `Idempotency-Key` header:
- Client generates a UUID v4 and sends: `Idempotency-Key: 7b9a5c8e-324f-4a1e-8e81-3c5b8d9f1a2b`.
- Server checks Redis cache:
  - If key exists with state `COMPLETED`: Return cached response immediately without re-executing logic.
  - If key exists with state `PROCESSING`: Return `409 Conflict` (Concurrent request in progress).
  - If key is new: Store with state `PROCESSING`, execute logic, update to `COMPLETED` with 24h TTL.

---

## 3. High-Performance Pagination Patterns

### Offset-Based Pagination (Simple catalogs)
- Query: `GET /api/v1/articles?page=2&limit=20`
- Limitation: Degrades at high offsets (`OFFSET 100000` scans 100,000 rows).

### Keyset / Cursor-Based Pagination (Recommended for scale)
- Query: `GET /api/v1/articles?limit=20&cursor=art_20261107_9921`
- SQL Implementation:
  ```sql
  SELECT id, title, created_at
  FROM articles
  WHERE (created_at, id) < (:cursor_created_at, :cursor_id)
  ORDER BY created_at DESC, id DESC
  LIMIT 21;
  ```
- Constant O(1) performance regardless of table depth.
