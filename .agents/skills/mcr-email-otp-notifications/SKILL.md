---
name: mcr-email-otp-notifications
description: Implement transactional email sending (Resend, SendGrid, SES), 6-digit cryptographic OTP generation, email verification links, password resets, and SPF/DKIM/DMARC deliverability.
---

# MCR Email, OTP & Notification Engineering Skill

Use this skill when implementing user email verification, password reset flows, one-time passwords (OTP), transactional email templates, or configuring email deliverability DNS records.

## Supporting Resources & Submodules
- Cryptographic OTP Generator Script: [generate_otp.py](./scripts/generate_otp.py)
- Reference Transactional Email Service: [resend-email-verification.ts](./examples/resend-email-verification.ts)
- Deliverability & DNS Manual: [email-deliverability-guide.md](./references/email-deliverability-guide.md)

---

## 1. Authentication Notification Flow

### Step 1: User Signup & OTP Generation
- When a user registers, generate a 6-digit cryptographic OTP using `./scripts/generate_otp.py`.
- Store the hash in Redis with a 5-minute TTL (`SETEX otp:user@example.com 300 <hash>`).
- Enforce a 60-second cooldown before allowing a resend.

### Step 2: Transactional Delivery via Resend / SES
- Dispatch email using [resend-email-verification.ts](./examples/resend-email-verification.ts).
- Ensure DKIM, SPF, and DMARC records are configured according to [email-deliverability-guide.md](./references/email-deliverability-guide.md) to guarantee inbox delivery.

### Step 3: Verification & Token Consumption
- User enters OTP on frontend.
- Backend verifies OTP against Redis hash using constant-time comparison (`crypto.timingSafeEqual`).
- Mark user record `is_email_verified = TRUE` and invalidate the Redis OTP key immediately.
