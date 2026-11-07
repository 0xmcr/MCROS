---
name: mcr-brand-logo-design
description: Design brand identity systems, generate production SVG logos, app icons, favicons, color palettes, and typography guidelines for products.
---

# MCR Brand, Logo & Icon Design Skill

Use this skill when designing a brand identity, creating logos, crafting vector SVG assets, establishing color palettes, or generating icon sets for web, mobile, and desktop applications.

## Brand Identity Architecture

### 1. Vector Logo & Icon Generation (SVG)
- Clean, Scalable Vectors: Create clean, mathematical SVG code with responsive viewBox parameters (e.g. `viewBox="0 0 512 512"`).
- Dark / Light Mode Adaptability: Use `currentColor` or CSS custom properties for stroke/fill so logos automatically switch between dark and light themes.
- Favicon & App Icon Bundle:
  - `favicon.ico` (multi-resolution 16x16, 32x32)
  - `icon.svg` (modern scalable browser tab icon)
  - `apple-touch-icon.png` (180x180 for iOS Home Screen)
  - `icon-192.png` and `icon-512.png` for Android PWA Web App Manifest

### 2. Design Tokens & Color Harmony
- Primary Brand Accent: High-contrast primary color matching brand personality.
- Functional Palette: Semantic tokens for Success (Green), Warning (Amber), Error (Red), and Info (Blue).
- Neutral Scale: Muted grays/slates for backgrounds, cards, borders, and typography.
- Contrast Ratios: Ensure all text-on-color combinations pass WCAG AAA (7:1) or AA (4.5:1).

### 3. Typography Pairing
- Display / Heading Font: Strong, modern geometric or grotesque sans-serif (e.g. Inter, Outfit, Plus Jakarta Sans, Geist).
- Body / Reading Font: High-legibility sans-serif with distinct optical sizing.
- Monospace Font: Clean code font (JetBrains Mono, Fira Code, Geist Mono).
- Output: Export specifications into `docs/BRAND_GUIDELINES.md`.
