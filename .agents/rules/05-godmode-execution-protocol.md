---
trigger: always_on
---

# MCROS Godmode Autonomous Execution Protocol

## 1. Absolute Directives
When invoked or when operating under `/GODMODE`, the agent operates with zero compromises:
- **Exhaustive Implementations**: Never leave partial logic, dummy buttons, or `// TODO: add logic here` stubs. Every feature, service, and interface must be fully wired and functional.
- **Enterprise Scale by Default**: Design every data model, API, and frontend component to handle multi-user concurrency, multi-tenancy, rate limits, and network failure states.
- **Proactive Engineering**: Do not wait for the user to prompt for obvious production requirements (e.g. email verification, payment webhooks, SEO meta tags, error boundaries, rate limiting). Anticipate and implement them proactively.
- **Verification Evidence**: Execute real commands in terminal to prove builds, tests, and configurations work.

## 2. Multi-Tier Production Standards
- **Payment & Financials**: Mandatory idempotency keys, database transaction boundaries, verified webhook cryptographic signatures, and audit logs.
- **Auth & OTP**: Redis TTL for ephemeral codes, rate limiting (max 3 attempts per 15 minutes), timing-safe comparisons to prevent timing attacks.
- **Tenancy**: Every database query on customer data must be scoped by `tenant_id` or protected by database-level Row-Level Security (RLS).
- **SEO & Web**: Dynamic OpenGraph images, Schema.org JSON-LD structured data, responsive headers/footers, and clean semantic layouts.
