# Public verification

You do not have to believe any claim in this repository. This page lets you check one.

## What you can verify yourself (30 seconds)

1. `sample-receipt.json` — a receipt produced by the system's signing key.
2. `public-key.pem` — the public half of that key.
3. `verify_receipt.py` — a standalone verifier that uses only the `cryptography`
   library (no code from this system).

```bash
pip install cryptography
python verify_receipt.py sample-receipt.json public-key.pem
```

Expected output: `OK: hash matches and the signature verifies against the public key`.

If you edit one character of the receipt, it fails. That is the point.

## Verify without trusting any code in this repo

Step 1 — openssl only (nothing from this repo):

    base64 -d PUBLIC-MANIFEST.sig > /tmp/m.sig
    openssl pkeyutl -verify -pubin -inkey public-key.pem -rawin -in PUBLIC-MANIFEST.json -sigfile /tmp/m.sig

You should see: Signature Verified Successfully

Step 2 — the manifest vouches for the verifiers. Compare:

    sha256sum prove_it.py verify.sh

with the hashes inside PUBLIC-MANIFEST.json.

Step 3 — now run either verifier (two independent implementations that must agree):

    sh verify.sh          (openssl only — no python, no libraries)
    python prove_it.py    (needs: pip install cryptography)

Expected: EVIDENCE VERIFIED from both.

## All four checks in one command

\`\`\`bash
python prove_it.py
\`\`\`

Expected: four PASS lines and \`EVIDENCE VERIFIED\`. It checks the receipt signature,
that a one-character edit is rejected, that every published file matches the signed
manifest, and that the manifest signature is valid.

## The record root as of 2026-09-20

- Records in the chain: **124438**
- Merkle root: `0742858e9e08e4b21901c872f9422eebd606b836a9a2e0de8e4d4b0d036c423d`

This root is published here so it cannot be quietly rewritten later: if the internal
record is changed, the root no longer matches what was published today. A copy of the
anchor is also held outside the main machine.


## It proves the signing system is real. It doesnt prove every claim.

**Proves:** a real signing system produced this receipt, and the published root is a
commitment to the record as of this date.

**Does not prove:** that every claim in the documentation is true. It proves the
evidence system is real; the claims still have to be checked one by one. That is why
the limits register is published next to the wins.

Corrections are appended, never rewritten.
