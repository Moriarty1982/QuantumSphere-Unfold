"""Erkundung (nicht blind): das Spin-1-Dreieck und die Rueckwaertssuche nach seiner Bezugsrichtung.
Teil A (exakt, sympy): drei koharente Spin-1-Zustaende, symmetrisch um die Zyklusachse, mit paarweiser Ueberlappung 1/2.
Teil B: Die Kandidatenliste nativer Richtungen und Winkel ist im Code festgelegt, bevor das Ergebnis ausgegeben wird.
Toleranz 0,05 Grad; Zufallserwartung = Zahl der Kandidaten * 0,1 / 90.
Aufruf: python spin1_triangle.py"""
import itertools, math
import numpy as np
import sympy as sp

# ---------- Teil A: exakt ----------
c = sp.sqrt(2) - 1                                   # Kosinus des Seitenwinkels
overlap = ((1 + c) / 2) ** 2                          # Spin 1: |<n|n'>|^2 = cos^4(a/2) = ((1+cos a)/2)^2
cos2psi = sp.nsimplify((1 + 2 * c) / 3)              # Kosinus^2 des Winkels zur Zyklusachse
A = sp.acos(c / (1 + c))
phi = 3 * A - sp.pi                                   # Raumwinkel des gleichseitigen Dreiecks; Ladung 1
print("A1 Ueberlappung:", sp.simplify(overlap), "| K = (1+2*1/2)/3 = 2/3")
print("A2 cos^2(psi) =", sp.simplify(cos2psi), "=", float(cos2psi), "-> psi =", round(math.degrees(math.acos(math.sqrt(float(cos2psi)))), 4), "Grad")
print("A3 Phase = 3*arccos(1 - 1/sqrt2) - pi:", sp.simplify(sp.cos(A) - (1 - 1/sp.sqrt(2))) == 0, "=", float(phi))
# Gram-Determinante fuer Ueberlappung 1/2 und Phase phi: (sqrt2 cos phi - 1)/2 > 0
print("A4 det G =", float((sp.sqrt(2) * sp.cos(phi) - 1) / 2), "> 0 (Rang 3)")
TARGET = math.degrees(math.acos(math.sqrt(float(cos2psi))))

# ---------- Teil B: Kandidaten (vorab festgelegt) ----------
cands = {}
diag = np.ones(3) / math.sqrt(3)
for v in itertools.product(range(-2, 3), repeat=3):          # Richtungen mit Eintraegen in {-2..2}
    v = np.array(v, float)
    if not v.any():
        continue
    ang = math.degrees(math.acos(min(1, abs(v @ diag) / np.linalg.norm(v))))
    cands.setdefault(f"Gitterrichtung {tuple(int(x) for x in v)} zur Diagonale", ang)
for name, c2 in (("Delta(96)-Spalte 1/3", 1/3), ("Delta(96)-Spalte (2-sqrt3)/6", (2 - math.sqrt(3))/6),
                 ("Delta(96)-Spalte (2+sqrt3)/6", (2 + math.sqrt(3))/6), ("Fourier <e0|F|e0>^2 = 1/3", 1/3),
                 ("Ueberlappung 1/2 als cos^2", 0.5), ("beta_sym^2 als cos^2", 0.301847), ("2/3 als cos^2", 2/3)):
    cands[name] = math.degrees(math.acos(math.sqrt(c2)))
beta = 0.549406; thH = 2 * math.degrees(math.asin(beta))
for name, deg in (("Hopf-Winkel theta_H", thH), ("theta_H/2", thH / 2), ("arctan beta_sym", math.degrees(math.atan(beta))),
                  ("arccos beta_sym", math.degrees(math.acos(beta))), ("pi/12", 15.0), ("pi/6", 30.0), ("pi/4", 45.0),
                  ("2/3 rad", math.degrees(2/3)), ("2/9 rad", math.degrees(2/9)), ("gamma_M rad", math.degrees(0.237533)),
                  ("magischer Winkel", math.degrees(math.acos(1/math.sqrt(3)))), ("Seitenwinkel Spin-1 (65,53) / 2", math.degrees(math.acos(math.sqrt(2) - 1)) / 2)):
    cands[name] = deg
n = len(cands)
print(f"\nB Ziel psi = {TARGET:.4f} Grad; {n} Kandidaten; Zufallserwartung bei +-0,05 Grad: {n*0.1/90:.3f}")
near = sorted(cands.items(), key=lambda kv: abs(kv[1] - TARGET))[:8]
for name, deg in near:
    print(f"   {deg:9.4f} Grad  (Abstand {deg - TARGET:+.4f})  {name}")
hits = [k for k, d in cands.items() if abs(d - TARGET) <= 0.05]
print("Treffer innerhalb 0,05 Grad:", hits if hits else "keiner")
