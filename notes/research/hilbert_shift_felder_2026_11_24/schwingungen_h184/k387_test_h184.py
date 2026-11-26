"""k387 (Test H184): Farbschwingungen um ein zirkulantes Leptonvakuum in der Albert-Algebra H3(O).
Vorab: Vorab_Notiz_H184_Quarks_als_Schwingungen_um_das_Leptonvakuum.md (Commit 3048625).
Aufruf: python k387_test_h184.py > k387_out.txt"""
import itertools, numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(387)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])       # C[i, j, k]: e_i e_j = sum_k C e_k
cj = np.diag([1.0] + [-1.0] * 7)
# --- Albert-Algebra: W als (3, 3, 8); 27 Koordinaten: d0, d1, d2, x_a = W[0,1], x_b = W[1,2], x_c = W[2,0]
PAIRS = [(0, 1), (1, 2), (2, 0)]
def toW(v):
    W = np.zeros((3, 3, 8))
    for i in range(3): W[i, i, 0] = v[i]
    for s, (i, j) in enumerate(PAIRS):
        x = v[3 + 8 * s: 11 + 8 * s]; W[i, j] = x; W[j, i] = cj @ x
    return W
def fromW(W):
    return np.concatenate([[W[i, i, 0] for i in range(3)]] + [W[i, j] for (i, j) in PAIRS])
mm = lambda X, Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
jo = lambda X, Y: 0.5 * (mm(X, Y) + mm(Y, X))
tr = lambda X: X[0, 0, 0] + X[1, 1, 0] + X[2, 2, 0]
def projU(W):
    Z = np.zeros_like(W); Z[:, :, 0] = W[:, :, 0]; Z[:, :, 7] = W[:, :, 7]; return Z
Pm = np.zeros((3, 3)); Pm[0, 1] = Pm[1, 2] = Pm[2, 0] = 1                                   # S: zyklischer Platztausch
def actP(v): W = toW(v); return fromW(np.einsum('ij,jka,lk->ila', Pm, W, Pm))
def actT(v):                                                                                # Tausch der Plaetze 1, 2 (Automorphismus)
    Tm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1.0]]); W = toW(v); return fromW(np.einsum('ij,jka,lk->ila', Tm, W, Tm))
def actK(v): W = toW(v); return fromW(np.einsum('ija,ba->ijb', W, cj))                       # Konjugation der Eintraege (= Transposition)
actTau = lambda v: actK(actT(v))
lin = lambda f: np.array([f(col) for col in np.eye(27)]).T
MP, MT, MK = lin(actP), lin(actT), lin(actK); MTau = MK @ MT
def W0(a, r, delta):
    v = np.zeros(27); v[:3] = a
    for s in range(3): v[3 + 8 * s] = r * np.cos(delta); v[3 + 8 * s + 7] = r * np.sin(delta)
    return v
a0 = 1.0; r0 = a0 / np.sqrt(2); d0 = 2.0 / 9.0; w0 = W0(a0, r0, d0)
ev0 = np.array([a0 + 2 * r0 * np.cos(d0 + 2 * np.pi * k / 3) for k in range(3)])
print("== Kontrollen ==")
X, Y = toW(rng.normal(size=27)), toW(rng.normal(size=27))
aut = lambda M: np.abs(fromW(jo(toW(M @ fromW(X)), toW(M @ fromW(Y)))) - M @ fromW(jo(X, Y))).max()
print(f"   Automorphismus-Defekt (Jordan-Produkt): P {aut(MP):.1e}; T (Platztausch) {aut(MT):.1e}; Konjugation K {aut(MK):.2f}; tau = K T {aut(MTau):.2f}")
print(f"   W0 fest unter P: {np.abs(MP @ w0 - w0).max():.1e}; unter tau: {np.abs(MTau @ w0 - w0).max():.1e}; unter T: {np.abs(MT @ w0 - w0).max():.3f} (T bildet delta auf -delta ab)")
Wv = toW(w0); A = np.zeros((3, 3), dtype=complex)
for i in range(3):
    for j in range(3): A[i, j] = Wv[i, j, 0] + 1j * Wv[i, j, 7]
