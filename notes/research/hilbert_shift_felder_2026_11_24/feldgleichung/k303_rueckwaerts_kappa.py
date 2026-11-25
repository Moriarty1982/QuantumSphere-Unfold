#!/usr/bin/env python3
"""k303: Rueckwaertssuche. Welche Regel muesste gelten, damit kappa ~ 1,2 herauskommt?

Erkundung, nicht blind (Ziel bekannt aus k300/k302; der Zahlentreffer in Teil 5 wurde
beim Planen bemerkt, bevor die Kandidatenliste feststand).
Werkzeug: Python (numpy, sympy). Gegenprobe: k303b_gegenprobe.wl.
Aufruf: python3 k303_rueckwaerts_kappa.py > k303_out.txt
"""
import numpy as np
import sympy as sp

mW, mZ, mt, mh, v = 80.37, 91.19, 172.6, 125.2, 246.22   # GeV, aus dem Gedaechtnis wie k300
N, M = 4, 4

print("=== Teil 1: Ziel und notwendige Bedingung ===")
SM = 6 * mW**4 + 3 * mZ**4 - 12 * mt**4


def mh_of(kap, n=M, mt_=mt):
    s = n * (2 * kap * v**2)**2 + 6 * mW**4 + 3 * mZ**4 - 12 * mt_**4
    return np.sign(s) * np.sqrt(abs(s) / (8 * np.pi**2 * v**2))


def kap_of(mh_, mt_=mt, n=M):
    return np.sqrt((mh_**2 * 8 * np.pi**2 * v**2 - 6 * mW**4 - 3 * mZ**4 + 12 * mt_**4) / n) / (2 * v**2)


ks = kap_of(mh)
print(f"Ziel: kappa* = {ks:.4f}  (m_S = {np.sqrt(2*ks)*v:.1f} GeV); Fenster ±20 % der Summe: {ks*np.sqrt(0.8):.4f} bis {ks*np.sqrt(1.2):.4f}")
g2, gp2, yt2 = 4 * mW**2 / v**2, 4 * (mZ**2 - mW**2) / v**2, 2 * mt**2 / v**2
print(f"in Kopplungen: g² = {g2:.4f}, g'² = {gp2:.4f}, y_t² = {yt2:.4f}, m_h²/v² = {mh**2/v**2:.4f}")
print("notwendige Bedingung: 16·kappa² = 8π²·m_h²/v² − (3/8)·g⁴ − (3/16)·(g²+g'²)² + 3·y_t⁴")
parts = (8 * np.pi**2 * mh**2 / v**2, -3 / 8 * g2**2, -3 / 16 * (g2 + gp2)**2, 3 * yt2**2)
print("  Anteile:", [round(p, 4) for p in parts], " Summe/16 =", round(sum(parts) / 16, 4), " kappa*² =", round(ks**2, 4))
kmin = np.sqrt(-SM / M) / (2 * v**2)
print(f"kleinstes kappa mit positivem m_s²: {kmin:.4f} (m_S = {np.sqrt(2*kmin)*v:.1f} GeV)")
print("Empfindlichkeit: d ln m_h / d ln kappa bei kappa* =", round((mh_of(ks * 1.001) - mh_of(ks)) / mh / 0.001, 3))
for dmt in (-0.7, 0.7):
    print(f"  m_t {dmt:+.1f} GeV: kappa* = {kap_of(mh, mt + dmt):.4f}")
for dmh in (-0.2, 0.2):
    print(f"  m_h {dmh:+.1f} GeV: kappa* = {kap_of(mh + dmh):.4f}")

print()
print("=== Teil 2: Regeln mit einem Prinzip dahinter ===")
rows = []
# R1 volle Norm
rows.append(("R1 volle Norm (auch S-a + su(3))", 0.0))
# Veltman: keine quadratische Divergenz in der Masse der Vorstufe
#   3 m_h² + 6 m_W² + 3 m_Z² + M·m_S² − 12 m_t² = 0  (m_S² = 2 kappa v²)
mS2_a = (12 * mt**2 - 6 * mW**2 - 3 * mZ**2) / M               # skalenfrei: lambda_A = 0 am Baum
rows.append(("V1 Veltman, skalenfrei (ohne m_h-Term)", mS2_a / (2 * v**2)))
mS2_b = (12 * mt**2 - 6 * mW**2 - 3 * mZ**2 - 3 * mh**2) / M
rows.append(("V2 Veltman mit gemessenem m_h", mS2_b / (2 * v**2)))
# selbstkonsistent: Veltman mit m_h aus der Schleifenformel
k = sp.symbols('k', positive=True)
mh2 = (M * (2 * k * v**2)**2 + SM) / (8 * sp.pi**2 * v**2)
sol = sp.nsolve(3 * mh2 + 6 * mW**2 + 3 * mZ**2 + M * 2 * k * v**2 - 12 * mt**2, k, 0.6)
rows.append(("V3 Veltman, m_h selbstkonsistent", float(sol)))
# Supertrace M^4 = 0 (endliches Ein-Schleifen-Potential)
rows.append(("S4 Sp M⁴ = 0 (Bosonen = Fermionen)", kmin))
# Unitaritaet gesaettigt: a0 = 2 kappa sqrt(NM)/(16 pi) = 1/2
rows.append(("U  Unitaritaetsgrenze gesaettigt, kappa = 4π/√(NM)", 4 * np.pi / np.sqrt(N * M)))
print(f"{'Regel':52s} {'kappa':>8s} {'m_S/GeV':>9s} {'m_h/GeV':>9s}  im Fenster")
for name, kv in rows:
    mhv = mh_of(kv)
    inw = ks * np.sqrt(0.8) <= kv <= ks * np.sqrt(1.2)
    print(f"{name:52s} {kv:8.4f} {np.sqrt(2*kv)*v:9.1f} {mhv:9.1f}  {inw}")
