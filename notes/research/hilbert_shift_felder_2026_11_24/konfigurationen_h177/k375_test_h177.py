"""k375 (H177): Phasenhalbierung delta_e : delta_d : delta_u = 4 : 2 : 1 (V1) bzw. pi/12, pi/24, pi/48 (V2) bei gemeinsamer Skala?
Ein-Schleifen-Laufen des Standardmodells oberhalb M_Z mit Top-Dominanz. Aufruf: python k375_test_h177.py > k375_out.txt"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

rng = np.random.default_rng(20261126)
w = np.exp(2j * np.pi / 3); kk = np.arange(3)
NMC = 100_000
MZ, MPL = 91.1876, 1.22e19
DE = 0.2222220470731

def K_delta(m, neg=False):
    v = np.sqrt(m)
    if neg:
        v = v * np.array([-1.0, 1.0, 1.0])
    c = np.sum(v * np.conj(w**kk), axis=-1)
    d = np.mod(np.angle(c), 2 * np.pi / 3)
    d = np.minimum(d, 2 * np.pi / 3 - d)
    return np.sum(m, axis=-1) / np.sum(v, axis=-1)**2, d

# Yukawa-Kopplungen bei M_Z (Tabelle aus k14/k367)
up = [(7.04e-6, 0.15e-6), (3.56e-3, 0.06e-3), (0.967, 0.004)]
dn = [(1.54e-5, 0.02e-5), (3.06e-4, 0.04e-4), (1.630e-2, 0.009e-2)]

# --- 1. Laufen: g1 (GUT-Normierung), g2, g3, y_t; I(mu) = int (3/2) y_t^2 / (16 pi^2) dln mu
def rhs(t, y):
    g1, g2, g3, yt, I = y
    k = 1 / (16 * np.pi**2)
    return [k * 41 / 10 * g1**3, -k * 19 / 6 * g2**3, -k * 7 * g3**3,
            k * yt * (4.5 * yt**2 - 17 / 20 * g1**2 - 9 / 4 * g2**2 - 8 * g3**2), k * 1.5 * yt**2]
y0 = [0.4613, 0.6517, 1.2198, 0.967, 0.0]
tmax = np.log(MPL / MZ)
sol = solve_ivp(rhs, [0, tmax], y0, dense_output=True, rtol=1e-10, atol=1e-12)
IMAX = sol.y[4, -1]
print("== 1. Laufen (eine Schleife, Standardmodell, Start M_Z: g1 0.4613, g2 0.6517, g3 1.2198, y_t 0.967) ==")
for mu in (MZ, 1e3, 1e6, 1e10, 1e13, 2e16, MPL):
    s = sol.sol(np.log(mu / MZ))
    print(f"   mu = {mu:9.3g} GeV: y_t = {s[3]:.4f}, g3 = {s[2]:.4f}, I = {s[4]:.5f}")
print(f"   Bereich: I von 0 bis I(M_Planck) = {IMAX:.5f}")
def mu_of_I(I):
    if I <= 0 or I >= IMAX: return np.nan
    return MZ * np.exp(brentq(lambda t: sol.sol(t)[4] - I, 0, tmax))

# --- 2. delta und K als Funktion von I
def scaled(m, I, typ):
    m = np.array(m, float).copy()
    f = np.exp(-I) if typ == "up" else np.exp(I)
    m[..., 0] *= f; m[..., 1] *= f      # leichte beiden relativ zur schwersten
    return m
def samples(dat):
    mu = np.array([a for a, _ in dat]); sd = np.array([b for _, b in dat])
    return mu, np.sort(np.clip(rng.normal(mu, sd, size=(NMC, 3)), 1e-30, None), axis=1)
MU = {"up": samples(up), "down": samples(dn)}
def obs(typ, I, neg=False):
    mu, sam = MU[typ]
    K0, d0 = K_delta(scaled(mu, I, typ), neg)
    Ks, ds = K_delta(scaled(sam, I, typ), neg)
    return K0, d0, Ks.std(), ds.std()

print("\n== 2. K und delta ueber den Bereich (Zentralwert +- Massenfehler) ==")
print("   I | mu [GeV] | delta_d | delta_u | delta_d/delta_u | delta_e/delta_d | K_d | K_u")
for I in np.linspace(0, IMAX, 9):
    Kd, dd, sKd, sdd = obs("down", I); Ku, du, sKu, sdu = obs("up", I)
    r = dd / du; sr = r * np.hypot(sdd / dd, sdu / du)
    print(f"   {I:.4f} | {mu_of_I(I) if 0 < I < IMAX else (MZ if I == 0 else MPL):9.3g} | {dd:.6f} +- {sdd:.6f} | {du:.6f} +- {sdu:.6f} | {r:.4f} +- {sr:.4f} | {DE/dd:.4f} | {Kd:.5f} +- {sKd:.5f} | {Ku:.5f} +- {sKu:.5f}")

# --- 3. Kriterien
print("\n== 3. H177a: Zielwerte gegen den Bereich ==")
grid = np.linspace(0, IMAX, 401)
cache = {(typ, neg): np.array([obs(typ, I, neg) for I in grid]) for typ in ("down", "up") for neg in (False, True)}
def crossing(typ, target, neg=False):
    """I, bei dem der Zentralwert das Ziel trifft (oder None), dazu 1-sigma-Breite in I."""
    f = lambda I: K_delta(scaled(MU[typ][0], I, typ), neg)[1] - target
    if f(0) * f(IMAX) > 0: return None
    I0 = brentq(f, 0, IMAX)
    sd = obs(typ, I0, neg)[3]
    slope = (f(min(I0 + 1e-4, IMAX)) - f(max(I0 - 1e-4, 0))) / (min(I0 + 1e-4, IMAX) - max(I0 - 1e-4, 0))
    return I0, abs(sd / slope)
for name, td, tu in (("V1 (delta_e/2, delta_e/4)", DE / 2, DE / 4), ("V2 (pi/24, pi/48)", np.pi / 24, np.pi / 48)):
    print(f"-- {name}: Ziel delta_d = {td:.6f}, delta_u = {tu:.6f}")
    zd = (cache[("down", False)][:, 1] - td) / cache[("down", False)][:, 3]
    zu = (cache[("up", False)][:, 1] - tu) / cache[("up", False)][:, 3]
    both = np.maximum(abs(zd), abs(zu)); i = both.argmin()
    print(f"   kleinstes max(|z_d|, |z_u|) im Bereich: {both[i]:.1f} bei I = {grid[i]:.4f} (z_d = {zd[i]:+.1f}, z_u = {zu[i]:+.1f})")
    print(f"   z-Bereich einzeln: Down {zd.min():+.1f} bis {zd.max():+.1f}, Up {zu.min():+.1f} bis {zu.max():+.1f}")
    cd, cu = crossing("down", td), crossing("up", tu)
    for lab, c in (("Down", cd), ("Up", cu)):
        print(f"   {lab}: " + (f"trifft bei I = {c[0]:.4f} +- {c[1]:.4f} (mu = {mu_of_I(c[0]):.3g} GeV)" if c else "erreicht den Zielwert im Bereich nicht (Zentralwert)"))
    hit_d = (abs(zd) < 3).any(); hit_u = (abs(zu) < 3).any()
    if both[i] < 3: v = "TRAEGT (gemeinsames I innerhalb 3 sigma; Faktor 2 fuer zwei Fassungen beachten)"
    elif hit_d and hit_u:
        sep = abs(cd[0] - cu[0]) / np.hypot(cd[1], cu[1]) if cd and cu else float("nan")
        v = f"NICHT GEMEINSAM (jede Phase erreicht ihr Ziel, I-Abstand {sep:.1f} sigma)"
    else: v = "WIDERLEGT (" + ", ".join(l for l, h in (("Down", hit_d), ("Up", hit_u)) if not h) + " erreicht das Ziel nicht innerhalb 3 sigma)"
    print(f"   Urteil: {v}")

print("\n== 4. H177b: Bericht ==")
f = lambda I: obs("down", I)[1] / obs("up", I)[1] - 2
if f(0) * f(IMAX) < 0:
    I2 = brentq(f, 0, IMAX); Kd, dd, _, sdd = obs("down", I2); Ku, du, _, sdu = obs("up", I2)
    print(f"   delta_d/delta_u = 2 bei I = {I2:.4f} (mu = {mu_of_I(I2):.3g} GeV): delta_d = {dd:.6f} +- {sdd:.6f}, delta_u = {du:.6f} +- {sdu:.6f}; delta_e/delta_d = {DE/dd:.4f}; K_d = {Kd:.5f}, K_u = {Ku:.5f}")
else:
    print(f"   delta_d/delta_u = 2 wird im Bereich nicht erreicht (Verhaeltnis {f(0)+2:.4f} bei I = 0, {f(IMAX)+2:.4f} bei I_max)")
for typ in ("down", "up"):
    a = cache[(typ, False)]; b = cache[(typ, True)]
    print(f"   {typ}: K von {a[0,0]:.5f} (M_Z) bis {a[-1,0]:.5f} (M_Planck); erreicht 2/3: {'ja' if (a[:,0].min() - 2/3) * (a[:,0].max() - 2/3) < 0 else 'nein'}")
    print(f"   {typ}, leichteste Wurzel negativ: delta von {b[0,1]:.6f} bis {b[-1,1]:.6f}, K von {b[0,0]:.5f} bis {b[-1,0]:.5f}")
# Empfindlichkeit: welche Verschiebung braeuchte man?
print("   Rueckwaerts: noetiges I je Ziel ohne Bereichsgrenze (negativ = unterhalb M_Z, dort laeuft das Verhaeltnis in dieser Naeherung nicht):")
for typ, targets in (("down", (DE / 2, np.pi / 24)), ("up", (DE / 4, np.pi / 48))):
    for tg in targets:
        g = lambda I: K_delta(scaled(MU[typ][0], I, typ))[1] - tg
        try: print(f"      {typ}, Ziel {tg:.6f}: I = {brentq(g, -3, 3):+.4f}")
        except ValueError: print(f"      {typ}, Ziel {tg:.6f}: keine Loesung in [-3, 3]")
