"""k453 (Test H237): Wellenfaehige Richtungen und stabile Bereiche in den Sedenionen. Vorab Vorab_H237_Sedenion_Bereiche.md (Commit 2f68c37).
Produkt wie k253/k321: (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c)).
Aufruf aus diesem Ordner: python3 k453_test_h237.py > k453_out.txt
"""
import itertools
import numpy as np
from scipy.linalg import null_space

rng = np.random.default_rng(453)
N = 16


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
LB = [np.array([mul(E[i], E[k]) for k in range(N)]).T for i in range(N)]   # L_{e_i}, Spalte k = e_i e_k


def Lmat(u):
    return sum(u[i] * LB[i] for i in range(N))


def wave(U):
    """U: Liste orthonormaler Imaginaerrichtungen -> (delta, dim W, Basis W)"""
    Ls = [Lmat(u) for u in U]
    Ks = []
    d = 0.0
    for a in range(len(U)):
        for b in range(a, len(U)):
            K = Ls[a] @ Ls[b] + Ls[b] @ Ls[a] + 2 * (a == b) * np.eye(N)
            d = max(d, np.abs(K).max())
            Ks.append(K)
    # absolute Toleranz (relative rcond zaehlt bei K = 0 das Rauschen als Rang; erster Lauf)
    M = np.vstack(Ks)
    _, sv, Vt = np.linalg.svd(M)
    sv = np.concatenate([sv, np.zeros(N - len(sv))])
    W = Vt[sv < 1e-9].T
    return d, W.shape[1], W


def is_subspace_of(B, W, tol=1e-9):
    """liegt span(B) in span(W)?"""
    P = W @ W.T
    return np.abs(B - B @ P.T).max() < tol if W.shape[1] else False


print("=" * 100)
print("H237 (k453)  Wellenfaehige Richtungen und stabile Bereiche in den Sedenionen")
print("=" * 100)

# ---- Teil A ----
print("\nTeil A (blind): die drei G2-stabilen Oktonion-Kopien O_v (H138), v = (1,0), (-1/2, +-sqrt3/2)")
copies = {"V1 v=(1,0)": (1.0, 0.0), "V2 v=(-1/2,+sqrt3/2)": (-0.5, np.sqrt(3) / 2), "V3 v=(-1/2,-sqrt3/2)": (-0.5, -np.sqrt(3) / 2)}
resA = {}
for name, (v0, v1) in copies.items():
    U = [v0 * E[i] + v1 * E[8 + i] for i in range(1, 8)]
    d, dw, W = wave(U)
    Vb = np.array([E[0]] + U)
    inside = is_subspace_of(Vb, W)
    resA[name] = (d, dw)
    print(f"  {name}: Wellendefekt delta = {d:.3e}, dim W = {dw}, Kopie selbst in W: {inside}")
    if dw > 8:
        # was liegt zusaetzlich in W? Projektion auf das Komplement der Kopie
        P = Vb.T @ Vb
        extra = W - P @ W
        r = np.linalg.matrix_rank(extra, tol=1e-9)
        print(f"     W reicht ueber die Kopie hinaus: {r} zusaetzliche Richtungen")
    # passt eine 8. Richtung dazu? Kandidat e8 (G2-Singulett, die Wand l)
    d8, dw8, _ = wave(U + [E[8]])
    print(f"     mit 8. Richtung e8 (G2-Singulett): delta = {d8:.1e}, dim W = {dw8}")
okT = all(d < 1e-9 for d, dw in resA.values())
okTT = any(d < 1e-9 for d, dw in resA.values()) or any(dw > 8 for d, dw in resA.values())
verdict = "TRAEGT" if okT else ("TRAEGT TEILWEISE" if okTT else "WIDERLEGT")
print(f"  Teil A Urteil: {verdict}")

# ---- Teil B1/B2 ----
print("\nTeil B1/B2: Basis-Unteralgebren (Basisprodukt e_i e_j = +-e_(i xor j) -> Untergruppen von (Z2)^4)")
idx = np.array([[int(np.argmax(np.abs(mul(E[i], E[j])))) for j in range(N)] for i in range(N)])
print(f"  Kontrolle e_i e_j ~ e_(i xor j): {all(idx[i, j] == i ^ j for i in range(N) for j in range(N))}")


def subgroups(dim):
    out = set()
    k = int(np.log2(dim))
    for gens in itertools.combinations(range(1, N), k):
        S = {0}
        for g in gens:
            S |= {s ^ g for s in S}
        if len(S) == dim:
            out.add(frozenset(S))
    return sorted(out, key=sorted)


