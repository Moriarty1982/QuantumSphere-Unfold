"""k329 (Test H146): Gram-Auslesung (r14-r16, H101) auf den Kopien: sqrt(m_k) = Eigenwerte der Gram-Matrix der Generationszustaende
iota_k(y_q), K = Tr G^2/(Tr G)^2. Drei Kopien (alle 84), vier Kopien mit H142-Relation (9). Vorab: Vorab_Notiz_H146_Massen_aus_Kopien.md.
Definitionen aus k326 (dieses aus k325) per exec."""
import itertools, numpy as np
src = open('k326_fuenf_kopien.py').read().split('TR = (1, 1, 1, 1, 1)')[0]
exec(src)
Q8 = B[0] @ Q[0] @ B[0].T
w, U = np.linalg.eigh(Q8)
Y = {round(float(q), 6): U[:, np.abs(w - q) < 1e-6][:, 0] for q in np.unique(np.round(w, 6))}   # je Ladung ein Zustand (Farbe: erster Vektor)
print("Ladungen der Oktonion-Kopie:", sorted(Y))
def gram(idx, y):
    X = np.array([B[k].T @ y for k in idx])          # Zeilen: iota_k(y) in A5-Koordinaten
    return X.conj() @ X.T
def K(lam): lam = np.abs(lam); return float(np.sum(lam**2) / np.sum(lam)**2)
mlep = np.array([0.51099895, 105.6583755, 1776.93]); Kl = np.sum(mlep) / np.sum(np.sqrt(mlep))**2
print(f"Messwert K_l = {Kl:.6f}, m_tau/m_e = {mlep[2]/mlep[0]:.1f}")
print("\n=== H146a: drei Kopien, alle 84 Auswahlen ===")
for q, name in ((0.0, "Lepton q=0"), (0.333333, "Farbe q=1/3"), (0.666667, "Farbe q=2/3"), (1.0, "Lepton q=1")):
    y = Y[round(q, 6)]; cl = {}
    for idx in itertools.combinations(range(9), 3):
        G = gram(idx, y); lam = np.sort(np.linalg.eigvalsh(G))
        key = (tuple(np.round(lam, 6)), round(K(lam), 6)); cl.setdefault(key, []).append(idx)
    Ks = [k[1] for k in cl]
    print(f"{name}: max K = {max(Ks):.6f}; Klassen (sqrt m, K, Anzahl, Beispiel):")
    for (lam, k), l in sorted(cl.items(), key=lambda t: -t[0][1]):
        m = np.array(lam)**2; ratio = (m.max()/m[m > 1e-12].min()) if np.sum(m > 1e-12) > 1 else float('nan')
        print(f"   sqrt m = {lam}, K = {k}, m_max/m_min(>0) = {ratio:.3f}, {len(l)} Auswahlen, z. B. {[lab(i) for i in l[0]]}")
    print(f"   Sedenion-Tripel (0,1,2): sqrt m = {np.round(np.sort(np.linalg.eigvalsh(gram((0, 1, 2), y))), 6)}")
print("\n=== H146b, c: vier Kopien mit H142-Relation (9 Auswahlen) ===")
quads = [(0, 1, 5, 8), (0, 2, 4, 7), (0, 3, 7, 8), (0, 4, 5, 6), (1, 2, 3, 6), (1, 3, 5, 7), (1, 4, 6, 8), (2, 3, 4, 8), (2, 5, 6, 7)]
c = None; minpos = np.inf; maxzero = 0; Kmass = []; ratios = []
for idx in quads:
    V4 = VS[list(idx)]; cvec = np.linalg.svd(np.vstack([V4.T, np.ones(4)]))[2][-1]
    for q in sorted(Y):
        G = gram(idx, Y[q]); lam, E4 = np.linalg.eigh(G)
        maxzero = max(maxzero, abs(lam[0])); minpos = min(minpos, lam[1])
        overlap_c = abs(E4[:, 0] @ cvec) / np.linalg.norm(cvec)
        mm = lam[1:]**2; Kmass.append((idx, q, K(lam[1:]), tuple(np.round(lam, 6)), round(float(overlap_c), 9))); ratios.append(mm.max()/mm.min())
print(f"kleinster Eigenwert |lambda_0| max {maxzero:.1e}; naechster min {minpos:.4f}")
print(f"Eigenvektor zum Eigenwert 0 = c: min |<e0, c>| = {min(k[4] for k in Kmass):.9f}")
for row in sorted(set((round(k[2], 6), k[3], k[1]) for k in Kmass)):
    print(f"   q = {row[2]:.4f}: sqrt m = {row[1]}, K der drei massiven = {row[0]}")
print(f"H146c: max |K - 2/3| ueber alle = {max(abs(k[2] - 2/3) for k in Kmass):.4f}, min |K - 2/3| = {min(abs(k[2] - 2/3) for k in Kmass):.4f}; max m_max/m_min = {max(ratios):.3f}")
