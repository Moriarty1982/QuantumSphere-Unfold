"""k197: Test H82 - effektive Massen und Kopplungen unter der zweiten Lesart, Vergleich mit den Gewichten aus r19.
Ableitungsterme mit K = a - b, uebrige mit P = a + b; kanonische Normierung. Ausgabe k197_out.json im aktuellen Ordner.
"""
import json
import sympy as sp

K, P, g, y, mu, lam, kap, m, gam = sp.symbols('K P g y mu lambda kappa m gamma', positive=True)
out = {}
# Majorana-/Dirac-Massenterm invariant unter S = -i sigma_z?
S = sp.Matrix([[-sp.I, 0], [0, sp.I]]); eps = sp.Matrix([[0, 1], [-1, 0]])
out['S^T eps S = eps'] = bool(sp.simplify(S.T*eps*S - eps) == sp.zeros(2, 2))
out['S eps S^T = eps (h.c.-Teil, holomorph)'] = bool(sp.simplify(S*eps*S.T - eps) == sp.zeros(2, 2))

# Lagrangedichte in Feldern phi, psi, A (Koeffizienten), kanonisch: phi = phic/sqrt(K) usw.
c = 1/sp.sqrt(K)
eff = {
    'g': g*c,                                   # aus |D phi|^2 bzw. psi-bar sigma D psi: g A -> g c A_c
    'y': P*y*c**3,                              # P y phi psi psi
    'mu2': P*mu**2*c**2,                        # P mu^2 phi^2 / 2
    'lambda': P*lam*c**4,                       # P lambda phi^4 / 4
    'm_Majorana': P*m*c**2,                     # P m psi psi
    'kappa': kap/K,                             # K/(2 kappa) e R
}
v2 = sp.simplify(eff['mu2']/eff['lambda']); v2_0 = mu**2/lam
derived = {
    'alpha': eff['g']**2/g**2,
    'v': sp.sqrt(v2/v2_0),
    'm_f = y v': sp.simplify(eff['y']*sp.sqrt(v2)/(y*sp.sqrt(v2_0))),
    'm_H^2 = 2 mu^2': eff['mu2']/mu**2,
    'm_H': sp.sqrt(eff['mu2']/mu**2),
    'm_W = g v / 2': sp.simplify(eff['g']*sp.sqrt(v2)/(g*sp.sqrt(v2_0))),
    'm_Majorana': eff['m_Majorana']/m,
    'G_N': eff['kappa']/kap,
    'l_P = sqrt(G)': sp.sqrt(eff['kappa']/kap),
    'm_P = 1/sqrt(G)': 1/sp.sqrt(eff['kappa']/kap),
    'theta_W (g, g\' gleich skaliert)': sp.Integer(1),
}
sub = {K: 1/gam, P: 1}
expo = {}
for name, f in derived.items():
    fg = sp.simplify(f.subs(sub))
    e = sp.simplify(sp.diff(sp.log(fg), gam)*gam)
    expo[name] = {'Faktor (allgemein)': str(sp.simplify(f)), 'Faktor (Materie-Gewichte)': str(fg), 'Exponent von gamma': str(e)}
out['H82a'] = expo
r19 = {'alpha': 1, 'alpha_s (wie alpha)': 1, 'G_N': 2, 'l_P = sqrt(G)': sp.Rational(3, 2), 'theta_W (g, g\' gleich skaliert)': 0}
cmp = {}
for name, k in r19.items():
    key = 'alpha' if name.startswith('alpha_s') else name
    e = sp.sympify(expo[key]['Exponent von gamma'])
    cmp[name] = {'k(r19)': str(k), 'Exponent': str(e), 'passt (|e| = |k|)': bool(abs(e) == abs(k))}
out['H82b'] = cmp
out['H82b_gesamt'] = all(v['passt (|e| = |k|)'] for v in cmp.values())
json.dump(out, open('k197_out.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
