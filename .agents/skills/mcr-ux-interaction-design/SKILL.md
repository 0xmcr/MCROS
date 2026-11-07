---
name: mcr-ux-interaction-design
description: Design interactive UX flows, click event sequences, global toast notifications, modal dialogs, and instant user feedback loops.
---

# MCR UX Interaction & Feedback Design Skill

Use this skill when designing user experience interactions, click feedback behaviors, toast notification messaging systems, modal transitions, or form validation loops.

## Interactive Experience Standards

### 1. The Global Feedback & Toast Notification System
Every interactive application must provide immediate, non-blocking feedback for asynchronous actions:
- **Toast States**:
  - `Success`: "Project created successfully! Click here to view." (Green badge, auto-dismiss in 4s, checkmark icon).
  - `Error`: "Failed to save changes. Network timeout occurred." (Red badge, manual dismiss or 8s, retry action button).
  - `Warning`: "Unsaved changes detected. Navigating away will discard edits." (Amber badge, action buttons).
  - `Info / Loading`: "Uploading document (45%)..." (Blue badge with animated progress bar or spinner).
- **Positioning**: Bottom-right on desktop (`bottom-4 right-4`), top-center on mobile (`top-4 inset-x-4`).
- **Accessibility**: Wrap toasts in `aria-live="polite"` or `role="status"` to announce updates to screen readers without interrupting audio flow.

### 2. Click & Tap Interaction Design
- Immediate Visual Feedback: Button states must react in <50ms upon click (`active:scale-95`, ripple effect, or instant brightness shift).
- Debounce & Double-Click Guard: Disable submit buttons immediately upon click to prevent duplicate transactions, displaying an inline loading spinner.
- Destructive Confirmation: Irreversible actions (e.g. Delete Account, Drop Database) must trigger a two-step confirmation modal with explicit text verification.

### 3. Modal Dialogs & Bottom Drawers
- Desktop: Centered modal dialog with backdrop blur (`backdrop-blur-sm bg-black/40`), closing via `Escape` key, backdrop click, or `X` button.
- Mobile: Smooth swipe-down bottom drawer (sheet) with drag handle for ergonomic one-thumb operation.
- Focus Trapping: Trap tab focus within open dialogs; restore focus to the triggering element upon closing.
