---
trigger: glob
globs: "**/*.{tsx,jsx,vue,svelte,html,css,scss}"
---

# Frontend Engineering Guidelines

## Core Principles
- Responsive & Accessible: WCAG 2.1 AA compliant, semantic HTML5, keyboard navigable, full ARIA support.
- State & Data Management: Predictable single-source-of-truth state handling, optimistic updates with rollback, robust error handling.
- Visual Quality & UX: Complete lifecycle states for all interactive elements:
  - Loading states (skeletons or spinners)
  - Error states (actionable feedback and retry buttons)
  - Empty states (helpful guidance for first-time use)
  - Success / settled states
- Performance: Core Web Vitals targets (LCP < 2.5s, INP < 200ms, CLS < 0.1), dynamic imports, image optimization, tree-shaking.
- Testing: Component tests (Testing Library / Vitest), visual regression where applicable, end-to-end user journey tests (Playwright).
