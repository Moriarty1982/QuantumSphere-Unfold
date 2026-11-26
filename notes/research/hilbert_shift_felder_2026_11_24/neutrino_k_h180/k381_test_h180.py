"""k381 (H180): K der Neutrinos frei gegen K = 2/3. Aufruf aus diesem Ordner: python3 -u k381_test_h180.py > k381_out.txt"""
import os, sys, numpy as np
from scipy.optimize import minimize, brentq
here = os.path.dirname(os.path.abspath(__file__)); os.chdir(os.path.join(here, "..", "mischung_h175")); sys.path.insert(0, os.getcwd())
import k371_test_h175 as K
r2 = np.sqrt(2); R_OBS, R_ERR = 0.030016, 0.000457
KDIR = (K.DIRS["K-1"] + K.DIRS["K-2"]) / r2

def lam(rho, d): return np.array([1 + r2 * rho * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
def Rratio(rho, d):
    m = np.sort(lam(rho, d)**2); return (m[1]**2 - m[0]**2) / (m[2]**2 - m[0]**2)
def Nhat(rho, d, sb=1):
    l = lam(rho, d); l = l[np.argsort(abs(l))]; c = l[0] - 1; b2 = ((l[1] - l[2])**2 - c**2) / 8
    if b2 < 0: return None
    b = sb * np.sqrt(b2); return np.array([[1, b, c], [b, 1, -b], [c, -b, 1]])
_ue = {}
def Ue(kap):
    k = round(float(kap), 7)
    if k not in _ue:
        s = K.solve(k * KDIR, 0.0); _ue[k] = None if s is None else s[2]
    return _ue[k]
def obs(rho, d, kap):
    N = Nhat(rho, d); U = Ue(kap)
    if N is None or U is None: return None
    r = K.pmns(U, K.eig_sorted(N)[1]); zz = K.z(*r[:3]); zR = (Rratio(rho, d) - R_OBS) / R_ERR
    return r, zz, zR
def chi2(rho, d, kap):
    o = obs(rho, d, kap); return 1e6 if o is None else float(sum(np.array(o[1])**2) + o[2]**2)
def sigma_m(rho, d):
    l2 = np.sort(lam(rho, d)**2); s = np.sqrt(7.53e-5 / (l2[1]**2 - l2[0]**2)); return 1e3 * s * l2
def roots(rho):
    ds = np.linspace(1e-4, np.pi / 3 - 1e-4, 4001); v = np.array([Rratio(rho, d) for d in ds]) - R_OBS
    return [brentq(lambda d: Rratio(rho, d) - R_OBS, ds[i], ds[i + 1]) for i in np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0] if abs(v[i] - v[i + 1]) < 0.5]
def fit(rho, free_kap=True):
    best = None
    for d0 in roots(rho):
        for k0 in ((-0.045, 0.0, 0.045) if free_kap else (0.0,)):
            if free_kap: r = minimize(lambda p: chi2(rho, p[0], p[1]), [d0, k0], method="Nelder-Mead", options={"xatol": 1e-7, "fatol": 1e-9, "maxiter": 600}); p = (r.x[0], r.x[1])
            else: r = minimize(lambda p: chi2(rho, p[0], 0.0), [d0], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10}); p = (r.x[0], 0.0)
            if best is None or r.fun < best[0]: best = (r.fun, p[0], p[1])
    return best

print("== Kontrolle: rho_nu = 1, delta_nu = pi/6 - x, kappa = tan x, x = 0,04478 (H176) ==")
x = 0.04478; o = obs(1.0, np.pi / 6 - x, np.tan(x))
print(f"   s12 = {o[0][0]:.4f}, s23 = {o[0][1]:.4f}, s13 = {o[0][2]:.5f}, sin delta_CP = {o[0][3]:+.3f}, z = ({o[1][0]:+.2f}, {o[1][1]:+.2f}, {o[1][2]:+.2f}), z_R = {o[2]:+.2f}, chi2 = {chi2(1.0, np.pi/6 - x, np.tan(x)):.2f} (k373: 2,86)")

