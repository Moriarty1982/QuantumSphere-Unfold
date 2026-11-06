"""k216: Test H97 - rueckgekoppelte Kaskade (Vakuum zerfaellt mit Rate beta^2 * eps * H in Materie) gegen DESI DR2 BAO.
Vorab-Notiz llm/Vorab_Notiz_H97_Bruecke_DESI_DR2.md (Commit de36fcc).
Daten: arXiv:2503.14738 Tabelle IV (HTML-Fassung), mit Systematik.
Aufruf (aus llm/): python k216_bruecke_desi_dr2.py
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import minimize_scalar
from scipy.stats import chi2

C100 = 2997.92458                      # c/(100 km/s/Mpc) in Mpc
Or = 9.1e-5
b2 = 0.3018465583346331
# (z, D_V) und (z, D_M, sD_M, D_H, sD_H, r)
BGS = (0.295, 7.942, 0.075)
AN = [(0.510, 13.588, 0.167, 21.863, 0.425, -0.459), (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
      (0.934, 21.576, 0.152, 17.641, 0.193, -0.416), (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
      (1.484, 30.512, 0.760, 12.817, 0.516, -0.500), (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]


def E_lcdm(Om):
    OL = 1 - Om - Or
    return lambda z: np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OL)


def E_kaskade(Om, eps):
    OL = 1 - Om - Or
    def rhs(x, y):                                   # x = ln a
        return [-3*y[0] + b2*eps*y[1], -b2*eps*y[1]]
    xs = np.linspace(0, -np.log(1 + 3.0), 3000)
    s = solve_ivp(rhs, (0, xs[-1]), [Om, OL], t_eval=xs, rtol=1e-11, atol=1e-14)
    zz = np.exp(-s.t) - 1; E2 = s.y[0] + s.y[1] + Or*(1 + zz)**4
    return lambda z: np.sqrt(np.interp(z, zz, E2))


def theory(E):
    DM = lambda z: quad(lambda t: 1/E(t), 0, z, limit=200)[0]
    out = []
    zv = BGS[0]; dm = DM(zv); out.append((zv*dm**2/E(zv))**(1/3))
    for (z, *_ ) in AN:
        out += [DM(z), 1/E(z)]
    return np.array(out)


def data_cov():
    d = [BGS[1]]; C = np.zeros((13, 13)); C[0, 0] = BGS[2]**2
    for i, (z, dm, sdm, dh, sdh, r) in enumerate(AN):
        j = 1 + 2*i; d += [dm, dh]
        C[j, j] = sdm**2; C[j+1, j+1] = sdh**2; C[j, j+1] = C[j+1, j] = r*sdm*sdh
    return np.array(d), np.linalg.inv(C)


d, Ci = data_cov()


def chi2_min(E):
    f = theory(E)                                   # Beobachtung = A f, A = C100/(h r_d)
    A = (f @ Ci @ d)/(f @ Ci @ f); r = d - A*f
    return float(r @ Ci @ r), C100/A


# Gueltigkeitskontrolle: LCDM mit freiem Om
res = minimize_scalar(lambda Om: chi2_min(E_lcdm(Om))[0], bounds=(0.2, 0.45), method='bounded', options={'xatol': 1e-6})
Om_fit = res.x; c_fit, hrd_fit = chi2_min(E_lcdm(Om_fit))
# Fehler aus Delta chi2 = 1
grid = np.linspace(Om_fit - 0.03, Om_fit + 0.03, 121); cg = np.array([chi2_min(E_lcdm(o))[0] for o in grid])
inside = grid[cg <= c_fit + 1]
print(f'Kontrolle LCDM: Om = {Om_fit:.4f} (+{inside.max()-Om_fit:.4f}/-{Om_fit-inside.min():.4f}), h r_d = {hrd_fit:.2f} Mpc, chi2 = {c_fit:.2f}')
ok = abs(Om_fit - 0.2975) <= 0.003 and abs(hrd_fit - 101.54) <= 0.5
print('Gueltigkeit erfuellt:', ok)
cL, hL = chi2_min(E_lcdm(b2)); print(f'LCDM bei Om = beta^2: chi2 = {cL:.2f}, p = {chi2.sf(cL, 12):.3f}, h r_d = {hL:.2f}')
cK, hK = chi2_min(E_kaskade(b2, 1.0)); pK = chi2.sf(cK, 12)
print(f'H97 Kaskade eps=1: chi2 = {cK:.2f}, p = {pK:.2e}, h r_d = {hK:.2f}  -> {"widerlegt" if pK < 0.01 else "nicht ausgeschlossen"}')
# Erkundung (nachtraeglich erlaubt): eps-Bereich bei Om = beta^2
for eps in (0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0):
    c, _ = chi2_min(E_kaskade(b2, eps)); print(f'  eps = {eps:.2f}: chi2 = {c:.2f}, p = {chi2.sf(c, 12):.3f}')
