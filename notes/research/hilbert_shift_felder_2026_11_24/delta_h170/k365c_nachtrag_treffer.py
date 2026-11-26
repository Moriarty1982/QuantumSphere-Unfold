"""k365c (H170, nachtraeglich): Der Beinahe-Treffer aus H170e als Vorhersage gerechnet.
Kandidat: 2x = arcsin(beta) - arctan(beta) (bzw. tan 2x = ...). Vergleich mit m_mu/m_e (CODATA 2022: 206.7682827(46)), K = 2/3.
Aufruf: python3 k365c_nachtrag_treffer.py > k365c_out.txt
"""
import mpmath as mp
mp.mp.dps = 30
BETA = mp.mpf("0.5494056410"); DSTAR = mp.mpf("0.2222220470731"); DERR = mp.mpf("4e-10")
R_OBS = mp.mpf("206.7682827"); R_ERR = mp.mpf("0.0000046")
g = mp.asin(BETA) - mp.atan(BETA)


def ratio(d):
    m = sorted([(1 + mp.sqrt(2) * mp.cos(d + 2 * mp.pi * k / 3))**2 for k in range(3)])
    return m[1] / m[0], m[2] / m[1]


print("delta* =", mp.nstr(DSTAR, 13), "; m_mu/m_e dort:", mp.nstr(ratio(DSTAR)[0], 12))
for name, xx in (("2x = gd - arctan", g / 2), ("tan 2x = gd - arctan", mp.atan(g) / 2), ("tan x = (gd - arctan)/2", mp.atan(g / 2))):
    d = mp.pi / 12 - xx
    rr = ratio(d)
    print(f"{name:>24}: x = {mp.nstr(xx, 12)}, delta = {mp.nstr(d, 12)}, delta - delta* = {mp.nstr(d - DSTAR, 5)} ({mp.nstr((d - DSTAR) / DERR, 4)} sigma_delta), "
          f"m_mu/m_e = {mp.nstr(rr[0], 9)} ({mp.nstr((rr[0] - R_OBS) / R_ERR, 4)} sigma), m_tau/m_mu = {mp.nstr(rr[1], 8)}")
print("zum Vergleich delta = 2/9: delta - delta* =", mp.nstr(mp.mpf(2) / 9 - DSTAR, 5), "; m_mu/m_e =", mp.nstr(ratio(mp.mpf(2) / 9)[0], 10))
print("Schwelle 1e-4 (wie H167, H168) statt 1e-3: kein Treffer (naechster 6.9e-4).")
