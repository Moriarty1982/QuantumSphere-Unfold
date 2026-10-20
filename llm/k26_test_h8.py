"""k26: Test der Vorab-Notiz H8 (Commit f6734ab): Cayley-Dickson-Involution als CP-Symmetrie.
Generationenbasis (e4,e5,e6); Triole = vorzeichenfreier Lift (zyklisch); CP: X = -1 (k25-Zusatz)."""
import numpy as np, contextlib, io, os
from scipy.optimize import minimize_scalar
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k25_test_h7.py")).read())

OBS = {"s12": (0.308, 0.012, 0.011), "s13": (0.02215, 0.00056, 0.00058),
       "s23": (0.470, 0.017, 0.013), "d": (212.0, 26.0, 41.0)}
def pull2(n, x):
    v, up, lo = OBS[n]; diff = ((x - v + 180) % 360 - 180) if n == "d" else x - v
    return (diff/(up if diff > 0 else lo))**2
def angles(U):
    s13 = abs(U[0, 2])**2; c13 = 1 - s13
    s12 = abs(U[0, 1])**2/c13; s23 = abs(U[1, 2])**2/c13
    S12, C12, S23, C23, S13 = np.sqrt(s12), np.sqrt(1-s12), np.sqrt(s23), np.sqrt(1-s23), np.sqrt(s13)
    den = S12*C12*S23*C23*S13
    J_ = np.imag(U[0, 0]*U[1, 1]*np.conj(U[0, 1])*np.conj(U[1, 0]))
    cosd = (abs(U[1, 0])**2 - s12*(1-s23) - (1-s12)*s23*s13)/(2*den)
    return s12, s13, s23, np.degrees(np.arctan2(J_/(den*c13), cosd)) % 360, J_

g3 = cmat(lifts3[3]).real
w, Vl = np.linalg.eig(g3.astype(complex))
i1 = int(np.argmin(abs(w - 1))); iw = int(np.argmin(abs(w - np.exp(2j*np.pi/3)))); iw2 = 3 - i1 - iw
Ul = {"mu=omega": Vl[:, [i1, iw, iw2]], "mu=omega^2": Vl[:, [i1, iw2, iw]]}
Ul = {k: v/np.linalg.norm(v, axis=0) for k, v in Ul.items()}
X = -np.eye(3)

alle = lifts_rel(lifts3[3])
hs = {"TM1": [C.real for M, C in alle["TM1"]], "TBM3": [C.real for M, C in alle["TBM3"]]}
hs["TM2"] = [cmat(K).real for K in kernel]

# (1) direkt aus den Nebenbedingungen: symmetrisches komplexes m, h^T m h = m, X^T m X = conj(m)
def solution_space(h):
    basis = []
    for i in range(3):
        for j in range(i, 3):
            for part in (1, 1j):
                E = np.zeros((3, 3), complex); E[i, j] = E[j, i] = part; basis.append(E)
    rows = []
    for E in basis:
        r1 = (h.T @ E @ h - E).flatten()
        r2 = (X.T @ E @ X).flatten()          # X^T m X = conj(m): linear in Real/Imag-Koordinaten
        rows.append(np.concatenate([r1.real, r1.imag]))
    A = np.array(rows).T                       # h-Bedingung
    # CP-Bedingung bei X = -1: m reell -> Imaginaerteil-Koeffizienten = 0
    B = np.array([[1.0 if (k % 2 == 1 and k == idx) else 0 for k in range(len(basis))] for idx in range(1, len(basis), 2)])
    M = np.vstack([A, B])
    _, s, Vt = np.linalg.svd(M); null = Vt[np.sum(s > 1e-10):]
    return [sum(c*E for c, E in zip(vec, basis)) for vec in null]

