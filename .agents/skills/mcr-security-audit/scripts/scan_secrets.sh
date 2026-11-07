#!/usr/bin/env bash
# ==============================================================================
# MCR Defensive Secrets & Credential Scanner
# Scans workspace for plaintext credentials, private keys, and API tokens.
# ==============================================================================
set -euo pipefail

echo "=========================================================="
echo "🛡️  MCR Defensive Secrets & Credential Scanner"
echo "=========================================================="

WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
cd "${WORKSPACE_ROOT}"

FOUND_SECRETS=0

# Pattern list for high-risk credentials
PATTERNS=(
    "AKIA[0-9A-Z]{16}"                  # AWS Access Key ID
    "ghp_[0-9a-zA-Z]{36}"               # GitHub Personal Access Token
    "BEGIN RSA PRIVATE KEY"              # Private RSA Key
    "BEGIN OPENSSH PRIVATE KEY"          # Private OpenSSH Key
    "postgres:\/\/[^:]+:[^@]+@"          # Postgres connection string with password
    "mongodb(\+srv)?:\/\/[^:]+:[^@]+@"   # MongoDB connection string with password
)

echo "Scanning tracked and untracked files (excluding .git, node_modules)..."

for pattern in "${PATTERNS[@]}"; do
    MATCHES=$(grep -rnE --exclude-dir=".git" --exclude-dir="node_modules" --exclude-dir=".venv" --exclude=".env.example" "${pattern}" . || true)
    if [ -n "${MATCHES}" ]; then
        echo -e "\n🚨 POTENTIAL SECRET EXPOSURE DETECTED (Pattern: ${pattern}):"
        echo "${MATCHES}"
        FOUND_SECRETS=$((FOUND_SECRETS + 1))
    fi
done

if [ ${FOUND_SECRETS} -eq 0 ]; then
    echo -e "\n✅ Zero exposed credentials detected. Workspace passes secrets hygiene check."
    exit 0
else
    echo -e "\n❌ Security scan FAILED: Found ${FOUND_SECRETS} potential secret exposures. Rotate credentials immediately!"
    exit 1
fi
