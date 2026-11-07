---
trigger: model_decision
description: Use when designing database schemas, writing migrations, indexing, data access queries, or planning backup and recovery.
---

# Database and Storage Engineering

## Schema Design & Integrity
- Normalize relational schemas to 3NF unless denormalization is backed by explicit query benchmarks.
- Enforce foreign keys, unique constraints, check constraints, and non-null guarantees at the database level.
- Document entity relationships and storage models clearly.

## Migrations & Versioning
- Use reversible, deterministic migration scripts (e.g. Prisma, Alembic, Flyway, goose).
- Never execute destructive migrations (`DROP COLUMN`, `DROP TABLE`) in production without dual-write/shadow deprecation phases.
- Zero-downtime migration strategy: Expand and Contract pattern for schema evolutions.

## Query Performance & Indexing
- Profile queries with `EXPLAIN ANALYZE` or equivalent tools.
- Add indexes covering high-cardinality search filters, sort keys, and join conditions.
- Prevent N+1 queries using dataloaders or eager joins.
- Use connection pooling (PgBouncer, built-in poolers) and strict query timeouts.