print(f"   Eigenwerte von W0 (K = 2/3, delta = 2/9): {np.round(np.sort(np.linalg.eigvalsh(A)), 6)}; Brannen-Form: {np.round(np.sort(ev0), 6)}; K = {np.sum(ev0**2) / np.sum(ev0)**2:.6f}")
# --- Farbe: Derivationen von O mit D(e7) = 0, auf alle Eintraege
rows = []
for i in range(8):
    for j in range(8):
        for k in range(8):
            r = np.zeros((8, 8)); r[k, :] += C[i, j, :]; r[:, i] -= C[:, j, k]; r[:, j] -= C[i, :, k]; rows.append(r.ravel())
fx = np.zeros((8, 64))
for k in range(8): fx[k, k * 8 + 7] = 1
st = null_space(np.vstack([np.array(rows), fx]), rcond=1e-9); g8 = [st[:, a].reshape(8, 8) for a in range(st.shape[1])]
def g27(g):
    M = np.zeros((27, 27))
    for s in range(3): M[3 + 8 * s: 11 + 8 * s, 3 + 8 * s: 11 + 8 * s] = g
    return M
G = [g27(g) for g in g8]
colidx = [3 + 8 * s + c for s in range(3) for c in range(1, 7)]; sngidx = [i for i in range(27) if i not in colidx]
print(f"   dim su(3)_c = {len(G)}; Farbe laesst W0 fest: {max(np.abs(g @ w0).max() for g in G):.1e}; Farbrichtungen {len(colidx)}, farblose Richtungen {len(sngidx)}")

print("\n== H184a, b: zweite Variation auf den 18 Farbrichtungen ==")
n = 18; idx = [(i, j) for i in range(n) for j in range(i, n)]; basis = []
for (i, j) in idx:
    B = np.zeros((n, n)); B[i, j] = B[j, i] = 1; basis.append(B)
sub = lambda M: M[np.ix_(colidx, colidx)]
Gc = [sub(g) for g in G]; Pc, Tauc = sub(MP), sub(MTau)
def forms(fin):
    cons = [np.array([(g.T @ B + B @ g).ravel() for B in basis]).T for g in Gc] + [np.array([(M.T @ B @ M - B).ravel() for B in basis]).T for M in fin]
    ns = null_space(np.vstack(cons), rcond=1e-9)
    return [sum(ns[k, a] * basis[k] for k in range(len(basis))) for a in range(ns.shape[1])]
F0, FP, FPT = forms([]), forms([Pc]), forms([Pc, Tauc])
print(f"   invariante quadratische Formen: nur Farbe {len(F0)} (hermitesche 3x3-Matrizen im Platzindex); mit P {len(FP)}; mit P und tau {len(FPT)}")
# Fourier-Raeume im Platzindex: Vektoren f_k (x) (beliebige Farbe)
om = np.exp(2j * np.pi / 3)
def fourier_overlap(H):
    w, V = np.linalg.eigh(H); out = []
    vals = sorted(set(np.round(w, 7)))
    for v in vals:
        E = V[:, np.abs(w - v) < 1e-6]                                                       # reeller Eigenraum
        # Platzanteil: 18 = 3 Plaetze x 6; Projektor auf Summe der Fourier-Moden k und -k ist reell
        best = 0
        for ks in ((0,), (1, 2), (0, 1, 2)):
            Pk = sum(np.outer(np.array([om ** (k * s) for s in range(3)]), np.conj(np.array([om ** (k * s) for s in range(3)]))) / 3 for k in ks).real
            Pfull = np.kron(Pk, np.eye(6)); ov = np.linalg.norm(Pfull @ E) ** 2 / E.shape[1]
            if ks != (0, 1, 2): best = max(best, ov)
        out.append(best)
    return out
def stats(Fs, label):
    mult = {}; ovmin = 1.0; gaps = []
    for _ in range(25):
        H = sum(rng.normal() * Q for Q in Fs); w = np.linalg.eigvalsh(H)
        vals = sorted(set(np.round(w / np.abs(w).max(), 7))); m = tuple(sorted(int(np.sum(np.abs(w / np.abs(w).max() - v) < 1e-6)) for v in vals))
        mult[m] = mult.get(m, 0) + 1; gaps.append(min(np.diff(np.sort(np.unique(np.round(w / np.abs(w).max(), 9))))) if len(vals) > 1 else 0)
    print(f"   {label}: Vielfachheiten in 25 Proben: {mult}")
    return mult
