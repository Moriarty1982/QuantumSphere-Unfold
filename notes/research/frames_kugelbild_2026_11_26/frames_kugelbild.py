#!/usr/bin/env python3
"""Frames der Konvention F als Bild auf der Zustandskugel (Erkundung, nicht blind, 26.11.2026).

Aufruf:  python frames_kugelbild.py [--lang de|en] [--out ORDNER]

Erzeugt drei Teilbilder (je PDF und PNG) und ein Gesamtbild:
  A  Halbkugel der Feldzustaende mit R, M, P, T, Schub-Meridian und den drei Abbildungen
  B  Schnitt durch die Meridianebene: Rapiditaet, Portgewichte
  C  je Frame: Feldvektoren E und B, Schwingungsellipse (Lesart k297), Portgewichte
Die Kontrollrechnung (sympy, exakt) wird vor dem Zeichnen ausgegeben.
"""
import argparse
import pathlib

import numpy as np
import sympy as sp

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, Rectangle, Arc

BETA = 0.5494056410          # beta_sym (eingesetzt; Zaehlpostulat r67, OP1 offen)
X = BETA**2
GAMMA = (1 + X) / (1 - X)    # gamma_L
EPS = np.arctanh(BETA)

COL = {"R": "#1f4e9c", "M": "#b3261e", "P": "#c98a00", "T": "#2e7d32", "Rd": "#6b6b6b",
       "E": "#b3261e", "B": "#1f4e9c", "S": "#c98a00", "ink": "#222222", "soft": "#9aa0a6"}

TXT = {
    "de": dict(
        R="R  Ruheframe", M="M  Materie-Frame", P="P  Lichtpunkt", T="T  Dual-Frame", Rd="D(R)",
        axb1=r"$b_1=\dfrac{|\mathbf{E}|^2-|\mathbf{B}|^2}{2u}$" + "\n(Port-Achse)",
        axb2=r"$b_2=\dfrac{\mathbf{E}\cdot\mathbf{B}}{u}$",
        axb3=r"$b_3=\dfrac{|\mathbf{E}\times\mathbf{B}|}{u}$" + "\n(Anteil Energiefluss)",
        boost=r"Schub $\varepsilon=\mathrm{artanh}\,\beta_{\rm sym}$",
        toP=r"Schub $\to\infty$",
        D=r"$D\colon z\mapsto iz$ (Dualität): halbe Drehung um die $b_3$-Achse",
        J=r"$J_B$: Spiegelung $b_1\to-b_1$",
        th=r"$\vartheta$: Spiegelung $b_2\to-b_2$",
        titleA="A  Die Frames auf der Zustandskugel",
        titleB="B  Schnitt entlang des Schub-Meridians",
        titleC="C  Was in jedem Frame vorliegt",
        disk="Zustandsscheibe der Konvention F\n(Schatten der Halbkugel)",
        rap=r"Rapidität $\eta$",
        port="Portgewichte $p_+ : p_-$",
        fields="Feldvektoren\n(Vertreter mit $\\mathbf{E}\\cdot\\mathbf{B}=0$)",
        ell="Schwingungsellipse\n(Lesart k297)",
        ports="Portgewichte",
        flow="Energiefluss",
        noflow="kein Energiefluss",
        ratio="Achsen",
        circle="Kreis", line="Strecke",
        sup="Frames der Konvention F als Zustände eines Feld-Dubletts $(\\mathbf{E},\\mathbf{B})$",
        foot=(r"$x=\beta_{\rm sym}^2=0{,}3018$ (eingesetzt), $\gamma_L=(1+x)/(1-x)=1{,}8647$, "
              r"$\varepsilon=0{,}6175$.  Lage der Punkte: $b_1=\mathrm{sech}\,2\eta$, $b_3=\tanh 2\eta$.  "
              "Die Namen der Frames und die Ellipse sind Lesarten."),
        pure="rein, $\\mathbf{E}\\parallel\\mathbf{B}$",
        lightlike="lichtartig",
    ),
    "en": dict(
        R="R  rest frame", M="M  matter frame", P="P  light point", T="T  dual frame", Rd="D(R)",
        axb1=r"$b_1=\dfrac{|\mathbf{E}|^2-|\mathbf{B}|^2}{2u}$" + "\n(port axis)",
        axb2=r"$b_2=\dfrac{\mathbf{E}\cdot\mathbf{B}}{u}$",
        axb3=r"$b_3=\dfrac{|\mathbf{E}\times\mathbf{B}|}{u}$" + "\n(share of energy flow)",
        boost=r"boost $\varepsilon=\mathrm{artanh}\,\beta_{\rm sym}$",
        toP=r"boost $\to\infty$",
        D=r"$D\colon z\mapsto iz$ (duality): half turn about the $b_3$ axis",
        J=r"$J_B$: reflection $b_1\to-b_1$",
        th=r"$\vartheta$: reflection $b_2\to-b_2$",
        titleA="A  The frames on the state sphere",
        titleB="B  Section along the boost meridian",
        titleC="C  What is present in each frame",
        disk="state disk of Convention F\n(shadow of the hemisphere)",
        rap=r"rapidity $\eta$",
        port="port weights $p_+ : p_-$",
        fields="field vectors\n(representative with $\\mathbf{E}\\cdot\\mathbf{B}=0$)",
        ell="oscillation ellipse\n(reading k297)",
        ports="port weights",
        flow="energy flow",
        noflow="no energy flow",
        ratio="axes",
        circle="circle", line="segment",
        sup="Frames of Convention F as states of one field doublet $(\\mathbf{E},\\mathbf{B})$",
        foot=(r"$x=\beta_{\rm sym}^2=0.3018$ (inserted), $\gamma_L=(1+x)/(1-x)=1.8647$, "
              r"$\varepsilon=0.6175$.  Positions: $b_1=\mathrm{sech}\,2\eta$, $b_3=\tanh 2\eta$.  "
              "The names of the frames and the ellipse are readings."),
        pure="pure, $\\mathbf{E}\\parallel\\mathbf{B}$",
        lightlike="light-like",
    ),
}


