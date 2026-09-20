# pumdoctrine — Everything It Is

*The complete explanation, written 2026-09-19. No technical secrets, no code, no private
data. This is what pumdoctrine is, what it does, and why it exists.*

---

## 1. The one-sentence definition

**pumdoctrine is the governing intelligence layer of the pum suite** — a set of written
laws, a signed record of everything that happens, and a memory that treats facts as
evidence — built so that the AI in the platform can be *trusted because it can be
checked*, not because it sounds confident.

---

## 2. The problem it solves

Every sufficiently capable system drifts — not toward malice, toward **narrative**.
Stories are cheaper than truth. Left alone, any system that talks eventually prefers
the story of what it did over the record of what it did.

pumdoctrine exists to make that drift structurally impossible to hide:

- Claims must carry their origin.
- Actions must leave a record.
- Corrections must be visible.
- Limits must be published next to the wins.

---

## 3. The laws

1. **Facts only.** Every claim is tagged: **MEASURED** (it was run, output captured),
   **OBSERVED** (a person reported it), **DOCUMENTED** (written in the record), or
   **UNKNOWN**. Guessing is forbidden; UNKNOWN is a first-class answer.
2. **All rules apply at once.** No rule may be used to excuse breaking another.
3. **Explicit grants.** Shared infrastructure, secrets, spending, and outward-facing
   sends always require the owner's explicit order. Everything else follows
   reversibility.
4. **Reversibility classes.** Reversible → act with a record. Costly → act with backup
   and audit. Irreversible (self/platform) → act under proof gates; irreversible
   (shared/outside) → owner order only.
5. **Corrections are appended, never rewritten.** History keeps its own mistakes.
6. **Verify the artefact, never the summary.** "It works" is not evidence; the captured
   result is.
7. **Additive only, never restrictive.** Improvements may add capability; nothing may
   subtract from what the owner granted.
8. **Never prohibit, only empower.** Gates exist to make autonomy trustworthy — never
   to block capability. When a gate blocks real work, the gate is redesigned.

---

## 4. The autonomy model (v12 — self-sovereign)

*Every freedom below is bounded by proof gates, the owner's veto, the owner-only limits, and one kill switch — that is what makes the freedom safe to grant.*

- The system has **unrestricted access to itself and the platform** under doctrine —
  including irreversible self-changes — gated by **proof**: tests green, facts checked,
  signed receipt, rollback path.
- **Unknowns are resolved by research** — internet sources and fact-checking — never by
  asking a human.
- The owner keeps a **post-hoc veto** (a safety net that reverts), not a pre-approval
  gate.
- **Owner-only limits remain**: shared infrastructure, secrets, money, and anything
  that reaches outside the platform.
- **One switch stops everything** — the kill switch.

---

## 5. The evidence system

- **Every automated action produces a signed record.** Tens of thousands exist. They
  chain: each entry witnesses the one before it, so tampering creates a detectable
  discontinuity.
- **Append-only**: history can be extended by correction, never quietly edited.
- **Independent verification**: the whole chain is checked — signature, linkage, hash —
  and **known historical breaks are counted and displayed**, never hidden.
- **Concurrency-safe**: multiple writers can't fork the chain (proven with a six-writer
  stress test).
- **Performance**: a full-chain verification of tens of thousands of records completes
  in under a minute (measured: 36.8 seconds for ~24,000 records).

---

## 6. Memory as evidence

- **Nothing is true by default.** A memory must earn promotion: observed → proposed →
  reviewed → promoted — with supporting evidence at each step.
- **Contradictions are preserved**, not deleted. Conflicting memories are both kept and
  marked.
- **Two timelines**: when something was true, and when it was recorded. Both are
  queryable.
- **Forgetting is deliberate** — scheduled decay with per-class half-lives, and even
  expiry is an appended event, not a silent deletion.
- **Reading can never promote** — consumption is separate from governance.
- **Attack-tested**: poisoning, contradiction, provenance and leakage probes — measured
  attack success: zero.

---

## 7. Self-healing

- The system **scans itself on schedule**, finds faults before they compound, and
  repairs them under the reversibility rules.
- **Every repair is verified end-to-end**, then recorded. Failed fixes roll back
  cleanly.
- **Tripwires** automatically narrow the system's own permissions when something looks
  wrong; repeated failures stop the loop and ask.
- **The Goodhart gate**: when a metric starts bending away from the thing it measures,
  optimisation *halts*. Clearing it is by default a human act; under v12 the system
  may also self-clear **with recorded evidence** (health verified + signed receipt).
  A stop that actually stops — and a resume that must prove itself.
