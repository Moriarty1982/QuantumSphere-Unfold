"""k385 (Test H182): Erlaubt der Tausch J einen ladungsabhaengigen Massenterm bei den Quarks und verbietet ihn bei den Leptonen?
Vorab: Vorab_Notiz_H182_Ladung_trennt_Up_und_Down.md (Commit 70fdce1). Aufruf: python k385_test_h182.py > k385_out.txt"""
import itertools, numpy as np
from scipy.linalg import null_space, expm, block_diag
rng = np.random.default_rng(385)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
n = 8; e = np.eye(n); C = np.array([[mul(e[i], e[j]) for j in range(n)] for i in range(n)])
rows = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            r = np.zeros((n, n)); r[k, :] += C[i, j, :]; r[:, i] -= C[:, j, k]; r[:, j] -= C[i, :, k]; rows.append(r.ravel())
fx = np.zeros((n, n * n))
for k in range(n): fx[k, k * n + 7] = 1
st = null_space(np.vstack([np.array(rows), fx]), rcond=1e-9)
gens8 = [st[:, a].reshape(n, n) for a in range(st.shape[1])]
U = e[7]; J8 = np.array([mul(U, conj(e[i])) for i in range(n)]).T; K8 = np.diag([1.0] + [-1.0] * 7)
L8 = np.einsum('i,ijk->kj', U, C); R8 = np.einsum('j,ijk->ki', U, C)
Q0 = 0.5 * np.eye(n) - 1j / 6 * L8 - 1j / 3 * R8
# reelle 16-dim Darstellung von C (x) O: Psi = a + i b -> (a, b); komplex-lineare M -> diag(M, M)
cl = lambda M: block_diag(M, M)
gens = [cl(g) for g in gens8]; J = cl(J8); K = cl(K8)
sig = np.diag([1.0] * 8 + [-1.0] * 8)                                   # komplexe Konjugation von C
I16 = np.block([[np.zeros((8, 8)), -np.eye(8)], [np.eye(8), np.zeros((8, 8))]])   # Multiplikation mit i
def herm(H):                                                           # hermitesche 8x8 -> reelle symmetrische 16x16 Form Psi^dagger H Psi
    return np.block([[H.real, -H.imag], [H.imag, H.real]])
sing = [0, 7]; col = [1, 2, 3, 4, 5, 6]
r16 = lambda ix: ix + [i + 8 for i in ix]
print(f"dim su(3)_c = {len(gens8)}; Ladungen auf {{1, U}}: {np.round(np.sort(np.linalg.eigvals(Q0[np.ix_(sing, sing)]).real), 4)}; auf dem Farbblock: {np.round(np.sort(np.linalg.eigvals(Q0[np.ix_(col, col)]).real), 4)}")

print("\n== H182a (nicht blind): ladungsungerade hermitesche Form unter J ==")
Hodd = Q0 - 0.5 * np.eye(8)                                            # Q0 - 1/2: ungerade unter komplexer Konjugation (Q0 -> 1 - Q0)
Pc = np.zeros((8, 8)); Pc[col, col] = 1; Ps = np.zeros((8, 8)); Ps[sing, sing] = 1
Hc = herm(Pc @ Hodd @ Pc); Hs = herm(Ps @ Hodd @ Ps)
print(f"   unter komplexer Konjugation ungerade: |sig Hc sig + Hc| = {np.abs(sig @ Hc @ sig + Hc).max():.1e}, |sig Hs sig + Hs| = {np.abs(sig @ Hs @ sig + Hs).max():.1e}")
da = np.abs(J.T @ Hc @ J - Hc).max(); db = np.abs(J.T @ Hs @ J + Hs).max()
print(f"   Farbblock: |J^T Hc J - Hc| = {da:.1e} (invariant);  farblos: |J^T Hs J + Hs| = {db:.1e} (ungerade)")
print(f"   Oktonion-Konjugation: |K^T Hc K - Hc| = {np.abs(K.T @ Hc @ K - Hc).max():.1e}; |K^T Hs K + Hs| = {np.abs(K.T @ Hs @ K + Hs).max():.1e}")
print(f"   Farbe: max |g^T Hc + Hc g| = {max(np.abs(g.T @ Hc + Hc @ g).max() for g in gens):.1e}")
print("   Urteil H182a:", "BESTAETIGT" if da < 1e-12 and db < 1e-12 else "WIDERLEGT")
# antilineare Fortsetzung J_a = J o sig
Ja = J @ sig
print(f"   Bericht, antilineare Fortsetzung: Farbblock |Ja^T Hc Ja + Hc| = {np.abs(Ja.T @ Hc @ Ja + Hc).max():.1e} (ungerade); farblos |Ja^T Hs Ja - Hs| = {np.abs(Ja.T @ Hs @ Ja - Hs).max():.1e} (invariant)")

