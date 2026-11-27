#!/usr/bin/env python3
"""k422 (Erkundung, nicht blind): Was passiert, wenn die fünf Bänder nicht gleich lang sind?

Aufruf:  python k422_baender_ungleich_lang.py [--lang de|en] [--out ORDNER] > k422_out.txt
Setzung: Länge des Bands der Stufe mit Dimension d ist 2 pi d/16 (R, C, H, O, S: 1/16, 1/8, 1/4, 1/2, 1 des Großkreises).
Teil 1: Kleinkreise müssen sich nicht kreuzen (Überlappenergie 0). Teil 2: Lesart "gleich lang, aber wiederholt" (Windungszahl 16/d).
Teil 3: Formen, auf denen jedes Band wieder ein längster Kreis ist (Stufen, Perlenkette), Zeichnung.
"""
import argparse, itertools, math, pathlib, sys
import numpy as np
from scipy.optimize import minimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.colors import to_rgb

NAMES = ["R", "C", "H", "O", "S"]; DIM = np.array([1.0, 2, 4, 8, 16])
SYM = [r"$\mathbb{R}$", r"$\mathbb{C}$", r"$\mathbb{H}$", r"$\mathbb{O}$", r"$\mathbb{S}$"]
COL = ["#6b6b6b", "#2e7d32", "#c98a00", "#b3261e", "#1f4e9c"]; INK = "#222222"
R = DIM / 16; TH = np.arcsin(R)                      # Radius des Kleinkreises, Polwinkel
P = list(itertools.combinations(range(5), 2))

def part1():
    print("== Teil 1: Baender als Kleinkreise der Laenge 2 pi d/16 auf der runden Sphaere ==")
    for i in range(5):
        print(f"   {NAMES[i]}: Laenge/Grosskreis = {R[i]:.4f}, Polwinkel {math.degrees(TH[i]):6.2f} Grad, Neigung der Flaeche dort cos = {math.cos(TH[i]):.4f}")
    # zwei Kreise (Achsen n_i, n_j, Winkelradien th_i, th_j) kreuzen sich genau dann, wenn |th_i - th_j| < gamma < th_i + th_j
    # (gamma = Winkel der Achsen). Zahl der erzwungenen Kreuzungen = Minimum ueber die Lagen.
    rng = np.random.default_rng(422)
    def crossings(v):
        n = 0
        for i, j in P:
            g = math.acos(np.clip(v[i] @ v[j], -1, 1))
            if abs(TH[i] - TH[j]) < g < min(TH[i] + TH[j], 2 * math.pi - TH[i] - TH[j]): n += 1
        return n
    best = 99; cnt0 = 0; N = 20000
    for _ in range(N):
        v = rng.standard_normal((5, 3)); v /= np.linalg.norm(v, axis=1, keepdims=True); c = crossings(v); best = min(best, c); cnt0 += (c == 0)
    print(f"   Zufallslagen: kleinste Zahl sich kreuzender Paare = {best}; Anteil ganz kreuzungsfreier Lagen = {cnt0/N:.4f}")
    v = np.tile(np.array([0, 0, 1.0]), (5, 1)); print(f"   koaxiale Lage (alle Achsen gleich): kreuzende Paare = {crossings(v)}")
    print("   Folge: Die Ueberlappenergie (H209) hat ihr Minimum 0 auf einer ganzen Schar von Lagen; kein Winkel zwischen den Baendern ist festgelegt.")
    print("   Nur Grosskreise kreuzen einander zwingend. Bei Laengen ~ Dimension ist S der einzige Grosskreis.")

def part2():
    print("\n== Teil 2: Lesart 'gleich lang, aber wiederholt' (alle Baender Grosskreise, Windungszahl m = 16/d) ==")
    m = 16 / DIM; rng = np.random.default_rng(11)
    def energy(x, w):
        u = x.reshape(-1, 3); u = u / np.linalg.norm(u, axis=1, keepdims=True); e = 0.0
        for i, j in P:
            c = abs(np.clip(u[i] @ u[j], -1, 1)); e += w[i] * w[j] / max(math.sqrt(1 - c * c), 1e-9)
        return e
    best = None
    for _ in range(400):
        r = minimize(energy, rng.standard_normal(15), args=(m,), method="BFGS", options={"maxiter": 600})
        if best is None or r.fun < best.fun - 1e-9: best = r
    u = best.x.reshape(-1, 3); u /= np.linalg.norm(u, axis=1, keepdims=True); M = np.degrees(np.arccos(np.clip(np.abs(u @ u.T), 0, 1)))
    print(f"   Gewicht = Windungszahl {m.astype(int).tolist()}, Gesetz 1/sin, Energie {best.fun:.4f} (H192 mit Gewicht = Dimension: 322.1532)")
    print("   " + "  ".join(f"{NAMES[i]}{NAMES[j]} {M[i,j]:.2f}" for i, j in P))
    print(f"   Die Rollen sind gespiegelt: R-C = {M[0,1]:.2f} (in H192 war O-S = 89.54), O-S = {M[3,4]:.2f} (in H192 war R-C = 35.59).")

