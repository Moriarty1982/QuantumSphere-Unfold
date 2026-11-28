"""k443 (Test H229): J bei Ordnung 6 lockern -- legt das volle Quadrat N^2 Zweig und Winkel phi fest?
Vorab-Notiz Vorab_H229_J_Ordnung6.md (vor der Rechnung committet). Modell wie H225 (k439) plus w*g(delta),
g = -2 sqrt2 cos 3delta + cos 6delta (delta-Teil von N^2 bei K = 2/3, normiert auf 2 r^6).
Aufruf aus diesem Ordner: python3 k443_test_h229.py > k443_out.txt
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq

DSTAR = 0.2222220470731
X = np.pi / 12 - DSTAR
XNU, SXNU = 0.04336, 0.00213
S2 = np.sqrt(2.0)
SECT = {"Im": (+1.0, np.pi / 4), "Re": (-1.0, 0.0)}
DG = np.linspace(0, 2 * np.pi, 6001)


def g(d):
    return -2 * S2 * np.cos(3 * d) + np.cos(6 * d)


def V(d, sec, phi, w):
    a, c = SECT[sec]
    return -a * np.cos(2 * (d - c - phi)) + w * g(d)


def argmin_d(sec, phi, w):
    f = lambda d: V(d, sec, phi, w)
    v = f(DG)
    best = (np.inf, None)
    for k in np.argsort(v)[:16]:
        res = minimize_scalar(f, bounds=(DG[max(k - 1, 0)], DG[min(k + 1, len(DG) - 1)]), method="bounded",
                              options={"xatol": 1e-13})
        if res.fun < best[0] - 1e-14:
            best = (res.fun, res.x)
    return best


def branch_ok(sec, phi, w):
    """Liegt das globale Minimum auf dem Datenzweig (modulo 2pi/3 und Konjugation delta->-delta)?"""
    e, d = argmin_d(sec, phi, w)
    target = (np.pi / 12 - phi) if sec == "Im" else (np.pi / 6 - phi)
    # Spektralklasse: delta ~ delta + 2pi/3 ~ -delta
    cands = [s * d + 2 * np.pi * k / 3 for s in (1, -1) for k in range(-3, 4)]
    dist = min(abs(c - target) for c in cands)
    # Abstand zum anderen Zweig (delta + pi/3)
    return dist, d, e


print("=" * 92)
print("H229 (k443)  J bei Ordnung 6 gelockert: V_s = -a_s cos2(delta - chi_s - phi) + w g(delta)")
print("             g = -2 sqrt2 cos 3delta + cos 6delta   (volles N^2 bei K = 2/3)")
print("=" * 92)

# ---------------- a ----------------
print("\nTeil a (nicht blind)  Zweigwahl: Abstand des globalen Minimums vom Datenzweig (Spektralklasse)")
WS = [1e-4, 1e-3, 1e-2, 0.03, 0.1, 0.3, 1.0, 3.0]
PHIS = np.linspace(0.01, 0.06, 11)
okw = []
for w in WS:
    worst = {"Im": 0.0, "Re": 0.0}
    for p in PHIS:
        for sec in ("Im", "Re"):
            dist, d, e = branch_ok(sec, p, w)
            worst[sec] = max(worst[sec], dist)
    # "auf dem Zweig" = Abstand klein gegen pi/6 (Zweige liegen pi/3 auseinander); Verschiebung durch w wird mitberichtet
    ok = worst["Im"] < np.pi / 12 and worst["Re"] < np.pi / 12
    okw.append((w, ok))
    print(f"  w = {w:8.4g}: groesster Abstand Im {worst['Im']:.3e}, Re {worst['Re']:.3e}  -> Datenzweig in beiden: {ok}")

# ---------------- b ----------------
print("\nTeil b (blind)  Winkel als Modulus: globale Minima von E(phi; w) = e_Im + e_Re ueber phi in [0, pi/3)")


def E(phi, w):
    return argmin_d("Im", phi, w)[0] + argmin_d("Re", phi, w)[0]


def minima_E(w, n=481):
    ph = np.linspace(0, np.pi / 3, n, endpoint=False)
    e = np.array([E(p, w) for p in ph])
    out = []
    for i in range(n):
        if e[i] <= e[i - 1] and e[i] <= e[(i + 1) % n]:
            res = minimize_scalar(lambda p: E(p, w), bounds=(ph[i] - np.pi / 3 / n, ph[i] + np.pi / 3 / n),
                                  method="bounded", options={"xatol": 1e-11})
            out.append((res.fun, res.x % (np.pi / 3)))
    out.sort()
    emin = out[0][0]
    glob = sorted({round(p, 9) for v, p in out if v < emin + 1e-10})
    return glob, out


def rel_to_x(ps):
    return min(min(abs(p - X), abs((np.pi / 4 - p) - X)) for p in ps) / X  # Paar phi*, pi/4 - phi* zulaessig


best_b = (np.inf, None)
for w in WS:
    glob, allm = minima_E(w)
    r = rel_to_x(glob)
    best_b = min(best_b, (r, w))
    print(f"  w = {w:8.4g}: globale Minima {[f'{p:.6f}' for p in glob]}; lokale {[round(p, 5) for v, p in allm]};"
          f" naechstes zu x (mit Paar pi/4 - phi): {r*100:.1f} %")
print("  feine Abtastung w in [1e-4, 10] (60 Werte, log):")
fine = []
for w in np.logspace(-4, 1, 60):
    glob, allm = minima_E(w, n=241)
    fine.append((w, glob, rel_to_x(glob)))
rmin = min(fine, key=lambda t: t[2])
wl = sorted({tuple(round(p, 4) for p in gl) for w, gl, r in fine})
print(f"  vorkommende Lagen der globalen Minima (gerundet): {wl}")
print(f"  bester Wert: w = {rmin[0]:.4g}, Minima {rmin[1]}, Abstand zu x {rmin[2]*100:.1f} %")
hit_b_nat = min(r for w, gl, r in fine if w < 2e-4) < 0.01 or rel_to_x(minima_E(1.0)[0]) < 0.01
hit_b_fit = rmin[2] < 0.01
print(f"  Treffer natuerlich (w->0+ oder w=1): {hit_b_nat};  Treffer mit angepasstem w: {hit_b_fit}")

# ---------------- c ----------------
print("\nTeil c (blind)  ohne Drehung (phi = 0): w aus dem Im-Sektor, Vorhersage des Re-Versatzes")


def delta_min(sec, w, near):
    f = lambda d: V(d, sec, 0.0, w)
    res = minimize_scalar(f, bounds=(near - 0.4, near + 0.4), method="bounded", options={"xatol": 1e-14})
    return res.x


# Datenzweige als Minima der Sektorpotentiale (Spektralklasse): Im 5pi/4 + phi ~ pi/12 - phi (4pi/3 - delta),
# Re pi/2 + phi ~ pi/6 - phi (2pi/3 - delta). Versatz also delta_min - 5pi/4 bzw. delta_min - pi/2.
# (Korrigiert vor der Auswertung: die erste Fassung suchte direkt bei pi/12 bzw. pi/6, wo das Potential kein Minimum hat.)
def off_im(w):
    return delta_min("Im", w, 5 * np.pi / 4) - 5 * np.pi / 4


def off_re(w):
    return delta_min("Re", w, np.pi / 2) - np.pi / 2


ws = np.logspace(-5, 1, 400)
oi = np.array([off_im(w) for w in ws])
orr = np.array([off_re(w) for w in ws])
print(f"  Im-Versatz bei phi=0 laeuft von {oi[0]:.3e} bis {oi[-1]:.3e}; Re-Versatz von {orr[0]:.3e} bis {orr[-1]:.3e}")
sgn = np.sign(oi - X)
idx = np.nonzero(sgn[:-1] * sgn[1:] < 0)[0]
hit_c = False
if len(idx) == 0:
    print("  kein w gibt den Im-Versatz x")
for i in idx:
    wst = brentq(lambda w: off_im(w) - X, ws[i], ws[i + 1], xtol=1e-15)
    # globales Minimum pruefen
    dI = argmin_d("Im", 0.0, wst)
    dR = argmin_d("Re", 0.0, wst)
    xr = off_re(wst)
    z = (xr - XNU) / SXNU
    hit_c |= abs(z) <= 2
    print(f"  w* = {wst:.8f}: Im-Versatz {off_im(wst):.10f} (Ziel {X:.10f}); globales Minimum Im bei delta = {dI[1]:.6f}"
          f" (lokal gesucht {5*np.pi/4 + X:.6f} = Klasse von pi/12 - x); Re: x_nu^pred = {xr:.6f}, Abstand {z:+.1f} sigma;"
          f" globales Re-Minimum bei {dR[1]:.6f} (Daten pi/2 + x_nu = {np.pi/2 + XNU:.6f})")

print("\n" + "=" * 92)
if hit_b_nat:
    v = "TRAEGT"
elif hit_b_fit or hit_c:
    v = "TRAEGT TEILWEISE"
else:
    v = "WIDERLEGT"
print(f"H229 Gesamturteil: {v}   (b natuerlich {hit_b_nat}, b angepasst {hit_b_fit}, c {hit_c})")
