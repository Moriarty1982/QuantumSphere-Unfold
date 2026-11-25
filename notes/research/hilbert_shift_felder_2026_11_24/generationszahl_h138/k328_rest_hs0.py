"""k328 (Test H145): Zerlegung des Rests K = (D0 (x) e0) + (R (x) Im O), Rest-Generation = R0 (x) O; HS(0)-Merkmale der Koeffizientenlinie,
induziertes Produkt auf der Linie, Abgeschlossenheit des Rests unter dem traegerweisen Produkt. Vorab: Vorab_Notiz_H145_Rest_als_HS0.md.
Definitionen aus k326 (dieses aus k325) per exec. Traegerkoordinaten: Zeile 0 = e0, Zeile i = e_i (x) v_k, also die Oktonion-Koordinaten unter iota_k."""
import itertools, numpy as np
src = open('k326_fuenf_kopien.py').read().split('TR = (1, 1, 1, 1, 1)')[0]
exec(src)
rng = np.random.default_rng(328)
def null(A, tol=1e-10):
    if A.shape[0] == 0: return np.eye(A.shape[1])
    _, s, vt = np.linalg.svd(A); return vt[int(np.sum(s > tol)):].T          # Spalten = ONB des Kerns
def orth(M):
    if M.shape[1] == 0: return M
    u, s, _ = np.linalg.svd(M, full_matrices=False); return u[:, s > 1e-10]
def proj(M): M = orth(M); return M @ M.conj().T
# ι_k Algebren-Isomorphismus?
E8 = np.eye(8)
def iota(y, v): return y[0]*E[0] + sum(y[i]*emb(np.eye(7)[i-1], v) for i in range(1, 8))
err = 0
for v in VS:
    for i in range(8):
        for j in range(8):
            err = max(err, np.abs(mul(iota(E8[i], v), iota(E8[j], v)) - iota(mul(E8[i], E8[j]), v)).max())
print(f"H145a: iota_k Algebren-Isomorphismus, max Produktfehler ueber 9 Kopien: {err:.1e}")
Q8 = B[0] @ Q[0] @ B[0].T            # Ladung der Kopie f0(x)f0 in Oktonion-Koordinaten (transportierte Orientierung: fuer alle gleich)
print("   Q in Oktonion-Koordinaten fuer alle 9 Kopien gleich:", max(np.abs(B[k] @ Q[k] @ B[k].T - Q8).max() for k in range(9)) < 1e-12)

def spaces(idx, sg):
    m = len(idx); V = VS[list(idx)]; sgv = np.array(sg)
    D0 = null(np.ones((1, m))); R = null(V.T); R0 = null(np.vstack([(sgv[:, None]*V).T, np.ones((1, m))]))
    def place(coef, comp):         # Vektor in V-Koordinaten: Traeger k bekommt coef_k * Einheitsvektor comp
        x = np.zeros(8*m, dtype=complex)
        for k in range(m): x[8*k + comp] = coef[k]
        return x
    Kp = [place(d, 0) for d in D0.T] + [place(c, i) for c in R.T for i in range(1, 8)]
    Wp = [place(c, 0) for c in R0.T] + [place(sgv*c, 7) for c in R0.T] + [place(c, i) for c in R.T for i in range(1, 7)]
    return np.array(Kp).T, (np.array(Wp).T if Wp else np.zeros((8*m, 0))), D0, R, R0
def check(idx, sg):
    m = len(idx); Kb, QV, blk = ops(idx, sg); Wb = stable_part(Kb, QV)
    Kp, Wp, D0, R, R0 = spaces(idx, sg)
    dK = np.abs(proj(Kp) - Kb.T @ Kb).max()
    dW = np.abs(proj(Wp) - (Wb @ Wb.conj().T if Wb.shape[1] else 0)).max() if (Wp.shape[1] or Wb.shape[1]) else 0.0
    dimform = (m - 1) + 7*R.shape[1]
    return dict(dK=dK, dW=dW, dimK=len(Kb), dimform=dimform, dimW=Wb.shape[1], R=R.shape[1], R0=R0.shape[1], R0b=R0, QV=QV, Kb=Kb, Wb=Wb)
