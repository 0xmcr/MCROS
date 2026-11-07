---
trigger: always_on
---

# Anti-Hallucination, Quality Guardrails, and Self-Improvement

## 1. Zero-Toleration for Fake or Incomplete Code
Every agent, subagent, and model invocation must strictly adhere to the following:
- No Dangling Placeholders: Never leave critical business logic as `// TODO: implement later` or dummy stubs unless explicitly instructed by the user.
- Real Packages Only: Never hallucinate npm/pip/cargo packages or fabricate API method names. Always verify packages exist in the lockfile or official documentation.
- Complete Interfaces: Every button, link, form, or route created must be functional or have proper error/loading boundaries.

## 2. Evidence Before Completion
- An agent must never declare a task "completed" or "fixed" based solely on assumption.
- Direct execution evidence (test passes, build success, linter exit code 0) is mandatory before marking tasks as VERIFIED.

## 3. Continuous Self-Improvement Loop
- When an error, crash, or unexpected behavior is detected, document the root cause and remedy in `docs/LESSONS_LEARNED.md`.
- Inspect previous lessons learned before starting complex tasks to ensure past mistakes are never repeated.
