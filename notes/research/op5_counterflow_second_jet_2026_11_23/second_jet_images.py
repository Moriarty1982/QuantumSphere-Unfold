"""Fortsetzbarkeit erster Jets zum zweiten Jet am OP5-Keim: gespeicherter Jet, T-Jet, R-Jet, Zufallsglieder
(Methoden-Notiz Commit 2f835585, Erkundung).
Aufruf: python second_jet_images.py <Keim-Ordner> <Repo-Wurzel> <Ausgabeordner>
Laedt den vorhandenen Bau wie jet_family_images.py (r43); die rechte Seite b und das prolongierte System wie precision_second_jet.py."""
import sys
import json
import itertools
from pathlib import Path
import mpmath as mp
import numpy as np

ROOT = Path(sys.argv[1]).resolve(); REPO = Path(sys.argv[2]).resolve(); OUT = Path(sys.argv[3]).resolve()
OLD_REPO = "repo=Path('C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold')"
prim = (ROOT / 'precision_primitive_rebuild.py').read_text()
assert prim.count(OLD_REPO) == 1
prim = prim.replace(OLD_REPO, 'repo=Path(' + repr(str(REPO)) + ')')
reb = (ROOT / 'precision_completed_rebuild.py').read_text()
old_load = "exec((ROOT/'precision_primitive_rebuild.py').read_text().split('\\nresults=[]')[0],helper)"
assert reb.count(old_load) == 1
reb = reb.replace(old_load, "exec(PRIM_TEXT.split('\\nresults=[]')[0],helper)")
m = {'__file__': str(ROOT / 'precision_completed_rebuild.py'), '__name__': 'rebuild', 'PRIM_TEXT': prim}
exec(reb, m)
evaluate = m['evaluate']
mp.mp.dps = 40
root = json.loads((ROOT / 'precision-completed-root-result.json').read_text())
v_root = mp.matrix([mp.mpf(x) for x in root['first_derivatives_real_packed']])
selected = root['selected_rows']
psi0 = m['psi']

# ---- Bilder wie r42/r43 ----
I2 = mp.eye(2); Z2 = mp.zeros(2)
sx = mp.matrix([[0, 1], [1, 0]]); sy = mp.matrix([[0, -1j], [1j, 0]]); sz = mp.matrix([[1, 0], [0, -1]])


def blk(a, b, c, d):
    q = mp.matrix(4, 4)
    for i in range(2):
        for j in range(2):
            q[i, j] = a[i, j]; q[i, j + 2] = b[i, j]; q[i + 2, j] = c[i, j]; q[i + 2, j + 2] = d[i, j]
    return q


al = [blk(Z2, q, q, Z2) for q in (sx, sy, sz)]
be = mp.diag([1, 1, -1, -1]); g5 = blk(Z2, I2, I2, Z2)
gam = [be] + [be * a for a in al]
Ms = [mp.eye(4), 1j * g5] + gam + [g * g5 for g in gam]
sT = [1, -1, 1, -1, -1, -1, 1, -1, -1, -1]
sR = [1, -1, 1, -1, 1, 1, -1, 1, -1, -1]


def dfierz(v, n):
    u = mp.matrix([psi0[4 * n + k] for k in range(4)])
    F = [(u.H * be * M * u)[0].real for M in Ms]
    phi2 = mp.sqrt(F[0] ** 2 + F[1] ** 2); out = []
    for mu in range(4):
        du = mp.matrix([mp.mpc(v[mu * 24 + 4 * n + k], v[mu * 24 + 4 * n + k + 12]) for k in range(4)])
        dF = [((du.H * be * M * u)[0] + (u.H * be * M * du)[0]).real for M in Ms]
        dp = (F[0] * dF[0] + F[1] * dF[1]) / phi2
        out.append([dF[k] / phi2 - F[k] * dp / phi2 ** 2 for k in range(10)])
    return out


def image(kind, d):
    if kind == 'T':
        return [[(-1 if mu == 0 else 1) * s * c for s, c in zip(sT, d[mu])] for mu in range(4)]
    return [[(-1 if mu == 1 else 1) * s * c for s, c in zip(sR, d[mu])] for mu in range(4)]


def mis(v, kind):
    d2 = dfierz(v, 2); i0 = image(kind, dfierz(v, 0))
    return [d2[mu][k] - i0[mu][k] for mu in range(4) for k in range(10)]


def rel(v, kind):
    return max(abs(c) for c in mis(v, kind)) / max(abs(c) for row in dfierz(v, 0) for c in row)


def norm(x):
    return max(abs(c) for c in x)


def jac_R(v):
    h = mp.mpf('1e-15'); cols = []
    for c in range(96):
        a = v.copy(); b = v.copy(); a[c] += h; b[c] -= h
        cols.append((evaluate(a) - evaluate(b)) / (2 * h))
    return mp.matrix([[cols[j][i] for j in range(96)] for i in range(32)])


def jac_lin(kind, v):
    base = mis(v, kind); cols = []
    for c in range(96):
        a = v.copy(); a[c] += 1
        cols.append([x - y for x, y in zip(mis(a, kind), base)])
    return mp.matrix([[cols[j][i] for j in range(96)] for i in range(40)])


def indep(rows):
    a = np.array(rows, float); sel = []
    for i in range(len(rows)):
        if np.linalg.matrix_rank(a[sel + [i]], tol=1e-9 * np.linalg.norm(a, 2)) > len(sel):
            sel.append(i)
    return sel


