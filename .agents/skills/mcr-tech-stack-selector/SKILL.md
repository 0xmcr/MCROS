---
name: mcr-tech-stack-selector
description: Evaluate project requirements, compare frameworks, databases, libraries and cloud tools, and select the optimal technology stack with an objective trade-off matrix.
---

# MCR Tech Stack & Tool Selection Skill

Use this skill when planning a new software application or modernizing an existing system. It guides the rational selection of languages, frameworks, databases, authentication, and tooling based on concrete requirements rather than trends.

## Decision Matrix Framework

### 1. Requirements & Constraints Analysis
- Target Platform: Web (SPA / SSR / Static), Mobile (React Native / Flutter / Native), Desktop (Electron / Tauri), Backend API, or CLI.
- Scale & Concurrency: Real-time traffic, batch processing, event-driven, or read-heavy.
- Team & Ecosystem: Language ergonomics, library maturity, community support, hiring availability.
- Latency & Resource Budget: Serverless vs. long-running containers, cold starts, memory footprint.

### 2. Technology Evaluation Tiers
- Frontend Runtime: Next.js (SSR/App Router), Vite + React/Vue (SPA), SvelteKit, Astro (Content-heavy).
- Backend Framework: FastAPI / Django (Python), Express / NestJS / Hono (Node/TS), Go (Gin/Fiber), Rust (Axum).
- Database & ORM:
  - Relational: PostgreSQL + Prisma / Drizzle / SQLAlchemy.
  - Document/Cache: MongoDB, Redis, Dragonfly.
  - Vector/AI: pgvector, Pinecone, Qdrant, Chroma.
- Styling & UI: Tailwind CSS, Shadcn UI, Radix primitives, Framer Motion.
- Auth & Identity: Auth0, Supabase Auth, Clerk, NextAuth/Auth.js, Lucia, Firebase Auth.
- Testing Suite: Vitest / Jest, Playwright / Cypress, Pytest, Supertest.
- DevOps & Cloud: Docker, GitHub Actions, AWS / GCP, Vercel / Railway / Fly.io.

### 3. Output Deliverable
Generate an Architecture Decision Record (ADR) in `docs/templates/ADR.md` format documenting:
1. Chosen Stack & Rationale.
2. Considered Alternatives & Why Rejected.
3. Known Trade-offs & Mitigations.