# --------------------------------------------------------------------------- Kontrollrechnung
def kontrolle():
    print("== Kontrollrechnung (sympy, exakt) ==")
    E1, E2, E3, B1, B2, B3 = sp.symbols("E1:4 B1:4", real=True)
    E = sp.Matrix([E1, E2, E3]); B = sp.Matrix([B1, B2, B3])
    u = (E.dot(E) + B.dot(B)) / 2
    b1 = (E.dot(E) - B.dot(B)) / (2 * u)
    b2 = E.dot(B) / u
    b3sq = E.cross(B).dot(E.cross(B)) / u**2
    print("1. b1^2 + b2^2 + |ExB|^2/u^2 - 1 =", sp.simplify(b1**2 + b2**2 + b3sq - 1),
          "  (jeder Feldzustand liegt auf der Einheitskugel, b3 >= 0)")

    eta, e0 = sp.symbols("eta e0", positive=True)
    v = sp.tanh(eta); g = sp.cosh(eta)
    # reines E-Feld entlang x, Schub entlang z:  E' = g(E + v x B), B' = g(B - v x E)
    Ev = sp.Matrix([e0, 0, 0]); Bv = sp.Matrix([0, 0, 0]); vv = sp.Matrix([0, 0, v])
    Ep = g * (Ev + vv.cross(Bv)); Bp = g * (Bv - vv.cross(Ev))
    up = (Ep.dot(Ep) + Bp.dot(Bp)) / 2
    b1p = sp.simplify((Ep.dot(Ep) - Bp.dot(Bp)) / (2 * up))
    b3p = sp.simplify(sp.sqrt(Ep.cross(Bp).dot(Ep.cross(Bp))) / up)
    print("2. R (reines E-Feld) unter Schub eta quer zum Feld:")
    print("   b1 - sech(2 eta) =", sp.simplify((b1p - 1 / sp.cosh(2 * eta)).rewrite(sp.exp)))
    print("   b3 - tanh(2 eta) =", sp.simplify((b3p - sp.tanh(2 * eta)).rewrite(sp.exp)))
    print("   |B'|/|E'| - tanh(eta) =", sp.simplify(sp.sqrt(Bp.dot(Bp) / Ep.dot(Ep)) - v))
    be = sp.symbols("beta", positive=True)
    p_plus = sp.simplify(((1 + b1p) / 2).subs(eta, sp.atanh(be)))
    print("3. bei eta = artanh(beta):  p_+ - 1/(1+beta^2) =", sp.simplify(p_plus - 1 / (1 + be**2)),
          ";  b1 - (1-beta^2)/(1+beta^2) =",
          sp.simplify(sp.expand_trig(b1p.rewrite(sp.tanh)).subs(eta, sp.atanh(be)) - (1 - be**2) / (1 + be**2)))
    mu = be**2
    print("4. Ellipse k297 (b/a = mu = beta^2): kleine/grosse Achse - b1(M) =",
          sp.simplify((1 - mu) / (1 + mu) - (1 - be**2) / (1 + be**2)))
    print("   Stokes-Anteil derselben Ellipse (1-mu^2)/(1+mu^2) =",
          f"{(1 - X**2) / (1 + X**2):.6f}", " gegen b1(M) = 1/gamma_L =", f"{1 / GAMMA:.6f}",
          " -> verschieden, siehe README")
    print("== Zahlen ==")
    print(f"beta_sym = {BETA:.10f}, x = {X:.6f}, gamma_L = {GAMMA:.6f}, eps = {EPS:.6f}")
    print(f"M: b1 = {1 / GAMMA:.6f}, b3 = {np.tanh(2 * EPS):.6f}, Winkel vom Pol R = "
          f"{np.degrees(np.arccos(1 / GAMMA)):.3f} Grad, p+ = {1 / (1 + X):.6f}, p- = {X / (1 + X):.6f}")
    print(f"T: b1 = {-1 / GAMMA:.6f}, b3 = {np.tanh(2 * EPS):.6f}, p+ = {X / (1 + X):.6f}, p- = {1 / (1 + X):.6f}")
    print("P: b1 = 0, b3 = 1, p+ = p- = 1/2;   R: b1 = 1, b3 = 0, p+ = 1")


