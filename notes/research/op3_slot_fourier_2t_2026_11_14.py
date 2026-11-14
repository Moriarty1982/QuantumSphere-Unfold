"""Erkundung (14.11.2026, nicht blind): die Fourier-Transformation der drei Slots und die Gruppe 2T.

Rueckwaertssuche zur Luecke aus v4.10.0-r13.6: gesucht ist eine nicht monomiale Slotoperation, die eine Zerlegung 2 + 1
des Slotraums C^3 erhaelt und auf dem Dublett eine zweizaehlige Achse unter dem magischen Winkel zu einem Element der
Ordnung 3 hat. Kandidat: die diskrete Fourier-Transformation F der Slots zusammen mit einer Slot-Phase der Ordnung 3.

(1) Bausteine: Zyklus tau, Uhr D = diag(1, w, w^2), Phase S = diag(1, w, w), Fourier F; Paritaet P = F^2.
(2) Zerlegung nach P (gerade 2, ungerade 1); Wirkung von S und F auf dem geraden Dublett; Gruppe <S, F>.
(3) Winkel zwischen der Achse von S und der Achse von F auf dem Dublett.
(4) Oktant: Bahn eines F-Eigenzustands unter S; rho^2, K, Bargmann-Phase; tan(theta/2) gegen 2 sin(pi/12).
(5) Verhaeltnis zu tau: Heisenberg-Gruppe <tau, D>, normalisiert von S und F; tau erhaelt das Dublett nicht.
(6) F als Summe monomialer Operationen: Entwicklung nach tau^a D^b.
(7) Allgemeines n: Dimension des geraden Teils und <e0|F|e0> = 1/sqrt(n).
Aufruf: python op3_slot_fourier_2t_2026_11_14.py
"""
import itertools
import numpy as np

W = np.exp(2j * np.pi / 3)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1])]


def fourier(n):
    w = np.exp(2j * np.pi / n)
    return np.array([[w ** (j * k) for k in range(n)] for j in range(n)]) / np.sqrt(n)


def su2(U):
    return U / np.sqrt(np.linalg.det(U))


def axis(U):
    V = su2(U)
    n = np.array([np.imag(np.trace(V @ s)) / 2 for s in SIG])
    nn = np.linalg.norm(n)
    ang = 2 * np.degrees(np.arccos(np.clip(abs(np.real(np.trace(V)) / 2), 0, 1)))
    return (n / nn if nn > 1e-12 else n), ang


def generate(gens, dim, cap=3000):
    grp = [np.eye(dim, dtype=complex)]
    frontier = list(grp)
    while frontier and len(grp) < cap:
        new = []
        for a in frontier:
            for b in gens:
                c = a @ b
                if not any(np.allclose(c, x) for x in grp):
                    grp.append(c); new.append(c)
        frontier = new
    return grp


def proj_count(grp):
    keys = set()
    for g in grp:
        v = g.ravel()
        k = np.argmax(np.abs(v) > 1e-9)
        keys.add(tuple(np.round(v * np.exp(-1j * np.angle(v[k])), 6)))
    return len(keys)


