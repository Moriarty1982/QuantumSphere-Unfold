#!/usr/bin/env python3
"""Grafik 2 (Erkundung): Wie verformt sich die Sphäre, wenn die fünf Bänder aus H192 darum liegen?

Aufruf:  python k420_baender_verformung.py [--lang de|en] [--out ORDNER] [--amp 0.28] [--m2 6]
Setzungen (nichts davon hergeleitet):
  S1 Jedes Band will möglichst lang sein, Zug nach außen proportional zum Gewicht w_i = Dimension.
  S2 Die Sphäre ist eine elastische Haut: Energie (1/2) Int (|grad u|^2 + m2 u^2), u = radiale Auslenkung, Volumen fest.
  S3 Die Bänder bleiben auf ihren Lagen aus H192 (keine Rückwirkung der Form auf die Lage).
  S4 Die Stärke der Kopplung ist frei; gezeichnet wird mit größter Auslenkung = amp.
Lineare Antwort: u(x) = sum_i w_i G(n_i.x), G(c) = sum_{l gerade >= 2} (2l+1)/2 P_l(0) P_l(c) / (l(l+1) + m2).
"""
import argparse, itertools, math, pathlib
import numpy as np
from numpy.polynomial import legendre as L
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.colors import to_rgb
import k420_baender_sphaere as bs

LMAX = 80
def green(c, m2, lmin=2):
    co = np.zeros(LMAX + 1)
    for l in range(lmin, LMAX + 1, 2):
        co[l] = (2 * l + 1) / 2 * L.legval(0.0, [0] * l + [1]) / (l * (l + 1) + m2)
    return L.legval(c, co), co
def field(x, V, w, m2):
    return sum(w[i] * green(np.clip(x @ V[i], -1, 1), m2)[0] for i in range(5))

TXT = {
 "de": dict(title="Die Sphäre unter den fünf Bändern: Erkundung mit gesetztem Spannungsgesetz",
   sub="Auf der runden Sphäre sind alle fünf Großkreise schon gleichzeitig maximal lang (k399). Eine Verformung entsteht erst mit einem gesetzten Zug je Band.",
   A="A  Verformte Sphäre, Blick wie in Grafik 1", B="B  Blick von oben auf den Pol von $\\mathbb{S}$", C="C  Schnitte gegen den Kreis",
   cutS="entlang Band $\\mathbb{S}$", cutO="entlang Band $\\mathbb{O}$", cutP="senkrecht zu beiden", ref="runde Sphäre",
   cb="Auslenkung nach außen / innen",
   setz=("Gesetzt (nicht hergeleitet):\n"
         "S1  Jedes Band will möglichst lang sein, Zug nach außen ~ Gewicht = Dimension.\n"
         "S2  Die Sphäre ist eine elastische Haut mit festem Volumen (Steifigkeit $m^2$ = {m2:g}).\n"
         "S3  Die Bänder bleiben auf den Lagen aus H192 (keine Rückwirkung).\n"
         "S4  Die Stärke der Kopplung ist frei: gezeichnet mit größter Auslenkung {amp:.0f} %."),
   res="Form bei dieser Steifigkeit:  {res}.\nGrößte Beule immer an der Kreuzung von $\\mathbb{{O}}$ und $\\mathbb{{S}}$; Verhältnis Delle zu Beule −0,26 bis −0,38 für $m^2$ = 20 bis 2."),
 "en": dict(title="The sphere under the five bands: exploration with a tension law set by hand",
   sub="On the round sphere all five great circles already have maximal length at once (k399). A deformation only arises once a pull per band is set.",
   A="A  Deformed sphere, view as in figure 1", B="B  View from above onto the pole of $\\mathbb{S}$", C="C  Sections against the circle",
   cutS="along band $\\mathbb{S}$", cutO="along band $\\mathbb{O}$", cutP="perpendicular to both", ref="round sphere",
   cb="displacement outward / inward",
   setz=("Set by hand (not derived):\n"
         "S1  Each band wants maximal length, outward pull ~ weight = dimension.\n"
         "S2  The sphere is an elastic skin with fixed volume (stiffness $m^2$ = {m2:g}).\n"
         "S3  The bands stay at their H192 positions (no back-reaction).\n"
         "S4  The coupling strength is free: drawn with largest displacement {amp:.0f} %."),
   res="Shape at this stiffness:  {res}.\nHighest bulge always at the crossing of $\\mathbb{{O}}$ and $\\mathbb{{S}}$; ratio dent to bulge −0.26 to −0.38 for $m^2$ = 20 to 2."),
}

