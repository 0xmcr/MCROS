# MCR Payment Security, Webhook Reliability & Billing Runbook

---

## 1. PCI-DSS Compliance & Cardholder Data
- Never transmit, log, or store raw credit card numbers, CVVs, or expiration dates on your application servers.
- Use client-side tokenization (Stripe Elements, Lemon Squeezy hosted checkout, PayPal SDK).
- Pass raw cards directly to the payment gateway's secure iframe/token endpoint.

---

## 2. Webhook Verification & Anti-Replay Attacks
- Always verify incoming webhooks using raw body bytes (never parsed JSON) and gateway HMAC secret.
- Reject requests where timestamp tolerance exceeds 5 minutes (`300 seconds`) to defeat replay attacks.
- Return `200 OK` promptly (<3 seconds) after recording the event; process long-running business side-effects asynchronously in a background queue.

---

## 3. Idempotent Payment Processing
- Store processed `event.id` in a database `processed_webhook_events` table with a unique index.
- If an event arrives that has already been recorded, acknowledge with `200 OK` and skip processing.
