"""k276 (Test H127, Vorab-Notiz ba473c5 vom 24.11.2026 15:59 UTC): Spin-Inhalt der Ladungsbrechung und Leckordnung in die Quarks.
Stufe A: A0 = P_s C P_s (C = L_e7 je Platz) unter so(3) (X -> R X R^T) in Spin-l-Komponenten zerlegen, Anteile w_l.
Stufe B: K(A) = sum_a L_{Y_a} A L_{Y_a} (Y_a Orthonormalbasis der Spurform), A_n = K(A_{n-1}), C_eff^(n) = P_t A_n P_t, Brechungsmass b_n.
Alle Rechnungen in einer Orthonormalbasis der Spurform Tr(X o Y). Konventionen wie k275. Aufruf: python3 k276_test_h127.py
"""
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(276)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def omul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([omul(a, c) - omul(conj(d), b), omul(d, a) + omul(b, conj(c))])


E8 = np.eye(8)
OT = np.array([[omul(E8[i], E8[j]) for j in range(8)] for i in range(8)])
om = lambda x, y: np.einsum('i,j,ijk->k', x, y, OT)
N = 27
I27 = np.eye(N)


def to_mat(v):
    a = v[:3]; x1, x2, x3 = v[3:11], v[11:19], v[19:27]
    M = np.zeros((3, 3, 8))
    for k in range(3):
        M[k, k, 0] = a[k]
    M[0, 1] = x3; M[1, 0] = conj(x3)
    M[1, 2] = x1; M[2, 1] = conj(x1)
    M[2, 0] = x2; M[0, 2] = conj(x2)
    return M


def to_vec(M):
    return np.concatenate([[M[0, 0, 0], M[1, 1, 0], M[2, 2, 0]], M[1, 2], M[2, 0], M[0, 1]])


def mmul(A, B):
    C = np.zeros((3, 3, 8))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i, j] += om(A[i, k], B[k, j])
    return C


def jordan(u, v):
    A, B = to_mat(u), to_mat(v)
    return to_vec(0.5 * (mmul(A, B) + mmul(B, A)))


# Spurform Tr(X o Y): Diagonale Gewicht 1, Oktonion-Eintraege Gewicht 2 -> S = sqrt(g), Koordinaten v' = S v
g = np.array([1.0] * 3 + [2.0] * 24)
S, Si = np.diag(np.sqrt(g)), np.diag(1 / np.sqrt(g))
tr = lambda u, v: sum(jordan(u, v)[:3])
x, y = rng.normal(size=N), rng.normal(size=N)
print("=" * 78)
print(f"Kontrolle Spurform: Tr(X o Y) - x^T g y = {tr(x, y) - x @ (g * y):.1e}")

# Jordan-Multiplikation L_Y in den Spurform-Orthonormalkoordinaten
CJ = np.array([[jordan(I27[i], I27[j]) for j in range(N)] for i in range(N)])  # CJ[i,j] = e_i o e_j


def LY(yc):  # yc in Originalkoordinaten
    Lm = np.einsum('i,ijk->kj', yc, CJ)
    return S @ Lm @ Si


Ybasis = [Si @ I27[a] for a in range(N)]  # Orthonormalbasis der Spurform (Originalkoordinaten)
Ls = [LY(Yc) for Yc in Ybasis]
print(f"L_Y selbstadjungiert (Spurform): max|L - L^T| = {max(np.abs(L - L.T).max() for L in Ls):.1e}")


def so3_gen(a):
    Lg = np.zeros((3, 3)); i, j = [(1, 2), (2, 0), (0, 1)][a]
    Lg[i, j], Lg[j, i] = -1, 1
    T = np.zeros((N, N))
    for k in range(N):
        M = to_mat(I27[k])
        T[:, k] = to_vec(np.einsum('ij,jkl->ikl', Lg, M) + np.einsum('ijl,kj->ikl', M, Lg))
    return S @ T @ Si


SO3 = [so3_gen(a) for a in range(3)]
print(f"so(3) antisymmetrisch in Spurform-Koordinaten: {max(np.abs(T + T.T).max() for T in SO3):.1e}")


