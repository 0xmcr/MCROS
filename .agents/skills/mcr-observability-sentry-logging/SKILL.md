---
name: mcr-observability-sentry-logging
description: Implement enterprise observability, structured JSON logging with correlation IDs, Sentry crash reporting, and OpenTelemetry distributed tracing.
---

# MCR Observability, Sentry & Structured Logging Skill

Use this skill when setting up production monitoring, structured logging pipelines, application error boundaries, or tracing requests across distributed services.

## Supporting Resources & Submodules
- Structured JSON Logger Reference: [structured-logger.ts](./examples/structured-logger.ts)
- Tracing & Monitoring Standards: [observability-manual.md](./references/observability-manual.md)

---

## 1. Observability Protocol

### Step 1: Structured JSON Logging
- Replace raw `console.log` with structured JSON logging using [structured-logger.ts](./examples/structured-logger.ts).
- Attach correlation `requestId` to every log line to trace user journeys across distributed services.

### Step 2: Sentry Error Monitoring & Alerting
- Initialize Sentry SDK on frontend and backend.
- Filter out noise (e.g. 404 Not Found, expected client validation errors).
- Route critical unhandled 500 crashes directly to Discord/Slack incident channels.

### Step 3: Health Probes & Metrics
- Expose `/healthz` and `/readyz` endpoints.
- Monitor p95 latency and error rates to trigger automated container restarts when anomalies occur.