def algebra_props(S):
    B = [E[i] for i in sorted(S)]
    dim = len(B)
    alt = nm = 0.0
    for _ in range(200):
        c = rng.normal(size=(2, dim))
        a = sum(c[0, i] * B[i] for i in range(dim)); b = sum(c[1, i] * B[i] for i in range(dim))
        alt = max(alt, np.abs(mul(mul(a, a), b) - mul(a, mul(a, b))).max(), np.abs(mul(mul(b, a), a) - mul(b, mul(a, a))).max())
        nm = max(nm, abs(mul(mul(a, b), conj(mul(a, b)))[0] - mul(a, conj(a))[0] * mul(b, conj(b))[0]))
    # Nullteiler innerhalb: e_i +- e_j
    zd = False
    cands = [E[i] + s * E[j] for i in sorted(S) for j in sorted(S) if j > i for s in (1, -1)]
    for x in cands:
        for y in cands:
            if np.abs(mul(x, y)).max() < 1e-12:
                zd = True; break
        if zd:
            break
    return alt < 1e-9, nm < 1e-9, zd


for dim in (2, 4, 8):
    subs = subgroups(dim)
    stats = [algebra_props(S) for S in subs]
    n_alt = sum(s[0] for s in stats); n_nm = sum(s[1] for s in stats); n_zd = sum(s[2] for s in stats)
    print(f"  dim {dim}: {len(subs)} Basis-Unteralgebren; alternativ {n_alt}, Norm multiplikativ {n_nm}, mit Nullteilern (e_i+-e_j) {n_zd}")
    if dim == 8:
        print("   B2: je 8-dim Basis-Unteralgebra: Typ, Wellendefekt ihres Imaginaerteils auf ganz S, dim W")
        for S, st in zip(subs, stats):
            U = [E[i] for i in sorted(S) if i]
            d, dw, W = wave(U)
            typ = "Oktonion" if st[0] and st[1] and not st[2] else "Quasi-Oktonion (nicht alternativ)"
            print(f"    {sorted(S)}: {typ:34s} delta = {d:.2f}, dim W = {dw}")

# ---- B3 ----
d, dw, W = wave([E[i] for i in range(1, N)])
print(f"\nTeil B3: ganz Im S (15 Richtungen): delta = {d:.2f}, dim W = {dw}" + (f", W = span{[np.round(W[:, k], 3).tolist() for k in range(dw)]}" if 0 < dw <= 2 else ""))

# ---- B4 ----
print("\nTeil B4: maximale Clifford-Mengen aus Basiseinheiten (L_i^2 = -1, paarweise L_i L_j + L_j L_i = 0 auf ganz S)")
sq = [np.abs(LB[i] @ LB[i] + np.eye(N)).max() < 1e-12 for i in range(1, N)]
print(f"  L_i^2 = -1 fuer alle 15 Basiseinheiten: {all(sq)}")
adj = {i: {j for j in range(1, N) if j != i and np.abs(LB[i] @ LB[j] + LB[j] @ LB[i]).max() < 1e-12} for i in range(1, N)}
cliques = []


def bk(R, P, X):
    if not P and not X:
        cliques.append(R); return
    for v in list(P):
        bk(R | {v}, P & adj[v], X & adj[v]); P = P - {v}; X = X | {v}


bk(set(), set(range(1, N)), set())
mx = max(len(c) for c in cliques)
best = [sorted(c) for c in cliques if len(c) == mx]
print(f"  groesste Clifford-Menge: {mx} Einheiten; Anzahl solcher Mengen: {len(best)}")
for c in best[:10]:
    print(f"    {c}")
copy1 = set(range(1, 8))
print(f"  enthaelt eine groesste Menge die 7 Imaginaereinheiten der Kopie V1 = {{e1..e7}}? {any(copy1 <= set(c) for c in best)}")
sizes = sorted({len(c) for c in cliques})
print(f"  Groessen aller maximalen (nicht erweiterbaren) Mengen: {sizes}")
for c in best[:3]:
    d, dw, W = wave([E[i] for i in c])
    print(f"    Menge {c}: delta = {d:.1e}, dim W = {dw} (ganz S = 16)")

print("\nTeil B5 (analytisch, statt Stichprobe): jedes U mit delta(U) = 0 auf ganz S liefert dim U antikommutierende komplexe Strukturen auf R^16;")
print("  nach Hurwitz-Radon ist dim U <= rho(16) - 1 = 8. Groesser als die Basis-Mengen aus B4 geht es also nicht.")

print("\n" + "=" * 100)
print(f"H237 Gesamturteil (Teil A): {verdict}")
