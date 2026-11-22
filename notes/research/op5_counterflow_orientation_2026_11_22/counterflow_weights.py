"""Gegenstrom am OP5-Keim: Zeitumkehrbild und Gewichte der Bloecke (Methoden-Notiz Commit 10e483e1, Erkundung, nicht blind).
Fierz-Groessen wie k168 (Dirac-Basis): Phi = u^+ beta u, Theta = u^+ beta i g5 u, J^a = u^+ beta g^a u, K^a = u^+ beta g^a g5 u.
Bild unter Zeitumkehr T: (Phi, -Theta, J^0, -J^i, K^0, -K^i); unter Spiegelung x -> -x: (Phi, -Theta, J^0, -J^x, J^y, J^z, -K^0, K^x, -K^y, -K^z).
Aufruf: python counterflow_weights.py <Keim-Ordner>"""
import sys
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 40
D = Path(sys.argv[1])
f70 = json.loads((D / 'precision-first-jet-70.json').read_text())
pt = [mp.mpf(v.split('/')[0]) / mp.mpf(v.split('/')[1]) if '/' in v else mp.mpf(v) for v in f70['point']]
psi = [mp.mpc(mp.mpf(a), mp.mpf(b)) for a, b in f70['psi']]
blocks = [mp.matrix([psi[4 * n + k] for k in range(4)]) for n in range(3)]

I2 = mp.eye(2)
sx = mp.matrix([[0, 1], [1, 0]]); sy = mp.matrix([[0, -1j], [1j, 0]]); sz = mp.matrix([[1, 0], [0, -1]])


def blk(a, b, c, d):
    m = mp.matrix(4, 4)
    for i in range(2):
        for j in range(2):
            m[i, j] = a[i, j]; m[i, j + 2] = b[i, j]; m[i + 2, j] = c[i, j]; m[i + 2, j + 2] = d[i, j]
    return m


Z2 = mp.zeros(2)
al = [blk(Z2, q, q, Z2) for q in (sx, sy, sz)]
be = mp.diag([1, 1, -1, -1])
g5 = blk(Z2, I2, I2, Z2)
gam = [be] + [be * a for a in al]


def bil(u, M):
    return (u.H * be * M * u)[0].real


def fierz(u):
    Phi = bil(u, mp.eye(4)); Th = bil(u, 1j * g5)
    J = [bil(u, g) for g in gam]; K = [bil(u, g * g5) for g in gam]
    return Phi, Th, J, K


def vec(Phi, Th, J, K):
    return [Phi, Th] + J + K


def T_img(v):
    s = [1, -1, 1, -1, -1, -1, 1, -1, -1, -1]
    return [a * b for a, b in zip(s, v)]


def Px_img(v):
    s = [1, -1, 1, -1, 1, 1, -1, 1, -1, -1]
    return [a * b for a, b in zip(s, v)]


print('Punkt (t, x, y, z) =', [mp.nstr(p, 6) for p in pt])
F = [fierz(u) for u in blocks]
V = []
for n, (Phi, Th, J, K) in enumerate(F):
    phi2 = mp.sqrt(Phi ** 2 + Th ** 2)
    v = [c / phi2 for c in vec(Phi, Th, J, K)]
    V.append(v)
    print(f'Block {n}: phi^2 = {mp.nstr(phi2, 20)}, J^0 = {mp.nstr(J[0], 20)}, beta = {mp.nstr(mp.degrees(mp.atan2(Th, Phi)), 8)} Grad')
    print('   normiert (Phi, Theta, J^a, K^a)/phi^2 =', [mp.nstr(c, 10) for c in v])

dev = lambda a, b: max(abs(x - y) for x, y in zip(a, b))
print('(1) Abweichung Block 2 vom Bild von Block 0: T', mp.nstr(dev(V[2], T_img(V[0])), 6), ', Spiegelung x', mp.nstr(dev(V[2], Px_img(V[0])), 6))
print('    Abweichung Block 2 vom Bild von Block 1: T', mp.nstr(dev(V[2], T_img(V[1])), 6), ', Spiegelung x', mp.nstr(dev(V[2], Px_img(V[1])), 6))
print('    Abweichung Block 1 von Block 0 (gleiche Orientierung):', mp.nstr(dev(V[1], V[0]), 6))
print('    groesste Abweichung T gegen Spiegelung am Bild von Block 0:', mp.nstr(dev(T_img(V[0]), Px_img(V[0])), 6))

phi2 = [mp.sqrt(f[0] ** 2 + f[1] ** 2) for f in F]
J0 = [f[2][0] for f in F]
for name, wts in (('phi^2', phi2), ('J^0 = psi^+ psi', J0)):
    p = (wts[0] + wts[1]) / (wts[0] + wts[1] + wts[2])
    w = 2 * p - 1
    print(f'(2) Gewicht {name}: p = {mp.nstr(p, 20)}, w = 2p - 1 = {mp.nstr(w, 12)}, groesste relative Abweichung von N_m |w| = {mp.nstr(abs(w), 6)}')
Jsum = [sum(f[2][a] for f in F) for a in range(4)]
print('    Gesamtstrom der drei Bloecke J^a =', [mp.nstr(c, 12) for c in Jsum], ';  Nettogeschwindigkeit J^x/J^0 =', mp.nstr(Jsum[1] / Jsum[0], 10))
