---
name: mcr-web3-blockchain
description: Design, write, test, and audit secure Web3 smart contracts (Solidity, Foundry, Hardhat) and decentralized application (dApp) integrations.
---

# MCR Web3 & Blockchain Engineering Skill

Use this skill when developing decentralized applications (dApps), writing Ethereum/EVM smart contracts, authoring Foundry/Hardhat test suites, or conducting defensive smart contract security audits.

## Web3 Engineering Standards

### 1. Smart Contract Development (Solidity)
- Use standard, battle-tested libraries (OpenZeppelin Contracts).
- Adhere to token standards: ERC-20 (Fungible), ERC-721 / ERC-1155 (Non-Fungible), ERC-4626 (Tokenized Vaults).
- Implement Checks-Effects-Interactions (CEI) to prevent reentrancy attacks.
- Guard against front-running and MEV by implementing commit-reveal schemes or slippage tolerances.

### 2. Testing & Fuzzing (Foundry)
- Write 100% invariant and property-based fuzz tests (`testFuzz_...`).
- Simulate edge cases: zero addresses, zero amounts, overflow boundaries, unauthorized callers.
- Benchmark gas consumption across key transactions using Foundry gas snapshots.

### 3. dApp Integration & Client Libraries
- Connect frontend via Wagmi, Viem, or Ethers.js.
- Handle wallet states: disconnected, connecting, wrong network, insufficient funds for gas, user rejected transaction.
- Provide real-time transaction toast notifications (Submitted, Mining, Confirmed, Failed).
