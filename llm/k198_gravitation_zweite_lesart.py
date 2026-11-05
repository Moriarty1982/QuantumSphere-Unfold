"""k198: Test H83 - Phasen und Gewichte von Einstein-Cartan, Yang-Mills, Skalar- und Weyl-Kinetik unter drei Regeln.
R2 wird aus g -> -g (Vierbein e -> i e) berechnet, nicht gesetzt. Ausgabe k198_out.json im aktuellen Ordner.
"""
import json
import sympy as sp

out = {}
# ---------- R2: g -> -g an einer allgemeinen diagonalen Metrik (Ricci-Skalar explizit) ----------
t, x, y, z = X = sp.symbols('t x y z')
f = [sp.Function(n)(t, z) for n in ('A', 'B', 'C', 'D')]
def ricci_scalar(g):
    ginv = g.inv()
    n = 4
    Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(n))/2
             for c in range(n)] for b in range(n)] for a in range(n)]
    def Ric(b, c):
        return sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                   + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(n)) for a in range(n))
    return sp.simplify(sum(ginv[b, c]*Ric(b, c) for b in range(n) for c in range(n)))
g = sp.diag(sp.exp(f[0]), -sp.exp(f[1]), -sp.exp(f[2]), -sp.exp(f[3]))
R1_ = ricci_scalar(g); R2_ = ricci_scalar(-g)
sqrt_ratio = sp.simplify(sp.sqrt(abs((-g).det())) / sp.sqrt(abs(g.det())))
out['R2_EC'] = {'R[-g]/R[g]': str(sp.simplify(R2_/R1_)), 'sqrt|g| Verhaeltnis': str(sqrt_ratio)}
# Skalar-Kinetik und Yang-Mills: Zahl der inversen Metriken
out['R2_Skalar_Kinetik_Phase'] = str((-1)**1)
out['R2_YM_Phase'] = str((-1)**2)
out['R2_Potential_Phase'] = '1'
# Weyl: det(e) e_a^mu mit e -> i e
e = sp.symbols('e', positive=True)
weyl_phase = sp.simplify((sp.I*e)**4 / e**4 * (1/(sp.I*e)) / (1/e))
out['R2_Weyl_Phase'] = str(weyl_phase)
ec_phase = sp.simplify((sp.I*e)**4 / e**4 * (1/(sp.I*e))**2 / (1/e)**2)
out['R2_EC_Phase_Vierbein'] = str(ec_phase)

# ---------- Gewichte und Exponenten ----------
bsym = 1/sp.Float(1.8203); xx = bsym**2
a, b = 1/(1+xx), xx/(1+xx); gam = (a+b)/(a-b)
def expo(w):        # Exponent von gamma in 1/w (Kopplung alpha_eff = alpha/w_YM, G_eff = G/w_EC)
    w = complex(sp.N(w))
    if abs(w.imag) > 1e-12:
        return 'komplex'
    return float(sp.N(-sp.log(w.real)/sp.log(gam)))
phases = {
    'R1': {'EC': -1, 'YM': -1, 'Skalar': -1, 'Weyl': -1, 'Potential': 1},
    'R2': {'EC': int(sp.sympify(ec_phase)), 'YM': 1, 'Skalar': -1, 'Weyl': sp.sympify(weyl_phase), 'Potential': 1},
}
res = {}
for rule, ph in phases.items():
    w = {k: a + v*b for k, v in ph.items()}
    res[rule] = {'Gewichte': {k: str(sp.N(v, 6)) for k, v in w.items()},
                 'alpha_Exponent': expo(w['YM']), 'G_Exponent': expo(w['EC']),
                 'Wirkung reell': all(sp.im(sp.N(v)) == 0 for v in w.values())}
# R3: eine Wirkung auf c*g, c = a - b
c = a - b
res['R3'] = {'EC Faktor': 'c (sqrt|cg| R[cg] = c sqrt|g| R)', 'YM Faktor': '1', 'Skalar Faktor': 'c', 'Potential Faktor': 'c^2',
             'alpha_Exponent': 0.0, 'G_Exponent': float(sp.N(-sp.log(c)/sp.log(gam))), 'Wirkung reell': True}
out['Regeln'] = res
out['r19'] = {'alpha': 1, 'G_N': 2}
out['H83'] = any(isinstance(r['alpha_Exponent'], float) and abs(abs(r['alpha_Exponent']) - 1) < 1e-9
                 and isinstance(r['G_Exponent'], float) and abs(abs(r['G_Exponent']) - 2) < 1e-9 and r['Wirkung reell']
                 for r in res.values())
json.dump(out, open('k198_out.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
