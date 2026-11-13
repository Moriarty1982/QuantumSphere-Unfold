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
