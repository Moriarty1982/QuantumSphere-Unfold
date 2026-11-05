"""k193: Geist-Kondensat P(X) = -X/2 + c X^2 auf FRW (Erkundung).
Erhaltungsgroesse a^3 P_X sqrt(X) = C; Entwicklung um X0 = 1/(4c): rho = rho_L + Staub ~ C/a^3.
Numerik: Feldgleichung mit H aus Friedmann (nur Kondensat), Kontrolle der Skalierung."""
import json
import numpy as np, sympy as sp
X, c, C, a = sp.symbols('X c C a', positive=True)
P = -X/2 + c*X**2; PX = sp.diff(P, X); X0 = sp.Rational(1, 4)/c
rho = 2*X*PX - P
# lineare Ordnung: X = X0 + d, P_X ~ 2c d, a^3 * 2c d * sqrt(X0) = C
d = C/(a**3*2*c*sp.sqrt(X0))
rho_lin = sp.series(rho.subs(X, X0 + sp.Symbol('e')), sp.Symbol('e'), 0, 2).removeO().subs(sp.Symbol('e'), d)
out = {'rho_L': str(sp.simplify(rho.subs(X, X0))), 'rho_lin': str(sp.simplify(sp.expand(rho_lin))),
       'p_lin': str(sp.simplify(sp.series(P.subs(X, X0 + sp.Symbol('e')), sp.Symbol('e'), 0, 2).removeO().subs(sp.Symbol('e'), d)))}
# Numerik: c = 1, Einheiten 8 pi G/3 = 1; y = ln a; Zustand X(y) aus Erhaltung loesen
cn = 1.0; x0 = 0.25/cn
def Xof(a_, Cn):
    # loese P_X sqrt(X) = Cn/a^3 auf dem Ast X > X0
    f = lambda x: (-0.5 + 2*cn*x)*np.sqrt(x) - Cn/a_**3
    lo, hi = x0, x0 + 10.0
    for _ in range(200):
        mid = 0.5*(lo+hi); (lo, hi) = (mid, hi) if f(mid) < 0 else (lo, mid)
    return 0.5*(lo+hi)
res = {}
for Cn in (0.0, 0.01, 0.1):
    rows = []
    for a_ in (1.0, 2.0, 4.0, 8.0):
        x = Xof(a_, Cn); r = 2*x*(-0.5 + 2*cn*x) - (-x/2 + cn*x**2); p = -x/2 + cn*x**2
        rows.append({'a': a_, 'rho': r, 'w': p/r, '(rho-rhoL)*a^3': (r - 1/(16*cn))*a_**3})
    res[str(Cn)] = rows
out['numerik'] = res
json.dump(out, open('k193_out.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
