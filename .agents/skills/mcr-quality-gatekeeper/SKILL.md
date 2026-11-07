---
name: mcr-quality-gatekeeper
description: Inspect and filter generated code against hallucinations, placeholder TODOs, broken imports, and ensure continuous self-learning via lessons learned.
---

# MCR Quality Gatekeeper & Self-Improvement Skill

Use this skill as an automated verification barrier to prevent hallucinated code, broken dependencies, dangling stubs, or recurring bugs. It enforces continuous self-learning across the entire multi-agent team.

## Gatekeeping Protocol

### 1. Anti-Hallucination & Flaw Detection
Before approving any code delivery, verify:
- [ ] No phantom imports: All imported packages exist in `package.json`, `pyproject.toml`, or standard library.
- [ ] No empty stubs: No core user journeys terminate in `// TODO: Implement later` or empty `pass`.
- [ ] No dead controls: Every interactive button, form field, and route has working event listeners or handlers.
- [ ] Type-safety: Zero implicit `any` types or unvalidated JSON parsing without Zod/Pydantic schemas.

### 2. Self-Learning Loop (`docs/LESSONS_LEARNED.md`)
Whenever a defect or failed build occurs during execution:
1. Record:
   - Date & Issue Summary.
   - Root Cause (e.g. "Next.js 14 server component used client-side hook without `'use client'` directive").
   - Applied Solution & Prevention Rule.
2. Read `docs/LESSONS_LEARNED.md` at the start of new epics to avoid repeating verified mistakes.

### 3. Automated Pre-Flight Check
Run linting and type-checks (`npm run lint`, `npx tsc --noEmit`, `ruff check .`) to prove code quality.
