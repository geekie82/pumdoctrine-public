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
| Calibration | Scored against 1,598 real outcomes (Brier 0.17, ECE 0.14) — not yet within the 0.1 target; published while it improves |
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