print("\n== H182b: Invarianten vom Grad 2 (SU(3)_c, Oktonion-Konjugation, J; komplex-linear) ==")
N = 16; idx = [(i, j) for i in range(N) for j in range(i, N)]; basis = []
for (i, j) in idx:
    B = np.zeros((N, N)); B[i, j] = B[j, i] = 1; basis.append(B)
def forms(fin):
    cons = [np.array([(g.T @ B + B @ g).ravel() for B in basis]).T for g in gens]
    cons += [np.array([(M.T @ B @ M - B).ravel() for B in basis]).T for M in fin]
    ns = null_space(np.vstack(cons), rcond=1e-9)
    return [sum(ns[k, a] * basis[k] for k in range(len(basis))) for a in range(ns.shape[1])]
def split(Qs):
    even = [Q + sig @ Q @ sig for Q in Qs]; odd = [Q - sig @ Q @ sig for Q in Qs]
    rk = lambda Ms, ix: int(np.linalg.matrix_rank(np.array([M[np.ix_(ix, ix)].ravel() for M in Ms]), tol=1e-9))
    rkx = lambda Ms: int(np.linalg.matrix_rank(np.array([M[np.ix_(r16(sing), r16(col))].ravel() for M in Ms]), tol=1e-9))
    return (rk(even, list(range(N))), rk(odd, list(range(N))), rk(odd, r16(sing)), rk(odd, r16(col)), rkx(odd), rk(even, r16(sing)), rk(even, r16(col)))
res = {}
for lab, fin in (("nur Farbe", []), ("Farbe + Konjugation", [K]), ("Farbe + J", [J]), ("Farbe + Konjugation + J", [K, J]), ("Farbe + Konjugation + J antilinear", [K, Ja])):
    Qs = forms(fin); res[lab] = Qs; s = split(Qs)
    print(f"   {lab:36s}: {len(Qs):2d} Formen; ladungsgerade {s[0]} (farblos {s[5]}, Farbe {s[6]}); ladungsungerade {s[1]} (farblos {s[2]}, Farbe {s[3]}, gemischt {s[4]})")
s = split(res["Farbe + Konjugation + J"])
vb = "BESTAETIGT" if s[3] >= 1 and s[2] == 0 else "WIDERLEGT"
print(f"   Urteil H182b: {vb} (ladungsungerade im Farbblock: {s[3]}, im Farblosen: {s[2]})")
Qs2 = res["Farbe + Konjugation + J"]
herm_cnt = int(np.linalg.matrix_rank(np.array([(Q + I16.T @ Q @ I16).ravel() for Q in Qs2]), tol=1e-9))
print(f"   davon hermitesch (invariant unter der Phase von C): {herm_cnt}")

print("\n== H182c: allgemeinstes invariantes Potential bis Grad 4 auf den Feldfamilien ==")
mons = list(itertools.combinations_with_replacement(range(N), 4)); MI = np.array(mons)
ev = lambda X: np.prod(X[:, MI], axis=2)                               # X: (m, 16) -> (m, 3876)
m = 5200; X = rng.normal(size=(m, N)); rws = []
els = []
for _ in range(m):
    r = rng.integers(0, 4)
    if r == 0: g = expm(sum(rng.normal() * G for G in gens))
    elif r == 1: g = K @ expm(sum(rng.normal() * G for G in gens))
    elif r == 2: g = J @ expm(sum(rng.normal() * G for G in gens))
    else: g = J @ K @ expm(sum(rng.normal() * G for G in gens))
    els.append(g)
