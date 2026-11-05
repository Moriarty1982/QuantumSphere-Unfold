"""k192: Test H77 - Lesarten A, B, B' des Tachyonbilds einer Wirkung gegen K1-K3.
Ein reeller Skalar in 1+1 Dimensionen; sympy. Ausgabe k192_out.json im aktuellen Ordner.
"""
import json
import sympy as sp

t, x, k, m, A0 = sp.symbols('t x k m A0', positive=True)
w = sp.symbols('omega')
chi = sp.Function('chi')(t, x)
ct, cx = sp.diff(chi, t), sp.diff(chi, x)
LM = sp.Rational(1, 2) * (ct ** 2 - cx ** 2) - sp.Rational(1, 2) * m ** 2 * chi ** 2
L = {'M': LM, 'A': -LM,
     'B': -sp.Rational(1, 2) * (ct ** 2 - cx ** 2) - sp.Rational(1, 2) * m ** 2 * chi ** 2,
     "B'": sp.Rational(1, 2) * (ct ** 2 - cx ** 2) + sp.Rational(1, 2) * m ** 2 * chi ** 2}

def euler_lagrange(Lx):
    return sp.diff(sp.diff(Lx, ct), t) + sp.diff(sp.diff(Lx, cx), x) - sp.diff(Lx, chi)

def dispersion(Lx):
    mode = sp.exp(sp.I * (k * x - w * t))
    e = sp.simplify(euler_lagrange(Lx).subs(chi, mode).doit() / mode)
    return sp.solve(sp.Eq(e, 0), w ** 2)[0] if sp.solve(sp.Eq(e, 0), w ** 2) else sp.solve(e, w)

def energy_mean(Lx, om2):
    """Hamiltondichte H = pi chi_t - L, gemittelt ueber eine Periode einer laufenden Mode A0 cos(kx - wt)."""
    pi = sp.diff(Lx, ct)
    H = pi * ct - Lx
    om = sp.sqrt(om2)
    mode = A0 * sp.cos(k * x - om * t)
    Hm = H.subs(chi, mode).doit()
    T = 2 * sp.pi / om
    return sp.simplify(sp.integrate(Hm.subs(x, 0), (t, 0, T)) / T)

out = {}
for name, Lx in L.items():
    om2 = sp.simplify(sp.solve(sp.Eq(sp.simplify(euler_lagrange(Lx).subs(chi, sp.exp(sp.I * (k * x - w * t))).doit()
                                                  / sp.exp(sp.I * (k * x - w * t))), 0), w ** 2)[0])
    E = energy_mean(Lx, om2)
    massless_ratio = sp.simplify(Lx.subs(m, 0) / LM.subs(m, 0))
    out[name] = {'omega2': str(om2), 'E_mean': str(E), 'L_T/L_M (m=0)': str(massless_ratio)}

EM = sp.sympify(out['M']['E_mean'].replace('omega', 'w'), locals={'A0': A0, 'k': k, 'm': m})
for name in ('A', 'B', "B'"):
    om2 = sp.sympify(out[name]['omega2'], locals={'k': k, 'm': m})
    K1 = sp.simplify(om2 - (k ** 2 - m ** 2)) == 0
    K2 = out[name]['L_T/L_M (m=0)'] == '-1'
    E = sp.sympify(out[name]['E_mean'], locals={'A0': A0, 'k': k, 'm': m})
    # Vorzeichen fuer k > m (laufende Mode) gegen Materie-Mode gleichen k
    kk, mm = 2, 1
    sE = sp.sign(E.subs({A0: 1, k: kk, m: mm})); sM = sp.sign(EM.subs({A0: 1, k: kk, m: mm}))
    K3 = bool(sE == -sM)
    out[name].update({'K1': bool(K1), 'K2': bool(K2), 'K3': K3, 'vertraeglich': bool(K1 and K2 and K3)})
# Potential-/Vakuumterm: Vorzeichen eines konstanten Potentials V0 in der Energiedichte je Lesart
V0 = sp.symbols('V0')
LMV = LM - V0
LV = {'M': LMV, 'A': -LMV, 'B': L['B'] - V0, "B'": -(L['B'] - V0)}   # B: Potential bleibt; B' = -B
for name, Lx in LV.items():
    H = sp.diff(Lx, ct) * ct - Lx
    out[name]['Vakuumenergie_von_V0'] = str(sp.simplify(H.subs(chi, 0).doit()))
json.dump(out, open('k192_out.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
