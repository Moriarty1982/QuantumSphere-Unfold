"""Erkundung: Eichung der U(3) auf dem Platzindex (13.11.2026, nicht blind).

Feld: X = [x_1 x_2 x_3], Spalten = Plaetze in einem Zustandsraum V (hier C^n), Gram-Matrix S = X^dagger X.
Platzindex-U(3): X -> X U.  Eichung: D X = dX - i g X A, A = A^alpha T^alpha (u(3)).
Massenterm der Eichbosonen aus tr (DX)^dagger (DX):  g^2 tr(A S A) = g^2 A^a A^b tr(T^a S T^b).
Geprueft: (1) Invarianz der Gram-Eigenwerte unter X -> X U und unter unitaeren Wirkungen auf V;
(2) Bosonenmassen fuer S = diag(s): Diagonal-Bosonen ~ s_i, Nebendiagonal-Paare ~ (s_i + s_j)/2;
(3) Vergleich mit Sumino (M_ij^2 ~ m_i + m_j) fuer zwei Auslesungen.
Aufruf: python op3_slot_u3_gauging_2026_11_13.py
"""
import numpy as np

rng = np.random.default_rng(20261113)
POL = np.array([0.51099895, 105.6583755, 1776.93])


def u3_generators():
    """Orthonormal bzgl. tr(T^a T^b) = delta/2: 8 Gell-Mann/2 und 1/sqrt(6)."""
    T = []
    for i in range(3):
        for j in range(i + 1, 3):
            E = np.zeros((3, 3), complex); E[i, j] = E[j, i] = 0.5; T.append(E)
            E = np.zeros((3, 3), complex); E[i, j] = -0.5j; E[j, i] = 0.5j; T.append(E)
    T.append(np.diag([0.5, -0.5, 0]).astype(complex))
    T.append(np.diag([1, 1, -2]).astype(complex) / (2 * np.sqrt(3)))
    T.append(np.eye(3, dtype=complex) / np.sqrt(6))
    return T


def boson_mass2(S, g=1.0):
    T = u3_generators()
    M = np.array([[2 * g ** 2 * np.real(np.trace(a @ S @ b)) for b in T] for a in T])
    M = (M + M.T) / 2
    return np.sort(np.linalg.eigvalsh(M))


def rand_unitary(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))


if __name__ == "__main__":
    n = 8
    X = rng.normal(size=(n, 3)) + 1j * rng.normal(size=(n, 3))
    S = X.conj().T @ X
    ev = np.linalg.eigvalsh(S)
    U3, W = rand_unitary(3), rand_unitary(n)
    print("(1) Invarianz der Gram-Eigenwerte:",
          f"X->XU {np.abs(np.linalg.eigvalsh((X @ U3).conj().T @ (X @ U3)) - ev).max():.1e},",
          f"X->WX {np.abs(np.linalg.eigvalsh((W @ X).conj().T @ (W @ X)) - ev).max():.1e}")
    # Bosonenmassen allgemein = Funktion der Eigenwerte (Kovarianz)
    s = ev
    expect = sorted([s[0], s[1], s[2]] + [(s[i] + s[j]) / 2 for i in range(3) for j in range(i + 1, 3) for _ in (0, 1)])
    got = boson_mass2(S)
    print("(2) Bosonenmassen^2 (g = 1):", np.round(got, 4))
    print("    erwartet {s_i} und je zweimal (s_i+s_j)/2:", np.round(expect, 4),
          f"Abweichung {np.abs(np.array(expect) - got).max():.1e}")
    print("    Diagonal-Bosonen massiv (kein masseloses Cartan-Boson):", got.min() > 0)
    # adjungiertes Feld S -> U^dagger S U zum Vergleich: Cartan-Bosonen masselos
    Tg = u3_generators()
    Madj = np.array([[np.real(np.trace((a @ np.diag(s) - np.diag(s) @ a).conj().T @ (b @ np.diag(s) - np.diag(s) @ b)))
                      for b in Tg] for a in Tg])
    print("    zum Vergleich S adjungiert: Zahl masseloser Bosonen =",
          int(np.sum(np.linalg.eigvalsh((Madj + Madj.T) / 2) < 1e-9)))

    print("\n(3) Vergleich mit Sumino (Familienbosonen M_ij^2 ~ m_i + m_j, Aufhebung bei alpha_F = 4 alpha)")
    for lab, s_l in (("Auslesung A: sqrt(m) ~ s (Gram, wie H99)", np.sqrt(POL)),
                     ("Auslesung B: m ~ s (sqrt(m) ~ Singulaerwerte von X)", POL)):
        s_l = s_l / s_l.sum()
        M2 = boson_mass2(np.diag(s_l))
        diag = np.sort(s_l)                       # Diagonal-Bosonen M_ii^2 = s_i
        slope = np.polyfit(np.log(np.sort(POL)), np.log(diag), 1)[0]
        print(f"    {lab}: ln M_ii^2 = {slope:.3f} * ln m_i + const  ->  noetig alpha_F = {4 / slope:.1f} alpha")


