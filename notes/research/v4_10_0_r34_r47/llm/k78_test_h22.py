"""k78: Test der Vorab-Notiz H22 (Commit ed74608): Triality-Form t = Re((xy)z) auf O^3 als Spin(8)-Triality,
Fixgruppe der Durchwanderung, und die Perioden der Struktur (tau, rho auf den Plaetzen, T, R auf dem C-Faktor)."""
import itertools, numpy as np, os, sys
from scipy.linalg import null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
T3 = np.array([[[omul(omul(E[i], E[j]), E[k])[0] for k in range(8)] for j in range(8)] for i in range(8)])
so8 = []
for a in range(8):
    for b in range(a + 1, 8):
        X = np.zeros((8, 8)); X[a, b] = 1; X[b, a] = -1; so8.append(X)
cols = ([np.einsum('mi,mjk->ijk', X, T3).ravel() for X in so8] +
        [np.einsum('mj,imk->ijk', X, T3).ravel() for X in so8] +
        [np.einsum('mk,ijm->ijk', X, T3).ravel() for X in so8])
M = np.column_stack(cols)                                    # 512 x 84
N = null_space(M, rcond=1e-12)
mat = lambda c: sum(c[s]*so8[s] for s in range(28))
trip = [(mat(N[:28, d]), mat(N[28:56, d]), mat(N[56:, d])) for d in range(N.shape[1])]
ranks = [np.linalg.matrix_rank(N[28*p:28*(p + 1)], TOL) for p in range(3)]
def intertw(p, q):
    K = np.vstack([np.kron(np.eye(8), tr[q]) - np.kron(tr[p].T, np.eye(8)) for tr in trip])   # X tr[p] = tr[q] X
    return 64 - np.linalg.matrix_rank(K, TOL)
