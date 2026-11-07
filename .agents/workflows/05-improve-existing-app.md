# Workflow: 05 Improve Existing Application

## Purpose
Disciplined engineering workflow to inspect, diagnose, refactor, or enhance an existing codebase without regressions or unrelated rewrites.

## Steps

### Step 1: Codebase Inspection
- Run `project-discovery` skill.
- Map directory structure, framework versions, package manifests, and test suites.

### Step 2: Architecture & Defect Mapping
- Trace data flows, state stores, and entry points.
- Identify specific bottlenecks, defects, security vulnerabilities, or tech debt.

### Step 3: Targeted Proposal
- Formulate a small, high-impact implementation plan.
- Review risks and obtain user alignment on changes before editing code.

### Step 4: Focused Implementation
- Execute changes in small, incremental steps.
- Preserve existing coding conventions, file structure, and unaffected modules.

### Step 5: Verification & Regression Check
- Run existing test suites and add new targeted tests for modified logic.
- Verify that previous functionality remains intact.