if __name__ == "__main__":
    print("\n== Auslesung A oder B: Feldtyp, Bosonenschwellen, Kopplungsbedingung ==")
    # Feldtypen mit Vakuumwert; Massenterm der Bosonen tr|delta Phi|^2 mit delta Phi = T-Wirkung
    T = u3_generators()
    sv = np.sqrt(POL) / np.sqrt(POL).sum() * 3      # A: s_i ~ sqrt(m_i)

    def masses(act):
        M = np.array([[np.real(np.trace(act(a).conj().T @ act(b))) for b in T] for a in T])
        return np.sort(np.linalg.eigvalsh((M + M.T) / 2))

    S0 = np.diag(sv)
    fields = {
        "X fundamental (X -> XU), Wert mit X^dag X = S": lambda a: np.diag(np.sqrt(sv)) @ a,
        "S adjungiert (S -> U^dag S U)": lambda a: a @ S0 - S0 @ a,
        "Phi = S von links (Phi -> U Phi), Singulaerwerte s": lambda a: a @ S0,
        "M = S symmetrisch (M -> U M U^T, Sumino-Massenmatrix)": lambda a: a @ S0 + S0 @ a.T,
    }
    for lab, act in fields.items():
        m2 = masses(act)
        nz = int(np.sum(m2 < 1e-12))
        # diagonale Schwellen: Wirkung der Diagonal-Generatoren E_ii
        d = []
        for i in range(3):
            E = np.zeros((3, 3), complex); E[i, i] = 1
            d.append(np.real(np.trace(act(E).conj().T @ act(E))))
        d = np.array(d)
        slopeA = np.polyfit(np.log(POL), np.log(np.maximum(d, 1e-300)), 1)[0] if nz == 0 else float("nan")
        # Auslesung B: s ~ m statt s ~ sqrt(m); die Steigung von ln M_ii^2 gegen ln m verdoppelt sich
        print(f"  {lab:55s} masselos: {nz};  A: ln M_ii^2 = {slopeA:.2f} ln m  -> alpha_F = {4 / slopeA if slopeA == slopeA else float('nan'):.1f} alpha;"
              f"  B: Steigung {2 * slopeA:.2f} -> alpha_F = {2 / slopeA if slopeA == slopeA else float('nan'):.1f} alpha")
    print("\n  Bogen unabhaengig von der Auslesung: K = 2/3 und alle Brannen-Wurzeln >= 0  <=>  |theta| <= pi/12")
    th = np.linspace(-np.pi / 3, np.pi / 3, 200001)
    ok = np.all((1 + np.sqrt(2) * np.cos(th[:, None] + 2 * np.pi * np.arange(3) / 3)) >= -1e-12, axis=1)
    print(f"  numerisch: groesstes |theta| mit allen Wurzeln >= 0: {np.abs(th[ok]).max():.6f}, pi/12 = {np.pi / 12:.6f}")