# --------------------------------------------------------------------------- Geometrie
def frames():
    th = np.arccos(1 / GAMMA)            # Winkel vom Pol R
    return {"R": 0.0, "M": th, "P": np.pi / 2, "T": np.pi - th, "Rd": np.pi}


def proj(b1, b2, b3, az=np.radians(38), el=np.radians(16)):
    """Orthografische Projektion.  b1 nach oben, b3 zum Betrachter, b2 seitlich.  Rueckgabe (x, y, tiefe)."""
    xw, yw, zw = b2, -b3, b1               # Weltkoordinaten: y zeigt vom Betrachter weg
    xr = xw * np.cos(az) - yw * np.sin(az)
    yr = xw * np.sin(az) + yw * np.cos(az)
    return xr, zw * np.cos(el) - yr * np.sin(el), -(yr * np.cos(el) + zw * np.sin(el))


def arrow(ax, p, q, color, lw=1.6, style="-|>", ls="-", ms=12, z=5, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, lw=lw, color=color, ls=ls,
                                 zorder=z, connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))


# --------------------------------------------------------------------------- Teilbild A
def panel_a(ax, t):
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(t["titleA"], loc="left", fontsize=12, fontweight="bold")
    s = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(s), np.sin(s), color=COL["ink"], lw=1.0, zorder=1)                 # Umriss
    ax.add_patch(plt.Circle((0, 0), 1, color="#eef2f7", zorder=0))

    def curve(b1, b2, b3, **kw):
        x, y, d = proj(b1, b2, b3)
        front = d >= -1e-9
        kwb = dict(kw); kwb.update(lw=kw.get("lw", 1) * 0.7, alpha=0.35, ls=":")
        for mask, k in ((front, kw), (~front, kwb)):
            xs = np.where(mask, x, np.nan); ys = np.where(mask, y, np.nan)
            ax.plot(xs, ys, **k)

    # Gitter
    for lat in np.radians([-60, -30, 30, 60]):
        curve(np.full_like(s, np.sin(lat)), np.cos(lat) * np.cos(s), np.cos(lat) * np.sin(s),
              color=COL["soft"], lw=0.6, zorder=2)
    for lon in np.radians([30, 60, 120, 150]):
        curve(np.cos(s), np.sin(s) * np.cos(lon), np.sin(s) * np.sin(lon), color=COL["soft"], lw=0.6, zorder=2)
    # Aequator (b1 = 0) und Rand der Halbkugel (b3 = 0)
    curve(np.zeros_like(s), np.cos(s), np.sin(s), color=COL["ink"], lw=1.0, zorder=3)
    curve(np.cos(s), np.sin(s), np.zeros_like(s), color=COL["ink"], lw=1.0, zorder=3)

    # Zustandsscheibe (b3 = 0) leicht getoent
    xd, yd, _ = proj(np.cos(s), np.sin(s), np.zeros_like(s))
    ax.fill(xd, yd, color="#d7dde6", alpha=0.55, zorder=1)

    # Achsen
    for vec, key, off, ha in (((1.45, 0, 0), "axb1", (0.04, 0.02), "left"),
                              ((0, 1.5, 0), "axb2", (0.03, -0.02), "left"),
                              ((0, 0, 1.45), "axb3", (0.04, 0.04), "left")):
        x0, y0, _ = proj(0, 0, 0); x1, y1, _ = proj(*vec)
        arrow(ax, (x0, y0), (x1, y1), COL["ink"], lw=0.9, ms=9, z=4)
        ax.text(x1 + off[0], y1 + off[1], t[key], fontsize=8.5, ha=ha, va="center", color=COL["ink"])

    # Meridian der Frames (b2 = 0, b3 >= 0)
    fr = frames()
    th = np.linspace(0, np.pi, 300)
    x, y, _ = proj(np.cos(th), 0 * th, np.sin(th))
    ax.plot(x, y, color=COL["ink"], lw=1.4, zorder=6)
    # Schub R -> M (durchgezogen) und M -> P (gestrichelt)
    tm = np.linspace(0.04, fr["M"] - 0.05, 80)
    x, y, _ = proj(np.cos(tm), 0 * tm, np.sin(tm) * 1.0)
    ax.plot(x * 1.0, y, color=COL["M"], lw=3.2, zorder=7, solid_capstyle="round")
    arrow(ax, (x[-2], y[-2]), (x[-1], y[-1]), COL["M"], lw=3.2, ms=16, z=7)
    tp = np.linspace(fr["M"] + 0.06, np.pi / 2 - 0.06, 60)
    x, y, _ = proj(np.cos(tp), 0 * tp, np.sin(tp))
    ax.plot(x, y, color=COL["P"], lw=2.2, ls=(0, (2, 1.5)), zorder=7)
    arrow(ax, (x[-2], y[-2]), (x[-1], y[-1]), COL["P"], lw=2.0, ms=12, z=7)

    # Lot von M und T auf die Port-Achse (Schatten in der Scheibe)
    for k in ("M", "T"):
        xa, ya, _ = proj(np.cos(fr[k]), 0, np.sin(fr[k])); xb, yb, _ = proj(np.cos(fr[k]), 0, 0)
        ax.plot([xa, xb], [ya, yb], color=COL[k], lw=1.0, ls="--", zorder=5)
        ax.plot([xb], [yb], marker="o", ms=5, mfc="white", mec=COL[k], zorder=8)
    xa, ya, _ = proj(0, 0, 1); xb, yb, _ = proj(0, 0, 0)
    ax.plot([xb], [yb], marker="o", ms=5, mfc="white", mec=COL["P"], zorder=8)

    # Dualitaet D: M <-> T (halbe Drehung um die b3-Achse)
    xm, ym, _ = proj(np.cos(fr["M"]), 0, np.sin(fr["M"])); xt, yt, _ = proj(np.cos(fr["T"]), 0, np.sin(fr["T"]))
    arrow(ax, (xm - 0.07, ym - 0.05), (xt - 0.07, yt + 0.05), COL["T"], lw=1.4, style="<|-|>", ms=11, z=9, rad=0.45)

    lab = {"R": (0.06, 0.07, "left"), "M": (-0.10, 0.05, "right"), "P": (-0.09, -0.02, "right"),
           "T": (-0.10, -0.06, "right"), "Rd": (0.06, -0.08, "left")}
    for k, a in fr.items():
        x, y, _ = proj(np.cos(a), 0, np.sin(a))
        ax.plot([x], [y], marker="o", ms=10 if k != "Rd" else 7, color=COL[k], mec="white", mew=1.2, zorder=10)
        dx, dy, ha = lab[k]
        ax.text(x + dx, y + dy, t[k], color=COL[k], fontsize=10.5 if k != "Rd" else 9, fontweight="bold",
                ha=ha, va="center", zorder=11,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8))

    xm, ym, _ = proj(np.cos(0.5 * fr["M"]), 0, np.sin(0.5 * fr["M"]))
    ax.annotate(t["boost"], (xm, ym), (-1.72, 1.02), fontsize=9, color=COL["M"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["M"], lw=0.8))
    xm, ym, _ = proj(np.cos(1.3), 0, np.sin(1.3))
    ax.annotate(t["toP"], (xm, ym), (-1.72, 0.52), fontsize=9, color=COL["P"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["P"], lw=0.8))
    xs, ys, _ = proj(-0.5, 0.45, 0)
    ax.annotate(t["disk"], (xs, ys), (0.6, -1.35), fontsize=8.5, color=COL["ink"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["ink"], lw=0.7))
    ax.text(-1.72, -1.32, t["D"] + "\n" + t["J"] + "\n" + t["th"], fontsize=8.5, va="top", color=COL["ink"],
            linespacing=1.5)
    ax.set_xlim(-1.75, 1.95); ax.set_ylim(-1.9, 1.6)


