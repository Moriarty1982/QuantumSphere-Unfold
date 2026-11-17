"""OP1: Mit welcher Frequenz liest M aus?  Quasinormal-Frequenz (Hod/Dreyer) gegen die Zaehlregeln je Frame.  (Erkundung, nicht blind.)

Dreyer (gr-qc/0211076): Bohr-Korrespondenz, Delta M = hbar omega_QNM = hbar ln3/(8 pi M), A = 16 pi M^2 -> Delta A = 4 ln3 (l_P = 1).
Geprueft: Welche Regel (Spektrum sqrt(j(j+1)) oder linear j; Gewicht 2 oder 2j+1; Spins alle oder nur j = 1/2) hat ein kleinstes
Flaechenquant 8 pi gamma a(j_min) = 4 ln3?  Dazu gamma_L = gamma_M/gamma_T und beta^2 = (gamma_L-1)/(gamma_L+1) je Spektrum.
"""
import numpy as np
from scipy.optimize import brentq

js = np.arange(1, 4001) / 2
spec = {"sqrt": lambda j: np.sqrt(j * (j + 1)), "linear": lambda j: j}


def gam(weights, a):
    return brentq(lambda g: np.sum(weights * np.exp(-2 * np.pi * g * a)) - 1, 1e-4, 5)


dA_qnm = 4 * np.log(3)
print(f"Dreyer: Delta A = 4 ln3 = {dA_qnm:.6f}")
res = {}
for sn, f in spec.items():
    a = f(js)
    rules = {"M (alle j, Gewicht 2)": gam(2 * np.ones_like(js), a),
             "P (alle j, Gewicht 2j+1)": gam(2 * js + 1, a),
             "T (nur j = 1/2, Gewicht 2)": np.log(2) / (2 * np.pi * f(0.5))}
    for rn, g in rules.items():
        dA = 8 * np.pi * g * f(0.5)
        res[(sn, rn)] = g
        print(f"  {sn:6s} {rn:28s} gamma = {g:.6f}  kleinstes Quant 8 pi gamma a(1/2) = {dA:.6f}  {'= 4 ln3' if abs(dA - dA_qnm) < 1e-6 else ''}")
    gL = rules["M (alle j, Gewicht 2)"] / rules["T (nur j = 1/2, Gewicht 2)"]
    print(f"  {sn:6s} gamma_L = gamma_M/gamma_T = {gL:.6f}, beta^2 = Omega_M = {(gL - 1) / (gL + 1):.4f}")
print(f"ln3/pi = {np.log(3)/np.pi:.6f}, ln2/pi = {np.log(2)/np.pi:.6f}, log2(3) = {np.log2(3):.6f}")
# Dreyer-Werte zum Vergleich
for jm in (0.5, 1.0):
    print(f"Dreyer gamma(j_min = {jm}) = ln3/(2 pi sqrt(j(j+1))) = {np.log(3) / (2 * np.pi * np.sqrt(jm * (jm + 1))):.6f}")
# Geometrische Lesart der linearen M-Regel: x = exp(-pi gamma) je Halbschritt
x = np.exp(-np.pi * np.log(3) / np.pi)
print(f"lineare M-Regel: Gewicht je Halbschritt x = e^(-pi gamma) = {x:.6f} (= 1/3); 2x/(1-x) = {2*x/(1-x):.6f}")
