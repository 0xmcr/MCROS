---
name: mcr-auth-security
description: Implement secure authentication (OAuth 2.0, OIDC, JWT, sessions) and fine-grained authorization (RBAC, ABAC, route guards) with best-practice cryptography.
---

# MCR Authentication & Authorization Skill

Use this skill when designing or implementing user login, social authentication, token management, session persistence, or permission-checking middleware.

## Security & Auth Guidelines

### 1. Authentication Strategies
- JWT + Refresh Tokens: Short-lived access tokens (15 minutes) + rotating refresh tokens stored in `HttpOnly`, `Secure`, `SameSite=Strict` cookies.
- Server-Side Sessions: Redis-backed or database-backed session store with cryptographic session identifiers.
- Social OAuth 2.0 / OIDC: Google, GitHub, Apple login using PKCE (Proof Key for Code Exchange) flow.

### 2. Password Security & Cryptography
- Never store plaintext passwords or weak hashes (MD5, SHA1, plain SHA256).
- Use Argon2id (recommended) or bcrypt with work factor ≥ 12.
- Enforce brute-force protection, account lockouts after consecutive failed attempts, and CAPTCHA / rate limits on `/login` and `/register`.

### 3. Fine-Grained Authorization
- Role-Based Access Control (RBAC): Enforce permissions at both the route handler and service layer (e.g. `requirePermission('articles:delete')`).
- Attribute-Based Access Control (ABAC): Validate resource ownership (e.g. `user.id === resource.ownerId` or `user.role === 'ADMIN'`).
- Multi-Tenant Isolation: Ensure all database queries include tenant identifiers (`WHERE tenant_id = :tenantId`) to prevent cross-tenant data leaks.
