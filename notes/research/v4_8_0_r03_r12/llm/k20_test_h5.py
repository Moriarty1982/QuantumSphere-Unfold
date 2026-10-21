"""k20: Test der Vorab-Notiz H5 (Commit 16eff15): Polwinkel der erhaltenen Spalte als Hopf-Winkel."""
import numpy as np, itertools
from scipy.optimize import minimize

OBS = {"s12": (0.308, 0.012, 0.011), "s13": (0.02215, 0.00056, 0.00058),
       "s23": (0.470, 0.017, 0.013), "d": (212.0, 26.0, 41.0)}
c1 = np.array([2, -1, -1])/np.sqrt(6); c2 = np.array([1, 1, 1])/np.sqrt(3); c3 = np.array([0, 1, -1])/np.sqrt(2)

def pull2(name, x):
    v, up, lo = OBS[name]
    diff = ((x - v + 180) % 360 - 180) if name == "d" else x - v
    return (diff/(up if diff > 0 else lo))**2

def obs_from_U(U):
    s13 = abs(U[0, 2])**2; c13 = 1 - s13
    if c13 <= 0: return None
    s12 = abs(U[0, 1])**2/c13; s23 = abs(U[1, 2])**2/c13
    S12, C12, S23, C23, S13 = np.sqrt(s12), np.sqrt(1-s12), np.sqrt(s23), np.sqrt(1-s23), np.sqrt(s13)
    den = S12*C12*S23*C23*S13
    if den < 1e-12: return None
    J = np.imag(U[0, 0]*U[1, 1]*np.conj(U[0, 1])*np.conj(U[1, 0]))
    sind = J/(den*c13)
    cosd = (abs(U[1, 0])**2 - s12*(1-s23) - (1-s12)*s23*s13)/(2*den)
    return s12, s13, s23, np.degrees(np.arctan2(sind, cosd)) % 360

def chi2_U(U):
    o = obs_from_U(U)
    if o is None: return 1e6
    return sum(pull2(k, x) for k, x in zip(("s12", "s13", "s23", "d"), o)), o

def build(a, b, th, ph, j, order):
    w = np.cos(a)*c2 - np.sin(a)*np.exp(1j*b)*c1
    u = np.sin(a)*np.exp(-1j*b)*c2 + np.cos(a)*c1
    x = np.cos(th)*u + np.sin(th)*np.exp(1j*ph)*c3
    y = -np.sin(th)*np.exp(-1j*ph)*u + np.cos(th)*c3
    cols = [None]*3; cols[j] = w
    rest = [k for k in range(3) if k != j]
    cols[rest[0]], cols[rest[1]] = (x, y) if order == 0 else (y, x)
    return np.array(cols).T

STARTS = [(t, p) for t in (0.1, 0.2, 0.5, 1.0, 1.4) for p in (0.5, 2.0, 3.5, 5.0)]
def fit(a, b, free_b=False, starts=STARTS):
    best = (1e9, None, None)
    for j, order in itertools.product((0, 1), (0, 1)):
        for t0, p0 in starts:
            if free_b:
                f = lambda q: chi2_U(build(a, q[2], q[0], q[1], j, order))[0] if chi2_U(build(a, q[2], q[0], q[1], j, order)) != 1e6 else 1e6
                x0 = [t0, p0, b]
            else:
                f = lambda q: (lambda r: r if r == 1e6 else r[0])(chi2_U(build(a, b, q[0], q[1], j, order)))
                x0 = [t0, p0]
            r = minimize(f, x0, method="Nelder-Mead", options=dict(xatol=1e-8, fatol=1e-9, maxiter=4000))
            if r.fun < best[0]:
                q = r.x; bb = q[2] if free_b else b
                best = (r.fun, chi2_U(build(a, bb, q[0], q[1], j, order))[1], (j+1, np.degrees(bb) % 360))
    return best

