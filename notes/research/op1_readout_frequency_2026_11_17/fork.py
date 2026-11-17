"""Gabel weiter: Ist die Aussage "M liest mit der Quasinormal-Frequenz aus" vom Flaechenspektrum unabhaengig?  (Erkundung, nicht blind.)

Fuer jedes Spektrum a(j): T (nur j = 1/2, Gewicht 2) hat kleinstes Quant 8 pi gamma_T a(1/2) = 4 ln 2 (aus 2 e^{-2 pi gamma_T a(1/2)} = 1).
M (alle j, Gewicht 2): kleinstes Quant 8 pi gamma_M a(1/2).  Verhaeltnis = gamma_M/gamma_T = gamma_L.  Bohr: omega = Delta A T_H / 4 (T_H = 1/(8 pi M)).
Also omega_M / omega_T = gamma_L und omega_M = gamma_L ln2 T_H.  QNM-Bedingung omega_M = ln3 T_H  <=>  gamma_L = log2 3, fuer jedes Spektrum.
Geprueft an mehreren Spektren; dazu, welches Spektrum die QNM-Bedingung erfuellt (M-Quant = 4 ln3).
"""
import numpy as np
from scipy.optimize import brentq

js = np.arange(1, 6001) / 2
specs = {"sqrt(j(j+1))": lambda j: np.sqrt(j * (j + 1)), "j": lambda j: j, "j+1/2": lambda j: j + 0.5,
         "sqrt(j(j+1)+1/4)": lambda j: np.sqrt(j * (j + 1) + 0.25), "j^0.8 (Testform)": lambda j: j ** 0.8}


def gam(weights, a):
    return brentq(lambda g: np.sum(weights * np.exp(-2 * np.pi * g * a)) - 1, 1e-5, 10)


print("Spektrum | gamma_M | gamma_T | gamma_L | Quant M | Quant T | omega_M/T_H | QNM-Bedingung (Quant M = 4 ln3)")
for n, f in specs.items():
    a = f(js)
    gM = gam(2 * np.ones_like(js), a); gT = np.log(2) / (2 * np.pi * f(0.5))
    qM, qT = 8 * np.pi * gM * f(0.5), 8 * np.pi * gT * f(0.5)
    print(f"{n:18s} | {gM:.6f} | {gT:.6f} | {gM/gT:.6f} | {qM:.4f} | {qT:.4f} | {qM/4:.6f} | {'erfuellt' if abs(qM - 4*np.log(3)) < 1e-6 else 'nein'}")
print(f"log2(3) = {np.log2(3):.6f};  ln3 = {np.log(3):.6f};  Datenpaarung H98: gamma_L = 1.864700 -> omega_M/T_H = gamma_L ln2 = {1.8647*np.log(2):.6f}")
# Identitaet: Anteil der j = 1/2-Punktierungen in der M-Zaehlung = 2 e^{-2 pi gamma_M a(1/2)} = 2^{1 - gamma_L}
a = specs["sqrt(j(j+1))"](js); gM = gam(2 * np.ones_like(js), a)
p_half = 2 * np.exp(-2 * np.pi * gM * a[0])
print(f"Anteil j = 1/2 in der M-Zaehlung (sqrt): {p_half:.6f} = 2^(1-gamma_L) = {2**(1-1.8647):.6f};  beta_sym = 0.549406 (nachtraeglich gesehen, Abweichung {abs(p_half-0.549406):.1e}, nicht exakt)")
