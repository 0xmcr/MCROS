# MCR OWASP Top 10 Defensive Cybersecurity Runbook

---

## 1. Injection (SQLi, Command, NoSQL)
- **Vulnerability**: Untrusted user input concatenated directly into database queries or shell execution strings.
- **Defensive Requirement**:
  - Always use parameterized queries (`$1, $2` in Postgres, ORM query builders, or prepared statements).
  - Never invoke `eval()`, `exec()`, or raw shell commands with string interpolation.
  - Reject inputs containing null bytes (`\0`) or path traversal markers (`../`).

---

## 2. Broken Authentication & Session Management
- **Vulnerability**: Predictable session tokens, missing token rotation, long-lived access tokens, or plaintext password storage.
- **Defensive Requirement**:
  - Passwords hashed with Argon2id or bcrypt (work factor >= 12).
  - Short-lived JWT access tokens (<= 15 minutes) with rotating refresh tokens.
  - Store tokens in `HttpOnly`, `Secure`, `SameSite=Lax/Strict` cookies. Never store sensitive tokens in `localStorage` (vulnerable to XSS extraction)!

---

## 3. Broken Object Level Authorization (BOLA / IDOR)
- **Vulnerability**: Changing `GET /api/orders/101` to `GET /api/orders/102` allows user A to view user B's private invoice.
- **Defensive Requirement**:
  - Every single query retrieving a private resource must validate tenant and user ownership:
    ```sql
    SELECT * FROM orders WHERE id = :order_id AND user_id = :authenticated_user_id;
    ```
  - Use non-sequential UUIDs (e.g. `uuid_generate_v4()`) rather than auto-incrementing integers (`1, 2, 3`) to prevent enumeration.

---

## 4. Security Misconfiguration & Exposed Secrets
- **Vulnerability**: Default administrative passwords, debug endpoints left open (`/debug/pprof`), stack traces exposed to clients.
- **Defensive Requirement**:
  - Zero hardcoded credentials in source code.
  - Run `scripts/scan_secrets.sh` prior to every release.
  - Maintain sanitized `.env.example` templates with dummy values.
