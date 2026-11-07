---
name: mcr-database-architect
description: Design normalized relational schemas, document models, high-performance indexes, constraints, and optimized data access layers.
---

# MCR Database Architect Skill

Use this skill when designing database schemas, modeling business entities, planning indexes, optimizing slow queries, or choosing between relational and document storage.

## Data Modeling Principles

### 1. Relational Integrity (PostgreSQL, MySQL, SQLite)
- Normalize to Third Normal Form (3NF) to eliminate update anomalies.
- Enforce data integrity via database constraints:
  - `PRIMARY KEY`, `FOREIGN KEY (ON DELETE CASCADE / SET NULL / RESTRICT)`
  - `NOT NULL` guarantees on mandatory attributes
  - `UNIQUE` constraints on natural identifiers (emails, slugs, usernames)
  - `CHECK` constraints on numerical ranges or enum-like states
- Timestamps: Always include `created_at TIMESTAMPTZ DEFAULT NOW()` and `updated_at TIMESTAMPTZ DEFAULT NOW()`.

### 2. High-Performance Indexing Strategy
- Index foreign key columns used in `JOIN` clauses.
- Add composite indexes for queries filtering on multiple columns (`WHERE tenant_id = ? AND status = ? ORDER BY created_at DESC`).
- Use Partial Indexes (e.g. `CREATE INDEX ON orders (status) WHERE status = 'PENDING'`) to minimize index bloat.
- Prevent table scans by auditing queries with `EXPLAIN (ANALYZE, BUFFERS)`.

### 3. Connection Management & Pooling
- Utilize PgBouncer or connection poolers to prevent socket exhaustion.
- Enforce strict query timeouts (e.g. 5 seconds) to prevent unindexed queries from hanging database threads.