def diag_slots(M8):
    D = np.zeros((N, N))
    for s in range(3):
        D[3 + 8 * s:11 + 8 * s, 3 + 8 * s:11 + 8 * s] = M8
    return D


C = S @ diag_slots(OT[7].T) @ Si  # x -> e7 x je Platz
idx_s = [0, 1, 2, 3, 11, 19, 10, 18, 26]
idx_t = [3 + 8 * s + c for s in range(3) for c in range(1, 7)]
Ps = np.zeros((N, N)); Ps[idx_s, idx_s] = 1
Pt = np.zeros((N, N)); Pt[idx_t, idx_t] = 1
print(f"[C, P_s] = {np.abs(C @ Ps - Ps @ C).max():.1e}, [so(3), P_s] = {max(np.abs(T @ Ps - Ps @ T).max() for T in SO3):.1e}")


def spin_parts(A, idx):
    """Spin-Zerlegung des Operators A (auf dem Unterraum idx) unter ad so(3). Rueckgabe {l: ||A_l||^2 / ||A||^2}."""
    n = len(idx)
    Ts = [T[np.ix_(idx, idx)] for T in SO3]
    a = A[np.ix_(idx, idx)].ravel()
    # ad_T als Matrix auf vec(A): [T, A] -> (T x I - I x T^T) vec(A) (Zeilen-Major)
    I = np.eye(n)
    ads = [np.kron(T, I) - np.kron(I, T.T) for T in Ts]
    Cas = -sum(ad @ ad for ad in ads)
    Cas = 0.5 * (Cas + Cas.T)
    ev, V = np.linalg.eigh(Cas)
    coef = V.T @ a
    out = {}
    tot = a @ a
    for e, c in zip(ev, coef):
        l = int(round((-1 + np.sqrt(1 + 4 * max(e, 0))) / 2))
        assert abs(l * (l + 1) - e) < 1e-6, e
        out[l] = out.get(l, 0.0) + c * c
    return {l: v / tot for l, v in sorted(out.items())}, tot


print("=" * 78)
print("Stufe A: A0 = P_s C P_s, Anteile w_l")
A0 = Ps @ C @ Ps
wA, nA = spin_parts(A0, idx_s)
for l, w in wA.items():
    print(f"   l = {l:2d}: w_l = {w:.10f}")
print(f"   ||A0||^2 = {nA:.6f}")
w3 = wA.get(3, 0.0)
allowed = {3, 6, 7, 9, 10}
ctrl = max([w for l, w in wA.items() if l not in allowed] + [0.0])
lead = max(wA, key=wA.get)
print(f"   w_3 = {w3:.10f}, fuehrende Komponente l = {lead}, Kontrolle max w_l (l nicht in {sorted(allowed)}) = {ctrl:.1e}")
if ctrl >= 1e-10:
    verdictA = "KONTROLLE VERLETZT"
elif w3 >= 1e-8 and all(w3 >= w - 1e-12 for w in wA.values()):
    verdictA = "bestaetigt"
elif w3 >= 1e-8:
    verdictA = "teilweise"
elif w3 < 1e-10:
    verdictA = "widerlegt"
else:
    verdictA = "unentschieden (zwischen den Schwellen)"
print(f"   -> Stufe A: {verdictA}")

# Nachkontrolle Stufe A: S4-ungerade? (zyklische Permutation = A4, Transposition mit Vorzeichen = ungerade)
def rep(R):
    M = np.zeros((N, N))
    for k in range(N):
        X = to_mat(I27[k]); M[:, k] = to_vec(np.einsum('ij,jkl,mk->iml', R, X, R))
    return S @ M @ Si


Rodd = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.0]])
Rcyc = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
print(f"   Nachkontrolle: rho(zykl.) A0 rho^T - A0 = {np.abs(rep(Rcyc) @ A0 @ rep(Rcyc).T - A0).max():.1e};"
      f"  rho(ungerade) A0 rho^T + A0 = {np.abs(rep(Rodd) @ A0 @ rep(Rodd).T + A0).max():.1e}")

print("=" * 78)
print("Stufe B: Leckordnung, C_eff^(n) = P_t K^n(A0) P_t")


def K(A):
    return sum(L @ A @ L for L in Ls)


