# Workflow: 01 Idea to Product

## Purpose
End-to-end disciplined lifecycle to take an idea, problem statement, or user brief and turn it into verified, tested, production-ready software.

## Steps

### Step 1: Project Discovery & Workspace Inspection
- Run the `project-discovery` skill or inspect the current directory.
- Determine whether this is an empty workspace or an existing codebase.
- Identify dependencies, existing frameworks, and environment constraints.
- Populate or update `docs/PROJECT_CONTEXT.md`.

### Step 2: Research & Market Validation
- Conduct initial market and competitive research if building a commercial product.
- Identify user personas, key pain points, and existing alternative solutions.
- Record findings using `docs/templates/RESEARCH_REPORT.md`.

### Step 3: Product Requirements Definition (PRD)
- Draft a comprehensive PRD using `docs/templates/PRD.md`.
- Define MVP scope vs. future phases (P0, P1, P2).
- Establish testable acceptance criteria for every functional requirement.
- Identify non-functional requirements (security, latency, accessibility).

### Step 4: System Architecture & Tech Stack Selection
- Formulate the technical design and data models in `docs/ARCHITECTURE.md`.
- Document major technical trade-offs in `docs/templates/ADR.md`.
- Establish API contracts, schema models, and security boundaries.

### Step 5: Iterative Implementation
- Follow the core execution loop: Understand → Plan → Implement → Test → Review.
- Work in small, isolated, high-cohesion commits or tasks.
- Never write dead code, placeholder buttons, or unvalidated mocks.

### Step 6: Testing & Quality Assurance
- Create a test plan using `docs/templates/TEST_PLAN.md`.
- Implement unit tests, integration tests, and static analysis checks.
- Verify test passes with direct command output evidence.

### Step 7: Security Assessment & Release Readiness
- Perform defensive security review using `docs/SECURITY_REPORT.md`.
- Complete the release readiness checklist in `docs/RELEASE_READINESS.md`.
- Summarize results, verified deliverables, and remaining next steps.
