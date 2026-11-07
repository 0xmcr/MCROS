# MCR Technical SEO, Open Graph & Structured Data Standards

---

## 1. The Open Graph Standard (Facebook, LinkedIn, Discord)
Every public web page must provide these 4 tags:
- `og:title`: Catchy headline (under 60 characters).
- `og:description`: Engaging summary (between 50-160 characters).
- `og:image`: High-resolution 1200x630px image (1.91:1 ratio).
- `og:url`: Explicit canonical URL (prevents duplicate link tracking penalties).

---

## 2. Dynamic Sitemap & Robots.txt Protocol
- `sitemap.xml`: Must list all public canonical URLs with `<lastmod>` timestamps and `<changefreq>`.
- `robots.txt`:
  ```txt
  User-agent: *
  Allow: /
  Disallow: /api/
  Disallow: /admin/
  Disallow: /dashboard/
  
  Sitemap: https://mcros.dev/sitemap.xml
  ```
