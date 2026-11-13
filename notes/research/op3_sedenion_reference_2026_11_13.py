"""Erkundung: nativer Bezugszustand fuer das Oktanten-Tripel in den Sedenionen (13.11.2026, nicht blind, kein Datenvergleich).

(1) Bedingung: Bezug = Eigenzustand einer zweizaehligen Achse, die unter dem magischen Winkel zur dreizaehligen Achse steht
    (in A4/2T: Koordinatenachsen gegen Raumdiagonale); in S3 (D3) stehen die zweizaehligen Achsen senkrecht (90 Grad).
(2) Sedenionen S = O + O e8 (Cayley-Dickson): span(1, e7, e8, e15) ist farbneutral; ist es eine Quaternionenalgebra?
(3) psi (Drehung um 2pi/3 in den Ebenen (e_i, e_i+8)) als Automorphismus; Wirkung auf Im span(1, e7, e8, e15).
(4) Bezug f = (e7 + e8 + e15)/sqrt3: magischer Winkel, Bahn, Qubit-Oktant; Vertauschung mit L_e7 (Ladungsstruktur).
Aufruf: python op3_sedenion_reference_2026_11_13.py
"""
import importlib.util
import os
import numpy as np

spec = importlib.util.spec_from_file_location("ho", os.path.join(os.path.dirname(os.path.abspath(__file__)), "op3_hopf_octant_2026_11_13.py"))
ho = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ho)
omul, oconj = ho.mul, ho.conj
rng = np.random.default_rng(1516)


def smul(x, y):
    """Cayley-Dickson: (a, b)(c, d) = (ac - conj(d) b, d a + b conj(c))."""
    a, b, c, d = x[:8], x[8:], y[:8], y[8:]
    return np.concatenate([omul(a, c) - omul(oconj(d), b), omul(d, a) + omul(b, oconj(c))])


def su(k):
    e = np.zeros(16); e[k] = 1; return e


def psi_matrix(angle):
    P = np.eye(16)
    for i in range(1, 8):
        c, s = np.cos(angle), np.sin(angle)
        P[i, i], P[i, i + 8], P[i + 8, i], P[i + 8, i + 8] = c, -s, s, c
    return P


if __name__ == "__main__":
    print("(1) Achsen in A4 gegen D3: Winkel zweizaehlige zu dreizaehliger Achse")
    print(f"    A4: Koordinatenachse gegen (1,1,1): {np.degrees(np.arccos(1 / np.sqrt(3))):.2f} Grad (magisch); D3: 90 Grad")
    e7, e8, e15 = su(7), su(8), su(15)
    Hn = [su(0), e7, e8, e15]
    # (2) Quaternionenalgebra?
    t = smul(e7, e8)
    print(f"(2) e7 e8 = {'+' if np.allclose(t, e15) else ('-' if np.allclose(t, -e15) else '?')}e15; "
          f"e15^2 = {smul(e15, e15)[0]:+.0f}; assoziativ auf span(1,e7,e8,e15): "
          f"{all(np.allclose(smul(smul(x, y), z), smul(x, smul(y, z))) for x in Hn for y in Hn for z in Hn)}")
    # (3) psi als Automorphismus (beide Drehsinne testen)
    for ang in (2 * np.pi / 3, -2 * np.pi / 3):
        P = psi_matrix(ang)
        err = max(np.abs(P @ smul(x, y) - smul(P @ x, P @ y)).max() for x, y in
                  ((rng.normal(size=16), rng.normal(size=16)) for _ in range(100)))
        print(f"    psi mit Winkel {np.degrees(ang):+.0f} Grad: Automorphismus-Fehler {err:.1e}")
    P = psi_matrix(2 * np.pi / 3)
    print(f"(3) psi(e8) = e8: {np.allclose(P @ e8, e8)}; psi(e7) = {np.round(P @ e7, 3)[[7, 15]].tolist()} in (e7, e15)")
    print("    -> auf Im span(1,e7,e8,e15) ist psi eine Drehung um 120 Grad um die Achse e8")
    # (4) Bezug: Diagonale des farbneutralen Dreibeins (e7, e8, e15)
    f = (e7 + e8 + e15) / np.sqrt(3)
    orb = [f, P @ f, P @ P @ f]
    G = np.array([[x @ y for y in orb] for x in orb])
    print(f"(4) f = (e7+e8+e15)/sqrt3: Winkel zu e8 cos = {f @ e8:.6f}; Skalarprodukte der Bahn\n{np.round(G, 10)}")
    # als Qubit: Bloch-Vektoren in Basis (e7, e15, e8)
    def qubit(n):
        n = n / np.linalg.norm(n)
        th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
        return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    qs = [qubit(np.array([v[7], v[15], v[8]])) for v in orb]
    S = np.array([[np.vdot(x, y) for y in qs] for x in qs])
    r2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
    print(f"    als Qubits: rho^2 = {r2:.4f}, K = {(1 + 2 * r2) / 3:.4f}, Bargmann-Phase {abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0])):.6f}")
    # Ladungsstruktur: vertauscht psi mit L_e7? haelt psi e7 fest?
    Le7 = np.array([smul(e7, su(b)) for b in range(16)]).T
    print(f"    psi vertauscht mit L_e7: {np.allclose(P @ Le7, Le7 @ P)};  L_e7 bildet e8 auf {np.round(Le7 @ e8, 3)[[8, 15]].tolist()} in (e8, e15) ab")


