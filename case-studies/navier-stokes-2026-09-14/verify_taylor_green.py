"""Taylor-Green 2D verification with analytic derivatives (machine-precision check)."""
import math
nu, t = 0.1, 0.3
E = math.exp(-2 * nu * t)
E4 = math.exp(-4 * nu * t)
def U(x, y): return math.sin(x) * math.cos(y) * E
def V(x, y): return -math.cos(x) * math.sin(y) * E
worst = 0.0
worst_div = 0.0
N = 64
for i in range(N):
    for j in range(N):
        x = (i + 0.5) * 2 * math.pi / N
        y = (j + 0.5) * 2 * math.pi / N
        ut, vt = -2 * nu * U(x, y), -2 * nu * V(x, y)
        ux = math.cos(x) * math.cos(y) * E
        uy = -math.sin(x) * math.sin(y) * E
        vx = math.sin(x) * math.sin(y) * E
        vy = -math.cos(x) * math.cos(y) * E
        uxx = uyy = -U(x, y)
        vxx = vyy = -V(x, y)
        px = -math.sin(2 * x) / 2 * E4
        py = -math.sin(2 * y) / 2 * E4
        r1 = ut + U(x, y) * ux + V(x, y) * uy + px - nu * (uxx + uyy)
        r2 = vt + U(x, y) * vx + V(x, y) * vy + py - nu * (vxx + vyy)
        worst = max(worst, abs(r1), abs(r2))
        worst_div = max(worst_div, abs(ux + vy))
print(f"Taylor-Green: N={N} max |NS residual| = {worst:.3e}")
print(f"max |div u| = {worst_div:.3e}")
