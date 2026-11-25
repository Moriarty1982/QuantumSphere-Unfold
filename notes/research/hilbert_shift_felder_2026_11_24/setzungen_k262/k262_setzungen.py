"""k262 (Erkundung, nicht blind, 25.11.2026): Welche Setzung aus H131 traegt die Spannung?
Teil 1: die 24 Elemente aus k260 auf dem Triplett z_k = s_k + i v_k (wie k261); Wirkung getrennt auf s (Realteil, ohne Ladung) und v (Ladungsrichtung).
Teil 2 (Lesart A, wie H131): Neutrinos als komplexes Triplett z (Majorana), ungerade Elemente antilinear. ALLE Paare von Untergruppen (G_e, G_nu).
Teil 3 (Lesart B): Neutrinos als reelles Triplett s (Majorana-Masse = reelle quadratische Form), alle 24 Elemente linear. ALLE Paare (G_e, G_nu).
Geladene Leptonen in beiden Lesarten auf z (hermitesche Form, ungerade Elemente antilinear).
Aufruf: python3 k262_setzungen.py   (benutzt ../kollaps_h128/k283_test_h128.py)
"""
import sys, os, itertools, numpy as np
from collections import Counter, defaultdict
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'kollaps_h128'))
import k283_test_h128 as k
rng = np.random.default_rng(262)
n = 4; J, T, d, N = k.albert(n); E = np.eye(d)

# ---------- Teil 1: Gruppe aus k260 (Aufbau wie k261) ----------
def rot(phi):
    M = np.eye(d); c, sn = np.cos(phi), np.sin(phi)
    for i in range(1, 8): M[i, i] = c; M[i + 8, i] = sn; M[i, i + 8] = -sn; M[i + 8, i + 8] = c
    return M
rho = rot(2 * np.pi / 3); refl = np.diag([1.0] * 8 + [-1.0] * 8)
S3 = [np.eye(d), rho, rho @ rho, refl, refl @ rho, refl @ rho @ rho]
copies = [np.linalg.matrix_power(rho, kk)[:, :8].T for kk in range(3)]
us = [np.linalg.matrix_power(rho, kk) @ E[7] for kk in range(3)]
pos = [(1, 2), (2, 0), (0, 1)]
Bm = np.zeros((N, 3, 3, d))
for kk in range(3): Bm[kk, kk, kk, 0] = 1.0
for kk, (i, j) in enumerate(pos):
    for p in range(d):
        ee = np.zeros(d); ee[p] = 1 / np.sqrt(2); Bm[3 + kk * d + p, i, j] = ee; Bm[3 + kk * d + p, j, i] = k.conj(ee)
def to_coords(C):
    M = np.zeros((N, N))
    for kk in range(3): M[kk] = C[:, kk, kk, 0]
    for kk, (i, j) in enumerate(pos): M[3 + kk * d:3 + (kk + 1) * d] = np.sqrt(2) * C[:, i, j, :].T
    return M
repR = lambda R: to_coords(np.einsum('ik,akjp,lj->ailp', R, Bm, R))
repS = lambda M: to_coords(np.einsum('aijp,qp->aijq', Bm, M))
cube = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.linalg.det(R) > 0: cube.append(R)
rows = [np.eye(N)[i] for i in range(3)]
for kk in range(3):
    for b in copies[kk]:
        v = np.zeros(N); v[3 + kk * d:3 + (kk + 1) * d] = b; rows.append(v)
