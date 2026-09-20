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