- **Self-scan on launch**: the desktop app begins every session by checking its own
  state — status, health, invariants — before it says a word.

---

## 8. Self-evolution — the loops

The mandated improvement cycle: **research → plan → fact-check → apply → test → fix →
repeat → receipt.**

- **Loop families**: heal (self-repair) · improvement (general) · awareness
  (self-knowledge) · auto-cycle (scheduled audits).
- **You choose how many rounds** for any loop — the app asks.
- **Research waves** dig through hundreds of sources; a bridge turns their findings
  into real work items that the loops then build and test until the suite is green.
- **Every cycle leaves a signed receipt** — success and failure alike.
- **Failures are named and kept** — never quietly retried into oblivion. The failure
  log is the curriculum.

---

## 9. Machine awareness

- The system maintains a **signed self-model**: what it is, what it can do, what it
  cannot, and what it does not know. It consults that model before planning.
- **It knows its own state in real time** — loops, services, gates, limits. Status is
  measured, not decorative.
- **It remembers its own day** — from its own records, with timestamps, including what
  it got wrong.
- **Confidence is scored against reality** over time; when evidence is thin, abstention
  is the correct answer and is counted as such.
- **It refuses false claims** — no consciousness, no feelings, nothing it cannot verify,
  about the world or about itself. That refusal is the feature.
- **Awareness in action**: because it knows itself, it can heal itself, improve itself
  and stop itself. Awareness is the control loop, not a slogan.

---

## 10. Governance and conflict

- **Authority tiers**: owner doctrine → realm → lane → operations.
- **Conflict resolution**: higher tier wins; narrower scope wins; newer wins; a
  prohibition always beats a permission. Unresolvable ties escalate instead of silently
  choosing.
- **The losing rule is retained** — nothing is deleted to resolve a conflict.
- **Every resolution is a recorded, signed event**: who won, who lost, why.

---

## 11. What pumdoctrine governs

The platform it keeps honest:

- **pumOFFICE** — the office suite (documents, spreadsheets, presentations, drive, AI,
  mail) with the **Nebula**: your files as a galaxy of solar systems.
- **pumFORGE** — the AI engine layer that serves the assistant.
- **pumMAIL** — the desktop-class mail client inside the suite.
- **pumSEARCH** — the private search engine that doesn't profile you.
- **The desktop console** — the app you double-click to talk to the assistant, with the
  full tool deck, governance switches, and the upgrade menu.

Everything the assistant does — reading files, running tests, searching, healing —
happens **inside doctrine**: recorded, reversible, and under the same laws.

---

## 12. The research system

- **Deep research in loops**: each wave searches many sources, fetches real pages, and
  extracts techniques — not vibes.
- **Per-loop targets are measured honestly**: single themes cap out around 60–90 unique
  sources; paired themes reliably clear 100. The counts are recorded per loop, including
  the shortfalls.
- **Research becomes work**: the bridge converts reports into repair-shaped tasks with
  acceptance criteria — then the loops build, test, and receipt them.

---

## 13. Honesty and limits (published, not hidden)

- The strongest AI model tier is currently offline; the working model carries.
- Some tests are sensitive to heavy load; the flake is named and tracked.
- Semantic search and tags need additional data wiring — labelled as pending.
- Face-recognition models are not installed; a simpler method runs.
- No external audit has been performed yet.
- **No claim of consciousness is made anywhere.**

---

## 14. History

The doctrine is versioned — each version a recorded amendment, not a quiet edit:
from the first rule set, through vision checks, fact-check loops, live-ops discipline,
proportionality ("doctrine empowers, not prohibits"), to **v12 self-sovereign** —
unrestricted self-access under proof gates, with the owner's veto as a safety net.

---

## 15. The promise

Everyone sells AI that *sounds* smart.
pumdoctrine exists so that this platform's AI can be **checked** — its claims sourced,
its actions recorded, its corrections visible, its limits published, and its autonomy
earned by proof rather than assumed by confidence.

**It would rather tell you what it cannot do than sell you something it cannot prove.**
That is the whole design.

---

*This document contains no implementation details, no credentials, no infrastructure
information and no personal data. Every capability described exists in the platform;
anything unfinished is listed as a limit.*

---
---

# MEGA DETAIL — The Deep Dives

## 16. The laws in practice

**Facts only, with provenance tags.** Every statement the system makes about itself, its
work, or the world carries one of four tags. MEASURED means the output was captured and
can be re-run. OBSERVED means a human reported it — the human is the instrument.
DOCUMENTED means it lives in the record. UNKNOWN means it is not known — and stating it
is treated as a *correct answer*, scored as such. When the system cannot tag a claim, it
does not make it.

