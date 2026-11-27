"""k390 (Test H187): Terme mit Adjunkter und Determinante der Albert-Algebra gegen die sechs Quarkmassen.
Vorab: Vorab_Notiz_H187_Adjunkte_und_Determinante_gegen_sechs_Quarkmassen.md (Commit beaa6ae).
Aufruf: python k390_test_h187.py > k390_out.txt"""
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(390)
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

I3 = np.zeros((3, 3, 8)); I3[0, 0, 0] = I3[1, 1, 0] = I3[2, 2, 0] = 1
def cross(A, B): return jo(A, B) - 0.5 * tr(A) * B - 0.5 * tr(B) * A + 0.5 * (tr(A) * tr(B) - tr(jo(A, B))) * I3
def sharp(A): return cross(A, A)
cand = [
 ("a1 Re Tr W# Wq", lambda W: tr(jo(sharp(W), cb(W))).real),
 ("a2 Tr W# Wq#", lambda W: tr(jo(sharp(W), sharp(cb(W)))).real),
 ("a3 Tr (W x Wq) Wu", lambda W: tr(jo(cross(W, cb(W)), U(W))).real),
 ("a4 Tr (W x Wq) (Wu Wuq)", lambda W: tr(jo(cross(W, cb(W)), jo(U(W), cb(U(W))))).real),
 ("a5 Tr (W x Wq) Wu#", lambda W: tr(jo(cross(W, cb(W)), sharp(U(W)))).real),
 ("a6 Tr (W x Wq)^2", lambda W: tr(jo(cross(W, cb(W)), cross(W, cb(W)))).real),
 ("a7 Tr (W x Wu) (Wq x Wuq)", lambda W: tr(jo(cross(W, U(W)), cross(cb(W), cb(U(W))))).real),
 ("a8 Re Tr W# Wuq#", lambda W: tr(jo(sharp(W), sharp(cb(U(W))))).real),
 ("d1 Re Tr (Wq x DW) Wu", lambda W: tr(jo(cross(cb(W), Dop(W)), U(W))).real),
 ("d2 Re Tr (Wq x DW) (Wu Wuq)", lambda W: tr(jo(cross(cb(W), Dop(W)), jo(U(W), cb(U(W))))).real),
 ("d3 Re Tr (Wq x DW) Wu#", lambda W: tr(jo(cross(cb(W), Dop(W)), sharp(U(W)))).real),
 ("d4 Re Tr (DW x Wu) (Wq x Wuq)", lambda W: tr(jo(cross(Dop(W), U(W)), cross(cb(W), cb(U(W))))).real),
]
print("== Kontrollen ==")
Xr = toW(rng.normal(size=27) + 0j); print(f"   W o W# = det(W) 1: Abweichung {np.abs(jo(Xr, sharp(Xr)) - tr(jo(Xr, sharp(Xr))) / 3 * I3).max():.1e}; Adjunkte der Diagonale (2, 3, 5): {np.round([sharp(toW(np.array([2, 3, 5.] + [0] * 24)))[i, i, 0].real for i in range(3)], 6)}")
w0 = W0(*vac[0]); l0 = ls(*vac[0]); mds = [modes(hess(ref, W0(*vc))) for vc in vac]
print(f"   Eigenwerte des Vakuums l = {np.round(l0, 6)}")
prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]; fnames = ["1", "(l_i + l_j)", "l_k", "(l_i^2 + l_j^2)", "l_i l_j", "l_k (l_i + l_j)", "l_k^2"]
def feats(l): return np.array([[1.0, l[i] + l[j], l[k], l[i]**2 + l[j]**2, l[i] * l[j], l[k] * (l[i] + l[j]), l[k]**2] for (i, j, k) in prs])
A7 = np.vstack([feats(ls(*vc)) for vc in vac])
def show(co): return " ".join(f"{c:+.4f} {n}" for c, n in zip(co, fnames) if abs(c) > 1e-8) or "0"
print("\n== Schritt 1 (ohne Daten): Funktion des Paars je Kandidat (vier Vakua gemeinsam) ==")
R = {}
def addR(co, src):
    if np.abs(co).max() < 1e-9: return
    v = co / np.abs(co).max(); v = v * np.sign(v[np.argmax(np.abs(v))]); key = tuple(np.round(v, 6))
    R.setdefault(key, []).append(src)
for name, f in cand:
    ev, od, rs_, mx_ = [], [], 0, 0
    for vc, md in zip(vac, mds):
        vals, rs, mx = shifts(hess(f, W0(*vc)), md); ev.append((vals[1] + vals[0]) / 2); od.append((vals[1] - vals[0]) / 2); rs_ = max(rs_, rs); mx_ = max(mx_, mx)
    for lab, y in (("gerade", np.concatenate(ev)), ("ungerade", np.concatenate(od))):
        if np.abs(y).max() < 1e-9: continue
        co, *_ = np.linalg.lstsq(A7, y, rcond=None); co[np.abs(co) < 1e-9] = 0; rr = np.abs(A7 @ co - y).max()
        print(f"   {name:30s} {lab:8s}: {show(co)}   (Rest {rr:.1e}; Eigenrest {rs_:.0e}; ladungsmischend {mx_:.0e})", flush=True)
        if rr < 1e-9: addR(co, name.split()[0])
