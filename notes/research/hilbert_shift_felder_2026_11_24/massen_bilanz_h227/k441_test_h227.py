"""k441 (Test H227): Bilanz der Leptonenmassen, festgeschriebene Neutrino-Vorhersagen, Skalenverhaeltnis mu_nu/mu_e.
Vorab-Notiz Vorab_H227_Massen_Bilanz.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k441_test_h227.py > k441_out.txt
"""
import numpy as np
from scipy.optimize import brentq

A = np.sqrt(2)
ME, MMU, MTAU, STAU = 0.51099895, 105.6583755, 1776.93, 0.09          # MeV
DM21, S21, DM31, S31 = 7.537e-5, 0.097e-5, 2.511e-3, 0.0205e-3          # eV^2
ROBS = DM21 / DM31; SR = ROBS * np.hypot(S21 / DM21, S31 / DM31)
X = 0.0395773407                                                         # unter J (H158d)
S12, S13 = 0.307, 0.0220
BS, GL, GM = 0.5494056410, 1.8646997646, 0.2375329580
EPS = np.arctanh(BS)
V = 246.22e9; MPL = 1.221e28; MPLR = 2.435e27                             # eV


def r(d):
    return np.array([1 + A * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def masses_rel(d):
    rr = r(d)
    idx = np.argsort(rr ** 2)
    return (rr ** 2)[idx], rr[idx]


print("=" * 88)
print("H227 1  Bilanz")
print("=" * 88)
# (i) aus m_e, m_mu allein (a = sqrt2): delta und mu, dann m_tau vorhergesagt
def ratio_err(d):
    m, _ = masses_rel(d)
    return m[0] / m[1] - ME / MMU
d_e = brentq(ratio_err, 0.15, 0.26)
m_rel, r_rel = masses_rel(d_e)
mu2 = ME / m_rel[0]
mtau_pred = mu2 * m_rel[2]
x_emu = np.pi / 12 - d_e
print(f"  (i) aus m_e, m_mu: delta = {d_e:.10f}, x = pi/12 - delta = {x_emu:.10f} (unter J aus m_tau: {X:.10f}, Differenz {x_emu-X:+.1e})")
print(f"      m_tau,pred = {mtau_pred:.3f} MeV, gemessen {MTAU} +- {STAU} -> {(mtau_pred-MTAU)/STAU:+.2f} sigma (Koide-Relation)")
mu_e = np.sqrt(mu2)                        # MeV^(1/2)
print(f"      mu_e^2 = M_e = {mu2:.6f} MeV  (Kontrolle Sum m / 6 = {(ME+MMU+MTAU)/6:.6f} MeV)")
# (ii) R aus phi
d_n = np.pi / 6 - X
mn_rel, rn_rel = masses_rel(d_n)
R = (mn_rel[1] ** 2 - mn_rel[0] ** 2) / (mn_rel[2] ** 2 - mn_rel[0] ** 2)
print(f"  (ii) Neutrinos delta = pi/6 - x = {d_n:.7f}: Wurzeln (aufsteigend nach Masse) {np.round(rn_rel, 6)};"
      f" R_pred = {R:.6f}, gemessen {ROBS:.6f} +- {SR:.6f} -> {(R-ROBS)/SR:+.2f} sigma")
print("  Zaehlung: 6 Massen, 3 Eingaben (phi, mu_e, mu_nu) -> 3 Vorhersagen: m_tau (Koide), R, absolute Neutrinoskala (Sigma m, m_beta, m_bb)")

print("\n" + "=" * 88)
print("H227 2  festgeschriebene Neutrino-Vorhersagen (normale Ordnung)")
print("=" * 88)
def nu_pred(x, dm31=DM31, dm21=None):
    mr, rr = masses_rel(np.pi / 6 - x)
    if dm21 is None:
        mu4 = dm31 / (mr[2] ** 2 - mr[0] ** 2)
    else:
        mu4 = dm21 / (mr[1] ** 2 - mr[0] ** 2)
    M = np.sqrt(mu4)
    return M * mr, rr, M
c12, s12, c13, s13 = np.sqrt(1 - S12), np.sqrt(S12), np.sqrt(1 - S13), np.sqrt(S13)
U2 = np.array([c12 ** 2 * c13 ** 2, s12 ** 2 * c13 ** 2, s13 ** 2])
def obs(m, rr):
    mb = np.sqrt(np.sum(U2 * m ** 2))
    t = U2 * m
    mbb_max = t.sum(); mbb_min = max(0.0, 2 * t.max() - t.sum())
    mbb_sign = abs(np.sum(np.sign(rr) * t))
    return mb, mbb_min, mbb_max, mbb_sign
m, rr, M_nu = nu_pred(X)
mb, lo, hi, sg = obs(m, rr)
print(f"  Hauptfall (mu_nu aus Delta m^2_31): m = {np.round(m*1e3, 4)} meV, Sigma m = {m.sum()*1e3:.3f} meV, M_nu = mu_nu^2 = {M_nu*1e3:.4f} meV")
print(f"     Delta m^2_21,pred = {(m[1]**2-m[0]**2):.4e} eV^2 (gemessen {DM21:.4e} +- {S21:.1e})")
print(f"     m_beta = {mb*1e3:.3f} meV; m_bb in [{lo*1e3:.3f}, {hi*1e3:.3f}] meV (Majorana-Phasen frei); Brannen-Vorzeichen (Lesart): {sg*1e3:.3f} meV")
# Fehler: Delta m^2_31 und x
rng = np.random.default_rng(227); samp = []
for _ in range(20000):
    mm, rrr, _ = nu_pred(X + rng.normal(0, 7.8e-7), dm31=rng.normal(DM31, S31))
    samp.append((mm.sum(), *mm, *obs(mm, rrr)))
samp = np.array(samp)
names = ["Sigma m", "m1", "m2", "m3", "m_beta", "m_bb,min", "m_bb,max", "m_bb,Vorz."]
for i, nm in enumerate(names):
    print(f"     {nm:10s} = {np.mean(samp[:, i])*1e3:.3f} +- {np.std(samp[:, i])*1e3:.3f} meV")
m2_, rr2, M2 = nu_pred(X, dm21=DM21)
print(f"  Kontrolle (mu_nu aus Delta m^2_21): m = {np.round(m2_*1e3, 4)} meV, Sigma m = {m2_.sum()*1e3:.3f} meV")
ok2 = mb < 0.45 and m.sum() < 0.0642 and hi < 0.028
print(f"  Schranken: m_beta {mb:.4f} < 0,45 eV: {mb < 0.45}; Sigma m {m.sum():.4f} < 0,0642 eV: {m.sum() < 0.0642}"
      f" (Abstand zur Schranke {(0.0642-m.sum())/np.std(samp[:,0]):.0f} Fehlerbreiten); m_bb,max {hi:.4f} < 0,028 eV: {hi < 0.028}")
print(f"  Kriterium 2 (verträglich): {ok2}")

print("\n" + "=" * 88)
print("H227 3  Skalenverhaeltnis rho = M_nu/M_e (Erkundung, nicht blind)")
print("=" * 88)
M_e = mu2 * 1e6        # eV
rho = M_nu / M_e
print(f"  M_e = {M_e:.6e} eV, M_nu = {M_nu:.6e} eV, rho = {rho:.6e}, mu_nu/mu_e = {np.sqrt(rho):.6e}")
hits = 0
for nm, b in (("beta_sym", BS), ("gamma_M", GM), ("1/gamma_L", 1 / GL), ("exp(-2 eps)", np.exp(-2 * EPS))):
    n = np.log(rho) / np.log(b)
    h = abs(n - round(n)) < 0.05
    hits += h
    print(f"  rho = {nm}^n: n = {n:.4f} -> naechste ganze Zahl {round(n)}, Abstand {abs(n-round(n)):.3f}: {'Treffer' if h else 'kein Treffer'}")
print(f"  Zufallserwartung (a): 4 x 0,1 = 0,4; Treffer: {hits}")
MX1 = M_e ** 2 / M_nu; MX2 = V ** 2 / M_nu
for lab, val in (("M_e^2/M_nu", MX1), ("v^2/M_nu", MX2)):
    best = min(((abs(np.log(val / s)), sn, s) for sn, s in (("v", V), ("M_Pl", MPL), ("M_Pl,red", MPLR))))
    h = best[0] < np.log(1.1)
    hits += h
    print(f"  {lab} = {val:.4e} eV = {val/1e9:.4e} GeV; naechste Liste {best[1]} ({best[2]/1e9:.3e} GeV), Faktor {np.exp(best[0]):.2e}: {'Treffer' if h else 'kein Treffer'}")

print("\n" + "=" * 88)
print("H227 Gesamturteil")
print("=" * 88)
v = "WIDERLEGT" if not ok2 else ("TRAEGT" if hits > 0 else "TRAEGT TEILWEISE")
print(f"  Kriterium 2: {ok2}; Treffer Teil 3: {hits} -> {v}")