print("(negatives m_h bedeutet m_s² < 0: kein Minimum)")

print()
print("--- fester Punkt von kappa mit Eichfeldern und Top (Formel der Zwei-Dublett-Modelle aus dem Gedaechtnis, lambda_3 = 4·kappa) ---")
l3 = sp.symbols('l3', real=True)
for label, gauge in (("Anhang als Dublett geeicht", 1), ("Anhang ungeeicht", 0)):
    # 16π² β = 4 l3² + l3(6 y_t² − c(9g²+3g'²)/…) + Eichanteil
    if gauge:
        expr = 4 * l3**2 + l3 * (6 * yt2 - 3 * (3 * g2 + gp2)) + sp.Rational(3, 4) * (3 * g2**2 + gp2**2 - 2 * g2 * gp2)
    else:
        expr = 4 * l3**2 + l3 * (6 * yt2 - sp.Rational(3, 2) * (3 * g2 + gp2))
    print(f"{label}: Nullstellen von β(lambda_3) bei lambda_A = lambda_C = 0:", [sp.N(r, 5) for r in sp.solve(expr, l3)])
print("Ziel waere lambda_3 =", round(4 * ks, 4))

print()
print("--- Variante: Eichfelder der eigenen su(2) des Anhangs statt Skalare ---")
n_v = 9
m_v = ((mh**2 * 8 * np.pi**2 * v**2 - SM) / n_v) ** 0.25
mu = 0.3018
print(f"drei Vektorfelder (9 Freiheitsgrade): noetig m = {m_v:.1f} GeV; mit gleicher Kopplung g und Anhang-Wert mu·v: m = {mW*mu:.1f} GeV; noetig waere ein Anhang-Wert von {m_v/mW:.2f}·v")

print()
print("=== Teil 3: reine Zahlen des HC als Kopplung (Zahlensuche, kein Prinzip) ===")
gL = (1 + mu) / (1 - mu)
c2 = (1 - mu**2) / (1 + mu**2)
s2 = 2 * mu / (1 + mu**2)
tau = 2 * mu / (1 - mu**2)
base = {"mu": mu, "1/mu": 1 / mu, "mu²": mu**2, "1/mu²": mu**-2, "√mu": np.sqrt(mu), "1/√mu": mu**-0.5,
        "gamma_L": gL, "1/gamma_L": 1 / gL, "tau=tan2θ": tau, "1/tau": 1 / tau,
        "cos2θ": c2, "1/cos2θ": 1 / c2, "sin2θ": s2, "1/sin2θ": 1 / s2}
norms = {"kappa": 1.0, "2kappa=m_S²/v²": 2.0, "4kappa=lambda_3": 4.0}
print(f"mu = {mu}, gamma_L = {gL:.4f}; {len(base)} Zahlen × {len(norms)} Normierungen = {len(base)*len(norms)} Kandidaten")
hits = []
for bn, bv in base.items():
    for nn, nf in norms.items():
        kv = bv / nf
        rel = kv / ks - 1
        if abs(np.log(kv / ks)) <= np.log(np.sqrt(1.2)):
            hits.append((abs(rel), bn, nn, kv, rel, mh_of(kv)))
for h in sorted(hits):
    print(f"  {h[2]:16s} = {h[1]:10s}: kappa = {h[3]:.4f}, Abweichung {100*h[4]:+.2f} %, m_h = {h[5]:.1f} GeV")
ncand = len(base) * len(norms)
lo, hi = min(base.values()) / 4, max(base.values())
span = np.log(hi / lo)
print(f"Kandidaten reichen von {lo:.3f} bis {hi:.3f} (ln-Spanne {span:.2f}).")
for w, label in ((np.log(1.2) , "Fenster ±20 % der Summe"), (2 * 0.05, "±5 % (grobe Genauigkeit der Ein-Schleifen-Formel)"), (2 * 0.003, "±0,3 %")):
    print(f"  erwartete Zufallstreffer bei log-gleichverteilten Kandidaten, {label}: {ncand*w/span:.2f}")
k1 = 1 / c2
print(f"bester Treffer: kappa = 1/cos2θ = (1+mu²)/(1−mu²) = (gamma_L + 1/gamma_L)/2 = {k1:.5f}; Ziel {ks:.5f}; m_h = {mh_of(k1):.2f} GeV")
print(f"  dasselbe mit Tribonacci (1,8393): kappa = {(1.8393+1/1.8393)/2:.4f}, m_h = {mh_of((1.8393+1/1.8393)/2):.1f} GeV; mit Silberzahl (√2+1): kappa = {np.sqrt(2):.4f}, m_h = {mh_of(np.sqrt(2)):.1f} GeV")
print(f"  Empfindlichkeit an gamma_L: gamma_L = 1,86 gibt m_h = {mh_of((1.86+1/1.86)/2):.2f}, 1,87 gibt {mh_of((1.87+1/1.87)/2):.2f} GeV")
print("  Lesart: 1/cos2θ = (a²+b²)/(a²−b²) = Linksladung/Rechtsladung auf der HC-Richtung (k292).")
