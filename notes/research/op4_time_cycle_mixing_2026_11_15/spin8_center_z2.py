"""OP4: Die Neutrino-Z2 als Zentrumselement von Spin(8) (Erkundung, nicht blind).

(1) Clifford-Algebra Cl(8): die Drehung um 2 pi in einer Ebene ist auf dem Vektor +1, auf den beiden chiralen Spinoren -1;
    auf den drei Trialitaets-Slots (8_v, 8_s, 8_c) also das Vorzeichentripel (1, -1, -1) aus v4.9.0-r38.1(c).
(2) Eine symmetrische Majorana-Matrix mit D M D = M, D = diag(1, -1, -1), entkoppelt Slot 1; in der Flavourbasis der
    geladenen Leptonen (Fourier-Moden) ist die feste Spalte (1,1,1)/sqrt3: TM2, sin^2 theta12 = 1/(3 cos^2 theta13).
(3) Mit der Maske aus r57 (Variante A, wie k97, Lepton-Maske W_l = (0, 0, -3)): welche der drei Z2 (fester Slot p = 1, 2, 3)
    liefert die Treffer? Gleiche Daten, Fenster und Raster wie k97 (Variante A).
"""
import itertools
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

# (1) Cl(8) aus Pauli-Matrizen
sx, sy, sz, I2 = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]), np.eye(2)
def kron(*ms):
    out = np.eye(1)
    for m in ms: out = np.kron(out, m)
    return out
G = []
for k in range(4):
    pre = [sz] * k; post = [I2] * (3 - k)
    G.append(kron(*pre, sx, *post)); G.append(kron(*pre, sy, *post))
G = [g.astype(complex) for g in G]
ok_cl = all(np.allclose(G[a] @ G[b] + G[b] @ G[a], 2 * (a == b) * np.eye(16)) for a in range(8) for b in range(8))
gam9 = np.eye(16, dtype=complex)
for g in G: gam9 = gam9 @ g
Pp, Pm = (np.eye(16) + gam9) / 2, (np.eye(16) - gam9) / 2   # gam9^2 = +1 fuer 8 Generatoren
S12 = G[0] @ G[1] / 2
Rspin = expm(2 * np.pi * S12)                                # Drehung um 2 pi auf Spinoren
L12 = np.zeros((8, 8)); L12[0, 1], L12[1, 0] = -1, 1
Rvec = expm(2 * np.pi * L12)
print(f"(1) Clifford-Relationen: {ok_cl}; Drehung um 2 pi: Vektor {np.allclose(Rvec, np.eye(8))} (+1),"
      f" Spinor 8_s {np.allclose(Pp @ Rspin @ Pp, -Pp)} (-1), Spinor 8_c {np.allclose(Pm @ Rspin @ Pm, -Pm)} (-1)")

# (2) D-invariante Majorana-Matrix -> TM2
w3 = np.exp(2j * np.pi / 3)
F = np.array([[w3 ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
D = np.diag([1., -1, -1]); rng = np.random.default_rng(57); dev = 0
for _ in range(500):
    A = rng.normal(size=(3, 3)); M = (A + A.T) / 2; M = (M + D @ M @ D) / 2
    w, V = np.linalg.eigh(M)
    U = F.conj().T @ V                                        # Flavour (Fourier-Moden) gegen Neutrino-Masse
    col = [k for k in range(3) if np.allclose(abs(V[:, k]), [1, 0, 0])][0]
    dev = max(dev, np.abs(abs(U[:, col]) ** 2 - 1 / 3).max())
print(f"(2) 500 zufaellige D-invariante Majorana-Matrizen: feste Spalte |U|^2 = 1/3 in jeder Zeile (max. Abw. {dev:.1e}) -> TM2")

# (3) Treffer nach festem Slot, Variante A wie k97
Wl = np.array([0., 0., -3.]); TOL = 1e-9
me_ = [0.48307e-3, 101.766e-3, 1728.56e-3]; dm21, dm31 = 7.49e-5, 2.534e-3
R13, R23, J12 = (0.02023, 0.02376), (0.430, 0.596), (0.2918, 0.3266)
PHI = np.deg2rad(np.arange(0, 180, 2))
def sv_sorted(M):
    U, s, Vh = np.linalg.svd(M); o = np.argsort(s); return s[o], U[:, o]
def charged(eps_grid):
    m = np.array(me_) / max(me_); out = {e: [] for e in eps_grid}
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if sg[0] == -1: continue
            lam = np.array([sg[i] * m[p[i]] for i in range(3)])
            for e in eps_grid:
                Mf = lambda x: np.diag(np.exp(e * Wl)) @ (F @ np.diag(x) @ F.conj().T) @ np.diag(np.exp(-e * Wl))
                r = least_squares(lambda x: (sv_sorted(Mf(x))[0] - m) / m, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if np.max(abs(r.fun)) > TOL: break
                lam = r.x; out[e].append(sv_sorted(Mf(lam))[1])
    return {e: np.array(v) for e, v in out.items() if v}
def Qphi(p, phi):
    q, r = [i for i in range(3) if i != p]
    Q = np.zeros((3, 3)); Q[p, 0] = 1
    Q[q, 1], Q[r, 1] = np.cos(phi), np.sin(phi); Q[q, 2], Q[r, 2] = -np.sin(phi), np.cos(phi)
    return Q
def angles(UE, UN):
    a = abs(np.einsum('nji,mjk->nmik', UE.conj(), UN)) ** 2
    s13 = a[..., 0, 2]
    with np.errstate(divide='ignore', invalid='ignore'):
        s12 = a[..., 0, 1] / (1 - s13); s23 = a[..., 1, 2] / (1 - s13)
    return s12, s23, s13
Ce = charged(np.round(np.arange(0, 2.0 + 1e-12, 0.01), 6))
for p in range(3):
    UN = np.array([Qphi(p, phi)[:, list(order)] for phi in PHI for order in itertools.permutations(range(3))])
    nh = 0; eps = []
    for e, UE in Ce.items():
        s12, s23, s13 = angles(UE, UN)
        hit = (s13 >= R13[0]) & (s13 <= R13[1]) & (s23 >= R23[0]) & (s23 <= R23[1]) & (s12 >= J12[0]) & (s12 <= J12[1])
        nh += int(hit.sum())
        if hit.any(): eps.append(e)
    print(f"(3) fester Slot {p + 1} (Maskengewicht {Wl[p]:+.0f}): {nh} Treffer" + (f", eps_e {min(eps)} bis {max(eps)}" if eps else ""))