def render(ax, V, w, m2, scale, B, hw, nth=320, nph=640):
    r, up, d = B
    th = np.linspace(0, np.pi, nth + 1); ph = np.linspace(0, 2 * np.pi, nph + 1)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    X = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)], -1)
    U = field(X.reshape(-1, 3), V, w, m2).reshape(TH.shape) * scale
    P = X * (1 + U)[..., None]
    q = np.stack([P[:-1, :-1], P[1:, :-1], P[1:, 1:], P[:-1, 1:]], 2).reshape(-1, 4, 3)
    xc = np.stack([X[:-1, :-1], X[1:, :-1], X[1:, 1:], X[:-1, 1:]], 2).reshape(-1, 4, 3).mean(1); xc /= np.linalg.norm(xc, axis=1, keepdims=True)
    uc = np.stack([U[:-1, :-1], U[1:, :-1], U[1:, 1:], U[:-1, 1:]], 2).reshape(-1, 4).mean(1)
    nrm = np.cross(q[:, 2] - q[:, 0], q[:, 3] - q[:, 1]); nn = np.linalg.norm(nrm, axis=1); ok = nn > 1e-12
    nrm[ok] /= nn[ok][:, None]; nrm[~ok] = xc[~ok]
    nrm *= np.sign(np.einsum("ij,ij->i", nrm, xc))[:, None]
    um = np.abs(U).max(); cm = plt.get_cmap("RdBu_r")
    col = cm(0.5 + 0.38 * uc / um)[:, :3]
    for i in np.argsort(w):                       # schwere Bänder zuletzt, liegen oben
        m = np.abs(xc @ V[i]) < math.sin(hw[i]); col[m] = to_rgb(bs.COL[i])
    light = np.array([-0.35, 0.45, 0.82]); light = light[0] * r + light[1] * up + light[2] * d; light /= np.linalg.norm(light)
    sh = 0.50 + 0.50 * np.clip(nrm @ light, 0, 1); col = np.clip(col * sh[:, None], 0, 1)
    depth = q.mean(1) @ d; vis = (nrm @ d) > 0; idx = np.argsort(depth[vis])
    xy = np.stack([q[vis] @ r, q[vis] @ up], -1)[idx]
    ax.add_collection(PolyCollection(xy, facecolors=col[vis][idx], edgecolors=col[vis][idx], linewidths=0.25, antialiaseds=False))
    t = np.linspace(0, 2 * np.pi, 400); ax.plot(np.cos(t), np.sin(t), color="#555555", lw=0.9, ls=(0, (4, 3)), zorder=5)
    ax.set_aspect("equal"); ax.axis("off"); lim = 1 + um + 0.06; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    return um

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lang", default="de"); ap.add_argument("--out", default=".")
    ap.add_argument("--amp", type=float, default=0.28); ap.add_argument("--m2", type=float, default=6.0)
    a = ap.parse_args(); T = TXT[a.lang]; out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(11); V = bs.align(bs.solve(bs.DIM, 1, rng)); w = bs.DIM
    # Kennzahlen der Form (unabhängig von der Kopplungsstärke)
    g = np.random.default_rng(1).standard_normal((200000, 3)); g /= np.linalg.norm(g, axis=1, keepdims=True)
    for m2 in (2.0, a.m2, 20.0):
        u = field(g, V, w, m2); imax, imin = u.argmax(), u.argmin()
        # Quadrupolanteil
        co = green(0.0, m2)[1]; pw = {}
        for l in range(2, 9, 2):
            c1 = np.zeros(LMAX + 1); c1[l] = co[l]; ul = sum(w[i] * L.legval(np.clip(g @ V[i], -1, 1), c1) for i in range(5)); pw[l] = (ul ** 2).mean()
        tot = (u ** 2).mean()
        print(f"m2 = {m2:5.1f}: max bei {np.round(g[imax],2)} (u = {u[imax]:+.3f}), min bei {np.round(g[imin],2)} (u = {u[imin]:+.3f}), "
              f"min/max = {u[imin]/u[imax]:+.3f}; Anteil l=2: {pw[2]/tot:.3f}, l=4: {pw[4]/tot:.3f}, l=6: {pw[6]/tot:.3f}; Mittel {u.mean():+.4f}")
        if m2 == a.m2: U0, G0 = u, g
    scale = a.amp / np.abs(U0).max(); imax, imin = U0.argmax(), U0.argmin()
    ex, ey, ez = np.eye(3)
    ax_vals = {k: field(np.array([v]), V, w, a.m2)[0] * scale for k, v in (("x", ex), ("y", ey), ("z", ez))}
    print("Auslenkung auf den Achsen (x = Pol von O, y = Kreuzung O/S, z = Pol von S):", {k: round(float(v), 3) for k, v in ax_vals.items()})

    fig = plt.figure(figsize=(16, 9.2)); fig.patch.set_facecolor("white")
    hw = np.radians(1.2 + 0.75 * np.log2(bs.DIM))
    axA = fig.add_axes([0.005, 0.20, 0.40, 0.66]); render(axA, V, w, a.m2, scale, bs.view_basis(22, 38), hw)
    axB = fig.add_axes([0.385, 0.24, 0.31, 0.58]); render(axB, V, w, a.m2, scale, bs.view_basis(89.9, 38), hw)
    axC = fig.add_axes([0.715, 0.24, 0.27, 0.58]); t = np.linspace(0, 2 * np.pi, 721)
    axC.plot(np.cos(t), np.sin(t), color="#555555", lw=1.0, ls=(0, (4, 3)), label=T["ref"])
    for (e1, e2), c, lab in (((ex, ey), bs.COL[4], T["cutS"]), ((ey, ez), bs.COL[3], T["cutO"]), ((ex, ez), bs.INK, T["cutP"])):
        pts = np.outer(np.cos(t), e1) + np.outer(np.sin(t), e2); rr = 1 + field(pts, V, w, a.m2) * scale
        axC.plot(rr * np.cos(t), rr * np.sin(t), color=c, lw=2.2, label=lab)
    axC.set_aspect("equal"); axC.axis("off"); axC.set_xlim(-1.45, 1.45); axC.set_ylim(-1.45, 1.45)
    axC.legend(loc="upper center", bbox_to_anchor=(0.5, 0.0), frameon=False, fontsize=10.5, ncol=2)
    for ax_, k in ((axA, "A"), (axB, "B"), (axC, "C")):
        fig.text(ax_.get_position().x0 + 0.012, 0.865, T[k], fontsize=13, fontweight="bold")
    fig.text(0.02, 0.955, T["title"], fontsize=19, fontweight="bold")
    fig.text(0.02, 0.918, T["sub"], fontsize=11.5, color=bs.INK)
    fig.text(0.02, 0.035, T["setz"].format(m2=a.m2, amp=100 * a.amp), fontsize=10.5, color=bs.INK, va="bottom", linespacing=1.45)
    dez = (lambda s: s.replace(".", ",")) if a.lang == "de" else (lambda s: s)
    res = dez(f"größte Beule {100*U0[imax]*scale:+.0f} %, tiefste Delle {100*U0[imin]*scale:+.0f} %") if a.lang == "de" else f"highest bulge {100*U0[imax]*scale:+.0f} %, deepest dent {100*U0[imin]*scale:+.0f} %"
    fig.text(0.50, 0.035, T["res"].format(res=res), fontsize=10.5, color=bs.INK, va="bottom")
    for ext in ("png", "pdf"): fig.savefig(out / f"baender_verformung_{a.lang}.{ext}", dpi=160)
    print("geschrieben")
if __name__ == "__main__":
    main()
