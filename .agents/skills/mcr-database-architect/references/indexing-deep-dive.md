# MCR Database Indexing & Query Optimization Deep Dive

---

## 1. Index Type Decision Framework (PostgreSQL)

| Index Type | Algorithmic Structure | Best Used For | Anti-Patterns (Avoid When) |
|---|---|---|---|
| **B-Tree** | Balanced Multi-way Tree | Equality (`=`) and range (`<`, `<=`, `>`, `>=`, `BETWEEN`, `ORDER BY`). Default index. | Full-text search or JSON array containment. |
| **GIN** | Generalized Inverted Index | JSONB document search (`?`, `@>`), Array tags, Full-Text Search (tsvector). | High-frequency write-heavy OLTP tables (slow to update). |
| **GiST** | Generalized Search Tree | Geometric coordinates (PostGIS), spatial overlap, IP range containment. | Standard scalar number/text lookups. |
| **BRIN** | Block Range Index | Massive time-series append-only tables (100M+ rows sorted physically by timestamp). | Highly updated, fragmented, or out-of-order data. |

---

## 2. The Rule of Composite Index Ordering: (Equality -> Inequality -> Sort)
When creating a multi-column composite index:
1. First column: The column filtered with exact equality (`WHERE tenant_id = 'abc'`).
2. Second column: The column filtered with range or inequality (`AND created_at >= '2026-01-01'`).
3. Third column: The column used in sorting (`ORDER BY id DESC`).

Example:
```sql
-- Optimal index for: WHERE tenant_id = ? AND status = ? ORDER BY created_at DESC
CREATE INDEX idx_tenants_status_created ON orders (tenant_id, status, created_at DESC);
```

---

## 3. Partial Indexes (The Secret to Blazing Fast Queries)
Instead of indexing an entire table of 10 million rows, index only the 1% of active records:
```sql
-- Index size is 99% smaller; writes to completed orders have zero index overhead!
CREATE INDEX idx_unprocessed_jobs ON background_jobs (priority, scheduled_at)
WHERE status = 'QUEUED';
```

---

## 4. Query Profiling with EXPLAIN (ANALYZE, BUFFERS)
Never assume an index is working without inspecting actual disk and buffer statistics:
```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)
SELECT id, total_cents FROM orders WHERE user_id = '...' ORDER BY created_at DESC LIMIT 20;
```
Look for:
- `Seq Scan`: Table scan reading every disk block (indicates missing index).
- `Index Scan` / `Bitmap Index Scan`: Targeted B-Tree lookup (optimal).
- `Buffers: shared hit=X read=0`: Query answered 100% from RAM buffer cache without hitting slow SSD/disk!
