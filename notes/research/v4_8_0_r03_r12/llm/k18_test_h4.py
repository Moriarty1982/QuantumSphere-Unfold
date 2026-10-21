"""k18: Test der Vorab-Notiz H4 (Commit 00d297e): TM1 gegen TM2, 1:1. NuFIT 6.0 IC24+SK, NO."""
import numpy as np
from scipy.optimize import minimize

OBS = {"s12": (0.308, 0.012, 0.011), "s13": (0.02215, 0.00056, 0.00058),
       "s23": (0.470, 0.017, 0.013), "d": (212.0, 26.0, 41.0)}  # Wert, +sigma, -sigma

def pull(name, x):
    v, up, lo = OBS[name]
    if name == "d":
        diff = (x - v + 180) % 360 - 180
    else:
        diff = x - v
    return diff/(up if diff > 0 else lo)

def model(pattern, s13, s23):
    c13 = 1 - s13; t13 = np.sqrt(s13); S23, C23 = np.sqrt(s23), np.sqrt(1 - s23)
    if pattern == "TM1":
        s12 = 1 - 2/(3*c13)
        S12, C12 = np.sqrt(s12), np.sqrt(1 - s12)
        cosd = (1/6 - s12*(1 - s23) - (1 - s12)*s23*s13)/(2*S12*C12*C23*S23*t13)
    else:
        s12 = 1/(3*c13)
        S12, C12 = np.sqrt(s12), np.sqrt(1 - s12)
        cosd = -(1/3 - (1 - s12)*(1 - s23) - s12*s23*s13)/(2*S12*C12*C23*S23*t13)
    return s12, cosd

def chi2(pattern, p, parts=False):
    s13, s23 = p
    s12, cosd = model(pattern, s13, s23)
    if not (-1 <= cosd <= 1):
        return 1e6
    best = None
    for d in (np.degrees(np.arccos(cosd)), 360 - np.degrees(np.arccos(cosd))):
        c = {k: pull(k, x)**2 for k, x in (("s12", s12), ("s13", s13), ("s23", s23), ("d", d))}
        if best is None or sum(c.values()) < sum(best[0].values()):
            best = (c, d, s12)
    return best if parts else sum(best[0].values())

res = {}
for pat in ("TM1", "TM2"):
    fits = [minimize(lambda p: chi2(pat, p), x0, method="Nelder-Mead", options=dict(xatol=1e-9, fatol=1e-10))
            for x0 in ([0.02215, 0.47], [0.02215, 0.55], [0.0222, 0.43], [0.0222, 0.6])]
    f = min(fits, key=lambda r: r.fun)
    c, d, s12 = chi2(pat, f.x, parts=True)
    res[pat] = f.fun
    print(f"{pat}: chi2_min = {f.fun:.3f}  (s12: {c['s12']:.2f}, s13: {c['s13']:.2f}, s23: {c['s23']:.2f}, dCP: {c['d']:.2f})"
          f"  sin2t12 = {s12:.4f}, sin2t13 = {f.x[0]:.5f}, sin2t23 = {f.x[1]:.3f}, dCP = {d:.0f} Grad")
    # Vorhersagebaender: dCP ueber sin2t23 im 1-sigma-Bereich (beide Zweige)
    band = []
    for S in np.linspace(0.457, 0.487, 31):
        s12m, cd = model(pat, 0.02215, S)
        if -1 <= cd <= 1:
            band.append(np.degrees(np.arccos(cd)))
    if band:
        print(f"   Vorhersage dCP fuer sin2t23 in [0.457, 0.487]: {min(band):.0f}-{max(band):.0f} oder "
              f"{360-max(band):.0f}-{360-min(band):.0f} Grad;  sin2t12 = {model(pat, 0.02215, 0.47)[0]:.4f} (JUNO)")
    else:
        print("   keine reelle dCP-Loesung im 1-sigma-Bereich von sin2t23")
D = res["TM2"] - res["TM1"]
print(f"\nDelta chi2 = chi2(TM2) - chi2(TM1) = {D:.3f};  Bayes-Faktor TM1:TM2 ~ {np.exp(D/2):.1f}:1")