iw = {(p, q): intertw(p, q) for p, q in ((0, 1), (0, 2), (1, 2))}
selfw = intertw(0, 0)
ok_a = N.shape[1] == 28 and ranks == [28, 28, 28] and all(v == 0 for v in iw.values()) and selfw == 1
print(f"H22a: dim g = {N.shape[1]} (28); Rang der Projektionen {ranks}; Verflechtungsraeume zwischen den Plaetzen {iw}"
      f" (0 = nicht aequivalent); Selbst-Verflechtung {selfw} (1 = irreduzibel, reeller Typ) -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H22b
shift_res = max(abs(M@np.concatenate([N[28:56, d], N[56:, d], N[:28, d]])).max() for d in range(N.shape[1]))
ok_b = shift_res < TOL and ok_a
print(f"\nH22b: tau bildet g auf sich ab (Rest {shift_res:.0e}), permutiert die Projektionen zyklisch;"
      f" aeusserer Automorphismus, da die Plaetze nicht aequivalent sind -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H22c
Md = M@np.vstack([np.eye(28)]*3)
Nd = null_space(Md, rcond=1e-12)
diagA = [mat(Nd[:, d]) for d in range(Nd.shape[1])]
rows = []
for i in range(8):
    for j in range(8):
        p = omul(E[i], E[j]); A = np.zeros((8, 64))
        for k in range(8):
            for m in range(8):
                A[k, 8*k + m] += p[m]
                A[:, 8*k + m] -= omul(E[k], E[j])*E[i][m]
                A[:, 8*k + m] -= omul(E[i], E[k])*E[j][m]
        rows.append(A)
Der = null_space(np.vstack(rows)); Ds = [Der[:, c].reshape(8, 8) for c in range(Der.shape[1])]
span_eq = np.linalg.matrix_rank(np.array([X.ravel() for X in diagA + Ds]), TOL)
Ne7 = null_space(np.array([X[:, 7] for X in diagA]).T, rcond=1e-12) if diagA else np.zeros((0, 0))
ok_c = len(diagA) == 14 and len(Ds) == 14 and span_eq == 14 and Ne7.shape[1] == 8
print(f"\nH22c: tau-feste Elemente (A,A,A): Dimension {len(diagA)}; Derivationen von O: {len(Ds)}; gemeinsamer Rang {span_eq}"
      f" (14 = gleich, G2); davon mit A e7 = 0: {Ne7.shape[1]} (SU(3)) -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H22d
rng = np.random.default_rng(78)
m = omul
brackets = {
    "((xy)z)w": lambda x, y, z, w: m(m(m(x, y), z), w)[0],
    "(x(yz))w": lambda x, y, z, w: m(m(x, m(y, z)), w)[0],
    "(xy)(zw)": lambda x, y, z, w: m(m(x, y), m(z, w))[0],
    "x((yz)w)": lambda x, y, z, w: m(x, m(m(y, z), w))[0],
    "x(y(zw))": lambda x, y, z, w: m(x, m(y, m(z, w)))[0]}
vs = [rng.normal(size=(4, 8)) for _ in range(20)]
dev4 = {name: max(abs(f(x, y, z, w) - f(y, z, w, x)) for x, y, z, w in vs) for name, f in brackets.items()}
dev3 = max(abs(m(m(x, y), z)[0] - m(m(y, z), x)[0]) for x, y, z, _ in vs)
ok_d = all(v > 1e-6 for v in dev4.values()) and dev3 < TOL
print(f"\nH22d: Kontrolle t zyklisch auf O^3: Abweichung {dev3:.0e}; vier Plaetze, Abweichung unter zyklischer Verschiebung:"
      + "".join(f"\n   {k}: {v:.3f}" for k, v in dev4.items()) + f"\n  -> H22d {'bestaetigt' if ok_d else 'widerlegt'} (schwach)")

# H22e
I8 = np.eye(8); Cj = np.diag([1] + [-1]*7)
def slot_op(perm, conj):                  # neuer Platz s = (conj) alter Platz perm[s]
    S = np.zeros((24, 24))
    for s, src in enumerate(perm):
        S[8*s:8*s + 8, 8*src:8*src + 8] = Cj if conj else I8
    return S
tau = np.kron(np.eye(2), slot_op((1, 2, 0), False))
rho = np.kron(np.eye(2), slot_op((0, 2, 1), True))
Tm = np.kron(np.diag([1., -1.]), np.eye(24))
Rm = np.kron(np.array([[0., -1.], [1., 0.]]), np.eye(24))
gens = [tau, rho, Tm, Rm]
key = lambda A: tuple(np.round(A, 6).ravel())
group = {key(np.eye(48)): np.eye(48)}; frontier = [np.eye(48)]
while frontier:
    new = []
    for A in frontier:
        for g in gens:
            B = g@A; k = key(B)
            if k not in group: group[k] = B; new.append(B)
    frontier = new
def order(A):
    P = A.copy()
    for n in range(1, 100):
        if np.allclose(P, np.eye(48)): return n
        P = A@P
orders = sorted({order(A) for A in group.values()})
comm = max(abs(a@b - b@a).max() for a in (tau, rho) for b in (Tm, Rm))
def t3(v): x, y, z = v[:8], v[8:16], v[16:24]; return m(m(x, y), z)[0]
tinv = max(max(abs(t3(slot_op((1, 2, 0), False)@v) - t3(v)), abs(t3(slot_op((0, 2, 1), True)@v) - t3(v)))
           for v in rng.normal(size=(20, 24)))
from collections import Counter
cnt = Counter(order(A) for A in group.values())
ok_e = len(group) == 48 and orders == [1, 2, 3, 4, 6, 12] and comm < TOL and tinv < TOL
print(f"\nH22e: Gruppenordnung {len(group)} (48); Elementordnungen {orders} mit Anzahlen {dict(sorted(cnt.items()))};"
      f" [tau/rho, T/R] = {comm:.0e}; t unter tau, rho invariant: {tinv:.0e} -> {'bestaetigt' if ok_e else 'widerlegt'}")

# Nachkontrolle zu H22d (nach der Auswertung, kein Teil des Kriteriums): zwei Klassen von Klammerungen
fA, fB = brackets["((xy)z)w"], brackets["(x(yz))w"]
same_A = max(abs(fA(*v) - brackets[k](*v)) for v in vs for k in ("(xy)(zw)", "x(y(zw))"))
same_B = max(abs(fB(*v) - brackets["x((yz)w)"](*v)) for v in vs)
swap = max(abs(fA(y, z, w, x) - fB(x, y, z, w)) + abs(fB(y, z, w, x) - fA(x, y, z, w)) for x, y, z, w in vs)
summ = max(abs(fA(x, y, z, w) + fB(x, y, z, w) - fA(y, z, w, x) - fB(y, z, w, x)) for x, y, z, w in vs)
print(f"\nNachkontrolle H22d: Klasse A = ((xy)z)w = (xy)(zw) = x(y(zw)) ({same_A:.0e}), Klasse B = (x(yz))w = x((yz)w) ({same_B:.0e});"
      f" die Verschiebung tauscht A und B ({swap:.0e}); A + B ist zyklisch invariant ({summ:.0e}). H22d liefert also kein Verbot.")
