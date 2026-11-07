---
name: mcr-frontend-ui
description: Build responsive, accessible (WCAG 2.1 AA), and performant user interface components with proper loading, error, empty, and settled states.
---

# MCR Frontend UI Craftsmanship Skill

Use this skill when developing frontend user interfaces, building reusable design system components, optimizing user interactions, or ensuring web accessibility.

## Engineering Standards

### 1. Component State Completeness
Every interactive or data-fetching UI component must handle all 4 visual states:
1. Loading State: Skeleton loaders or subtle spinners preserving layout geometry (preventing CLS).
2. Error State: Clear, non-technical feedback with an actionable retry button.
3. Empty State: Helpful illustration or text guiding first-time users to take action.
4. Settled / Success State: Clean, responsive presentation of data with appropriate feedback.

### 2. Accessibility (a11y) & Usability
- Semantic HTML: Use `<button>`, `<nav>`, `<main>`, `<article>`, `<header>`, `<dialog>` rather than clickable `<div>` elements.
- Keyboard Navigation: Ensure all interactive elements are focusable, tab-navigable, and display visible focus rings.
- ARIA: Correct `aria-label`, `aria-expanded`, `aria-haspopup`, and `role` attributes where native HTML tags are insufficient.
- Color Contrast: Minimum 4.5:1 contrast ratio for normal text and 3:1 for large text.

### 3. State Management & Performance
- Single Source of Truth: Centralize application state predictably (Zustand, Redux Toolkit, or React Context).
- Optimistic Updates: Update UI immediately upon user action, with automatic rollback if the server request fails.
- Core Web Vitals: Minimize Cumulative Layout Shift (CLS < 0.1), Largest Contentful Paint (LCP < 2.5s), and Interaction to Next Paint (INP < 200ms).
