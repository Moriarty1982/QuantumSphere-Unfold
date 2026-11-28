"""k434 (Test H221): Trennt der neutrale Sektor (c = 0) den skalenfreien Weg K (Konjugationsterm) und den Weg S (Ordnung 6, Skala)?
Vorab-Notiz Vorab_H221_Skala_zwei_Sektoren.md (vor der Rechnung committet).
Modell wie H167/k362c: V(delta) = alpha cos 2d - alphap cos 2(d - chi) + q cos 3d, K = 2/3 fest, alphap = +1 im geladenen Sektor.
Aufruf aus diesem Ordner: python3 k434_test_h221.py > k434_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import minimize_scalar, fsolve

DSTAR = 0.2222220470731                 # Ziel geladen (Postulat J), H166
X_LEP = np.pi / 12 - DSTAR              # 0.0395773
X_NU, SX_NU = 0.043359, 0.002128        # H213
RHO_K = 0.07932041                      # H167: alpha/alphap fuer delta* (Weg K)
Q_S = -0.08524791                       # H167: q/alphap fuer delta* (Weg S)
GRID = np.linspace(0, 2 * np.pi, 20001)


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def V(d, alpha, alphap, chi, q):
    return alpha * np.cos(2 * d) - alphap * np.cos(2 * (d - chi)) + q * np.cos(3 * d)


def global_min(alpha, alphap, chi, q):
    """alle lokalen Minima auf dem Gitter suchen, jedes mit Brent nachschaerfen; zurueck: globales (gefaltet) und alle
    (gefaltet) innerhalb 1e-12 des globalen Werts (entartete Zweige)."""
    f = lambda d: V(d, alpha, alphap, chi, q)
    v = f(GRID)
    idx = np.where((v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
    mins = []
    for j in idx:
        r = minimize_scalar(f, bracket=(GRID[j - 1], GRID[j], GRID[j + 1]), tol=1e-15)
        mins.append((r.fun, r.x))
    vmin = min(m[0] for m in mins)
    degen = []
    for val, x in sorted(mins):
        if val < vmin + 1e-12:
            fx = fold(x)
            if all(abs(fx - o) > 1e-7 for o in degen):
                degen.append(fx)
    gx = min(mins)[1]
    return fold(gx), sorted(degen)


def R_NO(d):
    m = np.sort(np.array([1 + np.sqrt(2) * np.cos(d + 2 * np.pi * k / 3) for k in range(3)]) ** 2)
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


ROBS = 0.030016; SR = 0.000457

print("=" * 82)
print("Kontrolle: geladener Sektor (c = 1, chi = pi/4, alphap = +1) reproduziert delta*")
print("=" * 82)
for lab, a, q in (("Weg K: alpha=+rho", RHO_K, 0.0), ("Weg K: alpha=-rho", -RHO_K, 0.0), ("Weg S: q=Q_S", 0.0, Q_S)):
    d, alls = global_min(a, 1.0, np.pi / 4, q)
    print(f"  {lab:20s}: Minimum gefaltet {d:.10f}  (delta* = {DSTAR:.10f}, Diff {d-DSTAR:+.1e});  entartet: {np.round(alls, 6)}")

print("\n" + "=" * 82)
print("Neutraler Sektor (c = 0, chi = 0): alphap_nu = -1, damit das Minimum ohne Zusatz bei pi/6 liegt (H168)")
print("=" * 82)
d0, a0 = global_min(0.0, -1.0, 0.0, 0.0)
print(f"  ohne Zusatz: Minima gefaltet {np.round(a0, 6)}  (pi/6 = {np.pi/6:.6f})")


def report(lab, alpha, q):
    d, alls = global_min(alpha, -1.0, 0.0, q)
    # Versatz relativ zu pi/6; nimm den entarteten Zweig, der pi/6 am naechsten liegt
    best = min(alls, key=lambda f: abs(f - np.pi / 6))
    xp = np.pi / 6 - best
    z = (xp - X_NU) / SX_NU
    Rp = R_NO(best)
    print(f"  {lab:34s}: Minima {np.round(alls, 6)}; Zweig bei pi/6: {best:.6f} -> x_nu,pred = {xp:+.6f}  ({z:+.1f} sigma);  R_pred = {Rp:.6f} ({(Rp-ROBS)/SR:+.1f} sigma)")
    return xp, z


print("\n" + "=" * 82)
print("H221 a (nicht blind)  Weg K universell: |alpha/alphap| = 0,0793204")
print("=" * 82)
resA = [report(f"alpha_nu = {s:+.0f}*rho", s * RHO_K, 0.0) for s in (+1, -1)]

print("\n" + "=" * 82)
print("H221 b (teilweise nicht blind)  Weg S universell: |q/alphap| = 0,0852479 (Lambda_s ~ v_s)")
print("=" * 82)

resB = [report(f"q_nu = {s:+.0f}*|Q_S|", 0.0 + 0 * s, s * abs(Q_S)) for s in (+1, -1)]
# linear: Verhaeltnis der Verschiebungen
eps_e_lin = -(3 * np.sqrt(2) / 8) * Q_S
eps_n_lin = (3 / 4) * abs(Q_S)
print(f"  lineare Naeherung: |eps_e| = {abs(eps_e_lin):.5f}, |eps_nu| = {eps_n_lin:.5f}, Verhaeltnis {eps_n_lin/abs(eps_e_lin):.4f} (sqrt2 = {np.sqrt(2):.4f})")
print(f"  exakt: x_lepton = {X_LEP:.6f}; |x_nu,pred| (Zweig mit passendem Vorzeichen) / x_lepton = "
      f"{max(r[0] for r in resB)/X_LEP:.4f}")

print("\n" + "=" * 82)
print("H221 c (blind)  beide Terme universell: (alpha/alphap, q/alphap) fuer x_lepton UND x_nu (Fit, keine Vorhersage)")
print("=" * 82)


def offs(p, sa, sq):
    a, q = p
    de, _ = global_min(a, 1.0, np.pi / 4, q)
    dn, alls = global_min(sa * a, -1.0, 0.0, sq * q)
    best = min(alls, key=lambda f: abs(f - np.pi / 6))
    return np.array([np.pi / 12 - de - X_LEP, np.pi / 6 - best - X_NU])


for sa, sq in itertools.product((+1, -1), (+1, -1)):
    sols = []
    for a0 in np.linspace(-0.3, 0.3, 7):
        for q0 in np.linspace(-0.3, 0.3, 7):
            try:
                p, info, ier, msg = fsolve(offs, [a0, q0], args=(sa, sq), full_output=True, xtol=1e-12)
            except Exception:
                continue
            if ier == 1 and np.max(np.abs(offs(p, sa, sq))) < 1e-8:
                if all(np.max(np.abs(p - s)) > 1e-5 for s in sols):
                    sols.append(p)
    tag = ", ".join(f"(alpha={s[0]:+.5f}, q={s[1]:+.5f})" for s in sols) if sols else "keine Loesung im Startbereich |.|<=0,3"
    print(f"  Vorzeichen neutral (s_alpha={sa:+d}, s_q={sq:+d}): {tag}")

print("\n" + "=" * 82)
print("H221 d (blind)  gemeinsame Drehung chi -> chi + phi in beiden Sektoren, ohne weitere Terme")
print("=" * 82)
maxdev = 0.0
for x in (0.02, X_LEP, 0.04, 0.06):
    de, ae = global_min(0.0, 1.0, np.pi / 4 + x, 0.0)
    dn, an = global_min(0.0, -1.0, 0.0 + x, 0.0)
    te = min(ae, key=lambda f: abs(f - (np.pi / 12 - x)))
    tn = min(an, key=lambda f: abs(f - (np.pi / 6 - x)))
    dev = max(abs(te - (np.pi / 12 - x)), abs(tn - (np.pi / 6 - x)))
    maxdev = max(maxdev, dev)
    print(f"  phi = {x:.6f}: geladen Minima {np.round(ae, 7)} (Ziel pi/12-phi = {np.pi/12-x:.7f});  neutral Minima {np.round(an, 7)} "
          f"(Ziel pi/6-phi = {np.pi/6-x:.7f});  Abweichung {dev:.1e}")
print(f"  groesste Abweichung {maxdev:.1e}  -> Kriterium d (< 1e-9): {'JA' if maxdev < 1e-9 else 'nein'}")
print("  Hinweis: ohne Ordnung 6 ist jedes Minimum zweifach entartet (Partner pi/12+phi bzw. pi/6+phi); die Zweigwahl bleibt offen (H167).")

print("\n" + "=" * 82)
print("H221 Gesamturteil")
print("=" * 82)
zA = min(abs(r[1]) for r in resA)
okB = [r for r in resB if r[0] > 0]
zB = min(abs(r[1]) for r in okB) if okB else np.inf
print(f"  Weg K universell: bester Zweig {zA:.1f} sigma;  Weg S universell (richtiges Vorzeichen): {zB:.1f} sigma")
failK, failS = zA > 3, zB > 3
if failK and not failS and zB <= 2:
    v = "TRAEGT (trennt: Weg S traegt, Weg K scheitert) -> spricht fuer die Skala"
elif failS and not failK and zA <= 2:
    v = "TRAEGT (trennt: Weg K traegt, Weg S scheitert)"
elif failK and failS:
    v = "TRAEGT TEILWEISE (beide universell ausgeschlossen)" + (" ; d traegt -> spricht fuer eine skalenfreie gemeinsame Drehung" if maxdev < 1e-9 else "")
elif zA <= 2 and zB <= 2:
    v = "WIDERLEGT (beide tragen)"
else:
    v = "UNENTSCHIEDEN"
print("  ->", v)
