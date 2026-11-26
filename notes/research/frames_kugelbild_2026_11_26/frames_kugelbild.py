#!/usr/bin/env python3
"""Frames der Konvention F und der HC als Bild auf der Zustandskugel (Erkundung, nicht blind, 26.11.2026).

Aufruf:  python frames_kugelbild.py [--lang de|en] [--out ORDNER]

Teilbilder (je PDF und PNG) und ein Gesamtbild:
  A  Halbkugel der Feldzustaende mit R, M, P, T, Schub-Meridian und den drei Abbildungen
  B  Schnitt durch die Meridianebene: Rapiditaet, Portgewichte
  C  je Frame: Feldvektoren E und B, Schwingungsellipse, Portgewichte
  D  was der HC macht: Achse der Kugel, Schatten auf der Achse, Sprung in einen Port
Die Kontrollrechnung (sympy, exakt) wird vor dem Zeichnen ausgegeben.

Achsen: b_C = E.B/u (Koeffizient von sigma_x, Achse des HC; im Artikel b_2),
        b_S = (|E|^2-|B|^2)/(2u) (Koeffizient von sigma_z, Sektorachse; im Artikel b_1),
        b_3 = |ExB|/u (Anteil des Energieflusses).
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
THM = np.arccos(1 / GAMMA)   # Winkel von M vom Pol R

COL = {"R": "#1f4e9c", "M": "#b3261e", "P": "#c98a00", "T": "#2e7d32", "Rd": "#6b6b6b",
       "E": "#b3261e", "B": "#1f4e9c", "S": "#c98a00", "ink": "#222222", "soft": "#9aa0a6",
       "HC": "#6a1b9a", "Q": "#00838f", "pp": "#6a1b9a", "pm": "#b39ddb"}

TXT = {
    "de": dict(
        R="R  Ruheframe", M="M  Materie-Frame", P="P  Lichtpunkt", T="T  Dual-Frame", Rd="D(R)",
        axC=r"$b_C=\dfrac{\mathbf{E}\cdot\mathbf{B}}{u}$" + "\n(Achse des HC)",
        axS=r"$b_S=\dfrac{|\mathbf{E}|^2-|\mathbf{B}|^2}{2u}$" + "\n(Sektorachse)",
        ax3=r"$b_3=\dfrac{|\mathbf{E}\times\mathbf{B}|}{u}$" + "\n(Anteil Energiefluss)",
        boost=r"Schub $\varepsilon=\mathrm{artanh}\,\beta_{\rm sym}$",
        toP=r"Schub $\to\infty$",
        maps=(r"$D\colon z\mapsto iz$ (Dualität): halbe Drehung um die $b_3$-Achse, M $\leftrightarrow$ T" + "\n"
              r"$\vartheta$ (Zeitumkehr): Spiegelung $b_C\to-b_C$, auf diesem Meridian wie $D$" + "\n"
              r"$J_B$ (Tausch E, B): Spiegelung $b_S\to-b_S$, lässt alle vier Frames fest"),
        titleA="A  Die Frames auf der Zustandskugel",
        titleB="B  Schnitt entlang des Schub-Meridians",
        titleC="C  Was in jedem Frame vorliegt",
        titleD="D  Was der HC macht",
        disk="Zustandsscheibe der Konvention F\n(Schatten der Halbkugel)",
        rap=r"Rapidität $\eta$",
        port="Portgewichte $p_+ : p_-$",
        fields="Feldvektoren\n(Vertreter mit $|\\mathbf{E}|=|\\mathbf{B}|$)",
        ell="Schwingungsellipse,\nwenn die Ports die zwei\nKreisanteile sind (k253)",
        ports="Portgewichte\n$p_\\pm=|\\mathbf{E}\\pm\\mathbf{B}|^2/4u$",
        flow="Energiefluss", noflow="kein Energiefluss",
        circle="Kreis", line="Strecke", axes="Achsen", k297="k297: ",
        sup="Frames der Konvention F und der HC als Zustände eines Feld-Dubletts $(\\mathbf{E},\\mathbf{B})$",
        foot=(r"$x=\beta_{\rm sym}^2=0{,}3018$ (eingesetzt), $\gamma_L=(1+x)/(1-x)=1{,}8647$, "
              r"$\varepsilon=0{,}6175$.  Lage der Frames: $b_C=\mathrm{sech}\,2\eta$, $b_3=\tanh 2\eta$, $b_S=0$.  "
              "Die Namen der Frames und die Ellipse sind Lesarten."),
        par="$\\mathbf{E}=\\mathbf{B}$", lightlike="$\\mathbf{E}\\perp\\mathbf{B}$, lichtartig",
        ang="Winkel zwischen $\\mathbf{E}$ und $\\mathbf{B}$: ",
        portC="Kompensator-Port  $C=\\frac{1}{2}(1+J_B)$\nbehält $(\\mathbf{E}+\\mathbf{B})/2$", 
        portA="Partner-Port  $A=\\frac{1}{2}(1-J_B)$\nbehält $(\\mathbf{E}-\\mathbf{B})/2$",
        hcaxis="Achse des HC",
        shadow="Schatten auf der Achse:\nPortgewichte",
        jumpC="mit 76,8 %", jumpA="mit 23,2 %",
        dual=r"Dualitätsdrehung um $\alpha=28{,}8°$" + "\n" + r"(auf der Kugel $2\alpha=57{,}6°$), r27",
        dtext=("Der HC ist eine Messung entlang der senkrechten Achse.\n"
               "1. Er sieht von jedem Zustand nur die Höhe $b_C$. Die Höhe\n"
               "    legt die Portgewichte fest: $p_\\pm=(1\\pm b_C)/2$.\n"
               "2. Was er durchlässt, liegt danach am Pol R ($\\mathbf{E}=\\mathbf{B}$).\n"
               "    Der Rest liegt am Gegenpol D(R).\n"
               "3. Zwei Wege führen von R auf dieselbe Höhe:\n"
               "    der Schub (rot, über die Kugel nach M) und die\n"
               "    Dualitätsdrehung mit HC (türkis, am Rand entlang, r27).\n"
               "    Der HC unterscheidet die beiden nicht."),
    ),
    "en": dict(
        R="R  rest frame", M="M  matter frame", P="P  light point", T="T  dual frame", Rd="D(R)",
        axC=r"$b_C=\dfrac{\mathbf{E}\cdot\mathbf{B}}{u}$" + "\n(axis of the HC)",
        axS=r"$b_S=\dfrac{|\mathbf{E}|^2-|\mathbf{B}|^2}{2u}$" + "\n(sector axis)",
        ax3=r"$b_3=\dfrac{|\mathbf{E}\times\mathbf{B}|}{u}$" + "\n(share of energy flow)",
        boost=r"boost $\varepsilon=\mathrm{artanh}\,\beta_{\rm sym}$",
        toP=r"boost $\to\infty$",
        maps=(r"$D\colon z\mapsto iz$ (duality): half turn about the $b_3$ axis, M $\leftrightarrow$ T" + "\n"
              r"$\vartheta$ (time reversal): reflection $b_C\to-b_C$, on this meridian the same as $D$" + "\n"
              r"$J_B$ (exchange of E, B): reflection $b_S\to-b_S$, fixes all four frames"),
        titleA="A  The frames on the state sphere",
        titleB="B  Section along the boost meridian",
        titleC="C  What is present in each frame",
        titleD="D  What the HC does",
        disk="state disk of Convention F\n(shadow of the hemisphere)",
        rap=r"rapidity $\eta$",
        port="port weights $p_+ : p_-$",
        fields="field vectors\n(representative with $|\\mathbf{E}|=|\\mathbf{B}|$)",
        ell="oscillation ellipse\nif the ports are the two\ncircular parts (k253)",
        ports="port weights\n$p_\\pm=|\\mathbf{E}\\pm\\mathbf{B}|^2/4u$",
        flow="energy flow", noflow="no energy flow",
        circle="circle", line="segment", axes="axes", k297="k297: ",
        sup="Frames of Convention F and the HC as states of one field doublet $(\\mathbf{E},\\mathbf{B})$",
        foot=(r"$x=\beta_{\rm sym}^2=0.3018$ (inserted), $\gamma_L=(1+x)/(1-x)=1.8647$, "
              r"$\varepsilon=0.6175$.  Positions of the frames: $b_C=\mathrm{sech}\,2\eta$, $b_3=\tanh 2\eta$, $b_S=0$.  "
              "The names of the frames and the ellipse are readings."),
        par="$\\mathbf{E}=\\mathbf{B}$", lightlike="$\\mathbf{E}\\perp\\mathbf{B}$, light-like",
        ang="angle between $\\mathbf{E}$ and $\\mathbf{B}$: ",
        portC="compensator port  $C=\\frac{1}{2}(1+J_B)$\nkeeps $(\\mathbf{E}+\\mathbf{B})/2$",
        portA="partner port  $A=\\frac{1}{2}(1-J_B)$\nkeeps $(\\mathbf{E}-\\mathbf{B})/2$",
        hcaxis="axis of the HC",
        shadow="shadow on the axis:\nport weights",
        jumpC="with 76.8 %", jumpA="with 23.2 %",
        dual=r"duality rotation by $\alpha=28.8°$" + "\n" + r"(on the sphere $2\alpha=57.6°$), r27",
        dtext=("The HC is a measurement along the vertical axis.\n"
               "1. Of every state it sees only the height $b_C$. The height\n"
               "    fixes the port weights: $p_\\pm=(1\\pm b_C)/2$.\n"
               "2. What it lets through lies at the pole R ($\\mathbf{E}=\\mathbf{B}$) afterwards.\n"
               "    The rest lies at the opposite pole D(R).\n"
               "3. Two routes lead from R to the same height:\n"
               "    the boost (red, over the sphere to M) and the\n"
               "    duality rotation with HC (teal, along the rim, r27).\n"
               "    The HC does not tell the two apart."),
    ),
}


# --------------------------------------------------------------------------- Kontrollrechnung
def stokes(E, B):
    u = (E.dot(E) + B.dot(B)) / 2
    return E.dot(B) / u, (E.dot(E) - B.dot(B)) / (2 * u), E.cross(B).dot(E.cross(B)) / u**2, u


def kontrolle():
    print("== Kontrollrechnung (sympy, exakt) ==")
    E = sp.Matrix(sp.symbols("E1:4", real=True)); B = sp.Matrix(sp.symbols("B1:4", real=True))
    bC, bS, b3sq, u = stokes(E, B)
    print("1. b_C^2 + b_S^2 + |ExB|^2/u^2 - 1 =", sp.simplify(bC**2 + bS**2 + b3sq - 1),
          "  (jeder Feldzustand liegt auf der Einheitskugel, b_3 >= 0)")

    eta, e0, be = sp.symbols("eta e0 beta", positive=True)
    v = sp.tanh(eta); g = sp.cosh(eta)
    Ev = sp.Matrix([e0, 0, 0]); Bv = sp.Matrix([e0, 0, 0]); vv = sp.Matrix([0, 0, v])   # R: E = B
    Ep = g * (Ev + vv.cross(Bv)); Bp = g * (Bv - vv.cross(Ev))
    c, s_, q, up = stokes(Ep, Bp)
    ex = lambda z: sp.simplify(z.rewrite(sp.exp))
    print("2. R (E = B) unter Schub eta quer zum Feld:")
    print("   b_C - sech(2 eta) =", ex(c - 1 / sp.cosh(2 * eta)), ";  b_S =", ex(s_),
          ";  b_3^2 - tanh(2 eta)^2 =", ex(q - sp.tanh(2 * eta)**2))
    pplus = sp.simplify(sp.expand_trig(((1 + c) / 2).rewrite(sp.tanh)).subs(eta, sp.atanh(be)))
    print("3. bei eta = artanh(beta):  p_+ - 1/(1+beta^2) =", sp.simplify(pplus - 1 / (1 + be**2)))

    print("4. HC im Feld-Dublett, C = (1+J_B)/2:  E' = B' = (E+B)/2")
    Ec = (E + B) / 2
    cC, cS, c3, uC = stokes(Ec, Ec)
    print("   Bild: b_C =", sp.simplify(cC), ", b_S =", sp.simplify(cS), ", b_3^2 =", sp.simplify(c3),
          " (Pol R);  behaltener Anteil - (1+b_C)/2 =", sp.simplify(uC / u - (1 + bC) / 2))
    Ea = (E - B) / 2
    aC, aS, a3, uA = stokes(Ea, -Ea)
    print("   Partner A: b_C =", sp.simplify(aC), " (Gegenpol D(R));  Anteil - (1-b_C)/2 =",
          sp.simplify(uA / u - (1 - bC) / 2))
    al = sp.symbols("alpha", real=True)
    print("5. Weg aus r27: R, Dualitaetsdrehung um alpha, dann HC (nicht selektiv): b_C = cos(2 alpha);")
    print("   mit tan(alpha) = beta:  cos(2 alpha) - (1-beta^2)/(1+beta^2) =",
          sp.simplify(sp.cos(2 * sp.atan(be)) - (1 - be**2) / (1 + be**2)),
          ";  p_+ = cos(alpha)^2 =", f"{np.cos(np.arctan(BETA))**2:.6f}")
    print("6. Portgewichte gegen Ellipse (a, b = Amplituden der zwei Kreisanteile, Gewichte a^2 : b^2):")
    xs = be**2
    print("   Konvention F, Gewichte 1 : x  ->  b/a = beta, Achsen (1+beta)/(1-beta) - exp(2 artanh beta) =",
          sp.simplify(((1 + be) / (1 - be) - sp.exp(2 * sp.atanh(be))).rewrite(sp.log)))
    print("   k292/k297, b/a = x  ->  Gewichte 1 : x^2, Achsen (1+x)/(1-x) = gamma_L, Hoehe (1-x^2)/(1+x^2);")
    print("   das ist die Hoehe nach einem Schub mit Geschwindigkeit x = beta^2:  sech(2 artanh x) - (1-x^2)/(1+x^2) =",
          sp.simplify(sp.expand_trig((1 / sp.cosh(2 * eta)).rewrite(sp.tanh)).subs(eta, sp.atanh(xs)) - (1 - xs**2) / (1 + xs**2)))
    print("== Zahlen ==")
    print(f"beta_sym = {BETA:.10f}, x = {X:.6f}, gamma_L = {GAMMA:.6f}, eps = {EPS:.6f}")
    print(f"M (Konvention F): Gewichte {1/(1+X):.6f} : {X/(1+X):.6f}, Hoehe b_C = {1/GAMMA:.6f}, Winkel vom Pol "
          f"{np.degrees(THM):.3f} Grad, b_3 = {np.tanh(2*EPS):.6f}, Ellipse {(1+BETA)/(1-BETA):.4f} : 1")
    print(f"k292/k297 (b/a = x): Gewichte {1/(1+X**2):.6f} : {X**2/(1+X**2):.6f}, Hoehe {(1-X**2)/(1+X**2):.6f}, "
          f"Winkel vom Pol {np.degrees(np.arccos((1-X**2)/(1+X**2))):.3f} Grad, Ellipse {GAMMA:.4f} : 1")


# --------------------------------------------------------------------------- Geometrie
def frames():
    return {"R": 0.0, "M": THM, "P": np.pi / 2, "T": np.pi - THM, "Rd": np.pi}


def proj(bc, bs, b3, az=np.radians(38), el=np.radians(16)):
    """Orthografisch.  b_C nach oben, b_3 zum Betrachter, b_S seitlich.  Rueckgabe (x, y, tiefe)."""
    xw, yw, zw = bs, -b3, bc
    xr = xw * np.cos(az) - yw * np.sin(az)
    yr = xw * np.sin(az) + yw * np.cos(az)
    return xr, zw * np.cos(el) - yr * np.sin(el), -(yr * np.cos(el) + zw * np.sin(el))


def arrow(ax, p, q, color, lw=1.6, style="-|>", ls="-", ms=12, z=5, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, lw=lw, color=color, ls=ls,
                                 zorder=z, connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))


def dec(t, s):
    return s.replace(".", ",") if t is TXT["de"] else s


BOX = dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8)


def sphere(ax, t, axes=True, grid=True):
    ax.set_aspect("equal"); ax.axis("off")
    s = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(s), np.sin(s), color=COL["ink"], lw=1.0, zorder=1)
    ax.add_patch(plt.Circle((0, 0), 1, color="#eef2f7", zorder=0))

    def curve(bc, bs, b3, **kw):
        x, y, d = proj(bc, bs, b3)
        front = d >= -1e-9
        kwb = dict(kw); kwb.update(lw=kw.get("lw", 1) * 0.7, alpha=0.35, ls=":")
        for mask, k in ((front, kw), (~front, kwb)):
            ax.plot(np.where(mask, x, np.nan), np.where(mask, y, np.nan), **k)

    if grid:
        for lat in np.radians([-60, -30, 30, 60]):
            curve(np.full_like(s, np.sin(lat)), np.cos(lat) * np.cos(s), np.cos(lat) * np.sin(s),
                  color=COL["soft"], lw=0.6, zorder=2)
        for lon in np.radians([30, 60, 120, 150]):
            curve(np.cos(s), np.sin(s) * np.cos(lon), np.sin(s) * np.sin(lon), color=COL["soft"], lw=0.6, zorder=2)
    curve(np.zeros_like(s), np.cos(s), np.sin(s), color=COL["ink"], lw=1.0, zorder=3)      # Aequator
    curve(np.cos(s), np.sin(s), np.zeros_like(s), color=COL["ink"], lw=1.0, zorder=3)      # Rand b_3 = 0
    xd, yd, _ = proj(np.cos(s), np.sin(s), np.zeros_like(s))
    ax.fill(xd, yd, color="#d7dde6", alpha=0.55, zorder=1)
    if axes:
        for vec, key, off, ha in (((1.45, 0, 0), "axC", (0.04, 0.02), "left"),
                                  ((0, 1.5, 0), "axS", (0.03, -0.02), "left"),
                                  ((0, 0, 1.45), "ax3", (0.04, 0.04), "left")):
            x0, y0, _ = proj(0, 0, 0); x1, y1, _ = proj(*vec)
            arrow(ax, (x0, y0), (x1, y1), COL["ink"], lw=0.9, ms=9, z=4)
            ax.text(x1 + off[0], y1 + off[1], t[key], fontsize=8.5, ha=ha, va="center", color=COL["ink"])


def meridian_arc(ax, a0, a1, color, lw=3.2, ls="-", head=True, ms=16, z=7, rim=False):
    th = np.linspace(a0, a1, 80)
    x, y, _ = proj(np.cos(th), np.sin(th) if rim else 0 * th, 0 * th if rim else np.sin(th))
    ax.plot(x, y, color=color, lw=lw, ls=ls, zorder=z, solid_capstyle="round")
    if head:
        arrow(ax, (x[-2], y[-2]), (x[-1], y[-1]), color, lw=lw, ms=ms, z=z)


def dot(ax, k, a, t, lab=None, size=10, rim=False):
    x, y, _ = proj(np.cos(a), np.sin(a) if rim else 0, 0 if rim else np.sin(a))
    ax.plot([x], [y], marker="o", ms=size, color=COL[k], mec="white", mew=1.2, zorder=10)
    if lab:
        dx, dy, ha, txt, fs = lab
        ax.text(x + dx, y + dy, txt, color=COL[k], fontsize=fs, fontweight="bold", ha=ha, va="center",
                zorder=11, bbox=BOX)
    return x, y


# --------------------------------------------------------------------------- Teilbild A
def panel_a(ax, t):
    sphere(ax, t)
    ax.set_title(t["titleA"], loc="left", fontsize=12, fontweight="bold")
    fr = frames()
    meridian_arc(ax, 0, np.pi, COL["ink"], lw=1.4, head=False, z=6)
    meridian_arc(ax, 0.04, fr["M"] - 0.05, COL["M"])
    meridian_arc(ax, fr["M"] + 0.06, np.pi / 2 - 0.06, COL["P"], lw=2.2, ls=(0, (2, 1.5)), ms=12)
    for k in ("M", "T"):
        xa, ya, _ = proj(np.cos(fr[k]), 0, np.sin(fr[k])); xb, yb, _ = proj(np.cos(fr[k]), 0, 0)
        ax.plot([xa, xb], [ya, yb], color=COL[k], lw=1.0, ls="--", zorder=5)
        ax.plot([xb], [yb], marker="o", ms=5, mfc="white", mec=COL[k], zorder=8)
    xb, yb, _ = proj(0, 0, 0)
    ax.plot([xb], [yb], marker="o", ms=5, mfc="white", mec=COL["P"], zorder=8)
    xm, ym, _ = proj(np.cos(fr["M"]), 0, np.sin(fr["M"])); xt, yt, _ = proj(np.cos(fr["T"]), 0, np.sin(fr["T"]))
    arrow(ax, (xm - 0.07, ym - 0.05), (xt - 0.07, yt + 0.05), COL["T"], lw=1.4, style="<|-|>", ms=11, z=9, rad=0.45)
    lab = {"R": (0.06, 0.07, "left"), "M": (-0.10, 0.05, "right"), "P": (-0.09, -0.02, "right"),
           "T": (-0.10, -0.06, "right"), "Rd": (0.06, -0.08, "left")}
    for k, a in fr.items():
        dot(ax, k, a, t, (*lab[k], t[k], 10.5 if k != "Rd" else 9), size=10 if k != "Rd" else 7)
    xm, ym, _ = proj(np.cos(0.5 * fr["M"]), 0, np.sin(0.5 * fr["M"]))
    ax.annotate(t["boost"], (xm, ym), (-1.72, 1.02), fontsize=9, color=COL["M"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["M"], lw=0.8))
    xm, ym, _ = proj(np.cos(1.3), 0, np.sin(1.3))
    ax.annotate(t["toP"], (xm, ym), (-1.72, 0.52), fontsize=9, color=COL["P"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["P"], lw=0.8))
    xs, ys, _ = proj(-0.5, 0.45, 0)
    ax.annotate(t["disk"], (xs, ys), (0.6, -1.35), fontsize=8.5, color=COL["ink"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["ink"], lw=0.7))
    ax.text(-1.72, -1.32, t["maps"], fontsize=8.2, va="top", color=COL["ink"], linespacing=1.5)
    ax.set_xlim(-1.75, 1.95); ax.set_ylim(-1.9, 1.6)


# --------------------------------------------------------------------------- Teilbild B
def panel_b(ax, t):
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(t["titleB"], loc="left", fontsize=12, fontweight="bold")
    fr = frames()
    th = np.linspace(0, np.pi, 300)
    ax.fill_betweenx(np.cos(th), 0, np.sin(th), color="#eef2f7", zorder=0)
    ax.plot(np.sin(th), np.cos(th), color=COL["ink"], lw=1.4, zorder=3)
    ax.plot([0, 0], [-1, 1], color=COL["HC"], lw=2.6, zorder=2, solid_capstyle="round")
    arrow(ax, (0, 1.0), (0, 1.3), COL["ink"], lw=0.9, ms=9, z=2)
    arrow(ax, (0, 0), (1.42, 0), COL["ink"], lw=0.9, ms=9, z=2)
    ax.text(0.04, 1.3, "$b_C$", fontsize=10, va="center"); ax.text(1.44, 0, "$b_3$", fontsize=10, va="center")
    ax.text(-0.04, -1.2, t["hcaxis"], fontsize=8.5, color=COL["HC"], ha="right", va="center")
    for eta in (0.25, 0.5, 1.0, 1.5):
        a = np.arccos(1 / np.cosh(2 * eta))
        ax.plot([np.sin(a), 1.05 * np.sin(a)], [np.cos(a), 1.05 * np.cos(a)], color=COL["ink"], lw=0.8, zorder=3)
        ax.text(1.12 * np.sin(a), 1.12 * np.cos(a), dec(t, f"{eta:g}"), fontsize=7.5, ha="center", va="center")
    ax.text(1.02, 0.86, t["rap"], fontsize=8.5, color=COL["ink"], ha="left")
    tm = np.linspace(0.03, fr["M"] - 0.04, 60)
    ax.plot(np.sin(tm), np.cos(tm), color=COL["M"], lw=3.2, zorder=4, solid_capstyle="round")
    arrow(ax, (np.sin(tm[-2]), np.cos(tm[-2])), (np.sin(tm[-1]), np.cos(tm[-1])), COL["M"], lw=3.2, ms=16, z=4)
    tp = np.linspace(fr["M"] + 0.05, np.pi / 2 - 0.05, 60)
    ax.plot(np.sin(tp), np.cos(tp), color=COL["P"], lw=2.2, ls=(0, (2, 1.5)), zorder=4)
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=90 - np.degrees(fr["M"]), theta2=90, color=COL["M"], lw=1.0))
    ax.text(0.10, 0.31, dec(t, f"{np.degrees(fr['M']):.1f}°"), fontsize=8, color=COL["M"])
    ax.plot([0, np.sin(fr["M"])], [0, np.cos(fr["M"])], color=COL["M"], lw=0.7, zorder=2)
    ax.text(-0.62, 1.3, t["port"], fontsize=8.5, ha="center", va="center", color=COL["ink"])
    lab = {"R": (0.07, 0.06), "M": (0.08, 0.03), "P": (0.10, -0.10), "T": (0.08, -0.03), "Rd": (0.07, -0.07)}
    for k, a in fr.items():
        bc, b3 = np.cos(a), np.sin(a)
        ax.plot([0, b3], [bc, bc], color=COL[k], lw=0.9, ls="--", zorder=2)
        ax.plot([b3], [bc], marker="o", ms=10 if k != "Rd" else 7, color=COL[k], mec="white", mew=1.2, zorder=6)
        ax.plot([0], [bc], marker="o", ms=5, mfc="white", mec=COL[k], zorder=6)
        ax.text(b3 + lab[k][0], bc + lab[k][1], t[k], color=COL[k], fontsize=10 if k != "Rd" else 9,
                fontweight="bold", va="center")
        pp = (1 + bc) / 2
        w, h, x0 = 0.9, 0.11, -1.07
        ax.add_patch(Rectangle((x0, bc - h / 2), w * pp, h, color=COL["pp"], lw=0, zorder=3))
        ax.add_patch(Rectangle((x0 + w * pp, bc - h / 2), w * (1 - pp), h, color=COL["pm"], lw=0, zorder=3))
        ax.text(x0 - 0.04, bc, dec(t, f"{100 * pp:.1f} : {100 * (1 - pp):.1f}"), fontsize=8, ha="right", va="center")
        ax.plot([x0 + w, 0], [bc, bc], color=COL[k], lw=0.6, ls=":", zorder=1)
    ax.text(-1.07, -1.42, "$p_+$", color=COL["pp"], fontsize=9, fontweight="bold")
    ax.text(-0.25, -1.42, "$p_-$", color=COL["pm"], fontsize=9, fontweight="bold")
    ax.set_xlim(-1.75, 1.95); ax.set_ylim(-1.5, 1.45)


# --------------------------------------------------------------------------- Teilbild D
def panel_d(ax, t):
    sphere(ax, t, axes=False, grid=False)
    ax.set_title(t["titleD"], loc="left", fontsize=12, fontweight="bold")
    xn, yn, _ = proj(1, 0, 0); xs, ys, _ = proj(-1, 0, 0)
    ax.plot([xn, xs], [yn, ys], color=COL["HC"], lw=3.0, zorder=5, solid_capstyle="round")
    meridian_arc(ax, 0, np.pi, COL["soft"], lw=1.0, head=False, z=4)
    meridian_arc(ax, 0.04, THM - 0.05, COL["M"])
    meridian_arc(ax, 0.04, THM - 0.05, COL["Q"], rim=True)
    xc, yc, _ = proj(np.cos(THM), 0, 0)
    xm, ym = dot(ax, "M", THM, t, (0.07, 0.06, "left", "M", 11))
    xq, yq = dot(ax, "Q", THM, t, rim=True)
    for (xa, ya), c in (((xm, ym), COL["M"]), ((xq, yq), COL["Q"])):
        arrow(ax, (xa, ya), (xc + 0.03 * np.sign(xa - xc), yc + 0.03 * (ya - yc) / abs(xa - xc)), c, lw=1.2, ls="--", ms=10, z=8)
    ax.plot([xc], [yc], marker="o", ms=8, mfc="white", mec=COL["HC"], mew=1.8, zorder=11)
    arrow(ax, (xc - 0.05, yc + 0.03), (xn - 0.05, yn - 0.06), COL["HC"], lw=2.0, ms=13, z=9)
    arrow(ax, (xc - 0.05, yc - 0.03), (xs - 0.05, ys + 0.06), COL["HC"], lw=2.0, ms=13, z=9)
    ax.text(xc - 0.10, (yc + yn) / 2, t["jumpC"], fontsize=9, color=COL["HC"], ha="right", va="center", bbox=BOX, zorder=12)
    ax.text(xc - 0.10, (yc + ys) / 2 - 0.1, t["jumpA"], fontsize=9, color=COL["HC"], ha="right", va="center", bbox=BOX, zorder=12)
    dot(ax, "R", 0, t, (0.07, 0.07, "left", "R", 11))
    dot(ax, "Rd", np.pi, t, (0.07, -0.07, "left", "D(R)", 9), size=7)
    ax.text(xn - 0.12, yn + 0.20, t["portC"], fontsize=8.8, color=COL["HC"], ha="right", va="center")
    ax.text(xs - 0.12, ys - 0.20, t["portA"], fontsize=8.8, color=COL["HC"], ha="right", va="center")
    ax.annotate(t["shadow"], (xc, yc), (-1.72, 0.25), fontsize=8.8, color=COL["HC"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["HC"], lw=0.8))
    xa, ya, _ = proj(np.cos(0.5 * THM), np.sin(0.5 * THM), 0)
    ax.annotate(t["dual"], (xa, ya), (0.75, 1.2), fontsize=8.8, color=COL["Q"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["Q"], lw=0.8))
    xa, ya, _ = proj(np.cos(0.6 * THM), 0, np.sin(0.6 * THM))
    ax.annotate(t["boost"], (xa, ya), (0.95, 0.72), fontsize=8.8, color=COL["M"], va="center",
                arrowprops=dict(arrowstyle="-", color=COL["M"], lw=0.8))
    ax.set_xlim(-1.75, 1.95); ax.set_ylim(-1.55, 1.55)


def panel_dtext(ax, t):
    ax.axis("off")
    ax.text(0.0, 0.5, t["dtext"], fontsize=10.5, va="center", ha="left", linespacing=1.55, color=COL["ink"],
            transform=ax.transAxes)


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
    for k in keys:
        phi = fr[k]                       # Winkel zwischen E und B = Winkel vom Pol
        bc, b3 = np.cos(phi), np.sin(phi)
        pp, pm = (1 + bc) / 2, (1 - bc) / 2
        ax = axes[0, k]
        ax.set_title(t[k], color=COL[k], fontsize=10.5, fontweight="bold")
        L, o = 0.95, np.array([0.0, -0.15])
        dE = L * np.array([np.sin(phi / 2), np.cos(phi / 2)]) * np.array([-1, 1])
        dB = L * np.array([np.sin(phi / 2), np.cos(phi / 2)])
        sh = np.array([0.05, 0]) if k == "R" else np.zeros(2)
        arrow(ax, tuple(o - sh), tuple(o - sh + dE), COL["E"], lw=2.4, ms=14)
        arrow(ax, tuple(o + sh), tuple(o + sh + dB), COL["B"], lw=2.4, ms=14)
        ax.text(*(o - sh + dE + np.array([-0.08, 0.02])), r"$\mathbf{E}$", color=COL["E"], fontsize=11, ha="right")
        ax.text(*(o + sh + dB + np.array([0.08, 0.02])), r"$\mathbf{B}$", color=COL["B"], fontsize=11, ha="left")
        if b3 > 1e-6:
            rr = 0.20 * np.sqrt(b3); cx, cy = -0.95, -0.72
            ax.add_patch(plt.Circle((cx, cy), rr, fc="white", ec=COL["S"], lw=1.6))
            for sg in (1, -1):
                ax.plot([cx - rr * 0.6, cx + rr * 0.6], [cy - sg * rr * 0.6, cy + sg * rr * 0.6], color=COL["S"], lw=1.4)
            ax.text(cx + 0.3, cy, dec(t, f"{t['flow']} $b_3={b3:.3f}$"), fontsize=7.5, color=COL["S"], va="center")
        else:
            ax.text(0.0, -0.72, t["noflow"] + ", $b_3=0$", fontsize=7.5, color=COL["soft"], va="center", ha="center")
        note = {"R": t["par"], "P": t["lightlike"]}.get(k, dec(t, t["ang"] + f"{np.degrees(phi):.1f}°"))
        ax.text(0.0, -1.2, note, fontsize=8, ha="center")
        # Ellipse aus den Portgewichten: a : b = sqrt(p+) : sqrt(p-)
        ax = axes[1, k]
        a_, b_ = np.sqrt(max(pp, pm)), np.sqrt(min(pp, pm))
        q = (a_ - b_) / (a_ + b_)
        sgn = 1 if k in ("R", "M") else -1
        if q > 1e-6:
            if k in ("M", "T"):       # zum Vergleich die Ellipse aus k297 (b/a = x)
                ax.add_patch(Ellipse((0, 0), 2 * 0.9 / GAMMA, 2 * 0.9, fc="none", ec=COL["soft"], lw=1.3, ls="--"))
            ax.add_patch(Ellipse((0, 0), 2 * 0.9 * q, 2 * 0.9, fc="none", ec=COL[k], lw=2.2))
            for a0 in (np.radians(35), np.radians(215)):
                p0 = (0.9 * q * np.cos(a0), 0.9 * np.sin(a0)); a1 = a0 + sgn * 0.12
                arrow(ax, p0, (0.9 * q * np.cos(a1), 0.9 * np.sin(a1)), COL[k], lw=2.2, ms=18)
            if k == "R":
                lab = t["circle"]
            else:
                lab = dec(t, f"{t['axes']} $e^{{2\\varepsilon}}:1$ = {1 / q:.2f} : 1\n") + \
                      dec(t, f"({t['k297']}$\\gamma_L:1$ = {GAMMA:.2f} : 1)")
        else:
            arrow(ax, (0, -0.9), (0, 0.9), COL[k], lw=2.2, style="<|-|>", ms=14)
            lab = t["line"]
        ax.text(0, -1.08, lab, fontsize=8, ha="center", va="top")
        ax = axes[2, k]
        ax.set_ylim(-0.9, 0.7)
        w, h = 2.0, 0.34
        ax.add_patch(Rectangle((-1, -h / 2), w * pp, h, color=COL["pp"], lw=0))
        ax.add_patch(Rectangle((-1 + w * pp, -h / 2), w * pm, h, color=COL["pm"], lw=0))
        rat = {"R": "1 : 0", "M": "1 : x", "P": "1 : 1", "T": "x : 1"}[k]
        ax.text(0, 0.42, f"$p_+:p_-$ = {rat}", fontsize=9, ha="center")
        ax.text(0, -0.5, dec(t, f"{100 * pp:.1f} % : {100 * pm:.1f} %"), fontsize=9, ha="center")


# --------------------------------------------------------------------------- Ausgabe
def save(fig, out, name):
    for ext in ("pdf", "png"):
        fig.savefig(out / f"{name}.{ext}", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


CW = dict(width_ratios=[0.75, 1, 1, 1, 1], height_ratios=[1, 1.08, 0.5], hspace=0.3, wspace=0.05)


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
    fig, ax = plt.subplots(figsize=(7.4, 5.9)); panel_b(ax, t); save(fig, out, f"frames_B_schnitt_{a.lang}")
    fig = plt.figure(figsize=(11.5, 6.9)); panel_c(fig, fig.add_gridspec(3, 5, **CW), t)
    save(fig, out, f"frames_C_je_frame_{a.lang}")
    fig = plt.figure(figsize=(13.0, 6.2)); g = fig.add_gridspec(1, 2, width_ratios=[1.2, 1], wspace=0.02)
    panel_d(fig.add_subplot(g[0]), t); panel_dtext(fig.add_subplot(g[1]), t); save(fig, out, f"frames_D_hc_{a.lang}")

    fig = plt.figure(figsize=(15.5, 21.0))
    g0 = fig.add_gridspec(3, 1, height_ratios=[1.05, 0.9, 1.0], hspace=0.08)
    gt = g0[0].subgridspec(1, 2, wspace=0.02)
    panel_a(fig.add_subplot(gt[0]), t); panel_b(fig.add_subplot(gt[1]), t)
    gm = g0[1].subgridspec(1, 2, width_ratios=[1.2, 1], wspace=0.02)
    panel_d(fig.add_subplot(gm[0]), t); panel_dtext(fig.add_subplot(gm[1]), t)
    panel_c(fig, g0[2].subgridspec(3, 5, **CW), t)
    fig.suptitle(t["sup"], fontsize=15, fontweight="bold", y=0.915)
    fig.text(0.5, 0.085, t["foot"], fontsize=9.5, ha="center", color=COL["ink"])
    save(fig, out, f"frames_gesamt_{a.lang}")
    print("geschrieben nach", out.name)


if __name__ == "__main__":
    main()
