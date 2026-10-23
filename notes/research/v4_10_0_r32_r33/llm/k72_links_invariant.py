"""k72: Modellbau (kein Massenvergleich): links-invariante Groessen auf dem Generationen-Tripel, die drei Plaetze unterscheiden.
Tripel in H (x) O: Psi = sum_b e_b (x) x_b, als 8 Quaternionen h_c (Spalte c = Oktonion-Komponente, Zeile b = H-Basis 1,i,j,k).
Lorentz (Spinor) wirkt von links: h_c -> q h_c.  Links-invariant: G_cd = conj(h_c) h_d.  Imaginaerteile A^(b)_cd, b = i,j,k.
mu_b = sum_cd (A^(b)_cd)^2.  Geprueft: Invarianz (links, auch SL(2,C) mit komplex-bilinearer Gram), Wirkung der Rechts-2T,
Formel mu_i = 2(|x_j|^2 |x_k|^2 - <x_j,x_k>^2), Lage bei orthogonalen Plaetzen."""
import numpy as np, itertools

def qm(p, r):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = r
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
qc = lambda q: q*np.array([1, -1, -1, -1])

def mu(H):
    """H: 4 x 8 (Zeilen 1,i,j,k).  Liefert (mu_i, mu_j, mu_k) und den Realteil der Gram-Matrix."""
    h = [H[:, c] for c in range(8)]
    G = np.array([[qm(qc(h[c]), h[d]) for d in range(8)] for c in range(8)])     # 8 x 8 x 4
    return np.array([(G[:, :, b]**2).sum() for b in (1, 2, 3)]), G[:, :, 0]

rng = np.random.default_rng(72)
H = np.zeros((4, 8)); H[1:] = rng.normal(size=(3, 8))          # reines Tripel: Zeilen i, j, k = Plaetze x_1, x_2, x_3
m0, G0 = mu(H)

# 1. Links-Invarianz unter Einheitsquaternionen (Drehungen)
dev = 0
for _ in range(200):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    Hq = np.array([qm(q, H[:, c]) for c in range(8)]).T
    m1, _ = mu(Hq); dev = max(dev, abs(m1 - m0).max()/m0.max())
    norms_moved = not np.allclose((Hq[1:]**2).sum(1), (H[1:]**2).sum(1))
print(f"1) mu unter Linksmultiplikation fest: rel. Abweichung {dev:.1e}; Platznormen dabei verschoben: {norms_moved}")

# 1b. Boosts: SL(2,C) = Biquaternionen q mit conj(q) q = 1 (komplex), komplex-bilineare Gram (ohne komplexe Konjugation)
def cqm(p, r):  # p, r komplexe Quaternionen (4 komplexe Komponenten), gleiche Formel
    return qm(p, r)
def mu_c(Hc):
    h = [Hc[:, c] for c in range(8)]
    G = np.array([[cqm(qc(h[c]), h[d]) for d in range(8)] for c in range(8)])
    return np.array([(G[:, :, b]**2).sum() for b in (1, 2, 3)])
dev = 0
for _ in range(200):
    q = rng.normal(size=4) + 1j*rng.normal(size=4)
    nq = np.sqrt(cqm(qc(q), q)[0]); q = q/nq                     # conj(q) q = 1 (komplex)
    Hq = np.array([cqm(q, H[:, c].astype(complex)) for c in range(8)]).T
    dev = max(dev, abs(mu_c(Hq) - m0).max()/m0.max())
print(f"1b) mit komplex-bilinearer Gram auch unter Boosts (SL(2,C)) fest: rel. Abweichung {dev:.1e}")

# 2. Rechtswirkung von 2T vertauscht die drei Etiketten wie die A4 aus K77.4
E = np.eye(4)
T2 = [s*E[i] for i in range(4) for s in (1, -1)] + [np.array(v)/2 for v in itertools.product((1, -1), repeat=4)]
perms = set()
for r in T2:
    Hr = np.array([qm(H[:, c], r) for c in range(8)]).T
    m1, _ = mu(Hr)
    p = tuple(int(np.argmin(abs(m0 - v))) for v in m1)
    assert np.allclose(sorted(m1), sorted(m0))
    perms.add(p)
print(f"2) Rechts-2T: mu wird permutiert; auftretende Permutationen der Etiketten: {sorted(perms)}")

# 3. Formel: mu_i = 2(|x_j|^2 |x_k|^2 - <x_j, x_k>^2) (Flaecheninhalt der beiden anderen Plaetze)
x = H[1:]
area = lambda a, b: 2*((a@a)*(b@b) - (a@b)**2)
f = np.array([area(x[1], x[2]), area(x[0], x[2]), area(x[0], x[1])])
print(f"3) mu = 2 * Flaeche der beiden anderen Plaetze: Abweichung {abs(f - m0).max():.1e}")
print(f"   Realteil der Gram-Matrix = sum_b x_b x_b^T (symmetrisch in den Plaetzen): {np.allclose(G0, x.T@x)}")

# 4. Orthogonale Plaetze: sqrt(mu_i/2) = n_j n_k = P / n_i
Qm, _ = np.linalg.qr(rng.normal(size=(8, 3)))
n = np.array([0.3, 1.1, 2.5]); Ho = np.zeros((4, 8)); Ho[1:] = (Qm*n).T
mo, _ = mu(Ho)
print(f"4) orthogonale Plaetze, Normen {n}: sqrt(mu/2) = {np.round(np.sqrt(mo/2), 6)}, P/n = {np.round(n.prod()/n, 6)}")
print("   -> die links-invariante Lesart kehrt die Reihenfolge der Normen um (kleinste Norm -> groesste Groesse).")
