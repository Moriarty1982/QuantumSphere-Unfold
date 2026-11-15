"""Erkundung (nicht blind): Koide 2/3 als vollstaendige Komplementaritaet.
Fuer Primzahl-Dimension d liefern die Eigenbasen von Z und X Z^k (k = 0..d-1) einen vollstaendigen Satz von d+1
gegenseitig unverzerrten Basen (Wootters-Fields). Aus jeder Basis ein Zustand: d+1 Zustaende, paarweise Ueberlappung 1/d,
K = (1 + 2/d)/3 im Ueberlappungsbild K = (1 + 2 rho^2)/3 (fuer drei Zustaende) bzw. Tr G^2/(Tr G)^2 allgemein."""
import numpy as np
def mub_states(d):
    w = np.exp(2j*np.pi/d); Z = np.diag(w**np.arange(d)); X = np.roll(np.eye(d), 1, axis=0)
    ops = [Z] + [X @ np.linalg.matrix_power(Z, k) for k in range(d)]
    return [np.linalg.eig(U)[1][:, 0] / np.linalg.norm(np.linalg.eig(U)[1][:, 0]) for U in ops]
for d in (2, 3, 5, 7):
    st = mub_states(d)
    ov = sorted({round(abs(np.vdot(a, b))**2, 9) for i, a in enumerate(st) for b in st[i+1:]})
    G = np.array([[np.vdot(a, b) for b in st] for a in st])
    K = np.trace(G @ G).real / np.trace(G).real**2
    print(f"d = {d}: {len(st)} Basen, paarweise Ueberlappung {ov}, K(Gram) = {K:.6f}, (1+2/d)/3 = {(1+2/d)/3:.6f}, "
          f"Gram-Rang {np.linalg.matrix_rank(G, 1e-9)}")
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
oct3 = [np.linalg.eigh(s)[1][:, 1] for s in (sx, sy, sz)]
B = np.vdot(oct3[0], oct3[1]) * np.vdot(oct3[1], oct3[2]) * np.vdot(oct3[2], oct3[0])
print("Oktant = je ein Eigenzustand von sigma_x, sigma_y, sigma_z: Ueberlappungen",
      [round(abs(np.vdot(oct3[i], oct3[(i+1) % 3]))**2, 6) for i in range(3)], "| Bargmann-Phase/pi", round(abs(np.angle(B))/np.pi, 6))
print("Nur d + 1 = 3 gibt drei Basen: d = 2, Ueberlappung 1/2, K = 2/3.")
