"""k326c (nachtraeglich, Erkundung zu H143): Stammen die 45 Fuenferauswahlen mit einer Rest-Generation alle aus einer der 9 Viererauswahlen
von H142 (plus eine beliebige fuenfte Kopie), oder gibt es neue Fuenf-Term-Relationen mit Summe 0?"""
import itertools, numpy as np
F = [np.array([np.cos(t), np.sin(t)]) for t in (0, 2*np.pi/3, 4*np.pi/3)]
VS = np.array([np.kron(a, b) for a in F for b in F])
def R0(idx): A = np.vstack([VS[list(idx)].T, np.ones(len(idx))]); return len(idx) - np.linalg.matrix_rank(A, tol=1e-10)
q = [i for i in itertools.combinations(range(9), 4) if R0(i) == 1]
f = [i for i in itertools.combinations(range(9), 5) if R0(i) >= 1]
print("H142-Viererauswahlen:", len(q), q)
print("Fuenferauswahlen mit dim R0 >= 1:", len(f))
print("davon mit einer H142-Viererauswahl als Teil:", sum(any(set(x) <= set(s) for x in q) for s in f))
print("davon mit genau einer / mehreren:", [sum(sum(set(x) <= set(s) for x in q) == n for s in f) for n in (1, 2, 3)])
print("Sechser- bis Neunerauswahlen, max dim R0:", {m: max(R0(i) for i in itertools.combinations(range(9), m)) for m in range(6, 10)})
