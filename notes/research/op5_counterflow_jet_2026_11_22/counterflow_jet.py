"""Zeitumkehr, Spiegelung x -> -x oder innere Umkehr am ersten Jet des OP5-Keims (Methoden-Notiz Commit 8006e893, Erkundung).
Normierte Fierz-Groessen F = (Phi, Theta, J^a, K^a)/phi^2 je Block (Dirac-Basis wie k168) und ihre Ableitungen d_mu F am Keim.
Aufruf: python counterflow_jet.py <Keim-Ordner>"""
import sys
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 40
D = Path(sys.argv[1])
f70 = json.loads((D / 'precision-first-jet-70.json').read_text())
cx = lambda ab: mp.mpc(mp.mpf(ab[0]), mp.mpf(ab[1]))
psi = [cx(v) for v in f70['psi']]
dpsi = [[cx(v) for v in f70['first_derivatives'][mu]] for mu in range(4)]
blk4 = lambda arr, n: mp.matrix([arr[4 * n + k] for k in range(4)])

I2 = mp.eye(2); Z2 = mp.zeros(2)
sx = mp.matrix([[0, 1], [1, 0]]); sy = mp.matrix([[0, -1j], [1j, 0]]); sz = mp.matrix([[1, 0], [0, -1]])


def blk(a, b, c, d):
    m = mp.matrix(4, 4)
    for i in range(2):
        for j in range(2):
            m[i, j] = a[i, j]; m[i, j + 2] = b[i, j]; m[i + 2, j] = c[i, j]; m[i + 2, j + 2] = d[i, j]
    return m


al = [blk(Z2, q, q, Z2) for q in (sx, sy, sz)]
be = mp.diag([1, 1, -1, -1]); g5 = blk(Z2, I2, I2, Z2)
gam = [be] + [be * a for a in al]
Ms = [mp.eye(4), 1j * g5] + gam + [g * g5 for g in gam]   # Phi, Theta, J^0..3, K^0..3


def vals(u):
    return [(u.H * be * M * u)[0].real for M in Ms]


def dvals(u, du):
    return [((du.H * be * M * u)[0] + (u.H * be * M * du)[0]).real for M in Ms]


def normed(u, dus):
    F = vals(u)
    phi2 = mp.sqrt(F[0] ** 2 + F[1] ** 2)
    dF = [dvals(u, du) for du in dus]
    dphi2 = [(F[0] * d[0] + F[1] * d[1]) / phi2 for d in dF]
    Fn = [f / phi2 for f in F]
    dFn = [[d[k] / phi2 - F[k] * dp / phi2 ** 2 for k in range(10)] for d, dp in zip(dF, dphi2)]
    return Fn, dFn


sT = [1, -1, 1, -1, -1, -1, 1, -1, -1, -1]
sR = [1, -1, 1, -1, 1, 1, -1, 1, -1, -1]
mulv = lambda s, v: [a * b for a, b in zip(s, v)]


def image(kind, Fn, dFn):
    if kind == 'T':
        return mulv(sT, Fn), [mulv(sT, d) if mu else [-c for c in mulv(sT, d)] for mu, d in enumerate(dFn)]
    if kind == 'R':
        return mulv(sR, Fn), [[-c for c in mulv(sR, d)] if mu == 1 else mulv(sR, d) for mu, d in enumerate(dFn)]
    return mulv(sT, Fn), [mulv(sT, d) for d in dFn]   # 'I'


B = [normed(blk4(psi, n), [blk4(dpsi[mu], n) for mu in range(4)]) for n in range(3)]
names = ['t', 'x', 'y', 'z']
lab = ['Phi', 'Theta', 'J0', 'Jx', 'Jy', 'Jz', 'K0', 'Kx', 'Ky', 'Kz']
for n in range(3):
    print(f'Block {n}: Ableitungen der normierten Fierz-Groessen (nur |Wert| > 1e-3)')
    for mu in range(4):
        print(f'   d_{names[mu]}:', {lab[k]: mp.nstr(B[n][1][mu][k], 8) for k in range(10) if abs(B[n][1][mu][k]) > 1e-3})

for src in (0, 1):
    scale = max(abs(c) for d in B[src][1] for c in d)
    print(f'Bilder von Block {src} gegen Block 2 (Skala max |dF_{src}| = {mp.nstr(scale, 6)}):')
    for kind in ('T', 'R', 'I'):
        Fi, dFi = image(kind, *B[src])
        dv = max(abs(a - b) for a, b in zip(B[2][0], Fi))
        per = [max(abs(a - b) for a, b in zip(B[2][1][mu], dFi[mu])) / scale for mu in range(4)]
        print(f'   {kind}: Werte {mp.nstr(dv, 4)}; Ableitungen relativ je mu (t, x, y, z) =', [mp.nstr(p, 4) for p in per],
              '; gesamt', mp.nstr(max(per), 4))
scale01 = max(abs(c) for d in B[0][1] for c in d)
print('Vergleich: Block 1 gegen Block 0 (gleiche Laufrichtung), Ableitungen relativ gesamt:',
      mp.nstr(max(max(abs(a - b) for a, b in zip(B[1][1][mu], B[0][1][mu])) for mu in range(4)) / scale01, 4))
# Nachtraeglich (nicht in der Methoden-Notiz): Geschwindigkeit v = J^x/J^0 und ihre Ableitungen gegen die Hubble-Form v = +-x/t
for n in range(3):
    Fn, dFn = B[n]
    v = Fn[3] / Fn[2]
    dv = [(d[3] * Fn[2] - Fn[3] * d[2]) / Fn[2] ** 2 for d in dFn]
    print(f'Block {n}: v = {mp.nstr(v, 8)}, d_t v = {mp.nstr(dv[0], 6)}, d_x v = {mp.nstr(dv[1], 6)} (Hubble-Form: d_t v = -+0.6, d_x v = +-1)')
