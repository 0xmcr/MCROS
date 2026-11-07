---
name: mcr-repo-scaffold
description: Scaffold enterprise-grade, clean directory architectures for full-stack, frontend, backend, or monorepo projects with standard configurations and linting.
---

# MCR Repository Scaffolding Skill

Use this skill when initializing a new codebase after the technology stack and architecture have been selected. It sets up standard clean architecture structures, configuration files, and linting rules.

## Recommended Directory Layouts

### 1. Full-Stack Modern Web (Next.js / TypeScript)
```
├── app/               # Routes, pages, API route handlers
├── components/        # UI components (ui/, forms/, layouts/)
├── lib/               # Utility functions, client instances (db, auth)
├── hooks/             # Custom React hooks
├── types/             # Shared TypeScript interfaces & types
├── styles/            # Global styles, Tailwind config
├── tests/             # Vitest / Playwright test suites
├── public/            # Static assets
└── .env.example       # Sanitized environment variable template
```

### 2. Modular Backend (Node/TS or Python FastAPI)
```
├── src/ (or app/)
│   ├── api/           # Route controllers & endpoints
│   ├── core/          # Config, security, database engine
│   ├── models/        # ORM / database entity models
│   ├── schemas/       # Request / response schemas (Zod or Pydantic)
│   ├── services/      # Business logic & external API wrappers
│   └── middlewares/   # Auth, logging, rate limiting, error handling
├── tests/             # Unit and integration test suites
└── docker/            # Dockerfile and docker-compose.yml
```

## Scaffolding Procedure
1. Create directories without overwriting existing files.
2. Generate base configuration files (`tsconfig.json`, `package.json` or `pyproject.toml`, `.eslintrc`, `.prettierrc`).
3. Create `.env.example` documenting all required configuration keys with dummy values.
4. Verify build and type-checking commands run cleanly on the empty scaffold.
