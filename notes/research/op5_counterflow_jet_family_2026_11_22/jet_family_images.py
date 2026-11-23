"""Zeitumkehr-, Spiegel- oder innere Bilder in der Familie der vervollstaendigten ersten Jets am OP5-Keim
(Methoden-Notiz Commit 1a23dd7a, Erkundung, teilweise nicht blind).
Aufruf: python jet_family_images.py <Keim-Ordner> <Repo-Wurzel>
Der Keim-Ordner enthaelt precision_completed_rebuild.py, precision_primitive_rebuild.py und die Ergebnisdateien; die Repo-Wurzel
enthaelt analysis/OP5_Counterflow_Full_Residual_Check.py. Der feste Pfad im vorhandenen Bau wird beim Laden ersetzt."""
import sys
import json
from pathlib import Path
import mpmath as mp
import numpy as np

ROOT = Path(sys.argv[1]).resolve()
REPO = Path(sys.argv[2]).resolve()
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
v_prim = m['v']
selected = root['selected_rows']
psi = m['psi']

# Dirac-Basis wie k168/r41/r42
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
    u = mp.matrix([psi[4 * n + k] for k in range(4)])
    F = [(u.H * be * M * u)[0].real for M in Ms]
    phi2 = mp.sqrt(F[0] ** 2 + F[1] ** 2)
    out = []
    for mu in range(4):
        du = mp.matrix([mp.mpc(v[mu * 24 + 4 * n + k], v[mu * 24 + 4 * n + k + 12]) for k in range(4)])
        dF = [((du.H * be * M * u)[0] + (u.H * be * M * du)[0]).real for M in Ms]
        dp = (F[0] * dF[0] + F[1] * dF[1]) / phi2
        out.append([dF[k] / phi2 - F[k] * dp / phi2 ** 2 for k in range(10)])
    return out


def image(kind, d):
    if kind == 'T':
        return [[(-1 if mu == 0 else 1) * s * c for s, c in zip(sT, d[mu])] for mu in range(4)]
    if kind == 'R':
        return [[(-1 if mu == 1 else 1) * s * c for s, c in zip(sR, d[mu])] for mu in range(4)]
    return [[s * c for s, c in zip(sT, d[mu])] for mu in range(4)]


def mis(v, kind):
    d2 = dfierz(v, 2); i0 = image(kind, dfierz(v, 0))
    return [d2[mu][k] - i0[mu][k] for mu in range(4) for k in range(10)]


def scale(v):
    return max(abs(c) for row in dfierz(v, 0) for c in row)


def rel(v, kind):
    return max(abs(c) for c in mis(v, kind)) / scale(v)


def norm(x):
    return max(abs(c) for c in x)


print('(1) Ausgangsjet: max |v_root - v_prim| =', mp.nstr(norm(v_root - v_prim), 6), '; |R(v_root)| =', mp.nstr(norm(evaluate(v_root)), 6))
print('    r42-Mass am vervollstaendigten Jet: T', mp.nstr(rel(v_root, 'T'), 4), ', R', mp.nstr(rel(v_root, 'R'), 4), ', I', mp.nstr(rel(v_root, 'I'), 4))


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


JR = jac_R(v_root)
sv = np.linalg.svd(np.array(JR.tolist(), dtype=float), compute_uv=False)
rk = int((sv > 1e-9 * sv[0]).sum())
print('(2) Jacobi-Matrix von R: Rang', rk, 'von 32; Singulaerwerte gross/klein', f'{sv[0]:.3e}', f'{sv[rk - 1]:.3e}', f'{sv[-1]:.3e}',
      '; lineare Familie der Dimension', 96 - rk)
MX = {k: jac_lin(k, v_root) for k in ('T', 'R', 'I')}
for k in ('T', 'R', 'I'):
    A = np.vstack([np.array(JR.tolist(), float)[selected], np.array(MX[k].tolist(), float)])
    print(f'    Rang [R_sel; m_{k}] =', np.linalg.matrix_rank(A, tol=1e-9 * np.linalg.norm(A, 2)), 'von', A.shape[0])
A2 = np.vstack([np.array(JR.tolist(), float)[selected], np.array(MX['T'].tolist(), float), np.array(MX['R'].tolist(), float)])
print('    Rang [R_sel; m_T; m_R] =', np.linalg.matrix_rank(A2, tol=1e-9 * np.linalg.norm(A2, 2)), 'von', A2.shape[0], '(96 Unbekannte)')


def solve_step(A, b):
    eps = mp.mpf('1e-30')
    if A.rows <= A.cols:
        return -A.T * ((A * A.T + eps * mp.eye(A.rows)) ** -1) * b
    return -((A.T * A + eps * mp.eye(A.cols)) ** -1) * (A.T * b)


STEPS = 12


def merit(v, kinds):
    return max([norm(evaluate(v))] + [max(abs(c) for c in mis(v, k)) / scale(v) for k in kinds])


def joint(kinds, steps=STEPS):
    # Lauf 2: unabhaengige Zeilen einmal waehlen (wie precision_completed_root.py), Schritt minimaler Norm,
    # Daempfung durch Halbieren, solange das Guetemass nicht sinkt; Verlauf je Schritt ausgeben.
    v = v_root.copy(); sel = None
    for it in range(steps):
        J = jac_R(v); r = evaluate(v)
        rows = [[J[i, j] for j in range(96)] for i in selected]; rhs = [r[i] for i in selected]
        for k in kinds:
            M = jac_lin(k, v); mm = mis(v, k)
            rows += [[M[i, j] for j in range(96)] for i in range(40)]; rhs += mm
        if sel is None:
            a = np.array(rows, float); sel = []
            for i in range(len(rows)):
                if np.linalg.matrix_rank(a[sel + [i]], tol=1e-9 * np.linalg.norm(a, 2)) > len(sel):
                    sel.append(i)
        A = mp.matrix([rows[i] for i in sel]); b = mp.matrix([rhs[i] for i in sel])
        dx = solve_step(A, b); m0 = merit(v, kinds); t = mp.mpf(1)
        while t > mp.mpf(2) ** -12 and merit(v + t * dx, kinds) >= m0:
            t /= 2
        v = v + t * dx
        print(f'      {"+".join(kinds)} Schritt {it + 1}: Daempfung {mp.nstr(t, 4)}, |R| = {mp.nstr(norm(evaluate(v)), 4)}, '
              f'Bild relativ = {[mp.nstr(rel(v, k), 4) for k in kinds]}, Zeilen {len(sel)}', flush=True)
        if merit(v, kinds) < mp.mpf('1e-25'):
            break
    return v


for kinds in (['T'], ['R'], ['I'], ['T', 'R']):
    v = joint(kinds)
    print(f'(3/4) Bild {"+".join(kinds)}: |R| =', mp.nstr(norm(evaluate(v)), 6),
          '; relative Bildabweichung', {k: mp.nstr(rel(v, k), 4) for k in ('T', 'R', 'I')},
          '; Aenderung der Ableitungen max', mp.nstr(norm(v - v_root), 4))
