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
- Measurement tooling — usage reconciliation, signed cost receipts, and an enforced
  claim gate that refuses to publish unsupported claims.

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

## New in this edition (2026-09-24)

- The claim gate is enforced at publish: dishonest statements cannot ship, and
  unsupported claims are zero across all public surfaces.
- Measurement tooling (five tools): usage reconciliation, a cold-cache A/B harness,
  signed cost receipts, usage accounting, and a claim oracle.
- Training ledger reference: learning cycles 1-10, scars, and receipts are tracked in
  the training ledger; dated entries are disclosed in `limits/LIMITS-REGISTER.md`.
- Cost-efficiency investigation (honest status): production cost telemetry is under
  investigation; prior art has been mapped (~3,900 sources [M 2026-09-24]); no
  efficiency claim is made until measurements reconcile.

The audit chain is Merkle-anchored and a copy is held on a second machine; the witness
page itself remains private.
