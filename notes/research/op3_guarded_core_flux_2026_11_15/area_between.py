"""Erkundung: Flaeche zwischen den Kurven A und B aus core_shift.py (Frage des Autors).
Analytisch: phi_A = A_rest/2, phi_B = k A_rest mit A_rest = pi/2 - f*Omega, k = 2 pi/(4 pi - Omega)."""
import json, math
import numpy as np
d = json.load(open("run/core_shift.json", encoding="utf-8"))
G = d["gamma_M"]; rows = d["rows"]
x = np.array([r["deg_from_axis"] for r in rows])[::-1]
A = np.array([r["phiA"] for r in rows])[::-1]; B = np.array([r["phiB"] for r in rows])[::-1]
ratio = B / A
print("Verhaeltnis phi_B/phi_A entlang des Wegs: min", round(ratio.min(), 6), "max", round(ratio.max(), 6),
      " analytisch 4pi/(4pi - gamma_M) =", round(4 * math.pi / (4 * math.pi - G), 6))
area = np.trapezoid(B - A, np.radians(x))
print("Flaeche zwischen den Kurven ueber den Weg (rad * rad):", round(area, 6),
      " = (ratio - 1) * Flaeche unter A:", round((4 * math.pi / (4 * math.pi - G) - 1) * np.trapezoid(A, np.radians(x)), 6))
print("Abfluss-Anteil gamma_M/(4 pi) =", round(G / (4 * math.pi), 6), " = 1 - 1/ratio =", round(1 - (4 * math.pi - G) / (4 * math.pi), 6))
ramp = [r for r in rows if 0 < r["f"] < 1]
lo, hi = min(r["deg_from_axis"] for r in ramp), max(r["deg_from_axis"] for r in ramp)
a = math.degrees(math.acos(1 - G / (2 * math.pi)))
print(f"Rampe (Kern auf der Kante) von {lo} bis {hi} Grad, Breite {hi - lo:.2f} Grad; Kappendurchmesser 2*alpha = {2 * a:.2f} Grad")
print("Rampenhoehe A:", round(rows[0]["phiA"] - rows[-1]["phiA"], 6), "= gamma_M/2 =", round(G / 2, 6),
      "; Rampenhoehe B:", round(rows[0]["phiB"] - rows[-1]["phiB"], 6), "= k*gamma_M =", round(2 * math.pi / (4 * math.pi - G) * G, 6))
# Entartung: Abfluss-Anteil lam des verdraengten Flusses (1 = A, 0 = B) gegen benoetigte Kerngroesse fuer phi = 2/3
from scipy.optimize import brentq
def phi(Om, lam):
    return (math.pi / 2 - Om) * (2 * math.pi - lam * Om / 2) / (4 * math.pi - Om)
print("Abfluss-Anteil lam -> benoetigter Raumwinkel Omega fuer phi = 2/3 (in Einheiten gamma_M):")
for lam in (1.0, 0.75, 0.5, 0.25, 0.0):
    Om = brentq(lambda o: phi(o, lam) - 2 / 3, 0.01, 1.0)
    print(f"   lam = {lam:.2f}: Omega = {Om:.6f} sr = {Om / G:.4f} gamma_M")