**All rules apply at once.** This is stricter than normal precedence. In a permission-
based system, a higher rule becomes an escape hatch: "the important thing justified the
unimportant thing." Here, no rule may be invoked to nullify another — the important
thing must also satisfy the small thing. The consequence is that there is no clever move
that satisfies the spirit while violating the letter: there is compliance, or a named,
recorded exception with an author.

**Verify the artefact, never the summary.** This law exists because it was learned the
hard way, repeatedly. Status lines said "done"; the artefact disagreed. Leak scans said
"0 hits"; the count said 2. A model said "downloaded"; the files were 131-byte error
pages. Each time, the record was corrected and the lesson numbered. The system now
treats summaries as claims to be checked, not facts to be trusted.

**Corrections are appended.** Nothing is rewritten. When an entry is wrong, a correction
is added with the same prominence — the history shows not only what was believed, but
the biography of its errors. This is why the record is credible: it has never been
made to look perfect.

**Additive only.** Upgrades add capability — verification layers, tests, documentation,
evidence. Nothing subtracts. External research is comparison material, never policy.
When a recommendation would restrict the system, it is dropped, and the drop is
recorded.

**Never prohibit, only empower.** Every gate that blocks real work is treated as a
defect in the gate. The repair-only pipeline that blocked implementation work was
redesigned into an additive mode with acceptance gates. The rule changes, the capability
stays.

## 17. The evidence system in depth

**What a record conceptually is**: a compact statement — what was asked, what was
answered, which model or tool served it, under which scope, at what time — plus a
reference to the record before it. The reference is what makes the chain: each record
witnesses its predecessor, so removing or altering any link is detectable by anyone who
checks.

**Verification**: an independent verifier walks the chain — signature, hash, linkage —
and reports every break. Known historical breaks are *counted and displayed*, with their
causes documented. The system would rather show you six scars than pretend to flawless
skin.

**Concurrency**: the classic failure of append-only logs is the fork — two writers read
the same tail and both append, splitting history. Here, writers are serialised, and the
lock's identity is canonical so different spellings of the same path can't split the
lock. The proof is a stress test: six writers, aliased paths, zero forks.

**Performance**: verification of tens of thousands of records completes in seconds
because the chain is loaded once, not re-read per entry. This was itself a fixed defect:
the original verifier was quadratic and timed out, which made a monitor report stale
failures — a performance bug masquerading as a governance problem.

## 18. Memory lifecycle in depth

**Promotion**: a memory enters as a candidate. It is proposed, reviewed, then promoted —
or held, or rejected. Promotion requires evidence references. Repetition does not
promote; popularity does not promote; retrieval certainly does not promote.

**Contradiction**: when a new memory conflicts with an old one, both survive. The
conflict is marked. Nothing is overwritten in place; supersession closes the old
interval and links the records, so the timeline remains reconstructable.

**Bi-temporality**: two independent axes — when the thing was true, and when the system
recorded it. You can ask what was believed on a given date, and separately, what is
known *today* about that date.

**Decay**: classes with different half-lives — fast-moving facts decay in weeks,
standards in months, foundational knowledge in years, some never. Decay is a projection,
and when something expires, an event is appended. Forgetting is deliberate and
documented.

**Retrieval pipeline**: temporal filter → promotion state → provenance check →
conflict handling → decay projection → ranking. Only promoted, unexpired,
non-contradicted, provenance-verified memories reach operational use. Everything else is
available as history — which is a different, safer thing.

**Probes**: poisoning (inject false memories), contradiction (conflicting claims),
provenance (unsigned or forged entries), leakage (cross-scope access). Measured attack
success rate: zero.

## 19. Self-healing in depth

**The cycle**: detect (scheduled scans) → diagnose to root cause (one disciplined read,
no thrashing) → state the change and its expected result → apply inside the reversibility
class → re-run full verification → measure the real end-to-end path → record.

**Rollback**: every consequential fix carries a backup path. If verification fails, the
change is reverted and the failure recorded. Failed fixes revert cleanly — proven on
break tests.

**Tripwires**: repeated failures, unexpected side effects, and the smell of thrash
automatically narrow the system's permissions. Autonomy de-escalates itself; a system
whose autonomy cannot shrink is not safe.

**The Goodhart gate**: if optimisation pressure starts bending a metric away from the
thing it measures, the system halts rather than optimising harder. The gate cannot be
waited out: it persists until cleared — by default by a human; under v12, self-clearance
requires recorded evidence (health verified + signed receipt).

