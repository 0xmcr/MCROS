# MCR Object Storage & CDN Security Manual

---

## 1. Zero Direct Server Proxying (Presigned URLs)
Never allow clients to upload 50MB files directly through your web application servers:
- Client requests a presigned PUT URL from backend API.
- Backend validates permissions and returns presigned URL with 15-minute expiration.
- Client uploads raw bytes directly to Cloudflare R2 / AWS S3 via `PUT`.
- Web server CPU and memory usage remain flat!

---

## 2. Preventing Malicious File Uploads (RCE Defense)
- Never preserve the user's original filename directly on the filesystem (prevents path traversal `../../../etc/cron.d/malware`).
- Generate synthetic UUID keys (`${uuid}.${ext}`).
- Strip executable headers from uploaded files.
- Serve uploaded files from a separate sandboxed CDN domain (`cdn.mcros.dev`) with `Content-Disposition: attachment` for untrusted formats.
