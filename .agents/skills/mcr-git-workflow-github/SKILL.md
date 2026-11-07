---
name: mcr-git-workflow-github
description: Automate daily Git operations, Conventional Commits, remote repository push, and GitHub Pull Request (PR) lifecycle via terminal commands.
---

# MCR Git & GitHub PR Automation Skill

Use this skill when initializing remotes, creating feature branches, staging atomic commits, pushing changes to GitHub, creating Pull Requests via CLI, or managing code merges.

## Terminal Command Recipes

### 1. Connecting Local Repo to Remote GitHub
```bash
# Set default branch
git branch -M main

# Link remote origin (replace with your repo URL)
git remote add origin https://github.com/<username>/<repo-name>.git

# Initial push to GitHub
git push -u origin main
```

### 2. Feature Branching & Atomic Commits
Never commit directly to `main` during feature development:
```bash
# Create and switch to a descriptive branch
git checkout -b feature/auth-oauth-login
# or
git checkout -b fix/payment-webhook-timeout

# Check status of changed files
git status

# Stage specific files
git add <filename>
# or stage all tracked changes
git add .
```

### 3. Conventional Commit Standard
Follow structured, human-readable commit messages:
```bash
# Features
git commit -m "feat(auth): implement Google OAuth 2.0 PKCE flow"

# Bug fixes
git commit -m "fix(api): handle database connection timeout with exponential retry"

# Refactoring
git commit -m "refactor(db): optimize user order query with composite index"

# Documentation
git commit -m "docs: update API contract and deployment instructions"
```

### 4. Pushing & Pull Request (PR) Creation
Push the feature branch to GitHub and create a Pull Request directly from the terminal using GitHub CLI (`gh`):
```bash
# Push branch to remote
git push -u origin feature/auth-oauth-login

# Create Pull Request using gh CLI
gh pr create \
  --title "feat(auth): implement Google OAuth 2.0 PKCE flow" \
  --body "### Summary of Changes
- Integrated Google OAuth 2.0 with PKCE security.
- Added session cookie handlers.
- Verified 100% passing tests via Vitest." \
  --base main

# Check PR status and CI checks
gh pr checks
gh pr status

# Merge PR after approval and CI pass
gh pr merge --squash --delete-branch
```
