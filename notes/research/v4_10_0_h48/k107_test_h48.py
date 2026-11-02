"""k107: Test H48 (Vorab-Notiz llm/Vorab_Notiz_H48_Einfrieren_beta.md, lokal e40a705, GitHub 0ff3ab2).

Modell (aus der Notiz):
  db/dt = w J b - G_C P_z b - G_R (b - b_T),  J(bx,bz)=(bz,-bx), P_z b=(0,bz), b_T=(0,-1), w=1
  G_C = g n, G_R = r g n,  n = n0 a^-3
  H^2 = (kappa/3)(m n - e_EC (3 kappa/16) n^2 bx^2) + Lambda/3
Dimensionslos mit x = n/n0 = a^-3, G = g n0, H0^2 = kappa m n0/3, c_EC = (3 kappa/16) n0/m, lam = Lambda/(3 H0^2):
  H^2 = H0^2 (x - e_EC c_EC x^2 bx^2 + lam)

Numerik (Abweichung von 'Mittel ueber 20 Drehperioden' nur in der Technik): Zeitschritte dt = eps/max(H, ...), in denen die Raten
als konstant gelten; ueber jeden Schritt wird das lineare System exakt geloest: b(t+dt) = b* + exp(A dt)(b - b*),
A = wJ - G_C P_z - G_R I, b* = -A^{-1} G_R b_T. Das ist fuer jede Drehfrequenz und jede Steifheit exakt bei konstanten Raten.
a und H werden mit dem Schritt fortgeschrieben (dN = H dt). Nach dem Einfrieren ist |b| unter der reinen Drehung erhalten;
|b_inf| ist |b| am Ende (G_C < 1e-8, Aenderung je e-Faltung < 1e-10). Kontrolle: eps = 1e-3 gegen 2.5e-4.
"""
import json, math, itertools, sys
import numpy as np

def expm2(A, dt):
    # exakte 2x2-Matrixexponentialfunktion
    a, b, c, d = A[0,0]*dt, A[0,1]*dt, A[1,0]*dt, A[1,1]*dt
    s = (a + d) / 2.0
    q = (a - d)**2 / 4.0 + b * c
    if q > 1e-14:
        r = math.sqrt(q)
        ep, em = math.exp(s + r), math.exp(s - r)      # stabil: s + r <= 0 fuer die gedaempfte Matrix
        ch, sh = (ep + em) / 2.0, (ep - em) / (2.0 * r)
    elif q < -1e-14:
        r = math.sqrt(-q); es = math.exp(s)
        ch, sh = es * math.cos(r), es * math.sin(r) / r
    else:
        es = math.exp(s)
        ch, sh = es * (1.0 + q/2), es * (1.0 + q/6)
    m00 = ch + sh * (a - s); m11 = ch + sh * (d - s)
    return np.array([[m00, sh * b], [sh * c, m11]])

def run(r, G, H0, eEC, cEC, lam, eps=1e-3, Nmax=60.0):
    w = 1.0
    bvec = np.array([0.0, 1.0])
    N = 0.0
    bT = np.array([0.0, -1.0])
    last_b, last_N = 1.0, 0.0
    while True:
        x = math.exp(-3*N)
        h2 = H0**2 * (x - eEC*cEC*x*x*bvec[0]**2 + lam)
        if h2 <= 0:
            return {"status": "bounce", "N": N, "b": float(np.hypot(*bvec))}
        H = math.sqrt(h2)
        GC, GR = G*x, r*G*x
        if GC < 1e-8:
            bb = float(np.hypot(*bvec))
            if N - last_N >= 1.0:
                if abs(bb - last_b) / (N - last_N) < 1e-10:
                    return {"status": "ok", "b_inf": bb, "N_end": N}
                last_b, last_N = bb, N
        if N > Nmax:
            return {"status": "no_freeze", "N": N, "b": float(np.hypot(*bvec))}
        A = np.array([[-GR, w], [-w, -GC - GR]])
        dt = eps / H
        # b* aus A b* + GR bT = 0
        if GR > 0:
            bstar = np.linalg.solve(A, -GR*bT)
        else:
            bstar = np.zeros(2)
        bvec = bstar + expm2(A, dt) @ (bvec - bstar)
        N += H * dt

