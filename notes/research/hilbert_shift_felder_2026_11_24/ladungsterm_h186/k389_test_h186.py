"""k389 (Test H186): ein einzelner Ladungsterm fuer drei Generationen gegen die Daten.
Vorab: Vorab_Notiz_H186_Ladungsterm_fuer_drei_Generationen.md (Commit c8ab85d).
Aufruf: python k389_test_h186.py > k389_out.txt"""
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(389)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
cj = np.diag([1.0] + [-1.0] * 7)
PAIRS = [(0, 1), (1, 2), (2, 0)]
def toW(v):                                                             # v reell oder komplex, 27 Koordinaten
    W = np.zeros((3, 3, 8), dtype=v.dtype)
    for i in range(3): W[i, i, 0] = v[i]
    for s, (i, j) in enumerate(PAIRS):
        x = v[3 + 8 * s: 11 + 8 * s]; W[i, j] = x; W[j, i] = cj @ x
    return W
def fromW(W): return np.concatenate([[W[i, i, 0] for i in range(3)]] + [W[i, j] for (i, j) in PAIRS])
mm = lambda X, Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
jo = lambda X, Y: 0.5 * (mm(X, Y) + mm(Y, X))
tr = lambda X: X[0, 0, 0] + X[1, 1, 0] + X[2, 2, 0]
def projU(W):
    Z = np.zeros_like(W); Z[:, :, 0] = W[:, :, 0]; Z[:, :, 7] = W[:, :, 7]; return Z
Pm = np.zeros((3, 3)); Pm[0, 1] = Pm[1, 2] = Pm[2, 0] = 1
Tm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1.0]])
lin = lambda f: np.array([f(col) for col in np.eye(27)]).T
MP = lin(lambda v: fromW(np.einsum('ij,jka,lk->ila', Pm, toW(v), Pm)))
MT = lin(lambda v: fromW(np.einsum('ij,jka,lk->ila', Tm, toW(v), Tm)))
MK = lin(lambda v: fromW(np.einsum('ija,ba->ijb', toW(v), cj))); MTau = MK @ MT
def W0(a, r, delta):
    v = np.zeros(27); v[:3] = a
    for s in range(3): v[3 + 8 * s] = r * np.cos(delta); v[3 + 8 * s + 7] = r * np.sin(delta)
    return v
# Farbe
rows = []
for i in range(8):
    for j in range(8):
        for k in range(8):
            r = np.zeros((8, 8)); r[k, :] += C[i, j, :]; r[:, i] -= C[:, j, k]; r[:, j] -= C[i, :, k]; rows.append(r.ravel())
fx = np.zeros((8, 64))
for k in range(8): fx[k, k * 8 + 7] = 1
st = null_space(np.vstack([np.array(rows), fx]), rcond=1e-9); g8 = [st[:, a].reshape(8, 8) for a in range(st.shape[1])]
colidx = [3 + 8 * s + c for s in range(3) for c in range(1, 7)]
sub = lambda M: M[np.ix_(colidx, colidx)]
LU = np.einsum('i,ijk->kj', e[7], C)[1:7, 1:7]                           # L_U auf einem Farbblock
RU = np.einsum('ijk,j->ki', C, e[7])[1:7, 1:7]
I2 = np.eye(2); J2 = np.array([[0, -1.0], [1, 0]])                       # Multiplikation mit i auf (A, B)
Gc = [np.kron(I2, np.kron(np.eye(3), g[1:7, 1:7])) for g in g8]
Pc = np.kron(I2, sub(MP)); Tauc = np.kron(I2, sub(MTau)); Cc = np.kron(np.diag([1.0, -1.0]), np.eye(18))
Ii = np.kron(J2, np.eye(18)); LUc = np.kron(I2, np.kron(np.eye(3), LU))
Qc = 0.5 * np.eye(36) + Ii @ LUc / 6                                     # Q0 = 1/2 + (i/6) L_U auf den Farbrichtungen

