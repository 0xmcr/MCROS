# MCROS (Maheshwar Chandra Roy Operating System) — Claude Code Contract

This repository is governed by **FRONTIER AI OS V3 / MCROS**.

## Operating Guidelines for Claude
1. **Core Invariants**:
   - Truth over confidence: Never hallucinate libraries, endpoints, or completion status.
   - Inspect before acting: Always read project structure, package manifests, and `docs/PROJECT_CONTEXT.md` first.
   - Evidence-based completion: Run builds/tests and verify clean command outputs before reporting completion.
   - Zero-destruction: Never delete user data or overwrite working systems without explicit user approval.
2. **Modular Rules**:
   - Consult `.agents/rules/` for specialist domain rules (Frontend, Backend, Database, Security, QA, Web3).
   - Consult `.agents/skills/` for execution procedures and runbooks.
3. **Anti-Hallucination & Quality**:
   - Check `docs/LESSONS_LEARNED.md` before starting tasks.
   - Never output dangling `// TODO: implement later` stubs in core business flows.
4. **Validation**:
   - Run `python3 scripts/validate_setup.py` to verify workspace compliance.