W = np.array(rows); PW = W.T @ W
stab = [repR(R) @ repS(M) for R in cube for M in S3 if np.abs((np.eye(N) - PW) @ repR(R) @ repS(M) @ PW).max() < 1e-9]
F = []
for kk in range(3): v = np.zeros(N); v[3 + kk * d] = 1; F.append(v)
for kk in range(3): v = np.zeros(N); v[3 + kk * d:3 + (kk + 1) * d] = us[kk]; F.append(v)
F = np.array(F)
G = []          # Elemente als (A, anti): Wirkung auf s ist A, auf v ist +A (linear) oder -A (antilinear)
worst = 0.0
for g in stab:
    m = F @ g @ F.T; A = m[:3, :3]; B = m[3:, 3:]
    worst = max(worst, np.abs(m[:3, 3:]).max(), np.abs(m[3:, :3]).max(), np.abs(A - np.round(A)).max())
    if np.abs(B - A).max() < 1e-9: G.append((np.round(A), 0))
    elif np.abs(B + A).max() < 1e-9: G.append((np.round(A), 1))
    else: raise SystemExit("unerwartete Wirkung")
print("=" * 78); print("Teil 1  Wirkung der 24 Elemente auf s (Realteil) und v (Ladungsrichtung)")
print(f"   {len(G)} Elemente; s und v mischen nicht (Rest {worst:.1e}); auf s wirkt A, auf v wirkt +A ({sum(1 for a in G if a[1] == 0)} Elemente) oder -A ({sum(1 for a in G if a[1] == 1)} Elemente)")
print(f"   det A: gerade {sorted(Counter(int(round(np.linalg.det(A))) for A, f in G if f == 0).items())}, ungerade {sorted(Counter(int(round(np.linalg.det(A))) for A, f in G if f == 1).items())}")
print(f"   die 24 Matrizen A sind paarweise verschieden: {len(set(tuple(A.ravel()) for A, f in G)) == 24} -> auf s allein wirkt die ganze S4 linear und reell")
key = lambda g: (tuple(g[0].ravel().astype(int)), g[1])
mulg = lambda a, b: (a[0] @ b[0], a[1] ^ b[1])
Gk = {key(g): g for g in G}
def generate(gens):
    S = {key((np.eye(3), 0)): (np.eye(3), 0)}; frontier = list(S.values())
    while frontier:
        new = []
        for a in frontier:
            for b in gens:
                c = mulg(a, b)
                if key(c) not in S: S[key(c)] = c; new.append(c)
        frontier = new
    return frozenset(S)
subs = set()
for a in G:
    for b in G: subs.add(generate([a, b]))
subs = sorted(subs, key=lambda s: (len(s), sorted(s)))
def order(A):
    o, x = 1, A.copy()
    while np.abs(x - np.eye(3)).max() > 1e-9: x = x @ A; o += 1
    return o
def name(s):
    els = [Gk[x] for x in s]; odd = sum(f for _, f in els); od = sorted(Counter(order(A) for A, _ in els).items())
    return f"|G|={len(s)}, ungerade {odd}, Ordnungen {od}"
print(f"   Untergruppen: {len(subs)} (S4 hat 30)")

# ---------- Loesungsraeume ----------
def nullsp(A):
    u, s, vt = np.linalg.svd(A); return vt[(np.concatenate([s, np.zeros(len(vt) - len(s))]) < 1e-10)]
def herm_space(grp):
    basis = []
    for a in range(3):
        for b in range(a, 3):
            for ph in ([1] if a == b else [1, 1j]):
                H = np.zeros((3, 3), complex); H[a, b] = ph; H[b, a] = np.conj(ph); basis.append(H)
    cons = []
    for H in basis:
        row = []
        for x in grp:
            A, f = Gk[x]; r = A @ (np.conj(H) if f else H) @ A.T - H; row += [r.real.ravel(), r.imag.ravel()]
        cons.append(np.concatenate(row))
    return [sum(c * H for c, H in zip(v, basis)) for v in nullsp(np.array(cons).T)]
