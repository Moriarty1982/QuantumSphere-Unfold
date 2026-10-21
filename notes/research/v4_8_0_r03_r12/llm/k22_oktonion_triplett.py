"""k22: Echte G2-Wirkung auf das Generationen-Triplett (zu K18.4). Reine Algebra, kein Datenvergleich.
Oktonionen nach Companion-Konvention (r04): (p+q l)(r+s l) = (pr - conj(s) q) + (s p + q conj(r)) l,
e4 = l, e5 = e1 l, e6 = e2 l, e7 = e3 l. Endliche Gruppe: Automorphismen, die e1..e7 bis aufs Vorzeichen permutieren."""
import numpy as np, itertools
from collections import Counter

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
qc = lambda a: a*np.array([1, -1, -1, -1])
def omul(x, y):
    p, q, r, s = x[:4], x[4:], y[:4], y[4:]
    return np.concatenate([qmul(p, r) - qmul(qc(s), q), qmul(s, p) + qmul(q, qc(r))])
# Basis: Index 0 = 1; e1,e2,e3 = Quaternionen i,j,k; e4 = l, e5 = e1 l, e6 = e2 l, e7 = e3 l
E = np.eye(8)
basis = [E[0], E[1], E[2], E[3], E[4], E[5], E[6], E[7]]   # (p | q) mit q-Anteil = Koeffizient von l
# Multiplikationstabelle e_i e_j = sgn * e_k
T = {}
for i in range(1, 8):
    for j in range(1, 8):
        if i == j: continue
        v = omul(basis[i], basis[j]); k = int(np.argmax(abs(v))); T[i, j] = (int(np.sign(v[k])), k)
tri = sorted({tuple(sorted((i, j, T[i, j][1]))) for i in range(1, 8) for j in range(1, 8) if i != j})
print("Fano-Linien aus der Multiplikation:", tri)

def mul_signed(a, b):  # a, b = (Vorzeichen, Index)
    if a[1] == b[1]: return (-a[0]*b[0], 0)
    s, k = T[a[1], b[1]]; return (a[0]*b[0]*s, k)

# Automorphismen aus Bildern von e1, e2, e4 (Basis-Tripel)
G = []
for a in itertools.product((1, -1), range(1, 8)):
    for b in itertools.product((1, -1), range(1, 8)):
        if b[1] == a[1]: continue
        c = mul_signed(a, b)
        for d in itertools.product((1, -1), range(1, 8)):
            if d[1] in (a[1], b[1], c[1]): continue
            img = {1: a, 2: b, 3: c, 4: d, 5: mul_signed(a, d), 6: mul_signed(b, d), 7: mul_signed(c, d)}
            ok = all(mul_signed(img[i], img[j]) == ((lambda s, k: (s*img[k][0], img[k][1]) if k else (s, 0))(*T[i, j]))
                     for i in range(1, 8) for j in range(1, 8) if i != j)
            if ok:
                M = np.zeros((7, 7))
                for i in range(1, 8): M[img[i][1]-1, i-1] = img[i][0]
                G.append(M)
print("Ordnung der Gruppe:", len(G))

# Stabilisator von +e7; komplexe Struktur J = Linksmultiplikation mit e7 auf span(e1..e6)
H = [M for M in G if M[6, 6] == 1]
J = np.zeros((6, 6))
for k in range(1, 7):
    s, m = T[7, k]; J[m-1, k-1] = s
assert all(np.allclose(M[:6, :6] @ J, J @ M[:6, :6]) for M in H), "nicht komplex-linear"
f = [3, 4, 5]                                   # komplexe Basis f_k = e4, e5, e6 (Indizes 3..5)
def cmat(M):
    A = M[:6, :6]; C = np.zeros((3, 3), complex)
    for j, fj in enumerate(f):
        for k, fk in enumerate(f):
            col = A[:, fk]; C[j, k] = col[fj] + 1j*(J[:, fj] @ col)
    return C
R = [cmat(M) for M in H]
print("Stab(+e7): Ordnung", len(R), "; unitaer:", all(np.allclose(C.conj().T @ C, np.eye(3)) for C in R),
      "; det = 1:", all(np.isclose(np.linalg.det(C), 1) for C in R))
def ordn(C):
    X = C.copy(); k = 1
    while not np.allclose(X, np.eye(3)): X = X @ C; k += 1
    return k
