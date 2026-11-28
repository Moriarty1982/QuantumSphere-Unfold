"""k455 (Test H239): Ist die Struktur von S zweimal RAIDZ2? Code C_x = Bild(L_x) fuer Nullteiler x.
Vorab Vorab_H239_RAIDZ2.md. Produkt wie k253/k321/k453/k454. Aufruf aus diesem Ordner: python3 k455_test_h239.py > k455_out.txt
"""
import itertools
import numpy as np

N = 16
rng = np.random.default_rng(455)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


E = np.eye(N)


def Lmat(x):
    return np.column_stack([mul(x, E[j]) for j in range(N)])


def rank(M, tol=1e-9):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > tol).sum())


def basis_of_image(M):
    U, s, _ = np.linalg.svd(M)
    return U[:, s > 1e-9]


def split_dims(C, grp):
    """dim(C cap span(e_grp)), dim(C cap span(e_rest)) for subspace C (columns orthonormal)."""
    rest = [i for i in range(N) if i not in grp]
    k = C.shape[1]
    # C cap span(grp): vectors in C with zero rest-coordinates -> null space of C[rest,:]
    d1 = k - rank(C[rest, :])
    d2 = k - rank(C[list(grp), :])
    return d1, d2


def group_code(C, grp):
    rest = [i for i in range(N) if i not in grp]
    Mrest = C[rest, :]
    _, s, Vt = np.linalg.svd(Mrest)
    s = np.concatenate([s, np.zeros(C.shape[1] - len(s))])
    null = Vt[s < 1e-9].T
    G = C[list(grp), :] @ null  # 8 x d generator of the group code
    return G


def erasure_profile(G):
    """G: 8 x d generator. Returns (all 2-erasures ok, all 3-erasures ok)."""
    d = rank(G)
    ok = {}
    for e in (1, 2, 3):
        ok[e] = all(rank(np.delete(G, list(S), axis=0)) == d for S in itertools.combinations(range(G.shape[0]), e))
    return d, ok


LOW = list(range(8))
HIGH = list(range(8, 16))

# --- Nullteiler-Stichproben
Z1 = []
for i in range(1, 8):
    for j in range(9, 16):
        if j == i + 8:
            continue
        for sg in (1, -1):
            Z1.append(((i, j, sg), (E[i] + sg * E[j]) / np.sqrt(2)))
Z2 = []; rejected = 0
while len(Z2) < 200:
    a = np.zeros(8); a[1:] = rng.normal(size=7); a /= np.linalg.norm(a)
    b = np.zeros(8); b[1:] = rng.normal(size=7); b -= (b @ a) * a; b /= np.linalg.norm(b)
    x = np.concatenate([a, b]) / np.sqrt(2)
    if rank(Lmat(x)) < 16:
        Z2.append(x)
    else:
        rejected += 1

