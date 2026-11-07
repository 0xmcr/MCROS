---
name: mcr-subagent-orchestrator
description: Orchestrate multi-agent workflows where a Main Agent delegates specialized tasks to subagents (Architect, Frontend, Backend, Database, QA, Security), tracks progress, and synthesizes final deliverables.
---

# MCR Subagent Orchestrator Skill

Use this skill when orchestrating complex engineering or research projects requiring multi-agent delegation. It coordinates specialized subagents to divide labor, execute in parallel, and synthesize findings into a unified, verified report.

## Orchestration Architecture

```
                  ┌──────────────────────────────┐
                  │    MCR Master Agent (Lead)   │
                  └──────────────┬───────────────┘
                                 │
     ┌──────────────┬────────────┼────────────┬──────────────┐
     ▼              ▼            ▼            ▼              ▼
┌─────────┐   ┌───────────┐ ┌─────────┐ ┌───────────┐ ┌────────────┐
│Research │   │ Frontend  │ │ Backend │ │ Database  │ │  Security  │
│Subagent │   │ Subagent  │ │Subagent │ │ Subagent  │ │  & QA Sub  │
└─────────┘   └───────────┘ └─────────┘ └───────────┘ └────────────┘
```

## Subagent Delegation Protocol

### 1. Task Definition & Boundary Setting
Before delegating via `invoke_subagent`:
- Define exact role: e.g. "Frontend Engineer", "Database Specialist", "Security Auditor".
- Provide clear context: File paths, schemas, API contracts, acceptance criteria.
- State strict boundaries: Subagents must NOT modify files outside their assigned scope.

### 2. Execution & Status Tracking
Track subagent task lifecycle:
- `PENDING`: Task defined and queued.
- `IN_PROGRESS`: Subagent actively executing.
- `BLOCKED`: Dependency missing (e.g. backend waiting on database schema).
- `COMPLETED`: Subagent has delivered code/findings.
- `VERIFIED`: Master agent has independently tested and verified the result.

### 3. Synthesis & Final Report
The Master Agent:
1. Gathers outputs from each subagent.
2. Resolves cross-boundary conflicts (e.g. frontend type mismatches with backend API schema).
3. Executes integration test suites across all modified components.
4. Generates a comprehensive completion report with direct verification evidence.
