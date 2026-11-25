"""k261 (Test H131, Vorab-Notiz 875e6d4 vom 25.11.2026 10:36 UTC): S4 mit der Ladung als verallgemeinerter CP, Mischungsklassen.
Teil 1: die 24 Elemente aus k260 (Kopie k auf Platz k von H3(S)) auf das Triplett z_k = s_k + i v_k einschraenken: 12 linear (A4), 12 antilinear (X).
Teil 2: Restsymmetrien Z3 = <T> (geladene Leptonen), Z2 = <S> und CP X (Majorana-Neutrinos); alle zulaessigen Kombinationen, je 200 Stichproben.
Aufruf: python3 k261_test_h131.py   (benutzt ../kollaps_h128/k283_test_h128.py)
"""
import sys, os, itertools, json, numpy as np
from collections import Counter, defaultdict
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'kollaps_h128'))
import k283_test_h128 as k
rng = np.random.default_rng(261)
n = 4; J, T, d, N = k.albert(n); E = np.eye(d)

# ---------- Teil 1: Gruppe aus k260 ----------
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
# Triplett: s_k (Realteil des Eintrags k), v_k (Richtung u_k)
F = []
for kk in range(3): v = np.zeros(N); v[3 + kk * d] = 1; F.append(v)
for kk in range(3): v = np.zeros(N); v[3 + kk * d:3 + (kk + 1) * d] = us[kk]; F.append(v)
F = np.array(F); I2 = np.block([[np.zeros((3, 3)), -np.eye(3)], [np.eye(3), np.zeros((3, 3))]])   # Multiplikation mit i auf (s, v)
lin, anti = [], []
leak = 0.0
for g in stab:
    leak = max(leak, np.abs(g @ F.T - F.T @ (F @ g @ F.T)).max())
    m = F @ g @ F.T
    if np.abs(m @ I2 - I2 @ m).max() < 1e-9: lin.append(m[:3, :3] + 1j * m[3:, :3])
    elif np.abs(m @ I2 + I2 @ m).max() < 1e-9: anti.append(m[:3, :3] + 1j * m[3:, :3])
print("=" * 78); print("Teil 1  Gruppe auf dem Triplett")
print(f"   Elemente, die W erhalten: {len(stab)}; Triplett-Teilraum erhalten (Rest {leak:.1e}); linear {len(lin)}, antilinear {len(anti)}")
rnd = lambda M: np.round(M.real).astype(int) if np.abs(M.imag).max() < 1e-9 and np.abs(M.real - np.round(M.real)).max() < 1e-9 else None
print(f"   alle Matrizen reell und ganzzahlig: {all(rnd(m) is not None for m in lin + anti)}")
lin = [rnd(m).astype(float) for m in lin]; anti = [rnd(m).astype(float) for m in anti]
print(f"   Determinanten linear {sorted(Counter(int(round(np.linalg.det(m))) for m in lin).items())}, antilinear {sorted(Counter(int(round(np.linalg.det(m))) for m in anti).items())}")
inl = lambda M, L: any(np.abs(M - x).max() < 1e-9 for x in L)
# gemischte Verknuepfung: lin*lin, anti*conj(anti) linear; lin*anti, anti*conj(lin) antilinear (alles reell, conj wirkungslos)
closed = all(inl(a @ b, lin) for a in lin for b in lin) and all(inl(a @ b, lin) for a in anti for b in anti) and all(inl(a @ b, anti) for a in lin for b in anti)
print(f"   Kontrolle (i) Gruppe unter gemischter Verknuepfung abgeschlossen: {closed}")
def order(m):
    o, x = 1, m.copy()
    while np.abs(x - np.eye(3)).max() > 1e-9: x = x @ m; o += 1
    return o
print(f"   Ordnungen linear {sorted(Counter(order(m) for m in lin).items())}; X X* fuer antilineare: Ordnung {sorted(Counter(order(x @ x) for x in anti).items())}")
print("   Beispiele antilinear X:", [x.astype(int).tolist() for x in anti[:3]])

# ---------- Teil 2: Restsymmetrien ----------
Ts = [m for m in lin if order(m) == 3]; Ss = [m for m in lin if order(m) == 2]
def herm_space(Tm):
    basis = []
    for a in range(3):
        for b in range(a, 3):
            for ph in ([1] if a == b else [1, 1j]):
                H = np.zeros((3, 3), complex); H[a, b] = ph; H[b, a] = np.conj(ph); basis.append(H)
    A = np.array([np.concatenate([(Tm @ H @ Tm.T - H).real.ravel(), (Tm @ H @ Tm.T - H).imag.ravel()]) for H in basis]).T
    u, s, vt = np.linalg.svd(A); null = vt[(np.concatenate([s, np.zeros(len(vt) - len(s))]) < 1e-10)]
    return [sum(c * H for c, H in zip(v, basis)) for v in null]
