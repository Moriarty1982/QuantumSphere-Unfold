"""k327 (Test H144): Sektorsignatur der Rest-Generation und der leckenden Zustaende; Frame-Abbildungen z -> iz, z -> conj(z).
Vorab: Vorab_Notiz_H144_Rest_als_Sektoren.md. Uebernimmt Definitionen aus k326 (dieses wiederum aus k325) per exec.
N(x) = sum_a x_a^2 (alle Koordinaten, bilinear), s(x) = N(x) - sum_k x_{k,e0}^2 (nur Imaginaerteil, T3). Summe ueber die Traeger."""
import itertools, numpy as np
src = open('k326_fuenf_kopien.py').read().split('TR = (1, 1, 1, 1, 1)')[0]
exec(src)
TOL = 1e-6
def eigspaces(Xb, QV):
    """Eigenraeume von QV auf dem invarianten Raum mit ONB Xb (Spalten): dict q -> ONB."""
    H = Xb.conj().T @ QV @ Xb; w, U = np.linalg.eigh(H); out = {}
    for q in np.unique(np.round(w, 6)):
        out[float(q)] = Xb @ U[:, np.abs(w - q) < 1e-6]
    return out
def takagi(X, m, im_only=False):
    Y = X.copy()
    if im_only:
        Y = Y.copy(); Y[[8*j for j in range(m)], :] = 0       # e0-Anteil je Traeger streichen
    return np.linalg.svd(X.T @ Y, compute_uv=False)              # X^T Y = Gram der bilinearen Form (N bzw. s)
def analyse(idx):
    m = len(idx); sg = (1,)*m
    Kb, QV, blk = ops(idx, sg); Wb = stable_part(Kb, QV)
    out = dict(m=m, dimK=len(Kb), dimW=Wb.shape[1])
    # H144a
    if Wb.shape[1]:
        PW = Wb @ Wb.conj().T; PcW = Wb.conj() @ Wb.T
        out['conjW'] = float(np.abs(PW - PcW).max())
        qW = np.sort(np.linalg.eigvalsh(Wb.conj().T @ QV @ Wb)); qc = np.sort(np.linalg.eigvalsh(Wb.T @ QV.conj() @ Wb.conj()))
        out['spiegel'] = bool(np.allclose(np.sort(1 - qW), qc, atol=1e-9))
        # Gewicht auf hoechstens zwei Traegern: dim(W cap (C_i + C_j)) fuer alle Paare
        mx = 0
        for i, j in itertools.combinations(range(m), 2):
            S = np.zeros((8*m, 16)); S[8*i:8*i+8, :8] = np.eye(8); S[8*j:8*j+8, 8:] = np.eye(8)
            sv = np.linalg.svd(np.hstack([Wb, S]), compute_uv=False)
            mx = max(mx, Wb.shape[1] + 16 - int(np.sum(sv > 1e-9)))
        out['W_in_2_traegern'] = mx
        # H144b/c
        es = eigspaces(Wb, QV)
        out['N_W'] = {q: float(takagi(X, m).max()) for q, X in es.items()}
        out['s_W'] = {q: tuple(np.round(takagi(X, m, True), 8)) for q, X in es.items()}
    # H144d: K (-) W
    PK = Kb.T @ Kb; PW = (Wb @ Wb.conj().T) if Wb.shape[1] else np.zeros_like(PK)
    U = np.linalg.svd(PK - PW)[0][:, :len(Kb) - Wb.shape[1]]
    if U.shape[1]:
        Hc = U.conj().T @ QV @ U; w, V = np.linalg.eigh(Hc); X = U @ V
        out['rest_q'] = tuple(np.round(w, 6))
        out['N_rest_einzeln'] = tuple(np.round([abs(X[:, k] @ X[:, k]) for k in range(X.shape[1])], 6))
        out['N_rest_takagi_min'] = float(takagi(U, m).min())
        out['s_rest_einzeln'] = tuple(np.round([abs(X[:, k] @ X[:, k] - sum(X[8*j, k]**2 for j in range(m))) for k in range(X.shape[1])], 6))
    return out
# Kopie allein (Materie-Frame der Kopie), Kontrolle zu H144b/c
print("=== Kopie f0(x)f0 allein ===")
q8 = B[0] @ Q[0] @ B[0].T; es = eigspaces(np.eye(8, dtype=complex), q8)
for q, X in es.items():
    print(f"  q = {q:.6f}: dim {X.shape[1]}, Takagi N {np.round(takagi(X, 1), 8)}, Takagi s {np.round(takagi(X, 1, True), 8)}")
def klassen(m):
    cl = {}
    for idx in itertools.combinations(range(9), m):
        r = analyse(idx)
        key = (r['dimK'], r['dimW'], r.get('rest_q'), tuple(sorted(r.get('s_W', {}).items())))
        cl.setdefault(key, []).append((idx, r))
    return cl
for m, name in ((3, "drei Kopien (H141/H140-Klassen)"), (4, "vier Kopien (H142)"), (5, "fuenf Kopien (H143)")):
    print(f"\n=== {name}: transportierte Orientierung ===")
    for key, lst in klassen(m).items():
        rs = [r for _, r in lst]; r = rs[0]
        print(f"{len(lst)} Auswahlen, z. B. {[lab(k) for k in lst[0][0]]}: dim K {r['dimK']}, dim W {r['dimW']}")
        if r['dimW']:
            print(f"   a: max |P_W - P_conjW| {max(x['conjW'] for x in rs):.1e}; Spektrum gespiegelt: {all(x['spiegel'] for x in rs)}; max dim(W in 2 Traegern) {max(x['W_in_2_traegern'] for x in rs)}")
            print(f"   b: max Takagi N je q in W: { {q: float(f'{max(x['N_W'][q] for x in rs):.1e}') for q in r['N_W']} }")
            print(f"   c: Takagi s je q in W: {r['s_W']}")
        if 'rest_q' in r:
            print(f"   d: Rest K-W gestauchte Ladungen {r['rest_q']}")
            print(f"      |N| je Zustand {r['N_rest_einzeln']}; min Takagi N auf K-W {min(x['N_rest_takagi_min'] for x in rs):.4f}; |s| je Zustand {r['s_rest_einzeln']}")
print("\nSedenion-Tripel (0,1,2) einzeln:", {k: v for k, v in analyse((0, 1, 2)).items() if k in ('dimK', 'dimW', 'rest_q', 'N_rest_einzeln', 's_rest_einzeln', 'N_rest_takagi_min')})
