# MCR Multi-Tenant SaaS Architecture & Isolation Patterns

---

## 1. Isolation Models Comparison

| Model | Architecture | Pros | Cons | Best Used For |
|---|---|---|---|---|
| **Pooled (Shared DB, Shared Schema)** | All tenants share tables with `tenant_id` + RLS | Lowest cost, easiest to query across all tenants, zero database proliferation | Requires disciplined RLS to prevent leaks | 95% of B2B SaaS applications |
| **Schema-per-Tenant** | Each tenant has a dedicated PostgreSQL schema | Logical data boundary, easier backup per tenant | Database migration complexity increases with tenant count | Regulated mid-market enterprise |
| **Database-per-Tenant** | Physical separate database per tenant | Highest compliance, independent scaling | High idle cost, connection pool overhead | Tier-1 Banks, Healthcare (HIPAA) |

---

## 2. Team Invitation & RBAC Matrix
Standard B2B SaaS Roles:
- **Owner**: Full access, billing management, workspace deletion, transfers ownership.
- **Admin**: Invites/removes members, updates settings, cannot delete workspace or touch billing.
- **Member**: Reads and writes standard business documents and data.
- **Guest / Viewer**: Read-only permissions on explicitly shared projects.
