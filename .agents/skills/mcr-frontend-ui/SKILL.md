---
name: mcr-frontend-ui
description: Build responsive, accessible (WCAG 2.1 AA), and performant user interface components with proper loading, error, empty, and settled states.
---

# MCR Frontend UI Craftsmanship Skill

Use this skill when developing frontend user interfaces, building reusable design system components, optimizing user interactions, or ensuring web accessibility.

## Supporting Resources & Submodules
- Reference Component: [accessible-data-table.tsx](./examples/accessible-data-table.tsx)
- Accessibility Manual: [wcag-accessibility-manual.md](./references/wcag-accessibility-manual.md)

---

## 1. Frontend Engineering Workflow

### Step 1: Component State Completeness
Every interactive or data-fetching UI component must implement all 4 visual states:
1. **Loading State**: Skeletons preserving exact geometry to prevent Cumulative Layout Shift (CLS). See [accessible-data-table.tsx](./examples/accessible-data-table.tsx).
2. **Error State**: Actionable error banner with an explicit retry button.
3. **Empty State**: Clear guidance for first-time users.
4. **Settled State**: Polished presentation of active data.

### Step 2: Accessibility & Keyboard Navigation Audit
- Check color contrast ratios against [wcag-accessibility-manual.md](./references/wcag-accessibility-manual.md).
- Ensure all clickable elements use semantic `<button>` or `<a>` tags with visible `:focus-visible` rings.
- Ensure screen readers are notified of asynchronous updates via `aria-live="polite"`.

### Step 3: Performance & Core Web Vitals
- Optimize Largest Contentful Paint (LCP < 2.5s) using priority image loading.
- Minimize Interaction to Next Paint (INP < 200ms) by avoiding heavy blocking main-thread computations during user input.