if __name__ == "__main__":
    print("=" * 96)
    print("H239 (k455)  Zweimal RAIDZ2?  Code C_x = Bild(L_x), Ausfallrichtungen K_x = Kern(L_x)")
    print("=" * 96)


    def analyse(name, xs, scan_all=False):
        ranks = []; walls = []; prof = []; kerinfo = []; anysplit = 0
        for x in xs:
            L = Lmat(x); r = rank(L); ranks.append(r)
            C = basis_of_image(L)
            walls.append(split_dims(C, LOW))
            _, s, Vt = np.linalg.svd(L); s = np.concatenate([s, np.zeros(N - len(s))]); K = Vt[s < 1e-9].T
            kerinfo.append((K.shape[1] - rank(K[HIGH, :]), K.shape[1] - rank(K[LOW, :]), rank(K[LOW, :]), rank(K[HIGH, :])))
            if walls[-1] == (6, 6):
                prof.append(tuple(erasure_profile(group_code(C, g))[1][e] for g in (LOW, HIGH) for e in (2, 3)))
        print(f"\n{name}: {len(xs)} Nullteiler")
        print(f"  D1 Rang L_x: {sorted(set(ranks))}")
        print(f"  D2 Spaltung an der Wand e8 (dim C cap unten, dim C cap oben): {sorted(set(walls))}")
        print(f"  Kern: (dim K cap unten, dim K cap oben, Rang Proj unten, Rang Proj oben): {sorted(set(kerinfo))}")
        if prof:
            print(f"  D3 Profil (unten: 2 ok, 3 ok, oben: 2 ok, 3 ok): {sorted(set(prof))}")
        return ranks, walls, prof


    r1, w1, p1 = analyse("Z1 Basis-Diagonalen (e_i +- e_j)/sqrt2", [x for _, x in Z1])
    r2, w2, p2 = analyse(f"Z2 allgemeine Nullteiler (a,b)/sqrt2 (verworfen, weil regulaer: {rejected})", Z2)

    # --- alle 8+8-Aufteilungen fuer Z1
    print("\nZ1: Suche ueber alle 6435 Aufteilungen 8+8 (Gruppe enthaelt Koordinate 0)")
    parts = [g for g in itertools.combinations(range(N), 8) if 0 in g]
    found = {}
    for lab, x in Z1:
        C = basis_of_image(Lmat(x))
        hits = [g for g in parts if split_dims(C, list(g)) == (6, 6)]
        found[lab] = hits
    nh = [len(v) for v in found.values()]
    print(f"  Zahl der 6+6-Aufteilungen je Nullteiler: {sorted(set(nh))}")
    lab0 = Z1[0][0]
    print(f"  Beispiel {lab0}: {found[lab0][:6]}")
    common = set(found[Z1[0][0]])
    for v in found.values():
        common &= set(v)
    print(f"  gemeinsame Aufteilungen aller 84: {sorted(common)}")
    # profile fuer gefundene Aufteilungen
    profs = set()
    for lab, x in Z1:
        C = basis_of_image(Lmat(x))
        for g in found[lab]:
            rest = [i for i in range(N) if i not in g]
            profs.add(tuple(erasure_profile(group_code(C, list(gg)))[1][e] for gg in (list(g), rest) for e in (1, 2, 3)))
    print(f"  D3 an gefundenen Aufteilungen (G1: 1,2,3 ok; G2: 1,2,3 ok): {sorted(profs)}")

    # --- Kopien
    print("\nNur Bericht: dim(K_x cap V_k) fuer die Kopien V_k (H138)")
    vs = [(1.0, 0.0), (-0.5, np.sqrt(3) / 2), (-0.5, -np.sqrt(3) / 2)]
    Vk = [np.column_stack([E[0]] + [v0 * E[i] + v1 * E[8 + i] for i in range(1, 8)]) for v0, v1 in vs]
    for name, xs in (("Z1", [x for _, x in Z1]), ("Z2", Z2)):
        res = set()
        for x in xs:
            L = Lmat(x); _, s, Vt = np.linalg.svd(L); s = np.concatenate([s, np.zeros(N - len(s))]); K = Vt[s < 1e-9].T
            res.add(tuple(K.shape[1] + 8 - rank(np.hstack([K, V])) for V in Vk))
        print(f"  {name}: {sorted(res)}")

    # --- Zufallskontrolle
    print("\nZufallskontrolle")
    cnt_a = 0; cnt_b = 0; pa = 0; pb = 0
    for _ in range(2000):
        Q, _ = np.linalg.qr(rng.normal(size=(N, 12)))
        if split_dims(Q, LOW) == (6, 6):
            cnt_a += 1
        M = rng.normal(size=(N, 12)) @ rng.normal(size=(12, N))
        if split_dims(basis_of_image(M), LOW) == (6, 6):
            cnt_b += 1
    print(f"  zufaellige 12-dim Unterraeume: 6+6-Spaltung an der Wand in {cnt_a}/2000")
    print(f"  zufaellige Rang-12-Bilder:     6+6-Spaltung an der Wand in {cnt_b}/2000")
    # Kontrolle Paritaetsprofil: zufaelliger 6-dim Code in 8 Koordinaten
    pp = set()
    for _ in range(200):
        G = rng.normal(size=(8, 6)); pp.add(tuple(erasure_profile(G)[1][e] for e in (1, 2, 3)))
    print(f"  D3-Profil zufaelliger [8,6]-Codes (1,2,3 ok): {sorted(pp)}")

    okD1 = set(r1) == {12} and set(r2) == {12}
    okD2 = set(w1) == {(6, 6)} and set(w2) == {(6, 6)}
    okD3 = bool(p1) and set(p1) == {(True, False, True, False)} and set(p2) == {(True, False, True, False)}
    print("\n" + "=" * 96)
    print(f"D1 {okD1}, D2 (Wand, Z1 und Z2) {okD2}, D3 {okD3}, Kontrolle spaltet nie {cnt_a == 0 and cnt_b == 0}")