def maj_space(Sm, X=None):
    basis = []
    for a in range(3):
        for b in range(a, 3):
            for ph in (1, 1j):
                M = np.zeros((3, 3), complex); M[a, b] = ph; M[b, a] = ph; basis.append(M)
    cons = []
    for M in basis:
        r = Sm.T @ M @ Sm - M; row = [r.real.ravel(), r.imag.ravel()]
        if X is not None:
            r2 = X.T @ M @ X - np.conj(M); row += [r2.real.ravel(), r2.imag.ravel()]
        cons.append(np.concatenate(row))
    A = np.array(cons).T
    u, s, vt = np.linalg.svd(A); null = vt[(np.concatenate([s, np.zeros(len(vt) - len(s))]) < 1e-10)]
    return [sum(c * M for c, M in zip(v, basis)) for v in null]
def sample(Tm, Sm, X, ns=200):
    He, Mn = herm_space(Tm), maj_space(Sm, X)
    out = dict(dimH=len(He), dimM=len(Mn), col=0.0, colconst=0.0, J=0.0, roweq=0.0, deg=np.inf)
    if not He or not Mn: return out
    ref = None
    for _ in range(ns):
        H = sum(rng.normal() * h for h in He); m = sum(rng.normal() * x for x in Mn)
        we, Ue = np.linalg.eigh(H); wn, Un = np.linalg.eigh(m.conj().T @ m)
        out['deg'] = min(out['deg'], np.diff(we).min() / np.abs(we).max(), np.diff(wn).min() / np.abs(wn).max())
        U = Ue.conj().T @ Un; P = np.abs(U) ** 2
        out['col'] = max(out['col'], min(np.abs(P[:, c] - 1 / 3).max() for c in range(3)))
        cols = [tuple(np.sort(P[:, c])) for c in range(3)]
        if ref is None: ref = cols; dev = [0.0, 0.0, 0.0]
        dev = [max(dv, min(np.abs(np.array(r) - np.array(c)).max() for c in cols)) for dv, r in zip(dev, ref)]
        out['J'] = max(out['J'], abs((U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])).imag))
        out['roweq'] = max(out['roweq'], min(np.abs(P[a] - P[b]).max() for a, b in ((0, 1), (0, 2), (1, 2))))
    out['colconst'] = min(dev); out['refcol'] = [round(float(x), 6) for x in ref[int(np.argmin(dev))]]
    return out
print("=" * 78); print("Teil 2  Kontrolle (ii): ohne CP")
worst = 0.0; jmax = 0.0; rmin = np.inf
for Tm in Ts:
    for Sm in Ss:
        o = sample(Tm, Sm, None, ns=50); worst = max(worst, o['col']); jmax = max(jmax, o['J']); rmin = min(rmin, o['roweq'])
print(f"   {len(Ts)} x {len(Ss)} Kombinationen (T, S): trimaximale Spalte, groesste Abweichung {worst:.1e}; |J| bis {jmax:.3f} (frei); kleinste Zeilendifferenz {rmin:.3f} (keine Zeilengleichheit)")
print("=" * 78); print("Teil 2  mit CP: alle zulaessigen (T, S, X)")
classes = defaultdict(list); nadm = 0; excluded = Counter()
for si, Sm in enumerate(Ss):
    for xi, X in enumerate(anti):
        if np.abs(X @ Sm - Sm @ X).max() > 1e-9: excluded['X S != S X'] += 1; continue
        xx = X @ X
        if np.abs(xx - np.eye(3)).max() < 1e-9: typ = 'X X* = 1'
        elif np.abs(xx - Sm).max() < 1e-9: typ = 'X X* = S'
        else: excluded['X X* nicht in {1, S}'] += 1; continue
        for ti, Tm in enumerate(Ts):
            nadm += 1; o = sample(Tm, Sm, X)
            if o['dimM'] == 0 or o['deg'] < 1e-8: key = ('entartet oder leer', typ)
            else:
                key = (typ, 'Spalte trimaximal' if o['col'] < 1e-9 else ('Spalte konstant ' + str(o['refcol']) if o['colconst'] < 1e-9 else 'keine konstante Spalte'),
                       'J = 0' if o['J'] < 1e-10 else 'J != 0', 'zwei Zeilen gleich' if o['roweq'] < 1e-9 else 'Zeilen verschieden')
            classes[key].append((ti, si, xi, o))
print(f"   zulaessige Kombinationen: {nadm}; ausgeschlossene Paare (S, X): {dict(excluded)}")
for key, lst in sorted(classes.items(), key=lambda kv: str(kv[0])):
    o = lst[0][3]
    print(f"   Klasse {key}: {len(lst)} Kombinationen; dim(H_e) {o['dimH']}, dim(m_nu) {o['dimM']}; max |J| {max(x[3]['J'] for x in lst):.4f}; Zeilengleichheit {max(x[3]['roweq'] for x in lst):.1e}; Spaltenrest {max(x[3]['col'] for x in lst):.1e}")
    ti, si, xi, _ = lst[0]
    print(f"      Vertreter: T = {Ts[ti].astype(int).tolist()}, S = {Ss[si].astype(int).tolist()}, X = {anti[xi].astype(int).tolist()}")
phys = [key for key in classes if key[0] != 'entartet oder leer']
print(f"   Klassen ohne die Art von X X*: {sorted(set(key[1:] for key in phys))}")
