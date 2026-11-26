"""k372 (Erkundung, NICHT BLIND, 26.11.2026; angekuendigt in der Vorab-Notiz H175): jede Z3-brechende Eingabe einzeln, dann stochastische Suche.
Alles hier ist angepasst, nicht hergeleitet.
Aufruf aus diesem Ordner: python3 -u k372_eingaben_und_suche.py > k372_out.txt
"""
import numpy as np
from scipy.optimize import minimize
import k371_test_h175 as K
names = list(K.DIRS)
rng = np.random.default_rng(372)
S13, S12, S23 = K.ns["S13"], K.ns["S12"], K.ns["S23"]
for label, x in (("x", K.X_LEP), ("x_R", K.X_R)):
    obs, chi2 = K.make(x)
    vec = lambda c: (lambda o: None if o is None else np.array([o[2][2], o[2][0], o[2][1], o[2][3], o[0], o[1]]))(obs(names, c))
    print(f"===== Versatz {label} = {x} =====")
    v0 = vec(np.zeros(8))
    print(f"Ausgangspunkt: th13 = {v0[0]:.5f}, th12 = {v0[1]:.5f}, th23 = {v0[2]:.5f}, sin delta = {v0[3]:+.3f}; Ziel: {S13}, {S12}, {S23}")
    print("== 1. Jede Eingabe einzeln: Ableitungen bei kappa = 0 und Wirkung bei kappa = +-0,05 ==")
    print("   Richtung | d th13 | d th12 | d th23 | d sin delta | d rho | d delta_C || th13, th12, th23 bei -0,05 | bei +0,05")
    Jm = []
    h = 1e-4
    for i, n in enumerate(names):
        e = np.zeros(8); e[i] = 1
        d = (vec(h * e) - vec(-h * e)) / (2 * h); Jm.append(d[:3])
        a, b = vec(-0.05 * e), vec(0.05 * e)
        fa = "nicht erreichbar" if a is None else f"{a[0]:.4f}, {a[1]:.4f}, {a[2]:.4f}"
        fb = "nicht erreichbar" if b is None else f"{b[0]:.4f}, {b[1]:.4f}, {b[2]:.4f}"
        print(f"   {n:4s} | {d[0]:+.4f} | {d[1]:+.4f} | {d[2]:+.4f} | {d[3]:+.3f} | {d[4]:+.4f} | {d[5]:+.4f} || {fa} | {fb}")
    Jm = np.array(Jm).T                                   # 3 x 8
    need = np.array([S13, S12, S23]) - v0[:3]
    print(f"   noetige Aenderung (th13, th12, th23): {np.round(need, 5).tolist()}")
    c_lin = np.linalg.pinv(Jm) @ need
    print("   lineare Naeherung, kleinste Norm: " + ", ".join(f"{n} {c:+.4f}" for n, c in zip(names, c_lin)) + f"; Norm {np.linalg.norm(c_lin):.4f}")
    print("   (th13 ist bei kappa = 0 in erster Ordnung nur bedingt linear; siehe Wirkung bei +-0,05)")

    print("== 2. Stochastische Suche (abgekuehlte Metropolis-Suche, 48 Laeufer, 8 Richtungen) ==")
    nw = 48
    W = rng.normal(0, 0.08, (nw, 8)); c2 = np.array([chi2(names, w) for w in W])
    temps = np.concatenate([np.geomspace(300, 1, 220), np.ones(260)])
    keep = []
    for it, Tm in enumerate(temps):
        step = 0.02 * (Tm / 300)**0.25 + 0.004
        prop = W + rng.normal(0, step, W.shape); pc = np.array([chi2(names, w) for w in prop])
        # schwache Vorgabe: kleine Terme bevorzugt (Breite 0,15), damit die Suche nicht wegläuft
        lp = -(pc - c2) / (2 * Tm) - (np.sum(prop**2, 1) - np.sum(W**2, 1)) / (2 * 0.15**2)
        acc = np.log(rng.random(nw)) < lp
        W[acc] = prop[acc]; c2[acc] = pc[acc]
        if it >= 300 and it % 4 == 0: keep.append(W[c2 < 9].copy())
        if it in (0, 100, 219, 479): print(f"   Schritt {it}: Temperatur {Tm:.1f}, chi2 Median {np.median(c2):.1f}, kleinstes {c2.min():.2f}, Laeufer mit chi2 < 9: {int((c2 < 9).sum())}")
    P = np.vstack(keep)
    print(f"   Stichprobe vertraeglicher Punkte (chi2 < 9): {len(P)}")
    print("   Richtung | Mittel | Streuung | Anteil am Normquadrat")
    tot = np.mean(np.sum(P**2, 1))
    for i, n in enumerate(names):
        print(f"   {n:4s} | {P[:, i].mean():+.4f} | {P[:, i].std():.4f} | {np.mean(P[:, i]**2)/tot:.3f}")
    cls = {"S A-gerade": [0, 1, 2], "S A-ungerade": [3, 4], "K A-gerade": [5], "K A-ungerade (Ladungsrichtung)": [6, 7]}
    print("   Anteil am Normquadrat je Klasse: " + ", ".join(f"{k} {np.mean(np.sum(P[:, v]**2, 1))/tot:.3f}" for k, v in cls.items()))
    ev, evec = np.linalg.eigh(np.cov(P.T))
    print("   Hauptachsen der vertraeglichen Menge (Streuung; Richtung):")
    for j in range(8):
        print(f"      {np.sqrt(ev[j]):.4f}: " + ", ".join(f"{n} {c:+.2f}" for n, c in zip(names, evec[:, j]) if abs(c) > 0.25))

    print("== 3. Kleinster Term, der alle drei Winkel genau trifft ==")
    tgt3 = np.array([S13, S12, S23])
    def con(c):
        v = vec(c)
        return np.ones(3) if v is None else (v[:3] - tgt3) / np.array([0.00056, 0.0064, 0.015])
    sols = []
    idx = np.argsort(np.sum(P**2, 1))[:5]
    for s0 in list(P[idx]) + [c_lin]:
        r = minimize(lambda c: np.sum(c**2), s0, method='SLSQP', constraints=[{'type': 'eq', 'fun': con}], options={'maxiter': 150, 'ftol': 1e-12})
        v = vec(r.x)
        if v is not None and np.max(abs(con(r.x))) < 1e-3: sols.append((np.linalg.norm(r.x), r.x, v))
    sols.sort(key=lambda t: t[0])
    seen = []
    for nrm, c, v in sols:
        if any(np.linalg.norm(c - s) < 5e-3 for s in seen): continue
        seen.append(c)
        print(f"   Norm {nrm:.4f}: " + ", ".join(f"{n} {ci:+.4f}" for n, ci in zip(names, c)) + f"; th13 = {v[0]:.5f}, th12 = {v[1]:.5f}, th23 = {v[2]:.5f}, sin delta = {v[3]:+.3f}, rho = {v[4]:.5f}")
        print("        Anteile am Normquadrat: " + ", ".join(f"{k} {np.sum(c[vv]**2)/nrm**2:.3f}" for k, vv in cls.items()))
        if len(seen) >= 4: break
