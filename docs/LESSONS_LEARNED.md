# MCROS Lessons Learned & Continuous Improvement Log

> This document records diagnosed root causes, solved bugs, and architectural takeaways.
> All MCR agents and subagents must inspect this log before starting new development tasks to prevent repeating past errors.

## Log Format
- **Date**: YYYY-MM-DD
- **Area**: Frontend / Backend / Database / Auth / Security / DevOps
- **Issue**: Description of the defect, build error, or unexpected behavior.
- **Root Cause**: Why it happened.
- **Remedy & Prevention**: What was done to fix it and the rule to follow in future.

---

### Initial Entry
- **Date**: 2026-11-07
- **Area**: MCROS Workspace Configuration
- **Issue**: Validation failed on clean repository due to missing `.agents/` modular rules and skills directories.
- **Root Cause**: Workspace initialization requires progressive disclosure rules with YAML frontmatter triggers and skill directories.
- **Remedy & Prevention**: Standardized `.agents/rules/` (with `trigger` tags) and `.agents/skills/` (with `name` and `description` frontmatter) and automated verification via `scripts/validate_setup.py`.
