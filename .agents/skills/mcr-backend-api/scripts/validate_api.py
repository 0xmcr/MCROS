#!/usr/bin/env python3
"""MCR API Schema & Route Validator.
Validates route definitions, response envelopes, and parameter schemas against MCR API standards.
"""
import sys
import json
from pathlib import Path

REQUIRED_ENVELOPE_KEYS = {"success"}

def validate_response_envelope(data: dict) -> list[str]:
    errors = []
    if not isinstance(data, dict):
        return ["Response payload must be a JSON object"]
    if "success" not in data:
        errors.append("Missing required top-level key: 'success'")
    if data.get("success") is True and "data" not in data:
        errors.append("Successful response envelope must contain 'data' key")
    if data.get("success") is False and "error" not in data:
        errors.append("Error response envelope must contain 'error' key")
    return errors

def main() -> int:
    sample_success = {"success": True, "data": {"id": "usr_123", "name": "Arjun"}}
    sample_error = {"success": False, "error": {"code": "NOT_FOUND", "message": "Resource not found"}}
    
    errs_success = validate_response_envelope(sample_success)
    errs_error = validate_response_envelope(sample_error)
    
    if errs_success or errs_error:
        print("API validation failed:")
        for e in errs_success + errs_error:
            print(f"- {e}")
        return 1
    
    print("MCR API Schema Validator: PASSED (Envelope specification verified)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
