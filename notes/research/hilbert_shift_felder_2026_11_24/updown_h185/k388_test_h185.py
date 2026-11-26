"""k388 (Test H185): Farbschwingungen im komplexen Feld C (x) H3(O) um das Leptonvakuum, nach Ladung zerlegt.
Vorab: Vorab_Notiz_H185_Up_und_Down_als_Schwingungen_im_komplexen_Feld.md (Commit df685ba).
Aufruf: python k388_test_h185.py > k388_out.txt"""
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(388)
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
print("== Kontrollen ==")
print(f"   dim su(3)_c = {len(g8)}; R_U = -L_U auf dem Farbblock: {np.abs(RU + LU).max():.1e}; Ladungen auf den 36 Farbrichtungen: "
      f"{dict(zip(*[x.tolist() for x in np.unique(np.round(np.linalg.eigvalsh((Qc + Qc.T) / 2), 6), return_counts=True)]))}")
print(f"   C tauscht die Ladungen (C Q C = 1 - Q): {np.abs(Cc @ Qc @ Cc - (np.eye(36) - Qc)).max():.1e}; P und tau vertauschen mit Q: {np.abs(Pc @ Qc - Qc @ Pc).max():.1e}, {np.abs(Tauc @ Qc - Qc @ Tauc).max():.1e}")
wq, Vq = np.linalg.eigh((Qc + Qc.T) / 2); E13, E23 = Vq[:, wq < 0.5], Vq[:, wq > 0.5]

print("\n== H185a, b, c: invariante quadratische Formen auf den 36 Farbrichtungen ==")
n = 36; basis = []
for i in range(n):
    for j in range(i, n):
        B = np.zeros((n, n)); B[i, j] = B[j, i] = 1; basis.append(B)
BM = np.array([B.ravel() for B in basis]).T                              # 1296 x 666
def forms(gens, fin, anti=None):
    cons = [np.kron(np.eye(n), g.T) @ BM + np.kron(g.T, np.eye(n)) @ BM for g in gens]
    cons += [np.kron(M.T, M.T) @ BM - BM for M in fin]
    if anti is not None: cons.append(np.kron(anti.T, anti.T) @ BM + BM)
    Mx = np.vstack(cons); G_ = Mx.T @ Mx; w, V = np.linalg.eigh(G_); ns = V[:, w < 1e-9 * max(w.max(), 1)]
    return [(BM @ ns[:, a]).reshape(n, n) for a in range(ns.shape[1])]
F0 = forms(Gc, []); FP = forms(Gc, [Pc]); FPq = forms(Gc + [Ii], [Pc]); FPm = forms(Gc, [Pc], anti=Ii)
FPqC = forms(Gc + [Ii], [Pc, Cc]); FPC = forms(Gc, [Pc, Cc]); FPqT = forms(Gc + [Ii], [Pc, Tauc]); FPqCT = forms(Gc + [Ii], [Pc, Cc, Tauc])
print(f"   nur Farbe: {len(F0)}; mit P: {len(FP)}; davon ladungserhaltend (vertauschen mit i): {len(FPq)}, ladungsmischend (antivertauschen): {len(FPm)}")
print(f"   mit P und C: {len(FPC)}; ladungserhaltend mit P und C: {len(FPqC)}; ladungserhaltend mit P und tau: {len(FPqT)}; mit P, C und tau: {len(FPqCT)}")
def mults(H):
    w = np.linalg.eigvalsh(H); s = np.abs(w).max(); vals = sorted(set(np.round(w / s, 7)))
    return tuple(sorted(int(np.sum(np.abs(w / s - v) < 1e-6)) for v in vals))
def stat(Fs, k=25):
    d = {}
    for _ in range(k):
        m = mults(sum(rng.normal() * Q for Q in Fs)); d[m] = d.get(m, 0) + 1
    return d
mA = stat(FP); print(f"   mit P: Vielfachheiten in 25 Proben: {mA}")
S36 = np.kron(I2, np.kron(Pm, np.eye(6)))
print(f"   alle 12 Formen vertauschen mit dem Platztausch (Fourier-Eigenrichtungen): {max(np.abs(S36.T @ Q @ S36 - Q).max() for Q in FP):.1e}")
va = len(FP) == 12 and set(mA) == {(6,) * 6}
print("   Urteil H185a:", "BESTAETIGT (12 Formen, sechs Frequenzquadrate je sechsfach)" if va else "WIDERLEGT")
vb = len(FPq) == 6 and len(FPm) == 6
print("   Urteil H185b:", "BESTAETIGT (6 ladungserhaltende, 6 ladungsmischende Formen)" if vb else "WIDERLEGT")
def specq(H): return np.sort(np.unique(np.round(np.linalg.eigvalsh(E13.T @ H @ E13), 9))), np.sort(np.unique(np.round(np.linalg.eigvalsh(E23.T @ H @ E23), 9)))
def blockspec(H): return np.sort(np.linalg.eigvalsh(E13.T @ H @ E13)), np.sort(np.linalg.eigvalsh(E23.T @ H @ E23))
dq = []; mq = {}
for _ in range(25):
    H = sum(rng.normal() * Q for Q in FPq); a, b = blockspec(H); dq.append(np.abs(a - b).max() / np.abs(H).max())
    m = (mults(E13.T @ H @ E13), mults(E23.T @ H @ E23)); mq[str(m)] = mq.get(str(m), 0) + 1
