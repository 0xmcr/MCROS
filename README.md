# MCROS V3 — Maheshwar Chandra Roy Operating System
### Autonomous AI Engineering, Research & Production Operating System
**Created & Architected by Maheshwar Chandra Roy (`0xmcr`)**

[![CI Status](https://github.com/0xmcr/MCROS/actions/workflows/ci.yml/badge.svg)](https://github.com/0xmcr/MCROS/actions)
[![npm version](https://img.shields.io/npm/v/@mcrdev/mcros.svg)](https://www.npmjs.com/package/@mcrdev/mcros)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Antigravity](https://img.shields.io/badge/Platform-Google%20Antigravity-4285F4.svg)]()
[![Platform: Claude Code](https://img.shields.io/badge/Platform-Anthropic%20Claude-D97706.svg)]()
[![Platform: Cursor](https://img.shields.io/badge/Platform-Cursor%20%2F%20Windsurf-000000.svg)]()
[![Platform: ChatGPT](https://img.shields.io/badge/Platform-OpenAI%20ChatGPT-10A37F.svg)]()

---

## 🌟 Overview

**MCROS (Maheshwar Chandra Roy Operating System)** is an enterprise-grade, file-based AI operating system that transforms conversational LLMs into an elite, multi-agent software engineering and research organization.

Instead of writing unverified code or guessing dependencies, MCROS enforces:
- **Truth Over Confidence**: No task is marked complete without direct terminal execution evidence (passes, exit code 0).
- **Zero-Stub Policy**: No `// TODO: implement later`, no mock interfaces, no unhandled edge cases.
- **Progressive Token Budgeting**: 15 modular rules and 43 skills load on demand without blowing context window token limits.
- **Multi-Agent Orchestration**: Main Agent orchestrates specialized Subagents (Frontend, Backend, Database, QA, Security, Web3).
- **Universal Compatibility**: Works out of the box in Google Antigravity, Anthropic Claude Code, Cursor, Windsurf, OpenAI ChatGPT, and terminal CLI.
- **Self-Improving Memory**: Logs solved defects in `docs/LESSONS_LEARNED.md` to prevent recurring errors.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    User["👤 Product Owner / User"] --> Lead["👑 MCR Lead Master Agent"]
    
    subgraph Multi_Agent_Team ["Specialized Subagent Team"]
        Lead --> Plan["📋 Project Planning & Tech Stack<br/>(/mcr-project-planning)"]
        Plan --> Scaffold["🏗️ Repo Scaffolding<br/>(/mcr-repo-scaffold)"]
        Scaffold --> Frontend["🎨 Frontend & UX<br/>(/mcr-frontend-ui)"]
        Scaffold --> Backend["⚙️ Backend & API<br/>(/mcr-backend-api)"]
        Scaffold --> DB["🗄️ Database & Migration<br/>(/mcr-database-architect)"]
        Scaffold --> Web3["⛓️ Web3 & Smart Contracts<br/>(/mcr-web3-blockchain)"]
    end
    
    subgraph Quality_And_Safety ["Quality & Safety Gates"]
        Frontend & Backend & DB & Web3 --> Test["🧪 Automated Testing<br/>(/mcr-test-automation)"]
        Test --> Sec["🛡️ Defensive Security<br/>(/mcr-security-audit)"]
        Sec --> Gatekeeper["🚦 Quality Gatekeeper<br/>(/mcr-quality-gatekeeper)"]
    end
    
    Gatekeeper --> Release["🚀 Verified Production Release<br/>(/mcr-release-readiness)"]
    Release --> User
```

---

## ⚡ The 43 Master Skills Catalog

Invoke any skill directly via slash command (`/<skill-name>`) in your AI chat:

| Domain | Skill Name | Slash Command | Description |
|---|---|---|---|
| **Planning** | `mcr-project-planning` | `/mcr-project-planning` | Work Breakdown Structure (WBS), milestones, MVP scoping |
| | `mcr-tech-stack-selector` | `/mcr-tech-stack-selector` | Objective technology evaluation matrix & trade-offs |
| | `mcr-repo-scaffold` | `/mcr-repo-scaffold` | Clean architecture repository initialization |
| | `mcr-project-discovery` | `/mcr-project-discovery` | Existing codebase discovery & dependency mapping |
| **Orchestration** | `mcr-subagent-orchestrator` | `/mcr-subagent-orchestrator` | Multi-agent delegation, parallel execution & synthesis |
| **Product & Specs** | `mcr-product-spec` | `/mcr-product-spec` | Product Requirements Documents (PRD) & user journeys |
| | `mcr-tech-architecture` | `/mcr-tech-architecture` | Component architecture, data contracts & ADR records |
| | `mcr-market-research` | `/mcr-market-research` | Market research, competitive analysis & TAM/SAM/SOM |
| **Frontend & UI** | `mcr-frontend-ui` | `/mcr-frontend-ui` | Accessible (WCAG AA) components, loading/error/empty states |
| | `mcr-responsive-styling` | `/mcr-responsive-styling` | Tailwind CSS, dark mode theming, view transitions |
| **Backend & Architecture** | `mcr-backend-api` | `/mcr-backend-api` | Scalable REST/GraphQL/gRPC APIs & Zod/Pydantic validation |
| | `mcr-backend-clean-architecture` | `/mcr-backend-clean-architecture` | Clean Architecture, DDD, Controller-Service-Repository patterns |
| | `mcr-auth-security` | `/mcr-auth-security` | OAuth 2.0, JWT, sessions, RBAC/ABAC route protection |
| **Database** | `mcr-database-architect` | `/mcr-database-architect` | 3NF relational modeling, composite indexes, query tuning |
| | `mcr-db-migration` | `/mcr-db-migration` | Zero-downtime expand/contract migrations & rollbacks |
| **UX & Branding** | `mcr-brand-logo-design` | `/mcr-brand-logo-design` | Vector SVG logos, favicons, app icons, color palettes |
| | `mcr-ux-interaction-design` | `/mcr-ux-interaction-design` | Click flows, toast notification system, modals & feedback loops |
| | `mcr-motion-animation` | `/mcr-motion-animation` | High-performance 60fps animations, Framer Motion, transitions |
| **Cross-Platform & i18n** | `mcr-crossplatform-mobile-desktop` | `/mcr-crossplatform-mobile-desktop` | Android, iOS, Windows, macOS, Linux native/hybrid apps |
| | `mcr-i18n-localization` | `/mcr-i18n-localization` | Multi-language catalogs (English, Bengali, RTL), locale formats |
| **QA & Debugging** | `mcr-test-automation` | `/mcr-test-automation` | Vitest, Playwright, Pytest automated testing suites |
| | `mcr-debugger-fixer` | `/mcr-debugger-fixer` | Error stack trace analysis & surgical root-cause repair |
| **Quality & Memory**| `mcr-quality-gatekeeper` | `/mcr-quality-gatekeeper` | Anti-hallucination filter & lessons learned learning loop |
| **Security** | `mcr-security-audit` | `/mcr-security-audit` | OWASP Top 10 defensive audits & threat modeling |
| | `mcr-secrets-guard` | `/mcr-secrets-guard` | Plaintext API key leak prevention & .env hygiene |
| **AI Systems** | `mcr-rag-architect` | `/mcr-rag-architect` | Vector DBs, semantic chunking, hybrid search & RAG |
| **Web3** | `mcr-web3-blockchain` | `/mcr-web3-blockchain` | Solidity smart contracts, ERC standards, Foundry fuzzing |
| **Git & Cloud Hosting** | `mcr-cloud-hosting-domains` | `/mcr-cloud-hosting-domains` | Wholesale domain purchase, Cloudflare DNS/SSL, cloud hosting |
| | `mcr-git-workflow-github` | `/mcr-git-workflow-github` | Git feature branches, atomic commits, remote push & GitHub PRs |
| **Payments & Billing** | `mcr-payments-billing` | `/mcr-payments-billing` | Stripe, Lemon Squeezy, webhook signatures, subscription lifecycle |
| **Email & OTP Auth** | `mcr-email-otp-notifications` | `/mcr-email-otp-notifications` | Resend/SendGrid transactional emails, 6-digit OTP, SPF/DKIM |
| **Multi-Tenant SaaS** | `mcr-multitenant-saas` | `/mcr-multitenant-saas` | Multi-tenant workspaces, team invites, PostgreSQL RLS isolation |
| **SEO & Social Cards** | `mcr-seo-meta-social` | `/mcr-seo-meta-social` | OpenGraph preview cards, Schema.org JSON-LD, dynamic sitemaps |
| **Queues & Workers** | `mcr-background-jobs-queues` | `/mcr-background-jobs-queues` | BullMQ/Celery async workers, exponential backoff, DLQ queues |
| **Storage & CDN** | `mcr-file-storage-cdn` | `/mcr-file-storage-cdn` | Cloudflare R2 / S3 presigned upload URLs, direct streaming |
| **Observability** | `mcr-observability-sentry-logging` | `/mcr-observability-sentry-logging` | Structured JSON logging with correlation IDs, Sentry tracking |
| **DevOps & Cloud** | `mcr-devops-cloud` | `/mcr-devops-cloud` | Docker containerization, GitHub Actions CI/CD pipelines |
| | `mcr-release-readiness` | `/mcr-release-readiness` | Production verification gate & rollback safety check |
| | `mcr-tech-docs` | `/mcr-tech-docs` | OpenAPI/Swagger specs, developer guides & changelogs |

---

## 📜 The 15 System Rules

Rules operate in the background and govern model discipline:

1. **`00-core-operating-contract.md`** (`always_on`): Truth over confidence, non-destructive safety, creator identity.
2. **`02-professional-focus-and-anti-flirt.md`** (`always_on`): Absolute engineering focus and boundary enforcement.
3. **`05-godmode-execution-protocol.md`** (`always_on`): /GODMODE autonomous protocol: zero placeholders, enterprise-scale by default.
4. **`15-clean-code-and-documentation.md`** (`always_on`): Professional JSDoc/TSDoc/Docstrings, clean code & logic documentation.
5. **`10-research-and-market-intel.md`** (`model_decision`): Verified evidence standards.
6. **`20-product-and-architecture.md`** (`model_decision`): PRD and system architecture standards.
7. **`30-frontend-engineering.md`** (`glob`): Full component visual state handling.
8. **`40-backend-engineering.md`** (`model_decision`): Strict input validation at perimeter.
9. **`50-database-and-storage.md`** (`model_decision`): Schema normalization and safe migrations.
10. **`60-defensive-security.md`** (`model_decision`): OWASP compliance and defensive assessments.
11. **`70-qa-and-verification.md`** (`model_decision`): Test pyramid and verification evidence.
12. **`80-ai-and-automation.md`** (`model_decision`): Structured output schemas and RAG pipelines.
13. **`85-quality-and-anti-hallucination.md`** (`always_on`): Zero phantom packages, zero incomplete TODOs.
14. **`90-devops-and-release.md`** (`manual`): Production release checklist.
15. **`95-web3-blockchain-safety.md`** (`glob`): Smart contract reentrancy and gas safety.

---

## 🚀 Quick Start & Installation

### Option 1: Universal NPX One-Liner (Any Project)
Initialize MCROS inside any existing or new project directory:
```bash
npx @mcrdev/mcros init
```

### Option 2: Clone & Self-Verification
Clone the repository and run the validation suite:
```bash
git clone https://github.com/0xmcr/MCROS.git
cd MCROS
python3 scripts/validate_setup.py
```

### Option 3: Global CLI
```bash
npm install -g @mcrdev/mcros
mcros init
mcros validate
```

### 2. Start Developing
Open this repository in **Antigravity**, **Claude Code**, or **Cursor**, and prompt:
```text
"Use the MCROS workflow. I want to build a [describe your application]. First plan the architecture and select the tech stack, scaffold the project, and delegate tasks to specialized subagents. Test and verify all outputs."
```

---

## 📖 Documentation
- [Master Architecture Guide](docs/MCROS_MASTER_GUIDE.md)
- [Quickstart Prompts](docs/QUICKSTART_PROMPTS.md)
- [Lessons Learned Log](docs/LESSONS_LEARNED.md)
- [Contributing Guide](CONTRIBUTING.md)

---

## 📄 License
Released under the [MIT License](LICENSE). Copyright (c) 2026 Maheshwar Chandra Roy (MCR).
