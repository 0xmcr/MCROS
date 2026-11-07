---
name: mcr-tech-architecture
description: Design scalable system architectures, map component boundaries, define data contracts, draw topology diagrams, and write Architecture Decision Records (ADRs).
---

# MCR Technical Architecture Skill

Use this skill when designing the architecture of a system, evaluating microservices vs. modular monolith, establishing data flow boundaries, or making pivotal technical decisions.

## Architecture Design Protocol

### 1. System Topology & Context
- Map external actors (browsers, mobile apps, third-party webhook senders).
- Define perimeter gateways (reverse proxy, load balancer, CDN, API Gateway).
- Establish backend service boundaries and inter-service communication protocols (REST, gRPC, Redis Pub/Sub, Kafka).

### 2. Trust Boundaries & Data Flow
- Clearly identify where untrusted public traffic enters the system.
- Enforce strict perimeter validation before data reaches internal services or databases.
- Designate encrypted communication channels (TLS 1.3 internal and external).

### 3. Component Architecture
- Single Responsibility: Each module or service must own a single bounded domain context.
- High Cohesion & Loose Coupling: Services communicate via explicit, strongly typed contracts.
- Resilience: Circuit breakers, retries with exponential backoff, dead-letter queues.

### 4. Output Deliverables
- Populate `docs/ARCHITECTURE.md`.
- Document major technical choices using `docs/templates/ADR.md`.
- Include Mermaid diagrams illustrating component interactions and data pipelines.