print(f"   ladungserhaltend mit P: Vielfachheiten (Ladung 1/3, Ladung 2/3): {mq}; Unterschied der beiden Spektren (relativ) zwischen {min(dq):.2f} und {max(dq):.2f}")
dc = []
for _ in range(25):
    H = sum(rng.normal() * Q for Q in FPqC); a, b = blockspec(H); dc.append(np.abs(a - b).max() / np.abs(H).max())
print(f"   mit C dazu: Unterschied der Spektren fuer 1/3 und 2/3 in 25 Proben hoechstens {max(dc):.1e}")
vc = max(dc) < 1e-8
print("   Urteil H185c:", "BESTAETIGT (mit C gleiche Spektren fuer beide Ladungen)" if vc else "WIDERLEGT")
dt = stat(FPqT); print(f"   ladungserhaltend mit P und tau: Vielfachheiten {dt}")
# ladungsmischender Anteil: Wirkung auf das Spektrum
H = sum(rng.normal() * Q for Q in FPq); Hm = sum(rng.normal() * Q for Q in FPm)
w, V = np.linalg.eigh(H + 0.3 * Hm); qexp = np.round(np.sort(np.unique(np.round(np.einsum('ia,ij,ja->a', V, (Qc + Qc.T) / 2, V), 4))), 4)
print(f"   Beispiel mit ladungsmischendem Anteil (Gewicht 0,3): Ladungserwartungswerte der Eigenrichtungen {qexp} (nicht mehr 1/3 und 2/3)")
print(f"   Bericht: freie Groessen: Farbe + P 12; ladungserhaltend 6 (fuer sechs Massen); mit C 3; mit tau {len(FPqT)}.")

print("\n== H185d: Spurpotentiale ohne expliziten Ladungsoperator ==")
def split(z, name): return [(f"Re {name}", lambda W, z=z: z(W).real), (f"Im {name}", lambda W, z=z: z(W).imag)]
cb = np.conj; U = projU
inv = []
inv += split(lambda W: tr(jo(W, W)), "Tr W^2")
inv += [("Tr W Wq", lambda W: tr(jo(W, cb(W))).real)]
inv += split(lambda W: tr(jo(jo(W, W), W)), "Tr W^3")
inv += split(lambda W: tr(jo(jo(W, W), cb(W))), "Tr W^2 Wq")
inv += split(lambda W: tr(jo(jo(W, W), U(W))), "Tr W^2 Wu")
inv += split(lambda W: tr(jo(jo(W, W), cb(U(W)))), "Tr W^2 Wuq")
inv += split(lambda W: tr(jo(jo(W, cb(W)), U(W))), "Tr (W Wq) Wu")
inv += split(lambda W: tr(jo(jo(W, W), jo(W, W))), "Tr W^2 o W^2")
inv += split(lambda W: tr(jo(jo(W, W), jo(W, cb(W)))), "Tr W^2 o (W Wq)")
inv += [("Tr W^2 o Wq^2", lambda W: tr(jo(jo(W, W), jo(cb(W), cb(W)))).real), ("Tr (W Wq)^2", lambda W: tr(jo(jo(W, cb(W)), jo(W, cb(W)))).real)]
inv += split(lambda W: tr(jo(jo(W, W), jo(U(W), U(W)))), "Tr W^2 o Wu^2")
inv += split(lambda W: tr(jo(jo(W, W), jo(cb(U(W)), cb(U(W))))), "Tr W^2 o Wuq^2")
inv += split(lambda W: tr(jo(jo(W, W), jo(U(W), cb(U(W))))), "Tr W^2 o (Wu Wuq)")
inv += split(lambda W: tr(jo(jo(W, cb(W)), jo(U(W), U(W)))), "Tr (W Wq) o Wu^2")
inv += [("Tr (W Wq) o (Wu Wuq)", lambda W: tr(jo(jo(W, cb(W)), jo(U(W), cb(U(W))))).real)]
inv += split(lambda W: tr(jo(jo(W, U(W)), jo(W, U(W)))), "Tr (W Wu)^2")
inv += split(lambda W: tr(jo(jo(W, U(W)), jo(W, cb(U(W))))), "Tr (W Wu) o (W Wuq)")
inv += split(lambda W: tr(jo(jo(W, U(W)), jo(cb(W), U(W)))), "Tr (W Wu) o (Wq Wu)")
inv += split(lambda W: tr(jo(jo(W, U(W)), jo(cb(W), cb(U(W))))), "Tr (W Wu) o (Wq Wuq)")
inv += split(lambda W: tr(jo(W, W)) * tr(jo(U(W), cb(U(W)))), "Tr W^2 Tr Wu Wuq")
inv += split(lambda W: tr(jo(W, cb(W))) * tr(jo(U(W), U(W))), "Tr W Wq Tr Wu^2")
inv += split(lambda W: tr(W) * tr(jo(jo(W, W), cb(W))), "Tr W Tr W^2 Wq")
c36 = colidx + [27 + c for c in colidx]
def hess(f, w0):
    def F(d):
        v = np.asarray(w0, dtype=complex).copy(); v[colidx] += d[:18] + 1j * d[18:]; return f(toW(v))
    def H1(h):
        Hh = np.zeros((36, 36)); E = np.eye(36) * h; f0 = F(np.zeros(36))
        fp = [F(2 * E[i]) for i in range(36)]; fm = [F(-2 * E[i]) for i in range(36)]
        for i in range(36):
            Hh[i, i] = (fp[i] - 2 * f0 + fm[i]) / (4 * h * h)
            for j in range(i + 1, 36):
                Hh[i, j] = Hh[j, i] = (F(E[i] + E[j]) - F(E[i] - E[j]) - F(E[j] - E[i]) + F(-E[i] - E[j])) / (4 * h * h)
        return Hh
    return (4 * H1(0.1) - H1(0.2)) / 3                                    # Richardson: fuer Grad <= 4 exakt
