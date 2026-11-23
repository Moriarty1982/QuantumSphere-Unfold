"""k243 Teil B: Test H124 - rueckgekoppelte Kaskade mit eps = 3 (Attraktor Omega_M = beta^2) gegen DESI DR2 BAO.
Vorab-Notiz ../predictions/Vorab_Notiz_H124_Kaskaden_Attraktor_DESI_DR2.md (Commit 7b2b665).
Daten und Modellcode aus ../v4_10_0_r05/llm/k216_bruecke_desi_dr2.py (H97), relativ zum Repo eingebunden.
Aufruf: python3 k243_test_h124.py
"""
import importlib.util, io, contextlib
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import chi2

src = Path(__file__).resolve().parent.parent / 'v4_10_0_r05' / 'llm' / 'k216_bruecke_desi_dr2.py'
spec = importlib.util.spec_from_file_location('k216', src); k216 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()) as buf:      # k216 druckt beim Import seine H97-Ausgaben; hier unterdrueckt
    spec.loader.exec_module(k216)
b2 = k216.b2

# Gueltigkeit (wie H97)
res = minimize_scalar(lambda Om: k216.chi2_min(k216.E_lcdm(Om))[0], bounds=(0.2, 0.45), method='bounded', options={'xatol': 1e-6})
cL, hL = k216.chi2_min(k216.E_lcdm(res.x))
ok = abs(res.x - 0.2975) <= 0.003 and abs(hL - 101.54) <= 0.5
print(f'Kontrolle LCDM: Om = {res.x:.4f}, h r_d = {hL:.2f} Mpc, chi2 = {cL:.2f}; Gueltigkeit erfuellt: {ok}')

def best(eps, lo=None, hi=0.999):
    lo = b2 + 1e-6 if lo is None else lo
    grid = np.linspace(lo, hi, 80)
    cg = [k216.chi2_min(k216.E_kaskade(o, eps))[0] for o in grid]
    i = int(np.argmin(cg)); a, b = grid[max(i-1, 0)], grid[min(i+1, len(grid)-1)]
    r = minimize_scalar(lambda o: k216.chi2_min(k216.E_kaskade(o, eps))[0], bounds=(a, b), method='bounded', options={'xatol': 1e-6})
    c, h = k216.chi2_min(k216.E_kaskade(r.x, eps))
    return r.x, c, h

Om, c, h = best(3.0)
p = chi2.sf(c, 11)
print(f'H124 Kaskade eps=3, Om0 frei in (beta^2, 1): Om0 = {Om:.4f}, h r_d = {h:.2f}, chi2_min = {c:.2f}, p(11) = {p:.2e}'
      f' -> {"widerlegt" if c > 24.72 else "nicht ausgeschlossen"} (Schwelle 24.72)')
print(f'  Vergleich LCDM frei: chi2 = {cL:.2f}; Delta chi2 = {c - cL:.2f}')
print('Erkundung (nachtraeglich erlaubt): eps bei freiem Om0 (Om0 > eps b2/3, sonst Bahn nicht aus der Materie-Aera)')
for eps in (0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 3.0):
    lo = max(eps*b2/3 + 1e-6, 0.2)
    o, cc, _ = best(eps, lo=lo, hi=0.6)
    print(f'  eps = {eps:.1f}: Attraktor {eps*b2/3:.4f}, bestes Om0 = {o:.4f}, chi2 = {cc:.2f}, p(11) = {chi2.sf(cc, 11):.3g}')
