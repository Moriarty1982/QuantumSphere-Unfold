"""Erkundung: Oktanten-Tripel fuer Spin j entlang dreier orthogonaler Achsen (13.11.2026, nicht blind, kein Datenvergleich).

Anlass: Bei Sumino (arXiv:0812.2103) transformiert Phi als U Phi O^T mit O in SO(3); im Vakuum sitzen die drei Generationen
auf drei orthogonalen Achsen dieser farb- und ladungsneutralen SU(2). Frage: Welcher Spin j gibt an diesen Achsen
Koide-Ueberlappung 1/2 und welche Bargmann-Phase?
Aufruf: python op3_neutral_su2_octant_2026_11_13.py
"""
import numpy as np


def spin_ops(j):
    m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m)
    Jp = np.zeros((len(m), len(m)))
    for k in range(1, len(m)):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    Jx = (Jp + Jp.T) / 2
    Jy = (Jp - Jp.T) / 2j
    return Jx, Jy, Jz


def coherent(j, n):
    """Hoechstgewichtszustand entlang der Achse n."""
    Jx, Jy, Jz = spin_ops(j)
    w, V = np.linalg.eigh(n[0] * Jx + n[1] * Jy + n[2] * Jz)
    return V[:, np.argmax(w)]


if __name__ == "__main__":
    axes = [np.array(a, float) for a in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    print("Spin-j-Zustaende entlang x, y, z (Oktant, Raumwinkel pi/2):")
    for j in (0.5, 1.0, 1.5, 2.0):
        q = [coherent(j, a) for a in axes]
        S = np.array([[np.vdot(a, b) for b in q] for a in q])
        fid = abs(S[0, 1]) ** 2
        r2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        ph = np.angle(S[0, 1] * S[1, 2] * S[2, 0])
        K = (1 + 2 * r2) / 3
        print(f"  j = {j}: Treue {fid:.4f} (= (1/2)^(2j) {0.5 ** (2 * j):.4f}), rho^2 = {r2:.4f}, K = {K:.4f}, "
              f"Bargmann-Phase {abs(ph):.4f} (j * pi/2 mod 2pi = {(j * np.pi / 2) % (2 * np.pi):.4f})")
    print("  -> nur j = 1/2 gibt rho^2 = 1/2 (Koide) und die Phase pi/4.")
    # reelle Vektoren (SO(3)-Vektorindex, wie Suminos zweiter Index): orthogonal, Ueberlappung 0, keine Phase
    V = np.eye(3)
    print(f"  SO(3)-Vektoren entlang der Achsen: Ueberlappungen {np.round(V.T @ V - np.eye(3), 3).ravel().tolist()} -> rho^2 = 0, keine Phase")


def casimir_spins(gens, dim):
    """Spins j einer Darstellung aus den Eigenwerten der Casimir-Summe J^2 = sum J_a^2."""
    C = sum(g @ g for g in gens)
    ev = np.round(np.linalg.eigvalsh(C).real, 8)
    js = sorted({float(round((-1 + np.sqrt(1 + 4 * e)) / 2, 4)) for e in ev})
    return js


if __name__ == "__main__":
    import importlib.util, os
    print("\n== Wo eine neutrale SU(2) sitzen kann ==")
    # (1) Zentralisator der Farb-su(3) in g2
    spec = importlib.util.spec_from_file_location("ho", os.path.join(os.path.dirname(os.path.abspath(__file__)), "op3_hopf_octant_2026_11_13.py"))
    ho = importlib.util.module_from_spec(spec); spec.loader.exec_module(ho)
    D = ho.derivations()
    e7 = ho.unit(7)
    Bm = np.array([(d @ e7) for d in D]).T
    _, sv, Vt = np.linalg.svd(Bm)
    su3 = [sum(c * d for c, d in zip(cv, D)) for cv in Vt[np.sum(sv > 1e-9):]]
    # Zentralisator: X in g2 mit [X, s] = 0 fuer alle s in su3
    A = np.array([np.concatenate([(d @ s - s @ d).ravel() for s in su3]) for d in D]).T
    cent = len(D) - np.linalg.matrix_rank(A, tol=1e-9)
    print(f"    (1) dim su(3) = {len(su3)}; Zentralisator in g2: {cent} -> keine Oktonionen-Symmetrie, die mit der Farbe vertauscht")
    # (2) Familien-U(3): SO(3)-Einbettung (reelle Drehungen) gegen SU(2)-Einbettung (2 + 1)
    L = [np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]]), np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
         np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])]
    Jso3 = [1j * l for l in L]                                     # hermitesch, Spin 1 auf C^3
    s = [np.array([[0, 1], [1, 0]]) / 2, np.array([[0, -1j], [1j, 0]]) / 2, np.diag([0.5, -0.5])]
    Jsu2 = [np.block([[x, np.zeros((2, 1))], [np.zeros((1, 2)), np.zeros((1, 1))]]) for x in s]
    def reps(J):
        out = {"3": J}
        # 6 = Sym^2(3), 8 = adjungiert
        I = np.eye(3)
        T2 = [np.kron(j, I) + np.kron(I, j) for j in J]
        P = np.zeros((9, 9))
        for a in range(3):
            for b in range(3):
                P[3 * a + b, 3 * a + b] += 0.5; P[3 * a + b, 3 * b + a] += 0.5
        w, V = np.linalg.eigh(P); Vs = V[:, w > 0.5]
        out["6"] = [Vs.conj().T @ t @ Vs for t in T2]
        gm = []                                                     # Gell-Mann-Basis fuer adjungiert
        for i in range(3):
            for k in range(i + 1, 3):
                E = np.zeros((3, 3), complex); E[i, k] = E[k, i] = 1; gm.append(E)
                E = np.zeros((3, 3), complex); E[i, k] = -1j; E[k, i] = 1j; gm.append(E)
        gm += [np.diag([1, -1, 0]).astype(complex), np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]
        def ad(j):
            return np.array([[np.trace(g1.conj().T @ (j @ g2 - g2 @ j)) / 2 for g2 in gm] for g1 in gm])
        out["8"] = [ad(j) for j in J]
        return out
    for lab, J in (("SO(3) reell (Generationen als Vektor)", Jso3), ("SU(2) als 2 + 1", Jsu2)):
        r = reps(J)
        print(f"    (2) {lab}: Spins in 3: {casimir_spins(r['3'], 3)}, 6: {casimir_spins(r['6'], 6)}, 8: {casimir_spins(r['8'], 8)}")
    print("    -> In der Familien-U(3) gibt es entweder Generationen als Vektor (nur ganzzahlige Spins, kein Spinor)")
    print("       oder einen Spinor (2 + 1), dann sind die Generationen kein Vektor auf drei Achsen.")