def part3_numbers():
    print("\n== Teil 3: Formen, auf denen jedes Band ein laengster Kreis ist (Rotationsflaeche, Baender koaxial) ==")
    print("   Ein Breitenkreis ist genau dann geschlossene Geodaete, wenn der Abstand rho von der Achse dort stationaer ist (Clairaut); 'laengster' heisst rho maximal.")
    print("   (a) Stufen: kleinster Eingriff, an jedem Band wird die Neigung cos(theta_i) auf 0 gebracht; Hoehe der Stufe frei.")
    print("   (b) Perlenkette: jedes Band ist Aequator einer eigenen Kugel mit Radius d/16.")
    area = (R ** 2).sum(); vol = (R ** 3).sum(); height = 2 * R.sum()
    print(f"       Flaeche / Flaeche der Einheitskugel = {area:.6f} (Grenzwert unendlicher Turm 4/3 = {4/3:.6f})")
    print(f"       Volumen / Volumen der Einheitskugel = {vol:.6f} (Grenzwert 8/7 = {8/7:.6f})")
    print(f"       Hoehe / Durchmesser der Einheitskugel = {height/2:.6f} (Grenzwert 2)")

TXT = {
 "de": dict(title="Ungleich lange Bänder: Erkundung k422 (Länge gesetzt ~ Dimension)",
   sub="Bänder der Länge 1/16, 1/8, 1/4, 1/2, 1 des Großkreises sind Kleinkreise. Sie müssen sich nicht kreuzen; dafür ist nur noch $\\mathbb{S}$ von selbst ein längster Kreis.",
   A="A  Runde Sphäre: Bänder als Kleinkreise", B="B  Kleinster Eingriff: Stufen", C="C  Größter Eingriff: Perlenkette",
   a="Kein Band kreuzt ein anderes.\nDie Abstoßung aus H209 greift nicht,\nkein Winkel ist festgelegt.",
   b="An jedem Band wird die Fläche waagerecht:\nRing und Rille. Höhe der Stufe frei.",
   c="Jedes Band ist Äquator einer eigenen Kugel\nmit Radius Dimension/16.",
   foot=("Gesetzt: Länge ~ Dimension; Bänder koaxial (ohne Kreuzung ist die Lage frei, koaxial ist nur die Zeichnung); die Regel „jedes Band liegt auf einem längsten Kreis“.\n"
         "Folgt: Auf der runden Sphäre ist nur $\\mathbb{S}$ maximal. Die vier kurzen Bänder erzwingen eine Verformung, zwischen Stufen (B) und Perlenkette (C) entscheidet erst eine Elastizität.")),
 "en": dict(title="Bands of unequal length: exploration k422 (length set ~ dimension)",
   sub="Bands of length 1/16, 1/8, 1/4, 1/2, 1 of the great circle are small circles. They need not cross; but only $\\mathbb{S}$ is a longest circle by itself.",
   A="A  Round sphere: bands as small circles", B="B  Smallest change: terraces", C="C  Largest change: string of pearls",
   a="No band crosses another.\nThe repulsion from H209 has nothing to act on,\nno angle is fixed.",
   b="At each band the surface becomes level:\nridge and groove. Step height free.",
   c="Each band is the equator of its own sphere\nwith radius dimension/16.",
   foot=("Set by hand: length ~ dimension; bands coaxial (without crossings the position is free, coaxial is only the drawing); the rule 'each band lies on a longest circle'.\n"
         "Follows: on the round sphere only $\\mathbb{S}$ is maximal. The four short bands force a deformation; between terraces (B) and pearls (C) only an elasticity decides.")),
}

def profile_sphere():
    t = np.linspace(0, np.pi, 1500); return np.sin(t), np.cos(t), [(np.cos(TH[i]), 0.012 + 0.006 * i) for i in range(5)]
def profile_terraces():
    t = np.linspace(0, np.pi, 6000); rho = np.sin(t).copy()
    for i in range(4):
        s = TH[i] / 4.2; rho += -math.cos(TH[i]) * (t - TH[i]) * np.exp(-(t - TH[i]) ** 2 / (2 * s * s))
    z = np.cos(t); return rho, z, [(np.cos(TH[i]), 0.012 + 0.006 * i) for i in range(5)]
