---
trigger: glob
globs: "**/*.{sol,vy}"
---

# Web3 and Smart Contract Safety Rules

## 1. Reentrancy & Execution Safety
- Use Checks-Effects-Interactions (CEI) pattern across all state-mutating functions.
- Apply OpenZeppelin `ReentrancyGuard` (`nonReentrant`) on all functions transferring ETH or tokens.

## 2. Access Control & Upgradability
- Explicit role-based access control (`Ownable2Step`, `AccessControlDefaultAdminRules`).
- Never leave critical initialization functions uncallable or exposed (`initializer` guards).

## 3. Gas & Overflow Optimization
- Solidity 0.8+ built-in overflow/underflow protection.
- Optimize storage layouts (pack structs to 32-byte slots, use `immutable` and `constant` variables).
- Audit contracts with Slither, Mythril, or Foundry tests before any testnet/mainnet deployment.