# --------------------------------------------------------------------------- Teilbild B
def panel_b(ax, t):
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(t["titleB"], loc="left", fontsize=12, fontweight="bold")
    fr = frames()
    th = np.linspace(0, np.pi, 300)
    ax.fill_betweenx(np.cos(th), 0, np.sin(th), color="#eef2f7", zorder=0)
    ax.plot(np.sin(th), np.cos(th), color=COL["ink"], lw=1.4, zorder=3)
    arrow(ax, (0, -1.25), (0, 1.3), COL["ink"], lw=0.9, ms=9, z=2)
    arrow(ax, (0, 0), (1.42, 0), COL["ink"], lw=0.9, ms=9, z=2)
    ax.text(0.04, 1.3, "$b_1$", fontsize=10, va="center"); ax.text(1.44, 0, "$b_3$", fontsize=10, va="center")

    # Rapiditaetsmarken: Winkel vom Pol = gd(2 eta)
    for eta in (0.25, 0.5, 1.0, 1.5):
        a = np.arccos(1 / np.cosh(2 * eta))
        ax.plot([np.sin(a), 1.05 * np.sin(a)], [np.cos(a), 1.05 * np.cos(a)], color=COL["ink"], lw=0.8, zorder=3)
        ax.text(1.12 * np.sin(a), 1.12 * np.cos(a), f"{eta:g}".replace(".", "," if t is TXT["de"] else "."),
                fontsize=7.5, ha="center", va="center", color=COL["ink"])
    ax.text(1.02, 0.86, t["rap"], fontsize=8.5, color=COL["ink"], ha="left")

    # Schub
    tm = np.linspace(0.03, fr["M"] - 0.04, 60)
    ax.plot(np.sin(tm), np.cos(tm), color=COL["M"], lw=3.2, zorder=4, solid_capstyle="round")
    arrow(ax, (np.sin(tm[-2]), np.cos(tm[-2])), (np.sin(tm[-1]), np.cos(tm[-1])), COL["M"], lw=3.2, ms=16, z=4)
    tp = np.linspace(fr["M"] + 0.05, np.pi / 2 - 0.05, 60)
    ax.plot(np.sin(tp), np.cos(tp), color=COL["P"], lw=2.2, ls=(0, (2, 1.5)), zorder=4)

    # Winkel am Mittelpunkt
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=90 - np.degrees(fr["M"]), theta2=90, color=COL["M"], lw=1.0))
    ax.text(0.10, 0.31, f"{np.degrees(fr['M']):.1f}°".replace(".", "," if t is TXT["de"] else "."),
            fontsize=8, color=COL["M"])
    ax.plot([0, np.sin(fr["M"])], [0, np.cos(fr["M"])], color=COL["M"], lw=0.7, zorder=2)

    # Portgewichte als Balken links von der Achse
    ax.text(-0.62, 1.3, t["port"], fontsize=8.5, ha="center", va="center", color=COL["ink"])
    lab = {"R": (0.07, 0.06), "M": (0.08, 0.03), "P": (0.10, -0.10), "T": (0.08, -0.03), "Rd": (0.07, -0.07)}
    for k, a in fr.items():
        b1, b3 = np.cos(a), np.sin(a)
        ax.plot([0, b3], [b1, b1], color=COL[k], lw=0.9, ls="--", zorder=2)
        ax.plot([b3], [b1], marker="o", ms=10 if k != "Rd" else 7, color=COL[k], mec="white", mew=1.2, zorder=6)
        ax.plot([0], [b1], marker="o", ms=5, mfc="white", mec=COL[k], zorder=6)
        ax.text(b3 + lab[k][0], b1 + lab[k][1], t[k], color=COL[k], fontsize=10 if k != "Rd" else 9,
                fontweight="bold", va="center")
        pp = (1 + b1) / 2
        w, h, x0 = 0.9, 0.11, -1.07
        ax.add_patch(Rectangle((x0, b1 - h / 2), w * pp, h, color=COL["E"], alpha=0.85, lw=0, zorder=3))
        ax.add_patch(Rectangle((x0 + w * pp, b1 - h / 2), w * (1 - pp), h, color=COL["B"], alpha=0.85, lw=0, zorder=3))
        txt = f"{100 * pp:.1f} : {100 * (1 - pp):.1f}"
        if t is TXT["de"]:
            txt = txt.replace(".", ",")
        ax.text(x0 - 0.04, b1, txt, fontsize=8, ha="right", va="center", color=COL["ink"])
        ax.plot([x0 + w, 0], [b1, b1], color=COL[k], lw=0.6, ls=":", zorder=1)
    ax.text(-1.07, -1.22, "$p_+$", color=COL["E"], fontsize=9, fontweight="bold")
    ax.text(-0.25, -1.22, "$p_-$", color=COL["B"], fontsize=9, fontweight="bold")
    ax.set_xlim(-1.75, 1.95); ax.set_ylim(-1.4, 1.45)