def analyse(H):
    s = np.abs(H).max()
    if s < 1e-10: return None
    inv_def = max(max(np.abs(g.T @ H + H @ g).max() for g in Gc), np.abs(Pc.T @ H @ Pc - H).max()) / s
    Hc = (H + Ii.T @ H @ Ii) / 2; Hmix = (H - Ii.T @ H @ Ii) / 2
    a, b = blockspec(Hc); odd = np.abs(a - b).max() / s
    return inv_def, odd, np.abs(Hmix).max() / s, np.unique(np.round(a, 5)), np.unique(np.round(b, 5))
res = {}
for dl, lab in ((2.0 / 9.0, "delta = 2/9"), (0.0, "delta = 0")):
    w0 = W0(1.0, 1 / np.sqrt(2), dl); print(f"   -- {lab} --"); res[lab] = []
    for name, f in inv:
        r = analyse(hess(f, w0))
        if r is None: print(f"      {name:26s}: traegt nichts bei"); continue
        res[lab].append((name, r[1], r[2]))
        print(f"      {name:26s}: Invarianzdefekt {r[0]:.0e}; ladungsungerade {r[1]:.2e}; ladungsmischend {r[2]:.2e}; Frequenzquadrate 1/3: {r[3]}, 2/3: {r[4]}", flush=True)
o29 = max(x[1] for x in res["delta = 2/9"]); o0 = max(x[1] for x in res["delta = 0"])
m29 = max(x[2] for x in res["delta = 2/9"]); m0 = max(x[2] for x in res["delta = 0"])
print(f"   groesster ladungsungerader Anteil: delta = 2/9: {o29:.2e}; delta = 0: {o0:.2e}. Groesster ladungsmischender Anteil: {m29:.2e}; {m0:.2e}")
if o29 > 1e-6 and o0 < 1e-9: print("   Urteil H185d: BESTAETIGT (ladungsungerader Anteil nur bei delta != 0)")
elif o29 < 1e-9: print("   Urteil H185d: WIDERLEGT (kein ladungsungerader Anteil ohne expliziten Ladungsoperator)")
else: print("   Urteil H185d: Bericht ohne Urteil (ladungsungerader Anteil auch bei delta = 0)")

print("\n== Zusatz (nachtraeglich, Erkundung): nicht reelles Vakuum ==")
def Wc(kind, g):
    v = W0(1.0, 1 / np.sqrt(2), 2.0 / 9.0).astype(complex)
    for s in range(3):
        x = v[3 + 8 * s: 11 + 8 * s].copy()
        if kind == "phase": x = x * np.exp(1j * g)                       # komplexe Phase auf den Eintraegen neben der Diagonale
        else: x[7] += 1j * g                                             # Zusatz i g U
        v[3 + 8 * s: 11 + 8 * s] = x
    return v
sel = [k for k, (nm, _) in enumerate(inv) if nm in ("Tr W Wq", "Re Tr W^2 Wq", "Im Tr W^2 Wq", "Re Tr (W Wq) Wu", "Im Tr (W Wq) Wu", "Tr (W Wq)^2",
                                                    "Re Tr (W Wq) o Wu^2", "Im Tr (W Wq) o Wu^2", "Re Tr (W Wu) o (Wq Wu)", "Im Tr (W Wu) o (Wq Wu)")]
for kind, g, lab in (("phase", 0.3, "Eintraege mal exp(0,3 i)"), ("iU", 0.3, "Eintraege plus 0,3 i U")):
    w0c = Wc(kind, g); print(f"   -- {lab} --"); mx = 0
    for k in sel:
        name, f = inv[k]; r = analyse(hess(f, w0c))
        if r is None: print(f"      {name:26s}: traegt nichts bei"); continue
        mx = max(mx, r[1])
        print(f"      {name:26s}: Invarianzdefekt {r[0]:.0e}; ladungsungerade {r[1]:.2e}; ladungsmischend {r[2]:.2e}; Frequenzquadrate 1/3: {r[3]}, 2/3: {r[4]}", flush=True)
    print(f"      groesster ladungsungerader Anteil: {mx:.2e}")
