#!/usr/bin/env python3
"""prove_it — verify the published evidence yourself. Only needs: pip install cryptography

Checks, in order:
  1. the sample receipt signature against the published public key
  2. the tampered copy is rejected (tamper-evidence works)
  3. every published file matches the signed manifest (docs cannot be silently edited)
  4. the manifest signature itself is valid

Usage: python prove_it.py
"""
import base64
import hashlib
import json
import pathlib
import sys

from cryptography.hazmat.primitives import serialization

D = pathlib.Path(__file__).resolve().parent
pub = serialization.load_pem_public_key((D / "public-key.pem").read_bytes())
ok = True


def line(name, good, detail=""):
    global ok
    ok = ok and good
    print(f"{'PASS' if good else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


# 1. sample receipt signature
rec = json.loads((D / "sample-receipt.json").read_text())
sig = rec.pop("sig", "")
h = rec.pop("hash", "")
rec.pop("sig_alg", None); rec.pop("pub", None)
canon = json.dumps(rec, sort_keys=True, separators=(",", ":")).encode()
try:
    pub.verify(base64.b64decode(sig), h.encode())
    line("sample receipt signature", hashlib.sha256(canon).hexdigest() == h, h[:16])
except Exception as e:
    line("sample receipt signature", False, str(e)[:40])

# 2. tampered copy must fail
t = json.loads((D / "tampered-receipt.json").read_text())
tsig = t.pop("sig", "")
th = t.pop("hash", "")
t.pop("sig_alg", None); t.pop("pub", None)
tcanon = json.dumps(t, sort_keys=True, separators=(",", ":")).encode()
line("tampered copy rejected", hashlib.sha256(tcanon).hexdigest() != th)

# 3. file manifest
man = json.loads((D / "PUBLIC-MANIFEST.json").read_text())
bad = [f for f, hh in man["files"].items()
       if hashlib.sha256((D / f).read_bytes()).hexdigest() != hh]
line("all published files match the signed manifest", not bad,
     f"{len(man['files'])} files" + (f", changed: {bad[:3]}" if bad else ""))

# 4. manifest signature
msig = (D / "PUBLIC-MANIFEST.sig").read_bytes()
try:
    pub.verify(base64.b64decode(msig), (D / "PUBLIC-MANIFEST.json").read_bytes())
    line("manifest signature", True)
except Exception as e:
    line("manifest signature", False, str(e)[:40])

print()
print("EVIDENCE VERIFIED" if ok else "EVIDENCE FAILED")
sys.exit(0 if ok else 1)
