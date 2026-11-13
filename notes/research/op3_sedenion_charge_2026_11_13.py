"""Erkundung: Ladung auf die Sedenionen anders als ueber e7 fortsetzen (13.11.2026, nicht blind, kein Datenvergleich).

Rueckwaertssuche. Gesucht ist ein Ladungsoperator Q auf C (x) S mit
  N1  [Q, psi] = 0          (der Generationsschritt aendert die Ladung nicht),
  N2  [Q, su(3)_c] = 0      (Farbe = Stabilisator von e7 in g2, diagonal auf S = O + O e8),
  N3  Q hermitesch, conj(Q) = 1 - Q (Teilchen/Antiteilchen wie bei Q8), Spektrum in {0, 1/3, 2/3, 1},
      Farbtriplett 3 -> 2/3, 3bar -> 1/3 (wie Q8 auf O),
  N4  danach: gibt es einen farb- und ladungsneutralen Unterraum, auf dem psi mit Ordnung 3 wirkt (Qubit),
      und einen nativen Bezugszustand unter dem magischen Winkel (Oktanten-Tripel)?
Aufruf: python op3_sedenion_charge_2026_11_13.py
"""
import importlib.util
import itertools
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ho = load("op3_hopf_octant_2026_11_13")
sr = load("op3_sedenion_reference_2026_11_13")
smul, su, psi_matrix = sr.smul, sr.su, sr.psi_matrix
rng = np.random.default_rng(1613)
TOL = 1e-9


def null_space(A, tol=1e-9):
    _, s, Vh = np.linalg.svd(A)
    return Vh[np.sum(s > tol):].conj().T


def commutant(gens, n=16):
    """Basis aller komplexen n x n-Matrizen X mit [X, g] = 0 fuer alle g."""
    I = np.eye(n)
    A = np.vstack([np.kron(g.T, I) - np.kron(I, g) for g in gens])   # vec(X g - g X), Spaltenstapelung
    N = null_space(A.astype(complex))
    return [N[:, k].reshape(n, n, order="F") for k in range(N.shape[1])]


def proj(vecs):
    U, s, _ = np.linalg.svd(np.array(vecs).T, full_matrices=False)
    U = U[:, s > 1e-9]
    return U @ U.conj().T