mP = stats(FP, "mit P (Stabilisator SU(3)_c x Z3)"); mPT = stats(FPT, "mit P und tau")
# Eigenrichtungen: kommutiert die zweite Variation mit dem Platztausch -> Eigenraeume sind Fourier-Raeume
com = max(np.abs(Pc.T @ Q @ Pc - Q).max() for Q in FP)
# explizit: Zirkulante im Platzindex. Komplexe Struktur der Farbe: I_c = L_U auf den Farbrichtungen
LU = np.einsum('i,ijk->kj', e[7], C)[1:7, 1:7]; Ic = np.kron(np.eye(3), LU)
S3 = np.kron(Pm, np.eye(6))
def circ_params(H):
    # H = alpha 1 + Re(beta) (S + S^T) (x) 1 + Im(beta) (S - S^T) (x) I_c  (bis auf die Wahl der Orientierung)
    Bs = [np.eye(18), np.kron(Pm + Pm.T, np.eye(6)), np.kron(Pm - Pm.T, LU)]
    co = np.linalg.lstsq(np.array([b.ravel() for b in Bs]).T, H.ravel(), rcond=None)[0]
    res = np.abs(sum(c * b for c, b in zip(co, Bs)) - H).max(); return co, res
rs = []; ok_spec = True
for _ in range(25):
    H = sum(rng.normal() * Q for Q in FP); co, res = circ_params(H); rs.append(res)
    al, be = co[0], co[1] + 1j * co[2]; pred = np.sort([al + 2 * abs(be) * np.cos(np.angle(be) + 2 * np.pi * k / 3) for k in range(3)])
    ok_spec &= np.allclose(np.sort(np.unique(np.round(np.linalg.eigvalsh(H), 8))), pred, atol=1e-7)
print(f"   Form alpha + beta S + conj(beta) S^2 (beta komplex ueber die Farbstruktur L_U): groesster Rest in 25 Proben {max(rs):.1e}; Spektrum alpha + 2|beta| cos(arg beta + 2 pi k/3): {ok_spec}")
rs2 = [abs(circ_params(sum(rng.normal() * Q for Q in FPT))[0][2]) for _ in range(25)]
print(f"   mit tau: Im(beta) in 25 Proben hoechstens {max(rs2):.1e}")
va = set(mP) == {(6, 6, 6)} and max(rs) < 1e-9
print("   Urteil H184a:", "BESTAETIGT (drei Frequenzquadrate je sechsfach; hermitesche Zirkulante, Eigenrichtungen sind die Fourier-Vektoren)" if va else "WIDERLEGT")
vb = set(mPT) == {(6, 12)}
print("   Urteil H184b:", "BESTAETIGT (mit tau immer zwei gleiche Frequenzquadrate: Vielfachheiten 6 und 12)" if vb else ("WIDERLEGT" if (6, 12) not in mPT else "gemischt"))
print(f"   Bericht: freie Groessen der Farb-Zirkulante: {len(FP)} (alpha, Re beta, Im beta) fuer drei Massen; mit tau: {len(FPT)}.")

print("\n== H184c: farblose Schwingungen (9 Richtungen), allgemeines Potential bis Grad 4 mit Symmetrie P ==")
ns_ = 9; Ps_ = MP[np.ix_(sngidx, sngidx)]; Taus_ = MTau[np.ix_(sngidx, sngidx)]; s0 = w0[sngidx]
mons = [m for d in range(1, 5) for m in itertools.combinations_with_replacement(range(ns_), d)]
def poly_eval(cf, x): return sum(c * np.prod(x[list(m)]) for c, m in zip(cf, mons))
def sym_coef(cf, mats):
    # exakte Mittelung ueber die endliche Gruppe: Auswertung an Punkten, Rueckfit auf Monome
    Xs = rng.normal(size=(len(mons) + 60, ns_)); Mx = np.array([[np.prod(x[list(m)]) for m in mons] for x in Xs])
    vals = np.mean([[poly_eval(cf, g @ x) for x in Xs] for g in mats], axis=0)
    return np.linalg.lstsq(Mx, vals, rcond=None)[0]
def grad_hess(cf, x):
    g = np.zeros(ns_); H = np.zeros((ns_, ns_))
    for c, m in zip(cf, mons):
        if abs(c) < 1e-13: continue
        for i in set(m):
            mi = list(m); mi.remove(i); g[i] += c * m.count(i) * np.prod(x[mi]) if mi else c * m.count(i)
        for i in set(m):
            for j in set(m):
                mi = list(m); mi.remove(i)
                if j not in mi: continue
                fac = m.count(i) * mi.count(j); mi.remove(j); H[i, j] += c * fac * (np.prod(x[mi]) if mi else 1.0)
    return g, H
