---
name: mcr-database-architect
description: Design normalized relational schemas, document models, high-performance indexes, constraints, and optimized data access layers.
---

# MCR Enterprise Database Architect Skill

Use this skill when designing database schemas, establishing relational integrity constraints, optimizing slow queries, and planning index strategies.

## Supporting Resources & Submodules
- Query & Index Diagnostic Script: [analyze_queries.sql](./scripts/analyze_queries.sql)
- Production 3NF Reference Schema: [ecommerce-schema.sql](./examples/ecommerce-schema.sql)
- Exhaustive Indexing Manual: [indexing-deep-dive.md](./references/indexing-deep-dive.md)

---

## 1. Schema Design Protocol

### Step 1: Relational Normalization (3NF)
- Eliminate update anomalies by normalizing entities (Users, Products, Orders, Order Items). See [ecommerce-schema.sql](./examples/ecommerce-schema.sql).
- Enforce business guarantees at the database engine level via `CHECK`, `UNIQUE`, and `NOT NULL` constraints.
- Foreign Keys: Always define explicit `ON DELETE` behavior (`CASCADE`, `RESTRICT`, or `SET NULL`).

### Step 2: High-Performance Indexing Strategy
- Consult [indexing-deep-dive.md](./references/indexing-deep-dive.md) before creating indexes.
- Always index foreign key columns to eliminate table lock escalations on deletions.
- Utilize Composite Indexes following the `Equality -> Inequality -> Sort` rule.
- Implement Partial Indexes on high-cardinality status filters (`WHERE status = 'PENDING'`).

### Step 3: Performance Diagnostics & Maintenance
- Execute `./scripts/analyze_queries.sql` to identify slow queries and unused indexes.
- Audit execution plans with `EXPLAIN (ANALYZE, BUFFERS)`.
- Enforce strict client query timeouts (e.g. 5000ms) to prevent thread exhaustion.
