---
name: mcr-cloud-hosting-domains
description: Guide domain acquisition at wholesale pricing, DNS and SSL configuration (Cloudflare), and select optimal cloud hosting platforms (Vercel, Railway, Cloudflare, AWS).
---

# MCR Cloud Hosting, Domains & DNS Skill

Use this skill when advising on domain registration, configuring DNS/SSL, selecting hosting providers, or deploying applications to cost-efficient cloud networks.

## 1. Domain Registration Strategy (Wholesale & No-Markup)
- **Top Recommendation: Cloudflare Registrar**
  - Charges exact at-cost wholesale registry pricing (e.g. `\$9.77/year` for `.com`, zero markup, zero renewal price hike).
  - Includes free WHOIS privacy protection, free DNSSEC, and direct CDN integration.
- **Alternative: Porkbun / Namecheap**
  - Excellent for niche TLDs (`.dev`, `.ai`, `.io`), free WHOIS privacy, easy interface.
  - Avoid registrars with deceptive renewal price hikes or expensive add-on fees.

## 2. DNS & SSL Configuration (Cloudflare Edge)
- **Nameservers**: Point domain nameservers to Cloudflare (`ns1.cloudflare.com`, `ns2.cloudflare.com`).
- **Essential DNS Records**:
  - `A` / `CNAME` records pointing root (`@`) and `www` to hosting provider.
  - `TXT` records for domain verification (Google, GitHub, Resend/SendGrid SPF/DKIM).
- **SSL / TLS**: Set encryption mode to **Full (Strict)** to ensure end-to-end encryption between visitor, Cloudflare Edge, and origin server.

## 3. Cloud Hosting Decision Matrix

| Project Component | Best Provider | Why Chosen | Cost / Free Tier |
|---|---|---|---|
| **Frontend / Web (Next.js / React)** | **Vercel** or **Cloudflare Pages** | Automated Git branch previews, edge CDN, zero-config SSR. | Generous free hobby tiers. |
| **Backend API (Node / Python / Go)** | **Railway** or **Render** or **Fly.io** | Native Docker support, auto-restarts, managed environment variables. | \$5/month usage credit or free tier. |
| **Relational Database (PostgreSQL)** | **Neon** or **Supabase** | Serverless branching, pooling, auto-suspend when idle, backups. | Free 500MB / 0.5GB tier. |
| **Object / Media Storage (S3)** | **Cloudflare R2** | 100% S3-compatible, **\$0 egress bandwidth fees** (huge cost saver). | 10GB free storage. |
| **Enterprise / Multi-Region** | **AWS (ECS / RDS)** or **GCP** | Maximum compliance, dedicated VPC, granular IAM. | Pay-per-use with free credits. |

## 4. Step-by-Step Deployment Runbook
1. Register domain on Cloudflare Registrar or Porkbun.
2. Link repository to Vercel/Railway for continuous Git deployment.
3. Add production environment variables in dashboard.
4. Verify custom domain SSL certificate and test live URL.
