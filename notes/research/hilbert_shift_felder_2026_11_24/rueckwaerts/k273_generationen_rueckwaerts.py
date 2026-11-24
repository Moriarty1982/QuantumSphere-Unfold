"""k273 (Erkundung, nicht blind, 24.11.2026): Was verlangen drei Generationen rueckwaerts vom Turm?
A  CP-Verletzung in der Mischung: Zahl der Phasen (N-1)(N-2)/2; N = 2 hat J = 0 identisch (Vollstaendigkeit);
   N = 3: Im(V_ij V_kl V*_il V*_kj) = J * sum eps_ikm eps_jln (eine Phase, getragen von eps).
   J als Bargmann-Viereck Tr(P_i Q_j P_k Q_l) (Flavour- und Massenprojektoren).
B  Wo hat der Turm ein eps (Kreuzprodukt)? x × y := Im(xy) auf Im A_n: |x×y|^2 = |x|^2|y|^2 - (x.y)^2 nur fuer n = 2, 3.
C  Wie traegt HS(2) eine Dreiergruppe? Aut(H) = SO(3) auf Im H (Vektor, eps invariant) gegen Multiplikation L_q (Spin 1/2, Dublett).
D  Zweite Bott-Periode: antikommutierende Achsen ueber dem ersten Oktonion-Block 0,1,3,7 (n = 4..7);
   Achsen, die mit allen 8 Block-Achsen antikommutieren, vertauschen mit allen Bilinearen (Farbe, Ladung). Ihr Modul ist ein Dublett.
Aufruf aus diesem Ordner: python3 k273_generationen_rueckwaerts.py
"""
import itertools
import numpy as np
from scipy.stats import unitary_group

rng = np.random.default_rng(273)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


def eps(i, j, k):
    return int(np.sign(np.linalg.det(np.eye(3)[[i, j, k]]))) if len({i, j, k}) == 3 else 0


print("=" * 78)
print("A  CP-Phase und Generationenzahl")
for N in (2, 3, 4, 5):
    print(f"   N={N}: Winkel {N*(N-1)//2}, CP-Phasen {(N-1)*(N-2)//2}")
J2 = max(abs(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))
         for V in [unitary_group.rvs(2, random_state=rng) for _ in range(200)])
print(f"   N=2: max |Im(V11 V22 V12* V21*)| ueber 200 Zufallsmatrizen = {J2:.1e}  (J = 0 identisch)")
V = unitary_group.rvs(3, random_state=rng)
J = np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0]))
dev = 0
for i, j, k, l in itertools.product(range(3), repeat=4):
    lhs = np.imag(V[i, j] * V[k, l] * np.conj(V[i, l]) * np.conj(V[k, j]))
    rhs = J * sum(eps(i, k, m) * eps(j, l, n) for m in range(3) for n in range(3))
    dev = max(dev, abs(lhs - rhs))
print(f"   N=3: J = {J:+.4f}; Im(V_ij V_kl V*_il V*_kj) = J sum eps eps, Abw. {dev:.1e}  (eine Phase, getragen von eps_ijk)")
# Bargmann-Viereck: P_i = |i><i| (Flavour), Q_j = |v_j><v_j| (Massenbasis, Spalten von V)
P = [np.outer(np.eye(3)[i], np.eye(3)[i]) for i in range(3)]
Q = [np.outer(V[:, j], np.conj(V[:, j])) for j in range(3)]
B = np.trace(P[0] @ Q[0] @ P[1] @ Q[1])
print(f"   Bargmann-Viereck Tr(P1 Q1 P2 Q2) = {B:.4f}; Im = {np.imag(B):+.4f} gegen J = {J:+.4f}"
      f"  (|Im B| = |J|: {abs(abs(np.imag(B)) - abs(J)) < 1e-12})")
# N=4: drei unabhaengige Quartett-Invarianten
V4 = unitary_group.rvs(4, random_state=rng)
quart = [np.imag(V4[i, j] * V4[k, l] * np.conj(V4[i, l]) * np.conj(V4[k, j]))
         for (i, k) in itertools.combinations(range(4), 2) for (j, l) in itertools.combinations(range(4), 2)]
# Rang der Ableitung der Quartette nach den Parametern ~ Zahl unabhaengiger Phasen (numerisch ueber Stichprobe)
samples = []
for _ in range(40):
    W = unitary_group.rvs(4, random_state=rng)
    samples.append([np.imag(W[i, j] * W[k, l] * np.conj(W[i, l]) * np.conj(W[k, j]))
                    for (i, k) in itertools.combinations(range(4), 2) for (j, l) in itertools.combinations(range(4), 2)])
print(f"   N=4: 36 Quartette, davon linear unabhaengig (ueber 40 Stichproben) {np.linalg.matrix_rank(np.array(samples), tol=1e-9)}: nicht mehr J * eps eps")

