#!/usr/bin/env python3
"""MCR Cryptographic OTP Token Generator.
Generates cryptographically secure 6-digit numeric OTPs and time-limited verification hashes.
"""
import secrets
import hmac
import hashlib
import time
import sys

def generate_secure_otp(length: int = 6) -> str:
    # Use secrets module (CSPRNG) rather than random module
    return "".join(secrets.choice("0123456789") for _ in range(length))

def generate_verification_hash(email: str, otp: str, secret: str, ttl_seconds: int = 300) -> dict:
    expires_at = int(time.time()) + ttl_seconds
    message = f"{email}:{otp}:{expires_at}".encode("utf-8")
    sig = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()
    return {
        "email": email,
        "otp": otp,
        "expires_at": expires_at,
        "token": f"{expires_at}.{sig}"
    }

def verify_token(email: str, otp: str, token: str, secret: str) -> bool:
    try:
        expires_at_str, expected_sig = token.split(".")
        expires_at = int(expires_at_str)
        if time.time() > expires_at:
            return False # Expired
        message = f"{email}:{otp}:{expires_at}".encode("utf-8")
        computed_sig = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed_sig, expected_sig)
    except Exception:
        return False

def main() -> int:
    secret = "mcr_secret_key_abcdef"
    email = "user@example.com"
    otp = generate_secure_otp()
    data = generate_verification_hash(email, otp, secret)
    
    if verify_token(email, otp, data["token"], secret):
        print(f"MCR OTP Generator: PASSED (Generated OTP {otp}, verified hash)")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
