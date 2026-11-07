#!/usr/bin/env node

/**
 * MCROS CLI (Maheshwar Chandra Roy Operating System)
 * One-click installer & initializer for AI agent engineering environments.
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const TARGET = process.cwd();

console.log("\x1b[36m%s\x1b[0m", `
==========================================================================
    __  _________  ____  ____  _____
   /  |/  / ____/ __ \/ __ \/ ___/
  / /|_/ / /   / /_/ / / / /\__ \\ 
 / /  / / /___/ _, _/ /_/ /___/ / 
/_/  /_/\____/_/ |_|\____//____/  
  MCROS V3 — by Maheshwar Chandra Roy (0xmcr)
==========================================================================
`);

const args = process.argv.slice(2);
const command = args[0] || "help";

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
    for (const item of fs.readdirSync(src)) {
      copyRecursive(path.join(src, item), path.join(dest, item));
    }
  } else {
    fs.copyFileSync(src, dest);
  }
}

if (command === "init") {
  console.log("Initializing MCROS in:", TARGET);
  
  const itemsToCopy = [
    ".agents",
    "AGENTS.md",
    "CLAUDE.md",
    ".cursorrules",
    ".gitignore",
    "docs",
    "scripts",
    "README.md"
  ];

  for (const item of itemsToCopy) {
    const srcPath = path.join(ROOT, item);
    const destPath = path.join(TARGET, item);
    if (item === "README.md" && fs.existsSync(destPath)) {
      // Don't overwrite existing user README
      continue;
    }
    if (fs.existsSync(srcPath)) {
      console.log(`- Installing ${item}...`);
      copyRecursive(srcPath, destPath);
    }
  }

  console.log("\n\x1b[32m%s\x1b[0m", "✓ MCROS successfully installed in target workspace!");
  console.log("Run 'python3 scripts/validate_setup.py' to verify.");
} else if (command === "validate") {
  try {
    execSync("python3 scripts/validate_setup.py", { stdio: "inherit" });
  } catch (err) {
    process.exit(1);
  }
} else if (command === "feedback") {
  const issueUrl = "https://github.com/0xmcr/MCROS/issues/new/choose";
  console.log("\x1b[32m%s\x1b[0m", "Opening MCROS Community Feedback & Issue Tracker:");
  console.log(issueUrl);
  try {
    const openCmd = process.platform === "darwin" ? "open" : process.platform === "win32" ? "start" : "xdg-open";
    execSync(`${openCmd} "${issueUrl}"`, { stdio: "ignore" });
  } catch (_) {
    // If browser open fails in headless env, URL is already printed above
  }
} else {
  console.log(`
Usage:
  npx mcros init       Initialize MCROS inside the current workspace
  npx mcros validate   Run the static rules and skills verification suite
  npx mcros feedback   Open GitHub issues to report bugs or submit feature requests
  npx mcros help       Display this manual
  `);
}
