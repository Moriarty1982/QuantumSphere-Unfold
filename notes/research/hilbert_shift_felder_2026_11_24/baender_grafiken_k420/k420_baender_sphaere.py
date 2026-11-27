#!/usr/bin/env python3
"""Fünf Bänder (HS-Stufen R, C, H, O, S) als Großkreise auf der Sphäre, Lagen aus der Minimierung von H192 (k400).

Aufruf:  python k420_baender_sphaere.py [--lang de|en] [--out ORDNER]
Die Lagen werden neu gerechnet (dasselbe Modell wie k400: E = sum w_i w_j / sin^s theta_ij), nichts wird eingegeben.
"""
import argparse, itertools, math, pathlib
import numpy as np
from scipy.optimize import minimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

NAMES = ["R", "C", "H", "O", "S"]
SYM = [r"$\mathbb{R}$", r"$\mathbb{C}$", r"$\mathbb{H}$", r"$\mathbb{O}$", r"$\mathbb{S}$"]
DIM = np.array([1.0, 2, 4, 8, 16])
COL = ["#6b6b6b", "#2e7d32", "#c98a00", "#b3261e", "#1f4e9c"]
INK, SOFT = "#222222", "#9aa0a6"
VARIANTS = [("dim", 1), ("dim", 2), ("sqrt", 1), ("sqrt", 2)]

def unit(x):
    v = x.reshape(-1, 3); return v / np.linalg.norm(v, axis=1, keepdims=True)
def energy(x, w, s):
    v = unit(x); e = 0.0
    for i, j in itertools.combinations(range(len(v)), 2):
        c = abs(np.clip(v[i] @ v[j], -1, 1)); e += w[i] * w[j] / max(math.sqrt(1 - c * c), 1e-9) ** s
    return e
def solve(w, s, rng, tries=300):
    best = None
    for _ in range(tries):
        r = minimize(energy, rng.standard_normal(15), args=(w, s), method="BFGS", options={"maxiter": 500})
        if best is None or r.fun < best.fun - 1e-9: best = r
    return unit(best.x)
def angles(v):
    return np.degrees(np.arccos(np.clip(np.abs(v @ v.T), 0, 1)))
def align(v):
    """S-Normale nach z, O-Normale in die xz-Ebene, Spiegelung so, dass die H-Normale y > 0 hat."""
    ez = v[4]; ex = v[3] - (v[3] @ ez) * ez; ex /= np.linalg.norm(ex); ey = np.cross(ez, ex)
    u = v @ np.array([ex, ey, ez]).T
    u = u * np.where(u[:, 2:3] < 0, -1, 1)
    if u[2, 1] < 0: u[:, 1] *= -1
    return u

TXT = {
 "de": dict(title="Fünf Bänder auf der Sphäre: die Stufen des HS-Turms (H192, k400)",
   sub=r"Lage aus der Minimierung von $E=\sum_{i<j} w_i w_j/\sin\theta_{ij}$, Gewicht $w$ = Dimension. Kein Winkel eingegeben.",
   robust="robust: bleibt bei allen vier Setzungen", gesetzt="läuft mit der Setzung (Gewicht, Gesetz)",
   ghost="dünne Linien: dieselben Bänder bei den drei anderen Setzungen",
   right="Winkel zwischen je zwei Bändern", xl="Winkel in Grad",
   leg_main="Gewicht = Dimension, 1/sin (gezeichnet)", leg_span="Spanne über vier Setzungen",
   okt="Oktant 90°", pre="vorab benannt", width="Bandbreite ~ log₂ Dimension (nur Darstellung)",
   foot=("Modell gesetzt: starre Großkreise auf einer gemeinsamen S², Gewicht 1, 2, 4, 8, 16, Abstoßung 1/sin. "
         "\nHergeleitet: 𝕆 senkrecht zu 𝕊 (87,9° bis 89,5°). Angepasst: die kleinen Winkel, z. B. ℂ–ℍ 49° bis 59°."),
   setz=["dim, 1/sin", "dim, 1/sin²", "√dim, 1/sin", "√dim, 1/sin²"], dimlab="Dim."),
 "en": dict(title="Five bands on the sphere: the levels of the HS tower (H192, k400)",
   sub=r"Positions from minimising $E=\sum_{i<j} w_i w_j/\sin\theta_{ij}$, weight $w$ = dimension. No angle put in.",
   robust="robust: holds for all four settings", gesetzt="moves with the setting (weight, law)",
   ghost="thin lines: the same bands for the three other settings",
   right="Angle between each pair of bands", xl="angle in degrees",
   leg_main="weight = dimension, 1/sin (drawn)", leg_span="range over four settings",
   okt="octant 90°", pre="named in advance", width="band width ~ log₂ dimension (display only)",
   foot=("Model set by hand: rigid great circles on one common S², weights 1, 2, 4, 8, 16, repulsion 1/sin. "
         "\nDerived: 𝕆 perpendicular to 𝕊 (87.9° to 89.5°). Fitted: the small angles, e.g. ℂ–ℍ 49° to 59°."),
   setz=["dim, 1/sin", "dim, 1/sin²", "√dim, 1/sin", "√dim, 1/sin²"], dimlab="dim"),
}

