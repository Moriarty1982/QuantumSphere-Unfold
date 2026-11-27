"""k427 (Test H214): Welches Massenschema gilt fuer x_lepton — Pol- oder laufende Massen?
Vorab-Notiz Vorab_H214_Massenschema.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k427_test_h214.py > k427_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import brentq

# --- Daten -----------------------------------------------------------------------------------------
POLE = np.array([0.51099895, 105.6583755, 1776.93]); POLE_E = np.array([1.5e-10, 2.3e-6, 0.09])
MZ = np.array([0.486570161, 102.7181359, 1746.24]); MZ_E = np.array([4.2e-8, 9.2e-6, 0.20])   # Xing-Zhang-Zhou 2008
DM21, S21, DM31, S31 = 7.537e-5, 0.097e-5, 2.511e-3, 0.0205e-3
ROBS = DM21 / DM31; SR = ROBS * np.hypot(S21 / DM21, S31 / DM31)
AINV0 = 137.035999


def K(m):
    return m.sum() / np.sqrt(m).sum() ** 2


def sigK(m, e):
    g = []
    for i in range(3):
        h = np.zeros(3); h[i] = e[i]
        g.append((K(m + h) - K(m - h)) / 2)
    return np.sqrt(sum(x * x for x in g))


def delta_amp(m):
    s = np.sqrt(m); best = None
    for p in itertools.permutations(range(3)):
        sp = s[list(p)]; mu = sp.mean()
        c = sum(sp[k] * np.exp(-2j * np.pi * k / 3) for k in range(3)) * 2 / 3 / mu
        a, d = abs(c), np.angle(c) % (2 * np.pi)
        if best is None or abs(d - 0.2222) < abs(best[1] - 0.2222):
            best = (a, d)
    return best


def xlep(m):
    return np.pi / 12 - delta_amp(m)[1]


def roots(d, a=np.sqrt(2)):
    return np.array([1 + a * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def R_NO(d):
    m = np.sort(roots(d) ** 2)
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


def x_nu_of_R(R):
    return np.pi / 6 - brentq(lambda d: R_NO(d) - R, np.pi / 12 + 1e-9, np.pi / 6)


XNU = x_nu_of_R(ROBS)
SXNU = abs(x_nu_of_R(ROBS - SR) - x_nu_of_R(ROBS + SR)) / 2


def ainv_running(mu, ainv_had_tau=1.2):
    """einschleifig: Elektron ab m_e, Myon ab m_mu, Hadronen pauschal (bei m_tau +ainv_had_tau abgezogen), Tau ab m_tau."""
    a = AINV0
    if mu > POLE[0]:
        a -= 2 / (3 * np.pi) * np.log(mu / POLE[0])
    if mu > POLE[1]:
        a -= 2 / (3 * np.pi) * np.log(mu / POLE[1])
    if mu >= POLE[2]:
        a -= ainv_had_tau
    return a


def common_scale(mu, ainv):
    """einschleifig Pol -> MS-bar an gemeinsamer Skala mu: M = mbar(mu) [1 + (alpha/pi)(1 + 3/4 ln(mu^2/M^2))]"""
    al = 1 / ainv
    return POLE / (1 + al / np.pi * (1 + 0.75 * np.log(mu ** 2 / POLE ** 2)))


def own_scale(had=1.2):
    out = []
    for M in POLE:
        al = 1 / ainv_running(M, had)
        out.append(M / (1 + al / np.pi))
    return np.array(out)


print("=" * 80)
print("H214 a (nicht blind)  Kriterium des Rahmens: K = 2/3 (a = sqrt2) innerhalb 2 sigma_K")
print("=" * 80)
schemes = {
    "Pol": (POLE, POLE_E),
    "laufend, gemeinsam M_Z (XZZ)": (MZ, MZ_E),
    "laufend, gemeinsam m_tau (1-Schl. QED)": (common_scale(POLE[2], ainv_running(POLE[2])), POLE_E),
    "laufend, gemeinsam 2 GeV (1-Schl. QED)": (common_scale(2000.0, ainv_running(2000.0)), POLE_E),
}
adm = {}
print(f"  {'Schema':42s} {'K':>12s} {'K-2/3':>11s} {'sigma_K':>9s} {'z':>9s}  {'a':>9s}  {'x_lepton':>9s}  zulaessig")
for nm, (m, e) in schemes.items():
    k = K(m); sk = sigK(m, e); z = (k - 2 / 3) / sk
    a, d = delta_amp(m); x = np.pi / 12 - d
    ok = abs(z) <= 2
    adm[nm] = (ok, x)
    print(f"  {nm:42s} {k:12.8f} {k-2/3:+11.2e} {sk:9.2e} {z:+9.1f}  {a:9.6f}  {x:9.6f}  {'JA' if ok else 'nein'}")

print("\n" + "=" * 80)
print("H214 b (blind)  laufend, je eigene Skala mbar(M) = M/(1 + alpha(M)/pi)")
print("=" * 80)
for had in (0.0, 1.2, 2.0):
    m = own_scale(had)
    k = K(m); sk = sigK(m, POLE_E); z = (k - 2 / 3) / sk
    x = xlep(m); dx = x - adm["Pol"][1]
    print(f"  Hadron-Anteil Delta(1/alpha)={had:3.1f}: alpha^-1(M_i) = {[round(ainv_running(M, had), 3) for M in POLE]}")
    print(f"     mbar = {np.round(m, 6)}; K = {k:.8f} (z = {z:+.2f}); x_lepton = {x:.7f}; Delta x vs Pol = {dx:+.2e} = {dx/SXNU:+.4f} sigma(x_nu)"
          f"  -> {'zulaessig' if abs(z) <= 2 else 'nicht zulaessig'}")
m_own = own_scale(1.2)
adm["laufend, je eigene Skala"] = (abs((K(m_own) - 2 / 3) / sigK(m_own, POLE_E)) <= 2, xlep(m_own))

print("\n" + "=" * 80)
print("H214 c (blind)  Rueckwaertssuche: welche Massenverhaeltnisse verlangt x = x_nu bei K = 2/3?")
print("=" * 80)


def ratios_at(x):
    m = np.sort(roots(np.pi / 12 - x) ** 2)
    return m[0] / m[1], m[1] / m[2]


r_lep = ratios_at(adm["Pol"][1]); r_nu = ratios_at(XNU)
print(f"  bei x_lepton(Pol)={adm['Pol'][1]:.6f}: m_e/m_mu = {r_lep[0]:.6e}, m_mu/m_tau = {r_lep[1]:.6f}"
      f"   (gemessen {POLE[0]/POLE[1]:.6e}, {POLE[1]/POLE[2]:.6f})")
print(f"  bei x_nu={XNU:.6f}:          m_e/m_mu = {r_nu[0]:.6e}, m_mu/m_tau = {r_nu[1]:.6f}")
need = (r_nu[0] / r_lep[0] - 1, r_nu[1] / r_lep[1] - 1)
print(f"  verlangte relative Aenderung: m_e/m_mu {need[0]:+.3%}, m_mu/m_tau {need[1]:+.3%}")
pole_r = (POLE[0] / POLE[1], POLE[1] / POLE[2])
maxshift = 0.0
for nm, (ok, x) in adm.items():
    if nm == "Pol" or not ok:
        continue
    m = m_own if nm.startswith("laufend, je") else schemes[nm][0]
    sh = (m[0] / m[1] / pole_r[0] - 1, m[1] / m[2] / pole_r[1] - 1)
    print(f"  zulaessiges Schema '{nm}': Verschiebung m_e/m_mu {sh[0]:+.4%}, m_mu/m_tau {sh[1]:+.4%}")
    maxshift = max(maxshift, abs(sh[0]), abs(sh[1]))
for nm in ("laufend, gemeinsam M_Z (XZZ)", "laufend, gemeinsam m_tau (1-Schl. QED)"):
    m = schemes[nm][0]
    sh = (m[0] / m[1] / pole_r[0] - 1, m[1] / m[2] / pole_r[1] - 1)
    print(f"  (nicht zulaessig) '{nm}': Verschiebung m_e/m_mu {sh[0]:+.3%}, m_mu/m_tau {sh[1]:+.3%}")
reqmin = min(abs(need[0]), abs(need[1]))
fac = reqmin / maxshift if maxshift > 0 else np.inf
print(f"  kleinste verlangte Aenderung / groesste zulaessige Verschiebung = {fac:.0f}")
print(f"  Kriterium c: {'kein zulaessiges Schema schliesst den Abstand' if fac > 10 else 'Schema koennte beitragen'}")

print("\n" + "=" * 80)
print("H214 d (blind)  Neutrino-Seite: Schemaabhaengigkeit von R (1-Schl. SM, nicht-universeller tau-Yukawa-Anteil)")
print("=" * 80)
v = 246.22; ytau = np.sqrt(2) * POLE[2] / 1000 / v; C = -1.5
U2 = np.array([0.24, 0.33, 0.43])            # |U_tau i|^2 (NuFIT, gerundet)
r = np.sort(roots(np.pi / 6 - XNU) ** 2)       # m_i ~ Wurzel^2 (Verhaeltnisse)
for lab, dt in (("ln(M_Z/1 GeV)", np.log(91.1876)), ("ln(M_Z/m_e)", np.log(91187.6 / 0.511)), ("ln(1 TeV/m_e)", np.log(1e6 / 0.511))):
    eps = 2 * C * ytau ** 2 * U2 * dt / (16 * np.pi ** 2)
    m2 = r * (1 + eps)
    R2 = (m2[1] ** 2 - m2[0] ** 2) / (m2[2] ** 2 - m2[0] ** 2)
    R1 = (r[1] ** 2 - r[0] ** 2) / (r[2] ** 2 - r[0] ** 2)
    dR = R2 - R1
    dxnu = x_nu_of_R(ROBS + dR) - XNU
    print(f"  Delta t = {lab:14s} ({dt:5.2f}): eps_i = {np.array2string(eps, precision=2)}; Delta R/R = {dR/R1:+.2e}; "
          f"Delta x_nu = {dxnu:+.2e} = {dxnu/SXNU:+.5f} sigma(x_nu)")
print(f"  y_tau = {ytau:.5f}; Kriterium d: |Delta x_nu| < 0,1 sigma -> R schemafest")

print("\n" + "=" * 80)
print("H214 Gesamturteil")
print("=" * 80)
allowed = [nm for nm, (ok, _) in adm.items() if ok]
spread = max(abs(adm[nm][1] - adm["Pol"][1]) for nm in allowed) / SXNU
print(f"  zulaessige Schemata: {allowed}")
print(f"  groesste x-Spreizung unter zulaessigen Schemata: {spread:.4f} sigma(x_nu)")
print(f"  Abstand x_nu - x_lepton(Pol) = {(XNU-adm['Pol'][1])/SXNU:.2f} sigma")
if not adm["Pol"][0]:
    print("  -> WIDERLEGT (Pol verfehlt K = 2/3)")
elif spread < 0.3 and fac > 10:
    print("  -> TRAEGT: Pol ist das Schema des Rahmens; M_Z-Lesart (H213c) unzulaessig; Abstand bleibt 1,78 sigma")
else:
    print("  -> TRAEGT TEILWEISE")
