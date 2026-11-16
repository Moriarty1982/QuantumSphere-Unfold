"""OP1: Vorpruefung der Konstruktion "einheitliche Flussauslesung in R" (Erkundung, analytisch, nicht blind).

Konstruktion: eine feste Auslesung in R (Projektor P auf die Extremzustaende |j, +-j> der Achse u, M-Maske); Objekte M und T entstehen aus
demselben Zustand durch die Frame-Abbildungen als Boosts: D_M = exp(eta K), D_T = exp((-eta + i pi/2) K), K Boostgenerator auf der
(j,0)-Darstellung (K = -i J_k fuer eine Achse k).  Gezaehlt wird der Rang des Effekts D^dag P D je Spin j.
Satz (r10.4(c)): D invertierbar und sektorerhaltend -> Rang je Sektor gleich -> M und T zaehlen gleich.  Numerisch fuer j = 1/2 .. 5,
Boost laengs u und quer dazu, eta = 0.6 (Wert ohne Belang).
"""
import numpy as np
from scipy.linalg import expm


def spin_ops(j):
    m = np.arange(j, -j - 1, -1); d = len(m)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    Jx = (Jp + Jp.conj().T) / 2; Jy = (Jp - Jp.conj().T) / 2j
    return Jx, Jy, Jz, m


eta = 0.6
rows = []
for j in np.arange(1, 11) / 2:
    Jx, Jy, Jz, m = spin_ops(j)
    P = np.diag([1.0 if abs(abs(mm) - j) < 1e-12 else 0.0 for mm in m]).astype(complex)
    for axis, J in (("laengs u", Jz), ("quer", Jx)):
        K = -1j * J
        for name, rap in (("M", eta), ("T", -eta + 1j * np.pi / 2)):
            D = expm(rap * K)
            E = D.conj().T @ P @ D
            rank = np.linalg.matrix_rank(E, tol=1e-9)
            comm = np.linalg.norm(D @ (Jx @ Jx + Jy @ Jy + Jz @ Jz) - (Jx @ Jx + Jy @ Jy + Jz @ Jz) @ D)
            rows.append((j, axis, name, rank, comm))
ok = all(r[3] == 2 for r in rows)
print(f"Rang des Effekts je Sektor fuer M und T, j = 1/2 .. 5, Boost laengs und quer: alle = 2: {ok}")
print(f"max. |[D, J^2]| = {max(r[4] for r in rows):.1e} (sektorerhaltend)")
print("Beispiele:", [(float(r[0]), r[1], r[2], r[3]) for r in rows[:4]])
