"""k194: Test H78 - T-Anteil als zweite Lesart desselben Feldes (k174: psi_T(x) = -i sigma_z psi(x+delta)).
Skalar und Weyl im flachen Raum, Gewichte a (M), b (T). Ausgabe k194_out.json im aktuellen Ordner.
"""
import json
import numpy as np
import sympy as sp

out = {}
a, b, m, delta = sp.symbols('a b m delta', positive=True)
Xs, Vs = sp.symbols('X V')

# --- H78a Skalar: Koeffizienten und Unabhaengigkeit von delta (numerisch auf periodischem Gitter) ---
LM = Xs/2 - Vs
LT = -Xs/2 - Vs                        # Lesart B
Ltot = sp.expand(a*LM + b*LT)
out['H78a_koeffizienten'] = {'X': str(sp.factor(Ltot.coeff(Xs))), 'V': str(sp.factor(Ltot.coeff(Vs)))}
# wirksame Masse: (a-b)/2 (phi_t^2 - ...) - (a+b) m^2 phi^2/2  ->  m_eff^2 = (a+b)/(a-b) m^2
out['H78a_meff2_durch_m2'] = str(sp.simplify((a + b)/(a - b)))
x0 = 0.6/1.6  # bsym^2 Platzhalter nicht noetig; Materie-Gewichte aus x = bsym^2
bsym = 1/1.8203; x = bsym**2; pp, pm = 1/(1+x), x/(1+x); gam = (1+x)/(1-x)
out['Materiegewichte'] = {'p+': pp, 'p-': pm, 'a-b': pp-pm, '1/gamma': 1/gam, '(a+b)/(a-b)': (pp+pm)/(pp-pm), 'gamma': gam}
# numerische Probe: S_T[phi(.+delta)] = S_T[phi] auf periodischem Gitter (Raumzeit 1+1, Periode 2 pi)
N = 128; g = np.linspace(0, 2*np.pi, N, endpoint=False); T_, Xg = np.meshgrid(g, g, indexing='ij')
def field(t, xx):
    return np.exp(np.cos(t) + 0.5*np.sin(2*xx)) * np.sin(xx + 2*t)  # 2 pi-periodisch in t und x (Lauf 1 hatte 0.3*t, nicht periodisch)
def action_T(dt, dx, mm=1.0):
    f = field(T_ + dt, Xg + dx)
    k = np.fft.fftfreq(N, d=g[1]-g[0])*2*np.pi
    ft = np.real(np.fft.ifft(1j*k[:, None]*np.fft.fft(f, axis=0), axis=0))
    fx = np.real(np.fft.ifft(1j*k[None, :]*np.fft.fft(f, axis=1), axis=1))
    L = -0.5*(ft**2 - fx**2) - 0.5*mm**2*f**2
    return L.sum()*(g[1]-g[0])**2
S0 = action_T(0, 0); S1 = action_T(0.7, -1.3)
out['H78a_delta_probe'] = {'S_T(0)': S0, 'S_T(delta)': S1, 'rel_diff': abs(S1-S0)/abs(S0)}

# --- H78b Weyl ---
I2 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
sbar = [I2, -sx, -sy, -sz]                       # sigma-bar^mu
S = -sp.I*sz                                     # psi_T = S psi
R = []
for mu in range(4):
    Mmu = sp.simplify(S.H*sbar[mu]*S)
    # Mmu = R^mu_nu sbar^nu, diagonal erwartet
    coeff = [sp.simplify((Mmu*sbar[nu]).trace()/2) * (1 if nu == 0 else 1) for nu in range(4)]
    R.append(coeff)
# Projektion: tr(sbar^mu sbar^nu)/2 = diag(1,1,1,1) fuer diese Basis
out['H78b_R'] = [[str(c) for c in row] for row in R]
w, kx, ky, kz = sp.symbols('omega k_x k_y k_z', real=True)
# ebene Welle psi ~ exp(-i(w t - k.x)): i d_t -> w, i d_j -> -k_j
kvec = [w, -kx, -ky, -kz]
op = sp.zeros(2, 2)
for mu in range(4):
    op += a*sbar[mu]*kvec[mu]
    TT = S.H*sbar[mu]*S
    op += -b*TT*kvec[mu]                          # F3-Vorzeichen
op = sp.simplify(op)
out['H78b_operator'] = str(op)
disp = sp.factor(sp.simplify(op.det()))
out['H78b_det'] = str(disp)
w2 = sp.solve(sp.Eq(op.det(), 0), w)
out['H78b_omega'] = [str(sp.simplify(s)) for s in w2]
q = sp.simplify((a + b)/(a - b))
check = sp.simplify(op.det() - (a-b)**2*(w**2 - kz**2 - q**2*(kx**2 + ky**2)))
out['H78b_dispersion_check_(sollte 0)'] = str(check)
out['H78b_delta_frei'] = 'delta tritt in der Wirkung nicht auf (Verschiebung des Arguments; Integral translationsinvariant, numerisch fuer den Skalar gezeigt)'
# Hamilton-Operator (a>b): H = (op ohne omega-Teil)/(a-b) hermitesch -> reelle Eigenwerte +-|k_eff|
Hk = sp.simplify(-(op - op.subs(w, 0))/w) if False else None
Hop = sp.simplify(-(op.subs(w, 0))/(a - b))
ev = [sp.simplify(e) for e in Hop.eigenvals()]
out['H78b_H_hermitesch'] = bool(sp.simplify(Hop - Hop.H) == sp.zeros(2, 2))
out['H78b_eigenwerte'] = [str(e) for e in ev]
out['H78b_q_Materiegewichte'] = (pp + pm)/(pp - pm)
json.dump(out, open('k194_out.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