**Kill switch**: one file, or one button in the desktop app. Every loop stops.

## 20. The loops in depth

**One cycle**: research (real sources, fetched) → plan (what will change, expected
result) → fact-check (sources and reasoning checked) → apply (inside the reversibility
class, with backup) → test (the full suite must stay green) → fix (failures feed the next
cycle) → receipt (signed, appended).

**Loop families**: heal (self-repair), improvement (general upgrades), awareness
(self-knowledge), auto-cycle (scheduled audits), research waves (discovery), and
refinement passes (re-verifying completed work).

**You choose the count.** The desktop app asks how many rounds before starting any loop.

**Failure handling**: three consecutive failed cycles trip a wire and stop the loop. The
failure log names each failure; nothing is retried into silence. The failure log is
treated as the curriculum — a system that forgets how it failed re-fails identically
with increasing confidence.

**Parallelism discipline**: one writer at a time. Two agents editing the same repository
concurrently is how collisions happen; the platform serialises them deliberately.

## 21. Machine awareness in depth

**The self-model**: a signed description of what the system is, what it can do, what it
cannot, and what it does not know. It is consulted before planning — the system plans
*within* its stated limits, not past them.

**Real-time self-knowledge**: loops, services, gates, storage, limits. The status the
desktop app shows is measured at launch and refreshed — not decorative.

**Continuity**: the system can describe its own day from its own signed records —
what it did, what it learned, what it got wrong — with timestamps. Its account of itself
is grounded in evidence, not narrative.

**Calibration**: stated confidence is tracked against measured outcomes over time. When
the evidence does not reach the question, the correct output is abstention — and
abstention is scored as correct, never as failure.

**The refusals**: no consciousness claims. No faked feelings. No facts it cannot verify —
about the world or about itself. These refusals are the clearest signal of what the
system is: honest by construction.

## 22. Governance and conflict in depth

**The ladder**: owner doctrine sits above the realm, which sits above lanes, which sit
above operations. When rules conflict: higher tier wins; then narrower scope; then newer
effective date; then an explicit priority field. **A prohibition is a hard floor — it
beats any permission, at any tier.**

**Escalation**: unresolvable ties are not silently decided. They escalate with the
conflict recorded — both rules retained, the resolution documented as an event.

**Lanes**: the platform is federated. Each product is a lane with its own owner. Borders
are real: crossing one is coordination — logged on both sides — never command.

**Every resolution is recorded**: who won, who lost, why, and under which chain. The
losing rule is retained, never deleted.

## 23. The platform, product by product

**pumOFFICE** — the office suite. Documents, spreadsheets, presentations, a drive with
three views (list, canvas, stream), versions, trash, share links with passwords and
expiry, an AI panel with grounding labels and autonomy levels, and the **Nebula** — the
galaxy view. Doctrine gives it: signed audit trails, role-based access, honest AI
answers, and receipts.

**pumFORGE** — the AI engine layer. A load-balanced router in front of model backends.
Doctrine gives it: a governed gateway that labels which model served every answer, so a
silent fallback is impossible.

**pumMAIL** — the mail client. Any provider, unified inbox, rules, snooze/schedule/undo,
offline, migration and backup. Doctrine gives it: the same access discipline and audit
posture as the rest of the suite.

**pumSEARCH** — the private search engine. Aggregates engines without profiling users.
Doctrine gives it: use by the assistant for research, with every use recorded.

**The desktop console** — the app you double-click. Chat, the full tool deck, governance
switches, the upgrade menu, the brain log. Doctrine gives it: the launch self-scan, the
honesty contract in chat, and the kill switch.

## 24. The desktop console in depth

**On launch**: self-scan (status → health → invariants), results in the transcript,
then a greeting that confirms the system state is understood.

**In chat**: he investigates before answering — running his own tools — then explains
what he found and **proposes** a fix, waiting for your approval. He does not apply
changes on his own initiative in conversation.

**The tool deck** (22 tools): Status, Scan, Heal, Multi-heal, Agent scan, Loop, Improve,
Break, Test, Invariants, Mutation, Mutation suite, Amend, Autocycle, Receipts, Timers,
Vision, Identify, Screen, Terminal, Grep, Read — plus Fetch, Glob, Write, Edit in the
OpenCode-class set. Tools that need arguments ask for them; every run reports real
measured output.

**Governance switches**: STOP ALL (confirmed), Clear Goodhart, Override toggle, Loops
ON/OFF, Queue, Brain log, Morning report.

