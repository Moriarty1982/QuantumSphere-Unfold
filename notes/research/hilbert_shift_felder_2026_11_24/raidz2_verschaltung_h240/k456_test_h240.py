"""k456 (Test H240): Zwei RAIDZ2 anders verschaltet? Matroid-Komponenten des Nullteiler-Codes C_x = Bild(L_x),
Standard- und G2-angepasste Koordinaten, Zufallskontrolle. Vorab Vorab_H240_RAIDZ2_Verschaltung.md.
Produkt wie k253/k321/k453/k454/k455. Aufruf aus diesem Ordner: python3 k456_test_h240.py > k456_out.txt
"""
import itertools
import numpy as np

N = 16
rng = np.random.default_rng(456)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


E = np.eye(N); E8 = np.eye(8)


def Lmat(x):
    return np.column_stack([mul(x, E[j]) for j in range(N)])


def rank(M, tol=1e-9):
    return 0 if M.size == 0 else int((np.linalg.svd(M, compute_uv=False) > tol).sum())


def parity_check(L):
    U, s, _ = np.linalg.svd(L)
    r = int((s > 1e-9).sum())
    return U[:, r:].T  # (16-r) x 16, Zeilen spannen das orthogonale Komplement von C


def components(H):
    n = H.shape[1]
    par = list(range(n))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i

    def union(i, j):
        par[find(i)] = find(j)

    # Spaltenbasis gierig
    B = []
    for j in range(n):
        if rank(H[:, B + [j]]) > len(B):
            B.append(j)
    HB = H[:, B]
    for j in range(n):
        if j in B:
            continue
        if np.linalg.norm(H[:, j]) < 1e-9:
            continue  # Schleife von M(H): eigene Komponente
        c, *_ = np.linalg.lstsq(HB, H[:, j], rcond=None)
        for i, ci in enumerate(c):
            if abs(ci) > 1e-9:
                union(j, B[i])
    comps = {}
    for j in range(n):
        comps.setdefault(find(j), []).append(j)
    return sorted(comps.values(), key=lambda s: (len(s), s))


def comp_params(H, S, maxw=6):
    n = len(S); k = n - rank(H[:, S])
    if k == 0:
        return (n, 0, None)
    d = None
    for w in range(1, min(n, maxw) + 1):
        if any(rank(H[:, list(T)]) < w for T in itertools.combinations(S, w)):
            d = w; break
    return (n, k, d if d is not None else f">{maxw}")


def layout(x, coords=None):
    L = Lmat(x)
    if coords is not None:
        L = coords.T @ L @ coords
    H = parity_check(L)
    cs = components(H)
    return tuple(sorted(comp_params(H, S) for S in cs)), cs


# Nullteiler wie H239
Z1 = []
for i in range(1, 8):
    for j in range(9, 16):
        if j != i + 8:
            for sg in (1, -1):
                Z1.append(((i, j, sg), (E[i] + sg * E[j]) / np.sqrt(2)))


def rand_im8():
    a = np.zeros(8); a[1:] = rng.normal(size=7); return a / np.linalg.norm(a)


Z2 = []
for _ in range(200):
    a = rand_im8(); b = rand_im8(); b -= (b @ a) * a; b /= np.linalg.norm(b)
    Z2.append((a, b, np.concatenate([a, b]) / np.sqrt(2)))


def fmt(lay):
    from collections import Counter
    c = Counter(lay)
    return " + ".join(f"{m}x[{n},{k},{d}]" for (n, k, d), m in sorted(c.items(), key=lambda t: (t[0][0], t[0][1])))


print("=" * 96)
print("H240 (k456)  Zwei RAIDZ2 anders verschaltet?  Komponenten [n,k,d] des Codes C_x = Bild(L_x)")
print("=" * 96)
print("\nTeil A1 (nicht blind): Kapazitaeten  V1 RAID1 ueber 2xRAIDZ2 = 6/16, V3 Produkt 4x4 = 9/16, V3' 4xRAID5 = 12/16, V2 = 12/16; C_x hat 12/16")
print("  -> V1 und V3 (Zeilen+Spalten) scheiden an der Kapazitaet aus.")

lays1 = {}
for lab, x in Z1:
    lay, cs = layout(x); lays1.setdefault(lay, []).append((lab, cs))
print(f"\nTeil A2 Z1 (84 Basis-Diagonalen): {len(lays1)} verschiedene Zerlegung(en)")
for lay, items in lays1.items():
    print(f"  {fmt(lay)}   ({len(items)} Nullteiler), Beispiel {items[0][0]}: Komponenten {[c for c in items[0][1] if len(c) > 1]}")
lays2 = {}
for a, b, x in Z2:
    lay, cs = layout(x); lays2.setdefault(lay, []).append(cs)
print(f"\nTeil A2 Z2 (200 allgemeine Nullteiler): {len(lays2)} verschiedene Zerlegung(en)")
for lay, items in lays2.items():
    print(f"  {fmt(lay)}   ({len(items)} Nullteiler), Einzelkomponenten: {[c for c in items[0] if len(c) == 1]}")
