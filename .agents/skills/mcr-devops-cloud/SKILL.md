---
name: mcr-devops-cloud
description: Configure Docker containerization, automated GitHub Actions CI/CD workflows, cloud infrastructure, and health check monitoring.
---

# MCR DevOps & Cloud Engineering Skill

Use this skill when configuring deployment pipelines, authoring Dockerfiles, setting up CI/CD test automation, managing cloud resources, or containerizing applications.

## DevOps Best Practices

### 1. Docker & Containerization
- Multi-Stage Builds: Use multi-stage Dockerfiles to keep production images minimal and free of development dependencies or build tools.
- Non-Root User: Run container processes as an unprivileged non-root user (`USER node` or `USER appuser`).
- Caching: Order `COPY` statements strategically (e.g. `COPY package*.json .` before `COPY . .`) to maximize Docker layer caching.

### 2. CI/CD Pipeline (GitHub Actions)
Configure automated workflows triggering on pull requests and main branch commits:
- Step 1: Install dependencies with frozen lockfile (`npm ci`, `poetry install --no-root`).
- Step 2: Code quality checks (linting, type-checking, formatting).
- Step 3: Automated test execution (unit and integration tests).
- Step 4: Security scan (dependency audit and secrets check).
- Step 5: Build container image and run smoke tests.

### 3. Production Monitoring & Health Checks
- Implement `/healthz` (liveness probe) verifying the web server process is responding.
- Implement `/readyz` (readiness probe) verifying database connections and external dependency readiness.
- Structured Logging: Emit JSON logs with timestamps, log levels (`INFO`, `WARN`, `ERROR`), and correlation request IDs.