GX = np.einsum('mij,mj->mi', np.array(els), X)
Amat = ev(GX) - ev(X)
sv = np.linalg.svd(Amat, compute_uv=False)
_, s_, vt = np.linalg.svd(Amat, full_matrices=True)
tol = 1e-8 * s_[0]; inv4 = vt[np.sum(s_ > tol):]
print(f"   Invarianten vom Grad 4: {inv4.shape[0]} (von {len(mons)} Monomen; Singulaerwerte um die Luecke: {s_[np.sum(s_ > tol) - 1]:.2e} / {(s_[np.sum(s_ > tol)] if np.sum(s_ > tol) < len(s_) else 0):.2e})")
# Probe der Invarianz an neuen Punkten
Xt = rng.normal(size=(50, N)); gt = [J @ K @ expm(sum(rng.normal() * G for G in gens)) for _ in range(50)]
print(f"   Probe an 50 neuen Punkten: max |P(gx) - P(x)| = {np.abs((ev(np.einsum('mij,mj->mi', np.array(gt), Xt)) - ev(Xt)) @ inv4.T).max():.1e}")
# Feldfamilien
w, V = np.linalg.eig(Q0[np.ix_(col, col)])
def nvec(q):
    v = V[:, np.argmin(np.abs(w - q))]; v = v / np.linalg.norm(v); z = np.zeros(8, dtype=complex); z[col] = v; return z
nD, nU = nvec(1 / 3), nvec(2 / 3)
real16 = lambda z: np.concatenate([z.real, z.imag])
ths = np.linspace(0.05, 1.5, 40)
def fam(nv): return np.array([real16(np.cos(t) * e[0].astype(complex) + np.sin(t) * nv) for t in ths])
FL = np.array([real16((np.cos(t) * e[0] + np.sin(t) * e[7]).astype(complex)) for t in ths])
FD, FU = fam(nD), fam(nU)
quad = lambda F: np.array([[x @ Q @ x for Q in Qs2] for x in F])       # (40, n2)
VL = np.hstack([quad(FL), ev(FL) @ inv4.T]); VD = np.hstack([quad(FD), ev(FD) @ inv4.T]); VU = np.hstack([quad(FU), ev(FU) @ inv4.T])
rank = lambda M: int(np.linalg.matrix_rank(M, tol=1e-8))
# (i) Lepton: Ableitung bei 45 Grad
h = 1e-5; lep = lambda t: real16((np.cos(t) * e[0] + np.sin(t) * e[7]).astype(complex))[None, :]
dq = np.array([(lep(np.pi / 4 + h)[0] @ Q @ lep(np.pi / 4 + h)[0] - lep(np.pi / 4 - h)[0] @ Q @ lep(np.pi / 4 - h)[0]) / (2 * h) for Q in Qs2])
d4 = ((ev(lep(np.pi / 4 + h)) - ev(lep(np.pi / 4 - h))) @ inv4.T / (2 * h)).ravel()
dmax = max(np.abs(dq).max(), np.abs(d4).max())
sym = np.abs(np.hstack([quad(FL), ev(FL) @ inv4.T]) - np.hstack([quad(np.array([lep(np.pi / 2 - t)[0] for t in ths])), ev(np.array([lep(np.pi / 2 - t)[0] for t in ths])) @ inv4.T])).max()
print(f"   (i) Leptonfeld: groesste Ableitung einer Invariante bei 45 Grad: {dmax:.1e}; V(theta) = V(pi/2 - theta) fuer jede Invariante: Abweichung {sym:.1e}; Funktionenraum Dimension {rank(VL)}")
# (ii) Quarkfelder
t = np.sin(ths)**2; T = np.vstack([np.ones_like(t), t, t**2]).T
fit = lambda M: np.abs(M - T @ np.linalg.lstsq(T, M, rcond=None)[0]).max()
print(f"   Quarkfelder: V ist Polynom vom Grad <= 2 in t = sin^2 theta (Restfehler d: {fit(VD):.1e}, u: {fit(VU):.1e})")
cD = np.linalg.lstsq(T, VD, rcond=None)[0]; cU = np.linalg.lstsq(T, VU, rcond=None)[0]          # (3, n_inv): Koeffizienten von 1, t, t^2
both = np.vstack([cD[1:], cU[1:]])                                    # (a_d, b_d, a_u, b_u) je Invariante
print(f"   Funktionenraum V_d: {rank(VD)}, V_u: {rank(VU)}, V_d - V_u: {rank(VD - VU)}; Rang von (a_d, b_d, a_u, b_u) ueber alle Invarianten: {rank(both)}")
vi = dmax < 1e-6; vii = rank(VD - VU) >= 1
print("   Urteil H182c:", "BESTAETIGT" if vi and vii else "WIDERLEGT", f"((i) {'erfuellt' if vi else 'verletzt'}, (ii) {'erfuellt' if vii else 'verletzt'})")

