# pumdoctrine — public governance layer

*pumdoctrine is a product of Madame Hong Co. Ltd. — the same company behind pumOFFICE.*

This repository is the **public governance record** of pumdoctrine: the doctrine
documents, the limits register, the lesson list, the external-verification log, and a
published audit case study. Alongside them are the standalone verification scripts and
sample receipts needed to check the record. It is the audit-first layer — published so
the governance model can be read and discussed.

**What is deliberately NOT here:** no product source code, no infrastructure, no
credentials, no internal names, no personal data. The implementation stays private; the
small verification scripts are published on purpose, so the record can be checked.

## Contents

- `governance/PUMDOCTRINE-EXPLAINED.md` — what pumdoctrine is, the laws, the evidence
  system, memory, self-healing, self-evolution, machine awareness, and the honest limits.
- `governance/PUM-SUITE-FACTBOOK-PUBLIC.md` — the public fact book (12 pillars + 500 facts).
- `governance/PUM-SUITE-4000.md` — a short summary of the whole thing.
- `limits/LIMITS-REGISTER.md` — every known limit, with its current status.
- `lessons/LESSONS.md` — the numbered lessons learned from the system's own mistakes.
- `EXTERNAL-VERIFICATIONS.md` — the log of checks made by people outside this project.
- `case-studies/navier-stokes-2026-09-14/` — an audit case study with re-runnable
  verification scripts.

## Check it yourself (30 seconds)

- `prove_it.py` — python verifier (needs: pip install cryptography)
- `verify.sh` — openssl-only verifier (no python, no libraries)
- `PUBLIC-VERIFICATION.md` — verify without trusting any code here (openssl first)
- `sample-receipt.json` + `public-key.pem` — a signed receipt and the key to check it

Run either one: `sh verify.sh` or `python prove_it.py` -> EVIDENCE VERIFIED.
Then change one letter in sample-receipt.json, run it again -> it fails. Thats the point.

## The rules this repository lives by

1. Facts only — every claim is tagged measured, observed, documented, or unknown.
2. Corrections are appended, never rewritten.
3. Verify the artefact, never the summary.
4. Additive only — nothing external may restrict the system or its owner.
5. No product code, no secrets, no personal data, ever.

*Every document here has been leak-scanned; the scan method is documented in the
private repository.*

## New in this edition (2026-09-23)

- `EXTERNAL-VERIFICATIONS.md` — the log of checks made by people outside this project.
  It is empty on purpose: an entry is only added after a real outside check, and the
  log is published now, before any prospect asks.
- `verify.sh` — a second, openssl-only verifier (no python, no libraries); both
  verifiers must agree on `EVIDENCE VERIFIED`.
- `governance/FOREVER-LIVE-DOCTRINE.md`, `governance/PUM-SUITE-FACTBOOK-PUBLIC.md`,
  `governance/VISION-ID-DOCTRINE.md`, and `limits/LIMITS-REGISTER.md` — re-synced from
  the current private documents.
- `PUBLIC-MANIFEST.json` + `PUBLIC-MANIFEST.sig` — re-signed for this edition; the
  manifest covers every published file, including the verifiers.

The audit chain is Merkle-anchored and a copy is held on a second machine; the
witness page itself stays on the owner's private network.
