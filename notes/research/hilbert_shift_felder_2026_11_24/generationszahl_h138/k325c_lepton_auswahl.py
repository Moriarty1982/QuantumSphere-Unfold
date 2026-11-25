"""k325c (nachtraeglich, Erkundung zu H142): die 9 Viererauswahlen mit 0 und 1 im Kern. Welche sind es, welche Kernrichtungen
lecken unter der Ladung, ist der Teil mit Spektrum (0, 1/3^3, 2/3^3, 1) ladungsstabil, und wie zerfaellt er unter su(3)?
Fuehrt k325_vier_kopien.py-Definitionen per exec aus (ohne dessen Ausgabe-Teil)."""
import itertools, numpy as np, io, contextlib
src = open('k325_vier_kopien.py').read().split('print("=== H142a ===")')[0]
exec(src)
def analyse(idx):
    m = len(idx); Phi = np.hstack([B[k].T for k in idx])
    u_, s_, vt_ = np.linalg.svd(Phi); r = int(np.sum(s_ > 1e-10)); Kb = vt_[r:]; PK = Kb.T @ Kb
    blk = lambda Ms: np.block([[Ms[a] if a == b else np.zeros((8, 8)) for b in range(m)] for a in range(m)])
    QV = blk([B[k] @ Q[k] @ B[k].T for k in idx])
    SV = [blk([B[k] @ g @ B[k].T for k in idx]) for g in Sg]
    Km = np.array([[np.trace(a @ b) for b in SV] for a in SV]); Ki = np.linalg.inv(Km)
    Cas = -sum(Ki[i, j] * SV[i] @ SV[j] for i in range(8) for j in range(8))
    Qk = Kb @ QV @ Kb.T
    w, W = np.linalg.eig(Qk); o = np.argsort(w.real); w, W = w[o].real, W[:, o]
    vecs = Kb.T @ W
    gen = [i for i in range(len(w)) if abs(w[i] - 0.5) > 1e-6]; half = [i for i in range(len(w)) if abs(w[i] - 0.5) < 1e-6]
    Gs = np.linalg.qr(vecs[:, gen])[0]; Hs = np.linalg.qr(vecs[:, half])[0]
    leak_gen = np.linalg.norm(QV @ Gs - Gs @ (Gs.conj().T @ QV @ Gs), 2)
    leak_half = np.linalg.norm(QV @ Hs - Hs @ (Hs.conj().T @ QV @ Hs), 2)
    cas_gen = np.round(np.linalg.eigvalsh(Gs.conj().T @ Cas @ Gs), 6)
    cas_vals = {float(c): int(n) for c, n in zip(*np.unique(np.abs(cas_gen) > 1e-6, return_counts=True))}
    # Ladung je Casimir-Teil
    return dict(spec=np.round(w, 6), leak_gen=leak_gen, leak_half=leak_half, cas_gen=cas_vals)
lst = []
for idx in itertools.combinations(range(9), 4):
    a = analyse(idx)
    if np.any(np.abs(a['spec']) < 1e-6) and np.any(np.abs(a['spec'] - 1) < 1e-6): lst.append((idx, a))
lab = lambda k: f"f{120*(k//3)}(x)f{120*(k%3)}"
print(f"Auswahlen mit 0 und 1 im Kern: {len(lst)}")
for idx, a in lst:
    print(f"  {idx} = {[lab(k) for k in idx]}")
    print(f"     Spektrum {a['spec']}; Leck des 8er-Teils (0,1/3,2/3,1): {a['leak_gen']:.1e}; Leck der 1/2-Singuletts: {a['leak_half']:.3f}; su(3) im 8er-Teil (Singulett False / Farbe True): {a['cas_gen']}")
