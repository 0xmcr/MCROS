#!/usr/bin/env bash
# ==============================================================================
# MCROS (Maheshwar Chandra Roy Operating System) — Setup & Validation Script
# ==============================================================================
set -euo pipefail

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "=========================================================================="
echo "    __  _________  ____  ____  _____"
echo "   /  |/  / ____/ __ \/ __ \/ ___/"
echo "  / /|_/ / /   / /_/ / / / /\__ \ "
echo " / /  / / /___/ _, _/ /_/ /___/ / "
echo "/_/  /_/\____/_/ |_|\____//____/  "
echo "  MCROS V3 — by Maheshwar Chandra Roy (MCR)"
echo "=========================================================================="
echo -e "${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo -e "${YELLOW}[1/3] Verifying Python 3 runtime...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 is required but not installed.${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✓ Detected ${PYTHON_VERSION}${NC}"

echo -e "\n${YELLOW}[2/3] Running MCROS Rules, Skills & Workflows Validation...${NC}"
python3 "${SCRIPT_DIR}/validate_setup.py"

echo -e "\n${YELLOW}[3/3] Checking Git Repository Status...${NC}"
if [ -d "${ROOT_DIR}/.git" ]; then
    echo -e "${GREEN}✓ Git repository is initialized.${NC}"
else
    echo -e "${YELLOW}! Git is not initialized. Run 'git init' to enable version control.${NC}"
fi

echo -e "\n${GREEN}=========================================================================="
echo "✓ MCROS is fully initialized, verified, and ready to engineer!"
echo "==========================================================================${NC}"
