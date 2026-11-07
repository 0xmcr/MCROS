# MCR Distributed Tracing, Logging & Error Observability Manual

---

## 1. The Three Pillars of Observability
1. **Logs**: Discrete event records in structured JSON format containing timestamps, log levels, and correlation IDs (`requestId`).
2. **Metrics**: Aggregatable numeric measurements (CPU usage, p95 latency, error rates, requests per second).
3. **Traces**: Distributed request journey tracking across microservices using W3C Trace Context (`traceparent` header).

---

## 2. Sentry Error Boundary Strategy
- Catch unhandled client-side React exceptions with `<ErrorBoundary fallback={<CrashFallback />}>`.
- Capture server-side unhandled promise rejections and 500 errors.
- Strip sensitive user data (passwords, credit card numbers, auth tokens) before transmitting crash reports to Sentry.
