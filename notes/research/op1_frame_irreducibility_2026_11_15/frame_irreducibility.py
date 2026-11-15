"""OP1: Wirken die Frame-Abbildungen auf einer Spin-j-Punktierung irreduzibel? (Erkundung, nicht blind)

Annahme (A): Die Frame-Abbildungen R, T, J_B wirken auf dem Dublett chi als halbe Drehungen um drei senkrechte Achsen
(v4.10.0-r16.7: sigma_z, sigma_x, sigma_y bis auf Phase) und auf einer Horizont-Punktierung mit Spin j ueber dieselbe SU(2),
also als exp(-i pi J_k). (A) ist eine Bruecke, nicht hergeleitet.
(1) Fuer j = 1/2 ... 20: Antikommutieren, Kommutant-Dimension, Zerlegung in irreduzible Teile (2-dim. Darstellung der
    Quaternionengruppe bzw. 1-dim. Charaktere), Invarianz des Extremdubletts |j, +-j> und der Paare |j, +-m>.
(2) Regeln: T = "Frame-Abbildungen irreduzibel" -> Spinbereich und Gewicht; M = "invariantes Extremdublett" -> Gewicht 2 je j.
    Gegenproben: T = "antikommutierend" (Kramers), M = "irreduzibel", M = "alle invarianten Paare" (SU(2)-Gewicht).
(3) gamma aus sum_j g(j) exp(-2 pi gamma sqrt(j(j+1))) = 1, j bis 2000; gamma_L, beta_sym = tanh(arccosh(gamma_L)/2).
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def spin(j):
    m = np.arange(j, -j - 1, -1); d = len(m)
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return (Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)


def commutant_dim(gens, d):
    M = np.vstack([np.kron(np.eye(d), G) - np.kron(G.T, np.eye(d)) for G in gens])
    return d * d - np.linalg.matrix_rank(M, 1e-8)


print("(1) Frame-Abbildungen exp(-i pi J_k) auf Spin j")
irreducible = []
for j2 in range(1, 41):
    j = j2 / 2; d = j2 + 1
    Jx, Jy, Jz = spin(j)
    X, Y, Z = (expm(-1j * np.pi * J) for J in (Jx, Jy, Jz))
    anti = np.allclose(X @ Y, -Y @ X)
    cd = commutant_dim([X, Y], d)
    # Zerlegung: halbzahlig -> d/2 Kopien der 2-dim. Darstellung (Kommutant d^2/4); ganzzahlig -> Charaktere
    if anti:
        parts = f"{d // 2} x (2-dim.)"; expect = (d // 2) ** 2
    else:
        # Vielfachheiten der vier Charaktere aus den Spuren
        chars = []
        for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            chars.append(round(np.real(np.trace(np.eye(d) + sx * X + sy * Y + sx * sy * (X @ Y))) / 4))
        parts = "Charaktere " + "+".join(map(str, chars)); expect = sum(c * c for c in chars)
    P = np.zeros((d, d)); P[0, 0] = P[-1, -1] = 1
    ext = all(np.allclose(P @ G @ P, G @ P) for G in (X, Y, Z))
    pairs = 0
    for k in range((d + 1) // 2):
        Q = np.zeros((d, d)); Q[k, k] = Q[d - 1 - k, d - 1 - k] = 1
        pairs += all(np.allclose(Q @ G @ Q, G @ Q) for G in (X, Y, Z))
    if cd == 1: irreducible.append(j)
    if j <= 4 or j2 % 10 == 0:
        print(f"    j = {j:4.1f}: antikommutierend {anti!s:5}, Kommutant {cd:4d} (erwartet {expect:4d}), {parts:20s},"
              f" Extremdublett invariant {ext}, invariante Paare |j,+-m>: {pairs}")
print(f"    irreduzibel nur bei j = {irreducible}")


def gamma(spins, weight):
    f = lambda g: sum(weight(j) * np.exp(-2 * np.pi * g * np.sqrt(j * (j + 1))) for j in spins) - 1
    return brentq(f, 1e-4, 5)


ALL = [k / 2 for k in range(1, 4001)]
HALF = [k / 2 for k in range(1, 4001, 2)]
rules = {
    "M: Extremdublett je j (alle j, Gewicht 2)": (ALL, lambda j: 2),
    "M: alle invarianten Paare (alle j, Gewicht 2j+1)": (ALL, lambda j: 2 * j + 1),
    "M: irreduzibel (nur j = 1/2, Gewicht 2)": ([0.5], lambda j: 2),
    "T: irreduzibel (nur j = 1/2, Gewicht 2)": ([0.5], lambda j: 2),
    "T: antikommutierend (halbzahlig, Gewicht 2)": (HALF, lambda j: 2),
}
g = {k: gamma(*v) for k, v in rules.items()}
print("\n(2)/(3) Regeln und gamma")
for k, v in g.items():
    print(f"    {k:50s} gamma = {v:.6f}")
pairs = [("M: Extremdublett je j (alle j, Gewicht 2)", "T: irreduzibel (nur j = 1/2, Gewicht 2)"),
         ("M: Extremdublett je j (alle j, Gewicht 2)", "T: antikommutierend (halbzahlig, Gewicht 2)"),
         ("M: alle invarianten Paare (alle j, Gewicht 2j+1)", "T: irreduzibel (nur j = 1/2, Gewicht 2)"),
         ("M: irreduzibel (nur j = 1/2, Gewicht 2)", "T: irreduzibel (nur j = 1/2, Gewicht 2)")]
for a, b in pairs:
    gl = g[a] / g[b]
    beta = np.tanh(np.arccosh(gl) / 2) if gl >= 1 else float("nan")
    print(f"    {a.split(' (')[0]:28s} / {b.split(' (')[0]:22s}: gamma_L = {gl:.6f}, beta_sym = {beta:.5f}")
print("    Vergleich: H98-Paar gamma_L = 1.864700, beta = 0.54941; Leptonfenster beta in [0.545, 0.570]")
