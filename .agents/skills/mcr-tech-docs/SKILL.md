---
name: mcr-tech-docs
description: Author technical documentation, OpenAPI/Swagger specifications, developer onboarding guides, architecture overviews, and changelogs.
---

# MCR Technical Documentation Skill

Use this skill when authoring API documentation, creating README guides, documenting architectural components, writing user manuals, or drafting release notes.

## Technical Writing Standards

### 1. Developer Documentation (README & Onboarding)
Every project repository must include a comprehensive `README.md` with:
- Project Overview & Value Proposition.
- Architecture Summary & High-Level Diagram.
- Prerequisites (Node/Python version, Docker, database).
- Quickstart Setup Instructions (step-by-step commands to run locally).
- Environment Variables table explaining required keys and purpose.
- Available Scripts & Test Commands.

### 2. API Documentation (OpenAPI / Swagger)
- Generate machine-readable OpenAPI 3.1 specifications.
- Document all endpoints, HTTP methods, path/query parameters, request payloads, and status codes (200, 201, 400, 401, 403, 404, 500).
- Provide realistic JSON request and response examples for every route.

### 3. Changelog & Release Notes
- Maintain `CHANGELOG.md` adhering to Keep a Changelog standards.
- Categorize updates: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
- Follow Semantic Versioning (MAJOR.MINOR.PATCH).
