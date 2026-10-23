"""k87: Test der Vorab-Notiz H31 (Commit ea74447): Verschiebungs-Readouts (aus P^(2^j)) vertauschen mit tau und erzeugen
keine Mischung; Art-Masken (diagonale Projektoren auf Generationen) brechen tau und erzeugen Mischung, linear in der Gewichtung."""
import itertools, numpy as np

TOL = 1e-9
rng = np.random.default_rng(87)
P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
mp = np.linalg.matrix_power
def herm_circ(a, b): return a*np.eye(3) + b*P + np.conj(b)*P.conj().T
def rand_circ(): return herm_circ(rng.normal()*3, rng.normal() + 1j*rng.normal())
def mixing(Mu, Md):
    wu, Uu = np.linalg.eigh(Mu); wd, Ud = np.linalg.eigh(Md)
    return abs(Uu.conj().T@Ud), wu, wd
def perm_dev(V):                                            # Abstand von |V| zur naechsten Permutationsmatrix
    best = 9
    for p in itertools.permutations(range(3)):
        Pm = np.zeros((3, 3)); Pm[range(3), p] = 1
        best = min(best, abs(V - Pm).max())
    return best

# H31a
ok_a = True; maxc = 0; maxdev = 0
for _ in range(200):
    kind = rng.integers(3)
    if kind == 0:                                           # Produkt (Lesart Sigma)
        js = rng.integers(0, 6, size=rng.integers(1, 5)); X = np.eye(3, dtype=complex)
        for j in js: X = X@mp(P, 2**int(j))
    elif kind == 1:                                         # Mittel ueber erzeugte Untergruppe (Lesart Vee)
        js = rng.integers(0, 6, size=rng.integers(1, 4))
        H = {0}
        for _ in range(4): H |= {(h + 2**int(j)) % 3 for h in H for j in js}
        X = sum(mp(P, h) for h in H)/len(H)
    else:                                                   # Selektor-Kontraktion
        chi = rng.normal(size=(6, 6)) + 1j*rng.normal(size=(6, 6))
        X = sum(chi[m, n]*mp(P, 2**m + 2**n) for m in range(6) for n in range(6))
    X = X + X.conj().T
    maxc = max(maxc, abs(X@P - P@X).max())
    V, _, _ = mixing(rand_circ() + X, rand_circ() + rng.normal()*X)
    maxdev = max(maxdev, perm_dev(V))
ok_a = maxc < TOL and maxdev < 1e-7
print(f"H31a: 200 Verschiebungs-Readouts: [X, tau] max {maxc:.0e}; Abstand |V| zur Permutation max {maxdev:.0e}"
      f" -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H31b
subsets = [S for r in (1, 2) for S in itertools.combinations(range(3), r)]
D = {S: np.diag([1.0 if i in S else 0.0 for i in range(3)]) for S in subsets}
comm = min(abs(D[S]@P - P@D[S]).max() for S in subsets)
mind = 9
for _ in range(200):
    S = subsets[rng.integers(len(subsets))]; delta = 0.3
    V, _, _ = mixing(rand_circ() + delta*D[S], rand_circ() + delta*D[S])
    mind = min(mind, perm_dev(V))
ok_b = comm > 0.5 and mind > 1e-6
print(f"\nH31b: Art-Masken vertauschen nicht mit tau (min |[D, tau]| = {comm:.2f}); mit delta = 0.3 und gleicher Maske fuer up und down:"
      f" kleinster Abstand |V| zur Permutation {mind:.2e} -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H31c
ratios = []; bounds = []
for _ in range(200):
    Mu, Md = rand_circ(), rand_circ(); S = subsets[rng.integers(len(subsets))]
    gu = min(np.diff(np.linalg.eigvalsh(Mu))); gd = min(np.diff(np.linalg.eigvalsh(Md)))
    r = []
    for delta in (1e-3, 1e-4):
        V, _, _ = mixing(Mu + delta*D[S], Md + delta*D[S])
        r.append(perm_dev(V)/delta)
    ratios.append(r[0]/r[1] if r[1] > 0 else np.nan)
    bounds.append(r[1]/(1/gu + 1/gd))
ratios = np.array(ratios); bounds = np.array(bounds)
ok_c = np.nanmax(abs(ratios - 1)) < 0.05 and bounds.max() < 1.05
print(f"\nH31c: Abstand/delta bei delta = 1e-3 gegen 1e-4: Verhaeltnis in [{np.nanmin(ratios):.4f}, {np.nanmax(ratios):.4f}] (linear);"
      f" Abstand/delta <= (1/Luecke_u + 1/Luecke_d) * {bounds.max():.3f} -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H31d
ok_d = all(abs(D[S].conj() - D[S]).max() < TOL for S in subsets)
print(f"\nH31d: Art-Masken reell, vertauschen mit T (komplexe Konjugation): {ok_d} -> {'bestaetigt' if ok_d else 'widerlegt'}")
