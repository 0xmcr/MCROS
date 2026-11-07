---
name: mcr-motion-animation
description: Implement high-performance 60fps animations, Framer Motion micro-interactions, layout transitions, and scroll-driven effects.
---

# MCR Motion & UI Animation Skill

Use this skill when implementing fluid animations, page transitions, interactive micro-interactions, or complex scroll-driven effects in web and mobile applications.

## Motion Design Principles

### 1. The Physics of Natural Motion
- **Spring Physics**: Prefer spring animations over linear easing for natural feel (`stiffness: 300, damping: 25`).
- **Timing Standards**:
  - Micro-interactions (hover, active button, tooltip): `150ms - 200ms`.
  - Content Transitions (modals, drawers, toasts): `250ms - 350ms`.
  - Page / Screen Routes: `300ms - 400ms`.

### 2. Implementation Technologies
- **React & Next.js**: Framer Motion (`motion.div`, `AnimatePresence`, `layoutId` shared element transitions).
- **Complex SVG & Canvas**: GSAP (GreenSock) with ScrollTrigger for pinning, scrubbed parallax, and timeline orchestrations.
- **Modern Browser Native**: View Transitions API (`document.startViewTransition`) for zero-bundle-size native morphing.

### 3. Hardware Acceleration & Accessibility
- **GPU-Accelerated Properties**: Only animate `transform` (`translate3d`, `scale`, `rotate`) and `opacity`. Never animate `top`, `left`, `width`, or `margin` to prevent costly browser reflows and jank.
- **Prefers-Reduced-Motion**: Always respect user motion sensitivity:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
    }
  }
  ```
