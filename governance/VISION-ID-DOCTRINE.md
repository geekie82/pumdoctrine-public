# VISION ID DOCTRINE

Date: 2026-09-20. Status: ACTIVE. Tags: MEASURED / DOCUMENTED / UNKNOWN per realm doctrine.
Tool: `pumoffice/tools/vision_id.py`. Research: `docs/agent/FACE-SECURITY-RESEARCH.md`
(10 loops, 42 fetched sources). Related: `docs/FOREVER-LIVE-DOCTRINE.md`.

## 1. Purpose and policy

Forgey may recognize people at the camera on owner order. Policy (owner directive
2026-09-18): only the owner and one authorized family member; anyone else -> "unknown"
and refuse. Refs live in `the private face-template directory` (0700, files 0600). Biometric
templates are on-device only, never sent anywhere, deletable with one command
(delete the ref files). No personal details are logged. Backups of previous templates
are kept locally (`refs.bak-<ts>`, 0700) and can be removed on request.

## 2. Cameras (measured 2026-09-20)

- a 720p webcam (`046d:0825`): RGB-only, YUYV/MJPG, max 1280x960 via our open path.
- a 1080p webcam HD Pro (`046d:0892`): RGB-only, YUYV/MJPG, **1920x1080** via our open
  path. This is the preferred camera.
- **Neither has IR or depth** (formats and USB interfaces measured). They are spoofable
  by a photo/video; the Windows Hello IR camera is the planned liveness upgrade.
- Device numbers MOVE on USB re-enumeration (measured: a 720p webcam went video0 -> video4,
  then back to video0 after the a 1080p webcam was plugged in). Never hardcode an index.

## 3. Camera selection and quality rules

- `_auto_cam()` probes every `/dev/video*`, opens each at the best resolution it
  actually delivers, and picks the **highest pixel count** (measured pick: cam 2, the
  a 1080p webcam at 1920x1080 — not the first index).
- `_open()` asks for 1080p then 720p (the a 1080p webcam otherwise defaults to 640x480).
- `_frame()` skips auto-exposure warmup frames (measured: the a 1080p webcam's first frame is
  near-black, gray mean 13.6 — a face "detected" on it is garbage).
- Enrollment quality gate: YuNet score >= 0.8 AND face box >= 4000 px. Weak frames
  never become templates.
- `_embed()` tries the full frame, then a 960px-wide resize (1080p full-frame made
  YuNet miss faces). YuNet score threshold 0.5; identify ignores detections below 0.7.
- Matching: SFace cosine, threshold 0.363 (OpenCV same-identity). Histogram fallback
  (threshold 0.6) only when no SFace ref/probe exists.

## 4. Commands

- `vision_id.py cams` — enumerate cameras and which deliver frames.
- `vision_id.py id [wait:N]` — identify (best camera; multi-frame sampling).
- `vision_id.py enroll-now <name> [wait:N]` — live enrollment, quality-gated.
- `vision_id.py both [wait:N]` — **two-view check**: the same enrolled person must
  match in BOTH working cameras at once; min-confidence fusion (weaker view decides).
- Console phrases: "who is this" / "do you see me" -> `id`; "learn my face" /
  "enroll me" -> live enrollment; "check both cameras" -> `both`.

## 5. Verified evidence (MEASURED 2026-09-20)

- SFace pipeline self-match 1.0 (OpenCV test face; artifact deleted).
- Owner enrolled live on a 720p webcam (yunet+sface) -> id 0.763 sface.
- a 1080p webcam swap: dark-first-frame bug found (garbage template 0.303) -> quality gate added
  -> re-enroll yunet+sface -> id owner 0.52-0.57 sface across runs.
- Two-view: `both` -> confirmed owner, a 720p webcam 0.521 / a 1080p webcam 0.566, min 0.521; console
  "check both cameras" -> confirmed/owner/0.51 reported as measured output.
- Camera preference fix: auto-pick = cam 2 (a 1080p webcam), `_open` delivers 1920x1080
  (a 720p webcam 1280x960); id -> source cam:2, owner 0.531.

## 6. Honest limits

- **No liveness detection**: a photo/video held to the lens can pass. RGB-only cameras
  cannot fix this; IR/depth (Windows Hello class) is the real upgrade.
- Two RGB views close together see nearly the same scene; a large angled photo could
  satisfy both. Two-view is a presence factor, not a silver bullet.
- SFace confidence varies with light/pose (0.5-0.8 typical here); thresholds are tuned
  for this machine and are not transferable.
- A false "unknown" is the safe failure; never guess a person.
- No anti-spoof benchmark (impostor/photo baseline) has been run yet — that is the
  next honest step before treating face ID as a security gate.
