"""Erkundung (14.11.2026): dritte Generation als Singulett. Rueckwaertssuche ueber Bedingungen, keine Simulation.

Ziel: eine Struktur mit drei Generationen, in der C(x)S das Familien-Dublett und eine weitere Generation das Singulett
ist (2 + 1). Kandidaten: (A) S + O mit psi + 1 und Ladung Q_* + Q8; (B) O^3 mit dem Slotzyklus tau (Weg B, r14.2).
(1) Z3-Zerlegung der reellen Traeger: (S, psi), (S + O, psi + 1), (O^3, tau); getrennt nach farbneutral und farbig.
(2) Spektren je Teilchenart: psi auf C(x)S mit Q_*; tau auf C(x)O^3 mit der Slot-Ladung Q8.
(3) Passt eine e8-artige Paarkopplung tau-symmetrisch auf drei Plaetze? Neutraler Teil R^2 (x) R^3, Ansatz
    A = d (1 (x) J) + c (Zyklus (x) X), Ladung Q = 1/2 - (i/2) A braucht A^2 = -1.
(4) Die tau-symmetrische 2 + 1-Zerlegung von O^3 (Fourier-Moden) und die Wirkung von tau darauf.
Aufruf: python op3_third_generation_singlet_2026_11_14.py
"""
import importlib.util
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("fs", os.path.join(HERE, "op3_family_su2_right_action_2026_11_14.py"))
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)
L, R, su, smul, I16 = fs.L, fs.R, fs.su, fs.smul, fs.I16
W = np.exp(2j * np.pi / 3)


def z3_mult(M, Pp=None):
    """Vielfachheiten der Eigenwerte 1, omega, omegabar von M (auf dem Bild von Pp)."""
    ev = np.linalg.eigvals(M) if Pp is None else fs.eig_on(M, Pp)
    return tuple(int(np.sum(abs(ev - lam) < 1e-8)) for lam in (1, W, W.conjugate()))


def spectra(Q, color, Z, n):
    """Je Teilchenart die Z3-Vielfachheiten von Z. color: Projektoren (P0, P3, P3bar); n: Dimension."""
    vals = (0.0, 1 / 3, 2 / 3, 1.0)
    out = {}
    for name, q, Pp in (("nu", 0.0, color[0]), ("e+", 1.0, color[0]), ("u", 2 / 3, color[1]), ("dbar", 1 / 3, color[2])):
        Pq = np.eye(n, dtype=complex)
        for q2 in vals:
            if abs(q2 - q) > 1e-9:
                Pq = Pq @ (Q - q2 * np.eye(n)) / (q - q2)
        Ps = Pq @ Pp
        U, s, _ = np.linalg.svd(Ps)
        Bq = U[:, s > 0.5]
        ev = np.linalg.eigvals(Bq.conj().T @ Z @ Bq)
        out[name] = tuple(int(np.sum(abs(ev - lam) < 1e-8)) for lam in (1, W, W.conjugate()))
    return out


