"""k378 (Erkundung, nicht blind): Farbanteil aus der Farbsymmetrie; wirkt die Farbrichtung auf die Phase delta?
Aufruf: python k378_farbanteil_und_delta.py > k378_out.txt"""
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(20261126)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8)
C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])      # C[i, j, k]: e_i e_j = sum_k C_ijk e_k

print("== 1. Farbanteil aus der Farbsymmetrie (Derivationen von O, die e7 festhalten) ==")
# D (8x8, D[k, i] = Komponente k von D(e_i)); Bedingung D(e_i e_j) = D(e_i) e_j + e_i D(e_j)
rows = []
for i in range(8):
    for j in range(8):
        for k in range(8):
            r = np.zeros((8, 8))
            r[k, :] += C[i, j, :]                        # D(e_i e_j)_k = sum_m C_ijm D[k, m]
            for m in range(8):
                r[m, i] -= C[m, j, k]                    # (D(e_i) e_j)_k = sum_m D[m, i] C_mjk
                r[m, j] -= C[i, m, k]                    # (e_i D(e_j))_k
            rows.append(r.ravel())
A = np.array(rows)
g2 = null_space(A, rcond=1e-10)
fix7 = np.zeros((8, 64))
for k in range(8): fix7[k, k * 8 + 7] = 1                # D(e7) = 0
su3 = null_space(np.vstack([A, fix7]), rcond=1e-10)
print(f"   dim Der(O) = {g2.shape[1]} (g2);  davon mit D(e7) = 0: {su3.shape[1]} (su(3)_c)")
gens = [su3[:, a].reshape(8, 8) for a in range(su3.shape[1])]
inv = null_space(np.vstack(gens), rcond=1e-10)
supp = sorted(set(int(i) for i in np.argwhere(np.abs(inv) > 1e-10)[:, 0]))
print(f"   gemeinsamer Kern aller Farbgeneratoren: Dimension {inv.shape[1]}, getragen von den Einheiten {supp} (also genau 1 und e7)")
cas = sum(-g @ g for g in gens); ev = np.round(np.linalg.eigvalsh((cas + cas.T) / 2), 8)
print(f"   Casimir-Eigenwerte (bis auf Normierung): {sorted(set(ev))} mit Vielfachheiten {[int((ev == v).sum()) for v in sorted(set(ev))]}: 1 + 1 + 6 (= 3 + 3-quer)")
print("   Folge (Schur): Ein Feld, das als Farbtriplett transformiert, liegt ganz in e1..e6. Fuer beide Quarktypen ist sin^2 alpha = 1; einen")
print("   gebrochenen Farbanteil (R1, R2 aus H178) gibt es fuer ein Farbmultiplett nicht.")
print("   Im Potential aus H178 (V = A q + B q^2 + kappa p) ist dann xU = 0 und sin^2 theta = -A/(2B) fuer beide Quarktypen gleich.")
td, tu = np.sin(np.radians(48.114))**2, np.sin(np.radians(52.207))**2
print(f"   Gemessen: sin^2 theta_d = {td:.4f}, sin^2 theta_u = {tu:.4f}. Mit reiner Farbe braucht es also je Quarktyp ein eigenes Verhaeltnis A/B: {-2*td:.4f} (d), {-2*tu:.4f} (u).")

print("\n== 2. Wirkt die Farbrichtung auf delta? Kubischer Term t = Re((x1 x2) x3) der Albert-Algebra ==")
def unit_im(v):
    z = np.zeros(8); z[1:] = v / np.linalg.norm(v); return z
def t3(x1, x2, x3): return mul(mul(x1, x2), x3)[0]
mx = 0
for _ in range(2000):
    n = unit_im(rng.normal(size=7)); ph = rng.uniform(0, 2 * np.pi); u = np.cos(ph) * e[0] + np.sin(ph) * n
    mx = max(mx, abs(t3(u, u, u) - np.cos(3 * ph)))
print(f"   Gleiche Eintraege x_i = cos(phi) + sin(phi) n, n beliebige imaginaere Richtung (2000 Zufallsfaelle): |t - cos(3 phi)| <= {mx:.1e}")
print("   Folge: Zeigen alle drei Nebendiagonalen in dieselbe Richtung, haengt der kubische Term nur von phi ab, nicht von der Richtung. Farbe verschiebt delta dann nicht.")
mx = 0
for _ in range(2000):
    ns = [unit_im(rng.normal(size=7)) for _ in range(3)]; ph = rng.uniform(0, 2 * np.pi)
    xs = [np.cos(ph) * e[0] + np.sin(ph) * n for n in ns]
    G = sum(ns[i] @ ns[j] for i, j in ((0, 1), (1, 2), (0, 2))); Phi = -t3(*ns)        # Phi = assoziative 3-Form
    mx = max(mx, abs(t3(*xs) - (np.cos(ph)**3 - np.cos(ph) * np.sin(ph)**2 * G - np.sin(ph)**3 * Phi)))
print(f"   Verschiedene Richtungen n_i: t = cos^3 phi - cos phi sin^2 phi (n1.n2 + n2.n3 + n1.n3) - sin^3 phi Phi(n1, n2, n3); Abweichung <= {mx:.1e}")
print("   Beispiele (n_i = cos(alpha) e7 + sin(alpha) c_i, Farbrichtungen c_i paarweise senkrecht):")
for name, cs in (("c = (e1, e2, e3) (assoziatives Tripel)", (1, 2, 3)), ("c = (e1, e2, e4)", (1, 2, 4)), ("c = (e1, e2, e5)", (1, 2, 5)), ("c = (e1, e2, e6)", (1, 2, 6))):
    out = []
    for s2 in (0.0, 1 / 3, 2 / 3, 1.0):
        al = np.arcsin(np.sqrt(s2)); ns = [np.cos(al) * e[7] + np.sin(al) * e[c] for c in cs]
        G = sum(ns[i] @ ns[j] for i, j in ((0, 1), (1, 2), (0, 2))); Phi = -t3(*ns)
        # Nullstelle von t in phi (masseloser Punkt des kubischen Terms), erste positive
        f = lambda p: np.cos(p)**3 - np.cos(p) * np.sin(p)**2 * G - np.sin(p)**3 * Phi
        ps = np.linspace(1e-6, np.pi, 200001); v = f(ps); k = np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]
        out.append(f"sin^2 a = {s2:.2f}: G = {G:+.3f}, Phi = {Phi:+.3f}, erste Nullstelle phi = {ps[k[0]]:.4f}")
    print(f"   {name}: " + "; ".join(out))
print("   Bei alpha = 0 ist die Nullstelle pi/6 = 0,5236 (cos 3 phi = 0). Mit Farbanteil und verschiedenen Farbrichtungen wandert sie.")

print("\n== 3. Je Sektor: Abstand vom masselosen Punkt (kleinste Wurzel null) ==")
for nm, rho, d in (("e", 1.0, 0.222222), ("d", 1.11506, 0.100129), ("u", 1.28952, 0.051806)):
    d0 = np.arccos(-1 / (np.sqrt(2) * rho)) - 2 * np.pi / 3
    print(f"   {nm}: rho = {rho:.5f}, masseloser Punkt delta0 = {d0:.6f}, gemessen delta = {d:.6f}, Abstand x = {d0 - d:.6f}, x/delta0 = {(d0 - d)/d0:.4f}")
print("   Lesart: x misst nur, wie klein die leichteste Masse ist (sqrt(m1)/Summe); es ist keine neue Groesse.")
