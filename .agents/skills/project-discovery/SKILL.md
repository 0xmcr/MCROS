---
name: project-discovery
description: Discover and inspect existing project codebase, detect technology stack, frameworks, package manifests, entry points, and populate project context and architecture documentation.
---

# Project Discovery Skill

Use this skill when initializing or auditing a new workspace or existing project. It guides systematic inspection of the codebase without modifying or breaking existing implementations.

## Objectives
1. Map repository layout, entry points, and directory structure.
2. Detect language runtimes, package managers, frameworks, and database dependencies.
3. Identify existing test harnesses, build commands, and CI configurations.
4. Populate `docs/PROJECT_CONTEXT.md` and `docs/ARCHITECTURE.md` with verified facts.

## Inspection Procedure

### Step 1: Filesystem Layout & Manifest Inspection
Inspect root files to identify technology stack:
- Node.js / TypeScript: `package.json`, `tsconfig.json`, `pnpm-lock.yaml`, `package-lock.json`, `bun.lockb`
- Python: `pyproject.toml`, `requirements.txt`, `Pipfile`, `setup.py`, `poetry.lock`
- Rust: `Cargo.toml`, `Cargo.lock`
- Go: `go.mod`, `go.sum`
- Java / Kotlin: `pom.xml`, `build.gradle`, `build.gradle.kts`
- Infrastructure / Docker: `Dockerfile`, `docker-compose.yml`, `.github/workflows/`

### Step 2: Architecture & Entry Point Mapping
- Locate application entry points (`src/index.ts`, `app/main.py`, `cmd/server/main.go`, `pages/_app.tsx`, `app/layout.tsx`).
- Trace data stores (PostgreSQL, SQLite, Redis, MongoDB, Prisma/Drizzle/SQLAlchemy models).
- Identify external service integrations, authentication providers, and third-party APIs.

### Step 3: Test & Build Verification
- Inspect test scripts in package manifests or test directories (`tests/`, `__tests__/`, `spec/`).
- Execute a dry-run or read-only test command if available (e.g., `npm test -- --passWithNoTests`, `pytest --collect-only`).

### Step 4: Populate Project Documentation
Document discovered facts into:
- `docs/PROJECT_CONTEXT.md`: Stack, dependencies, commands, environment variable names.
- `docs/ARCHITECTURE.md`: Components, trust boundaries, data flows, and topology.
