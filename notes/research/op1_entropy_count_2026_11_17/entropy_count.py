"""Folgt die Zaehlung je Frame aus der Register-Entropie?  (Erkundung, nicht blind: gamma_M = 0,2375 und die Gewichte sind bekannt.)

Modell: Eine Punktierung mit Spin j besteht aus 2j Straengen (r17.5, (S1)); jeder Strang ist ein chi-Qubit im Registerzustand des Frames
rho(b) = (1 + b sigma_z)/2 (Konvention F: R b = 1, M b = |b_M| = 0,5363, P b = 0).  Das Buendel liegt im symmetrischen Unterraum (Spin j);
die Gewichte der m-Zustaende im symmetrischen Teil sind w_m ~ p+^(j+m) p-^(j-m) (Dicke-Zustaende, kein Binomialfaktor), also geometrisch mit
Quotient x = p-/p+ = beta^2.  Fuer j -> unendlich: Beteiligung 1/sum w^2 -> (1+x)/(1-x) = gamma (Frame-Faktor, algebraische Identitaet).
Effektive Zustandszahl je Punktierung: N_eff = 2^H (Shannon) und 1/sum w^2 (Beteiligung).
Vergleich mit den Zaehlgewichten: T 2 nur bei j = 1/2; M 2 je j; P 2j+1.
Zusaetzlich: die +-Mischung (beide Ports, rho+ und sein J_B-Spiegel) und die daraus folgenden gamma-Werte.
"""
import numpy as np
from math import comb
from scipy.optimize import brentq

bM = (1 - 0.549406 ** 2) / (1 + 0.549406 ** 2)


def weights(j, b):
    n = int(round(2 * j)); pp, pm = (1 + b) / 2, (1 - b) / 2
    # Gewicht des Dicke-Zustands |j, m> unter rho^(x n): <D_k| rho^(x n) |D_k> = pp^k pm^(n-k)  (kein Binomialfaktor), k = j + m
    w = np.array([pp ** k * pm ** (n - k) for k in range(n + 1)])
    return w / w.sum()


def neff(w):
    w = w[w > 1e-300]
    return 2 ** (-np.sum(w * np.log2(w))), 1 / np.sum(w ** 2)


print(f"Register-Sichtbarkeit M: b = {bM:.4f}")
print("j | R (b=1) N_Shannon | M (b=0,536) N_Shannon, N_Beteiligung | P (b=0) N_Shannon | Zaehlgewichte M / P")
for j in (0.5, 1, 1.5, 2, 3, 5, 10):
    nR = neff(weights(j, 1.0))[0]; nM = neff(weights(j, bM)); nP = neff(weights(j, 0.0))[0]
    print(f"{j:4} | {nR:.3f} | {nM[0]:.3f}, {nM[1]:.3f} | {nP:.3f} | 2 / {int(2*j+1)}")


def mix_pm(j, b):
    """Gleichgewichtete Mischung aus rho(b) und dem Spiegel rho(-b) (beide Ports)."""
    return 0.5 * (weights(j, b) + weights(j, b)[::-1])


print("+-Mischung (beide Ports): N_Shannon je j fuer b = 1 (reiner Fall) und b = b_M")
for j in (0.5, 1, 2, 5):
    print(f"   j = {j}: b = 1: {neff(mix_pm(j, 1.0))[0]:.3f}   b = b_M: {neff(mix_pm(j, bM))[0]:.3f}")
js = np.arange(1, 400) / 2; a = np.sqrt(js * (js + 1))


def gam(g):
    return brentq(lambda x: np.sum(g * np.exp(-2 * np.pi * x * a)) - 1, 0.01, 3)


gM_entropy = np.array([neff(weights(j, bM))[0] for j in js])
gPM_pure = np.array([neff(mix_pm(j, 1.0))[0] for j in js])
print(f"gamma mit N_Shannon aus rho_M: {gam(gM_entropy):.6f} (Regel M: 0,237533)")
print(f"gamma mit N_Shannon aus rho_P (= 2j+1): {gam(np.array([neff(weights(j, 0.0))[0] for j in js])):.6f} (Vorschlag P: 0,274067)")
print(f"gamma mit +-Mischung reiner Zustaende (= 2 je j): {gam(gPM_pure):.6f}")
print(f"Bits je Punktierung: M-Regel 1 bit fuer jedes j; P-Regel log2(2j+1); Register-Entropie je Strang M {-(0.5*(1+bM))*np.log2(0.5*(1+bM))-(0.5*(1-bM))*np.log2(0.5*(1-bM)):.4f} bit, P 1 bit")