def view_basis(elev, azim):
    e, a = np.radians(elev), np.radians(azim)
    d = np.array([np.cos(e) * np.cos(a), np.cos(e) * np.sin(a), np.sin(e)])   # zum Betrachter
    r = np.array([-np.sin(a), np.cos(a), 0.0]); up = np.cross(d, r)
    return r, up, d
def circle_pts(n, off=0.0, m=721):
    a = np.cross(n, [0, 0, 1.0]);
    if np.linalg.norm(a) < 1e-6: a = np.array([1.0, 0, 0])
    a /= np.linalg.norm(a); b = np.cross(n, a); t = np.linspace(0, 2 * np.pi, m)
    return math.cos(off) * (np.outer(np.cos(t), a) + np.outer(np.sin(t), b)) + math.sin(off) * n
def draw_band(ax, n, hw, col, B, z0):
    r, up, d = B
    p1, p2 = circle_pts(n, hw), circle_pts(n, -hw)
    for k in range(len(p1) - 1):
        quad = np.array([p1[k], p1[k + 1], p2[k + 1], p2[k]]); front = (quad @ d).mean() > 0
        xy = np.c_[quad @ r, quad @ up]
        ax.add_patch(Polygon(xy, closed=True, fc=col, ec="none", antialiased=False, alpha=0.95 if front else 0.18, zorder=z0 + (3 if front else 0), rasterized=True))
