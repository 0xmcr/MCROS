---
name: mcr-brand-logo-design
description: Design brand identity systems, generate production SVG logos, app icons, favicons, color palettes, and typography guidelines for products.
---

# MCR Brand, Logo & Icon Design Skill

Use this skill when establishing product visual identities, generating vector SVG logos, crafting responsive favicon bundles, and defining design token color systems.

## Supporting Resources & Submodules
- Asset Generator Script: [generate_svg_icons.py](./scripts/generate_svg_icons.py)
- Reference Design Tokens: [brand-identity.json](./examples/brand-identity.json)
- Technical Vector Manual: [svg-standards.md](./references/svg-standards.md)

---

## 1. Visual Brand Design Workflow

### Step 1: Define Brand Personality & Core Colors
- Select high-contrast primary, secondary, and accent colors.
- Define accessible semantic tokens for Success, Warning, Error, and Info.
- Format tokens according to [brand-identity.json](./examples/brand-identity.json).

### Step 2: Vector SVG Logo Generation
- Execute `./scripts/generate_svg_icons.py` or author custom mathematical SVG paths.
- Enforce strict `viewBox` geometry without hardcoded width/height constraints.
- Implement theme awareness via CSS custom properties or `currentColor`.

### Step 3: Icon & Favicon Suite Export
Generate full web, iOS, and Android asset manifests according to [svg-standards.md](./references/svg-standards.md):
- `favicon.ico`
- `icon.svg`
- `apple-touch-icon.png` (180x180)
- `icon-192.png` & `icon-512.png`

### Step 4: Verification & Theme Audit
- Check color contrast ratios against WCAG AAA (7:1 for normal text, 4.5:1 for graphical objects).
- Test SVG scaling at 16px (favicon), 48px (app header), and 512px (splash screen) for visual clarity.