print("\n== H182d: Zaehlung und Daten ==")
rk4 = rank(both)
TH = {"d": (48.114, 0.039), "u": (52.207, 0.021)}
td, tu = (np.sin(np.radians(TH[k][0]))**2 for k in "du")
print(f"   V_q(t) = a_q t + b_q t^2 + konst., stationaer bei t* = -a_q / (2 b_q), Minimum fuer b_q > 0.")
print(f"   unabhaengige Kombinationen (a_d, b_d, a_u, b_u): {rk4}; unabhaengige Verhaeltnisse fuer die zwei Winkel: {min(2, rk4 - 2) if rk4 >= 2 else 0}")
print(f"   Daten verlangen a_d/b_d = {-2 * td:.4f} (theta_d = {TH['d'][0]}), a_u/b_u = {-2 * tu:.4f} (theta_u = {TH['u'][0]}); Unterschied {(-2 * tu) - (-2 * td):+.4f}")
# Zerlegung in ladungsgerade und -ungerade Anteile: a_q = A -+ C, b_q = B -+ D
r = lambda x: x                                                        # mit b_d = b_u = 1 normiert (nur zur Anschauung)
print(f"   Lesart mit D = 0 (gleicher Grad-4-Koeffizient B): A/B = {-(td + tu):.4f}, C/B = {-(tu - td):.4f}; |C/A| = {(tu - td) / (tu + td):.4f}")
if rk4 >= 4: print("   Urteil H182d: VERTRAEGLICH, KEINE BESTAETIGUNG (zwei freie Verhaeltnisse fuer zwei Messgroessen; stabile Minima mit b_d, b_u > 0 waehlbar)")

print("\n== Zusatz (nachtraeglich, nach dem Urteil zu H182b): Welche ladungsungeraden Formen sind das? ==")
odd = [Q - sig @ Q @ sig for Q in Qs2]
hpart = lambda Q: (Q + I16.T @ Q @ I16) / 2                            # hermitescher Anteil; Rest: bilinear (Typ Re/Im von Psi.Psi)
rk = lambda Ms, ix: int(np.linalg.matrix_rank(np.array([M[np.ix_(ix, ix)].ravel() for M in Ms]), tol=1e-9))
oh = [hpart(Q) for Q in odd]; ob = [Q - hpart(Q) for Q in odd]
print(f"   ladungsungerade und hermitesch: farblos {rk(oh, r16(sing))}, Farbe {rk(oh, r16(col))};  ladungsungerade und bilinear: farblos {rk(ob, r16(sing))}, Farbe {rk(ob, r16(col))}")
Bs = np.zeros((16, 16))
for i in sing: Bs[i, i + 8] = Bs[i + 8, i] = 1                          # Im(x0^2 + xU^2) = 2 (Re x0 Im x0 + Re xU Im xU)
inspan = np.linalg.lstsq(np.array([Q.ravel() for Q in Qs2]).T, Bs.ravel(), rcond=None)
print(f"   Im(x0^2 + xU^2) liegt im Raum der Invarianten: Rest {np.abs(np.array([Q.ravel() for Q in Qs2]).T @ inspan[0] - Bs.ravel()).max():.1e}")
P0 = real16((e[0] - 1j * e[7]).astype(complex) / np.sqrt(2)); P1 = real16((e[0] + 1j * e[7]).astype(complex) / np.sqrt(2))
q0v = [float(np.real(np.conj(v) @ Q0 @ v)) for v in ((e[0] - 1j * e[7]) / np.sqrt(2), (e[0] + 1j * e[7]) / np.sqrt(2))]
print(f"   Ladungs-Eigenzustaende im Farblosen (Q = {q0v[0]:.0f}, {q0v[1]:.0f}): Wert der Form {P0 @ Bs @ P0:+.1e}, {P1 @ Bs @ P1:+.1e}; auf reellen Feldern: 0")
print(f"   hermitesche Invarianten insgesamt: {herm_cnt} (|s|^2, |c|^2 und die ladungsungerade Form im Farbblock); im Farblosen gibt es keine ladungsungerade hermitesche Invariante.")
p0 = (e[0] - 1j * e[7]) / np.sqrt(2); p1 = (e[0] + 1j * e[7]) / np.sqrt(2)
print(f"   J tauscht die Ladungs-Eigenzustaende im Farblosen: |J P(Q=1) + i P(Q=0)| = {np.abs(J8 @ p0 + 1j * p1).max():.1e}, |J P(Q=0) - i P(Q=1)| = {np.abs(J8 @ p1 - 1j * p0).max():.1e}; jede J-Invariante gewichtet beide also gleich.")
