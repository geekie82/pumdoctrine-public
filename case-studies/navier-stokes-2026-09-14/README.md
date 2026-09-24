# Case study — the method, used on someone else's claim (2026-09-14, re-verified 2026-09-22)

An early external test of the doctrine: a 2026 announcement about the Navier–Stokes Millennium
problem, audited with the same method used on our own system.

- `ANSWER.md` — what is proven, what is claimed, what is open; evidence tags throughout;
  the full corrections log from the fact-check pass.
- `verify_poiseuille.py` — exact unforced solution, numeric substitution check
  (residual 1.74e-9 at n=4000; finite-difference accuracy) [M 2026-09-22].
- `verify_taylor_green.py` — 2D Taylor–Green, analytic-derivative check
  (residual 2.43e-16; machine precision; divergence exactly 0).

Both scripts are deterministic (20 repeat runs, byte-identical). Re-run them yourself:
`python3 verify_poiseuille.py` and `python3 verify_taylor_green.py`.

Honest scope: this directory does not prove or refute the claimed 2026 result. It verifies
what is verifiable, labels what is not, and publishes its own corrections.