def profile_pearls():
    c = [0.0]; 
    for i in (3, 2, 1, 0): c.append(c[-1] + (R[i + 1] + R[i]) * 0.985)
    cen = dict(zip([4, 3, 2, 1, 0], c)); z = np.linspace(-1, cen[0] + R[0], 9000); rho = np.zeros_like(z)
    for i in range(5): rho = np.maximum(rho, np.sqrt(np.clip(R[i] ** 2 - (z - cen[i]) ** 2, 0, None)))
    return rho, z, [(cen[i], 0.012 + 0.006 * i) for i in range(5)]

def render(ax, rho, z, bands, elev=16, nph=260):
    e = math.radians(elev); d = np.array([math.cos(e), 0, math.sin(e)]); r = np.array([0, 1.0, 0]); up = np.cross(d, r)
    ph = np.linspace(0, 2 * np.pi, nph + 1); RHO, PH = np.meshgrid(rho, ph, indexing="ij"); Z = np.meshgrid(z, ph, indexing="ij")[0]
    Pt = np.stack([RHO * np.cos(PH), RHO * np.sin(PH), Z], -1)
    q = np.stack([Pt[:-1, :-1], Pt[1:, :-1], Pt[1:, 1:], Pt[:-1, 1:]], 2).reshape(-1, 4, 3); cen = q.mean(1)
    nrm = np.cross(q[:, 2] - q[:, 0], q[:, 3] - q[:, 1]); nn = np.linalg.norm(nrm, axis=1); nn[nn < 1e-14] = 1; nrm /= nn[:, None]
    out = cen.copy(); out[:, 2] = 0; flip = np.einsum("ij,ij->i", nrm, out) < 0
    zc = cen[:, 2]
    nrm[flip] *= -1
    col = np.tile(np.array(to_rgb("#e9edf2")), (len(q), 1))
    for i in np.argsort(DIM)[::-1]:
        zb, hw = bands[i]; col[np.abs(zc - zb) < hw] = to_rgb(COL[i])
    light = -0.35 * r + 0.45 * up + 0.82 * d; light /= np.linalg.norm(light)
    col = np.clip(col * (0.52 + 0.48 * np.clip(np.abs(nrm @ light), 0, 1))[:, None], 0, 1)
    idx = np.argsort(cen @ d); xy = np.stack([q @ r, q @ up], -1)[idx]
    ax.add_collection(PolyCollection(xy, facecolors=col[idx], edgecolors=col[idx], linewidths=0.2, antialiaseds=False, rasterized=True))
    ax.set_aspect("equal"); ax.axis("off")

def draw(lang, out):
    T = TXT[lang]; fig = plt.figure(figsize=(16, 9)); fig.patch.set_facecolor("white")
    specs = [("A", profile_sphere(), [0.02, 0.25, 0.31, 0.58], (-1.15, 1.15, -1.15, 1.15), "a"),
             ("B", profile_terraces(), [0.345, 0.25, 0.31, 0.58], (-1.15, 1.15, -1.15, 1.15), "b"),
             ("C", profile_pearls(), [0.67, 0.21, 0.31, 0.64], (-1.45, 1.45, -1.15, 3.05), "c")]
    for k, (rho, z, bands), box, lim, cap in specs:
        ax = fig.add_axes(box); render(ax, rho, z, bands); ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3])
        fig.text(box[0] + 0.01, 0.865, T[k], fontsize=13, fontweight="bold"); fig.text(box[0] + 0.01, 0.185, T[cap], fontsize=10.5, color=INK, va="top", linespacing=1.4)
    fig.text(0.02, 0.955, T["title"], fontsize=19, fontweight="bold"); fig.text(0.02, 0.918, T["sub"], fontsize=11.5, color=INK)
    for i in range(5):
        fig.text(0.36 + 0.055 * i, 0.225, f"{SYM[i]} {int(DIM[i])}/16", color=COL[i], fontsize=12, fontweight="bold")
    fig.text(0.02, 0.022, T["foot"], fontsize=10, color=INK, linespacing=1.4)
    for ext in ("png", "pdf"): fig.savefig(out / f"baender_ungleich_lang_{lang}.{ext}", dpi=160)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--lang", default="de"); ap.add_argument("--out", default=".")
    a = ap.parse_args(); out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    part1(); part2(); part3_numbers(); draw(a.lang, out); print("\ngeschrieben: baender_ungleich_lang_" + a.lang, file=sys.stderr)
