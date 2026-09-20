#!/usr/bin/env python3
"""Independent verifier for a pumdoctrine receipt. Requires: pip install cryptography

Usage: python verify_receipt.py sample-receipt.json public-key.pem
"""
import base64
import hashlib
import json
import sys

from cryptography.hazmat.primitives import serialization

rec = json.load(open(sys.argv[1]))
pub_pem = open(sys.argv[2], "rb").read()

sig = rec.pop("sig", "")
h = rec.pop("hash", "")
alg = rec.pop("sig_alg", "")
rec.pop("pub", None)

canonical = json.dumps(rec, sort_keys=True, separators=(",", ":")).encode()
if hashlib.sha256(canonical).hexdigest() != h:
    print("FAIL: hash mismatch — the receipt was altered")
    sys.exit(1)

pub = serialization.load_pem_public_key(pub_pem)
try:
    pub.verify(base64.b64decode(sig), h.encode())
except Exception:
    print("FAIL: signature does not match the public key")
    sys.exit(1)

print("OK: hash matches and the signature verifies against the public key")
print("receipt hash:", h)
print("scope:", rec.get("scope"), "| model:", rec.get("model"), "| ts:", rec.get("ts"))