stat = sorted(Counter(ordn(C) for C in R).items())
print("Elementordnungen Stab(+e7):", stat)
# Vergleich: Delta(96) = (Z4 x Z4) x| S3 in SU(3)
I4 = 1j
D = [np.diag([I4**k, I4**l, I4**(-k-l)]) for k in range(4) for l in range(4)]
perms = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]
P3 = [P if np.isclose(np.linalg.det(P), 1) else -P for P in perms]
D96 = [d @ p for d in D for p in P3]
print("Delta(96) zum Vergleich:     ", sorted(Counter(ordn(C) for C in D96).items()))
irr = np.mean([abs(np.trace(C))**2 for C in R])
print(f"<|Spur|^2> = {irr:.3f}  (=1 heisst: Triplett irreduzibel)")

# Mischung: Dreier-Element mit e4 -> e5 -> e6, Eigenbasis; danach alle Involutionen
def perm_of(M): return tuple(int(np.argmax(abs(M[:, i]))) + 1 for i in range(7))
g3 = [M for M in H if perm_of(M)[3:6] == (5, 6, 4) and ordn(cmat(M)) == 3]
C3 = cmat(g3[0]); w, V = np.linalg.eig(C3); i1 = int(np.argmin(abs(w - 1)))
print("\nDreier-Element (e4->e5->e6): Eigenwerte", np.round(w, 3))
lineL = (1, 2, 3)
res = Counter()
for M, C in zip(H, R):
    if ordn(C) != 2: continue
    ev, EV = np.linalg.eig(C); vals = np.round(ev.real).astype(int)
    single = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    coef = np.linalg.solve(V, EV[:, single]); mod = np.abs(coef)**2/np.sum(np.abs(coef)**2)
    p = perm_of(M)
    fixed = [i for i in range(1, 8) if p[i-1] == i]
    if len(fixed) == 7: typ = "Vorzeichen-Kern (Fano-Bild trivial)"
    else:
        # Zentrum der Fano-Transvektion: der Punkt, der mit seinem Bild ... ; Fixpunkte bilden die Achse
        moved = [i for i in range(1, 8) if p[i-1] != i]
        cen = [k for k in fixed if all(T[i, p[i-1]][1] == k for i in moved)]
        cen = cen[0] if cen else None
        typ = ("Zentrum e7" if cen == 7 else f"Zentrum in {{e1,e2,e3}}" if cen in lineL else f"Zentrum in {{e4,e5,e6}}")
    res[(typ, round(mod[i1], 4), tuple(sorted(np.round(mod, 4))))] += 1
print("Involutionen in Stab(+e7):")
for (typ, m1, mods), n in sorted(res.items()):
    print(f"  {typ:38s} x{n}: Anteil Eigenwert-1-Richtung {m1:.4f}, Betragsquadrate {mods}")

# Zuordnung Fano-Zentrum -> Mischungstyp (je Lift der Ordnung 2)
from collections import defaultdict
z = defaultdict(list)
for M, C in zip(H, R):
    if ordn(C) != 2: continue
    ev, EV = np.linalg.eig(C); vals = np.round(ev.real).astype(int)
    single = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    coef = np.linalg.solve(V, EV[:, single]); mod = np.abs(coef)**2/np.sum(np.abs(coef)**2)
    typ = {0.3333: "TM2", 0.6667: "TM1", 0.0: "TBM3"}.get(round(mod[i1], 4), "D96-Spalte") \
        if round(mod[i1], 4) != 0.3333 or np.allclose(sorted(mod), [1/3]*3, atol=1e-3) else "D96-Spalte"
    p = perm_of(M); moved = [i for i in range(1, 8) if p[i-1] != i]
    cen = [k for k in range(1, 8) if p[k-1] == k and moved and all(T[i, p[i-1]][1] == k for i in moved)]
    z[f"e{cen[0]}" if cen else "kein (Vorzeichen-Kern)"].append(typ)
print("\nFano-Zentrum -> Typen der Lifts der Ordnung 2:")
for k in sorted(z): print(f"  {k}: {sorted(z[k])}")
print("Fano-Involutionen mit Zentrum e7 haben nur Lifts der Ordnung 4 (siehe Klassenzaehlung).")