if __name__ == "__main__":
    print("\n== Ladung auf die Sedenionen fortsetzen ==")
    # Companion-Ladung auf O (k85): Q8 = 1/2 - (i/6) L_e7 - (i/3) R_e7 (komplexifiziert)
    L8 = [np.array([omul(ho.unit(k), ho.unit(b)) for b in range(8)]).T for k in range(8)]
    R8 = [np.array([omul(ho.unit(b), ho.unit(k)) for b in range(8)]).T for k in range(8)]
    Q8 = 0.5 * np.eye(8) - (1j / 6) * L8[7] - (1j / 3) * R8[7]
    print(f"    Q8 auf O: Eigenwerte {sorted(np.round(np.linalg.eigvals(Q8).real, 4).tolist())}")
    P = psi_matrix(2 * np.pi / 3).astype(complex)
    # (a) naheliegende Fortsetzung mit sedenionischer Links-/Rechtsmultiplikation
    LS7 = np.array([smul(e7, su(b)) for b in range(16)]).T
    RS7 = np.array([smul(su(b), e7) for b in range(16)]).T
    QS = 0.5 * np.eye(16) - (1j / 6) * LS7 - (1j / 3) * RS7
    print(f"    (a) Q_S = 1/2 - (i/6) L_e7 - (i/3) R_e7 auf S: stimmt auf O mit Q8 ueberein {np.allclose(QS[:8, :8], Q8)}, "
          f"vertauscht mit psi {np.allclose(QS @ P, P @ QS)}")
    # (b) allgemein: gibt es Q auf S mit Q|_O = Q8 (Block) und [Q, psi] = 0?
    n = 16
    unknown = [(i, j) for i in range(n) for j in range(n) if not (i < 8 and j < 8)]
    idx = {ij: k for k, ij in enumerate(unknown)}
    rows, rhs = [], []
    for r in range(n):
        for c in range(n):
            row = np.zeros(len(unknown), complex); b = 0j
            # (Q P - P Q)[r, c] = sum_k Q[r,k] P[k,c] - P[r,k] Q[k,c]
            for k in range(n):
                for (ii, jj, coef) in ((r, k, P[k, c]), (k, c, -P[r, k])):
                    if coef == 0:
                        continue
                    if ii < 8 and jj < 8:
                        b -= coef * Q8[ii, jj]
                    else:
                        row[idx[(ii, jj)]] += coef
            rows.append(row); rhs.append(b)
    A = np.array(rows); bvec = np.array(rhs)
    sol, res, rank, _ = np.linalg.lstsq(A, bvec, rcond=None)
    resid = np.abs(A @ sol - bvec).max()
    print(f"    (b) Q mit Q|_O = Q8 und [Q, psi] = 0: kleinster Restfehler {resid:.2e} -> {'loesbar' if resid < 1e-9 else 'nicht loesbar'}")
    # (c) psi bewegt die Ladungsachse: psi(e7)
    print(f"    (c) psi(e7) = -1/2 e7 + sqrt3/2 e15: Jede Ladung aus Multiplikation mit e7 wird von psi in eine mit psi(e7) ueberfuehrt;")
    print("        psi-feste imaginaere Richtung in S ist nur e8 (G2-fest, nicht die Ladungsachse des Companion).")


if __name__ == "__main__":
    print("\n== Alternative: Zyklus um die Ladungsachse e7 (symmetrischer Punkt a = exp(2pi e7/3), auf S fortgesetzt) ==")
    a = np.cos(2 * np.pi / 3) * su(0) + np.sin(2 * np.pi / 3) * e7
    ai = a.copy(); ai[1:] *= -1
    Cm = np.array([smul(smul(a, su(b)), ai) for b in range(16)]).T     # x -> (a x) a^-1
    Cm2 = np.array([smul(a, smul(su(b), ai)) for b in range(16)]).T    # x -> a (x a^-1)
    print(f"    Klammerung egal: {np.allclose(Cm, Cm2)}; a^3 = 1: {np.allclose(smul(smul(a, a), a), su(0))}")
    err = max(np.abs(Cm @ smul(x, y) - smul(Cm @ x, Cm @ y)).max() for x, y in
              ((rng.normal(size=16), rng.normal(size=16)) for _ in range(100)))
    print(f"    Konjugation mit a ist Automorphismus von S: Fehler {err:.1e}")
    print(f"    vertauscht mit Q_S: {np.allclose(Cm @ QS, QS @ Cm)}; haelt e7 fest: {np.allclose(Cm @ e7, e7)}; "
          f"dreht (e8, e15): {np.round(Cm @ e8, 3)[[8, 15]].tolist()}")
    f2 = (e7 + e8 + e15) / np.sqrt(3)
    orb = [f2, Cm @ f2, Cm @ Cm @ f2]
    G = np.array([[x @ y for y in orb] for x in orb])
    print(f"    Bahn der Diagonale unter diesem Zyklus orthonormal: {np.allclose(G, np.eye(3))}")
    # Ladungen der Richtungen in H_n (komplexifiziert): Eigenwerte von Q_S auf span(1, e7, e8, e15)
    idxH = [0, 7, 8, 15]
    sub = QS[np.ix_(idxH, idxH)]
    inv = np.allclose(QS[np.ix_([i for i in range(16) if i not in idxH], idxH)], 0)
    print(f"    Q_S laesst span(1,e7,e8,e15) invariant: {inv}; Eigenwerte dort {sorted(np.round(np.linalg.eigvals(sub).real, 4).tolist())}")