def main(out):
    grid = []
    for r, G, H0, (eEC, cEC), lamf in itertools.product(
            [0.5, 1.0, 1.157, 2.0], [1e2, 1e3, 1e4], [1e-3, 1e-1, 10.0, 1e3],
            [(0, 0.0), (1, 1e-2), (1, 1.0)], [0.0, 1e-6]):
        res = run(r, G, H0, eEC, cEC, lamf)
        res.update({"r": r, "gn0": G, "H0": H0, "e_EC": eEC, "c_EC": cEC, "lam": lamf, "target": r/(1+r)})
        if res["status"] == "ok":
            res["rel_dev"] = res["b_inf"]/res["target"] - 1
        grid.append(res)
    ctrl = []
    for r, G, H0 in [(1.0, 1e2, 1e-3), (1.0, 1e3, 1e-1), (2.0, 1e4, 10.0), (0.5, 1e2, 1e3)]:
        a = run(r, G, H0, 0, 0.0, 0.0, eps=1e-3); b = run(r, G, H0, 0, 0.0, 0.0, eps=2.5e-4)
        ctrl.append({"r": r, "gn0": G, "H0": H0, "eps1e-3": a.get("b_inf"), "eps2.5e-4": b.get("b_inf")})
    json.dump({"grid": grid, "control_eps": ctrl}, open(out, "w"), indent=1)

    ok = [g for g in grid if g["status"] == "ok"]
    print(f"Laeufe: {len(grid)}, eingefroren: {len(ok)}, Bounce: {sum(g['status']=='bounce' for g in grid)}, "
          f"kein Einfrieren: {sum(g['status']=='no_freeze' for g in grid)}")
    for r in [0.5, 1.0, 1.157, 2.0]:
        sel = [g for g in ok if g["r"] == r]
        within = sum(abs(g["rel_dev"]) <= 0.01 for g in sel)
        bs = [g["b_inf"] for g in sel]
        print(f"r={r}: Ziel r/(1+r) = {r/(1+r):.4f}; |b_inf| von {min(bs):.3e} bis {max(bs):.4f}; innerhalb 1 %: {within}/{len(sel)}")
    print("A erfuellt:", len(ok) == len(grid) and all(abs(g["rel_dev"]) <= 0.01 for g in ok))
    print("|b_inf| fuer r = 1, ohne EC, Lambda = 0 (Zeilen g n0, Spalten H0 = 1e-3, 1e-1, 10, 1e3):")
    for G in [1e2, 1e3, 1e4]:
        row = []
        for H0 in [1e-3, 1e-1, 10.0, 1e3]:
            g = [g for g in grid if g["r"] == 1.0 and g["gn0"] == G and g["H0"] == H0 and g["e_EC"] == 0 and g["lam"] == 0.0][0]
            row.append(f"{g['b_inf']:.4e}" if g["status"] == "ok" else g["status"])
        print(f"  g n0 = {G:g}: " + "  ".join(row))
    dev_ec = []
    for g in ok:
        if g["e_EC"] == 1:
            base = [h for h in ok if h["e_EC"] == 0 and all(h[k] == g[k] for k in ("r", "gn0", "H0", "lam"))]
            if base:
                dev_ec.append((abs(g["b_inf"]/base[0]["b_inf"] - 1), g))
    big = [d for d in dev_ec if d[0] > 0.01]
    print(f"B: Einstein-Cartan aendert |b_inf| um > 1 % in {len(big)}/{len(dev_ec)} Faellen"
          + (f"; max {max(d[0] for d in dev_ec):.3e}" if dev_ec else ""))
    for d, g in sorted(big, key=lambda t: -t[0])[:6]:
        print(f"   r={g['r']}, g n0={g['gn0']:g}, H0={g['H0']:g}, c_EC={g['c_EC']}: {d:.3e}")
    bounces = [g for g in grid if g["status"] == "bounce"]
    print(f"B: Bounce in {len(bounces)} Laeufen")
    for g in bounces[:12]:
        print(f"   r={g['r']}, g n0={g['gn0']:g}, H0={g['H0']:g}, c_EC={g['c_EC']}, lam={g['lam']}: N={g['N']:.3f}, |b|={g['b']:.4f}")
    dev_l = []
    for g in ok:
        if g["lam"] > 0:
            base = [h for h in ok if h["lam"] == 0.0 and all(h[k] == g[k] for k in ("r", "gn0", "H0", "e_EC", "c_EC"))]
            if base:
                dev_l.append(abs(g["b_inf"]/base[0]["b_inf"] - 1))
    print(f"C: Lambda aendert |b_inf| um hoechstens {max(dev_l):.3e}" if dev_l else "C: keine Vergleichsfaelle")
    print("Kontrolle Schrittweite:", ctrl)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "k107_out.json")