print("(1) Zufallsstichproben aus dem Loesungsraum (je 2000):")
rng = np.random.default_rng(26)
for typ in ("TM1", "TBM3", "TM2"):
    for h in hs[typ][:1]:
        sp = solution_space(h)
        res = []
        for _ in range(2000):
            m = sum(rng.normal()*E for E in sp)
            lam, O = np.linalg.eigh(m.real)
            Unu = O @ np.diag([1 if l >= 0 else 1j for l in lam])
            for key_, U_l in Ul.items():
                U = U_l.conj().T @ Unu
                # Spalten so ordnen, dass die erhaltene Spalte an der TM-typischen Stelle steht, Rest nach |U_e|
                order = np.argsort(-abs(U[0])**2) if typ != "TBM3" else np.argsort(-abs(U[0])**2)
                U = U[:, order]
                res.append(angles(U)[:4])
        r = np.array(res)
        print(f"  {typ}: Dimension Loesungsraum {len(sp)};  sin2t23 in [{r[:,2].min():.4f}, {r[:,2].max():.4f}],"
              f"  dCP-Werte: {sorted(set(np.round(r[:,3]).astype(int) % 360))[:8]}")

# (2) Parametrisierung: erhaltene Spalte w (reell) + reelle Drehung theta im Orthogonalraum
def Unu_theta(h, th, slot):
    ev, EV = np.linalg.eigh(h); vals = np.round(ev).astype(int)
    s = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    wv = EV[:, s]; rest = [EV[:, i] for i in range(3) if i != s]
    a = np.cos(th)*rest[0] + np.sin(th)*rest[1]; b = -np.sin(th)*rest[0] + np.cos(th)*rest[1]
    cols = [None]*3; cols[slot] = wv; others = [i for i in range(3) if i != slot]
    cols[others[0]], cols[others[1]] = a, b
    return np.array(cols).T

print("\n(2) Ein-Winkel-Fit an NuFIT 6.0 (NO), TM1-Spalte als nu1:")
best_all = None
for key_, U_l in Ul.items():
    for k, h in enumerate(hs["TM1"]):
        f = lambda th: sum(pull2(n, x) for n, x in zip(("s12", "s13", "s23", "d"), angles(U_l.conj().T @ Unu_theta(h, th, 0))[:4]))
        grid = np.linspace(0, np.pi, 3601); vals = [f(t) for t in grid]
        t0 = grid[int(np.argmin(vals))]
        r = minimize_scalar(f, bounds=(t0 - 0.01, t0 + 0.01), method="bounded")
        a = angles(U_l.conj().T @ Unu_theta(h, r.x, 0))
        parts = [pull2(n, x) for n, x in zip(("s12", "s13", "s23", "d"), a[:4])]
        print(f"  {key_:11s} h{k}: chi2 = {r.fun:.3f}  (s12 {parts[0]:.2f}, s13 {parts[1]:.2f}, s23 {parts[2]:.2f}, d {parts[3]:.2f})"
              f"  sin2t12={a[0]:.4f} sin2t13={a[1]:.5f} sin2t23={a[2]:.4f} dCP={a[3]:.1f}")
        if best_all is None or r.fun < best_all[0]: best_all = (r.fun, a, key_, k, r.x)
c2, a, key_, k, th = best_all
print(f"\n  Bestes: chi2_min = {c2:.3f} bei 3 FG ({key_}, h{k}): sin2t12={a[0]:.4f}, sin2t23={a[2]:.4f}, dCP={a[3]:.1f}")
print("  Kriterium: vertraeglich < 7,81; Spannung 7,81-11,34; disfavorisiert >= 11,34")

# (3) m_bb mit H2-Massen, Majorana-Paritaeten eta in {+-1}^3 (CP erzwingt reelle Paritaeten)
m = np.array([0.364, 8.662, 50.131])*1e-3
U = Ul[key_].conj().T @ Unu_theta(hs["TM1"][k], th, 0)
mbb = {}
import itertools
for eta in itertools.product((1, -1), repeat=3):
    mbb[eta] = abs(sum(eta[i]*U[0, i]**2*m[i] for i in range(3)))*1e3
print(f"\n(3) m_bb (meV) mit H3-Paritaeten (-1,+1,+1): {mbb[(-1, 1, 1)]:.3f};  alle Paritaeten: "
      f"{min(mbb.values()):.3f} bis {max(mbb.values()):.3f}")
