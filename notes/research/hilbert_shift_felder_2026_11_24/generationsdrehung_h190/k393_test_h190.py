"""k393 (Test H190): Vakuum mit Drehung in den Generationen und die Quarkmassen.
Vorab: Vorab_Notiz_H190_Drehung_in_den_Generationen.md (Commit d918623).
Aufruf: python k393_test_h190.py > k393_out.txt"""
import itertools
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(393)
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
def toW(v):
    v = np.asarray(v, dtype=complex); W = np.zeros((3, 3, 8), dtype=complex)
    for i in range(3): W[i, i, 0] = v[i]
    for s, (i, j) in enumerate(PAIRS):
        x = v[3 + 8 * s: 11 + 8 * s]; W[i, j] = x; W[j, i] = cj @ x
    return W
mm = lambda X, Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
jo = lambda X, Y: 0.5 * (mm(X, Y) + mm(Y, X))
tr = lambda X: X[0, 0, 0] + X[1, 1, 0] + X[2, 2, 0]
def projU(W):
    Z = np.zeros_like(W); Z[:, :, 0] = W[:, :, 0]; Z[:, :, 7] = W[:, :, 7]; return Z
N = lambda X: np.sum(np.abs(X)**2)                                      # hermitesche Norm
ip = lambda X, Y: np.sum((np.conj(X) * Y).real)
def assoc(X, Y, Z): return mm(mm(X, Y), Z) - mm(X, mm(Y, Z))
def W0(a, r, delta):
    v = np.zeros(27); v[:3] = a
    for s in range(3): v[3 + 8 * s] = r * np.cos(delta); v[3 + 8 * s + 7] = r * np.sin(delta)
    return v
colidx = [3 + 8 * s + c for s in range(3) for c in range(1, 7)]
LU8 = np.einsum('i,ijk->kj', e[7], C); LU = LU8[1:7, 1:7]
I2 = np.eye(2); J2 = np.array([[0, -1.0], [1, 0]])
Ii = np.kron(J2, np.eye(18)); LUc = np.kron(I2, np.kron(np.eye(3), LU)); Qc = 0.5 * np.eye(36) + Ii @ LUc / 6
wq, Vq = np.linalg.eigh((Qc + Qc.T) / 2); E13, E23 = Vq[:, wq < 0.5], Vq[:, wq > 0.5]
def colW(d):
    v = np.zeros(27, dtype=complex); v[colidx] = d[:18] + 1j * d[18:]; return toW(v)
ref = lambda W: tr(jo(jo(W, np.conj(W)), projU(W))).real
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
def quadform(g):
    """Matrix einer exakt quadratischen Form auf den 36 Farbrichtungen (Polarisation)."""
    E = np.eye(36); d = np.array([g(colW(E[a])) for a in range(36)]); M = np.diag(d)
    for a in range(36):
        for b in range(a + 1, 36): M[a, b] = M[b, a] = (g(colW(E[a] + E[b])) - d[a] - d[b]) / 2
    return M
