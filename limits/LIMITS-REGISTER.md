# Limits register

Each limit is published next to the wins, on purpose.

| Limit | Status |
|---|---|
| Strongest model tier | Restored via a cloud API (a dead credential was found and replaced) |
| Semantic search & tag filters | Need data wiring — labelled pending, not faked |
| Lasso selection, 3D context menu | Queued |
| Face-recognition models | Not installed; a simpler method runs |
| External audit | Not yet performed |
| Load-sensitive test | Named and tracked, not hidden |
| Calibration | Scored against real outcomes, published while it improves. Current measured window (2026-09-23, n=217): **Brier 0.039, ECE 0.0734 — inside the 0.1 target**. Earlier cumulative point (n=1,598: Brier 0.17, ECE 0.14) kept in the record, not rewritten; the most recent scored prediction (crypto, 2026-09-22) was WRONG and is included |
| Awareness | Measured self-knowledge only — no consciousness claim anywhere |

## 2026-09-20 additions (measured)

- Face ID has NO liveness detection on RGB-only cameras: a photo or video can pass.
  IR/depth hardware is the real fix (planned, not built).
- The two-camera presence check is a factor, not a silver bullet: two nearby RGB
  views see nearly the same scene.
- Fix-brain retrieval: keyword search plateaus on paraphrases; the local embedding
  experiment scored worse and failed ALL off-topic traps at every threshold tested
  (0.55-0.75). Keyword stays the default; semantic is opt-in. Negative
  discrimination is the open weakness (next: a local confirmation step).
- The receipt chain is hash-linked and externally anchored, not perfect: known break
  events are documented, including a fork that occurred after a lock fix.
- Camera device numbers move on USB re-enumeration; tools auto-detect, but hardware
  can still vanish mid-session.

## 2026-09-23 additions (measured)

- Calibration correction above. The published figure was stale and contradicted the
  current measurement; corrected in place with both numbers kept (append-only).
- **Doctrine hash is now a published artifact.** Every receipt carries a hash of the
  rule file it ran under. Registry of published doctrine hashes exists; the latest
  published rule hash is `2ad0d066d49215eb`. A receipt whose doctrine hash is not in
  the registry is from an unpublished ruleset — that is checkable.
- **Interop alignment:** the receipt/checkpoint format is being aligned to the IETF
  SCITT transparency-spec family (RFC 9943 / 9942, June 2026). Alignment claimed only
  where implemented; not yet a conformance claim.
- **Security review (measured, sanitized).** 7,641 requests in the public server log
  were parsed and classified: every exploit and secret-probe attempt returned 404 and
  no compromise was found. A decoy/honeypot surface is live on separate infrastructure
  (location and addresses withheld by policy). No hostnames or IPs are published.
- License terms remain intentionally unpublished pending legal review: the current
  LICENSE grants nothing. No pricing, availability or partner claim is made here.

## 2026-09-24 additions (measured)

- **Scar-10 — authoritative-domain bypass (training gate).** The brain-ingest
  training gate was blocking standards bodies whose pages never phrase-match the
  search snippets, so their content could not be learned. A curated list of
  authoritative domains is now admitted regardless of relevance: `spdx.dev`,
  `cyclonedx.org`, `sigstore.dev`, `slsa.dev`, `in-toto.io`, `theupdateframework.org`,
  `nist.gov`, `cisa.gov`. The change is docstring-documented and kept small;
  `UNVERIFIED` tags on stored content are unchanged; provenance is still recorded per
  entry (URL, fetch time, sha256). Training ledger row 10, receipt `a921cb5e`.
- **Honest eval note:** the supply-chain eval MRR moved from 0.658 to 0.567 in the
  same cycle. This is not claimed as an improvement — the eval expectations were
  tightened so the expected domains became the standards bodies themselves, and the
  comparison is not like-for-like. Published as such on purpose.
- **Publish gate (leak + claim, fail-closed).** Every public publish now runs a leak
  gate (21 leak patterns) and a claim gate; any leak or unsupported claim refuses the
  publish. `--skip-claims` is a documented escape hatch, and its use is logged.
- **Claim triage result (measured 2026-09-24).** The claim oracle ran over all public
  surfaces: 234 supported, 157 exempt, 0 unsupported (391 candidates; receipt `929683ec`).
- **Measurement tooling (five tools):**
  - Usage reconciliation — hourly usage exports reconciled against recorded usage.
  - Cold-cache A/B harness — capped, controlled before/after runs for cache behaviour.
  - Signed cost receipts — 17 required fields, signed, hash-chained, tamper-evident.
  - Usage accounting — usage exported in the official telemetry attribute scheme,
    with receipt and doctrine-hash extensions.
  - Claim oracle — every numeric or superlative claim in public text is
    verdict-tagged; unsupported claims refuse the publish.
- **Time layering — honest status.** The term is under investigation: every mechanism
  exists separately in the literature; the composition is unproven; claim-checked,
  not claimed. Usage exports reconcile to zero discrepancy across all hourly cells
  (measured, receipt available).

## 2026-09-26 additions (measured)

- **Doctrine v12 — SELF-SOVEREIGN** is the current published rule version.
- **Azure OpenAI and AWS Bedrock.** The gateway's inbound and upstream routes for both are
  live (routed and authenticated). **Not yet proven end-to-end against a real Azure
  resource** — staging was routed and authenticated with a stub upstream. Stated as pending,
  not claimed.
- **Interim licence.** `LICENSE` is now an **interim commercial licence**. It supersedes the
  earlier "grants nothing" notice; a final version is under legal review.
- **Anchor disclosure.** Merkle anchors 7 and 8 no longer match the chain because an earlier,
  documented repair re-signed entries inside their range. Both anchors are **retained and
  listed** as disclosed history (never deleted and never silently passed), and anchoring
  resumed. The tamper-evidence worked: it detected the rewrite.
- **Local model fit.** The local engine runs mostly on CPU on the current card (slow); cloud
  models are recommended for production, with local kept as the fallback.
- **External audit.** Still not performed.
