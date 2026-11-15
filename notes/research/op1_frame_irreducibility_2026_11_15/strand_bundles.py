"""Penrose-Buendel: Spin j als Sym^{2j} eines Dubletts; bosonische gegen fermionische Straenge (Erkundung, nicht blind).

(1) Auf Sym^n(C^2) (n = 2j) ist sigma_k^{(x)n} gleich exp(-i pi J_k) bis auf eine Phase (k = x, y, z).
(2) Lambda^n(C^2): Dimensionen und Spins (n = 1: j = 1/2; n = 2: j = 0; n >= 3: leer).
(3) Die ausgerichteten Buendel |up>^n, |down>^n sind in Sym^n genau |j, +-j>.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm

sig = {"x": np.array([[0, 1], [1, 0]], complex), "y": np.array([[0, -1j], [1j, 0]]), "z": np.diag([1, -1]).astype(complex)}


def kron_n(M, n):
    out = np.eye(1, dtype=complex)
    for _ in range(n): out = np.kron(out, M)
    return out


def dicke(n):
    """Orthonormale Basis von Sym^n(C^2): Spalte k = Dicke-Zustand mit k Einsen (m = n/2 - k)."""
    B = np.zeros((2 ** n, n + 1), complex)
    for idx in range(2 ** n):
        k = bin(idx).count("1"); B[idx, k] += 1
    return B / np.linalg.norm(B, axis=0)


def spin(j):
    m = np.arange(j, -j - 1, -1); dd = len(m); Jp = np.zeros((dd, dd), complex)
    for k in range(1, dd): Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return {"x": (Jp + Jp.conj().T) / 2, "y": (Jp - Jp.conj().T) / 2j, "z": np.diag(m).astype(complex)}


print("(1) Sym^n: sigma^{(x)n} gegen exp(-i pi J) (bis auf Phase)")
for n in range(1, 9):
    B = dicke(n); j = n / 2; J = spin(j)
    devs = []
    for k in "xyz":
        S = B.conj().T @ kron_n(sig[k], n) @ B
        E = expm(-1j * np.pi * J[k])
        ph = np.trace(E.conj().T @ S) / (n + 1)
        devs.append(np.abs(S - ph * E).max())
    print(f"    n = {n} (j = {j}): max. Abweichung {max(devs):.1e}")

print("(2) Lambda^n(C^2): antisymmetrische Potenzen")
for n in range(1, 5):
    dim = math.comb(2, n)
    spin_label = {1: "j = 1/2 (Dublett, Frame-Abbildungen irreduzibel)", 2: "j = 0 (Singulett, keine Flaeche)"}.get(n, "leer")
    # Kontrolle: Projektor auf total antisymmetrische Zustaende in (C^2)^n
    P = np.zeros((2 ** n, 2 ** n))
    for perm in itertools.permutations(range(n)):
        sgn = np.linalg.det(np.eye(n)[list(perm)])
        M = np.zeros((2 ** n, 2 ** n))
        for idx in range(2 ** n):
            bits = [(idx >> (n - 1 - p)) & 1 for p in range(n)]
            nb = [bits[perm[p]] for p in range(n)]
            M[int("".join(map(str, nb)), 2), idx] = 1
        P += sgn * M
    P /= math.factorial(n)
    print(f"    n = {n}: Dimension {dim} (Rang des Projektors {np.linalg.matrix_rank(P, 1e-9)}): {spin_label}")

print("(3) Ausgerichtete Buendel |up>^n, |down>^n = |j, +j>, |j, -j>")
for n in (2, 3, 5):
    B = dicke(n); up = np.zeros(2 ** n); up[0] = 1; dn = np.zeros(2 ** n); dn[-1] = 1
    cu, cd = B.conj().T @ up, B.conj().T @ dn
    print(f"    n = {n}: |up>^n -> Komponente m = +j: {abs(cu[0]):.3f}; |down>^n -> m = -j: {abs(cd[-1]):.3f}")