vac0 = (1.0, 1 / np.sqrt(2), 2.0 / 9.0)
def ls(a, r, d): return np.sort([a + 2 * r * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
def fromW(W): return np.concatenate([[W[i, i, 0] for i in range(3)]] + [W[i, j] for (i, j) in PAIRS])
prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]                                   # Moden g = 0, 1, 2 gehoeren zu den Paaren (0,1), (0,2), (1,2) der Eigenrichtungen
l0 = ls(*vac0); w0 = W0(*vac0)

print("== H190a (nicht blind): Drehung in einer Eigenebene, Wirkung auf die Farbschwingungen ==", flush=True)
a_, r_, d_ = vac0; M0 = a_ * np.eye(3, dtype=complex)
for (i, j) in PAIRS: M0[i, j] = r_ * np.exp(1j * d_); M0[j, i] = r_ * np.exp(-1j * d_)
ev, V = np.linalg.eigh(M0); print(f"   Eigenwerte des Vakuums l = {np.round(ev, 6)}")
def Tmat(p, q):
    T0 = np.zeros((3, 3), dtype=complex); T0[p, q] = 1; T0[q, p] = -1; Tc = V @ T0 @ V.conj().T; T = np.zeros((3, 3, 8), dtype=complex); T[:, :, 0] = Tc.real; T[:, :, 7] = Tc.imag; return T
def DT(T, W): return mm(T, W) - mm(W, T)
md = modes(hess(ref, w0)); Bm = [np.hstack([md[q][g] for g in range(3)]) for q in range(2)]       # je Ladung 18 Spalten, nach Moden geordnet
X = toW(rng.normal(size=27)); Y = toW(rng.normal(size=27)); ok_a = True; Dc = {}
for g, (p, q, k) in enumerate(prs):
    T = Tmat(p, q); der = np.abs(DT(T, jo(X, Y)) - jo(DT(T, X), Y) - jo(X, DT(T, Y))).max()
    vacmove = np.abs(fromW(DT(T, toW(w0)))).max(); M = np.zeros((36, 36)); leak = 0
    for a in range(36):
        Wd = DT(T, colW(np.eye(36)[a])); v = fromW(Wd); M[:, a] = np.concatenate([v[colidx].real, v[colidx].imag]); v2 = v.copy(); v2[colidx] = 0
        leak = max(leak, np.abs(v2).max(), np.abs(Wd - toW(v)).max())
    Dc[g] = M; com = max(np.abs(M @ Ii - Ii @ M).max(), np.abs(M @ Qc - Qc @ M).max()); asym = np.abs(M + M.T).max(); line = []
    for qn, Bq in zip(("1/3", "2/3"), Bm):
        Mb = Bq.T @ M @ Bq; blk = np.array([[np.linalg.norm(Mb[6 * x: 6 * x + 6, 6 * y: 6 * y + 6]) / np.sqrt(6) for y in range(3)] for x in range(3)])
        others = [x for x in range(3) if x != g]; sub = np.ix_([6 * x + c for x in others for c in range(6)], [6 * x + c for x in others for c in range(6)])
        sq = np.abs((Mb @ Mb)[sub] + np.eye(12)).max(); line.append(f"Ladung {qn}: Blocknormen {np.round(blk, 6).tolist()}, |D^2 + 1| auf den zwei anderen {sq:.1e}")
        expb = np.zeros((3, 3)); expb[others[0], others[1]] = expb[others[1], others[0]] = 1; ok_a &= np.abs(blk - expb).max() < 1e-8 and sq < 1e-8
    ok_a &= max(der, leak, com, asym) < 1e-8
    print(f"   Ebene der Eigenrichtungen ({p}, {q}): Derivation {der:.1e}; bewegt das Vakuum (|D W0| = {vacmove:.3f}); bleibt in den Farbrichtungen {leak:.1e}; vertauscht mit i und Ladung {com:.1e}; antisymmetrisch {asym:.1e}")
    for s in line: print("      " + s)
om = 0.83; hq = np.array([[0.9, 2.3, 4.1], [1.4, 2.9, 5.2]]); H = sum(hq[q, g] * md[q][g] @ md[q][g].T for q in range(2) for g in range(3)); dv = 0
def spec(h, g, w):
    """Frequenzquadrate: Mode g ungekoppelt, die zwei anderen gyroskopisch gekoppelt. h (3,), w = omega^2."""
    o = [x for x in range(3) if x != g]; ha, hb = h[o[0]], h[o[1]]; s = (ha + hb) / 2 + w; dsc = (ha - hb)**2 / 4 + 2 * w * (ha + hb)
    return np.array([h[g], s - np.sqrt(dsc), s + np.sqrt(dsc)]) if dsc >= 0 else np.array([np.nan] * 3)
for g in range(3):
    Msys = np.block([[np.zeros((36, 36)), np.eye(36)], [-(H + om**2 * Dc[g] @ Dc[g]), -2 * om * Dc[g]]]); lam = np.linalg.eigvals(Msys); num = np.sort(np.abs(lam.imag)**2)
    pred = np.sort(np.concatenate([np.repeat(spec(hq[q], g, om**2), 12) for q in range(2)])); dv = max(dv, np.abs(num - pred).max(), np.abs(lam.real).max())
print(f"   Bewegungsgleichung d'' + 2 omega D d' + omega^2 D^2 d + H d = 0, Beispiel omega = {om}, h = {hq.tolist()}: Frequenzquadrate gegen die Formel, groesste Abweichung {dv:.1e}")
ok_a &= dv < 1e-8
print("   Urteil H190a:", "BESTAETIGT (nicht blind): Formel fuer h_c, Omega^2_+- gilt im vollen Modell, fuer beide Ladungen gleich" if ok_a else "WIDERLEGT")

print("\n== H190b, c: gegen die sechs Massen (M_Z, k376) ==", flush=True)
import sys
from scipy.optimize import minimize_scalar
Rdef = [("l_k", lambda i, j, k: k), ("l_k^2", lambda i, j, k: k * k), ("l_i l_j", lambda i, j, k: i * j), ("l_i l_j - l_k^2/2", lambda i, j, k: i * j - k * k / 2),
        ("1", lambda i, j, k: 1.0), ("l_i + l_j", lambda i, j, k: i + j), ("l_i^2 + l_j^2", lambda i, j, k: i * i + j * j),
        ("(l_i^2 + l_j^2)/2 + l_i l_j", lambda i, j, k: (i * i + j * j) / 2 + i * j), ("l_k (l_i + l_j)", lambda i, j, k: k * (i + j))]
FR = np.array([[f(l0[i], l0[j], l0[k]) for (i, j, k) in prs] for _, f in Rdef])
combos = [(n, s, g) for n in range(9) for s in (1, -1) for g in range(3)]
def cname(c): return f"{'+' if c[1] > 0 else '-'}f{c[0] + 1} ({Rdef[c[0]][0]}), Ebene {prs[c[2]][:2]}"
def ratios(c, w):
    sp = np.sort(spec(c[1] * FR[c[0]], c[2], w))
    return (sp[0] / sp[2], sp[1] / sp[2]) if np.all(np.isfinite(sp)) and sp[0] > 0 else (np.nan, np.nan)
def grid(c):
    h = c[1] * FR[c[0]]; o = [x for x in range(3) if x != c[2]]; sc = np.abs(h).max(); ws = [np.array([0.0]), sc * 10 ** np.arange(-8, 8, 0.004)]
    for t in (h[o[0]], h[o[1]]):
        if t > 0:
            u = 10 ** np.arange(-10, 0, 0.005); ws += [t * (1 - u), t * (1 + u)]
    return np.unique(np.concatenate(ws))
CW, CR, CI = [], [], []
for ci, c in enumerate(combos):
    w = grid(c); rr = np.array([ratios(c, x) for x in w]); ok = np.isfinite(rr[:, 0]); CW.append(w[ok]); CR.append(rr[ok]); CI.append(np.full(ok.sum(), ci))
CWa = np.concatenate(CW); CRa = np.concatenate(CR); CIa = np.concatenate(CI); starts = np.concatenate([[0], np.cumsum([len(x) for x in CW])[:-1]]); nonempty = np.array([len(x) > 0 for x in CW])
print(f"   {len(combos)} Kombinationen (9 Funktionen, 2 Vorzeichen, 3 Ebenen); Raster in w: {len(CWa)} zulaessige Punkte (reelle positive Frequenzquadrate); Kombinationen ohne zulaessigen Punkt: {int((~nonempty).sum())}")
md_ = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd_ = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu_ = np.array([7.04e-6, 3.56e-3, 0.967]); su_ = np.array([0.15e-6, 0.06e-3, 0.004])
les = {"Omega^2 = sqrt(m)": (np.sqrt, lambda m: 0.5 / np.sqrt(m)), "Omega^2 = m": (lambda m: m, lambda m: np.ones_like(m)), "Omega^2 = m^2": (lambda m: m**2, lambda m: 2 * m)}
def target(m, s, fx, dfx):
    X = fx(m); sX = np.abs(dfx(m)) * s; r = X[:2] / X[2]; return r, r * np.sqrt((sX[:2] / X[:2])**2 + (sX[2] / X[2])**2)
def devs(r, sr):
    d = np.maximum(np.abs(CRa[:, 0] - r[0]) / sr[0], np.abs(CRa[:, 1] - r[1]) / sr[1]); out = np.full(len(combos), np.inf)
    idx = np.where(nonempty)[0]; red = np.minimum.reduceat(d, starts[idx]); arg = np.array([starts[i] + np.argmin(d[starts[i]: starts[i] + len(CW[i])]) for i in idx]) if r is not None else None
    out[idx] = red; return out, dict(zip(idx, arg))
def devs_fast(r, sr):
    d = np.maximum(np.abs(CRa[:, 0] - r[0]) / sr[0], np.abs(CRa[:, 1] - r[1]) / sr[1]); out = np.full(len(combos), np.inf); idx = np.where(nonempty)[0]; out[idx] = np.minimum.reduceat(d, starts[idx]); return out
def refine(c, wg, r, sr):
    ci = combos.index(c); w = CW[ci]; k = int(np.argmin(np.abs(w - wg))); lo, hi = w[max(k - 1, 0)], w[min(k + 1, len(w) - 1)]
    def z(x):
        a, b = ratios(c, x); return 1e9 if not np.isfinite(a) else max(abs(a - r[0]) / sr[0], abs(b - r[1]) / sr[1])
    res = minimize_scalar(z, bounds=(lo, hi), method="bounded", options={"xatol": 1e-14 * max(hi, 1e-300)}); return (res.x, res.fun) if res.fun < z(wg) else (wg, z(wg))
def info(c, w):
    h = c[1] * FR[c[0]]; o = [x for x in range(3) if x != c[2]]; th = [t for t in (h[o[0]], h[o[1]]) if t > 0]
    near = min(abs(w / t - 1) for t in th) if th else np.nan; return f"w = {w:.6g}" + (f", Abstand zur Schwelle |w/h - 1| = {near:.2e}" if th else "")
hb = hc = False
for ln, (fx, dfx) in les.items():
    res = {}
    for nm, m, s in (("Up", mu_, su_), ("Down", md_, sd_)):
        r, sr = target(m, s, fx, dfx); d, arg = devs(r, sr); res[nm] = (r, sr, d, arg)
    print(f"   {ln}:")
    for nm in ("Up", "Down"):
        r, sr, d, arg = res[nm]; ci = int(np.argmin(d)); w, z = refine(combos[ci], CWa[arg[ci]], r, sr); nh = int((d < 3).sum())
        print(f"      {nm:4s}: bester Abstand {z:.2f} sigma mit {cname(combos[ci])}, {info(combos[ci], w)}; Kombinationen unter 3 sigma (Raster): {nh} von {len(combos)}")
        for cj in np.where(d < 3)[0]:
            w2, z2 = refine(combos[cj], CWa[arg[cj]], r, sr); print(f"            {cname(combos[cj])}: {z2:.2f} sigma, {info(combos[cj], w2)}")
    both = np.maximum(res["Up"][2], res["Down"][2]); cb = int(np.argmin(both)); zz = []
    for nm in ("Up", "Down"):
        r, sr, d, arg = res[nm]; zz.append(refine(combos[cb], CWa[arg[cb]], r, sr) if np.isfinite(d[cb]) else (np.nan, np.inf))
    print(f"      gemeinsame Form (H190c): beste {cname(combos[cb])}: Up {zz[0][1]:.2f} sigma ({info(combos[cb], zz[0][0])}), Down {zz[1][1]:.2f} sigma ({info(combos[cb], zz[1][0])}); gemeinsame Formen unter 3 sigma: {int((both < 3).sum())}", flush=True)
    hb |= bool((res["Up"][2] < 3).any() and (res["Down"][2] < 3).any()); hc |= bool((both < 3).any())
print(f"   verglichen: {len(combos)} Kombinationen je Sektor und Lesart, 3 Lesarten")
NF = int(sys.argv[1]) if len(sys.argv) > 1 else 2000; cb_ = cc_ = 0
for it in range(NF):
    fake = []
    for s, m in ((su_, mu_), (sd_, md_)):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5); mf = np.array([m1, m2, 1.0]); fake.append((mf, mf * s / m))
    b_ = c_ = False
    for fx, dfx in les.values():
        du = devs_fast(*target(*fake[0], fx, dfx)); dd = devs_fast(*target(*fake[1], fx, dfx)); b_ |= bool((du < 3).any() and (dd < 3).any()); c_ |= bool((np.maximum(du, dd) < 3).any())
    cb_ += b_; cc_ += c_
    if it % 500 == 499: print(f"   ... {it + 1} erfundene Datensaetze gerechnet", flush=True)
print(f"   Zufallskontrolle ({NF} erfundene Datensaetze): Treffer je Sektor frei (H190b) {cb_ / NF:.2%}, gemeinsame Form (H190c) {cc_ / NF:.2%}")
for lab, h, q in (("H190b", hb, cb_ / NF), ("H190c", hc, cc_ / NF)):
    if not h: print(f"   Urteil {lab}: WIDERLEGT (kein Treffer innerhalb von 3 sigma fuer beide Sektoren)")
    elif q < 0.05: print(f"   Urteil {lab}: BESTAETIGT als Kandidat (Treffer, Zufallsquote {q:.2%}); eigener Vorab-Test noetig")
    else: print(f"   Urteil {lab}: OHNE URTEIL (Treffer, aber Zufallsquote {q:.2%})")
