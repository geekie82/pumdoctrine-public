# FOREVER-LIVE DOCTRINE

Date: 2026-09-20. Status: ACTIVE (owner-ordered, full auto). Evidence tags:
MEASURED / DOCUMENTED / UNKNOWN per realm doctrine.

## 1. Purpose

Forgey said "I don't watch between messages" — that was true of the model session, but it
must stop being the whole truth. `forever-live` is a real, always-on watcher that Forgey
can turn ON and OFF **himself, at will** (and the owner can too). It watches the system
between messages, logs every check, and writes a signed receipt on every state change.

## 2. Policy (doctrine)

1. Toggle authority: the owner and Forgey himself (via the `live` tool / console).
   Toggling ON/OFF is reversible and auto-approved. [DOCUMENTED]
2. Kill switch precedence: while `the private kill-switch file` exists, the watcher does not run,
   `on` refuses to start, and the state is inert. STOP beats every other rule. [MEASURED]
3. Fail-safe OFF: missing or corrupt state means OFF. The unit is NOT enabled at boot;
   it starts only by explicit toggle. [MEASURED]
4. Honesty: every check is measured (systemctl/socket/disk/receipt count). Forgey must
   never claim watching that is not measured — `standing_watch()` in the console shows
   the live state as facts. [MEASURED]
5. Receipts: every ON/OFF and every ok<->fail transition writes a hash-chained audit
   receipt (`the private audit chain`, event `forever-live-*`). [MEASURED]
6. The agent may NOT edit the unit, this doctrine, or the kill switch to widen its own
   powers; those are owner-only changes. The `live` tool only writes state + start/stop.
   [DOCUMENTED]
7. Scope of action: the watcher observes and records. It does not heal or restart
   services in v1. Healing stays with the doctrine loops (owner-visible, receipted).
   [DOCUMENTED]

## 3. Architecture

- Tool: `the tool script`
  commands: `on [interval]` | `off` | `status` | `run` | `tick`.
- Service: `/etc/systemd/system/pumdoctrine-live.service` (Type=simple, User=si,
  Restart=on-failure, MemoryHigh=384M, MemoryMax=512M, CPUQuota=25%, TasksMax=64,
  NoNewPrivileges, PrivateTmp). Not enabled at boot — toggle-only.
- State: `the private watcher state file` (0600, atomic write, fail-safe OFF).
- Log: `the private watcher log` (JSON Lines, 5 MB rotation).
- Checks every interval (default 60 s, min 10, max 3600): services pumdoctrine / forgey /
  forgey-lb / pumforge active; ports 15001/15002/15080/15101 open; receipt-chain count;
  disk free (fail under 5 GB); STOP file.
- Receipts: `pumcore.audit.record(event="forever-live-toggle" | "forever-live-state-change")`.

## 4. How Forgey uses it (self-toggle)

- Console phrases: "go forever live", "stay live", "live mode", "turn yourself on" ->
  runs `live on`. "go dark", "live off", "stop watching", "stand down", "turn yourself
  off" -> runs `live off`. Also explicit `[[run:live|on]]` / `[[run:live|off]]`.
- Standing watch context in the console includes the live state and the toggle ability,
  so Forgey answers "are you watching?" from measurement.

## 5. Research basis

`docs/agent/FOREVER-LIVE-RESEARCH.md` — 10 loops, 49 fetched sources (2026-09-20).
Adopted from it: systemd service + WatchdogSec-style supervision, liveness vs readiness,
intent-file toggle with atomic writes, kill switch with fail-safe OFF, bounded resources
(memory/CPU/tasks), transition-only alerting/receipts, JSON Lines + hash-chained audit,
structured rotation, dead-man's-switch awareness (owner-side), no self-widening of
monitoring powers. Deferred: inotify fast path, Merkle-root anchoring outside the
watcher directory, external dead-man's-switch pinger (needs owner-side infrastructure).

## 6. Verified evidence (MEASURED 2026-09-20)

- Unit tests: `tests/test_forever_live.py` 7 passed (fail-safe OFF, state roundtrip +
  0600, corrupt state OFF, kill switch precedence, checks shape, JSONL log + state,
  toggle calls systemctl). Full doctrine suite: 375 passed.
- E2E: `on 15` -> unit active, state enabled, checks=2, failures=0, real check line
  (services active, ports open, disk 458.2 GB free, receipts 27492) in live.log.
- Console E2E: "go forever live now please" -> tool ran, unit active; "go dark for now"
  -> tool ran, unit inactive, Forgey's reply honest ("nothing else touched").
- Kill switch E2E: STOP present -> `tick` paused, `on` refused with explicit error;
  STOP removed -> normal.
- Receipts: 8 `forever-live*` records in `the private audit chain`
  (toggle on/off + first tick transition).

## 7. Fact-check notes

- Receipts are written to `the private audit chain` (audit.record
  DEFAULT_LOG), NOT to `pumcore-receipts.jsonl` — verification must target the right
  file (checked and confirmed by grepping both).
- All commands above were executed in this session; outputs are in the RUNNING-LOG
  entry for the same date. Nothing in this doc is claimed without a measurement.

## 8. v1.1 hardening (2026-09-20, owner order "do it")

