"""k373 (Nachtrag zu H175, NACHTRAEGLICH, nicht vorab festgelegt, 26.11.2026):
In H175c ist mit x_R der Fall kappa = +tan x, Richtung (K-1 + K-2)/sqrt2 vertraeglich. Die Richtung ist nach Ansicht von 16 Faellen ausgewaehlt.
Hier: ein einziger Parameter x fuer Neutrino-Spektrum (R), Staerke kappa = tan x und alle drei Winkel. 4 Messgroessen, 1 Parameter.
Aufruf: python3 -u k373_nachtrag_gemeinsam.py > k373_out.txt
"""
import numpy as np
from scipy.optimize import minimize_scalar
import k371_test_h175 as K
R_OBS, R_ERR = 0.030016, 0.000457
r2 = np.sqrt(2)
def Rratio(d):
    m = np.sort(np.array([1 + r2 * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])**2)
    return (m[1]**2 - m[0]**2) / (m[2]**2 - m[0]**2)
CASES = {"(K-1 + K-2)/sqrt2": (1 / r2, 1 / r2), "K-2 allein": (0, 1), "K-1 allein": (1, 0), "(K-1 - K-2)/sqrt2": (1 / r2, -1 / r2), "ohne Term (H173)": (0, 0)}
for nm, vec in CASES.items():
    for sg in (1, -1):
        if nm.startswith("ohne") and sg < 0: continue
        def parts(x):
            obs, _ = K.make(x)
            o = obs(["K-1", "K-2"], sg * np.tan(x) * np.array(vec))
            if o is None: return None
            zz = K.z(*o[2][:3]); zR = (Rratio(np.pi / 6 - x) - R_OBS) / R_ERR
            return zz, zR, o
        f = lambda x: (lambda p: 1e6 if p is None else float(sum(np.array(p[0])**2) + p[1]**2))(parts(x))
        xs = np.linspace(0.03, 0.06, 61); v = [f(x) for x in xs]; x0 = xs[int(np.argmin(v))]
        r = minimize_scalar(f, bounds=(x0 - 0.0005, x0 + 0.0005), method='bounded', options={'xatol': 1e-9})
        p = parts(r.x)
        print(f"{'+' if sg > 0 else '-'}tan x, {nm}: bestes x = {r.x:.5f}, chi2 = {r.fun:.2f} (4 Messgroessen, 1 Parameter); z(R) = {p[1]:+.2f}; " + K.line(p[2][2]) + f"; rho = {p[2][0]:.5f}")
        if nm.startswith("(K-1 + K-2)") and sg > 0:
            # Fehlerband in x: chi2 + 1
            lo = [x for x in np.linspace(r.x - 0.004, r.x, 400) if f(x) < r.fun + 1][0]; hi = [x for x in np.linspace(r.x, r.x + 0.004, 400) if f(x) < r.fun + 1][-1]
            print(f"      x = {r.x:.5f} (+{hi - r.x:.5f}/-{r.x - lo:.5f}); zum Vergleich x der geladenen Leptonen 0.039577 ({(0.0395773407 - r.x)/((hi - lo)/2):+.1f} sigma), chi2 dort {f(0.0395773407):.1f}")