grpP = [np.linalg.matrix_power(Ps_, k) for k in range(3)]; grpPT = grpP + [Taus_ @ g for g in grpP]
for label, grp in (("mit P", grpP), ("mit P und tau", grpPT)):
    zero = {}; stable = 0
    for trial in range(8):
        cf = sym_coef(rng.normal(size=len(mons)), grp)
        # W0 stationaer machen: Gradient ist P-fest (3 Richtungen); mit den linearen Termen ausgleichen
        g, H = grad_hess(cf, s0)
        for i in range(ns_): cf[mons.index((i,))] -= g[i]
        g, H = grad_hess(cf, s0); w = np.linalg.eigvalsh(H); nz = int(np.sum(np.abs(w) < 1e-8)); zero[nz] = zero.get(nz, 0) + 1; stable += int(w.min() > 0)
        assert np.abs(g).max() < 1e-9
    print(f"   {label}: Zahl der Nullrichtungen in 8 Proben: {zero} (erwartet 0: Farbe laesst W0 fest, P und tau sind endlich); Proben mit lauter positiven Frequenzquadraten: {stable}")
    if label == "mit P": vc = set(zero) == {0}
print("   Urteil H184c:", "BESTAETIGT (keine erzwungenen Nullrichtungen)" if vc else "WIDERLEGT")

print("\n== Zusatz (nachtraeglich, Erkundung): Potentiale aus den Spuren der Albert-Algebra ==")
def invs(v):
    W = toW(v); Wu = projU(W); W2 = jo(W, W); U2 = jo(Wu, Wu); t = tr(W)
    return {"Tr W^2": tr(W2), "Tr Wu^2": tr(U2), "Tr W^3": tr(jo(W2, W)), "Tr Wu^3": tr(jo(U2, Wu)), "Tr W^4": tr(jo(W2, W2)), "Tr Wu^4": tr(jo(U2, U2)),
            "Tr W^2 o Wu^2": tr(jo(W2, U2)), "(Tr W^2)^2": tr(W2) ** 2, "Tr W^2 Tr Wu^2": tr(W2) * tr(U2), "(Tr Wu^2)^2": tr(U2) ** 2,
            "Tr W Tr W^3": t * tr(jo(W2, W)), "(Tr W)^2 Tr W^2": t * t * tr(W2), "(Tr W)^2 Tr Wu^2": t * t * tr(U2)}
names = list(invs(w0).keys())
def hess_fd(f, x, ix, h=0.05):
    # zweite Ableitungen auf den Richtungen ix; fuer Polynome bis Grad 4 exakt (Richardson aus h und 2h)
    nx = len(ix); H = np.zeros((nx, nx)); E = np.eye(len(x))[ix]
    def d2(i, j, hh):
        return (f(x + hh * E[i] + hh * E[j]) - f(x + hh * E[i] - hh * E[j]) - f(x - hh * E[i] + hh * E[j]) + f(x - hh * E[i] - hh * E[j])) / (4 * hh * hh)
    for i in range(nx):
        for j in range(i, nx):
            H[i, j] = H[j, i] = (4 * d2(i, j, h) - d2(i, j, 2 * h)) / 3
    return H
allf = lambda v: np.array(list(invs(v).values()))
def color_spectra(wv):
    Hc = hess_fd(allf, wv, colidx) if False else None
    return None
def hess_all(wv, ix):
    nx = len(ix); E = np.eye(27)[ix]; H = np.zeros((len(names), nx, nx))
    def d2(i, j, hh):
        return (allf(wv + hh * E[i] + hh * E[j]) - allf(wv + hh * E[i] - hh * E[j]) - allf(wv - hh * E[i] + hh * E[j]) + allf(wv - hh * E[i] - hh * E[j])) / (4 * hh * hh)
    for i in range(nx):
        for j in range(i, nx):
            H[:, i, j] = H[:, j, i] = (4 * d2(i, j, 0.05) - d2(i, j, 0.1)) / 3
    return H
Hcol = hess_all(w0, colidx)
print("   Farbblock der zweiten Variation je Invariante bei W0 (drei Frequenzquadrate, je sechsfach):")
for q, nm in enumerate(names):
    w = np.linalg.eigvalsh(Hcol[q]); u = np.sort(np.unique(np.round(w, 7)))
    print(f"      {nm:18s}: " + (", ".join(f"{x:+.5f}" for x in u) if np.abs(w).max() > 1e-9 else "0 (traegt nichts bei)"))
