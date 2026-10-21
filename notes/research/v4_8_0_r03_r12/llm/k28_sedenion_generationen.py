"""k28: Trennung von Farbe und Generation ueber die Sedenionen (Aut(S) = G2 x S3). Reine Algebra.
Cayley-Dickson wie im Companion (r04): (p+q l)(r+s l) = (pr - conj(s) q) + (s p + q conj(r)) l,
angewandt einmal (H -> O, l = e4) und noch einmal (O -> S, l = e8). Basis e0..e15, e_{i+8} = e_i e8."""
import numpy as np, contextlib, io, os
from scipy.linalg import expm, null_space
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k22_oktonion_triplett.py")).read().split("# Mischung:")[0])
oc = lambda a: a*np.array([1] + [-1]*7)
def smul(x, y):
    p, q, r, s = x[:8], x[8:], y[:8], y[8:]
    return np.concatenate([omul(p, r) - omul(oc(s), q), omul(s, p) + omul(q, oc(r))])
E = np.eye(16)
rng = np.random.default_rng(28)
def is_aut(A, n=40):
    for _ in range(n):
        x, y = rng.normal(size=16), rng.normal(size=16)
        if not np.allclose(A @ smul(x, y), smul(A @ x, A @ y), atol=1e-9): return False
    return True
print("e1 e8 = e9? ", np.allclose(smul(E[1], E[8]), E[9]), "| Sedenionen nicht alternativ:",
      not np.allclose(smul(smul(E[3]+E[10], E[3]+E[10]), E[6]-E[15]), smul(E[3]+E[10], smul(E[3]+E[10], E[6]-E[15]))))

# psi und eps (Gillard-Gresnigt, Gl. 47 ff.): Drehung um 2pi/3 in den Ebenen (e_i, e_{i+8}); eps: e_{i+8} -> -e_{i+8}
c, s = -0.5, np.sqrt(3)/2
psi = np.eye(16); eps = np.eye(16)
for i in range(1, 8):
    psi[i, i] = c; psi[i+8, i] = -s; psi[i, i+8] = s; psi[i+8, i+8] = c
    eps[i+8, i+8] = -1
eps[8, 8] = -1                       # a + b e8 -> a - b e8 negiert auch e8 selbst
for name, A in (("psi", psi), ("eps", eps)):
    print(f"{name} ist Automorphismus der Sedenionen (Companion-Konvention): {is_aut(A)}")
# Falls psi mit dieser Drehrichtung nicht passt, die andere pruefen
psi_alt = psi.T.copy()
print("psi (Gegenrichtung) ist Automorphismus:", is_aut(psi_alt))
P = psi if is_aut(psi) else psi_alt
print("psi^3 = 1:", np.allclose(np.linalg.matrix_power(P, 3), np.eye(16)), "| eps^2 = 1:", np.allclose(eps @ eps, np.eye(16)),
      "| eps psi eps = psi^-1 (Diedergruppe S3):", np.allclose(eps @ P @ eps, np.linalg.inv(P)))

# G2 diagonal: g(a + b e8) = g(a) + g(b) e8. (a) alle 1344 Vorzeichen-Permutationen, (b) zufaellige G2-Elemente
def diag_g(M7):
    D = np.eye(16); D[1:8, 1:8] = M7; D[9:16, 9:16] = M7; return D
print("Diagonale G2-Wirkung ist Automorphismus (Stichprobe 20 von 1344):", all(is_aut(diag_g(M), 10) for M in G[:20]))
print("psi und eps kommutieren mit allen 1344 diagonalen Elementen:",
      all(np.allclose(diag_g(M) @ P, P @ diag_g(M)) and np.allclose(diag_g(M) @ eps, eps @ diag_g(M)) for M in G))
# Derivationen von O (Lie-Algebra g2): D(xy) = D(x) y + x D(y), D(1) = 0
rows = []
basisO = [np.eye(8)[k] for k in range(8)]
for i in range(8):
    for j in range(8):
        xy = omul(basisO[i], basisO[j])
        # lineare Gleichung in den 64 Eintraegen von D (8x8)
        R = np.zeros((8, 64))
        for a in range(8):
            for b in range(8):
                Eab = np.zeros((8, 8)); Eab[a, b] = 1
                R[:, a*8+b] = Eab @ xy - omul(Eab @ basisO[i], basisO[j]) - omul(basisO[i], Eab @ basisO[j])
        rows.append(R)
Dsp = null_space(np.vstack(rows))
print("Dimension der Derivationsalgebra von O (g2 = 14):", Dsp.shape[1])
ok = True
for _ in range(5):
    Dm = (Dsp @ rng.normal(size=Dsp.shape[1])).reshape(8, 8)
    g = expm(Dm)
    Gs = np.eye(16); Gs[:8, :8] = g; Gs[8:, 8:] = g
    ok &= is_aut(Gs, 10) and np.allclose(Gs @ P, P @ Gs) and np.allclose(Gs @ eps, eps @ Gs)
print("Zufaellige kontinuierliche G2-Elemente: Automorphismen und vertauschen mit psi, eps:", ok)

