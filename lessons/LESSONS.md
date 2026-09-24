# Lessons learned (from the system's own mistakes)

Each lesson was extracted from a real failure, recorded, and kept. Corrections are
appended, never rewritten.

1. Verify the artefact, not the summary line — status lines lie; the captured output doesn't.
2. Check which artefact was modified, not just that a command succeeded.
3. Read the count — a scan that says "2 hits" is not clean, however much it looks like zero.
4. Run the functional test before the commit — a compile pass proves nothing about an edit that never happened.
5. A verification that didn't run is worse than none — it manufactures false confidence.
6. Write the log entry after the verified result, never before.
7. The count is the artefact.
8. A parser must be verified before a zero is trusted.
9. A loop count is total cycles, not additional ones.

23. After rotating a secret, restart every service that caches it at startup —
    the file being correct is not the service being correct.
24. A proxy that normalizes messages must merge, not pick one and drop the rest: dropped
    context is invisible and produces confident false denials.
25. Never enroll from the camera's opening frame: auto-exposure warmup frames are
    near-black and produce garbage templates. Gate on brightness and detector
    confidence.
26. Publish negative results: the semantic search experiment did not beat keyword
    search and failed off-topic traps at every threshold — measured, documented,
    and deliberately not shipped as the default.
