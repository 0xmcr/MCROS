---
name: mcr-background-jobs-queues
description: Architect asynchronous background job queues (BullMQ, Celery, SQS), worker processes, exponential backoff retries, and Dead-Letter Queues (DLQ).
---

# MCR Background Job Queues & Worker Architecture Skill

Use this skill when offloading long-running tasks (email delivery, video encoding, PDF reports, webhook retries) from HTTP request threads to asynchronous background workers.

## Supporting Resources & Submodules
- Reference Worker Implementation: [bullmq-worker.ts](./examples/bullmq-worker.ts)
- Queue Resilience Manual: [queue-resilience-guide.md](./references/queue-resilience-guide.md)

---

## 1. Background Processing Workflow

### Step 1: Offloading from API Threads
- HTTP requests that exceed 200ms must be enqueued as background jobs.
- Return `202 Accepted` immediately with a `jobId` so clients can poll or await WebSocket completion events.

### Step 2: Worker Concurrency & Idempotency
- Configure BullMQ or Celery workers with concurrency limits matching CPU cores.
- Implement idempotency checks according to [queue-resilience-guide.md](./references/queue-resilience-guide.md).

### Step 3: Failure Handling & DLQ Isolation
- Configure 5 retries with exponential backoff.
- Move unrecoverable jobs to Dead-Letter Queues and alert engineering teams without crashing the worker process.