print("   Jede Farbmode gehoert zu einem Paar (i, j) von Eigenrichtungen von W0 (Eigenwerte l_i, l_j; dritter l_k). Anpassung ueber vier Vakua gemeinsam:")
pairs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
vacs = [(1.0, 1 / np.sqrt(2), 2 / 9), (1.0, 0.5, 0.4), (0.7, 0.9, 0.15), (1.3, 0.4, 0.7)]
data = []
for (a, r, dl) in vacs:
    wv = W0(a, r, dl); lm = np.sort([a + 2 * r * np.cos(dl + 2 * np.pi * k / 3) for k in range(3)]); data.append((lm, hess_all(wv, colidx)))
feats = {0: (["1"], lambda a, b, c: [1.0]),
         1: (["(l_i + l_j)", "l_k"], lambda a, b, c: [a + b, c]),
         2: (["(l_i^2 + l_j^2)", "l_i l_j", "l_k (l_i + l_j)", "l_k^2"], lambda a, b, c: [a * a + b * b, a * b, c * (a + b), c * c])}
degs = {"Tr W^2": 0, "Tr Wu^2": 0, "Tr W^3": 1, "Tr Wu^3": 1, "Tr W^4": 2, "Tr Wu^4": 2, "Tr W^2 o Wu^2": 2, "(Tr W^2)^2": 2, "Tr W^2 Tr Wu^2": 2, "(Tr Wu^2)^2": 2,
        "Tr W Tr W^3": 2, "(Tr W)^2 Tr W^2": 2, "(Tr W)^2 Tr Wu^2": 2}
for q, nm in enumerate(names):
    if np.abs(Hcol[q]).max() < 1e-9: continue
    lab, fn = feats[degs[nm]]; best = (1e9, None)
    for perm in itertools.permutations(range(3)):
        M, y = [], []
        for (lm, Hs) in data:
            u = np.sort(np.linalg.eigvalsh(Hs[q]))[::6]
            for p_, (i, j, k) in enumerate(pairs): M.append(fn(lm[i], lm[j], lm[k])); y.append(u[perm[p_]])
        co, *_ = np.linalg.lstsq(np.array(M), np.array(y), rcond=None); res = np.abs(np.array(M) @ co - np.array(y)).max()
        if res < best[0]: best = (res, co)
    print(f"      {nm:18s}: " + " ".join(f"{c:+.4f} {l}" for c, l in zip(best[1], lab) if abs(c) > 1e-6) + f"   (Rest {best[0]:.1e})")
Hsng = hess_all(w0, sngidx); cfs = rng.normal(size=len(names))
print(f"   farbloser Block eines zufaelligen Spur-Potentials (nur Struktur der zweiten Ableitungen): Rang {np.linalg.matrix_rank(np.einsum('q,qij->ij', cfs, Hsng), tol=1e-7)} von 9")
# F4-invariantes Spurpotential, bei dem W0 stationaer ist: V = Tr v(W), v'(l) = (l - l_1)(l - l_2)(l - l_3)
l1, l2, l3 = np.sort(ev0); e1, e2, e3 = l1 + l2 + l3, l1 * l2 + l1 * l3 + l2 * l3, l1 * l2 * l3
cF = {"Tr W^4": 1 / 4, "Tr W^3": -e1 / 3, "Tr W^2": e2 / 2}                                  # v = l^4/4 - e1 l^3/3 + e2 l^2/2 - e3 l
HF = sum(c * Hcol[names.index(nm)] for nm, c in cF.items()); HFs = sum(c * Hsng[names.index(nm)] for nm, c in cF.items())
print(f"   F4-invariantes Spurpotential mit W0 stationaer (v' = (l - l_1)(l - l_2)(l - l_3)): Farbfrequenzen hoechstens {np.abs(np.linalg.eigvalsh(HF)).max():.1e} (masselos: Bahn von W0 unter F4);")
print(f"      farbloser Block: Eigenwerte {np.round(np.linalg.eigvalsh(HFs), 5)} (sechs Nullrichtungen aus der Familien-SU(3), drei massive)")
print("   Regel im F4-invarianten Teil: Frequenzquadrat der Mode (i, j) = 2 (v'(l_i) - v'(l_j)) / (l_i - l_j); null, sobald W0 stationaer ist.")
print("   Folge: Die Frequenzen der Farbschwingungen kommen allein aus Termen, die U auszeichnen (hier Tr W^2 o Wu^2, Tr W^2 Tr Wu^2).")