# Farb-SU(3) = Stabilisator von e7 in G2: Derivationen mit D(e7) = 0
Dsu3 = [ (Dsp @ v).reshape(8, 8) for v in null_space(np.vstack([(Dsp[:, k].reshape(8, 8) @ basisO[7]) for k in range(Dsp.shape[1])]).T).T ]
print("Dimension der Farbalgebra (Stab e7 in g2, su(3) = 8):", len(Dsu3))

# Triolen-Relation: auf span(e_i, e_{i+8}) gilt 1 + psi + psi^2 = 0; fest bleiben genau e0 und e8
T3 = np.eye(16) + P + P @ P
print("Fixraum von psi:", [k for k in range(16) if np.allclose(P[:, k], E[k])],
      "| 1+psi+psi^2 verschwindet auf den 14 Ebenen-Richtungen:", np.allclose(T3[:, [*range(1, 8), *range(9, 16)]], 0))

# Drei Oktonionen-Unteralgebren O_k = psi^k(O): Unteralgebren? verschieden? Schnitt?
def span(k): return np.linalg.matrix_power(P, k)[:, :8]
for k in range(3):
    B = span(k)
    closed = all(np.allclose((np.eye(16) - B @ np.linalg.pinv(B)) @ smul(B[:, i], B[:, j]), 0) for i in range(8) for j in range(8))
    print(f"O_{k} = psi^{k}(O) ist Unteralgebra: {closed}")
for a_, b_ in ((0, 1), (0, 2), (1, 2)):
    M = np.hstack([span(a_), span(b_)]); print(f"dim(O_{a_} ∩ O_{b_}) =", 16 - np.linalg.matrix_rank(M))
print("dim(O_0 + O_1 + O_2) =", np.linalg.matrix_rank(np.hstack([span(0), span(1), span(2)])))
# Farbtriplett in jeder Kopie: psi^k(e4), psi^k(e5), psi^k(e6) -> 3 Generationen x 3 Farben
trip = np.hstack([np.linalg.matrix_power(P, k)[:, [4, 5, 6]] for k in range(3)])
print("Rang der 9 Vektoren psi^k(e_c), c = 4,5,6, k = 0,1,2:", np.linalg.matrix_rank(trip), "(9 waeren voll unabhaengig)")

# ---- S3-Zerlegung der Sedenionen: Spuren von psi und eps
print("\nSpuren auf S: tr(psi) =", round(np.trace(P), 6), " tr(eps) =", round(np.trace(eps), 6))
print("Charakter von 1 + sgn + 7*Standard: psi -> 1 + 1 + 7*(-1) = -5, eps -> 1 - 1 + 7*0 = 0")
print("psi-Eigenwerte auf einer Ebene (e4, e12):", np.round(np.linalg.eigvals(P[np.ix_([4, 12], [4, 12])]), 4))

# ---- Gegenprobe: Triality-Form t(x,y,z) = Re((xy)z) auf O + O + O
def t(x, y, z): return omul(omul(x, y), z)[0]
X = [rng.normal(size=8) for _ in range(3)]
cyc = np.isclose(t(*X), t(X[1], X[2], X[0]))
oconj = lambda a: a*np.array([1] + [-1]*7)
refl = np.isclose(t(*X), t(oconj(X[0]), oconj(X[2]), oconj(X[1])))
print("\nTriality-Form: zyklisch invariant (Triole Z3):", cyc, "| invariant unter (x,y,z) -> (conj x, conj z, conj y):", refl)
g2ok = True
for _ in range(5):
    g = expm((Dsp @ rng.normal(size=Dsp.shape[1])).reshape(8, 8))
    g2ok &= np.isclose(t(*X), t(*(g @ x for x in X)))
print("diagonal G2-invariant:", g2ok, "(G2 wirkt auf alle drei Kopien gleich, vertauscht also mit der S3-Permutation)")
# 3 Kopien des Farbtripletts (e4,e5,e6) in O+O+O: Rang
trip3 = np.zeros((24, 9))
for k in range(3):
    for j, cidx in enumerate((4, 5, 6)): trip3[8*k + cidx, 3*k + j] = 1
print("Rang der 9 Zustaende (3 Generationen x 3 Farben) in O+O+O:", np.linalg.matrix_rank(trip3))

# ---- Mischung aus reiner S3 (Generationen): Z3 = zyklische Vertauschung, Z2 = Transposition (mit/ohne Vorzeichen)
w3 = np.exp(2j*np.pi/3)
F = np.array([[1, 1, 1], [1, w3, w3**2], [1, w3**2, w3]])/np.sqrt(3)       # Eigenbasis der Zyklik, Spalte 0 = Eigenwert 1
for name, tau in (("Transposition (2 3)", np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])),
                  ("-Transposition (mit Konjugation auf Im O)", -np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]))):
    ev, EV = np.linalg.eigh(tau.astype(float)); vals = np.round(ev).astype(int)
    u = EV[:, [i for i in range(3) if list(vals).count(vals[i]) == 1][0]]
    mod = np.abs(F.conj().T @ u)**2
    print(f"{name}: erhaltene Spalte in der Triolen-Eigenbasis |U|^2 = {np.round(mod, 4)}  -> theta13 = 0")
