"""k274 (Erkundung, nicht blind, 24.11.2026): Nichtlineares Ursprungsfeld. Bleibt der Turm skalenfrei?
HS(0): psi'' = -w^2 psi - lam psi^3 (Duffing). Verallgemeinert auf jede Stufe: psi'' = -w^2 psi - lam |psi|^2 psi, psi in A_n.
A  HS(0): Periode gegen Amplitude; fuer lam < 0 Fluchtschwelle A* = w/sqrt(|lam|) (Vorzeichenwechsel der Rueckstellung).
B  HS(1): Bahnen in C. Ladung L (Drehimpuls) erhalten; Linie (a=b) und Kreis (b=0) bleiben geschlossen;
   jede echte Ellipse praezediert (Bertrand). Praezessionswinkel je Radialperiode.
C  Kreisbahn exp(u W t) psi0 mit W^2 = w^2 + lam |psi0|^2 ist exakte Loesung fuer n <= 3, nicht fuer n = 4.
D  Struktur: |g psi| = |psi| fuer Automorphismen g -> der Nichtlinearterm vertauscht mit Der; Der, Stab unveraendert.
Aufruf aus diesem Ordner: python3 k274_nichtlinear.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

rng = np.random.default_rng(274)
w = 1.0


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


def rhs(lam):
    def f(t, s):
        D = len(s) // 2
        q, p = s[:D], s[D:]
        return np.concatenate([p, -w ** 2 * q - lam * (q @ q) * q])
    return f


print("=" * 78)
print("A  HS(0) Duffing: Periode T(A) (linear: 2 pi = 6.2832)")
for lam in (0.0, 0.5, -0.5):
    row = []
    for A in (0.1, 0.5, 1.0, 1.3):
        sol = solve_ivp(rhs(lam), (0, 60), [A, 0.0], rtol=1e-11, atol=1e-12, dense_output=True,
                        events=lambda t, s: s[1], max_step=0.01)
        tz = [t for t in sol.t_events[0] if t > 1e-6]
        esc = np.abs(sol.y[0]).max() > 50 or sol.status == -1
        if esc:
            row.append(f"A={A}: flieht")
        elif len(tz) >= 2:
            row.append(f"A={A}: T={2 * (tz[1] - tz[0]):.4f}")
        else:
            row.append(f"A={A}: ?")
    print(f"   lam={lam:+.1f}: " + ", ".join(row))
print(f"   lam=-0.5: Rueckstellkraft -w^2 psi - lam psi^3 wechselt das Vorzeichen bei |psi| = w/sqrt(|lam|) = {w / np.sqrt(0.5):.4f}")

print("=" * 78)
print("B  HS(1) mit lam |psi|^2 psi: Ladung und Praezession der Ellipse a e^{iwt} + b e^{-iwt} (Startwerte des linearen Falls)")


def apsis_precession(a, b, lam, T=300.0):
    q0 = np.array([a + b, 0.0])
    v = w * (a - b)
    if b == 0 or a == 0:  # Kreis: Geschwindigkeit an die nichtlineare Frequenz W angepasst
        r0 = a + b
        v = np.sign(a - b) * r0 * np.sqrt(w ** 2 + lam * r0 ** 2)
    p0 = np.array([0.0, v])
    sol = solve_ivp(rhs(lam), (0, T), np.concatenate([q0, p0]), rtol=1e-11, atol=1e-12, max_step=0.01)
    q = sol.y[:2]; p = sol.y[2:]
    if sol.status != 0 or np.abs(q).max() > 50:
        return None
    L = q[0] * p[1] - q[1] * p[0]
    r = np.hypot(q[0], q[1])
    idx = [k for k in range(1, len(r) - 1) if r[k] > r[k - 1] and r[k] >= r[k + 1]]
    th = np.arctan2(q[1][idx], q[0][idx])
    # Hauptachse ist eine Richtung mod pi: Differenzen nach (-pi/2, pi/2] falten
    d = (np.diff(th) + np.pi / 2) % np.pi - np.pi / 2
    return L.max() - L.min(), L[0], (d.mean() if len(d) else float('nan')), r.max() - r.min()


for lam in (0.0, 0.3, -0.3):
    for a, b in [(1.0, 1.0), (1.0, 0.0), (1.0, 0.5), (0.5, 1.0), (0.7, 0.6)]:
        lab = "Linie" if a == b else ("Kreis" if b == 0 else "Ellipse")
        res = apsis_precession(a, b, lam)
        if res is None:
            print(f"   lam={lam:+.1f} a={a:.1f} b={b:.1f} ({lab:7s}): flieht (Startradius ueber der Schwelle)")
            continue
        dL, L0, prec, dr = res
        msg = f"   lam={lam:+.1f} a={a:.1f} b={b:.1f} ({lab:7s}): L={L0:+.3f} (Drift {dL:.1e})"
        if lab == "Ellipse":
            msg += f", Drehung der Hauptachse je Halbumlauf = {prec:+.4f} rad"
        if lab == "Kreis":
            msg += f", Radius schwankt um {dr:.1e} (exakter Kreis)"
        print(msg)
print("   -> Linie und Kreis bleiben geschlossen; jede echte Ellipse praezediert (Bertrand). Der Sinn der Praezession folgt")
print("      dem Umlaufsinn (a<->b kehrt beide um) und dem Vorzeichen von lam; einen Drehsinn waehlt die Nichtlinearitaet nicht.")

print("=" * 78)
print("C  Kreisbahn exp(u W t) psi0, W^2 = w^2 + lam |psi0|^2, als Loesung der nichtlinearen Gleichung")
lam = 0.7
for n in range(1, 5):
    N = 2 ** n
    E = np.eye(N)
    Lmat = lambda v: np.array([mul(v, E[k]) for k in range(N)]).T
    worst = 0.0
    for _ in range(20):
        u = rng.normal(size=N); u[0] = 0; u /= np.linalg.norm(u)
        psi0 = rng.normal(size=N)
        W = np.sqrt(w ** 2 + lam * psi0 @ psi0)
        Lu = Lmat(u)
        for t in (0.3, 1.7):
            psi = expm(Lu * W * t) @ psi0
            acc = Lu @ Lu @ psi * W ** 2
            res = acc - (-w ** 2 * psi - lam * (psi @ psi) * psi)
            worst = max(worst, np.abs(res).max())
    print(f"   n={n} (dim {N:2d}): max Residuum = {worst:.1e}")

print("=" * 78)
print("D  Nichtlinearterm und Automorphismen (O): |g psi| = |psi|")
E8 = np.eye(8)
C8 = np.array([[mul(E8[i], E8[j]) for j in range(8)] for i in range(8)])
# Derivation aus k270-Methode: einfache bekannte Derivation D = [L_a, L_b] + [L_a, R_b] + [R_a, R_b] (Schafer) fuer a,b imaginaer
La = lambda i: C8[i].T
Ra = lambda i: C8[:, i, :].T
a, b = 1, 2
D = (La(a) @ La(b) - La(b) @ La(a)) + (La(a) @ Ra(b) - Ra(b) @ La(a)) + (Ra(a) @ Ra(b) - Ra(b) @ Ra(a))
x, y = rng.normal(size=8), rng.normal(size=8)
print(f"   D ist Derivation: |D(xy) - D(x)y - xD(y)| = {np.abs(D @ mul(x, y) - mul(D @ x, y) - mul(x, D @ y)).max():.1e}")
g = expm(0.37 * D)
print(f"   g = exp(tD): |g psi| - |psi| = {abs(np.linalg.norm(g @ x) - np.linalg.norm(x)):.1e};"
      f"  g(|psi|^2 psi) - |g psi|^2 g psi = {np.abs(g @ ((x @ x) * x) - ((g @ x) @ (g @ x)) * (g @ x)).max():.1e}")
print("   -> Der Nichtlinearterm ist G2-aequivariant: Symmetrien, Stabilisatoren und Lecks bleiben; es aendern sich nur Frequenzen.")
