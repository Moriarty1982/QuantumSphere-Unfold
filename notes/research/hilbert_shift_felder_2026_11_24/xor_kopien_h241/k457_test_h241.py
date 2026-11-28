"""k457 (Test H241): Klartext-Block B_x eines Nullteilers vs. die drei G2-Kopien; XOR-Relationen.
Vorab Vorab_H241_XOR_Kopien.md. Produkt wie k253/k321/k453-k456. Aufruf aus diesem Ordner: python3 k457_test_h241.py > k457_out.txt
"""
import itertools
import numpy as np

N = 16
rng = np.random.default_rng(457)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


E = np.eye(N); e8 = np.eye(8)


def rank(M, tol=1e-9):
    return 0 if M.size == 0 else int((np.linalg.svd(M, compute_uv=False) > tol).sum())


def orth(M):
    U, s, _ = np.linalg.svd(M, full_matrices=False); return U[:, s > 1e-9]


def cap(A, B):
    return rank(A) + rank(B) - rank(np.hstack([A, B]))


def is_algebra(B):
    """B: 16 x 8 orthonormal. Abgeschlossen, alternativ, normmultiplikativ?"""
    P = B @ B.T
    clo = max(np.abs(mul(B[:, i], B[:, j]) - P @ mul(B[:, i], B[:, j])).max() for i in range(B.shape[1]) for j in range(B.shape[1]))
    alt = nm = 0.0
    for _ in range(30):
        x = B @ rng.normal(size=B.shape[1]); y = B @ rng.normal(size=B.shape[1])
        alt = max(alt, np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max(), np.abs(mul(mul(y, x), x) - mul(y, mul(x, x))).max())
        nm = max(nm, abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)))
    return clo < 1e-9, alt < 1e-9, nm < 1e-9


vs = [(1.0, 0.0), (-0.5, np.sqrt(3) / 2), (-0.5, -np.sqrt(3) / 2)]


def u(v, q):
    return np.concatenate([v[0] * q, v[1] * q])


V = [np.column_stack([E[0]] + [u(v, e8[i]) for i in range(1, 8)]) for v in vs]

Z1 = []
for i in range(1, 8):
    for j in range(9, 16):
        if j != i + 8:
            for sg in (1, -1):
                a = e8[i]; b = sg * e8[j - 8]
                Z1.append(((i, j, sg), a, b))


def rand_im8():
    a = np.zeros(8); a[1:] = rng.normal(size=7); return a / np.linalg.norm(a)


Z2 = []
for _ in range(200):
    a = rand_im8(); b = rand_im8(); b -= (b @ a) * a; b /= np.linalg.norm(b)
    Z2.append((None, a, b))


def block(a, b):
    hq = [e8[0], a, b, mul(a, b)]
    z = np.zeros(8)
    return orth(np.column_stack([np.concatenate([h, z]) for h in hq] + [np.concatenate([z, h]) for h in hq]))


# Basis-Unteralgebren (Hyperebenen von (Z2)^4) und ihr Typ
hyper = []
for f in range(1, 16):
    S = [k for k in range(16) if bin(k & f).count("1") % 2 == 0]
    B = np.column_stack([E[k] for k in S])
    c, al, nm = is_algebra(B)
    hyper.append((f, S, "Oktonion" if (al and nm) else "Quasi-Oktonion", c))