target = [((8, 6, 3), (8, 6, 3)), tuple([(4, 3, 2)] * 4)]
hitA = any(lay in target for lay in list(lays1) + list(lays2))
coloops = all(any(p == (1, 1, 1) for p in lay) for lay in list(lays1) + list(lays2))
print(f"\n  zwei [8,6,3] oder vier [4,3,2] gefunden: {hitA}")
print(f"  A3: ungeschuetzte Koordinaten [1,1,1] in jedem Nullteiler-Code: {coloops}  -> V4 (jede Platte geschuetzt) scheidet aus: {coloops}")

# --- Teil B: G2-angepasste Koordinaten
print("\nTeil B: G2-angepasste Koordinaten")
e = E8


def sgn(p, q):
    v = np.round(p, 9); idx = np.nonzero(v)[0]; assert len(idx) == 1
    return idx[0], v[idx[0]]


i3, s3 = sgn(mul(e[1], e[2]), None); i5, s5 = sgn(mul(e[1], e[4]), None)
i6, s6 = sgn(mul(e[2], e[4]), None); i7, s7 = sgn(mul(mul(e[1], e[2]), e[4]), None)
print(f"  Konvention: e1 e2 = {s3:+.0f} e{i3}, e1 e4 = {s5:+.0f} e{i5}, e2 e4 = {s6:+.0f} e{i6}, (e1 e2) e4 = {s7:+.0f} e{i7}")


def g2_frame(a, b):
    ab = mul(a, b)
    c = np.zeros(8); c[1:] = rng.normal(size=7)
    for v in (a, b, ab):
        c -= (c @ v) * v
    c /= np.linalg.norm(c)
    F = np.zeros((8, 8)); F[:, 0] = e[0]; F[:, 1] = a; F[:, 2] = b; F[:, 4] = c
    F[:, i3] = s3 * ab; F[:, i5] = s5 * mul(a, c); F[:, i6] = s6 * mul(b, c); F[:, i7] = s7 * mul(ab, c)
    return F


maxdev_o = maxdev_s = maxorth = 0.0; laysB = {}; b2 = set()
for a, b, x in Z2:
    F = g2_frame(a, b)
    maxorth = max(maxorth, np.abs(F.T @ F - np.eye(8)).max())
    for p in range(8):
        for q in range(8):
            maxdev_o = max(maxdev_o, np.abs(mul(F[:, p], F[:, q]) - F @ mul(e[p], e[q])).max())
    G = np.zeros((16, 16)); G[:8, :8] = F; G[8:, 8:] = F
    for _ in range(3):
        X = rng.normal(size=16); Y = rng.normal(size=16)
        maxdev_s = max(maxdev_s, np.abs(mul(G @ X, G @ Y) - G @ mul(X, Y)).max())
    lay, cs = layout(x, coords=G); laysB.setdefault(lay, []).append(cs)
    # B2 invariant
    L = Lmat(x); U, s, _ = np.linalg.svd(L); C = U[:, s > 1e-9]
    _, s2, Vt = np.linalg.svd(L); Kr = Vt[np.concatenate([s2, np.zeros(16 - len(s2))]) < 1e-9].T
    Hq = np.column_stack([F[:, k] for k in range(4)])
    Hblk = np.zeros((16, 8)); Hblk[:8, :4] = Hq; Hblk[8:, 4:] = Hq
    Qc = np.zeros((16, 8)); Qc[:8, :4] = F[:, 4:]; Qc[8:, 4:] = F[:, 4:]
    inC = rank(np.hstack([C, Hblk])) == 12
    capQ = 12 + 8 - rank(np.hstack([C, Qc]))
    kerQ = rank(np.hstack([Qc, Kr])) == 8
    b2.add((inC, capQ, kerQ))
print(f"  Rahmen orthonormal (max Abw.) {maxorth:.1e}; Automorphismus von O (max Abw.) {maxdev_o:.1e}; diagonal auf S (max Abw.) {maxdev_s:.1e}")
print(f"  Zerlegungen in angepassten Koordinaten (200 Nullteiler): {len(laysB)}")
for lay, items in laysB.items():
    print(f"    {fmt(lay)}   ({len(items)}), Paare: {[c for c in items[0] if len(c) == 2]}")
ref = layout((E[1] + E[10]) / np.sqrt(2))[0]
print(f"  Basis-Nullteiler (e1 + e10)/sqrt2 in Standardkoordinaten: {fmt(ref)};  gleich: {set(laysB) == {ref}}")
print(f"  B2 (C_x enthaelt H_x + H_x e8, dim(C_x cap Komplement), Kern im Komplement): {sorted(b2)}")

# --- Zufallskontrolle
print("\nZufallskontrolle: 200 zufaellige [16,12]-Codes")
rl = {}
for _ in range(200):
    M = rng.normal(size=(16, 12)) @ rng.normal(size=(12, 16))
    H = parity_check(M); cs = components(H)
    lay = tuple(sorted(comp_params(H, S, maxw=5) for S in cs)); rl[lay] = rl.get(lay, 0) + 1
for lay, m in rl.items():
    print(f"  {fmt(lay)}   ({m})")

print("\n" + "=" * 96)
fixed = len(laysB) == 1
print(f"Zwei-RAIDZ2-Verschaltung gefunden: {hitA}; feste Verschaltung in angepassten Koordinaten: {fixed}; ungeschuetzte Platten: {coloops}")