def maj_space(grp, real):
    basis = []
    for a in range(3):
        for b in range(a, 3):
            for ph in ((1,) if real else (1, 1j)):
                M = np.zeros((3, 3), complex); M[a, b] = ph; M[b, a] = ph; basis.append(M)
    cons = []
    for M in basis:
        row = []
        for x in grp:
            A, f = Gk[x]; r = A.T @ M @ A - (np.conj(M) if (f and not real) else M); row += [r.real.ravel(), r.imag.ravel()]
        cons.append(np.concatenate(row))
    return [sum(c * M for c, M in zip(v, basis)) for v in nullsp(np.array(cons).T)]
def classify(He, Mn, ns=40):
    if not He or not Mn: return ('leer',)
    cand = None; Jm = 0.0; req = 0.0; deg_e = deg_n = np.inf
    for _ in range(ns):
        H = sum(rng.normal() * h for h in He); m = sum(rng.normal() * x for x in Mn)
        we, Ue = np.linalg.eigh(H); wn, Un = np.linalg.eigh(m.conj().T @ m)
        deg_e = min(deg_e, np.diff(we).min() / np.abs(we).max()); deg_n = min(deg_n, np.diff(wn).min() / np.abs(wn).max())
        if deg_e < 1e-8 or deg_n < 1e-8: break
        U = Ue.conj().T @ Un; P = np.abs(U) ** 2
        cols = [np.sort(P[:, c]) for c in range(3)]
        if cand is None: cand = cols
        else: cand = [c for c in cand if min(np.abs(c - c2).max() for c2 in cols) < 1e-8]
        Jm = max(Jm, abs((U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])).imag))
        req = max(req, min(np.abs(P[a] - P[b]).max() for a, b in ((0, 1), (0, 2), (1, 2))))
    if deg_e < 1e-8: return ('geladene Leptonen entartet',)
    if deg_n < 1e-8: return ('Neutrinos entartet',)
    fixed = tuple(sorted(tuple(round(float(x), 4) + 0.0 for x in c) for c in cand))
    return (f"feste Spalten {list(fixed) if fixed else 'keine'}", 'J = 0' if Jm < 1e-9 else 'J frei', 'zwei Zeilen gleich' if req < 1e-8 else 'Zeilen verschieden', f"dim m_nu {len(Mn)}")
def scan(real):
    Hs = {s: herm_space(s) for s in subs}; Ms = {s: maj_space(s, real) for s in subs}
    out = defaultdict(list)
    for ge in subs:
        for gn in subs:
            out[classify(Hs[ge], Ms[gn])].append((ge, gn))
    return out
def report(out):
    tm1 = (0.1667, 0.1667, 0.6667)
    for cl, lst in sorted(out.items(), key=lambda kv: str(kv[0])):
        if cl[0] in ('leer', 'geladene Leptonen entartet', 'Neutrinos entartet'):
            print(f"   {cl[0]}: {len(lst)} Paare"); continue
        ge, gn = min(lst, key=lambda p: (len(p[0]) + len(p[1])))
        print(f"   {' | '.join(cl)}: {len(lst)} Paare; kleinstes Beispiel G_e ({name(ge)}), G_nu ({name(gn)})")
    hit = [cl for cl in out if cl[0].startswith('feste') and str(list(tm1)) [1:-1] in cl[0]]
    print(f"   Klassen mit fester Spalte (2/3, 1/6, 1/6): {len(hit)}")
    return hit

print("=" * 78); print("Teil 2  Lesart A (H131): Neutrinos auf z, ungerade Elemente antilinear; alle Paare von Untergruppen")
outA = scan(False); hitA = report(outA)
print("=" * 78); print("Teil 3  Lesart B: Neutrinos auf s (reell), alle 24 Elemente linear; alle Paare von Untergruppen")
outB = scan(True); hitB = report(outB)
for cl in hitB:
    print(f"   TM1-Klasse im Einzelnen: {' | '.join(cl)}")
    ge, gn = min(outB[cl], key=lambda p: (len(p[0]) + len(p[1])))
    print("      G_e erzeugt von:", [Gk[x][0].astype(int).tolist() for x in ge if order(Gk[x][0]) == 3][:1])
    print("      G_nu:", [(Gk[x][0].astype(int).tolist(), 'ungerade' if Gk[x][1] else 'gerade') for x in gn if order(Gk[x][0]) > 1])