print("=" * 78)
print("B  Kreuzprodukt x × y = Im(xy) auf Im A_n")
for n in range(1, 6):
    D = 2 ** n
    worst = 0.0
    for _ in range(300):
        x = rng.normal(size=D); y = rng.normal(size=D); x[0] = y[0] = 0
        c = mul(x, y); c[0] = 0
        worst = max(worst, abs(c @ c - ((x @ x) * (y @ y) - (x @ y) ** 2)))
    print(f"   n={n} (Im-Dim {D-1:2d}): max | |x×y|^2 - (|x|^2|y|^2 - (x.y)^2) | = {worst:.1e}")
print("   -> echtes Kreuzprodukt nur auf Im H (3) und Im O (7); eps_ijk genau auf Im H.")

print("=" * 78)
print("C  HS(2) als Traeger: Vektor (Automorphismen) gegen Dublett (Multiplikation)")
E4 = np.eye(4)
q = rng.normal(size=4); q /= np.linalg.norm(q)
R = np.array([[mul(mul(q, E4[a]), conj(q))[b] for a in range(1, 4)] for b in range(1, 4)])
print(f"   Aut: x -> q x q*, auf Im H: R^T R = 1 (Abw. {np.abs(R.T @ R - np.eye(3)).max():.1e}), det R = {np.linalg.det(R):+.3f}"
      "  -> Vektor (Spin 1), drei reelle Richtungen")
tp = lambda x, y, z: mul(x, mul(y, z))[0]
x, y, z = [np.concatenate([[0], rng.normal(size=3)]) for _ in range(3)]
Rx = lambda v: np.concatenate([[0], R @ v[1:]])
print(f"   Tripelprodukt Re(x(yz)) = -det[x,y,z]: {tp(x, y, z):+.4f} gegen {-np.linalg.det(np.array([x[1:], y[1:], z[1:]])):+.4f};"
      f" invariant unter Aut: {abs(tp(Rx(x), Rx(y), Rx(z)) - tp(x, y, z)) < 1e-12}")
# Multiplikation: L_i, L_j, L_k auf H = C^2 (komplexe Struktur R_i): Paulimatrizen -> Dublett
L = [np.array([mul(E4[a], E4[b]) for b in range(4)]).T for a in range(1, 4)]
gens = [0.5 * Li for Li in L]
cas = sum(g @ g for g in gens)
print(f"   Mult: (L_i/2)^2 summiert = {np.round(np.linalg.eigvalsh(cas), 3)} = -j(j+1) mit j = 1/2 -> Dublett (2 komplexe Zustaende)")
print("   -> Drei Generationen als Triplett verlangen Im H unter Automorphismen (adjungiert), nicht unter Multiplikation.")
print("      Die reelle Eins ist dabei Singulett: H = 1 + 3; eine vierte Richtung waere kein Mitglied der Familie.")

print("=" * 78)
print("D  Zweite Bott-Periode: Achsen ueber dem Oktonion-Block")


def table(N):
    E = np.eye(N); C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N):
            C[i, j] = mul(E[i], E[j])
    return C


def max_clique(adj, cand, cur, best):
    if len(cur) + len(cand) <= len(best[0]):
        return
    if not cand:
        best[0] = list(cur); return
    for v in list(cand):
        max_clique(adj, [w for w in cand if w > v and adj[v][w]], cur + [v], best)
        cand = [w for w in cand if w != v]
        if len(cur) + len(cand) <= len(best[0]):
            return


for n in range(4, 7):
    Nn = 2 ** n
    C = table(Nn)
    Ls = [C[i].T for i in range(Nn)]
    ac = lambda a, b: np.abs(Ls[a] @ Ls[b] + Ls[b] @ Ls[a]).max() < 1e-9
    block = list(range(1, 8))
    cand = [v for v in range(8, Nn) if all(ac(v, b) for b in block)]
    adj = {v: {w: ac(v, w) for w in cand} for v in cand}
    best = [[]]
    max_clique(adj, sorted(cand), [], best)
    extra = best[0]
    comm = max((np.abs(Ls[e] @ Ls[a] @ Ls[b] - Ls[a] @ Ls[b] @ Ls[e]).max()
                for e in extra for a, b in itertools.combinations(block, 2)), default=0.0)
    line = (f"   n={n}: Block e1..e7 + {len(extra)} antikommutierende Achsen {[f'e{e}' for e in extra]} "
            f"(gesamt {7 + len(extra)}); [Extra, Block-Bilineare] max {comm:.1e}")
    if len(extra) >= 3:
        # drei Extra-Achsen: so(3) aus Paaren, Casimir
        x = extra[:3]
        T = [0.5 * Ls[x[1]] @ Ls[x[2]], 0.5 * Ls[x[2]] @ Ls[x[0]], 0.5 * Ls[x[0]] @ Ls[x[1]]]
        cas = sum(g @ g for g in T)
        line += f"\n          so(3) aus den drei Extra-Achsen: Casimir {np.unique(np.round(np.linalg.eigvalsh(cas), 6))} -> j = 1/2 (Dublett)"
    print(line)
print("   Radon-Hurwitz erlaubt 8, 9, 11 Achsen fuer n = 4, 5, 6. Mit festem Block und Basis-Einheiten (exakte Cliquensuche) sind es 8, 9, 10;")
print("   eine elfte Achse waere nur in einer Nicht-Basis-Richtung moeglich (hier nicht gesucht).")
