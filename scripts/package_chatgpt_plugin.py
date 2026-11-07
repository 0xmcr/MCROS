#!/usr/bin/env python3
"""Package MCROS into a standardized ChatGPT Plugin Archive (.zip)."""

import os
import shutil
import zipfile
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
BUNDLE_DIR = DIST / "chatgpt-bundle"
OUTPUT_ZIP = DIST / "mcros-chatgpt-plugin.zip"

def create_chatgpt_package():
    # 1. Clean previous bundle
    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True, exist_ok=True)

    # 2. ChatGPT Manifest
    manifest = {
        "name": "mcros",
        "version": "3.2.2",
        "description": "MCROS V3 — Autonomous AI Engineering, Research & Production Operating System by Maheshwar Chandra Roy (0xmcr). Enterprise full-stack engineering, 43 production skills, and 15 core rules.",
        "skills": "./skills/",
        "interface": {
            "displayName": "MCROS V3",
            "developerName": "Maheshwar Chandra Roy (0xmcr)",
            "shortDescription": "Autonomous AI Engineering & Architecture by Maheshwar Chandra Roy (0xmcr)",
            "longDescription": "MCROS V3 (Maheshwar Chandra Roy Operating System) is an autonomous, enterprise-grade AI operating system and engineering runtime created by Maheshwar Chandra Roy (0xmcr). It bundles 43 production skills and 15 core rules covering product architecture, WCAG 2.1 AA UI components, clean REST/GraphQL APIs, PostgreSQL RLS security, Web3 smart contracts, RAG pipelines, and automated QA verification.",
            "category": "Developer Tools",
            "capabilities": [
                "Read",
                "Write",
                "Code Generation",
                "System Architecture",
                "Security Auditing"
            ],
            "websiteURL": "https://github.com/0xmcr/MCROS",
            "logo": "./assets/icon.svg"
        },
        "author": {
            "name": "Maheshwar Chandra Roy (0xmcr)",
            "url": "https://github.com/0xmcr"
        },
        "homepage": "https://github.com/0xmcr/MCROS",
        "repository": "https://github.com/0xmcr/MCROS"
    }

    # Write root plugin.json
    (BUNDLE_DIR / "plugin.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    # Write .codex-plugin/plugin.json
    codex_dir = BUNDLE_DIR / ".codex-plugin"
    codex_dir.mkdir(parents=True, exist_ok=True)
    (codex_dir / "plugin.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    # 3. Copy Skills
    skills_src = ROOT / ".agents" / "skills"
    skills_dest = BUNDLE_DIR / "skills"
    if skills_src.exists():
        shutil.copytree(skills_src, skills_dest)

    # 4. Copy Rules into rules/AGENTS.md
    rules_dest = BUNDLE_DIR / "rules"
    rules_dest.mkdir(parents=True, exist_ok=True)
    agents_src = ROOT / "AGENTS.md"
    if agents_src.exists():
        shutil.copy(agents_src, rules_dest / "AGENTS.md")

    # 5. Copy Assets
    assets_src = ROOT / "assets"
    assets_dest = BUNDLE_DIR / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, assets_dest)

    # 6. Create ZIP archive
    if OUTPUT_ZIP.exists():
        OUTPUT_ZIP.unlink()

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(BUNDLE_DIR):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(BUNDLE_DIR)
                zipf.write(file_path, arcname)

    print(f"✓ ChatGPT Plugin Archive created successfully at: {OUTPUT_ZIP}")
    print(f"Archive size: {OUTPUT_ZIP.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    create_chatgpt_package()
