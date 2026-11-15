"""OP4: Ist der Dreierzyklus der Dirac-Auslesung (v4.9.0-r55) der Zeitzyklus aus v4.10.0-r16.9? (Erkundung, nicht blind)

Harmonische Basis (s+, w, conj s-) mit Zeitverschiebung um ein Drittel der Periode U = diag(w^-1, 1, w), w = e^{2 pi i/3}.
Slotbasis e_1, e_2, e_3 mit zyklischer Verschiebung tau (r55: Dirac-Kopplungen zirkulant, invariant unter tau).
(1) Die Fourier-Matrix F verbindet beide: F tau F^dagger = U (bis auf Reihenfolge); die Slotzustaende sind die drei
    gleich gewichteten Auslesungen zu den Zeiten 0, T/3, 2T/3; die harmonischen Zustaende die Masseneigenzustaende.
(2) Wie wirkt die Frame-Abbildung T (B -> -B; auf S: s+ <-> conj s-, komplex konjugiert) auf den Slotzustaenden?
    Erwartung vor dem Lauf: Transposition rho. Ergebnis siehe Ausgabe.
(3) Kandidaten fuer die Neutrino-Z2 (r55: G_M) und ihre feste Spalte in der Flavourbasis (= harmonische Basis):
    A4-Vorzeichen diag(1,-1,-1) (r55, TM2) gegen die Zeitumkehr-Transposition rho (r38).
"""
import numpy as np

w = np.exp(2j * np.pi / 3)
F = np.array([[w ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)   # Spalte k: Fourier-Mode k in Slotbasis
tau = np.roll(np.eye(3), 1, axis=0)                                               # e_k -> e_{k+1}
Ud = F.conj().T @ tau @ F
print("(1) F^dagger tau F =", np.round(np.diag(Ud), 6), "(diagonal:", np.allclose(Ud, np.diag(np.diag(Ud))), ")")
print("    Eigenwerte {1, w, w^-1} wie U = diag(w^-1, 1, w) auf (s+, w, conj s-): Zeitzyklus und tau sind gleichwertig")
H = F.conj().T                                                                    # Slot -> harmonische Koordinaten
for k in range(3):
    e = np.eye(3)[k]
    print(f"    Slotzustand e_{k+1} in harmonischen Koordinaten: |Komponenten|^2 = {np.round(abs(H @ e)**2, 4)}"
          f" (gleich gewichtete Auslesung)")

# (2) Zeitumkehr auf harmonischen Koordinaten (Reihenfolge Moden k = 0, 1, 2 <-> w, conj s-, s+):
#     T tauscht die Moden k = 1 und k = 2 und konjugiert; wirkt auf Slotzustaenden?
def T_harm(x):
    y = np.conj(x).copy(); y[1], y[2] = np.conj(x[2]), np.conj(x[1]); return y
for k in range(3):
    e = np.eye(3)[k].astype(complex)
    img = F @ T_harm(H @ e)
    tgt = [j for j in range(3) if abs(abs(img[j]) - 1) < 1e-12]
    print(f"(2) Frame-Abbildung T: e_{k+1} -> e_{tgt[0]+1}" if tgt else f"(2) e_{k+1}: kein Slotzustand")

def fixed_column(Z):
    """Eigenvektor von Z zum nicht entarteten Eigenwert, in harmonischen (Flavour-)Koordinaten."""
    vals, vecs = np.linalg.eigh(Z)
    for i, v in enumerate(vals):
        if np.sum(np.isclose(vals, v)) == 1:
            return v, H @ vecs[:, i]
    return None, None

print("(3) Neutrino-Z2-Kandidaten: feste Spalte |U_ai|^2 in der Flavourbasis")
cands = {"A4-Vorzeichen diag(1,-1,-1) (r55)": np.diag([1., -1, -1]),
         "Transposition rho (r38, kein Frame-Bild)": np.array([[1., 0, 0], [0, 0, 1], [0, 1, 0]])}
for name, Z in cands.items():
    v, col = fixed_column(Z)
    print(f"    {name}: Eigenwert {v:+.0f}, |Spalte|^2 = {np.round(abs(col)**2, 4)}")
s13 = 0.02215
print(f"    TM2 (Spalte (1,1,1)/sqrt3): sin^2 theta12 = 1/(3 cos^2 theta13) = {1/(3*(1-s13)):.4f}; JUNO 0.3092 +- 0.0087")
print("    rho (Spalte mit |U_e|^2 = 0 in einer Zeile): theta13 = 0 oder theta12 extrem, vgl. H6 (v4.8.0-r12)")
