"""k81: Test der Vorab-Notiz H25 (Commit d1aba48): zweiseitige Kontraktion ueber mehrere Frames (Vorderseite C-Faktor mit
R, T, J_B), Zentralisator der Farbe in der Triality-Algebra, zwei SU(2) von links und rechts auf W = C (x) H (x) O."""
import numpy as np, os, sys
from scipy.linalg import null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
rng = np.random.default_rng(81)
E = np.eye(8)

# ---------- Frame-Abbildungen auf der Vorderseite (C-Faktor)
frames = {"R": (lambda X: 1j*X, lambda w: -1j*w),
          "T": (lambda X: X.conj(), lambda w: w.conj()),
          "J_B": (lambda X: 1j*X.conj(), lambda w: -1j*w.conj())}
cplx = lambda n: rng.normal(size=n) + 1j*rng.normal(size=n)
G = rng.normal(size=(8, 8)); G = G + G.T
samples = [(cplx(8), cplx(8)) for _ in range(20)]
# H25b
dev_b = {}
for name, (fX, fw) in frames.items():
    inv = max(abs(fw(w)@fX(X) - w@X) for X, w in samples)
    con = max(abs(fw(w)@fX(X) - (w@X).conj()) for X, w in samples)
    dev_b[name] = ("invariant" if inv < TOL else "konjugiert" if con < TOL else f"weder ({inv:.2f}, {con:.2f})")
