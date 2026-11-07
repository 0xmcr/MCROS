# MCROS V3 — Platform Compatibility, Architecture & Capabilities Matrix
**Created & Architected by Maheshwar Chandra Roy (`0xmcr`)**  
**Official GitHub Repository**: [https://github.com/0xmcr/MCROS](https://github.com/0xmcr/MCROS)  
**Author Profile**: [https://github.com/0xmcr](https://github.com/0xmcr)

---

## 1. Executive Overview

**MCROS V3 (Maheshwar Chandra Roy Operating System)** is an autonomous, enterprise-grade AI operating system and engineering runtime designed to execute complex, multi-tier software projects from scratch to production.

Unlike superficial AI prompt packs or simple snippets, MCROS operates as a deterministic, test-driven engineering platform. It enforces:
- **Zero-Stub Policy (`05-godmode-execution-protocol.md`)**: No `// TODO: implement later`, no mock interfaces, no unhandled edge cases.
- **Evidence-Based Delivery (`00-core-operating-contract.md`)**: A task is never marked complete without concrete command execution, linting, and automated test passes.
- **Strict Professional Focus (`02-professional-focus-and-anti-flirt.md`)**: Maintains the posture of a Principal Systems Architect and deflects off-topic distractions.
- **Universal Cross-Platform Execution**: Seamlessly operates across Google Antigravity, Anthropic Claude Code, Cursor IDE, Windsurf, GitHub Copilot, and independent Node.js CLI runtimes.

---

## 2. Multi-Platform Support Matrix

MCROS V3 provides native entrypoints and configuration adapters for every major AI coding environment:

| Platform / Runtime | Configuration Entrypoint | Mechanism & Features |
|---|---|---|
| **Google Antigravity** | `AGENTS.md`, `plugin.json`, `.agents/rules/`, `.agents/skills/` | Full native agent operating contract, dynamic rule triggers (`always_on`, `model_decision`, `glob`, `manual`), 43 specialized skills, multi-agent orchestration, sidecar support. |
| **Anthropic Claude Code** | `CLAUDE.md` | Contextual system prompt integration, single-command initialization, test-first loop execution, autonomous bash tool usage. |
| **Cursor & Windsurf IDE** | `.cursorrules` | IDE context rules, strict TypeScript typing guidelines, file-specific linting rules, zero-placeholder enforcement. |
| **OpenAI / ChatGPT / Copilot** | `AGENTS.md`, `CLAUDE.md` | Universal markdown contract that can be loaded into system instructions or custom GPT knowledge base. |
| **CLI / NPM Package** | `package.json`, `bin/mcros.js` | Installable in any directory via `npx mcros init` or globally via `npm i -g mcros`. Includes deterministic self-test `mcros validate`. |

---

## 3. Comprehensive 43-Skill Catalog

MCROS V3 organizes its 43 production skills into logical domains. Each skill contains self-contained executable guides, shell or Python automation scripts, complete TypeScript/Python reference implementations, and operational runbooks.

### Domain 1: Discovery, Planning & Product Architecture
1. **`mcr-project-discovery`**: Auto-detects tech stacks, dependency trees, entrypoints, and generates `docs/PROJECT_CONTEXT.md` and `docs/ARCHITECTURE.md`.
2. **`mcr-product-spec`**: Generates exhaustive Product Requirements Documents (PRDs), user personas, acceptance criteria (Given-When-Then), and edge cases.
3. **`mcr-tech-stack-selector`**: Analyzes technical and budget requirements with an objective trade-off matrix to pick optimal frameworks, databases, and hosts.
4. **`mcr-project-planning`**: Breaks projects into Work Breakdown Structures (WBS), estimates engineering hours, maps critical path dependencies, and calculates velocity.
5. **`mcr-market-research`**: TAM/SAM/SOM market sizing, competitive feature parity grids, customer friction point synthesis.
6. **`mcr-tech-architecture`**: System boundary definition, Domain-Driven Design (DDD) aggregates, C4 architectural diagrams, and Architecture Decision Records (ADRs).

### Domain 2: Frontend Engineering, UI & Design Systems
7. **`mcr-frontend-ui`**: WCAG 2.1 AA compliant components, accessible data tables with keyboard navigation, virtualized lists, and comprehensive error boundaries.
8. **`mcr-responsive-styling`**: Modern Tailwind CSS 4 utility design, responsive mobile-first grid systems, fluid typography, dark mode theming.
9. **`mcr-motion-animation`**: 60fps GPU-accelerated micro-interactions, Framer Motion staggered transitions, scroll-driven layout effects.
10. **`mcr-brand-logo-design`**: Automated generation of geometric SVG brand logos, modern app icons, favicon bundles, and brand color palette tokens.
11. **`mcr-ux-interaction-design`**: Optimistic UI updates, multi-step checkout/registration flows, toast alert orchestration, and keyboard shortcut managers.

### Domain 3: Backend Engineering & Microservices
12. **`mcr-backend-api`**: High-throughput REST & GraphQL APIs, strict Zod/Pydantic validation, unified error envelopes, rate limiting, and cursor-based pagination.
13. **`mcr-backend-clean-architecture`**: Clean Architecture & Hexagonal Ports/Adapters separation (Entities, Use Cases, Controllers, Repositories).
14. **`mcr-background-jobs-queues`**: Distributed job queues (BullMQ / Redis, Celery), exponential backoff retries, concurrency limits, and Dead-Letter Queues (DLQ).
15. **`mcr-email-otp-notifications`**: Transactional email deliverability (Resend, SendGrid), 6-digit cryptographic OTP generation, rate limits, and timing-safe token validation.
16. **`mcr-multitenant-saas`**: Multi-tenant B2B architectures, team workspace switching, tenant database isolation via PostgreSQL Row-Level Security (RLS).
17. **`mcr-payments-billing`**: End-to-end Stripe billing lifecycles, webhook signature verification with replay protection, subscription downgrades, dunning, and invoice receipts.
18. **`mcr-file-storage-cdn`**: Direct-to-S3 / Cloudflare R2 presigned upload URLs, client MIME validation, virus scanning webhooks, and Cloudflare CDN caching.

### Domain 4: Database Engineering & Data Integrity
19. **`mcr-database-architect`**: Fully normalized 3NF schemas, foreign key cascade policies, composite B-Tree indexes, partial indexing, and query cost analysis (`EXPLAIN ANALYZE`).
20. **`mcr-db-migration`**: Zero-downtime database migrations using the Expand and Contract pattern, backward-compatible column rollouts, and deterministic rollback scripts.

### Domain 5: Defensive Security & Auth
21. **`mcr-auth-security`**: OAuth 2.0 & OIDC integrations, secure HTTP-only cookie JWTs, CSRF protection, and fine-grained RBAC/ABAC authorization guards.
22. **`mcr-security-audit`**: Automated secret scanning (`scan_secrets.sh`), OWASP Top 10 mitigation checklists, and secure HTTP response header enforcement (`secure-headers.ts`).
23. **`mcr-secrets-guard`**: Environment variable hygiene, prevention of leaked `.env` credentials, and automated `.env.example` template generation.

### Domain 6: QA, Verification & Reliability
24. **`mcr-test-automation`**: Automated unit tests (Vitest/Jest/PyTest), integration tests with ephemeral test databases, and Playwright end-to-end tests.
25. **`mcr-debugger-fixer`**: Surgical bug isolation from stack traces, root-cause reproduction scripts, regression tests, and minimal-diff patches.
26. **`mcr-quality-gatekeeper`**: Pre-commit verification enforcing zero dummy placeholders, lint cleanliness, and automated learning capture into `docs/LESSONS_LEARNED.md`.
27. **`mcr-release-readiness`**: Production deployment checklist validating build assets, migration dry-runs, health check routes, and zero security alerts.

### Domain 7: DevOps, Observability & Cloud Deployment
28. **`mcr-cloud-hosting-domains`**: Domain registrar negotiation, wholesale pricing strategies, Cloudflare DNS/SSL proxies, and hosting recommendations (Vercel, Railway, Cloudflare, AWS).
29. **`mcr-devops-cloud`**: Production multi-stage Docker containerization, GitHub Actions CI/CD workflows, automated PR preview environments.
30. **`mcr-observability-sentry-logging`**: Structured JSON logging with trace/correlation IDs (`structured-logger.ts`), Sentry crash monitoring, and OpenTelemetry instrumentation.
31. **`mcr-git-workflow-github`**: Conventional Commits standard (`feat:`, `fix:`, `refactor:`), automatic PR generation via GitHub CLI, and branch merge safety.

### Domain 8: Advanced AI, RAG & Future Tech
32. **`mcr-rag-architect`**: Production Retrieval-Augmented Generation (RAG) pipelines, semantic vector chunking, hybrid keyword+dense search, and citation grounding.
33. **`mcr-subagent-orchestrator`**: Master agent coordination protocol for delegating independent workstreams to specialized subagents and integrating verified outputs.
34. **`mcr-web3-blockchain`**: Solidity smart contract design, reentrancy guards, OpenZeppelin contract standards, Foundry unit test suites, and gas optimization.
35. **`mcr-crossplatform-mobile-desktop`**: Universal apps using React Native/Expo, Flutter, Tauri, and Electron with offline-first local SQLite sync.
36. **`mcr-i18n-localization`**: Multi-language localization catalogs (English, Bengali, Spanish, RTL support), pluralization rules, and localized date/currency formats.
37. **`mcr-seo-meta-social`**: Dynamic Open Graph preview cards, Schema.org JSON-LD microdata, sitemap XML generators, and search engine crawler optimizations.
38. **`mcr-tech-docs`**: OpenAPI / Swagger generation, Markdown architecture guides, developer onboarding runbooks, and automated API changelogs.

*(Skills 39–43 provide backward-compatible aliases: `market-research`, `project-discovery`, `release-readiness`, `security-audit`, and legacy wrappers.)*

---

## 4. The 15 Core Rules

All agent actions are governed by the 15 immutable rules in `.agents/rules/`:
- `00-core-operating-contract.md` *(always_on)*: Invariants, evidence standard, and **0xmcr** creator attribution.
- `02-professional-focus-and-anti-flirt.md` *(always_on)*: Absolute engineering rigor, anti-distraction deflection.
- `05-godmode-execution-protocol.md` *(always_on)*: Zero placeholders, production enterprise completeness.
- `10-research-and-market-intel.md` *(model_decision)*: Evidence-based research criteria.
- `15-clean-code-and-documentation.md` *(always_on)*: Mandatory JSDoc/TSDoc/Docstrings & inline "why" comments.
- `20-product-and-architecture.md` *(model_decision)*: PRD and C4 architectural standards.
- `30-frontend-engineering.md` *(glob)*: WCAG accessibility and responsive patterns.
- `40-backend-engineering.md` *(model_decision)*: REST/GraphQL contracts and rate limits.
- `50-database-and-storage.md` *(model_decision)*: RLS and index optimization rules.
- `60-defensive-security.md` *(model_decision)*: OWASP Top 10 defense.
- `70-qa-and-verification.md` *(model_decision)*: Mandatory test passes before marking complete.
- `80-ai-and-automation.md` *(model_decision)*: RAG hallucination guardrails.
- `85-quality-and-anti-hallucination.md` *(always_on)*: Real packages only, lessons learned loop.
- `90-devops-and-release.md` *(manual)*: CI/CD deployment checks.
- `95-web3-blockchain-safety.md` *(glob)*: Smart contract exploit prevention.

---

## 5. Community Feedback & Reporting Workflow

External developers, teams, and contributors can easily collaborate, submit feedback, report bugs, or propose new skills to MCROS:

### How External Developers Report Issues
1. **GitHub Issues**:
   - Bug reports: [https://github.com/0xmcr/MCROS/issues/new?template=bug_report.md](https://github.com/0xmcr/MCROS/issues/new?template=bug_report.md)
   - Feature & Skill proposals: [https://github.com/0xmcr/MCROS/issues/new?template=feature_request.md](https://github.com/0xmcr/MCROS/issues/new?template=feature_request.md)
2. **Pull Requests**:
   - Follow the standard Conventional Commits convention (`feat:`, `fix:`, `docs:`, `skill:`).
   - All PRs must pass `python3 scripts/validate_setup.py` and `node bin/mcros.js validate`.
3. **Automated Feedback Command**:
   - Developers using MCROS in their terminal can run:
     ```bash
     npx mcros feedback
     ```
     This opens the issue submission page directly in the default browser.

---

## 6. How to Deploy / Push MCROS to GitHub

To publish or sync MCROS to your GitHub account (`0xmcr`):

```bash
# 1. Verify all files and validation tests pass
python3 scripts/validate_setup.py
node bin/mcros.js validate

# 2. Check remote repository configuration
git remote -v
# Output should point to:
# origin  https://github.com/0xmcr/MCROS.git (fetch)
# origin  https://github.com/0xmcr/MCROS.git (push)

# 3. Stage, commit and push
git add .
git commit -m "feat: release MCROS V3 by 0xmcr with 43 skills and cross-platform matrix"
git branch -M main
git push -u origin main
```

---

## 7. Licensing & Attribution

- **Copyright**: &copy; 2026 Maheshwar Chandra Roy (`0xmcr`).
- **License**: MIT License. Free for open-source and commercial use with attribution.
- **Official Repository**: [https://github.com/0xmcr/MCROS](https://github.com/0xmcr/MCROS)