if __name__ == "__main__":
    tau = np.zeros((3, 3), complex); tau[0, 1] = tau[1, 2] = tau[2, 0] = 1      # tau(x, y, z) = (y, z, x)
    D = np.diag([1, W, W ** 2])
    S = np.diag([1, W, W])
    F = fourier(3)
    P = F @ F
    print("(1) Bausteine")
    print(f"    F unitaer: {np.allclose(F.conj().T @ F, np.eye(3))}; F^4 = 1: {np.allclose(np.linalg.matrix_power(F, 4), np.eye(3))}; "
          f"P = F^2 vertauscht Slot 1 und 2: {np.allclose(P, np.eye(3)[[0, 2, 1]])}")
    print(f"    Eintraege ungleich null: tau {int(np.sum(abs(tau) > 1e-9))}, D {int(np.sum(abs(D) > 1e-9))}, "
          f"S {int(np.sum(abs(S) > 1e-9))}, F {int(np.sum(abs(F) > 1e-9))} (monomial: 3)")

    print("\n(2) Zerlegung nach der Paritaet P")
    e0 = np.array([1, 0, 0], complex); u = np.array([0, 1, 1], complex) / np.sqrt(2); a = np.array([0, 1, -1], complex) / np.sqrt(2)
    B = np.array([e0, u]).T
    for name, M in (("S", S), ("F", F), ("tau", tau), ("D", D)):
        leak = np.linalg.norm(a.conj() @ M @ B) + np.linalg.norm(B.conj().T @ M @ a)
        print(f"    {name:3s}: vertauscht mit P: {np.allclose(M @ P, P @ M)}; mischt gerade/ungerade: {leak:.3f}; "
              f"auf dem Singulett: {np.round(a.conj() @ M @ a, 4)}")
    Sd, Fd = B.conj().T @ S @ B, B.conj().T @ F @ B
    print(f"    S auf dem Dublett = {np.round(Sd, 4).tolist()}")
    print(f"    F auf dem Dublett = {np.round(Fd.real, 6).tolist()} (reell; 1/sqrt3 = {1 / np.sqrt(3):.6f}, sqrt(2/3) = {np.sqrt(2 / 3):.6f})")
    G3 = generate([S, F], 3)
    G2 = generate([su2(Sd), su2(Fd)], 2)
    orders = {}
    for g in G2:
        for n in range(1, 13):
            if np.allclose(np.linalg.matrix_power(g, n), np.eye(2)):
                orders[n] = orders.get(n, 0) + 1; break
    print(f"    <S, F> auf C^3: {len(G3)} Elemente, projektiv {proj_count(G3)}; auf dem Dublett (Determinante 1): "
          f"{len(G2)} Elemente, Ordnungen {dict(sorted(orders.items()))} (2T: 1:1, 2:1, 3:8, 4:6, 6:8)")

    print("\n(3) Achsen auf der Bloch-Kugel des Dubletts")
    nS, aS = axis(Sd); nF, aF = axis(Fd)
    print(f"    S: Drehwinkel {aS:.1f} Grad, Achse {np.round(nS, 4).tolist()}; F: Drehwinkel {aF:.1f} Grad, Achse {np.round(nF, 4).tolist()}")
    print(f"    |cos| zwischen beiden Achsen = {abs(nS @ nF):.10f}; 1/sqrt3 = {1 / np.sqrt(3):.10f}")

    print("\n(4) Oktant: Bahn eines F-Eigenzustands unter S")
    w, V = np.linalg.eigh((Fd + Fd.conj().T) / 2)
    for k in range(2):
        r = V[:, k]
        orb = [r, Sd @ r, Sd @ Sd @ r]
        G = np.array([[np.vdot(x, y) for y in orb] for x in orb])
        rho2 = (abs(G[0, 1]) ** 2 + abs(G[1, 2]) ** 2 + abs(G[2, 0]) ** 2) / 3
        ph = abs(np.angle(G[0, 1] * G[1, 2] * G[2, 0]))
        vec = B @ r
        vec = vec / vec[np.argmax(abs(vec))]
        t = min(abs(r[1] / r[0]), abs(r[0] / r[1]))
        print(f"    Eigenwert {w[k]:+.0f}: Slot-Vektor ~ {np.round(vec.real, 4).tolist()}; rho^2 = {rho2:.6f}, K = {(1 + 2 * rho2) / 3:.6f}, "
              f"Phase {ph:.6f} (pi/4 = {np.pi / 4:.6f}); tan(theta/2) = {t:.6f} (2 sin(pi/12) = {2 * np.sin(np.pi / 12):.6f})")
    fix = np.array([1 + np.sqrt(3), 1, 1])
    print(f"    Kontrolle: F (1 + sqrt3, 1, 1) = (1 + sqrt3, 1, 1): {np.allclose(F @ fix, fix)}")

    print("\n(5) Verhaeltnis zum Slotzyklus tau")
    H = generate([tau, D], 3)
    def in_H(M):
        return any(np.allclose(M, h) for h in H)
    inv = np.linalg.inv
    print(f"    Heisenberg-Gruppe <tau, D>: {len(H)} Elemente; F tau F^-1 in ihr: {in_H(F @ tau @ inv(F))}; "
          f"F D F^-1: {in_H(F @ D @ inv(F))}; S tau S^-1: {in_H(S @ tau @ inv(S))}; S D S^-1: {in_H(S @ D @ inv(S))}")
    print(f"    F tau F^-1 = D oder D^-1: {np.allclose(F @ tau @ inv(F), D) or np.allclose(F @ tau @ inv(F), inv(D))}; "
          f"tau in <S, F> (projektiv): {any(abs(abs(np.trace(g.conj().T @ tau)) - 3) < 1e-9 for g in G3)}")

    print("\n(6) F als Summe monomialer Operationen: F = Summe c_ab tau^a D^b")
    basis = [(aa, bb, np.linalg.matrix_power(tau, aa) @ np.linalg.matrix_power(D, bb)) for aa in range(3) for bb in range(3)]
    coef = {(aa, bb): np.trace(M.conj().T @ F) / 3 for aa, bb, M in basis}
    rec = sum(coef[aa, bb] * M for aa, bb, M in basis)
    print(f"    Rekonstruktion exakt: {np.allclose(rec, F)}; Betraege der neun Koeffizienten: "
          f"{sorted({round(float(abs(c)), 6) for c in coef.values()})} (1/3 = {1 / 3:.6f})")

    print("\n(7) Allgemeines n: gerader Teil unter j -> -j und <e0|F|e0>")
    for n in (2, 3, 4, 5, 7):
        even = n // 2 + 1
        print(f"    n = {n}: gerader Teil Dimension {even}, ungerader {n - even}; <e0|F|e0> = 1/sqrt({n}) = {fourier(n)[0, 0].real:.6f}")