if __name__ == "__main__":
    print("Kontrolle: TM1 (theta=180):", round(fit(np.pi/2, 0)[0], 3), "  TM2 (theta=0):", round(fit(0.0, 0)[0], 3))
    print("\nVariante (i): kanonische Azimute")
    hits = 0
    for th_deg in (66.64, 70.53, 180-66.64, 180-70.53):
        for b_deg in (0, 90, 180, 270):
            c, o, (j, _) = fit(np.radians(th_deg)/2, np.radians(b_deg))
            ok = c < 5.99; hits += ok
            os_ = "" if o is None else f"s12={o[0]:.4f} s13={o[1]:.5f} s23={o[2]:.3f} dCP={o[3]:.0f}"
            print(f"  theta={th_deg:6.2f}  b={b_deg:3d}: chi2={c:9.2f} (nu{j}) {'VERTRAEGLICH' if ok else ''}  {os_}")
    print(f"  Treffer: {hits} von 32 (je Kombination beste Zuordnung; 16 Zeilen x 2 Zuordnungen intern)")
    print("\nVariante (ii): Azimut frei")
    for th_deg in (66.64, 70.53, 180-66.64, 180-70.53):
        best = min((fit(np.radians(th_deg)/2, np.radians(b0), free_b=True) for b0 in (10, 100, 190, 280)),
                   key=lambda r: r[0])
        c, o, (j, bb) = best
        print(f"  theta={th_deg:6.2f}: chi2={c:.3f} (nu{j}, b={bb:.1f})  s12={o[0]:.4f} s13={o[1]:.5f} "
              f"s23={o[2]:.3f} dCP={o[3]:.0f}  {'vertraeglich' if c < 3.84 else 'NICHT vertraeglich'}")
    print("\nFlaechenanteil f der S^2 mit chi2 < 5,99 (Versuchsfaktor):")
    rng = np.random.default_rng(20); n = 400; good = 0
    small = [(0.2, 1.0), (1.0, 4.0), (0.5, 2.5)]
    for _ in range(n):
        th = np.arccos(rng.uniform(-1, 1)); b = rng.uniform(0, 2*np.pi)
        good += fit(th/2, b, starts=small)[0] < 5.99
    f = good/n
    print(f"  f = {f:.3f} (n={n}),  erwartete Zufallstreffer bei 32 Versuchen: {32*f:.1f}")

# ---- Nachbefund (NICHT vorab registriert): Geometrie auf der Hopf-Sphaere ----
def nachbefund():
    print("\nNachbefund (nicht vorab registriert):")
    m = np.array([2*np.sqrt(2)/3, 0, 1/3])
    rng = np.random.default_rng(1); err = 0
    for _ in range(1000):
        th = np.arccos(rng.uniform(-1, 1)); b = rng.uniform(0, 2*np.pi); a = th/2
        w = np.cos(a)*c2 - np.sin(a)*np.exp(1j*b)*c1
        n = np.array([np.sin(th)*np.cos(b), np.sin(th)*np.sin(b), np.cos(th)])
        err = max(err, abs(abs(w[0])**2 - (1 - m@n)/2), abs(abs(w[1])**2 - abs(w[2])**2))
    print(f"  |w_e|^2 = (1 - m.n)/2 mit m = (2sqrt2/3, 0, 1/3) und |w_mu| = |w_tau|: max. Abw. {err:.1e}")
    print(f"  Punkt E (w_e = 0): Polwinkel {np.degrees(np.arccos(1/3)):.2f} Grad, b = 0")
    s12, s13 = 0.308, 0.02215
    for name, ue in (("nu1", (1-s12)*(1-s13)), ("nu2", s12*(1-s13))):
        print(f"  {name}: |U_e|^2 = {ue:.4f} -> Abstand zu E: gamma = {np.degrees(2*np.arcsin(np.sqrt(ue))):.2f} Grad")
    beta = 0.54935
    print(f"  theta_H = 2 arcsin(beta_sym) = {np.degrees(2*np.arcsin(beta)):.2f} Grad;  beta_sym^2 = {beta**2:.5f}")
    print(f"  Relation |U_e2|^2 = beta_sym^2  =>  sin^2 theta12 = {beta**2/(1-s13):.4f} (gemessen 0.308 +0.012/-0.011)")
nachbefund()