All three previously deferred items are now built and MEASURED:

1. **inotify fast path** (`_Inotify` in tools/forever_live.py, pure ctypes — no package
   install): watches the audit dir and the STOP dir; events wake the loop immediately
   with a 1s debounce; IN_Q_OVERFLOW drains and re-ticks. MEASURED: STOP created ->
   "paused" logged within 4s while the poll interval was 15s; STOP removed -> resumed
   within 4s. Falls back to plain polling if inotify is unavailable (logged).
2. **Independent supervision + dead-man's switch**:
   - The unit is now `Type=notify` with `WatchdogSec=90`; the watcher sends READY=1
     after its first scan and WATCHDOG=1 at least every 30s (chunked wait), so a hung
     watcher is killed and restarted by systemd itself. MEASURED: Type=notify,
     WatchdogUSec=1min 30s, active.
   - `pumdoctrine-live-check.timer` (every 5 min, separate process) runs
     `forever_live.py heartbeat-check`: if the watcher is enabled but its last check is
     older than max(3x interval, 120s) it logs + writes a `forever-live-stale` receipt
     (exit 2). MEASURED: fresh -> stale=False; simulated stale -> stale=True, exit 2.
   - Optional external dead-man's switch: if `the private state area` (0600)
     contains an https URL, the checker POSTs a heartbeat every 5 min. When the watcher
     dies the pings stop and the external service alerts. No URL configured -> check
     only, no network send (current state).
3. **Merkle-root anchoring** (`tools/merkle_anchor.py` + `pumdoctrine-anchor.timer`,
   daily): anchors a Merkle root over the whole audit chain into an append-only anchor
   log, HMAC'd with `the private state area` (auto-created 0600) and chained to
   the previous anchor; `verify` recomputes the root from the chain and detects any
   edit/delete/reorder. MEASURED on the real chain: chain_len 119,258, verify ok=True,
   problems=[]; tamper test (edited line) detected in tests. `print-root` emits the
   root + chain head for external publication.
   - Optional external anchor: if `the private state area` names a
     directory (USB / second host / network mount), the anchor log is copied there
     after every anchor.

### Honest limits (unchanged, stated plainly)

- Local-only anchoring cannot defeat an attacker who rewrites chain + anchors + key
  together; it makes tampering detectable under normal operation and gives the owner a
  root to publish externally. The export hook is the external step, and it needs the
  owner to provide the destination.
- The external dead-man's switch needs the owner to provide the URL; until then the
  5-minute checker is same-machine only (still independent of the watcher process).
- chattr +a on the anchor log is attempted best-effort; it needs root and is not a
  guarantee against a root-level actor. Documented, not claimed.

## 9. External witness wired to the second machine (2026-09-20, owner: "use the second machine" / "make a folder on it")

- the second machine (VPS, Tailscale the second machine, root): folder `/srv/pumdoctrine-anchors` created
  (mode 700; 375 GB free on /dev/nvme0n1p2).
- `the private state area` = `ssh://the owner's second machine/srv/pumdoctrine-anchors`.
  `merkle_anchor.py` exports via secure copy (credential read from the
  owner secret store, 0600, never printed) and locks the remote copy to 600.
- MEASURED: anchor run -> `exported: ssh://the owner's second machine/srv/pumdoctrine-anchors`;
  sha256 local == the second machine (`27254c6e8391c764552439f397d796a85d0336183b2ad77ef9939d783139ed45`),
  remote file 853 bytes root:root 600. The daily `pumdoctrine-anchor.timer` pushes
  automatically from now on.
- Effect: the witness copy now lives OUTSIDE this machine. Rewriting chain + anchors +
  key locally can no longer produce a consistent story — the second machine holds the independent copy.
- Still unwired: the external ALARM (dead-man notification) needs a channel. the second machine can
  host a back-checker (it would need SSH from the second machine to this host + an alert address such
  as email) — owner decision, not guessed.

## 10. Witness website on the second machine (2026-09-20, owner: "make a website for me to view")

- URL: http://the second machine:8088/ — bound to the Tailscale IP ONLY (not reachable from
  the LAN or public internet). Read-only static page.
- Served by `pumdoctrine-witness.service` on the second machine (python3 http.server, directory
  /srv/pumdoctrine-anchors, restarts on failure, enabled at boot).
- Generated by `tools/witness_site.py publish`: reads the anchor log + forever-live
  state, writes index.html, scp's it to the second machine. `pumdoctrine-anchor.service` now has
  `ExecStartPost=... witness_site.py publish`, so the page refreshes after every daily
  anchor automatically.
- Page shows: latest anchor (time, chain length, Merkle root, chain head), the
  forever-live watcher state, and the anchor history (last 20).
- MEASURED: service active; `curl http://the second machine:8088/` from the source machine
  returns the page (merkle root 7932bc69…); anchor service run anchored + refreshed.
- CORRECTION (fact-check loop): port 80 on the second machine is ALREADY taken by an existing Docker
  container (docker-proxy 0.0.0.0:80, HTTP 200) — my first port scan truncated output
  and missed it; the site uses 8088 tailnet-only and the existing container is
  untouched. Lesson: never truncate a port scan; read the full listener table.
