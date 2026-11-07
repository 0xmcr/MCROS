# Contributing to MCROS (Maheshwar Chandra Roy Operating System)

Thank you for your interest in contributing to **MCROS**, created by **Maheshwar Chandra Roy (MCR)**.

This project is a universal, file-based AI operating system designed for Google Antigravity, Anthropic Claude, Cursor, Windsurf, and modern agentic engineering environments.

## Contribution Guidelines

### 1. Adding New Rules (`.agents/rules/`)
All rule files must:
- Be located in `.agents/rules/<name>.md`.
- Start with valid YAML frontmatter:
  ```markdown
  ---
  trigger: always_on | model_decision | glob | manual
  description: Required if trigger is model_decision
  globs: Required if trigger is glob (e.g. "**/*.{ts,tsx}")
  ---
  ```
- Keep rules concise to respect token budgets and progressive disclosure.

### 2. Adding New Skills (`.agents/skills/`)
All skills must:
- Be placed in a dedicated subdirectory: `.agents/skills/<skill-name>/SKILL.md`.
- Start with valid YAML frontmatter:
  ```markdown
  ---
  name: <skill-name>
  description: Actionable description of what the skill does and when to invoke it.
  ---
  ```
- Use lowercase kebab-case for the skill name.
- Include step-by-step procedures, acceptance criteria, and verification commands.

### 3. Adding New Workflows (`.agents/workflows/`)
Workflows represent user-invoked, repeatable step-by-step sequences:
- Numbered naming convention: `01-...`, `02-...`.
- Explicit verification checkpoints at each phase.

### 4. Running Validation
Before submitting any pull request, run the local validator:
```bash
python3 scripts/validate_setup.py
# or
bash scripts/setup.sh
```
All rules and skills must pass validation with exit code `0`.
