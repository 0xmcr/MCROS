# MCR Background Queues & Worker Resilience Manual

---

## 1. At-Least-Once Delivery & Idempotent Workers
Background workers can crash after completing a task but before acknowledging it to the queue. Therefore:
- All background job handlers must be idempotent.
- Check database state before performing side-effects (e.g. check if invoice already generated before creating duplicate PDF).

---

## 2. Exponential Backoff & Dead-Letter Queues (DLQ)
- Retry strategy:
  - Attempt 1: Immediate retry.
  - Attempt 2: 2 seconds backoff.
  - Attempt 3: 4 seconds backoff.
  - Attempt 4: 8 seconds backoff.
  - Attempt 5: 16 seconds backoff.
- After 5 failed attempts: Move job to the **Dead-Letter Queue (DLQ)** and trigger a high-severity alert in Sentry/Slack.
