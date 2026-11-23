"""k240: H120, Medium aus lichtartigen Strukturen (Lesart a). Vorab-Notiz llm/Vorab_Notiz_H120_Nullmedium.md (Commit d3810e58).
Universelle effektive Metrik G = eta + kappa * sum_s w_s l_s l_s fuer Higgsradius und beide Vermittler; Kegelgrenze wie r47.
Aufruf: python k240_h120_null_medium.py   (keine Daten, keine Pfade)"""
import numpy as np
import sympy as sp

Z, G0, GM = 1.0, 0.03, 0.03


def medium_r(theta, kw):
    """groesstes v^2 der Wurzeln von v^2 - 1 + sum_s kappa w_s (v - s c)^2 = 0; kw = [(kappa*w_s, s), ...]."""
    c = np.cos(theta)
    A2 = 1.0 + sum(k for k, s in kw)
    A1 = -2.0 * sum(k * s * c for k, s in kw)
    A0 = -1.0 + sum(k * c * c for k, s in kw)
    roots = np.roots([A2, A1, A0])
    return max(abs(x) ** 2 for x in roots)


def cone_max(r, al, ch2=None):
    """groesstes Geschwindigkeitsquadrat des gekoppelten Hauptteils (r47) mit c_h^2 = r0 = rm = r (universell), falls ch2 None."""
    ch2 = r if ch2 is None else ch2
    A = Z - 2 * GM / 3
    b = Z * ch2 + 2 * GM / 3 * (r - al)
    j0 = np.sqrt(G0 * al ** 2 / 2)
    jm = np.sqrt(2 * GM / 3 * (r ** 2 - r * al + al ** 2))
    Kh = np.diag([1 / np.sqrt(A), 1, 1])
    V = np.array([[b, j0, jm], [j0, r, 0], [jm, 0, r]])
    return max(np.linalg.eigvalsh(Kh @ V @ Kh))


thetas = np.linspace(0, np.pi, 41)
alphas = np.linspace(0, 1, 21)
print('Kontrolle: Vergleichsmodell r = 1/2 ueberall: max =', round(max(cone_max(0.5, al) for al in alphas), 6))

# ---- H120a: ein Strahl ----
print('H120a (ein Strahl l = (1,0,0,1)):')
for k in (0.1, 1.0, 10.0, 100.0):
    r0 = medium_r(0.0, [(k, +1)])
    worst = max(cone_max(r0, al) for al in alphas)
    print(f'   kappa w = {k}: r in Richtung l = {r0:.12f}; groesstes Geschwindigkeitsquadrat dort (ueber alpha) = {worst:.6f}')

# ---- H120b: zwei Gegenstroeme ----
def worst_over_grid(kw):
    rs = [medium_r(t, kw) for t in thetas]
    return max(cone_max(r, al) for r in rs for al in alphas), min(rs), max(rs)

print('H120b (zwei Gegenstroeme, konservativ: alle theta x alpha):')
found = []
for ka in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0):
    for kb in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0):
        w, rmin, rmax = worst_over_grid([(ka, +1), (kb, -1)])
        if w <= 1 + 1e-9:
            found.append((ka, kb, w, rmin, rmax))
print(f'   Parametersaetze mit Kegelgrenze in allen Richtungen: {len(found)} von 49')
for f in found[:6]:
    print(f'      kappa a = {f[0]}, kappa b = {f[1]}: max = {f[2]:.6f}, r zwischen {f[3]:.4f} und {f[4]:.4f}')
# geometrisch statt konservativ, n parallel z (alpha = sin^2 theta) und n = x (alpha = 1 - sin^2 theta cos^2 phi)
ka = kb = 0.3
rs = {t: medium_r(t, [(ka, +1), (kb, -1)]) for t in thetas}
geo_z = max(cone_max(rs[t], np.sin(t) ** 2) for t in thetas)
geo_x = max(cone_max(rs[t], 1 - np.sin(t) ** 2 * np.cos(p) ** 2) for t in thetas for p in np.linspace(0, np.pi, 9))
print(f'   geometrisch bei kappa a = kappa b = 0.3: n || z: {geo_z:.6f}; n = x: {geo_x:.6f}')
# Zusatz: Beobachter mit Rapiditaet eta entlang z sieht a e^{-2 eta}, b e^{2 eta}
print('   Zusatz \"nur in P\": groesste Verlangsamung max_theta(1 - r) fuer kappa a = kappa b = 0.3 bei Rapiditaet eta:')
for eta in (0.0, 0.6, 1.0, 2.0, 4.0, 8.0):
    kw = [(0.3 * np.exp(-2 * eta), +1), (0.3 * np.exp(2 * eta), -1)]
    rr = [medium_r(t, kw) for t in thetas]
    worst = max(cone_max(r, al) for r in rr for al in alphas)
    print(f'      eta = {eta}: max(1 - r) = {1 - min(rr):.6f}, min(1 - r) = {1 - max(rr):.3e}, Kegelgrenze max = {worst:.6f}')

# ---- H120c: Mindestverlangsamung ----
g, r, al, e = sp.symbols('g r alpha epsilon', positive=True)
Zs = sp.Integer(1)
upper = (Zs * (1 - r) - sp.Rational(2, 3) * g * (1 + r - al)) * (1 - r) - g * al ** 2 / 2 - sp.Rational(2, 3) * g * (r ** 2 - r * al + al ** 2)
lead = sp.expand(upper.subs(r, 1 - e))
print('H120c: obere Bedingung (mal (1 - r)) mit r = 1 - epsilon:', sp.collect(lead, e))
h = sp.Rational(1, 2) * al ** 2 + sp.Rational(2, 3) * (1 - al + al ** 2)
print('   Koeffizient von g bei epsilon = 0: -(alpha^2/2 + 2/3 (1 - alpha + alpha^2)); Maximum auf [0, 1]:',
      sp.maximum(h, al, sp.Interval(0, 1)), 'bei alpha = 1')
for gv in (sp.Rational(3, 100), sp.Rational(1, 10**4), sp.Rational(1, 10**8)):
    sol = sp.nsolve(lead.subs({g: gv, al: 1}), e, 0.5 if gv > 1e-3 else 1e-2)
    print(f'   g = {gv}: kleinstes epsilon bei alpha = 1: {float(sol):.6e};  sqrt(7 g/6) = {float(sp.sqrt(sp.Rational(7, 6) * gv)):.6e}')
eps_lv = 1e-13
print(f'   Laborgrenze epsilon <= {eps_lv:g}: g_m^2 <= (6/7) epsilon^2 = {6 / 7 * eps_lv ** 2:.3e}')
