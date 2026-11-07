#!/usr/bin/env python3
"""MCR Payment & Webhook Signature Verifier.
Simulates cryptographic HMAC-SHA256 signature verification for payment webhooks.
"""
import hmac
import hashlib
import time
import sys

def verify_signature(payload: bytes, signature_header: str, secret: str) -> bool:
    try:
        parts = dict(item.split("=") for item in signature_header.split(","))
        timestamp = parts.get("t")
        expected_sig = parts.get("v1")
        if not timestamp or not expected_sig:
            return False
        
        # Check for replay attacks (tolerance 300 seconds)
        if abs(time.time() - int(timestamp)) > 300:
            return False
            
        signed_payload = f"{timestamp}.".encode("utf-8") + payload
        computed_sig = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed_sig, expected_sig)
    except Exception:
        return False

def main() -> int:
    secret = "whsec_test_secret_12345"
    payload = b'{"type": "invoice.payment_succeeded", "id": "evt_test123"}'
    now = str(int(time.time()))
    signed_payload = f"{now}.".encode("utf-8") + payload
    sig = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    header = f"t={now},v1={sig}"
    
    if verify_signature(payload, header, secret):
        print("MCR Payment Webhook Signature Verifier: PASSED (HMAC-SHA256 verified)")
        return 0
    else:
        print("MCR Payment Webhook Signature Verifier: FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
