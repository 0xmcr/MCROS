---
name: mcr-file-storage-cdn
description: Implement secure cloud object storage (Cloudflare R2, AWS S3), presigned upload URLs, client direct streaming, and CDN asset optimization.
---

# MCR File Storage & CDN Architecture Skill

Use this skill when implementing avatar uploads, user document attachments, video/media storage, or image transformation pipelines.

## Supporting Resources & Submodules
- Presigned URL Generator Reference: [s3-presigned-upload.ts](./examples/s3-presigned-upload.ts)
- Storage Security & Anti-RCE Manual: [storage-security-runbook.md](./references/storage-security-runbook.md)

---

## 1. Cloud Storage Protocol

### Step 1: Secure Presigned Upload Flow
- When a user uploads a file, generate a secure presigned upload URL using [s3-presigned-upload.ts](./examples/s3-presigned-upload.ts).
- Validate file size limits (<10MB) and MIME types before generating the signature.
- Client uploads bytes directly to Cloudflare R2 or AWS S3.

### Step 2: Storage Key Isolation
- Isolate files by user and tenant (`uploads/{tenantId}/{userId}/{randomKey}.ext`).
- Sanitize filenames to prevent path traversal vulnerabilities according to [storage-security-runbook.md](./references/storage-security-runbook.md).

### Step 3: Fast CDN Distribution
- Deliver public assets through global edge CDN with aggressive browser caching headers (`Cache-Control: public, max-age=31536000, immutable`).