print("\n== H180a: Profil ueber rho_nu, frei delta_nu und kappa ==")
print("   rho_nu | K_nu | chi2_min | delta_nu | kappa | s12 | s23 | s13 | sin dCP | Summe m [meV]")
rhos = np.unique(np.round(np.concatenate([np.arange(0.60, 1.5001, 0.025), np.arange(0.93, 1.0601, 0.005)]), 3)); prof = []
for rho in rhos:
    b = fit(rho)
    if b is None or b[0] > 1e5: print(f"   {rho:.3f} | {(1+rho**2)/3:.4f} | keine Loesung (R nicht erreichbar, b^2 < 0 oder Massen der geladenen Leptonen nicht anpassbar)"); continue
    o = obs(rho, b[1], b[2]); sm = sigma_m(rho, b[1]); prof.append((rho, b[0], b[1], b[2], sm.sum(), o[0][3]))
    print(f"   {rho:.3f} | {(1+rho**2)/3:.4f} | {b[0]:8.2f} | {b[1]:.5f} | {b[2]:+.5f} | {o[0][0]:.4f} | {o[0][1]:.4f} | {o[0][2]:.5f} | {o[0][3]:+.3f} | {sm.sum():.1f}", flush=True)
prof = np.array(prof); cmin = prof[:, 1].min(); im = prof[:, 1].argmin()
okr = prof[prof[:, 1] < cmin + 4]
print(f"   globales Minimum: chi2 = {cmin:.2f} bei rho_nu = {prof[im, 0]:.3f} (K_nu = {(1+prof[im,0]**2)/3:.4f}); chi2 bei rho_nu = 1: {prof[np.argmin(abs(prof[:,0]-1)), 1]:.2f}")
print(f"   Bereich Delta chi2 < 4: rho_nu von {okr[:,0].min():.3f} bis {okr[:,0].max():.3f} (K_nu von {(1+okr[:,0].min()**2)/3:.4f} bis {(1+okr[:,0].max()**2)/3:.4f}); Summe m dort {okr[:,4].min():.1f} bis {okr[:,4].max():.1f} meV; sin dCP {okr[:,5].min():+.3f} bis {okr[:,5].max():+.3f}")
has1 = (okr[:, 0].min() <= 1 <= okr[:, 0].max()); wide = (okr[:, 0].max() - 1 > 0.1) or (1 - okr[:, 0].min() > 0.1)
edge = okr[:, 0].min() <= rhos[0] + 1e-9 or okr[:, 0].max() >= rhos[-1] - 1e-9
print(f"   Urteil H180a: {'DATEN BEVORZUGEN FREIES K_nu' if not has1 else ('DATEN UNTERSCHEIDEN NICHT' if wide else 'DATEN STUETZEN K_nu ~ 2/3')}" + (" (Bereich reicht bis an den Rand des Rasters)" if edge else ""))

print("\n== H180b: kappa = 0, frei rho_nu und delta_nu ==")
pb = []
for rho in rhos:
    b = fit(rho, False)
    if b is not None and b[0] < 1e5: pb.append((rho, b[0], b[1]))
pb = np.array(pb); j = pb[:, 1].argmin()
r = minimize(lambda p: chi2(p[0], p[1], 0.0), [pb[j, 0], pb[j, 2]], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10})
o = obs(r.x[0], r.x[1], 0.0)
print(f"   bestes chi2 = {r.fun:.2f} bei rho_nu = {r.x[0]:.4f} (K_nu = {(1+r.x[0]**2)/3:.4f}), delta_nu = {r.x[1]:.5f}: s12 = {o[0][0]:.4f}, s23 = {o[0][1]:.4f}, s13 = {o[0][2]:.5f}; z = ({o[1][0]:+.1f}, {o[1][1]:+.1f}, {o[1][2]:+.1f}), z_R = {o[2]:+.1f}")
print("   Profil: " + ", ".join(f"{a:.2f}: {c:.0f}" for a, c, _ in pb[::6]))
print(f"   Urteil H180b: {'TRAEGT' if r.fun < 9.2 else 'WIDERLEGT'} (Schwelle 9,2)")

print("\n== Bericht: eine Zahl x (delta_nu = pi/6 - x, kappa = tan x) bei freiem rho_nu ==")
for rho in (0.8, 0.9, 1.0, 1.1, 1.2):
    r = minimize(lambda p: chi2(rho, np.pi / 6 - p[0], np.tan(p[0])), [0.045], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10})
    print(f"   rho_nu = {rho:.2f}: x = {r.x[0]:.5f}, chi2 = {r.fun:.2f}")