wq, Vq = np.linalg.eigh((Qc + Qc.T) / 2); E13, E23 = Vq[:, wq < 0.5], Vq[:, wq > 0.5]
LU8 = np.einsum('i,ijk->kj', e[7], C); RU8 = np.einsum('ijk,j->ki', C, e[7]); Dm = -1j / 6 * LU8 - 1j / 3 * RU8      # Q0 - 1/2
def Dop(W):
    v = fromW(W).astype(complex); o = np.zeros(27, dtype=complex)
    for s in range(3): o[3 + 8 * s: 11 + 8 * s] = Dm @ v[3 + 8 * s: 11 + 8 * s]
    return toW(o)
cb = np.conj; U = projU
def split(z, name): return [("Re " + name, lambda W, z=z: z(W).real), ("Im " + name, lambda W, z=z: z(W).imag)]
ref = lambda W: tr(jo(jo(W, cb(W)), U(W))).real                           # Referenz: Frequenzquadrat 2 (l_i + l_j), ladungsgerade
cand = [("c1  Re Tr Wq DW", lambda W: tr(jo(cb(W), Dop(W))).real)]
cand += [(f"c{2 + k}  " + n, f) for k, (n, f) in enumerate(split(lambda W: tr(jo(jo(cb(W), Dop(W)), U(W))), "Tr (Wq DW) Wu"))]
cand += [("c4  Re Tr (Wq DW) o (Wu Wuq)", lambda W: tr(jo(jo(cb(W), Dop(W)), jo(U(W), cb(U(W))))).real)]
cand += [(f"c{5 + k}  " + n, f) for k, (n, f) in enumerate(split(lambda W: tr(jo(jo(cb(W), Dop(W)), jo(U(W), U(W)))), "Tr (Wq DW) o Wu^2"))]
cand += [(f"c{7 + k}  " + n, f) for k, (n, f) in enumerate(split(lambda W: tr(jo(jo(cb(W), U(W)), jo(Dop(W), cb(U(W))))), "Tr (Wq Wu) o (DW Wuq)"))]
cand += [(f"c{9 + k}  " + n, f) for k, (n, f) in enumerate(split(lambda W: tr(jo(jo(cb(W), cb(U(W))), jo(Dop(W), U(W)))), "Tr (Wq Wuq) o (DW Wu)"))]
cand += [("c11 Re Tr (Wq DW) o (W Wq)", lambda W: tr(jo(jo(cb(W), Dop(W)), jo(W, cb(W)))).real)]
def hess(f, w0):
    def F(d):
        v = np.asarray(w0, dtype=complex).copy(); v[colidx] += d[:18] + 1j * d[18:]; return f(toW(v))
    def H1(h):
        Hh = np.zeros((36, 36)); E = np.eye(36) * h; f0 = F(np.zeros(36))
        for i in range(36):
            Hh[i, i] = (F(2 * E[i]) - 2 * f0 + F(-2 * E[i])) / (4 * h * h)
            for j in range(i + 1, 36):
                Hh[i, j] = Hh[j, i] = (F(E[i] + E[j]) - F(E[i] - E[j]) - F(E[j] - E[i]) + F(-E[i] - E[j])) / (4 * h * h)
        return Hh
    return (4 * H1(0.1) - H1(0.2)) / 3
def modes(Href):
    """Eigenraeume der Referenzform je Ladung, aufsteigend nach l_i + l_j: Generation 1, 2, 3."""
    out = []
    for E in (E13, E23):
        w, V = np.linalg.eigh(E.T @ Href @ E); out.append([E @ V[:, 6 * g: 6 * g + 6] for g in range(3)])
    return out
def shifts(H, md):
    Hc = (H + Ii.T @ H @ Ii) / 2; mix = np.abs(H - Hc).max(); vals = np.zeros((2, 3)); res = 0
    for q in range(2):
        for g in range(3):
            V = md[q][g]; vals[q, g] = np.trace(V.T @ Hc @ V) / 6; res = max(res, np.abs(Hc @ V - V * vals[q, g]).max())
    return vals, res, mix
