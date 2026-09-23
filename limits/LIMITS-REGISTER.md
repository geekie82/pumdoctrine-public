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
