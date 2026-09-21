"""Poiseuille verification: substitute u(y)=G/(2nu) y(h-y) into the x-momentum eq."""
import math
G, nu, h = 1.0, 0.1, 1.0
def u(y): return G / (2 * nu) * y * (h - y)
n = 4000
dy = h / n
worst = 0.0
for i in range(1, n):
    y = i * dy
    upp = (u(y + dy) - 2 * u(y) + u(y - dy)) / (dy * dy)
    worst = max(worst, abs(nu * upp - (-G)))
print(f"Poiseuille: grid n={n} dy={dy:.2e} max |nu*u'' - (-G)| = {worst:.3e}")
print(f"no-slip: u(0)={u(0):.3e} u(h)={u(h):.3e}")
