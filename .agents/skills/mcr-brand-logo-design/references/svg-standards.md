# MCR Vector Graphics & SVG Accessibility Standards

---

## 1. Mathematical Scaling & ViewBox Rules
- Always specify `viewBox="0 0 512 512"` (or standard aspect ratio) instead of fixed pixel dimensions.
- Use `width="100%"` and `height="100%"` to allow clean CSS container scaling.
- Round coordinates to integers or at most 2 decimal places to minimize SVG file weight.

---

## 2. Dark & Light Theme Adaptability
To ensure logos look spectacular in both dark and light UI themes:
```xml
<!-- Adaptive SVG using CSS Variables -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <style>
    .brand-mark { fill: var(--logo-primary, #2563EB); }
    @media (prefers-color-scheme: dark) {
      .brand-mark { fill: var(--logo-dark-primary, #60A5FA); }
    }
  </style>
  <circle class="brand-mark" cx="50" cy="50" r="40" />
</svg>
```

---

## 3. Web & Mobile Icon Bundle Specifications
When exporting brand assets, generate the complete asset hierarchy:
1. `favicon.ico`: Multi-layer icon containing 16x16, 32x32, and 48x48 bitmaps for legacy browsers.
2. `favicon.svg`: Modern vector icon supporting dark mode via media query.
3. `apple-touch-icon.png`: 180x180 solid-background square with 0 corner radius (iOS rounds automatically).
4. `icon-192.png` & `icon-512.png`: Android Web App Manifest icons with `purpose: "any maskable"`.
