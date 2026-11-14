"""Erkundung (nicht blind): die Hurwitz-Einheiten von H_n = span(1, e7, e8, e15), von rechts auf das neutrale Qubit N.

(1) Die 24 Hurwitz-Einheiten (+-1, +-e7, +-e8, +-e15, (+-1 +- e7 +- e8 +- e15)/2) wirken von rechts auf N: Gruppe 2T?
    Projektives Bild A4 (12 Drehungen)?
(2) Achsen: zweizaehlige Achsen (e7, e15, e8) und dreizaehlige Achsen (Raumdiagonalen); Winkel zur psi-Achse e8.
(3) Bezug = Eigenzustand einer dreizaehligen Hurwitz-Einheit; Bahn unter psi: rho^2, K, Bargmann-Phase.
(4) Verhaeltnis von psi zu 2T: normalisiert psi die Gruppe?
Aufruf: python op3_hurwitz_2t_neutral_qubit_2026_11_14.py
"""
import importlib.util
import itertools
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("k225", os.path.join(HERE, "predictions", "k225_test_h103.py"))
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)
B, R, su, P = k.B, k.R, k.su, k.P
IDX = [0, 7, 8, 15]


def quat(c):
    x = np.zeros(16); x[IDX] = c; return x


def on_N(x):
    """Rechtsmultiplikation mit x, eingeschraenkt auf N (2x2)."""
    M = R(x).astype(complex)
    return B.conj().T @ M @ B


def proj_key(U):
    """Projektive Klasse einer 2x2-Unitaeren (Phase herausgenommen)."""
    d = np.linalg.det(U)
    V = U / np.sqrt(d)
    i = np.argmax(np.abs(V.ravel()))
    V = V * np.exp(-1j * np.angle(V.ravel()[i]))
    return tuple(np.round(V.ravel(), 6))


def axis(U):
    """Bloch-Drehachse einer 2x2-Unitaeren und Drehwinkel."""
    V = U / np.sqrt(np.linalg.det(U))
    a = np.real(np.trace(V)) / 2
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
    n = np.array([np.imag(np.trace(V @ s)) / 2 for s in (sx, sy, sz)]) * -1
    nn = np.linalg.norm(n)
    return (n / nn if nn > 1e-12 else n), 2 * np.degrees(np.arccos(np.clip(abs(a), -1, 1)))


if __name__ == "__main__":
    units = []
    for i in range(4):
        for s in (1, -1):
            c = np.zeros(4); c[i] = s; units.append(c)
    for s in itertools.product((1, -1), repeat=4):
        units.append(np.array(s) / 2)
    U = [on_N(quat(c)) for c in units]
    unit_ok = all(np.allclose(u.conj().T @ u, np.eye(2)) for u in U)
    keys = {proj_key(u) for u in U}
    # Abgeschlossenheit: Produkte bleiben in der Menge
    Ukeys = [tuple(np.round(u.ravel(), 6)) for u in U]
    closed = all(tuple(np.round((a @ b).ravel(), 6)) in set(Ukeys) for a in U for b in U)
    print(f"(1) 24 Hurwitz-Einheiten auf N: unitaer {unit_ok}; treu (24 verschiedene Matrizen) {len(set(Ukeys)) == 24}; "
          f"abgeschlossen {closed}; projektives Bild {len(keys)} Elemente (A4: 12)")
    orders = {}
    for u in U:
        for n in range(1, 13):
            if np.allclose(np.linalg.matrix_power(u, n), np.eye(2)):
                orders[n] = orders.get(n, 0) + 1; break
    print(f"    Ordnungen der 24 Elemente: {dict(sorted(orders.items()))} (2T: 1:1, 2:1, 4:6, 3:8, 6:8)")
    # (2) Achsen relativ zur psi-Achse; psi auf N ist diag(1, omega) -> Achse z
    zaxis = np.array([0, 0, 1.0])
    print("(2) Achsen auf der Bloch-Kugel von N (psi-Achse = z):")
    seen = {}
    for c, u in zip(units, U):
        n, ang = axis(u)
        if np.linalg.norm(n) < 1e-9:
            continue
        key = round(abs(n @ zaxis), 6)
        seen.setdefault((round(ang, 3), key), []).append(c)
    for (ang, cz), cs in sorted(seen.items()):
        print(f"    Drehwinkel {ang:7.3f} Grad, |cos(Achse, psi-Achse)| = {cz:.6f}: {len(cs)} Einheiten")
    # (3) Bezug = Eigenzustand einer dreizaehligen Einheit h = (1 + e7 + e8 + e15)/2
    h = on_N(quat(np.array([1, 1, 1, 1]) / 2))
    w, V = np.linalg.eig(h)
    PN = B.conj().T @ P @ B
    for j in range(2):
        r = V[:, j]
        orb = [r, PN @ r, PN @ PN @ r]
        S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
        rho2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        ph = abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0]))
        print(f"(3) Eigenzustand von R_h (h = (1+e7+e8+e15)/2), Eigenwert {np.round(w[j], 6)}: unter psi rho^2 = {rho2:.6f}, "
              f"K = {(1 + 2 * rho2) / 3:.6f}, Bargmann-Phase {ph:.6f} (pi/4 = {np.pi / 4:.6f})")
    # (4) normalisiert psi die Gruppe? psi^-1 u psi in der Menge?
    PNi = np.linalg.inv(PN)
    norm = all(tuple(np.round((PNi @ u @ PN).ravel(), 6)) in set(Ukeys) for u in U)
    proj_norm = all(proj_key(PNi @ u @ PN) in keys for u in U)
    print(f"(4) psi normalisiert 2T auf N: {norm}; projektiv: {proj_norm}")
    # Wirkt psi auf H_n als Automorphismus, der Hurwitz-Einheiten auf Hurwitz-Einheiten abbildet?
    Ps = P.real
    imgs = [Ps @ quat(c) for c in units]
    inH = sum(any(np.allclose(x, quat(c)) for c in units) for x in imgs)
    print(f"    psi bildet {inH} von 24 Hurwitz-Einheiten auf Hurwitz-Einheiten ab")
