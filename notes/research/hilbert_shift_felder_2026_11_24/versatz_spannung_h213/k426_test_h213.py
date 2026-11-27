"""k426 (Test H213): Ist der "4,2 sigma"-Abstand zwischen Neutrino-Versatz x_nu und Lepton-Versatz x_lepton echt?
Vorab-Notiz Vorab_H213_Versatz_Spannung.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k426_test_h213.py > k426_out.txt
"""
import numpy as np
from scipy.optimize import brentq, fsolve
from scipy.stats import norm

# Daten wie H168/H99b (k363)
DM21, S21, DM31, S31 = 7.537e-5, 0.097e-5, 2.511e-3, 0.0205e-3
ROBS = DM21 / DM31
SR = ROBS * np.hypot(S21 / DM21, S31 / DM31)
# geladene Leptonen, Polmassen (PDG, wie k370)
POLE = np.array([0.51099895, 105.6583755, 1776.93]); POLE_E = np.array([0.00000000015, 0.0000023, 0.09])
# laufende MS-bar-Massen bei M_Z (Xing-Zhang-Zhou 2008, PRD 77, 113016), Fehler dort
MZ = np.array([0.486570161, 102.7181359, 1746.24]); MZ_E = np.array([0.000000042, 0.0000092, 0.20])
SX_H207 = 0.00091   # in H207 benutzter Nenner (Fit-Unsicherheit H175)
X_LEP_REPO, X_R_REPO = 0.0395773407, 0.043359