for co, src in (([1, 0, 0, 0, 0, 0, 0], "H184/H186"), ([0, 1, 0, 0, 0, 0, 0], "H184/H186"), ([0, 0, 0, 1, 0, 0, 0], "H186"), ([0, 0, 0, 1, 2, 0, 0], "H186"), ([0, 0, 0, 0, 0, 0, 1], "H184"), ([0, 0, 0, 0, 0, 1, 0], "H184")):
    addR(np.array(co, float), src)
keys = list(R); print(f"\n   Funktionsmenge R ({len(keys)} Funktionen):")
for n_, k in enumerate(keys): print(f"      f{n_ + 1}: {show(np.array(k))}   [{', '.join(sorted(set(R[k])))}]")
pure_prod = any(np.allclose(np.abs(k), [0, 0, 0, 0, 1, 0, 0]) for k in keys); only_lk = any(np.allclose(np.array(k)[[0, 1, 3, 4, 5]], 0) and (abs(k[2]) > 0 or abs(k[6]) > 0) for k in keys)
print("   Urteil H187a:", "BESTAETIGT" if pure_prod and only_lk else "WIDERLEGT", f"(reines l_i l_j: {pure_prod}; Funktion von l_k allein: {only_lk})")

print("\n== Schritt 2: gegen die sechs Massen (M_Z, k376) ==")
F0 = feats(l0); FR = np.array([F0 @ np.array(k) for k in keys])                       # (n, 3) in Paarordnung (e mu), (e tau), (mu tau)
md_ = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd_ = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu_ = np.array([7.04e-6, 3.56e-3, 0.967]); su_ = np.array([0.15e-6, 0.06e-3, 0.004])
les = {"X = sqrt(m)": (np.sqrt, lambda m: 0.5 / np.sqrt(m)), "X = m": (lambda m: m, lambda m: np.ones_like(m)), "X = m^2": (lambda m: m**2, lambda m: 2 * m)}
zu = {"A": [0, 1, 2], "B": [2, 1, 0]}
def single(X, sX, Fm):
    """groesster Abstand der zwei Verhaeltnisse je Funktion."""
    r = X[:2] / X[2]; sr = np.abs(r) * np.sqrt((sX[:2] / X[:2])**2 + (sX[2] / X[2])**2); out = []
    for f in Fm:
        out.append(np.inf if abs(f[2]) < 1e-12 else np.abs((f[:2] / f[2] - r) / sr).max())
    return np.array(out)
def double(X, sX, Fm):
    n = len(Fm); out = np.full((n, n), np.inf)
    for a in range(n):
        for b in range(a + 1, n):
            c = np.cross(Fm[a], Fm[b]); nc = np.linalg.norm(c)
            if nc < 1e-9 * np.linalg.norm(Fm[a]) * np.linalg.norm(Fm[b]): continue
            out[a, b] = abs(c @ X) / np.sqrt(np.sum(c**2 * sX**2))
    return out
def search(mu, su, md, sd, verbose=False):
    hb = hc = False; best = []
    for ln, (fx, dfx) in les.items():
        for zn, perm in zu.items():
            Fm = FR[:, perm]; res = []
            for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
                X = fx(m); sX = np.abs(dfx(m)) * s; z1 = single(X, sX, Fm); z2 = double(X, sX, Fm); ia = np.unravel_index(np.argmin(z2), z2.shape)
                res.append((nm, z1.min(), int(np.argmin(z1)), z2.min(), ia))
            hb |= all(r[1] < 3 for r in res); hc |= all(r[3] < 3 for r in res)
            if verbose:
                print(f"   {ln}, Zuordnung {zn}: " + "; ".join(f"{r[0]}: eine Funktion f{r[2] + 1} {r[1]:.1f} sigma, zwei Funktionen (f{r[4][0] + 1}, f{r[4][1] + 1}) {r[3]:.2f} sigma" for r in res))
    return hb, hc
hb, hc = search(mu_, su_, md_, sd_, verbose=True)
n = len(keys); print(f"   verglichen: {n} Funktionen, {n * (n - 1) // 2} Paare, je 3 Lesarten und 2 Zuordnungen, je Sektor")
print("   Urteil H187b:", "BESTAETIGT" if hb else "WIDERLEGT (keine einzelne Funktion je Sektor trifft beide Verhaeltnisse in beiden Sektoren)")
NF = 2000; cb_ = cc_ = 0
for _ in range(NF):
    fake = []
    for s, m in ((su_, mu_), (sd_, md_)):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5); mf = np.array([m1, m2, 1.0]); fake += [mf, mf * s / m]
    b_, c_ = search(fake[0], fake[1], fake[2], fake[3]); cb_ += b_; cc_ += c_
print(f"   Zufallskontrolle ({NF} erfundene Datensaetze): Treffer mit einer Funktion {cb_ / NF:.2%}, mit zwei Funktionen {cc_ / NF:.2%}")
if not hc: print("   Urteil H187c: WIDERLEGT (kein Paar von Funktionen trifft beide Sektoren innerhalb von 3 sigma)")
elif cc_ / NF < 0.05: print("   Urteil H187c: BESTAETIGT als Kandidat (Treffer, Zufallsquote unter 5 %); eigener Vorab-Test noetig")
else: print("   Urteil H187c: OHNE URTEIL (Treffer, aber mit Zufall vertraeglich)")
