"""Eine Generation je Frame-Abbildung (Erkundung, nicht blind).

Auf dem Dublett nach v4.9.0-r51: Zeitumkehr T = sigma_z, J_B = sigma_x,
Tachyon-Abbildung R: z -> iz (Eigenvektoren wie sigma_y).
Prueft: (1) Eigenbasen paarweise unverzerrt, (2) Bargmann-Phase je Wahl der
Eigenzustaende, (3) Wirkung von R (unitaer) und komplexer Konjugation
(antiunitaer) auf das Tripel.
"""
import itertools
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
R = np.array([[0, -1], [1, 0]], complex)  # z -> iz als reelle Drehung, R^2 = -1


def eig(m):
    w, v = np.linalg.eigh(m)
    return {int(round(x.real)): v[:, i] for i, x in enumerate(w)}


def eig_R():
    w, v = np.linalg.eig(R)
    return {complex(np.round(x, 12)): v[:, i] for i, x in enumerate(w)}


B = {"T(sz)": eig(sz), "JB(sx)": eig(sx), "R(sy)": eig(sy)}
print("R hat Eigenwerte", sorted(eig_R(), key=lambda c: c.imag), "; gleiche Eigenlinien wie sigma_y:",
      all(min(abs(abs(np.vdot(a, b)) - 1) for b in eig(sy).values()) < 1e-12 for a in eig_R().values()))

print("\n(1) Ueberlappungen zwischen den Basen")
names = list(B)
for a, b in itertools.combinations(names, 2):
    ov = {round(abs(np.vdot(u, v)) ** 2, 12) for u in B[a].values() for v in B[b].values()}
    print(f"  {a} vs {b}: |<u|v>|^2 in {sorted(ov)}")


def bargmann(s):
    a, b, c = s
    return np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, a))


def koide(s):
    G = np.array([[abs(np.vdot(u, v)) for v in s] for u in s])
    return np.trace(G @ G) / np.trace(G) ** 2


print("\n(2) Alle 8 Wahlen (je ein Eigenzustand aus T, J_B, R)")
for signs in itertools.product([1, -1], repeat=3):
    s = [B[n][e] for n, e in zip(names, signs)]
    bloch = [tuple(int(round(np.real(np.vdot(v, m @ v)))) for m in (sx, sy, sz)) for v in s]
    orient = int(round(np.linalg.det(np.array(bloch, float))))
    print(f"  Wahl {signs}: Phase/pi = {bargmann(s)/np.pi:+.4f}, K = {koide(s):.6f}, Orientierung {orient:+d}")

print("\n(3) Frame-Wechsel auf das Tripel (+,+,+)")
s0 = [B[n][1] for n in names]
sR = [R @ v for v in s0]
sK = [v.conj() for v in s0]
for lab, s in (("R (Tachyon, unitaer)", sR), ("Konjugation (antiunitaer)", sK)):
    print(f"  {lab}: Phase/pi = {bargmann(s)/np.pi:+.4f}, K = {koide(s):.6f}")
    for n, v in zip(names, s):
        hits = [e for e, u in B[n].items() if abs(abs(np.vdot(u, v)) - 1) < 1e-12]
        print(f"     {n}: Eigenzustand {hits}")
