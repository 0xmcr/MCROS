---
name: mcr-multitenant-saas
description: Design multi-tenant B2B SaaS architectures, tenant workspace switching, team member invitations, Row-Level Security (RLS) data isolation, and RBAC permissions.
---

# MCR Multi-Tenant SaaS & Workspace Architecture Skill

Use this skill when developing multi-tenant software, managing organization memberships, configuring database Row-Level Security (RLS), or implementing team role permissions.

## Supporting Resources & Submodules
- PostgreSQL RLS Policies Reference: [rls-tenant-policies.sql](./examples/rls-tenant-policies.sql)
- SaaS Isolation Architecture: [multitenant-patterns.md](./references/multitenant-patterns.md)

---

## 1. Multi-Tenant Engineering Workflow

### Step 1: Tenant Context Middleware
- Extract active tenant from subdomain (`tenant.app.com`), path (`/org/:orgSlug`), or session token.
- Validate that the authenticated user is an active member of the requested tenant.
- Set PostgreSQL session variable `app.current_tenant_id` at the start of database connection checkout.

### Step 2: Enforce Database Row-Level Security (RLS)
- Implement database policies according to [rls-tenant-policies.sql](./examples/rls-tenant-policies.sql).
- Ensure queries without explicit `WHERE tenant_id = ...` still cannot access rows from rival organizations.

### Step 3: Team Invitations & RBAC
- Manage user roles (Owner, Admin, Member, Viewer) adhering to [multitenant-patterns.md](./references/multitenant-patterns.md).
- Implement cryptographically signed invitation tokens with 7-day expiration for new employee onboarding.
