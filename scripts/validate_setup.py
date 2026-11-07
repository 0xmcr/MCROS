#!/usr/bin/env python3
"""Validate FRONTIER AI OS V3 workspace files and Antigravity rule frontmatter.

This checks local kit structure only. It does not verify Antigravity runtime loading,
security posture, or project correctness.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "README.md",
    ".agents/rules/00-core-operating-contract.md",
    ".agents/workflows/01-idea-to-product.md",
    ".agents/skills/project-discovery/SKILL.md",
    "docs/templates/PRD.md",
]
VALID_TRIGGERS = {"always_on", "model_decision", "glob", "manual"}

def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    rules_dir = ROOT / ".agents" / "rules"
    for path in sorted(rules_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}: malformed frontmatter")
            continue
        fm = match.group(1)
        trigger = re.search(r"(?m)^trigger:\s*([a-z_]+)\s*$", fm)
        if not trigger or trigger.group(1) not in VALID_TRIGGERS:
            errors.append(f"{path.relative_to(ROOT)}: invalid or missing trigger")
        if "model_decision" in fm and not re.search(r"(?m)^description:\s*.+$", fm):
            errors.append(f"{path.relative_to(ROOT)}: model_decision requires description")
        if re.search(r"(?m)^trigger:\s*glob\s*$", fm) and not re.search(r"(?m)^globs?:\s*.+$", fm):
            errors.append(f"{path.relative_to(ROOT)}: glob trigger requires globs")

    skills_dir = ROOT / ".agents" / "skills"
    skills_count = 0
    if skills_dir.is_dir():
        for skill_path in sorted(skills_dir.glob("*/SKILL.md")):
            skills_count += 1
            content = skill_path.read_text(encoding="utf-8")
            if not content.startswith("---\n"):
                errors.append(f"{skill_path.relative_to(ROOT)}: missing YAML frontmatter")
                continue
            match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
            if not match:
                errors.append(f"{skill_path.relative_to(ROOT)}: malformed frontmatter")
                continue
            fm = match.group(1)
            if not re.search(r"(?m)^name:\s*[\w-]+", fm):
                errors.append(f"{skill_path.relative_to(ROOT)}: missing or invalid skill name")
            if not re.search(r"(?m)^description:\s*.+$", fm):
                errors.append(f"{skill_path.relative_to(ROOT)}: missing skill description")

    if errors:
        print("FRONTIER AI OS V3 validation: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FRONTIER AI OS V3 validation: PASSED")
    print(f"Workspace: {ROOT}")
    print(f"Rules checked: {len(list(rules_dir.glob('*.md')))}")
    print(f"Skills checked: {skills_count}")
    print("Note: runtime discovery and agent behavior must be checked in Antigravity.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
