---
name: mcr-backend-clean-architecture
description: Implement enterprise Clean Architecture, Domain-Driven Design (DDD), Controller-Service-Repository patterns, and modular backend structuring.
---

# MCR Backend Clean Architecture Skill

Use this skill when architecting scalable, enterprise-grade backend services. It decouples business logic from external frameworks, databases, and third-party APIs.

## Architectural Layers

```
        ┌────────────────────────────────────────────────────────┐
        │            Presentation / HTTP Layer                  │
        │      (Controllers, Routes, Middlewares, DTOs)          │
        └───────────────────────────┬────────────────────────────┘
                                    │ Calls
                                    ▼
        ┌────────────────────────────────────────────────────────┐
        │                 Application / Service Layer            │
        │             (Use Cases, Business Orchestration)        │
        └───────────────────────────┬────────────────────────────┘
                                    │ Implements
                                    ▼
        ┌────────────────────────────────────────────────────────┐
        │                   Domain Layer                         │
        │        (Pure Business Entities, Value Objects)         │
        └───────────────────────────┬────────────────────────────┘
                                    │ Inverted Dependency
                                    ▼
        ┌────────────────────────────────────────────────────────┐
        │              Infrastructure / Data Layer               │
        │   (Database Repositories, ORMs, External API Clients)   │
        └────────────────────────────────────────────────────────┘
```

## Modular Directory Pattern
```
src/
├── domain/             # Pure entities, domain errors, repository interfaces
│   ├── entities/       # e.g. User.ts, Order.ts
│   └── repositories/   # Interfaces: IUserRepository.ts, IOrderRepository.ts
├── application/        # Application use cases & service workflows
│   ├── use-cases/      # CreateOrderUseCase.ts, AuthenticateUserUseCase.ts
│   └── dtos/           # Input / output transfer objects (Zod schemas)
├── infrastructure/     # Database implementations & external adapters
│   ├── database/       # Prisma / TypeORM / Drizzle repository implementations
│   └── mail/           # Resend / SendGrid email clients
└── presentation/       # Entry points (HTTP API controllers, CLI, WebSockets)
    ├── controllers/    # OrderController.ts, AuthController.ts
    └── middlewares/    # AuthMiddleware.ts, ErrorHandler.ts
```

## Key Rules
1. Inverted Dependencies: High-level business logic must never depend directly on low-level database libraries. They depend on abstractions (interfaces).
2. Swappable Adapters: You can replace PostgreSQL with MongoDB without touching a single line of domain business logic.
3. Testability: Every use case is testable in isolation by mocking the repository interfaces.
