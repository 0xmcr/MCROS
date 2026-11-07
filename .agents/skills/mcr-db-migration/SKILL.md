---
name: mcr-db-migration
description: Author deterministic, reversible database migrations, manage schema evolutions using the Expand and Contract pattern, and test rollback procedures.
---

# MCR Database Migration & Versioning Skill

Use this skill when modifying database schemas in development or production. It ensures zero data loss, minimal downtime, and reliable rollbacks.

## Migration Protocols

### 1. Deterministic & Versioned Migrations
- Use trusted migration engines (Prisma, Alembic, Drizzle Kit, Flyway, goose).
- Never modify applied migration files; always create a new incremental migration file.
- Every migration must provide both an `UP` (apply) and a `DOWN` (rollback) procedure.

### 2. Expand and Contract Pattern (Zero-Downtime)
When renaming or removing columns/tables in production:
1. Phase 1 (Expand): Add the new column/table alongside the old one. Deploy backend code that writes to both (dual-write).
2. Phase 2 (Backfill): Run an asynchronous script to backfill existing data from old to new column.
3. Phase 3 (Switch Read): Deploy backend code to read exclusively from the new column.
4. Phase 4 (Contract): Remove the old column/table in a subsequent migration after verifying stability.

### 3. Pre-Migration Verification
- Execute `migrate` against a staging database or ephemeral test container.
- Test rollback (`migrate down` or rollback script) to confirm the database returns cleanly to its prior state.
- Ensure no destructive operations (`DROP TABLE`, `DROP COLUMN`) run without explicit approval.