ok_b = dev_b == {"R": "invariant", "T": "konjugiert", "J_B": "konjugiert"}
print(f"H25b: klassische Kontraktion omega_a X^a unter den Frames: {dev_b} -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H25c
q = lambda X: X@G@X
h = lambda X: X.conj()@G@X
want = {"R": lambda v: -v, "T": lambda v: v.conjugate(), "J_B": lambda v: -v.conjugate()}
dev_q = {n: max(abs(q(f[0](X)) - want[n](q(X))) for X, _ in samples) for n, f in frames.items()}
# D4 vollstaendig: erzeugt von R und T, acht Elemente (als Funktionen auf X)
def compose(f, g): return lambda X: f(g(X))
d4 = {"1": lambda X: X}
gens = {"R": frames["R"][0], "T": frames["T"][0]}
words = {"1": d4["1"]}
frontier = ["1"]
X0 = cplx(8)
def keyf(f): return tuple(np.round(f(X0), 8))
seen = {keyf(words["1"]): "1"}
while frontier:
    nw = []
    for w in frontier:
        for gn, g in gens.items():
            f = compose(g, words[w]); k = keyf(f)
            if k not in seen: seen[k] = gn + "." + w; words[gn + "." + w] = f; nw.append(gn + "." + w)
    frontier = nw
dev_h = max(abs(h(f(X)) - h(X)) for f in words.values() for X, _ in samples)
ok_c = all(v < TOL for v in dev_q.values()) and len(words) == 8 and dev_h < TOL
print(f"\nH25c: bilineare Form q: Abweichung von (R: -q, T: conj q, J_B: -conj q) {dict((k, f'{v:.0e}') for k, v in dev_q.items())};"
      f" D4 hat {len(words)} Elemente; hermitesche Form h unter allen invariant: {dev_h:.0e} -> {'bestaetigt' if ok_c else 'widerlegt'}")

# ---------- Triality-Algebra g (wie k78)
T3 = np.array([[[omul(omul(E[i], E[j]), E[k])[0] for k in range(8)] for j in range(8)] for i in range(8)])
pairs = [(a, b) for a in range(8) for b in range(a + 1, 8)]
so8 = []
for a, b in pairs:
    X = np.zeros((8, 8)); X[a, b] = 1; X[b, a] = -1; so8.append(X)
M = np.column_stack([np.einsum('mi,mjk->ijk', X, T3).ravel() for X in so8] +
                    [np.einsum('mj,imk->ijk', X, T3).ravel() for X in so8] +
                    [np.einsum('mk,ijm->ijk', X, T3).ravel() for X in so8])
N = null_space(M, rcond=1e-12)
mat = lambda c: sum(c[s]*so8[s] for s in range(28))
trip = lambda y: tuple(mat((N@y)[28*p:28*(p + 1)]) for p in range(3))
Nd = null_space(M@np.vstack([np.eye(28)]*3), rcond=1e-12)       # g2 diagonal
g2 = [mat(Nd[:, d]) for d in range(Nd.shape[1])]
S = null_space(np.array([A[:, 7] for A in g2]).T, rcond=1e-12)
su3 = [sum(S[k, c]*g2[k] for k in range(len(g2))) for c in range(S.shape[1])]
assert len(g2) == 14 and len(su3) == 8
# H25d: Zentralisator von su3 (diagonal) in g
basis = [trip(np.eye(28)[d]) for d in range(28)]
rows = []
for s in su3:
    cols = [np.concatenate([(A@s - s@A).ravel() for A in t]) for t in basis]
    rows.append(np.column_stack(cols))
Cz = null_space(np.vstack(rows), rcond=1e-12)
cent = [trip(Cz[:, c]) for c in range(Cz.shape[1])]
abel = max((abs(a[p]@b[p] - b[p]@a[p]).max() for a in cent for b in cent for p in range(3)), default=0)
# W = C (x) H (x) O
def hmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
E4 = np.eye(4)
Lh = [np.array([hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
Rh = [np.array([hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
I2, I4, I8 = np.eye(2), np.eye(4), np.eye(8)
Tm, Rm = np.diag([1., -1.]), np.array([[0., -1.], [1., 0.]])
front = [np.kron(np.kron(Tm, I4), I8), np.kron(np.kron(Rm, I4), I8)] + [np.kron(np.kron(I2, Lh[a]), I8) for a in (1, 2, 3)]
back = [np.kron(np.kron(I2, Rh[a]), I8) for a in (1, 2, 3)] + [np.kron(np.kron(I2, I4), s) for s in su3]
comm_W = max(abs(f@b - b@f).max() for f in front for b in back)
suL = max(abs(Lh[1]@Lh[2] - Lh[2]@Lh[1] - 2*Lh[3]).max(), 0)
suR = max(abs(Rh[1]@Rh[2] - Rh[2]@Rh[1] + 2*Rh[3]).max(), 0)
LR = max(abs(Lh[a]@Rh[b] - Rh[b]@Lh[a]).max() for a in (1, 2, 3) for b in (1, 2, 3))
ok_d = Cz.shape[1] == 2 and abel < TOL and comm_W < TOL and suL < TOL and suR < TOL and LR < TOL
print(f"\nH25d: Zentralisator von su(3)_c in g: Dimension {Cz.shape[1]}, abelsch {abel:.0e};"
      f" auf W: L_q und R_q je su(2) ({suL:.0e}, {suR:.0e}), vertauschen untereinander ({LR:.0e}) und mit su(3)_c, D4"
      f" -> {'bestaetigt' if ok_d else 'widerlegt'}")
# H25a (Kontrolle)
print(f"\nH25a: vordere (D4, L_q) und hintere (R_q, su(3)_c) Abbildungen vertauschen auf W: {comm_W:.0e}"
      f" -> {'bestaetigt' if comm_W < TOL else 'widerlegt'} (Kontrolle)")
# H25e
ranks = [np.linalg.matrix_rank(N[28*p:28*(p + 1)], TOL) for p in range(3)]
ok_e = ranks == [28, 28, 28]
print(f"\nH25e: Projektionen von g auf die Plaetze injektiv (Rang {ranks}): kein Element wirkt nur auf einem Spinor-Platz"
      f" -> {'bestaetigt' if ok_e else 'widerlegt'} (Kontrolle)")

# Nachkontrolle (nach der Auswertung, kein Teil des Kriteriums): Wird der Zentralisator der Farbe von L_e7, R_e7 aufgespannt?
L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
for p in range(3):
    span = np.linalg.matrix_rank(np.array([c[p].ravel() for c in cent] + [L7.ravel(), R7.ravel()]), TOL)
    print(f"Nachkontrolle Platz {p + 1}: Rang von Zentralisator + {{L_e7, R_e7}} = {span} (2 = gleicher Raum)")