print("\n=== H145a: Zerlegung, alle Auswahlen von 3, 4, 5 Kopien und alle relativen Orientierungen ===")
for m in (3, 4, 5):
    mxK = mxW = 0; bad = 0; n = 0
    for idx in itertools.combinations(range(9), m):
        for sg in itertools.product([1, -1], repeat=m - 1):
            r = check(idx, (1,) + sg); n += 1
            mxK = max(mxK, r['dK']); mxW = max(mxW, r['dW']); bad += (r['dimK'] != r['dimform'])
    print(f"m = {m}: {n} Faelle; max Abstand Projektor K {mxK:.1e}, Projektor W {mxW:.1e}; dim K != (m-1) + 7 dim R: {bad}")

print("\n=== H145b, c, d: Generationsklassen (n_gen >= 1), alle Orientierungen ===")
mxb = mxc = 0; mind = np.inf; maxd = 0; cnt = 0; ex = None
for m in (4, 5):
    for idx in itertools.combinations(range(9), m):
        for sg in itertools.product([1, -1], repeat=m - 1):
            sg1 = (1,) + sg; r = check(idx, sg1)
            if r['R0'] == 0: continue
            cnt += 1; sgv = np.array(sg1)
            for c in r['R0b'].T:
                # b: Q wirkt auf c (x) y als c (x) Q8 y (Traeger k: e0-Koeffizient c_k, Im-Koeffizient s_k c_k)
                for _ in range(3):
                    y = rng.normal(size=8) + 1j*rng.normal(size=8)
                    x = np.concatenate([c[k]*np.concatenate([[y[0]], sgv[k]*y[1:]]) for k in range(m)])
                    Qy = Q8 @ y if sgv[0] > 0 else Q8 @ y
                    # Ladung der Kopie mit Vorzeichen s: Q_{s v} = Q8 mit Im-Koordinaten s-gedreht; Erwartung in Traegerkoordinaten:
                    Sk = [np.diag([1] + [s]*7) for s in sgv]
                    exp_ = np.concatenate([c[k]*(Sk[k] @ (Q8 if sgv[k] > 0 else (np.eye(8) - Q8)) @ Sk[k] @ (Sk[k] @ np.concatenate([[y[0]], sgv[k]*y[1:]])) * 0 + c[k]*0) for k in range(m)])
                    mxb = max(mxb, np.linalg.norm(r['QV'] @ x - np.concatenate([c[k]*(Sk[k] @ Q8 @ y) for k in range(m)])))
                # c: induziertes Produkt auf der Linie
                mxc = max(mxc, abs(np.sum(c**3)) / np.linalg.norm(c)**3)
            # d: Abgeschlossenheit
            PK = r['Kb'].T @ r['Kb']
            for _ in range(5):
                a = r['Wb'] @ (rng.normal(size=r['dimW']) + 1j*rng.normal(size=r['dimW']))
                b = r['Wb'] @ (rng.normal(size=r['dimW']) + 1j*rng.normal(size=r['dimW']))
                z = []
                for k, j in zip(idx, range(m)):
                    ya, yb = B[k].T @ a[8*j:8*j+8], B[k].T @ b[8*j:8*j+8]
                    p = (mul(ya.real, yb.real) - mul(ya.imag, yb.imag)) + 1j*(mul(ya.real, yb.imag) + mul(ya.imag, yb.real))
                    z.append(B[k] @ p)
                z = np.concatenate(z); d = np.linalg.norm(z - PK @ z) / np.linalg.norm(z)
                mind = min(mind, d); maxd = max(maxd, d)
            if ex is None: ex = (idx, sg1, r['R0b'].T[0])
print(f"{cnt} Faelle mit n_gen >= 1")
print(f"H145b: max |QV(c (x) y) - c (x) Q8 y| = {mxb:.1e} (Q wirkt nur auf y, trivial auf c)")
print(f"H145c: max |sum c_k^3| / |c|^3 (induziertes Produkt auf der Linie) = {mxc:.1e}")
print(f"H145d: Anteil von x*y ausserhalb K (relativ), min {mind:.4f}, max {maxd:.4f}")
print(f"Beispiel: Auswahl {[lab(k) for k in ex[0]]}, Orientierung {ex[1]}, Koeffizienten c (normiert) {np.round(ex[2]/np.abs(ex[2]).max(), 6)}")
print("\nKoeffizienten c der Rest-Generation (normiert auf max |c_k| = 1), transportierte Orientierung, alle Generationsklassen:")
seen = set()
for m in (4, 5):
    for idx in itertools.combinations(range(9), m):
        r = check(idx, (1,)*m)
        for c in r['R0b'].T:
            c = c / c[np.argmax(np.abs(c))]; seen.add(tuple(sorted(np.round(c, 6))))
print(sorted(seen))