if __name__ == "__main__":
    P, SU3, P0, Pc, P3, P3b, Qs = fs.setup()
    e7 = su(7)
    # Oktonionen als die ersten acht Koordinaten von S
    O = slice(0, 8)
    Q8 = (0.5 * I16 - (1j / 6) * L(e7) - (1j / 3) * R(e7))[O, O]
    P0o = np.zeros((8, 8)); P0o[[0, 7], [0, 7]] = 1
    w, V = np.linalg.eig(Q8[1:7, 1:7])
    B3 = np.zeros((8, 3), complex); B3[1:7, :] = V[:, abs(w - 2 / 3) < 1e-9]
    P3o = B3 @ np.linalg.pinv(B3)
    P3bo = np.eye(8) - P0o - P3o
    print(f"Kontrolle: Spektrum Q8 auf C(x)O = {sorted(np.round(np.linalg.eigvals(Q8).real, 4).tolist())} "
          f"(eine Generation: 0, 1/3 x3, 2/3 x3, 1)")

    print("\n(1) Z3-Zerlegung der reellen Traeger: Vielfachheiten der Eigenwerte (1, omega, omegabar)")
    cyc = np.zeros((3, 3)); cyc[0, 1] = cyc[1, 2] = cyc[2, 0] = 1                 # tau(x, y, z) = (y, z, x)
    tau = np.kron(cyc, np.eye(8))
    psi_plus = np.block([[P, np.zeros((16, 8))], [np.zeros((8, 16)), np.eye(8)]])
    P0_SO = np.block([[P0, np.zeros((16, 8))], [np.zeros((8, 16)), P0o]])
    P0_O3 = np.kron(np.eye(3), P0o)
    rows = [("(S, psi)", P, P0, 16), ("(S + O, psi + 1)", psi_plus, P0_SO, 24), ("(O^3, tau)", tau, P0_O3, 24)]
    for name, Z, Pn, n in rows:
        print(f"    {name:18s}: gesamt {z3_mult(Z)}; farbneutral {z3_mult(Z, Pn)}; farbig {z3_mult(Z, np.eye(n) - Pn)}")
    print("    (O (x) 2, tau) = O^3 ohne die tau-feste Kopie: gesamt (0, 8, 8); farbneutral (0, 2, 2); farbig (0, 6, 6)")

    print("\n(2) Spektren je Teilchenart (Vielfachheiten von 1, omega, omegabar)")
    sA = spectra(Qs, (P0, P3, P3b), P, 16)
    QB = np.kron(np.eye(3), Q8)
    sB = spectra(QB, (np.kron(np.eye(3), P0o), np.kron(np.eye(3), P3o), np.kron(np.eye(3), P3bo)), tau.astype(complex), 24)
    print(f"    Kontrolle: [Q8 je Slot, tau] = {np.linalg.norm(QB @ tau - tau @ QB):.1e}")
    for k in ("nu", "e+", "u", "dbar"):
        a = sA[k]
        apl = (a[0] + (1 if k in ("nu", "e+") else 3), a[1], a[2])
        print(f"    {k:5s}: psi auf C(x)S {a}; psi + 1 auf S + O {apl}; tau auf C(x)O^3 {sB[k]}")

    print("\n(3) e8-artige Paarkopplung auf drei Plaetzen: A = d (1 (x) J) + c (Zyklus (x) X), gesucht A^2 = -1 mit c != 0")
    J = np.array([[0.0, -1.0], [1.0, 0.0]])
    # X aus S: L_e8 und L_e15 bilden span(1, e7) des ersten Slots auf span(e8, e15) des zweiten ab
    def pair_block(x):
        M = L(x)
        return M[np.ix_([8, 15], [0, 7])]
    Xs = {"L_e8 (e8-Ladung)": pair_block(su(8)), "R_e8": R(su(8))[np.ix_([8, 15], [0, 7])],
          "L_e15": pair_block(su(15)), "R_e15": R(su(15))[np.ix_([8, 15], [0, 7])]}
    def resid(c, d, X):
        A = d * np.kron(np.eye(3), J) + c * (np.kron(cyc, X) - np.kron(cyc.T, X.T))
        return np.linalg.norm(A @ A + np.eye(6))
    for name, X in Xs.items():
        best = (9.0, 0.0, 0.0)
        for c in np.linspace(-1.5, 1.5, 301):
            if abs(c) < 0.3:
                continue                                              # c -> 0 ist die reine Slot-Ladung, kein Paarterm
            for d in np.linspace(-1.5, 1.5, 301):
                r = resid(c, d, X)
                if r < best[0]:
                    best = (r, c, d)
        ex = min(resid(-2 / 3, 1 / 3, X), resid(2 / 3, -1 / 3, X), resid(2 / 3, 1 / 3, X), resid(-2 / 3, -1 / 3, X))
        print(f"    X aus {name:17s} = {np.round(X, 3).tolist()}: Rastermin |A^2 + 1| (|c| >= 0,3) = {best[0]:.4f} "
              f"bei c = {best[1]:.2f}, d = {best[2]:.2f}; exakt bei |c| = 2/3, |d| = 1/3: {ex:.1e}")

    print("\n(4) tau-symmetrisches 2 + 1 in O^3: Fourier-Moden der Slots")
    F = np.array([[1, 1, 1], [1, W, W ** 2], [1, W ** 2, W]]).T / np.sqrt(3)       # Spalten: Moden
    tm = F.conj().T @ cyc @ F
    print(f"    tau auf den Moden (sym, omega, omegabar): diag {np.round(np.diag(tm), 4).tolist()}; "
          f"auf dem Dublett det = {np.round(tm[1, 1] * tm[2, 2], 4)}, Ordnung 3: {np.allclose(np.linalg.matrix_power(tm, 3), np.eye(3))}")
    # Bahn eines Dublett-Zustands unter tau: Treue, K, Bargmann-Phase in Abhaengigkeit vom Polarwinkel
    for cth, label in ((0.0, "Aequator (reeller Slot-Vektor)"), (1 / np.sqrt(3), "magischer Winkel")):
        th = np.arccos(cth)
        r = np.array([np.cos(th / 2), np.sin(th / 2)], complex)
        U = np.diag([tm[1, 1], tm[2, 2]])
        orb = [r, U @ r, U @ U @ r]
        S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
        rho2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        ph = abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0]))
        print(f"    Dublett-Bezug, {label}: rho^2 = {rho2:.6f}, K = {(1 + 2 * rho2) / 3:.6f}, Phase {ph:.6f}")
