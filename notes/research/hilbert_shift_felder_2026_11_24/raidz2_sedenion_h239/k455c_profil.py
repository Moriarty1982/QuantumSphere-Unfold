"""k455c (nachtraeglich, nur Bericht): Ausfallprofil des ganzen [16,12]-Codes C_x = Bild(L_x) und Blockstruktur der Basis-Nullteiler.
Aufruf aus diesem Ordner: python3 k455c_profil.py > k455c_out.txt
"""
import itertools
import numpy as np
from k455_test_h239 import Lmat, E, N, rank, basis_of_image, Z1, Z2, rng  # noqa: E402  (laeuft k455 beim Import nicht neu: siehe Guard unten)


def parity(L):
    U, s, _ = np.linalg.svd(L)
    return U[:, s <= 1e-9].T if (s <= 1e-9).any() else U[:, 12:].T


def profile(H):
    out = {}
    for e in (1, 2, 3, 4):
        out[e] = sum(rank(H[:, list(S)]) < e for S in itertools.combinations(range(N), e))
    return out


def two_per_half_ok(H):
    bad = 0
    for S1 in itertools.combinations(range(8), 2):
        for S2 in itertools.combinations(range(8, 16), 2):
            S = list(S1 + S2)
            bad += rank(H[:, S]) < 4
    return bad


print("k455c: Ausfallprofil = Zahl der NICHT rekonstruierbaren Ausfallmengen der Groesse 1..4 (von 16, 120, 560, 1820)")
print("        und Zahl der nicht rekonstruierbaren Muster '2 unten + 2 oben' (von 784)")
for name, xs in (("Z1 Basis-Diagonalen", [x for _, x in Z1[:12]]), ("Z2 allgemein", Z2[:12])):
    res = set()
    for x in xs:
        L = Lmat(x); U, s, _ = np.linalg.svd(L); H = U[:, 12:].T
        p = profile(H); res.add((p[1], p[2], p[3], p[4], two_per_half_ok(H)))
    print(f"  {name} (12 Stueck): {sorted(res)}")
res = set()
for _ in range(12):
    H = rng.normal(size=(4, 16)); p = profile(H); res.add((p[1], p[2], p[3], p[4], two_per_half_ok(H)))
print(f"  Zufallskontrolle (12 zufaellige [16,12]-Codes): {sorted(res)}")

print("\nBlockstruktur Basis-Nullteiler: L_x bildet e_k auf eine Summe zweier Basiseinheiten ab -> Paare {p,q}")
lab, x = Z1[0]
L = Lmat(x) * np.sqrt(2)
pairs = {}
for k in range(N):
    sup = tuple(np.nonzero(np.abs(L[:, k]) > 1e-9)[0])
    pairs.setdefault(tuple(sorted(sup)), []).append(k)
for sup, ks in sorted(pairs.items()):
    sub = L[np.ix_(list(sup), ks)]
    print(f"  Ziel {sup} <- Quellen {ks}: Rang {rank(sub)}")
print(f"  ({lab}): Paare mit Rang 2 = Klartext, Paare mit Rang 1 = Spiegel (Wiederholungscode, RAID1)")

print("\nZ2: ungeschuetzte Einzelkoordinaten (Spalte der Paritaetspruefung = 0) und 6+6-Spaltungen ueber alle 6435 Aufteilungen (5 Stueck)")
from k455_test_h239 import split_dims  # noqa: E402
parts = [g for g in itertools.combinations(range(N), 8) if 0 in g]
for x in Z2[:5]:
    L = Lmat(x); U, s, _ = np.linalg.svd(L); H = U[:, 12:].T
    unprot = [k for k in range(N) if np.linalg.norm(H[:, k]) < 1e-9]
    C = basis_of_image(L)
    nsplit = sum(split_dims(C, list(g)) == (6, 6) for g in parts)
    print(f"  ungeschuetzt: {unprot}; 6+6-Aufteilungen: {nsplit}")
