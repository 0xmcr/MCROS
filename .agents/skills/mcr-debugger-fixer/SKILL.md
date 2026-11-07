---
name: mcr-debugger-fixer
description: Diagnose complex bugs, analyze stacktraces and error logs, isolate root causes, and implement minimal, surgical fixes without regressions.
---

# MCR Debugger & Bug Fixer Skill

Use this skill when diagnosing runtime errors, unhandled exceptions, application crashes, failing tests, or unexpected UI/API behavior.

## Systematic Debugging Protocol

### 1. Capture & Reproduce
- Capture the exact error message, stack trace, HTTP status, and reproduction steps.
- Create a minimal failing test case or reproduction script before touching application code.

### 2. Root-Cause Analysis (5 Whys)
- Differentiate between the symptom (e.g. `TypeError: Cannot read properties of undefined`) and the root cause (e.g. missing null check after an upstream API timeout).
- Trace data flow upstream to determine where unvalidated or corrupt data entered the pipeline.

### 3. Surgical & Minimal Remediation
- Formulate a targeted fix addressing the root cause directly.
- Avoid broad refactorings or rewriting unrelated files during a bug fix.
- Add defensive guards and explicit error logging where appropriate.

### 4. Verification & Regression Testing
- Run the previously failing test to verify the fix works.
- Run the full test suite to confirm no existing functionality was broken.
- Document root cause, resolution, and prevention steps in PR/commit message.
