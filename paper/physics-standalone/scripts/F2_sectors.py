"""F2: sectors of the field invariant s = (E+iB).(E+iB) on the real slice E.B = 0.

Schematic 3D picture for Section 2 of the physics article.  Coordinates: E in the
horizontal plane (E_x, E_y), B along the vertical axis, so E.B = 0 and
s = |E|^2 - |B|^2 is real.  Drawn:
  * the null cone s = 0 (light-like fields, plus the zero field at the apex),
  * the one-sheet hyperboloid s = +c (electric dominance; working name: matter),
  * the two-sheet hyperboloid s = -c (magnetic dominance; working name: tachyon).
Level sets of s are the SO(3,C) orbits (v4.8.0-r06.3) restricted to this slice.
No data enter; c = 1 is a display choice.
Usage: python3 scripts/F2_sectors.py [output.pdf]   (default figures/F2-sectors.pdf)
"""
import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

here = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]) if len(sys.argv) > 1 else here / "figures" / "F2-sectors.pdf"

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 10})
fig = plt.figure(figsize=(6.4, 4.6))
ax = fig.add_subplot(111, projection="3d")
ax.set_proj_type("persp", focal_length=0.35)
ax.view_init(elev=16, azim=-58)

H = 2.0
phi = np.linspace(0, 2 * np.pi, 73)

# null cone |B| = |E|
t = np.linspace(-H, H, 41)
P, T = np.meshgrid(phi, t)
ax.plot_surface(np.abs(T) * np.cos(P), np.abs(T) * np.sin(P), T,
                color="0.80", alpha=0.35, linewidth=0, shade=False, zorder=1)
for tt in (-H, H):
    ax.plot(abs(tt) * np.cos(phi), abs(tt) * np.sin(phi), tt, color="0.35", lw=0.8)

# s = +1: one-sheet hyperboloid  x^2+y^2 = 1 + z^2   (electric dominance)
z = np.linspace(-1.7, 1.7, 31)
Pz, Z = np.meshgrid(phi, z)
r = np.sqrt(1 + Z ** 2)
ax.plot_wireframe(r * np.cos(Pz), r * np.sin(Pz), Z, rstride=5, cstride=6,
                  color="#1f3f7a", lw=0.6)

# s = -1: two-sheet hyperboloid  z^2 = 1 + x^2 + y^2   (magnetic dominance)
rr = np.linspace(0, 1.3, 14)
Pr, Rr = np.meshgrid(phi, rr)
for sgn in (1, -1):
    ax.plot_wireframe(Rr * np.cos(Pr), Rr * np.sin(Pr), sgn * np.sqrt(1 + Rr ** 2),
                      rstride=3, cstride=6, color="#9a3030", lw=0.6, linestyle="--")

# apex: the zero field
ax.scatter([0], [0], [0], color="k", s=12, depthshade=False)

# axes
L = 2.6
for v, lab in (((L, 0, 0), r"$E_x$"), ((0, L, 0), r"$E_y$"), ((0, 0, L), r"$B$")):
    ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color="k", lw=0.7)
    ax.text(*(1.06 * np.array(v)), lab)

fig.text(0.74, 0.30, r"$s>0$" "\nelectric dominance\n(working name: matter)", color="#1f3f7a", fontsize=9)
fig.text(0.02, 0.86, r"$s<0$" "\nmagnetic dominance\n(working name: tachyon)", color="#9a3030", fontsize=9)
fig.text(0.74, 0.80, r"$s=0$" "\nnull cone\n(light-like fields)", color="0.25", fontsize=9)

ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2); ax.set_zlim(-2.2, 2.2)
ax.set_box_aspect((1, 1, 1))
ax.set_axis_off()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, bbox_inches="tight", pad_inches=0.05)
print("wrote", out)