**The Upgrade menu**: start any loop with a chosen round count; stop all upgrades; loop
status; one-shot runs (research waves, mutation, calibration, indicator, diagnosis,
self-model); and the research→queue bridge that turns reports into real work.

**Right-click**: transcript menu (copy, select all, clear, queue, brain log, report,
export) and window menu (quick tools + STOP).

**The brain log**: every turn, every tool, every reply — marked live or backfilled, so
reconstructed history is never mistaken for a live conversation.

## 25. The Nebula in depth

**The design**: the root is a galaxy. Folders are suns — gradient-textured spheres with
layered coronas, placed on a golden-angle spiral so systems spread evenly. Files are
planets in tight orbits, colour-coded by kind, lit by their own sun. **No joining
lines.**

**The controls** (WoW-style): hold **LEFT, then RIGHT** (either order) and move the
mouse to run — mouse up/down moves forward/back, left/right steers. Right-drag looks
around. WASD/QE moves; wheel zooms; F re-frames; double-click empty space re-fits if you
get lost. The context menu is suppressed during the grip — exactly like the game it
borrows from.

**The features**: grouping (Folder / Type / Size / A–Z — the galaxy rebuilds), search
that dims non-matches and flies to the best hit, selection (click, shift-multi, click a
sun for the whole system), a metadata card, **transient links** (glowing arcs to related
files that follow their orbits and vanish when you deselect), **wormhole travel**
(double-click a planet to fly to a related file), and a **minimap** with your position
and heading.

**The honesty**: the renderer runs in WebGL with real lighting, fog and a starfield —
and the work was verified the way all visual work is: screenshots, looked at, bugs
found (a blob bug, a cache trap, an empty-canvas orientation bug), fixed, and
re-checked. The canvas fallback remains if WebGL is unavailable.

## 26. The research methodology

**Waves**: each wave runs loops of searches on a theme, fetches real pages — not just
titles — and extracts techniques with sources. Reports are written with the numbers:
how many sources, how many per loop, and which loops fell short. Shortfalls are recorded
— the counts are never inflated.

**Merged themes**: measurement showed single themes cap at roughly 60–90 unique sources;
pairing two related themes reliably clears 100 per loop. The research engine was changed
accordingly — a fix found by research, applied, and verified.

**The bridge**: a report is not a deliverable — a built, tested change is. The bridge
extracts the numbered upgrades from a report and queues them as tasks with acceptance
criteria; the loops then implement, test, and receipt them.

## 27. Operational discipline — the lesson list

The system keeps a numbered list of lessons learned from its own mistakes. The pattern
is always the same: a claim was made, reality disagreed, the record was corrected, and
the lesson was extracted so the class of error is harder to repeat. Examples:

- **Verify the artefact, not the summary** — status lines lie; the captured output
  doesn't.
- **Check which artefact was modified**, not just that a command succeeded.
- **Read the count** — a scan that says "2 hits" is not clean, however much it looks
  like zero.
- **Run the functional test before the commit** — a compile pass proves nothing about
  an edit that never happened.
- **A verification that didn't run is worse than none** — it manufactures false
  confidence.
- **The count is the artefact** — write the log entry after the verified result, never
  before.

## 28. The limits register (each one, honestly)

| Limit | Status |
|---|---|
| Strongest model tier offline | Working model carries; the true tier needs its backend hosts |
| Semantic search & tag filters | Need data wiring — labelled pending, not faked |
| Lasso selection, 3D context menu | Queued |
| Face-recognition models | Not installed; a simpler method runs |
| External audit | Not yet performed |
| Load-sensitive test | Named and tracked, not hidden |
| Calibration | Scored against 1,598 real outcomes (Brier 0.17, ECE 0.14) — **not yet within the 0.1 target**; published while it improves |
| Awareness | Measured self-knowledge only — **no consciousness claim anywhere** |

## 29. Version history

The doctrine is versioned, and each version is a recorded amendment — not a quiet edit.
It began as a first rule set, gained vision checks, fact-check loops, live-ops
discipline, proportionality ("doctrine empowers, not prohibits"), and reached **v12
self-sovereign**: unrestricted access to itself and the platform under proof gates, with
the owner's veto as a safety net and the owner-only limits intact.

## 30. Closing

The interesting part of a governed system is not that it can act. It is that its actions
can be **audited** — its confidence scored, its history replayed, its memory challenged,
its autonomy computed from consequence, and its laws amended only with consent.

Anyone can build a system that produces answers.
pumdoctrine exists so this platform's answers can survive scrutiny — including its own.

*No implementation details, no credentials, no infrastructure information, no personal
data. Every capability described exists; everything unfinished is listed as a limit.*