# Aequivarianz von K pruefen
R = expm(sum(c * T for c, T in zip(rng.normal(size=3), SO3)))
Z = rng.normal(size=(N, N))
print(f"   Kontrolle K aequivariant: |K(R Z R^T) - R K(Z) R^T| = {np.abs(K(R @ Z @ R.T) - R @ K(Z) @ R.T).max():.1e}")
Rs = [expm(sum(c * T for c, T in zip(rng.normal(size=3) * 2, SO3))) for _ in range(20)]


def bmeas(Ce):
    nrm = np.linalg.norm(Ce)
    if nrm < 1e-12:
        return 0.0, nrm
    return max(np.linalg.norm(R @ Ce @ R.T - Ce) for R in Rs) / nrm, nrm


b0, n0 = bmeas(Pt @ C @ Pt)
print(f"   n = 0 (Kontrolle P_t C P_t): ||.|| = {n0:.4f}, b_0 = {b0:.1e}")
A = A0
bs = {}
Ceffs = {}
for n in (1, 2, 3):
    A = K(A)
    Ce = Pt @ A @ Pt
    bs[n], nrm = bmeas(Ce)
    Ceffs[n] = Ce
    print(f"   n = {n}: ||C_eff|| = {nrm:.6e}, b_{n} = {bs[n]:.3e}, ||A_n|| gesamt = {np.linalg.norm(A):.4e},"
          f" Anteil Singulettblock {np.linalg.norm(Ps @ A @ Ps):.4e}")
nq = next((n for n in (1, 2, 3) if bs[n] > 1e-8), None)
print(f"   Leckordnung n_q = {nq}")
if nq is not None:
    wB, nB = spin_parts(Ceffs[nq], idx_t)
    print(f"   Spin-Anteile von C_eff^({nq}) auf den Tripletts:")
    for l, w in wB.items():
        print(f"      l = {l:2d}: w_l = {w:.10f}")
    brk = {l: w for l, w in wB.items() if l > 0}
    leadB = max(brk, key=brk.get) if brk else None
    print(f"   fuehrende Komponente l > 0: {leadB}")
if b0 >= 1e-10:
    verdictB = "KONTROLLE VERLETZT"
elif nq == 1 and leadB == 3:
    verdictB = "bestaetigt"
elif nq in (1, 2, 3):
    verdictB = "teilweise"
elif all(bs[n] < 1e-10 for n in bs):
    verdictB = "widerlegt (Quarks tragen SO(3) effektiv exakt)"
else:
    verdictB = "unentschieden (zwischen den Schwellen)"
print(f"   -> Stufe B: {verdictB}")

print("=" * 78)
print("Nachkontrolle (nach der Auswertung angehaengt, kein Kriterium): warum ist K(A0) = 0?")
Z = rng.normal(size=(N, N))
print(f"   K(zufaellig antisym.) = {np.linalg.norm(K(Z - Z.T)):.3f}, K(zufaellig sym.) = {np.linalg.norm(K(Z + Z.T)):.3f}  (K ist nicht trivial 0)")
basisA = []
for i in range(N):
    for j in range(i + 1, N):
        E = np.zeros((N, N)); E[i, j], E[j, i] = 1, -1; basisA.append(E)
MK = np.array([K(E).ravel() for E in basisA]).T
print(f"   Rang von K auf Lambda^2(27) (dim 351 = 52 + 273 unter F4): {np.linalg.matrix_rank(MK, 1e-9)}")
T0 = SO3[0]; cK = (K(T0) * T0).sum() / (T0 * T0).sum()
print(f"   K(T) = c T fuer T in so(3) c f4: c = {cK:.6f}, Rest {np.abs(K(T0) - cK * T0).max():.1e}")
print(f"   K(C) gesamt = {np.linalg.norm(K(C)):.1e}, K(P_t C P_t) = {np.linalg.norm(K(Pt @ C @ Pt)):.1e}")
print("   -> Auf Lambda^2 ist K = (3/2) * Projektor auf f4 (Schur: Lambda^2 27 = 52 + 273, Rang 52). C = L_e7 je Platz ist")
print("      orthogonal zu f4, also K(C) = 0 und alle A_n = 0. Das Ergebnis von Stufe B folgt aus der Wahl von K, nicht aus den Quarks.")