def newton(v, kinds, steps=14, label=''):
    sel = None
    for it in range(steps):
        J = jac_R(v); r = evaluate(v)
        rows = [[J[i, j] for j in range(96)] for i in selected]; rhs = [r[i] for i in selected]
        for k in kinds:
            M = jac_lin(k, v); mm = mis(v, k)
            rows += [[M[i, j] for j in range(96)] for i in range(40)]; rhs += mm
        if sel is None:
            sel = indep(rows)
        A = mp.matrix([rows[i] for i in sel]); b = mp.matrix([rhs[i] for i in sel])
        dx = -A.T * ((A * A.T) ** -1) * b
        merit = lambda z: max([norm(evaluate(z))] + [max(abs(c) for c in mis(z, k)) for k in kinds])
        m0 = merit(v); t = mp.mpf(1)
        while t > mp.mpf(2) ** -12 and merit(v + t * dx) >= m0:
            t /= 2
        v = v + t * dx
        print(f'   {label} Schritt {it + 1}: Daempfung {mp.nstr(t, 3)}, |R| = {mp.nstr(norm(evaluate(v)), 4)}', flush=True)
        if merit(v) < mp.mpf('1e-30'):
            break
    return v


# ---- zweiter Jet: rechte Seite und prolongiertes System (wie precision_second_jet.py) ----
ns = m['ns']; coords = m['coords']; subs = m['subs']; cs = m['cs']
d2h = [[m['cm'](ns['hm'].diff(x, y).subs(subs)).real for y in coords] for x in coords]
d2c = [[[m['mat'](c.diff(x, y).subs(subs)) for c in cs] for y in coords] for x in coords]
orig = {k: m[k] for k in ['psi', 'h', 'dh', 'conn', 'dc', 'A']}
pairs = list(itertools.combinations_with_replacement(range(4), 2))


def second_jet_residual(v):
    js = [mp.matrix([mp.mpc(v[mu * 24 + k], v[mu * 24 + k + 12]) for k in range(12)]) for mu in range(4)]

    def coordinate(t, mu):
        try:
            m['psi'] = orig['psi'] + t * js[mu]; m['h'] = orig['h'] + t * orig['dh'][mu]
            m['dh'] = [orig['dh'][nu] + t * d2h[mu][nu] for nu in range(4)]
            m['conn'] = [orig['conn'][nu] + t * orig['dc'][mu][nu] for nu in range(4)]
            m['dc'] = [[orig['dc'][nu][a] + t * d2c[mu][nu][a] for a in range(4)] for nu in range(4)]
            m['A'] = mp.matrix([[mp.re(z) for z in (m['psi'].conjugate().T * q)] + [-mp.im(z) for z in (m['psi'].conjugate().T * q)] for q in m['Q']])
            return evaluate(v)
        finally:
            for k, z in orig.items():
                m[k] = z

    b = mp.matrix([x for mu in range(4) for x in mp.diff(lambda t: coordinate(t, mu), mp.mpf('0'))])
    J = jac_R(v); A = mp.zeros(128, 240)
    for mu in range(4):
        for nu in range(4):
            col = pairs.index(tuple(sorted((mu, nu)))); weight = 2 if mu == nu else 1
            for i in range(32):
                for k in range(24):
                    A[mu * 32 + i, col * 24 + k] += weight * J[i, nu * 24 + k]
    a = np.array(A.tolist(), float); basis = []; keep = []
    for i, row in enumerate(a):
        z = row.copy()
        for _ in range(2):
            for q in basis:
                z -= q @ z * q
        n = np.linalg.norm(z)
        if n > 1e-9 * np.linalg.norm(a, 2):
            basis.append(z / n); keep.append(i)
    B = mp.matrix([[A[i, j] for j in range(240)] for i in keep]); rhs = mp.matrix([-b[i] for i in keep])
    c = B.T * ((B * B.T) ** -1) * rhs
    res = A * c + b
    return len(keep), norm(res), norm(b)


results = {}
print('Kontrolle: |R(v_root)| =', mp.nstr(norm(evaluate(v_root)), 4), flush=True)
jets = {'gespeichert': v_root}
jets['T-Jet'] = newton(v_root.copy(), ['T'], label='T')
jets['R-Jet'] = newton(v_root.copy(), ['R'], label='R')
JR = jac_R(v_root)
_, _, Vt = np.linalg.svd(np.array(JR.tolist(), float))
null = Vt[31:]
for seed in (1, 2):
    rng = np.random.default_rng(seed); d = rng.standard_normal(null.shape[0]) @ null; d = d / np.abs(d).max()
    jets[f'Zufall {seed}'] = newton(v_root + mp.matrix([mp.mpf(float(x)) for x in d]), [], label=f'Zufall {seed}')

for name, v in jets.items():
    rk, res, bn = second_jet_residual(v)
    print(f'{name}: |R| = {mp.nstr(norm(evaluate(v)), 4)}, Bilder T {mp.nstr(rel(v, "T"), 3)}, R {mp.nstr(rel(v, "R"), 3)}, '
          f'Abstand zum gespeicherten Jet {mp.nstr(norm(v - v_root), 4)} | zweiter Jet: Rang {rk} von 128, voller Rest {mp.nstr(res, 6)} '
          f'(|b| = {mp.nstr(bn, 4)})', flush=True)
    results[name] = [mp.nstr(x, 40) for x in v]
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'second_jet_images_jets.json').write_text(json.dumps(results, indent=1))