if __name__ == "__main__":
    e7, e8, e15 = su(7), su(8), su(15)
    P = psi_matrix(2 * np.pi / 3).astype(complex)
    # g2 diagonal auf S, Farbalgebra = Stabilisator von e7
    D8 = ho.derivations()
    DS = [np.kron(np.eye(2), d) for d in D8]
    err = max(np.abs(D @ smul(x, y) - smul(D @ x, y) - smul(x, D @ y)).max()
              for D in DS[:3] for x, y in ((rng.normal(size=16), rng.normal(size=16)) for _ in range(20)))
    A = np.array([(D @ e7) for D in DS]).T
    c = null_space(A)
    SU3 = [sum(c[k, j] * DS[k] for k in range(14)).real for j in range(c.shape[1])]
    print(f"(0) g2 diagonal auf S: Derivationsfehler {err:.1e}; dim g2 = {len(DS)}; Farbalgebra Stab(e7): dim {len(SU3)}")
    sing = null_space(np.vstack(SU3))
    sing_idx = [i for i in range(16) if np.abs(sing[i]).max() > 1e-6]
    print(f"    farbneutraler Unterraum von S: dim {sing.shape[1]}, getragen von Basis {['e%d' % i for i in sing_idx]}")

    # N1 + N2: Kommutant
    Com = commutant([P] + [g.astype(complex) for g in SU3])
    print(f"(1) Kommutant von psi und su(3)_c auf C(x)S: komplexe Dimension {len(Com)} "
          "(erwartet 6 farbneutral [gl(2) + 1 + 1] + 4 farbig)")

    # Bausteine
    H = [0, 7, 8, 15]
    P0 = np.zeros((16, 16)); P0[H, H] = 1
    Pc = np.eye(16) - P0
    L = lambda x: np.array([smul(x, su(b)) for b in range(16)]).T
    R = lambda x: np.array([smul(su(b), x) for b in range(16)]).T
    Le8, Re8, Le7, Re7 = L(e8), R(e8), L(e7), R(e7)
    QS = 0.5 * np.eye(16) - (1j / 6) * Le7 - (1j / 3) * Re7          # fruehere Fortsetzung ueber e7

    # Farbtriplett 3 = 2/3-Eigenraum von Q_S auf den farbigen Richtungen von O, mit psi auf S verteilt
    Ocol = [i for i in range(1, 7)]
    w, V = np.linalg.eig(QS[np.ix_(Ocol, Ocol)])
    V3 = []
    for k in range(6):
        if abs(w[k] - 2 / 3) < 1e-9:
            v = np.zeros(16, complex); v[Ocol] = V[:, k]; V3.append(v)
    V3 = V3 + [P @ v for v in V3] + [P @ P @ v for v in V3]
    P3 = proj(V3)
    r3 = np.linalg.matrix_rank(np.array(V3), 1e-8)
    P3bar = Pc - P3
    is_rep = all(np.allclose(P3 @ g, g @ P3) for g in SU3)
    print(f"    Triplett-Isotypie: span(V3, psi V3, psi^2 V3) hat dim {r3}; Projektor vertauscht mit su(3) {is_rep}, mit psi {np.allclose(P3 @ P, P @ P3)}")

    # (2) farbneutraler Block: Klassifikation der zulaessigen Ladungen
    print("\n(2) Farbneutraler Block span(1, e7, e8, e15):")
    print(f"    psi-Eigenwerte dort: {sorted(np.round(np.angle(np.linalg.eigvals(P[np.ix_(H, H)])) / (2 * np.pi / 3), 6).tolist())} (x 2pi/3)")
    print(f"    Schnitt mit fruehrerem Befund: psi-Mittel von L_e7 = {np.abs((Le7 + P @ Le7 @ P.conj().T + P @ P @ Le7 @ (P @ P).conj().T) / 3).max():.1e}"
          " -> generationsgemittelte Q_S = 1/2 konstant")
    blk = lambda M: M[np.ix_(H, H)]
    print(f"    L_e8 und R_e8 vertauschen mit psi: {np.allclose(Le8 @ P, P @ Le8)}, {np.allclose(Re8 @ P, P @ Re8)}; "
          f"mit su(3): {all(np.allclose(Le8 @ g, g @ Le8) for g in SU3)}")
    # Allgemeine Loesung: hermitesch, conj(Q) = 1 - Q, [Q, psi] = 0, Eigenwerte in {0, 1}
    # Parametrisierung Q = 1/2 + i A, A reell antisymmetrisch 4x4, [A, psi] = 0
    PH = P[np.ix_(H, H)].real
    basisA = []
    for i, j in itertools.combinations(range(4), 2):
        E = np.zeros((4, 4)); E[i, j], E[j, i] = 1, -1; basisA.append(E)
    M = np.array([(E @ PH - PH @ E).ravel() for E in basisA]).T
    cA = null_space(M)
    gensA = [sum(cA[k, j] * basisA[k] for k in range(6)) for j in range(cA.shape[1])]
    print(f"    reell antisymmetrische A mit [A, psi] = 0: dim {len(gensA)} (K: 1<->e8, J: e7<->e15)")
    K = np.zeros((4, 4)); K[2, 0], K[0, 2] = 1, -1          # 1 -> e8
    J = np.zeros((4, 4)); J[3, 1], J[1, 3] = 1, -1          # e7 -> e15
    span_ok = np.linalg.matrix_rank(np.array([g.ravel() for g in gensA] + [K.ravel(), J.ravel()]), 1e-9) == 2
    print(f"    = span(K, J): {span_ok}; Q = 1/2 + i(b K + a J) hat Eigenwerte 1/2 +- b, 1/2 +- a")
    print("    Spektrum {0, 1} (Leptonen) erzwingt |a| = |b| = 1/2: genau vier Ladungen (zwei Vorzeichen)")
    print(f"    L_e8 auf dem Block = K {'-' if np.allclose(blk(Le8), K - J) else '+'} J: {np.allclose(blk(Le8), K - J) or np.allclose(blk(Le8), K + J)}; "
          f"R_e8 = K {'+' if np.allclose(blk(Re8), K + J) else '-'} J: {np.allclose(blk(Re8), K + J) or np.allclose(blk(Re8), K - J)}")

    # (3) die Kandidaten Q_* = P0 (1/2 - (i/2) X_e8) + 2/3 P3 + 1/3 P3bar, X = L oder R
    print("\n(3) Kandidaten Q_* = P0 (1/2 - (i/2) X_e8) P0 + 2/3 P_3 + 1/3 P_3bar, X = L_e8 oder R_e8:")
    cands = {}
    for name, X in (("L", Le8), ("R", Re8)):
        Q = P0 @ (0.5 * np.eye(16) - 0.5j * X) @ P0 + (2 / 3) * P3 + (1 / 3) * P3bar
        ev = np.round(np.linalg.eigvalsh((Q + Q.conj().T) / 2), 6)
        vals, cnt = np.unique(ev, return_counts=True)
        ok = dict(herm=np.allclose(Q, Q.conj().T), psi=np.allclose(Q @ P, P @ Q),
                  su3=all(np.allclose(Q @ g, g @ Q) for g in SU3), conj=np.allclose(Q.conj(), np.eye(16) - Q))
        inCom = np.linalg.matrix_rank(np.array([C.ravel() for C in Com] + [Q.ravel()]), 1e-8) == len(Com)
        O_inv = np.allclose(Q[8:, :8], 0) and np.allclose(Q[:8, 8:], 0)
        print(f"    X = {name}_e8: {ok}, im Kommutant {inCom}; Spektrum {dict(zip(vals.tolist(), cnt.tolist()))}; "
              f"laesst O invariant {O_inv}; Q_*|_O = Q8: {np.allclose(Q[:8, :8], QS[:8, :8])}")
        cands[name] = Q
    eps = np.diag([1.0] * 8 + [-1.0] * 8)
    Q = cands["L"]
    print(f"    epsilon (a + b e8 -> a - b e8) vertauscht mit Q_*: {np.allclose(eps @ Q, Q @ eps)}; "
          f"eps Q_* eps = 1 - Q_* auf dem farbneutralen Block: {np.allclose(blk(eps @ Q @ eps), np.eye(4) - blk(Q))}; "
          f"auf dem farbigen Teil vertauscht eps: {np.allclose(Pc @ eps @ Q @ Pc, Pc @ Q @ eps @ Pc)}")

    # (4) neutrales Qubit
    print("\n(4) Farb- und ladungsneutraler Unterraum N = ker Q_* (X = L_e8):")
    w, V = np.linalg.eigh(Q)
    N = V[:, np.abs(w) < 1e-9]
    print(f"    dim N = {N.shape[1]}; in span(1,e7,e8,e15): {np.allclose(N[[i for i in range(16) if i not in H]], 0)}")
    PN = N.conj().T @ P @ N
    ewN = np.linalg.eigvals(PN)
    print(f"    psi auf N: Eigenwerte {np.round(ewN, 6).tolist()} -> projektiv Ordnung 3: {not np.allclose(ewN[0], ewN[1])}")
    # Eigenbasis von psi in N
    wv, U = np.linalg.eig(PN)
    order = np.argsort(np.abs(np.angle(wv)))
    v1, vw = N @ U[:, order[0]], N @ U[:, order[1]]
    show = lambda v: {('1', 'e7', 'e8', 'e15')[k]: complex(np.round(v[H[k]] / v[H][np.argmax(np.abs(v[H]))], 6)) for k in range(4) if abs(v[H[k]]) > 1e-9}
    print(f"    psi-fester neutraler Zustand v1 ~ {show(v1)}; psi-Eigenwert omega: v_w ~ {show(vw)}")

    def triple(r):
        r = r / np.linalg.norm(r)
        orb = [r, P @ r, P @ P @ r]
        S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
        rho2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        return rho2, (1 + 2 * rho2) / 3, abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0]))

    def bloch_cos(x):
        a = abs(np.vdot(v1, x)) ** 2; b = abs(np.vdot(vw, x)) ** 2
        return (a - b) / (a + b)

    # (5) Bezugszustand
    print("\n(5) Bezugszustand in N (Bloch-Achse = psi-Achse v1/v_w; Oktant verlangt cos theta = +-1/sqrt3 = +-0.57735):")
    f = (e7 + e8 + e15) / np.sqrt(3)
    fN = N @ (N.conj().T @ f)
    print(f"    Projektion der frueheren Diagonale (e7+e8+e15)/sqrt3: Norm^2 {np.linalg.norm(fN) ** 2:.4f}, cos theta {bloch_cos(fN):+.4f}, "
          "rho^2 = %.4f, K = %.4f, Phase %.4f" % triple(fN))
    vals = set()
    for coeffs in itertools.product((-1, 0, 1), repeat=4):
        if not any(coeffs):
            continue
        x = np.zeros(16); x[H] = coeffs
        xN = N @ (N.conj().T @ x)
        if np.linalg.norm(xN) > 1e-9:
            vals.add(round(float(bloch_cos(xN)), 6))
    print(f"    reelle Elemente mit Koeffizienten in {{-1,0,1}} auf (1,e7,e8,e15), auf N projiziert: cos theta in {sorted(vals)}")
    print("    allgemein: cos theta = (a^2 + c^2 - b^2 - d^2)/(a^2+b^2+c^2+d^2) fuer x = a + b e7 + c e8 + d e15 -> rational fuer"
          " rationale Koeffizienten; 1/sqrt3 nicht erreichbar")
    th = np.arccos(1 / np.sqrt(3))
    r = np.cos(th / 2) * v1 + np.sin(th / 2) * vw
    print(f"    Bezug mit cos theta = 1/sqrt3 (von Hand gesetzt): rho^2 = %.4f, K = %.4f, Bargmann-Phase %.6f (pi/4 = %.6f)" % (*triple(r), np.pi / 4))
    print(f"    dafuer noetiges Amplitudenverhaeltnis tan(theta/2) = {np.tan(th / 2):.6f} = 2 sin(pi/12) = {2 * np.sin(np.pi / 12):.6f}")