vac = [(1.0, 1 / np.sqrt(2), 2.0 / 9.0), (1.3, 0.55, 0.31), (0.8, 0.7, 0.12), (1.1, 0.4, 0.45)]
def ls(a, r, d): return np.sort([a + 2 * r * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
print("== Kontrollen ==")
w0 = W0(*vac[0]); l0 = ls(*vac[0]); Href = hess(ref, w0); md0 = modes(Href); v, rs, mx = shifts(Href, md0)
print(f"   Eigenwerte des Vakuums l = {np.round(l0, 6)}; Referenzform: Frequenzquadrate {np.round(v[0], 5)} (Ladung 1/3), {np.round(v[1], 5)} (2/3); erwartet 2 (l_i + l_j) = {np.round([2 * (l0[0] + l0[1]), 2 * (l0[0] + l0[2]), 2 * (l0[1] + l0[2])], 5)}")
print("   Zuordnung (Setzung): Paar (e, mu) = 1. Generation, (e, tau) = 2., (mu, tau) = 3.")

print("\n== Kandidaten am Vakuum K = 2/3, delta = 2/9: Frequenzquadrate je Ladung und Generation ==")
tab = {}; allv = {}
for name, f in cand:
    per = []
    for iv, vc in enumerate(vac):
        wv = W0(*vc); mdv = md0 if iv == 0 else modes(hess(ref, wv)); per.append(shifts(hess(f, wv), mdv))
    vals, rs, mx = per[0]; odd = (vals[1] - vals[0]) / 2; even = (vals[1] + vals[0]) / 2; tab[name] = odd; allv[name] = per
    print(f"   {name:30s}: ungerade (Up - Down)/2 = {np.round(odd, 5)}; gerade = {np.round(even, 5)}; Rest {rs:.0e}; ladungsmischend {mx:.0e}", flush=True)

print("\n== Form der ungeraden Verschiebung als Funktion der l (vier Vakua gemeinsam) ==")
def feats(l, deg):
    prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]; rows = []
    for (i, j, k) in prs:
        if deg == 0: rows.append([1.0])
        elif deg == 1: rows.append([l[i] + l[j], l[k]])
        else: rows.append([l[i]**2 + l[j]**2, l[i] * l[j], l[k] * (l[i] + l[j]), l[k]**2])
    return np.array(rows)
fn = {0: ["1"], 1: ["(l_i + l_j)", "l_k"], 2: ["(l_i^2 + l_j^2)", "l_i l_j", "l_k (l_i + l_j)", "l_k^2"]}
degs = {"c1": 0, "c2": 1, "c3": 1}
for name, _ in cand:
    dg = degs.get(name.split()[0], 2); A = np.vstack([feats(ls(*vc), dg) for vc in vac]); y = np.concatenate([(p[0][1] - p[0][0]) / 2 for p in allv[name]])
    if np.abs(y).max() < 1e-10: print(f"   {name:30s}: null"); continue
    co, *_ = np.linalg.lstsq(A, y, rcond=None); rr = np.abs(A @ co - y).max()
    print(f"   {name:30s}: " + " ".join(f"{c:+.4f} {n}" for c, n in zip(co, fn[dg]) if abs(c) > 1e-8) + f"   (Rest {rr:.1e})")

print("\n== H186a: Rang der ungeraden Richtungen ==")
M = np.array([tab[n] for n, _ in cand]); sv = np.linalg.svd(M, compute_uv=False)
print(f"   Singulaerwerte: {np.round(sv, 5)}; relativ kleinster: {sv[-1] / sv[0]:.2e}")
rank = int(np.sum(sv / sv[0] > 1e-6))
print("   Urteil H186a:", "BESTAETIGT (Rang 3: Symmetrie und Grad legen die Richtung nicht fest)" if rank == 3 else f"WIDERLEGT (Rang {rank})")

print("\n== H186b: einzelne Kandidaten gegen die Daten (M_Z, k376) ==")
md_ = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd_ = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu_ = np.array([7.04e-6, 3.56e-3, 0.967]); su_ = np.array([0.15e-6, 0.06e-3, 0.004])
NMC = 200000; Sd = rng.normal(md_, sd_, size=(NMC, 3)); Su = rng.normal(mu_, su_, size=(NMC, 3))
les = {"X = sqrt(m)": lambda m: np.sqrt(m), "X = m": lambda m: m, "X = m^2": lambda m: m**2}
best = (1e9, None); hit = []
for ln, fx in les.items():
    d0 = fx(mu_) - fx(md_); ds = fx(Su) - fx(Sd); r0 = d0[:2] / d0[2]; rs_ = ds[:, :2] / ds[:, 2:3]; sg = rs_.std(axis=0)
    print(f"   {ln}: Daten r1 = {r0[0]:+.6f} +- {sg[0]:.6f}, r2 = {r0[1]:+.6f} +- {sg[1]:.6f}")
    for name, _ in cand:
        o = tab[name]
        if abs(o[2]) < 1e-10: print(f"      {name:30s}: Verschiebung der 3. Generation null, kein Verhaeltnis"); continue
        r = o[:2] / o[2]; z = (r - r0) / sg; zz = np.abs(z).max()
        print(f"      {name:30s}: r1 = {r[0]:+.5f}, r2 = {r[1]:+.5f}; Abstand {z[0]:+.1f} sigma, {z[1]:+.1f} sigma")
        if zz < best[0]: best = (zz, f"{name.strip()} mit {ln}")
        if zz < 3: hit.append((name, ln))
print(f"   kleinster groesster Abstand: {best[0]:.1f} sigma ({best[1]})")
print("   Urteil H186b:", f"BESTAETIGT ({hit}); 33 Paare verglichen, eigener Vorab-Test noetig" if hit else "WIDERLEGT (kein Kandidat trifft beide Verhaeltnisse innerhalb von 3 sigma)")

print("\n== Bericht (nachtraeglich): andere Zuordnungen der Generationen, nur Lesart X = sqrt(m) ==")
import itertools
d0 = np.sqrt(mu_) - np.sqrt(md_); ds = np.sqrt(Su) - np.sqrt(Sd)
for perm in itertools.permutations(range(3)):
    if perm == (0, 1, 2): continue
    bz = (1e9, None)
    for name, _ in cand:
        o = tab[name][list(perm)]
        if abs(o[2]) < 1e-10: continue
        r = o[:2] / o[2]; z = np.abs((r - d0[:2] / d0[2]) / (ds[:, :2] / ds[:, 2:3]).std(axis=0)).max()
        if z < bz[0]: bz = (z, name.strip())
    print(f"   Paare in der Reihenfolge {perm}: kleinster Abstand {bz[0]:.1f} sigma ({bz[1]})")

print("\n== Zusatz (nachtraeglich, Erkundung): Daten im Raum der erlaubten Verschiebungen ==")
print("   Alle Kandidaten haengen nur an (l_i, l_j) des Paars, nicht an l_k. Basis: 1, (l_i + l_j), l_i l_j, (l_i^2 + l_j^2).")
prs = [(0, 1), (0, 2), (1, 2)]
B3 = np.array([[1.0, l0[i] + l0[j], l0[i] * l0[j]] for (i, j) in prs]); q2 = np.array([l0[i]**2 + l0[j]**2 for (i, j) in prs])
for ln, fx in les.items():
    d0 = fx(mu_) - fx(md_); co = np.linalg.solve(B3, d0 / d0[2]); pure = B3[:, 2] / B3[2, 2]
    print(f"   {ln}: Daten (auf die 3. Generation normiert) = {co[0]:+.4f} * 1 {co[1]:+.4f} * (l_i + l_j) {co[2]:+.4f} * l_i l_j")
print(f"   reines l_i l_j (= 3 c7 - 1,5 c4): r1 = {pure[0]:+.5f}, r2 = {pure[1]:+.5f}; reines (l_i^2 + l_j^2): r1 = {q2[0] / q2[2]:+.5f}, r2 = {q2[1] / q2[2]:+.5f}")
d0 = np.sqrt(mu_) - np.sqrt(md_); ds = np.sqrt(Su) - np.sqrt(Sd); sg = (ds[:, :2] / ds[:, 2:3]).std(axis=0); z = (pure[:2] - d0[:2] / d0[2]) / sg
print(f"   reines l_i l_j gegen X = sqrt(m): Abstand {z[0]:+.0f} sigma, {z[1]:+.0f} sigma; relativ zu r2 der Daten: {pure[1] / (d0[1] / d0[2]):.2f}-fach")
