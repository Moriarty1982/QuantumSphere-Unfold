"""k256 (Erkundung, nicht blind): Welche Mischungsmatrizen erlaubt die S3 der Kopien als Restsymmetrie?
Kopienbasis g_k (k255). Geladene Leptonen mit Z3 (psi) -> zirkulante Massenmatrix, U_e = DFT.
Neutrinos mit Z2 (Spiegelung, die Kopie 0 festhaelt: Tausch g1 <-> g2) oder Z3 oder gar nichts.
U = U_e^dagger U_nu; Ausgabe |U_ij|^2, sin^2 theta_13, sin^2 theta_12, sin^2 theta_23 und erhaltene Spalten."""
import numpy as np
w = np.exp(2j * np.pi / 3)
F = np.array([[w ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)  # Eigenbasis jeder zirkulanten Matrix
def angles(U):
    P = np.abs(U) ** 2
    s13 = P[0, 2]; s12 = P[0, 1] / (1 - s13) if s13 < 1 else np.nan; s23 = P[1, 2] / (1 - s13) if s13 < 1 else np.nan
    return s13, s12, s23
print("Kopienbasis-Vektoren der Standardspalten (V_w-Koordinaten 1, w f1, w f2):")
a, b = 1 / np.sqrt(3), np.sqrt(2 / 3); th = [0, 2 * np.pi / 3, 4 * np.pi / 3]
G = np.array([[a, b * np.cos(t), b * np.sin(t)] for t in th])  # Zeilen g_k
for name, c in {"(1,1,1)/sqrt3 [TM2-Spalte]": np.ones(3) / np.sqrt(3), "(2,-1,-1)/sqrt6 [TM1-Spalte]": np.array([2, -1, -1]) / np.sqrt(6),
                "(0,1,-1)/sqrt2": np.array([0, 1, -1]) / np.sqrt(2)}.items():
    print(f"  {name}: Zustand = {np.round(c @ G, 6)}")
print("(a) beide Sektoren Z3 (zirkulant): U = F^dagger F =", np.round(np.abs(F.conj().T @ F) ** 2, 6).tolist())
print("(b) Leptonen Kopienbasis, Neutrinos Z3: |U|^2 =", np.round(np.abs(F) ** 2, 6).tolist(), "(trimaximal, vgl. H39a)")
print("(c) Leptonen Z3 (U_e = F), Neutrinos Z2 = Tausch g1<->g2, freier Winkel phi im festen 2D-Raum:")
for phi in np.deg2rad([0, 20, 35.26, 45, 70, 90]):
    v3 = np.array([0, 1, -1]) / np.sqrt(2)
    v1 = np.cos(phi) * np.array([1, 0, 0]) + np.sin(phi) * np.array([0, 1, 1]) / np.sqrt(2)
    v2 = -np.sin(phi) * np.array([1, 0, 0]) + np.cos(phi) * np.array([0, 1, 1]) / np.sqrt(2)
    U = F.conj().T @ np.column_stack([v1, v2, v3])
    P = np.abs(U) ** 2
    # beste Spaltenreihenfolge nach kleinstem |U_e3|^2
    best = min(((P[0, k], k) for k in range(3)))
    print(f"   phi={np.rad2deg(phi):6.2f}: Spalte (0,1,-1)/sqrt2 -> |U_ei|^2 = {np.round(P[:, 2], 4).tolist()}; min_k |U_ek|^2 = {best[0]:.4f}")
print("(d) Leptonen Z3, Neutrinos mit erhaltener Spalte = reelle Eins (1,1,1)/sqrt3: |F^dag (1,1,1)/sqrt3|^2 =",
      np.round(np.abs(F.conj().T @ (np.ones(3) / np.sqrt(3))) ** 2, 6).tolist())
print("    erhaltene Spalte = imaginaere Kopienachse (2,-1,-1)/sqrt6: |F^dag c|^2 =",
      np.round(np.abs(F.conj().T @ (np.array([2, -1, -1]) / np.sqrt(6))) ** 2, 6).tolist())
print("(e) Welche Z2 erhaelt welche Spalte? Koordinaten (1, w f0, w f0_perp) auf V_w; Flavourbasis = Kopienbasis (Koide-Amplituden):")
K = np.diag([1, -1, -1])          # Oktonion-Konjugation x -> x* auf V_w
S0 = np.diag([1, 1, -1])          # S3-Spiegelung, die Kopie 0 festhaelt (f0 fest, f0_perp -> -f0_perp)
Gc = np.array([[a, b, 0], [a, b * np.cos(th[1]), b * np.sin(th[1])], [a, b * np.cos(th[2]), b * np.sin(th[2])]])  # Zeilen g_k in (1, wf0, wf0perp)
for name, Z in {"Spiegelung S0": S0, "Konjugation K": K, "K * S0": K @ S0}.items():
    ev, V = np.linalg.eigh(Z)
    minus = V[:, np.isclose(ev, -1)]
    cols = [np.round(Gc @ minus[:, i], 6).tolist() for i in range(minus.shape[1])]
    print(f"   {name}: Eigenwert -1 hat Dimension {minus.shape[1]}; als Spalte in Kopienbasis: {cols}")
