---
name: mcr-responsive-styling
description: Implement modern responsive styling, Tailwind CSS utility systems, dark mode theming, view transitions, and smooth CSS animations.
---

# MCR Responsive Styling & Theming Skill

Use this skill when implementing application styling, mobile-first layouts, color systems, dark/light theme switching, and fluid micro-animations.

## Styling Guidelines

### 1. Mobile-First Responsive Breakpoints
Design for mobile screens first, enhancing progressively for larger viewports:
- Mobile: Default `< 640px` (single column, touch-friendly hit targets ≥ 44x44px).
- Tablet: `sm: 640px` / `md: 768px` (multi-column cards, condensed navigation).
- Desktop: `lg: 1024px` / `xl: 1280px` (full sidebar, multi-panel grids).

### 2. Design Tokens & Theme Switching
- Use CSS Custom Properties (CSS variables) for semantic colors:
  - `--background`, `--foreground`, `--primary`, `--secondary`, `--muted`, `--accent`, `--destructive`, `--border`.
- Support seamless Dark Mode using `class="dark"` or `@media (prefers-color-scheme: dark)`.
- Avoid hardcoded hex codes across components; always reference theme tokens.

### 3. Motion & Micro-interactions
- Keep transitions snappy and purposeful (150ms to 250ms with `ease-out`).
- Respect user accessibility preferences:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```