# --------------------------------------------------------------------------- Teilbild C
def panel_c(fig, gs, t):
    fr = frames()
    keys = ["R", "M", "P", "T"]
    rows = [t["fields"], t["ell"], t["ports"]]
    axes = {}
    for r in range(3):
        for c, k in enumerate(keys):
            ax = fig.add_subplot(gs[r, c + 1]); ax.set_aspect("equal"); ax.axis("off")
            ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25)
            axes[r, k] = ax
        axl = fig.add_subplot(gs[r, 0]); axl.axis("off")
        axl.text(1.0, 0.5, rows[r], fontsize=9, ha="right", va="center", transform=axl.transAxes, color=COL["ink"])
        if r == 0:
            axl.text(0.0, 1.22, t["titleC"], fontsize=12, fontweight="bold", transform=axl.transAxes, va="bottom")
    dec = (lambda s: s.replace(".", ",")) if t is TXT["de"] else (lambda s: s)
    for k in keys:
        b1, b3 = np.cos(fr[k]), np.sin(fr[k])
        pp, pm = (1 + b1) / 2, (1 - b1) / 2
        # Zeile 1: Feldvektoren, Laengen sqrt(2 p+), sqrt(2 p-) bei festem u
        ax = axes[0, k]
        ax.set_title(t[k], color=COL[k], fontsize=10.5, fontweight="bold")
        e, b = np.sqrt(pp) * 1.1, np.sqrt(pm) * 1.1
        if e > 1e-6:
            arrow(ax, (0, 0), (0, e), COL["E"], lw=2.4, ms=14)
            ax.text(0.08, e * 0.95, r"$\mathbf{E}$", color=COL["E"], fontsize=11, va="top")
        if b > 1e-6:
            arrow(ax, (0, 0), (b, 0), COL["B"], lw=2.4, ms=14)
            ax.text(b * 0.95, 0.1, r"$\mathbf{B}$", color=COL["B"], fontsize=11, ha="right")
        if b3 > 1e-6:      # Energiefluss senkrecht zur Zeichenebene, Flaeche ~ b3
            rr = 0.30 * np.sqrt(b3)
            ax.add_patch(plt.Circle((-0.62, -0.62), rr, fc="white", ec=COL["S"], lw=1.8))
            ax.plot([-0.62 - rr * 0.6, -0.62 + rr * 0.6], [-0.62 - rr * 0.6, -0.62 + rr * 0.6], color=COL["S"], lw=1.6)
            ax.plot([-0.62 - rr * 0.6, -0.62 + rr * 0.6], [-0.62 + rr * 0.6, -0.62 - rr * 0.6], color=COL["S"], lw=1.6)
            ax.text(-0.2, -0.66, dec(f"{t['flow']}\n$b_3={b3:.3f}$"), fontsize=7.5, color=COL["S"], va="center")
        else:
            ax.text(0.0, -0.66, t["noflow"] + "\n$b_3=0$", fontsize=7.5, color=COL["soft"], va="center", ha="center")
        if k == "M":
            ax.text(0.0, -1.2, dec(r"$|\mathbf{B}|/|\mathbf{E}|=\beta_{\rm sym}=0.549$"), fontsize=8, ha="center")
        if k == "T":
            ax.text(0.0, -1.2, dec(r"$|\mathbf{E}|/|\mathbf{B}|=\beta_{\rm sym}=0.549$"), fontsize=8, ha="center")
        if k == "P":
            ax.text(0.0, -1.2, r"$|\mathbf{E}|=|\mathbf{B}|$, " + t["lightlike"], fontsize=8, ha="center")
        if k == "R":
            ax.text(0.0, -1.2, t["pure"], fontsize=8, ha="center")
        # Zeile 2: Ellipse mit kleine/grosse Achse = |b1|
        ax = axes[1, k]
        q = abs(b1)
        if q > 1e-6:
            ax.add_patch(Ellipse((0, 0), 2 * 0.9 * q, 2 * 0.9, fc="none", ec=COL[k], lw=2.2))
            sgn = 1 if k in ("R", "M") else -1          # Drehsinn; bei T umgekehrt
            a0 = np.radians(35)
            p0 = (0.9 * q * np.cos(a0), 0.9 * np.sin(a0)); a1 = a0 + sgn * 0.12
            p1 = (0.9 * q * np.cos(a1), 0.9 * np.sin(a1))
            arrow(ax, p0, p1, COL[k], lw=2.2, ms=18)
            a0 += np.pi; p0 = (0.9 * q * np.cos(a0), 0.9 * np.sin(a0)); a1 = a0 + sgn * 0.12
            p1 = (0.9 * q * np.cos(a1), 0.9 * np.sin(a1))
            arrow(ax, p0, p1, COL[k], lw=2.2, ms=18)
            lab = t["circle"] if k == "R" else dec(f"{t['ratio']} $\\gamma_L:1$ = {GAMMA:.3f} : 1")
        else:
            arrow(ax, (0, -0.9), (0, 0.9), COL[k], lw=2.2, style="<|-|>", ms=14)
            lab = t["line"]
        mu = {"R": "0", "M": "x", "P": "1", "T": "1/x"}[k]
        ax.text(0, -1.2, f"$\\mu={mu}$:  {lab}", fontsize=8, ha="center")
        # Zeile 3: Portgewichte
        ax = axes[2, k]
        ax.set_ylim(-0.9, 0.7)
        w, h = 2.0, 0.34
        ax.add_patch(Rectangle((-1, -h / 2), w * pp, h, color=COL["E"], alpha=0.85, lw=0))
        ax.add_patch(Rectangle((-1 + w * pp, -h / 2), w * pm, h, color=COL["B"], alpha=0.85, lw=0))
        rat = {"R": "1 : 0", "M": "1 : x", "P": "1 : 1", "T": "x : 1"}[k]
        ax.text(0, 0.42, f"$p_+:p_-$ = {rat}", fontsize=9, ha="center")
        ax.text(0, -0.5, dec(f"{100 * pp:.1f} % : {100 * pm:.1f} %"), fontsize=9, ha="center")