print("=" * 78); print("Teil 4  Lesart B mit Z3 und einer ungeraden Z2: Zaehlung und Winkel")
Z3 = [s for s in subs if len(s) == 3]; Z2o = [s for s in subs if len(s) == 2 and any(Gk[x][1] for x in s)]; Z2e = [s for s in subs if len(s) == 2 and not any(Gk[x][1] for x in s)]
cnt = Counter()
for ge in Z3:
    for gn in Z2o: cnt[classify(herm_space(ge), maj_space(gn, True))] += 1
for cl, c in sorted(cnt.items(), key=str): print(f"   Z3 x ungerade Z2 ({len(Z3)} x {len(Z2o)}): {c} Paare -> {' | '.join(cl)}")
cnt = Counter()
for ge in Z3:
    for gn in Z2e: cnt[classify(herm_space(ge), maj_space(gn, True))] += 1
for cl, c in sorted(cnt.items(), key=str): print(f"   Z3 x gerade Z2 ({len(Z3)} x {len(Z2e)}): {c} Paare -> {' | '.join(cl)}")
# Winkel in der TM1-Klasse: sin^2(theta23), |sin delta|, sin^2(theta12) gegen sin^2(theta13)
for ge in Z3:
    done = False
    for gn in Z2o:
        cl = classify(herm_space(ge), maj_space(gn, True))
        if '0.6667' in cl[0]:
            He, Mn = herm_space(ge), maj_space(gn, True); res = []
            for _ in range(2000):
                H = sum(rng.normal() * h for h in He); m = sum(rng.normal() * x for x in Mn)
                we, Ue = np.linalg.eigh(H); wn, Un = np.linalg.eigh(m.conj().T @ m); U = Ue.conj().T @ Un; P = np.abs(U) ** 2
                # Zuordnung: Spalte 1 = TM1-Spalte, Zeile e = Zeile mit 2/3 darin; Spalte 3 = die mit kleinstem |U_e|
                c1 = int(np.argmin([np.abs(np.sort(P[:, c]) - [1 / 6, 1 / 6, 2 / 3]).max() for c in range(3)])); re = int(np.argmax(P[:, c1]))
                oth = [c for c in range(3) if c != c1]; c3 = min(oth, key=lambda c: P[re, c]); c2 = [c for c in oth if c != c3][0]
                rmu, rtau = [r for r in range(3) if r != re]
                s13 = P[re, c3]; s12 = P[re, c2] / (1 - s13); s23 = P[rmu, c3] / (1 - s13)
                Jv = (U[re, c1] * U[rmu, c2] * np.conj(U[re, c2]) * np.conj(U[rmu, c1])).imag
                Jmax = np.sqrt(s12 * (1 - s12) * s23 * (1 - s23) * s13) * (1 - s13)
                res.append((s13, s12, s23, abs(Jv) / Jmax))
            res = np.array(res)
            print(f"   TM1-Klasse, 2000 Stichproben: sin^2(theta23) in [{res[:, 2].min():.6f}, {res[:, 2].max():.6f}]; |sin delta| in [{res[:, 3].min():.6f}, {res[:, 3].max():.6f}]")
            print(f"   sin^2(theta12) - (1 - 2/(3 cos^2 theta13)): groesste Abweichung {np.abs(res[:, 1] - (1 - 2 / (3 * (1 - res[:, 0])))).max():.1e}; sin^2(theta13) frei in [{res[:, 0].min():.4f}, {res[:, 0].max():.4f}]")
            print(f"   bei sin^2(theta13) = 0,022: sin^2(theta12) = {1 - 2 / (3 * (1 - 0.022)):.4f}")
            done = True; break
    if done: break
