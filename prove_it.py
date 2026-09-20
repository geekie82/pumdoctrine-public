#!/usr/bin/env python3
"""prove_it — verify the published evidence yourself. Only needs: pip install cryptography

Checks: (1) sample receipt signature, (2) the tampered copy is rejected, (3) every
published file matches the signed manifest, (4) the manifest signature is valid.
Missing or corrupt files are reported as clean FAIL lines — never a traceback.
"""
import base64
import hashlib
import json
import pathlib
import sys

from cryptography.hazmat.primitives import serialization

D = pathlib.Path(__file__).resolve().parent
ok = True


def line(name, good, detail=""):
    global ok
    ok = ok and bool(good)
    print(f"{'PASS' if good else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def read_json(name):
    try:
        return json.loads((D / name).read_text())
    except Exception as exc:  # noqa: BLE001
        line(f"{name} readable", False, type(exc).__name__)
        return None


def read_bytes(name):
    try:
        return (D / name).read_bytes()
    except OSError as exc:
        line(f"{name} readable", False, "missing")
        return None


pub = None
pem = read_bytes("public-key.pem")
if pem:
    try:
        pub = serialization.load_pem_public_key(pem)
    except Exception:  # noqa: BLE001
        line("public key readable", False, "invalid key")

rec = read_json("sample-receipt.json")
if rec and pub:
    sig = rec.pop("sig", "")
    h = rec.pop("hash", "")
    rec.pop("sig_alg", None)
    rec.pop("pub", None)
    canon = json.dumps(rec, sort_keys=True, separators=(",", ":")).encode()
    try:
        pub.verify(base64.b64decode(sig), h.encode())
        line("sample receipt signature", hashlib.sha256(canon).hexdigest() == h, h[:16])
    except Exception:  # noqa: BLE001
        line("sample receipt signature", False, "signature does not verify")

t = read_json("tampered-receipt.json")
if t:
    t.pop("sig", None)
    th = t.pop("hash", "")
    t.pop("sig_alg", None)
    t.pop("pub", None)
    tcanon = json.dumps(t, sort_keys=True, separators=(",", ":")).encode()
    line("tampered copy rejected", hashlib.sha256(tcanon).hexdigest() != th)

man = read_json("PUBLIC-MANIFEST.json")
if man:
    changed = []
    for f, hh in man.get("files", {}).items():
        try:
            h = hashlib.sha256((D / f).read_bytes()).hexdigest()
        except OSError:
            changed.append(f + " (missing)")
            continue
        if h != hh:
            changed.append(f)
    line("all published files match the signed manifest", not changed,
         f"{len(man.get('files', {}))} files" + (f", changed/missing: {changed[:3]}" if changed else ""))

if pub and man is not None:
    msig = read_bytes("PUBLIC-MANIFEST.sig")
    mbytes = read_bytes("PUBLIC-MANIFEST.json")
    if msig and mbytes:
        try:
            pub.verify(base64.b64decode(msig), mbytes)
            line("manifest signature", True)
        except Exception:  # noqa: BLE001
            line("manifest signature", False, "does not verify")

print()
print("EVIDENCE VERIFIED" if ok else "EVIDENCE FAILED")
sys.exit(0 if ok else 1)
