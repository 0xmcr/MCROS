---
name: mcr-payments-billing
description: Integrate payment gateways (Stripe, Lemon Squeezy, PayPal), verify cryptographic webhooks, manage subscription billing lifecycles, and handle dunning and refunds.
---

# MCR Payments, Subscriptions & Billing Skill

Use this skill when implementing checkout sessions, recurring SaaS subscriptions, cryptographic webhook verification, customer billing portals, or automated refund handling.

## Supporting Resources & Submodules
- Webhook Signature Verifier Script: [verify_stripe_webhook.py](./scripts/verify_stripe_webhook.py)
- Reference Webhook Processor: [stripe-subscription-webhook.ts](./examples/stripe-subscription-webhook.ts)
- Security & PCI Standards: [payment-security-runbook.md](./references/payment-security-runbook.md)

---

## 1. Billing Integration Protocol

### Step 1: Checkout Session Initialization
- Create server-side checkout session with customer metadata (`userId`, `tenantId`, `tierPlan`).
- Redirect user to secure hosted checkout (Stripe Checkout or Lemon Squeezy).
- Return success and cancel URLs pointing back to application dashboard.

### Step 2: Cryptographic Webhook Handler
- Receive raw bytes and verify HMAC signature using [verify_stripe_webhook.py](./scripts/verify_stripe_webhook.py).
- Process subscription lifecycle events according to [stripe-subscription-webhook.ts](./examples/stripe-subscription-webhook.ts):
  - `checkout.session.completed` -> Provision account features.
  - `customer.subscription.updated` -> Update tier and renewal dates.
  - `customer.subscription.deleted` -> Gracefully downgrade access.
  - `invoice.payment_failed` -> Initiate email notification loop.

### Step 3: Self-Service Customer Billing Portal
- Provide a button in account settings that redirects to the payment provider's billing portal.
- Allow users to update credit cards, download PDF tax invoices, or cancel subscriptions without contacting customer support.
