"""k86: Test der Vorab-Notiz H30 (Commit d755a08): Bricht die anomaliefreie Chiralitaet (iL_e7) die Symmetrien rho und tau
der Triality-Form? Modell I (gleiche Chiralitaet auf allen Plaetzen), Modell II (triality-kovariante Fortsetzung in g)."""
import numpy as np, os, sys
from scipy.linalg import null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
c = np.diag([1.] + [-1.]*7)
t = lambda x, y, z: omul(omul(x, y), z)[0]
rng = np.random.default_rng(86)

# H30a
a1 = abs(c@L7@c + R7).max(); a2 = abs(c@R7@c + L7).max()
swap = max(abs(t(x, z, y) - t(x, y, z)) for x, y, z in rng.normal(size=(20, 3, 8)))
ok_a = a1 < TOL and a2 < TOL and swap > 1e-3
print(f"H30a: c L_e7 c = -R_e7: {a1:.0e}; c R_e7 c = -L_e7: {a2:.0e}; reines Vertauschen (x,z,y) aendert t um bis zu {swap:.3f}"
      f" -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H30b: auf C (x) O^3
I8, I3 = np.eye(8), np.eye(3)
P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]); Rp = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
tau = np.kron(P, I8); rho = np.kron(Rp, c)
def t3(v): return t(v[:8], v[8:16], v[16:24])
sym_ok = max(max(abs(t3(tau@v) - t3(v)), abs(t3(rho@v) - t3(v))) for v in rng.normal(size=(20, 24)))
G = {"1": np.eye(24)}
for name, g in [("tau", tau), ("tau2", tau@tau), ("rho", rho), ("tau.rho", tau@rho), ("tau2.rho", tau@tau@rho)]: G[name] = g
Cd = np.kron(I3, 0.5*(I8 + 1j*L7)); Cr = np.kron(I3, 0.5*(I8 - 1j*R7))
res = {}
for n, g in G.items():
    Cg = g@Cd@np.linalg.inv(g)
    res[n] = "erhaelt C" if abs(Cg - Cd).max() < TOL else ("-> 1/2(1 - iR_e7)" if abs(Cg - Cr).max() < TOL else "anders")
ok_b = sym_ok < TOL and all(res[n] == "erhaelt C" for n in ("1", "tau", "tau2")) and \
       all(res[n] == "-> 1/2(1 - iR_e7)" for n in ("rho", "tau.rho", "tau2.rho"))
print(f"\nH30b: Symmetrien von t (Kontrolle {sym_ok:.0e}); Wirkung auf diag C(iL_e7): {res} -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H30c, d: Triality-Algebra wie k78
T3 = np.array([[[t(E[i], E[j], E[k]) for k in range(8)] for j in range(8)] for i in range(8)])
pairs = [(a, b) for a in range(8) for b in range(a + 1, 8)]
so8 = []
for a, b in pairs:
    X = np.zeros((8, 8)); X[a, b] = 1; X[b, a] = -1; so8.append(X)
Mx = np.column_stack([np.einsum('mi,mjk->ijk', X, T3).ravel() for X in so8] +
                     [np.einsum('mj,imk->ijk', X, T3).ravel() for X in so8] +
                     [np.einsum('mk,ijm->ijk', X, T3).ravel() for X in so8])
N = null_space(Mx, rcond=1e-12)
mat = lambda co: sum(co[s]*so8[s] for s in range(28))
coefL = np.array([L7[a, b] for a, b in pairs])
y = np.linalg.lstsq(N[:28], coefL, rcond=None)[0]
A, B, Cm = mat(N[:28]@y), mat(N[28:56]@y), mat(N[56:]@y)
fitA = abs(A - L7).max()
def in_LR(X):
    co = np.linalg.lstsq(np.column_stack([L7.ravel(), R7.ravel()]), X.ravel(), rcond=None)[0]
    return co, abs(co[0]*L7 + co[1]*R7 - X).max()
coB, rB = in_LR(B); coC, rC = in_LR(Cm)
tau_inv = abs(B - A).max() > 1e-6 or abs(Cm - B).max() > 1e-6
# (A,A,A) in g mit A = L_e7?  Pruefe Rest von M x fuer x = (coefL, coefL, coefL)
diag_res = abs(Mx@np.concatenate([coefL]*3)).max()
ok_c = fitA < TOL and rB < TOL and rC < TOL and tau_inv and diag_res > 1e-6
print(f"\nH30c: (L_e7, L_e7, L_e7) in g? Rest {diag_res:.3f} (nein, wenn > 0); Fortsetzung von A = L_e7 ({fitA:.0e}):"
      f" B = {coB[0]:+.4f} L_e7 {coB[1]:+.4f} R_e7 (Rest {rB:.0e}), C = {coC[0]:+.4f} L_e7 {coC[1]:+.4f} R_e7 (Rest {rC:.0e});"
      f" tau-invariant: {not tau_inv} -> {'bestaetigt' if ok_c else 'widerlegt'}")
def kind(X):
    for nm, M in (("+L_e7", L7), ("-L_e7", -L7), ("+R_e7", R7), ("-R_e7", -R7)):
        if abs(X - M).max() < 1e-8: return nm
    return "Mischung"
invB = abs((1j*B)@(1j*B) - np.eye(8)).max(); invC = abs((1j*Cm)@(1j*Cm) - np.eye(8)).max()
kB, kC = kind(B), kind(Cm)
ok_d = not (kB in ("+L_e7", "-L_e7") and kC in ("+L_e7", "-L_e7"))
print(f"\nH30d: Platz 2: {kB} (iB Involution: {invB:.0e}), Platz 3: {kC} (iC Involution: {invC:.0e})"
      f" -> {'bestaetigt' if ok_d else 'widerlegt'}")
