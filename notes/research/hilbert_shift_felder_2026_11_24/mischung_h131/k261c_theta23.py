"""k261c (nach dem Test H131, nachtraeglich): Was legt die Klasse 'TM2 mit J = 0' fuer theta23 fest?
Parametrisierung TM2 mit reeller Drehung: U = U_TBM . R13(t), sin^2(theta13) = (2/3) sin^2(t). Vergleich mit Stichproben aus k261 (Vertreter T, S, X1).
Aufruf: python3 k261c_theta23.py"""
import numpy as np
rng = np.random.default_rng(2611)
Utbm = np.array([[np.sqrt(2 / 3), 1 / np.sqrt(3), 0], [-1 / np.sqrt(6), 1 / np.sqrt(3), 1 / np.sqrt(2)], [1 / np.sqrt(6), -1 / np.sqrt(3), 1 / np.sqrt(2)]])
def obs(t):
    c, s = np.cos(t), np.sin(t); U = Utbm @ np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]]); P = U ** 2
    return P[0, 2], P[0, 1] / (1 - P[0, 2]), P[1, 2] / (1 - P[0, 2])
for s13sq in (0.0215, 0.0220, 0.0225):
    t = np.arcsin(np.sqrt(1.5 * s13sq))
    a, b = obs(t), obs(-t)
    print(f"sin^2(theta13) = {s13sq}: sin^2(theta12) = {a[1]:.4f}; sin^2(theta23) = {a[2]:.4f} (t > 0) oder {b[2]:.4f} (t < 0); delta = 0 oder 180 Grad, J = 0")
# Stichprobe: allgemeine Loesung aus k261b (Wolfram): m = [[a,0,0],[0,e+i e2,f],[0,f,e-i e2]], H_e zyklisch
w = np.exp(2j * np.pi / 3); F = np.array([[1, 1, 1], [1, w, w * w], [1, w * w, w]]).T / np.sqrt(3)
worst = 0.0; n = 0
for _ in range(2000):
    a, e, e2, f = rng.normal(size=4); m = np.array([[a, 0, 0], [0, e + 1j * e2, f], [0, f, e - 1j * e2]])
    wn, Un = np.linalg.eigh(m.conj().T @ m); U = F.conj().T @ Un; P = np.abs(U) ** 2
    c2 = int(np.argmin([np.abs(P[:, c] - 1 / 3).max() for c in range(3)]))
    for c3 in [c for c in range(3) if c != c2]:
        for er in range(3):
            s13 = P[er, c3]
            if s13 > 0.2: continue
            t = np.arcsin(np.sqrt(1.5 * s13)); cand = [obs(t)[2], obs(-t)[2]]
            for mu in [r for r in range(3) if r != er]:
                s23 = P[mu, c3] / (1 - s13); worst = max(worst, min(abs(s23 - x) for x in cand)); n += 1
print(f"Stichprobe: {n} Zuordnungen mit sin^2(theta13) < 0.2; groesste Abweichung von der Formel {worst:.1e}")
