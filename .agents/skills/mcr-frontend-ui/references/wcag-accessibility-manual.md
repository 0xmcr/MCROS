# MCR Frontend Accessibility (WCAG 2.1 AA) Manual

---

## 1. Color Contrast Requirements
- **Normal Text (< 18pt or < 14pt bold)**: Minimum contrast ratio of **4.5:1** against the background.
- **Large Text (>= 18pt or >= 14pt bold)**: Minimum contrast ratio of **3.0:1**.
- **Interactive UI Components & Graphical Objects**: Minimum contrast ratio of **3.0:1** for borders, focus rings, and icons.

---

## 2. Keyboard Navigation & Focus Management
- Every interactive element (buttons, links, inputs, dropdowns) must be reachable via the `Tab` key.
- Never set `outline: none` without providing an explicit replacement focus indicator:
  ```css
  /* Compliant Focus Ring */
  button:focus-visible {
    outline: 2px solid #2563EB;
    outline-offset: 2px;
  }
  ```
- Modals & Dialogs: Must trap focus within the modal container while open and restore focus to the triggering element upon closure.

---

## 3. ARIA Roles & Semantic Markup
- Prefer native HTML5 tags over ARIA:
  - Use `<button>` instead of `<div onClick="...">`.
  - Use `<nav>` instead of `<div role="navigation">`.
- Live Regions for Asynchronous Updates:
  - Use `aria-live="polite"` for non-urgent updates (e.g. search result count changes, status toasts).
  - Use `aria-live="assertive"` only for critical time-sensitive errors.
