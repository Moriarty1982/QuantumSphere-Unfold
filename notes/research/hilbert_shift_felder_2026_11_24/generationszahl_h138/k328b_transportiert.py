"""k328b (Test H145, Auswertung getrennt nach Orientierung): k328 hat alle relativen Orientierungen gemischt. Bei Vorzeichen s_k = -1 ist der
Transport y -> (y0, -y_im) die Konjugation, ein Anti-Isomorphismus; die Formel c (x) y der Vorab-Notiz ist fuer gleich orientierte Kopien
gemacht. Hier: (1) transportierte Orientierung (gewertet wie vorab); (2) gemischte Orientierungen (nachtraeglich offengelegt), mit der
berichtigten Farbbedingung c in R und s*c in R. Definitionen aus k328 per exec (ohne dessen Ausgabe-Teil)."""
import itertools, numpy as np
src = open('k328_rest_hs0.py').read()
exec(src.split('err = 0')[0]); Q8 = B[0] @ Q[0] @ B[0].T
rng = np.random.default_rng(3282)
def W_formel(idx, sg, berichtigt):
    m = len(idx); V = VS[list(idx)]; s = np.array(sg)
    R = null(V.T); R0 = null(np.vstack([(s[:, None]*V).T, np.ones((1, m))]))
    Rc = null(np.vstack([V.T, (s[:, None]*V).T])) if berichtigt else R          # c in R und s*c in R
    def place(coef, comp):
        x = np.zeros(8*m, dtype=complex)
        for k in range(m): x[8*k + comp] = coef[k]
        return x
    Wp = [place(c, 0) for c in R0.T] + [place(s*c, 7) for c in R0.T] + [place(c, i) for c in Rc.T for i in range(1, 7)]
    return np.array(Wp).T if Wp else np.zeros((8*m, 0)), R0
def dist(Wp, Wb):
    A = proj(Wp) if Wp.shape[1] else 0; Bm = Wb @ Wb.conj().T if Wb.shape[1] else 0
    return float(np.abs(A - Bm).max()) if (Wp.shape[1] or Wb.shape[1]) else 0.0
print("=== (1) transportierte Orientierung (gewertet) ===")
for m in (3, 4, 5):
    mx = 0; mxb = 0; mxc = 0; dmin = np.inf; ng = 0
    for idx in itertools.combinations(range(9), m):
        sg = (1,)*m; Kb, QV, _ = ops(idx, sg); Wb = stable_part(Kb, QV); Wp, R0 = W_formel(idx, sg, False)
        mx = max(mx, dist(Wp, Wb))
        if R0.shape[1]:
            ng += 1; PK = Kb.T @ Kb
            for c in R0.T:
                y = rng.normal(size=8) + 1j*rng.normal(size=8); x = np.concatenate([c[k]*y for k in range(m)])
                mxb = max(mxb, np.linalg.norm(QV @ x - np.concatenate([c[k]*(Q8 @ y) for k in range(m)])))
                mxc = max(mxc, abs(np.sum(c**3)) / np.linalg.norm(c)**3)
                yb = rng.normal(size=8) + 1j*rng.normal(size=8)
                z = np.concatenate([c[k]**2 * ((mul(y.real, yb.real) - mul(y.imag, yb.imag)) + 1j*(mul(y.real, yb.imag) + mul(y.imag, yb.real))) for k in range(m)])
                dmin = min(dmin, np.linalg.norm(z - PK @ z) / np.linalg.norm(z))
    print(f"m = {m}: max Abstand Projektor W zur Formel {mx:.1e}; Auswahlen mit n_gen >= 1: {ng}" +
          (f"; b: max |QV(c(x)y) - c(x)Q8 y| {mxb:.1e}; c: max |sum c^3|/|c|^3 {mxc:.1e}; d: min Anteil (c(x)y)(c(x)y') ausserhalb K {dmin:.4f}" if ng else ""))
print("\n=== (2) gemischte Orientierungen (nachtraeglich) ===")
for m in (3, 4, 5):
    mx_naiv = 0; mx_ber = 0; n = 0; c3 = []
    for idx in itertools.combinations(range(9), m):
        for sg in itertools.product([1, -1], repeat=m - 1):
            sg1 = (1,) + sg
            if all(x > 0 for x in sg1): continue
            n += 1; Kb, QV, _ = ops(idx, sg1); Wb = stable_part(Kb, QV)
            mx_naiv = max(mx_naiv, dist(W_formel(idx, sg1, False)[0], Wb)); Wp, R0 = W_formel(idx, sg1, True)
            mx_ber = max(mx_ber, dist(Wp, Wb))
            for c in R0.T: c3.append(abs(np.sum(c**3)) / np.linalg.norm(c)**3)
    print(f"m = {m}: {n} Faelle; Abstand W zur Vorab-Formel max {mx_naiv:.2f}; zur berichtigten Formel max {mx_ber:.1e}; "
          f"|sum c^3|/|c|^3 bei n_gen >= 1: min {min(c3) if c3 else float('nan'):.3f}, max {max(c3) if c3 else float('nan'):.3f}, Faelle {len(c3)}")