if __name__ == "__main__":
    print("\n== Feldsuche ==")
    # (1) so(8) (Trialitaets-Spin(8) auf O): Zentralisator der Farb-su(3)
    so8 = []
    for i in range(8):
        for k in range(i + 1, 8):
            E = np.zeros((8, 8)); E[i, k] = 1; E[k, i] = -1; so8.append(E)
    A = np.array([np.concatenate([(x @ s_ - s_ @ x).ravel() for s_ in su3]) for x in so8]).T
    print(f"    (1) Zentralisator der Farb-su(3) in so(8): Dimension {len(so8) - np.linalg.matrix_rank(A, tol=1e-9)} "
          "(nur abelsch moeglich, keine SU(2))")
    # (2) r82.4: Paarkanal nu^c nu^c (psi^T eps psi). Plaetze mit Spin-Richtungen entlang x, y, z:
    eps = np.array([[0, 1], [-1, 0]], complex)
    q = [coherent(0.5, a) for a in axes]
    Mmaj = np.array([[qa @ eps @ qb for qb in q] for qa in q])
    sv = np.sort(np.linalg.svd(Mmaj, compute_uv=False))
    print(f"    (2) Majorana-Paarung chi_a^T eps chi_b, Spins entlang x, y, z: |M_ab|^2 = "
          f"{np.round(np.abs(Mmaj) ** 2, 4).tolist()}")
    print(f"        Diagonale null (gleiche Richtung paart nicht), Nebendiagonale |.|^2 = 1/2; Singulaerwerte {np.round(sv, 4)}")
    # mit gemeinsamer Diagonale d: M + d*1, Koide der Singulaerwerte (mit Vorzeichen der Eigenwerte, falls reell-symmetrisch)
    for d in (0.5, 1.0, 1.5):
        sv2 = np.sort(np.linalg.svd(Mmaj + d * np.eye(3), compute_uv=False))
        K = (sv2 ** 2).sum() / sv2.sum() ** 2
        print(f"        M + {d}*1: Singulaerwerte {np.round(sv2, 4)}, K (positive Wurzeln) = {K:.4f}")


