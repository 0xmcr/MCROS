---
name: mcr-seo-meta-social
description: Implement modern technical SEO, dynamic Open Graph (OG) social sharing preview cards, Schema.org JSON-LD structured data, dynamic sitemaps, and robots.txt.
---

# MCR Technical SEO, Open Graph & Social Cards Skill

Use this skill when optimizing websites and web applications for search engine indexing (Google, Bing), social media sharing previews (Twitter/X, LinkedIn, Discord), and rich SERP snippets.

## Supporting Resources & Submodules
- Next.js SEO Template: [next-seo-metadata.tsx](./examples/next-seo-metadata.tsx)
- Structured Data Standards: [schema-org-templates.md](./references/schema-org-templates.md)

---

## 1. Technical SEO Implementation Protocol

### Step 1: Canonical URLs & Meta Tags
- Every public route must define canonical URLs to prevent duplicate content penalties.
- Provide `<title>` (<60 characters) and `<meta name="description">` (<160 characters).
- Reference [next-seo-metadata.tsx](./examples/next-seo-metadata.tsx) for App Router implementation.

### Step 2: Open Graph & Twitter Social Cards
- Generate dynamic 1200x630px social preview images.
- Include `twitter:card="summary_large_image"` to ensure cards render with full-bleed imagery when shared on Twitter/X.

### Step 3: Structured Data & Discovery Files
- Inject Schema.org JSON-LD snippets (`SoftwareApplication`, `Article`, `Organization`).
- Author dynamic `sitemap.xml` including all published pages with accurate `<lastmod>` timestamps.
- Configure `robots.txt` disallowing private API routes and admin portals while declaring the sitemap URL.