def roots(d, a=np.sqrt(2)):
    return np.array([1 + a * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def R_NO(d):
    m = np.sort(roots(d) ** 2)
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


def x_nu_of_R(R):
    dn = brentq(lambda d: R_NO(d) - R, np.pi / 12 + 1e-9, np.pi / 6)
    return np.pi / 6 - dn


def delta_from_masses(m):
    """sqrt m_k = mu (1 + a cos(delta + 2 pi k/3)), k=0,1,2 in Brannen-Zuordnung; eindeutig.
    Fourier: s_k = sqrt m_k; mu = mean(s); a e^{i delta} aus der ersten Harmonischen."""
    s = np.sqrt(m)
    # Brannen-Zuordnung: k=0 tau? -> wir suchen die Permutation, die delta im Bereich (0, 2pi/3) nahe 2/9 gibt
    best = None
    import itertools
    for p in itertools.permutations(range(3)):
        sp = s[list(p)]
        mu = sp.mean()
        c = sum(sp[k] * np.exp(-2j * np.pi * k / 3) for k in range(3)) * 2 / 3 / mu   # = a e^{i delta}
        a, d = abs(c), np.angle(c) % (2 * np.pi)
        if best is None or abs(d - 0.2222) < abs(best[2] - 0.2222):
            best = (p, a, d, mu)
    return best


def K(m):
    return m.sum() / np.sqrt(m).sum() ** 2


print("=" * 78)
print("H213 a (nicht blind)  richtige Fehler fuer x_nu und x_lepton")
print("=" * 78)
xnu = x_nu_of_R(ROBS)
xlo, xhi = x_nu_of_R(ROBS + SR), x_nu_of_R(ROBS - SR)
snu = abs(xhi - xlo) / 2
p, a_p, d_p, _ = delta_from_masses(POLE)
xlep = np.pi / 12 - d_p
# sigma(x_lepton) aus Massenfehlern (numerische Ableitung)
g = []
for i in range(3):
    h = np.zeros(3); h[i] = POLE_E[i] if POLE_E[i] > 0 else 1e-12
    g.append((delta_from_masses(POLE + h)[2] - delta_from_masses(POLE - h)[2]) / 2)
slep = np.sqrt(sum(gi ** 2 for gi in g))
print(f"  R_obs = {ROBS:.6f} +- {SR:.6f}")
print(f"  x_nu      = {xnu:.6f} +- {snu:.6f}   (Repo X_R = {X_R_REPO})")
print(f"  Polmassen: K = {K(POLE):.8f}, a = {a_p:.7f} (sqrt2 = {np.sqrt(2):.7f}), delta = {d_p:.10f}")
print(f"  x_lepton  = {xlep:.8f} +- {slep:.8f}   (Repo X_LEP = {X_LEP_REPO})")
dx = xnu - xlep
Ta = abs(dx) / np.hypot(snu, slep)
print(f"  Differenz x_nu - x_lepton = {dx:.6f}")
print(f"  mit H207-Nenner 0,00091:      {abs(dx)/SX_H207:.2f} sigma  (so in H207 berichtet)")
print(f"  mit richtigem Nenner:         T_a = {Ta:.2f} sigma   (sigma_nu dominiert: {snu:.5f} vs {slep:.2e})")
print(f"  Kriterium a: T_a < 2 -> {'JA, 4,2 sigma war ein Nenner-Fehler' if Ta < 2 else ('echter Abstand' if Ta >= 3 else 'zwischen 2 und 3')}")

print("\n" + "=" * 78)
print("H213 b (blind)  Monte Carlo der Fehlerfortpflanzung (10^6 Ziehungen)")
print("=" * 78)
rng = np.random.default_rng(213)
N = 1_000_000
d21 = rng.normal(DM21, S21, N); d31 = rng.normal(DM31, S31, N)
Rs = d21 / d31
# x_nu(R) monoton: tabellieren und interpolieren
Rgrid = np.linspace(Rs.min() * 0.999, Rs.max() * 1.001, 4001)
xgrid = np.array([x_nu_of_R(r) for r in Rgrid])
xs = np.interp(Rs, Rgrid, xgrid)
q16, q50, q84 = np.percentile(xs, [16, 50, 84])
frac = np.mean(xs <= xlep)
Tb = norm.isf(frac) if frac > 0 else np.inf
print(f"  x_nu: Median {q50:.6f}, 16 % {q16:.6f}, 84 % {q84:.6f}  (-{q50-q16:.6f} / +{q84-q50:.6f})")
print(f"  Anteil x_nu <= x_lepton: {frac:.5f}  -> einseitig {Tb:.2f} sigma")
print(f"  Differenz MC - linear: {Tb - Ta:+.2f} sigma -> {'MC-Zahl gilt' if abs(Tb-Ta) > 0.3 else 'linear ausreichend'}")

print("\n" + "=" * 78)
print("H213 c (blind)  Massenschema: laufende Massen bei M_Z statt Polmassen")
print("=" * 78)
pz, a_z, d_z, _ = delta_from_masses(MZ)
xlep_z = np.pi / 12 - d_z
gz = []
for i in range(3):
    h = np.zeros(3); h[i] = MZ_E[i]
    gz.append((delta_from_masses(MZ + h)[2] - delta_from_masses(MZ - h)[2]) / 2)
slep_z = np.sqrt(sum(gi ** 2 for gi in gz))
dxs = xlep_z - xlep
print(f"  M_Z-Massen: K = {K(MZ):.8f} (Pol {K(POLE):.8f}), a = {a_z:.7f}, delta = {d_z:.10f}")
print(f"  x_lepton(M_Z) = {xlep_z:.6f} +- {slep_z:.6f}   Verschiebung Delta x_Schema = {dxs:+.6f} = {dxs/snu:+.2f} sigma(x_nu)")
Tc = abs(xnu - xlep_z) / np.hypot(snu, slep_z)
print(f"  Abstand x_nu - x_lepton(M_Z): {xnu - xlep_z:+.6f} = {Tc:.2f} sigma")
if Tc <= 1:
    vc = "Schema erklaert den Abstand"
elif abs(dxs) < 0.3 * snu:
    vc = "Schema unerheblich"
else:
    vc = "teilweise"
print(f"  Kriterium c: {vc}")
# Zwischenstufe: Richtung der Wirkung pro Masse
for i, nm in enumerate(("m_e", "m_mu", "m_tau")):
    mm = POLE.copy(); mm[i] = MZ[i]
    print(f"    nur {nm} auf M_Z: x_lepton = {np.pi/12 - delta_from_masses(mm)[2]:.6f}")

print("\n" + "=" * 78)
print("H213 d (blind)  weitere Zweige der Brannen-Form (K=2/3), normale und invertierte Ordnung")
print("=" * 78)
ds = np.linspace(0, 2 * np.pi / 3, 200001)


def spectra(d):
    m = roots(d) ** 2          # Massen ~ Wurzel^2 (Vorzeichen der Wurzel egal)
    return np.sort(m)


def R_IO(d):
    m = spectra(d)             # IO: m3 leichtest; m1 < m2 nahe beieinander oben
    m3, m1, m2 = m[0], m[1], m[2]
    return (m2 ** 2 - m1 ** 2) / abs(m2 ** 2 - m3 ** 2)


for lab, Rf, Rt, St in (("NO", R_NO, ROBS, SR),
                         ("IO", R_IO, DM21 / 2.498e-3, (DM21 / 2.498e-3) * np.hypot(S21 / DM21, 0.025e-3 / 2.498e-3))):
    vals = np.array([Rf(d) for d in ds[::50]])
    dd = ds[::50]
    sols = []
    for i in range(len(dd) - 1):
        f1, f2 = vals[i] - Rt, vals[i + 1] - Rt
        if np.sign(f1) != np.sign(f2):
            r = brentq(lambda d: Rf(d) - Rt, dd[i], dd[i + 1])
            sols.append(r)
    print(f"  {lab}: R_Ziel = {Rt:.6f}; Loesungen delta_nu (in [0, 2pi/3)): {np.round(sols, 6)}")
    for s in sols:
        # Versatz relativ zum naechsten Minimum der c=0-Familie {0, pi/6, pi/3, ...}: x = Minimum - delta
        cands = {"0": 0.0, "pi/6": np.pi / 6, "pi/3": np.pi / 3, "pi/2": np.pi / 2, "2pi/3": 2 * np.pi / 3}
        nm, base = min(cands.items(), key=lambda kv: abs(kv[1] - s))
        xx = base - s
        print(f"     delta_nu = {s:.6f}: naechstes c=0-Minimum {nm}, Versatz x = {xx:+.6f}; |x| - x_lepton = {abs(xx)-xlep:+.6f}"
              f"  ({(abs(xx)-xlep)/snu:+.2f} sigma_nu)")

print("\n" + "=" * 78)
print("H213 Gesamturteil")
print("=" * 78)
T = Tb if abs(Tb - Ta) > 0.3 else Ta
if T < 2:
    verdict = "TRAEGT: der Abstand ist nicht signifikant (4,2 sigma war der falsche Nenner)"
elif T < 3:
    verdict = "TRAEGT TEILWEISE: 2 <= T < 3"
else:
    verdict = "WIDERLEGT: echter Abstand"
print(f"  T (massgeblich) = {T:.2f} sigma -> {verdict}")