if __name__ == "__main__":
    print("=" * 96)
    print("H241 (k457)  Klartext-Block B_x = H_x + H_x e8 vs. drei G2-Kopien; XOR-Relationen")
    print("=" * 96)
    print("\nTeil A: Lage des Blocks")
    for name, Z in (("Z1 (84 Basis-Nullteiler)", Z1), ("Z2 (200 allgemeine)", Z2)):
        caps = set(); inside = 0; algs = set(); xin = set(); which = {}
        for lab, a, b in Z:
            B = block(a, b)
            x = np.concatenate([a, b]) / np.sqrt(2)
            caps.add(tuple(cap(B, Vk) for Vk in V))
            inside += any(cap(B, Vk) == 8 for Vk in V)
            algs.add(is_algebra(B))
            xin.add((rank(np.hstack([B, x[:, None]])) == 8, rank(np.hstack([B, E[8][:, None]])) == 8))
            if lab is not None:
                S = tuple(k for k in range(16) if np.linalg.norm(B.T @ E[k]) > 1 - 1e-9)
                t = [h for h in hyper if tuple(h[1]) == S]
                which.setdefault(t[0][2] if t else "keine Basis-Unteralgebra", []).append(lab)
        print(f"  {name}: dim(B_x cap V_k) = {sorted(caps)}; B_x in einer Kopie: {inside}; (abgeschlossen, alternativ, normmult.) = {sorted(algs)};"
              f" (x in B_x, e8 in B_x) = {sorted(xin)}")
        if which:
            print(f"    A-blind: Typ von B_x unter den 15 Basis-Unteralgebren: { {k: len(v) for k, v in which.items()} }")
    print("  Typen der 15 Basis-Unteralgebren (Funktional f -> Typ): " + ", ".join(f"{h[0]}:{'O' if h[2]=='Oktonion' else 'Q'}" for h in hyper))
    print(f"  Oktonionen: {sum(h[2]=='Oktonion' for h in hyper)}, Quasi-Oktonionen: {sum(h[2]!='Oktonion' for h in hyper)}; alle abgeschlossen: {all(h[3] for h in hyper)}")
    print(f"  Oktonionen, die e8 enthalten: {[h[0] for h in hyper if h[2]=='Oktonion' and 8 in h[1]]}; Oktonion ohne e8: {[h[0] for h in hyper if h[2]=='Oktonion' and 8 not in h[1]]}")

    print("\nTeil B1: e_i e_j = +- e_(i XOR j)")
    ok = all(abs(abs(mul(E[i], E[j])[i ^ j]) - 1) < 1e-12 and np.count_nonzero(np.round(mul(E[i], E[j]), 12)) == 1 for i in range(16) for j in range(16))
    print(f"  alle 256 Paare: {ok}")

    print("\nTeil B2: Bueschel aus drei Basis-Unteralgebren (f3 = f1 XOR f2)")
    pencils = []
    for f1, f2 in itertools.combinations(range(1, 16), 2):
        f3 = f1 ^ f2
        if f3 > f2:
            pencils.append((f1, f2, f3))
    types = {h[0]: h[2] for h in hyper}
    sets = {h[0]: set(h[1]) for h in hyper}
    rel = all((sets[a] ^ sets[b]) == set(range(16)) - sets[c] for a, b, c in pencils)
    from collections import Counter
    combo = Counter(tuple(sorted("O" if types[f] == "Oktonion" else "Q" for f in p)) for p in pencils)
    print(f"  Zahl der Bueschel: {len(pencils)}; H1 Delta H2 = Komplement H3 in allen: {rel}")
    print(f"  Typenkombinationen: {dict(combo)}")

    print("\nTeil B3: Parität der G2-Kopien")
    res = max(np.abs(sum(u(v, q) for v in vs)).max() for q in [rand_im8() for _ in range(50)])
    print(f"  max |u1(q)+u2(q)+u3(q)| ueber 50 q: {res:.1e}")
    hits = 0
    for _ in range(10000):
        th = rng.uniform(0, np.pi, 3)
        w = [np.array([np.cos(t), np.sin(t)]) for t in th]
        best = min(np.linalg.norm(w[0] + s1 * w[1] + s2 * w[2]) for s1 in (1, -1) for s2 in (1, -1))
        hits += best < 1e-6
    print(f"  Zufallskontrolle: Anteil zufaelliger Winkel-Tripel mit Paritaet: {hits}/10000")

    print("\nTeil B4: Vertraeglichkeit mit dem Produkt")
    d1 = 0.0
    for _ in range(50):
        p = rand_im8(); q = rand_im8()
        for k in range(3):
            prod = mul(u(vs[k], p), u(vs[k], q))
            pred = -(p @ q) * E[0] + u(vs[k], mul(p, q) + (p @ q) * e8[0])  # u(Im(pq))
            d1 = max(d1, np.abs(prod - pred).max())
    print(f"  u_k(p) u_k(q) = -(p.q) + u_k(Im pq) fuer alle drei Kopien (max Abw.): {d1:.1e}  -> q -> u_k(q) ist fuer jedes k ein Isomorphismus von O")
    par = set()
    for _, a, b in Z2:
        B = block(a, b)
            # Schnitte explizit
        caps_ = []
        for Vk in V:
            M = np.hstack([B, -Vk]); _, s, Vt = np.linalg.svd(M); s = np.concatenate([s, np.zeros(M.shape[1] - len(s))])
            ns = Vt[s < 1e-9].T; caps_.append(orth(B @ ns[:B.shape[1], :]))
        par.add(rank(np.hstack([caps_[0], caps_[1], caps_[2]])) == rank(np.hstack([caps_[0], caps_[1]])))
    print(f"  Paritaet im Block: B_x cap V3 in (B_x cap V1)+(B_x cap V2) fuer alle 200: {par == {True}}")

    print("\nNur Bericht (nachtraeglich): Produkt ueber Kreuz u1(p) u2(q), Anteil in V3 im Vergleich zu V1, V2 und Zufall")
    fr = np.zeros(3); fr_r = 0.0
    for _ in range(500):
        p = rand_im8(); q = rand_im8()
        z = mul(u(vs[0], p), u(vs[1], q))
        for k in range(3):
            fr[k] += np.linalg.norm(V[k].T @ z) ** 2 / np.linalg.norm(z) ** 2
        Rr = orth(rng.normal(size=(16, 8))); fr_r += np.linalg.norm(Rr.T @ z) ** 2 / np.linalg.norm(z) ** 2
    print(f"  mittlerer Anteil in V1, V2, V3: {np.round(fr / 500, 4)}; zufaelliger 8-dim Raum: {fr_r / 500:.4f}")

    print("\n" + "=" * 96)
