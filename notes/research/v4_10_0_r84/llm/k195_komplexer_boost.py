"""k195: Test H79 - zweite Lesart mit vollstaendigem komplexem Boost (Spinor S und Argument Lambda(i pi) x + delta).
Hermitesche gegen holomorphe Abbildung der Adjungierten. Ausgabe k195_out.json im aktuellen Ordner.
"""
import json
import numpy as np
import sympy as sp

out = {}
th = sp.symbols('theta')
I2 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
sbar = [I2, -sx, -sy, -sz]

def Lam(t):   # Boost entlang z (t, x, y, z), symmetrisch
    return sp.Matrix([[sp.cosh(t), 0, 0, sp.sinh(t)], [0, 1, 0, 0], [0, 0, 1, 0], [sp.sinh(t), 0, 0, sp.cosh(t)]])

# Vorzeichenkonvention s: S(theta) = exp(s theta sigma_z / 2) mit S sbar^mu S = Lam^mu_nu sbar^nu fuer reelles theta
found = None
for s in (1, -1):
    S = sp.diag(sp.exp(s*th/2), sp.exp(-s*th/2))
    ok = all(sp.simplify((S*sbar[mu]*S - sum((Lam(th)[mu, nu]*sbar[nu] for nu in range(4)), sp.zeros(2, 2))).applyfunc(
        lambda e: sp.simplify(e.rewrite(sp.exp)))) == sp.zeros(2, 2) for mu in range(4))
    if ok:
        found = s; break
out['Konvention_s'] = found
s = found
Sip = sp.simplify(sp.diag(sp.exp(s*sp.I*sp.pi/2), sp.exp(-s*sp.I*sp.pi/2)))
LamI = sp.simplify(Lam(sp.I*sp.pi))
out['S(i pi)'] = str(Sip); out['Lambda(i pi)'] = str(LamI)
out['S(i pi) = +-(-i sigma_z)'] = bool(sp.simplify(Sip - (-sp.I*sz)) == sp.zeros(2, 2) or sp.simplify(Sip + (-sp.I*sz)) == sp.zeros(2, 2))

# Koeffizienten des Bild-Terms: L_T = -(adj) sbar^mu (Lambda_mu^mu d_mu^y) psi  ->  Matrix C_mu
res = {}
for name, left in (('holomorph', Sip), ('hermitesch', Sip.H)):
    C = [sp.simplify(-(left*sbar[mu]*Sip)*LamI[mu, mu]) for mu in range(4)]
    # Vergleich mit L_M = sbar^mu d_mu
    rel = [sp.simplify(C[mu][0, 0]/sbar[mu][0, 0]) if sbar[mu][0, 0] != 0 else sp.simplify(C[mu][0, 1]/sbar[mu][0, 1]) for mu in range(4)]
    prop = all(sp.simplify(C[mu] - rel[mu]*sbar[mu]) == sp.zeros(2, 2) for mu in range(4))
    res[name] = {'L_T / L_M je Richtung (t,x,y,z)': [str(r) for r in rel], 'proportional_zu_sbar': prop}
out['Bildterm'] = res
# Gesamtoperator und Dispersion (holomorph)
a, b = sp.symbols('a b', positive=True)
w, kx, ky, kz = sp.symbols('omega k_x k_y k_z', real=True)
kv = [w, -kx, -ky, -kz]
for name in ('holomorph', 'hermitesch'):
    rel = [sp.sympify(r) for r in res[name]['L_T / L_M je Richtung (t,x,y,z)']]
    op = sp.zeros(2, 2)
    for mu in range(4):
        op += (a + b*rel[mu])*sbar[mu]*kv[mu]
    det = sp.factor(sp.simplify(op.det()))
    res[name]['Gewicht'] = str(sp.simplify(a + b*rel[0]))
    res[name]['det'] = str(det)
    res[name]['isotrop'] = bool(len(set(rel)) == 1)
    res[name]['K3_Bild_entgegengesetzt'] = bool(rel[0] == -1)
# Skalar: X unter Lambda(i pi) invariant
Lam_num = np.diag([-1.0, 1, 1, -1]); eta = np.diag([1.0, -1, -1, -1])
out['Lambda_erhaelt_eta'] = bool(np.allclose(Lam_num.T @ eta @ Lam_num, eta))
# numerische Probe: Wirkung des Bildes mit Spiegelung t->-t, z->-z und Verschiebung, periodisches Gitter (1+1: t, z)
N = 128; g = np.linspace(0, 2*np.pi, N, endpoint=False); T_, Z_ = np.meshgrid(g, g, indexing='ij')
def field(t, z):
    return np.exp(np.cos(t) + 0.5*np.sin(2*z)) * np.sin(z + 2*t)
def S_T(f):
    k = np.fft.fftfreq(N, d=g[1]-g[0])*2*np.pi
    ft = np.real(np.fft.ifft(1j*k[:, None]*np.fft.fft(f, axis=0), axis=0))
    fz = np.real(np.fft.ifft(1j*k[None, :]*np.fft.fft(f, axis=1), axis=1))
    return (-0.5*(ft**2 - fz**2) - 0.5*f**2).sum()*(g[1]-g[0])**2
s0 = S_T(field(T_, Z_)); s1 = S_T(field(-T_ + 0.7, -Z_ - 1.3))
out['Probe_Spiegelung_Verschiebung'] = {'S_T': s0, 'S_T(Lambda x + delta)': s1, 'rel_diff': abs(s1 - s0)/abs(s0)}
json.dump(out, open('k195_out.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