def draw_line(ax, n, col, B, lw=0.8, alpha=0.7):
    r, up, d = B; p = circle_pts(n)
    f = (p @ d) > 0; x, y = p @ r, p @ up
    ax.plot(np.where(f, x, np.nan), np.where(f, y, np.nan), color=col, lw=lw, alpha=alpha, zorder=6)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lang", default="de"); ap.add_argument("--out", default=".")
    a = ap.parse_args(); T = TXT[a.lang]; out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(11); sols = {}
    for wl, s in VARIANTS:
        v = align(solve(DIM if wl == "dim" else np.sqrt(DIM), s, rng)); sols[(wl, s)] = v
        M = angles(v); print(f"{wl:5s} 1/sin^{s}: " + "  ".join(f"{NAMES[i]}{NAMES[j]} {M[i,j]:.2f}" for i, j in itertools.combinations(range(5), 2)))
    main_v = sols[("dim", 1)]; Ms = np.array([angles(v) for v in sols.values()])

    fig = plt.figure(figsize=(15, 8.6)); fig.patch.set_facecolor("white")
    ax = fig.add_axes([0.01, 0.09, 0.56, 0.79]); ax.set_aspect("equal"); ax.axis("off")
    B = view_basis(22, 38)
    ax.add_patch(Circle((0, 0), 1, fc="#eef1f5", ec=INK, lw=1.6, zorder=1))
    for (wl, s), v in sols.items():
        if (wl, s) == ("dim", 1): continue
        for i in range(5): draw_line(ax, v[i], COL[i], B, lw=0.9, alpha=0.55)
    hw = np.radians(1.2 + 0.75 * np.log2(DIM))
    for i in np.argsort(-DIM):
        draw_band(ax, main_v[i], hw[i], COL[i], B, z0=2)
    # Beschriftung der Bänder: Punkt auf dem Band, der am weitesten außen vorn liegt
    r, up, d = B
    lab = {0: (-1.30, 0.62), 1: (-1.32, 0.25), 2: (-1.30, -0.62), 3: (1.18, 0.86), 4: (1.20, -0.42)}
    for i in range(5):
        p = circle_pts(main_v[i]); f = (p @ d) > 0.25; q = p[f]; xy = np.c_[q @ r, q @ up]
        k = np.argmin(np.hypot(xy[:, 0] - lab[i][0], xy[:, 1] - lab[i][1]))
        ax.annotate(f"{SYM[i]}  {T['dimlab']} {int(DIM[i])}", xy=xy[k], xytext=lab[i], color=COL[i], fontsize=17, fontweight="bold",
                    ha="center", va="center", arrowprops=dict(arrowstyle="-", color=COL[i], lw=1.2), zorder=20)
    ax.set_xlim(-1.6, 1.5); ax.set_ylim(-1.22, 1.12)
    ax.text(-1.58, -1.02, T["ghost"] + "\n" + T["width"], fontsize=10.5, color=INK, va="top")

    # rechte Tafel: Winkel je Paar mit Spanne
    bx = fig.add_axes([0.63, 0.27, 0.35, 0.57])
    pairs = list(itertools.combinations(range(5), 2)); order = sorted(pairs, key=lambda p: -Ms[0][p])
    for y, (i, j) in enumerate(order[::-1]):
        vals = Ms[:, i, j]; rob = vals.max() - vals.min() < 3
        bx.plot([vals.min(), vals.max()], [y, y], color=INK if rob else "#b3261e", lw=7, alpha=0.30, solid_capstyle="round")
        bx.plot(vals[1:], [y] * 3, "|", color=INK, ms=9, mew=1.0, alpha=0.7)
        bx.plot(vals[0], y, "o", color=INK, ms=7, zorder=5)
        pre = "  ◄ " + T["pre"] if {NAMES[i], NAMES[j]} in ({"O", "S"}, {"C", "H"}) else ""
        bx.text(vals.max() + 1.2, y, f"{vals[0]:.1f}°".replace(".", "," if a.lang == "de" else ".") + pre, va="center", fontsize=10, color=INK)
        bx.text(27.5, y, SYM[i], color=COL[i], fontsize=15, ha="right", va="center"); bx.text(28.3, y, "–", ha="center", va="center", fontsize=11)
        bx.text(29.2, y, SYM[j], color=COL[j], fontsize=15, ha="left", va="center")
    bx.axvline(90, color=SOFT, lw=1, ls=":"); bx.text(90, 9.75, T["okt"], ha="center", va="bottom", fontsize=9.5, color=INK)
    bx.set_xlim(32, 118); bx.set_ylim(-0.7, 10.2); bx.set_yticks([]); bx.set_xticks([40, 50, 60, 70, 80, 90])
    for sp in ("left", "right", "top"): bx.spines[sp].set_visible(False)
    bx.set_xlabel(T["xl"], fontsize=11); bx.set_title(T["right"], fontsize=13, fontweight="bold", loc="left", pad=18)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], marker="o", color=INK, ls="", ms=7, label=T["leg_main"]),
         Line2D([], [], marker="|", color=INK, ls="", ms=9, label=", ".join(T["setz"][1:])),
         Line2D([], [], color=INK, lw=7, alpha=0.30, label=T["robust"] + " (< 3°)"),
         Line2D([], [], color="#b3261e", lw=7, alpha=0.30, label=T["gesetzt"])]
    bx.legend(handles=h, loc="upper center", bbox_to_anchor=(0.42, -0.13), fontsize=9.5, frameon=False, ncol=1)
    fig.text(0.02, 0.955, T["title"], fontsize=19, fontweight="bold", color="black")
    fig.text(0.02, 0.915, T["sub"], fontsize=12, color=INK)
    fig.text(0.02, 0.018, T["foot"], fontsize=10, color=INK)
    for ext in ("png", "pdf"):
        fig.savefig(out / f"baender_sphaere_{a.lang}.{ext}", dpi=170)
    print("geschrieben:", out / f"baender_sphaere_{a.lang}.png")
if __name__ == "__main__":
    main()
