# pumdoctrine — public governance layer

*pumdoctrine is a product of Madame Hong Co. Ltd. — the same company behind pumOFFICE.*

This repository contains the public governance record of pumdoctrine: doctrine documents,
the limits register, lessons learned, the external-verification log, and a published audit
case study. It is the layer built for audit — published so the governance model can be read,
verified, and discussed.

## What's here

- `governance/PUMDOCTRINE-EXPLAINED.md` — doctrine, laws, evidence system, memory, self-healing, self-evolution, machine awareness, honest limits.
- `governance/PUM-SUITE-FACTBOOK-PUBLIC.md` — fact book (12 pillars + 500 facts) [M: counted in the file].
- `governance/PUM-SUITE-4000.md` — short summary.
- `limits/LIMITS-REGISTER.md` — every known limit, with current status.
- Training ledger — governance learning cycles, disclosed as dated scar entries in
  `limits/LIMITS-REGISTER.md` (ledger row + receipt hash per scar).
- `lessons/LESSONS.md` — numbered lessons from real failures.
- `EXTERNAL-VERIFICATIONS.md` — log of outside checks (empty until real entries exist).
- `case-studies/navier-stokes-2026-09-14/` — audit case study with re-runnable verification scripts.

## Verify it yourself (30 seconds)

- `prove_it.py` — Python verifier (pip install cryptography).
- `verify.sh` — OpenSSL-based verifier (no Python, no libraries).
- `PUBLIC-VERIFICATION.md` — verify without trusting any code here.
- `sample-receipt.json` + `public-key.pem` — signed receipt + key.

Run either: `sh verify.sh` or `python prove_it.py` → EVIDENCE VERIFIED.
Change one letter in sample-receipt.json, run again → it fails. That's the point.

## Rules this repository lives by

1. Facts only — every claim tagged measured, observed, documented, or unknown.
2. Corrections appended, never rewritten.
3. Verify the artefact, never the summary.
4. Additive only — nothing external may restrict the system or its owner [D: doctrine law].
5. No product code, no secrets, no personal data, ever. The verifier scripts are
   published on purpose; every document is leak-scanned, and the scan method is
   documented privately.
6. Scars are curated and disclosed — gate changes (e.g. authoritative-domain bypass)
   are docstring-documented, provenance-tagged, and logged in the training ledger.

## New in this edition (2026-09-23)

- `EXTERNAL-VERIFICATIONS.md` — published before any prospect asks.
- `verify.sh` — second verifier; both must agree on EVIDENCE VERIFIED.
- `governance/FOREVER-LIVE-DOCTRINE.md`, `governance/PUM-SUITE-FACTBOOK-PUBLIC.md`,
  `governance/VISION-ID-DOCTRINE.md`, `limits/LIMITS-REGISTER.md` — re-synced from
  private documents.
- `PUBLIC-MANIFEST.json` + `PUBLIC-MANIFEST.sig` — re-signed; the manifest covers every
  published file, including the verifiers.

The audit chain is Merkle-anchored and a copy is held on a second machine; the witness
page itself remains private.
