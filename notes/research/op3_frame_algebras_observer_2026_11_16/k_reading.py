"""Nachtrag zur Betrachter-Erkundung: K fuer gemischte Auslesungen und Dephasierung um die Zyklusachse.

K in der Gram-Lesart: K = Tr(G^2)/(Tr G)^2.  Fuer reine Zustaende ist Tr(G^2) = Tr(S^2) mit dem Frame-Operator S = sum_k |k><k|;
fuer gemischte Auslesungen ist S = sum_k rho_k die natuerliche Fortsetzung:  K = Tr(S^2)/(Tr S)^2 = (9 + |R|^2)/18,  R = sum_k r_k.
(a) gleichmaessig geschrumpfte Bloch-Vektoren (lam): K = (3 + lam^2)/6 -> K = 2/3 nur bei lam = 1.
(b) Dephasierung im Betrachter-Basis (Achse n = Zyklusachse): Laengsanteil bleibt, Queranteil * kappa.
    Dann R = sum r_k unveraendert -> K = 2/3 fuer jedes kappa; Phase = arctan(kappa^2 / (2 - kappa^2)).
Keine Kandidatenwerte fuer kappa ausgewertet.
"""
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
sig = lambda r: r[0] * X + r[1] * Y + r[2] * Z
n = np.ones(3) / np.sqrt(3)
E = [np.array(v, float) for v in ([0, 0, 1], [1, 0, 0], [0, 1, 0])]


def K_phase(rs):
    rho = [(I2 + sig(r)) / 2 for r in rs]; S = sum(rho)
    return np.trace(S @ S).real / np.trace(S).real ** 2, abs(np.angle(np.trace(rho[0] @ rho[1] @ rho[2])))


print("(a) gleichmaessig geschrumpft:")
for lam in (1.0, 0.9, 0.8):
    K, ph = K_phase([lam * e for e in E]); print(f"    lam = {lam}: K = {K:.6f} (Formel {(3 + lam**2) / 6:.6f}), Phase = {ph:.6f}")
print("(b) Dephasierung um n (Laengsanteil fest, Queranteil * kappa):")
for kap in (1.0, 0.9, 0.8):
    rs = [(e @ n) * n + kap * (e - (e @ n) * n) for e in E]
    K, ph = K_phase(rs); print(f"    kappa = {kap}: K = {K:.6f}, Phase = {ph:.6f}, Formel arctan(k^2/(2-k^2)) = {np.arctan(kap**2 / (2 - kap**2)):.6f}")
t = np.tan(0.666665); k2 = 2 * t / (1 + t)
print(f"    noetig fuer 0.666665: kappa^2 = {k2:.6f}, kappa = {np.sqrt(k2):.6f}")
