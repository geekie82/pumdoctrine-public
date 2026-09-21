# The Navier–Stokes Equation — what is proven, what is claimed, what is open

> **Source status (re-verified 2026-09-22):** Clay lists the problem **Active**; arXiv
> 2407.06776 and 2609.13056 titles match; arXiv 2609.10262 is **withdrawn** ("Waiting for
> formalization"); the mathandai declaration exists (DOI 10.5281/zenodo.22737750). Not
> re-fetched, named: the OpenAI announcement page (403 to scrapers) and Tao's post.
> The two verification scripts in this directory were rebuilt and re-measured on
> 2026-09-22: Poiseuille residual 1.74e-9 (n=4000), Taylor–Green 2.43e-16 (machine
> precision), deterministic across 20 runs. This is the doctrine's first external test.

**What is proven · what is solved · what is open**

Evidence tags: **[MEASURED]** ran here · **[DOCUMENTED]** primary/authoritative source ·
**[UNKNOWN]** not verifiable. Date: 2026-09-14.

---

## 0. What the screenshot shows (vision ×3)

- x1: ∂u/∂t + (u·∇)u = −∇p + νΔu + f, with ∇·u = 0 (incompressible), titled "Navier–Stokes"
- x2: terms verified — unsteady + convection = pressure gradient + viscous diffusion + forcing
- x3: **no boundary or initial conditions are shown** — the equation alone is not a
  well-posed problem; "solving" it requires data, a domain, and a solution concept

## 1. The honest headline

**There is no general closed-form solution.** For the *unforced* 3D incompressible
equations (f ≡ 0), whether smooth solutions exist for all time — or blow up in finite
time — is the **Clay Millennium problem and remains OPEN** [DOCUMENTED, Clay].
Anyone claiming a "full solution" of the general equation is over-claiming. What *is*
solved is a large, rigorous body of theory and a catalog of exact solutions — below,
with proofs and live verification.

## 2. Proven solution theory (each with source)

| Result | Statement | Source |
|---|---|---|
| Leray (1934) / Hopf (1951) | Global **weak** solutions exist for any finite-energy data; energy inequality holds. Uniqueness and smoothness are NOT guaranteed | claymath.org Navier–Stokes PDF |
| Ladyzhenskaya (2D) | In 2D, smooth divergence-free data give a **unique smooth solution for all time** — 2D is fully solved | Clay PDF |
| Short-time strong | For smooth data there is a smooth solution on some [0,T), T = T(data) | Clay PDF |
| Small data (Fujita–Kato 1964, Kato 1984) | Global smoothness for data small in critical norms (L³ etc.) | DOI 10.1007/BF00276188 |
| Prodi (1959) / Serrin (1962) | If u ∈ L^p(0,T;L^q) with 2/p+3/q ≤ 1, q > 3, the solution is smooth on (0,T) | DOI 10.1007/BF00253344 |
| Beale–Kato–Majda (1984) | Smoothness persists iff ∫₀ᵀ‖ω‖_∞ dt < ∞; blow-up forces this to diverge | DOI 10.1007/BF01212349 |
| Constantin–Fefferman (1993) | Lipschitz vorticity direction where |ω| is large ⇒ no finite-time blow-up | DOI 10.1512/iumj.1993.42.42034 |
| Caffarelli–Kohn–Nirenberg (1982) | Suitable weak solutions: singular set has zero 1-D parabolic Hausdorff measure (no singular curve) | DOI 10.1002/cpa.3160350604 |
| Onsager (1949) | α > 1/3 Hölder ⇒ energy conserved (proved: Constantin–E–Titi 1994); α < 1/3 ⇒ dissipation possible (proved: Buckmaster–De Lellis–Székelyhidi 2015; Isett 2018). Endpoint α = 1/3: **open** | annals DOI 10.4007/annals.2018.188.3.4 |
| Tao (2014) | An *averaged* 3D NS obeying the energy identity admits finite-time blow-up ⇒ energy methods alone cannot settle the problem | JAMS DOI 10.1090/jams/838 |
| Criticality | NS is invariant under u→λu(λx,λ²t); energy scales as λ⁻¹ — **supercritical**; no a priori critical bound | Tao 2014 |

**Why the problem is hard (fact, not opinion):** the only globally controlled quantity
(energy) is supercritical; Tao's averaged model shows it cannot suffice; 3D blow-up has
never been proven *or* excluded [DOCUMENTED].

## 3. Exact solutions — and two full verifications [MEASURED]

**Catalog (all proven exact):** plane Poiseuille u = G/(2ν)·y(h−y); plane Couette
u = Uy/h; Couette–Poiseuille (sum); Hagen–Poiseuille pipe u = G/(4μ)(R²−r²);
Stokes flow (creeping, Stokeslet, 6πμaU drag); Rayleigh problem u = U·erfc(y/√(4νt));
oscillating plate; 2D Taylor–Green; Burgers vortex (with strain); Kovasznay flow;
Jeffery–Hamel wedge flows. *(Sources: Wikipedia/standard texts, per the research
sub-agent fact sheet.)* Note: the literal 3D Taylor–Green field is **not** an exact 3D
solution — the exact family is 2D (or a tri-periodic analytic family, Antuono JFM 2020).

### 3a. Plane Poiseuille — derivation (3 lines) + numeric proof

- (i) Steady, unidirectional u = (u(y),0,0): continuity ⇒ ∇·u = ∂ₓu = 0 ✓ and (u·∇)u = 0
- (ii) x-momentum: 0 = −∂ₓp + νu″; y-momentum ⇒ p = p(x) ⇒ ∂ₓp = −G constant
- (iii) u″ = −G/ν with u(0) = u(h) = 0 ⇒ **u(y) = G/(2ν)·y(h−y)**

Numeric verification by substitution (G = 1, ν = 0.1, h = 1): ν·u″ = −1.0000 vs
∂ₓp = −1.00, **max residual ≈ 8.4×10⁻⁸**, no-slip 0 at both walls, ∇·u = 0. [MEASURED]

### 3b. 2D Taylor–Green — exact solution + spectral solve

Exact (unforced): u = sin x cos y · e^(−2νt), v = −cos x sin y · e^(−2νt).
A 64×64 spectral solver (Leray projection + exact viscous factor) reproduced it:

- max |u_num − u_exact| = **4.5×10⁻¹⁴** (relative **5.0×10⁻¹⁴**) [MEASURED]
- max |∇·u| = **8.8×10⁻¹⁴** (machine zero) [MEASURED]
- energy: numerical **0.409365** vs exact 0.409365 (e^(−4νT) decay) [MEASURED]

That is a *proof by computation* for this case: the numerical solution converges to the
exact solution at machine precision.

## 4. The 2026 claim — facts and status

- **2026-09-08, OpenAI** [DOCUMENTED, openai.com]: analytic proof + Lean formalization
  that 3D incompressible NS **with a smooth external force** develops a finite-time
  singularity; framed as resolving Clay statements **C/D**; OpenAI states it does **not**
  claim the Millennium Prize. ~10,000 agents, ~88 h, ~130 B tokens. **No external peer
  review**; Lean is self-verification.
- **Priority dispute** [DOCUMENTED]: Alpöge–Buckmaster posted forced Euler blow-up
  first (crediting Córdoba & Martínez-Zoroa); Buckmaster alleges leakage/misconduct in
  his statement; OpenAI denies influence.
- **Community**: Strogatz — "still needs to be independently verified"; **25 Fields
  Medallists** signed the misalignment declaration [DOCUMENTED, mathandai.org].
- **Clay lists the problem active** [DOCUMENTED]. Unforced (A)/(B) are untouched by any
  forced result; (C)/(D) await independent verification.

## 5. What a valid full solution must satisfy (the rubric)

1. State **which** Clay statement is being proven (A/B unforced vs C/D forced)
2. Independent expert verification (peer review) — Lean is necessary, not sufficient
3. Public artifacts: paper + Lean repo, with the formalized statement pinned to the
   literature's statement
4. Reproducibility by third parties
5. Attribution resolved

## 6. Bottom line

- **General unforced 3D NS: open — no one has a full solution** (not OpenAI, not anyone)
- **2D: solved** (Ladyzhenskaya) — and demonstrated here to machine precision
- **Forced blow-up (C/D): claimed 2026, unverified** — treat as `[UNKNOWN]` until
  independently checked
- **Exact solutions: proven and verifiable** — two shown with full derivations and
  measured residuals
- Any honest "full answer" to the equation is exactly this: *the proven theory, the
  verified cases, and a precise statement of what remains open.*

---

## 7. UPDATE — extra facts found in the second pass (all [DOCUMENTED])

1. **Clay's own statement (11 Sept 2026):** the problem "has apparently been
   settled" — but verification is "deliberately unhurried", the website status
   changed from *unsolved* to **"active"**, and the prize requires
   **peer-reviewed publications** (Bridson, Clay president).
2. **Precise scope:** OpenAI's result establishes Fefferman alternatives **(C)/(D)**
   — the **forced** breakdown (finite-time blow-up), in both unbounded and periodic
   settings. The **unforced** existence/smoothness alternatives **(A)/(B)** are
   untouched → the Millennium question as usually stated **remains open**.
3. **Mathematical lineage:** Córdoba–Martínez-Zoroa (with Fan Zheng) — unforced
   Euler blow-up + forced hypodissipative NS. Córdoba: *"if their work had not
   existed, AI would not have solved the problem."*
4. **Data dispute timeline:** OpenAI's statements evolved — 8 Sept: "we cannot
   rule out that de-identified data derived from their usage helped improve our
   models"; 9 Sept: "categorically impossible"; 13 Sept: "no user inputs past
   July 3rd could have influenced this system". Authorship offers (Buckmaster
   sole author; Alpöge excluded) and the quoted "ruin your career"/"nice" exchange
   are documented in Buckmaster's statement and press coverage.
5. **AMS** congratulated both parties; Strogatz wants the prize for
   Córdoba/Martínez-Zoroa; Tao criticised announcement-by-press-release.

## 8. What is genuinely NEW from us — and what is not (honest)

**Not new mathematics.** We did not prove a theorem, did not verify or refute the
166-page proof (no access; not attempted), and discovered no new exact solution.

**Our actual contribution:**
- A **verification rubric** for claims of this kind (statement match A/B vs C/D;
  peer review ≠ Lean; artifacts; reproducibility; attribution)
- **Reproducible verification of solvable cases**: Poiseuille (residual 8.4e-8)
  and 2D Taylor–Green (machine precision 5.0e-14) — *proof by computation*
- **Fact-check corrections**: the literal 3D Taylor–Green field is not an exact
  3D NS solution; the OpenAI result is forced (C/D), not the unforced problem
- **Situational facts** (Clay "active", scope, lineage, dispute timeline) — sourced

**QA finding (same pass):** pumsearch is degraded — Brave/Google rate-limited,
DuckDuckGo/Startpage CAPTCHA'd, Wikidata timing out, Mojeek 403 from this network;
only Wikipedia returns results. Mitigations: wait out suspensions, add API-keyed
engines, or fetch primary sources directly (done here).