# --------------------------------------------------------------------------- Ausgabe
def save(fig, out, name):
    for ext in ("pdf", "png"):
        fig.savefig(out / f"{name}.{ext}", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["de", "en"], default="de")
    ap.add_argument("--out", default=str(pathlib.Path(__file__).resolve().parent))
    a = ap.parse_args()
    t = TXT[a.lang]
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    kontrolle()
    plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})

    fig, ax = plt.subplots(figsize=(7.4, 7.0)); panel_a(ax, t); save(fig, out, f"frames_A_kugel_{a.lang}")
    fig, ax = plt.subplots(figsize=(7.4, 5.7)); panel_b(ax, t); save(fig, out, f"frames_B_schnitt_{a.lang}")
    fig = plt.figure(figsize=(11.5, 6.6))
    gs = fig.add_gridspec(3, 5, width_ratios=[0.75, 1, 1, 1, 1], height_ratios=[1, 1, 0.5], hspace=0.25, wspace=0.05)
    panel_c(fig, gs, t); save(fig, out, f"frames_C_je_frame_{a.lang}")

    fig = plt.figure(figsize=(15.5, 14.2))
    g0 = fig.add_gridspec(2, 1, height_ratios=[1.05, 0.95], hspace=0.10)
    gt = g0[0].subgridspec(1, 2, wspace=0.02)
    panel_a(fig.add_subplot(gt[0]), t); panel_b(fig.add_subplot(gt[1]), t)
    gb = g0[1].subgridspec(3, 5, width_ratios=[0.75, 1, 1, 1, 1], height_ratios=[1, 1, 0.5], hspace=0.25, wspace=0.05)
    panel_c(fig, gb, t)
    fig.suptitle(t["sup"], fontsize=15, fontweight="bold", y=0.93)
    fig.text(0.5, 0.075, t["foot"], fontsize=9.5, ha="center", color=COL["ink"])
    save(fig, out, f"frames_gesamt_{a.lang}")
    print("geschrieben nach", out)


if __name__ == "__main__":
    main()