if __name__ == "__main__":
    print("\n== Pruefung Punkt 3: genuegt eine diskrete Gruppe? ==")
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
    qi, qj, qk = -1j * sx, -1j * sy, -1j * sz                       # Quaternionen als SU(2), ijk = -1
    a = -(np.eye(2) + qi + qj + qk) / 2                             # Hurwitz-Einheit, a^3 = 1 (symmetrischer Punkt aus r15)
    print(f"    Hurwitz-Einheit a = -(1+i+j+k)/2: unitaer {np.allclose(a.conj().T @ a, np.eye(2))}, a^3 = 1 {np.allclose(a @ a @ a, np.eye(2))}")
    # binaere Tetraedergruppe 2T: erzeugt von i, j, k, a
    G = [np.eye(2, dtype=complex)]
    gens = [qi, qj, qk, a]
    changed = True
    while changed:
        changed = False
        for g in list(G):
            for h in gens:
                p = g @ h
                if not any(np.allclose(p, x) for x in G):
                    G.append(p); changed = True
    print(f"    erzeugte Gruppe hat {len(G)} Elemente (binaere Tetraedergruppe 2T, Doppelueberlagerung von A4 mit 12)")
    # Bahn eines Zustands unter a: Oktanten-Tripel?
    def bloch(psi):
        return np.real([np.vdot(psi, sx @ psi), np.vdot(psi, sy @ psi), np.vdot(psi, sz @ psi)])
    psi = coherent(0.5, np.array([1.0, 0, 0]))
    orb = [psi, a @ psi, a @ a @ psi]
    B = [bloch(v) for v in orb]
    S = np.array([[np.vdot(u, v) for v in orb] for u in orb])
    print(f"    Bahn von |+x> unter a: Bloch-Vektoren {[np.round(b, 3).tolist() for b in B]}")
    print(f"    Treuen {np.round(np.abs(S[0, 1]) ** 2, 4)}, {np.round(np.abs(S[1, 2]) ** 2, 4)}, {np.round(np.abs(S[2, 0]) ** 2, 4)}; "
          f"Bargmann-Phase {abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0])):.6f} (pi/4)")
    # A4 auf den drei Achsen: Klein-Gruppe = Vorzeichenwechsel, Z3 = zyklische Vertauschung (Konjugation mit a)
    R = np.array([[np.real(np.trace(s1 @ a @ s2 @ a.conj().T)) / 2 for s2 in (sx, sy, sz)] for s1 in (sx, sy, sz)])
    print(f"    Wirkung von a auf die Achsen (SO(3)-Bild):\n{np.round(R, 6)}")
    print("    -> Eine stetige SU(2) ist nicht noetig: Der Zyklus tau als Element der Ordnung 3 in SU(2) (Hurwitz-Einheit)")
    print("       erzeugt das Oktanten-Tripel; A4 (r55, Platzsymmetrie) ist dessen Bild in SO(3), 2T die Spinor-Huelle.")
    print("       Die Darstellungen von A4 (1, 1', 1'', 3) sind keine Spinoren; ein 2T-Dublett waere weiterhin ein neues Feld.")


if __name__ == "__main__":
    print("\n== Sedenionen (r13): farbneutrale Ebene (e7, e15) als S3-Dublett ==")
    # psi dreht jede Ebene (e_i, e_{i+8}) um 2pi/3; komplexifiziert: Eigenwerte omega, omega^2 -> SU(2)-Element diag(omega, omega^2)
    w3 = np.exp(2j * np.pi / 3)
    U = np.diag([w3, w3 ** 2])
    print(f"    Z3 auf der komplexifizierten Ebene: diag(omega, omega^2), det = {np.round(np.linalg.det(U), 12)}, U^3 = 1 {np.allclose(U @ U @ U, np.eye(2))}")
    # Achse der Drehung = z (Eigenbasis); reelle Vektoren der Ebene, z.B. e7 = (f_w + f_w2)/sqrt2, liegen auf dem Aequator
    for lab, psi in (("reeller Vektor e7 (Aequator)", np.array([1, 1]) / np.sqrt(2)),
                     ("komplexer Bezug unter dem magischen Winkel", np.array([np.sqrt((1 + 1 / np.sqrt(3)) / 2), np.sqrt((1 - 1 / np.sqrt(3)) / 2)]))):
        orb = [psi, U @ psi, U @ U @ psi]
        S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
        r2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        print(f"    {lab:44s}: rho^2 = {r2:.4f}, K = {(1 + 2 * r2) / 3:.4f}, Bargmann-Phase {abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0])):.4f}")
