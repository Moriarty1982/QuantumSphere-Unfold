"""k69 (bis zur Uebernahme k66): Test der Vorab-Notiz H17 (Commit 2a7271a): Massen aus Potentialen mit Realteil-Invarianten auf dem Tripel-Raum.
V_R = -S + beta S^2 + gamma Q - kappa t - mu L - nu R2 - lambda L^2 auf O^3 (24 reelle Koordinaten),
t = Re((ab)c), L = sum Re a_k, R2 = sum (Re a_k)^2, S = sum |a_k|^2, Q = sum |a_k|^4."""
import numpy as np, os, sys
from scipy.optimize import minimize

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
qc = lambda q: q*np.array([1, -1, -1, -1])
def omul(x, y):     # Cayley-Dickson wie in k22_oktonion_triplett.py
    p, q, r, s = x[:4], x[4:], y[:4], y[4:]
    return np.concatenate([qmul(p, r) - qmul(qc(s), q), qmul(s, p) + qmul(q, qc(r))])
oc = lambda x: x*np.array([1, -1, -1, -1, -1, -1, -1, -1])
E0 = np.eye(8)[0]
TOL = 1e-4

def V(z, b, g, k, mu, nu, la):
    a, bb, c = z[:8], z[8:16], z[16:]
    x = np.array([a@a, bb@bb, c@c]); S = x.sum(); Q = (x**2).sum()
    t = omul(omul(a, bb), c)[0]; r = np.array([a[0], bb[0], c[0]]); L = r.sum()
    return -S + b*S**2 + g*Q - k*t - mu*L - nu*(r**2).sum() - la*L**2

def G(z, b, g, k, mu, nu, la):
    a, bb, c = z[:8], z[8:16], z[16:]
    x = np.array([a@a, bb@bb, c@c]); S = x.sum(); L = a[0] + bb[0] + c[0]
    dt = [oc(omul(bb, c)), oc(omul(c, a)), oc(omul(a, bb))]   # Re((ab)c) = Re(a(bc)) = Re(b(ca)) = Re(c(ab))
    out = []
    for i, u in enumerate((a, bb, c)):
        out.append(-2*u + 4*b*S*u + 4*g*x[i]*u - k*dt[i] - (mu + 2*nu*u[0] + 2*la*L)*E0)
    return np.concatenate(out)

def gmin(p, starts, rng, scale=1.0):
    best = None
    for _ in range(starts):
        r = minimize(V, scale*rng.normal(size=24)/np.sqrt(8), args=p, jac=G, method="BFGS",
                     options=dict(gtol=1e-10, maxiter=4000))
        if best is None or r.fun < best.fun: best = r
    return best

def describe(z):
    blocks = [z[:8], z[8:16], z[16:]]
    n = np.array([np.linalg.norm(u) for u in blocks]); s = n.max()
    srt = np.sort(n); nz = int((srt > TOL*s).sum())
    nd = 1 + sum(abs(srt[i+1]-srt[i]) > TOL*s for i in range(2))
    real = all(np.linalg.norm(u[1:]) < TOL*s for u in blocks)
    return n, nd, nz, real

Kf = lambda n: (n**2).sum()/n.sum()**2

if __name__ == "__main__":
    # Gradientenkontrolle
    rng0 = np.random.default_rng(0); z = rng0.normal(size=24); p = (0.7, 0.3, 1.1, -0.4, 0.6, 0.2)
    num = np.array([(V(z+h, *p)-V(z-h, *p))/2e-6 for h in np.eye(24)*1e-6])
    print(f"Gradientenkontrolle: max. Abweichung {np.abs(num-G(z, *p)).max():.1e}")

    part = sys.argv[1] if len(sys.argv) > 1 else "ab"
    # ------------------------------------------------------------ H17a / H17c
    if "a" in part:
        rng = np.random.default_rng(41); N = 2000; pars = []
        while len(pars) < N:
            b, g = rng.uniform(0.1, 3), rng.uniform(-1, 2)
            k, mu, nu, la = rng.uniform(0, 3), rng.uniform(-2, 2), rng.uniform(-1, 2), rng.uniform(-1, 1)
            if b + g <= 0.05: continue
            pars.append((b, g, k, mu, nu, la))
        counts = {}; three = []; nreal = 0
        for i, p in enumerate(pars):
            r = gmin(p, 20, rng); n, nd, nz, real = describe(r.x)
            counts[(int(nd), nz)] = counts.get((int(nd), nz), 0) + 1; nreal += real
            if nd == 3 and nz == 3: three.append((*p, Kf(n), (n.min()/n.max())**2, real))
        print("\nH17a: Muster des globalen Minimums (verschiedene Normen, von null verschiedene), N = 2000:")
        for key in sorted(counts): print(f"  {key}: {counts[key]}")
        print(f"  drei verschiedene, alle != 0: {len(three)} ({100*len(three)/N:.1f} %)")
        print(f"  Minima auf der reellen Achse (G2 ungebrochen): {nreal} von {N}")
        if three:
            T = np.array(three); Ks = T[:, 6]
            print(f"  davon auf der reellen Achse: {int(T[:,8].sum())} von {len(T)}")
            print("\nH17c: K-Verteilung der Minima mit drei verschiedenen Normen")
            print(f"  K: min {Ks.min():.4f}, Median {np.median(Ks):.4f}, max {Ks.max():.4f}")
            hist, edges = np.histogram(Ks, bins=np.linspace(1/3, 1, 9))
            for h, a_, c_ in zip(hist, edges[:-1], edges[1:]): print(f"    [{a_:.3f}, {c_:.3f}): {h}")
            print(f"  Anteil |K - 2/3| < 0,01: {100*np.mean(np.abs(Ks-2/3) < 0.01):.1f} %  (Schwelle 50 %)")
            print(f"  Anteil x_min/x_max < 1e-3: {100*np.mean(T[:,7] < 1e-3):.1f} %;  kleinstes {T[:,7].min():.2e}")
        np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "k69_three.npy"), np.array(three))

    # ------------------------------------------------------------ H17b
    if "b" in part:
        m = np.array([0.51099895, 105.6583755, 1776.93]); nl = np.sqrt(m/m[2])
        print(f"\nH17b: Lepton-Tripel sqrt(m)/sqrt(m_tau) = {np.round(nl, 6)}, K = {Kf(nl):.6f}")
        rng_b = np.random.default_rng(4117)
        stat = dict(unbeschraenkt=0, kein_lokales_min=0, lokal_nicht_global=0, global_=0); sol = []
        for s in np.logspace(-2, 2, 21):
            n = np.sqrt(s)*nl; Sx = (n**2).sum(); L = n.sum(); P = n.prod(); e2 = n[0]*n[1] + n[0]*n[2] + n[1]*n[2]
            for g in (0.1, 0.3, 1, 3):
                for nu in (0, 0.5, 1, 2, 5, 10, 30):
                    for la in (-1, 0, 1):
                        k = 4*g*L
                        mu = 4*g*(P - L*e2) - 2*la*L
                        b = (4*g*(e2 - L**2) + 2*(1 + nu))/(4*Sx)
                        if not (b > 0 and b + g > 0): stat["unbeschraenkt"] += 1; continue
                        p = (b, g, k, mu, nu, la)
                        z0 = np.zeros(24); z0[0], z0[8], z0[16] = n
                        assert np.abs(G(z0, *p)).max() < 1e-8*max(1, np.abs(G(z0+1e-3, *p)).max())
                        h = 1e-6*np.sqrt(s)
                        Hm = np.array([(G(z0+e, *p)-G(z0-e, *p))/(2*h) for e in np.eye(24)*h]); Hm = (Hm+Hm.T)/2
                        ev = np.linalg.eigvalsh(Hm)
                        if ev.min() < -1e-8*np.abs(ev).max(): stat["kein_lokales_min"] += 1; continue
                        V0 = V(z0, *p); r = gmin(p, 100, rng_b, scale=np.sqrt(s))
                        if r.fun < V0 - 1e-9*abs(V0): stat["lokal_nicht_global"] += 1; continue
                        stat["global_"] += 1; sol.append((s, g, nu, la, b, k, mu))
        print(f"  Gitter 21 x 4 x 7 x 3: {stat}")
        if sol:
            A = np.array(sol)
            for j, name in enumerate(("s", "gamma", "nu", "lambda")):
                print(f"  {name}: Werte mit globalem Minimum {sorted(set(np.round(A[:,j], 4)))}")
            s, g, nu, la, b, k, mu = sol[len(sol)//2]
            print(f"  Beispiel: s = {s:.4g}, beta = {b:.4g}, gamma = {g}, kappa = {k:.4g}, mu = {mu:.4g}, nu = {nu}, lambda = {la}")
            r = gmin((b, g, k, mu, nu, la), 100, rng_b, scale=np.sqrt(s)); n, nd, nz, real = describe(r.x); n = np.sort(n)
            print(f"    wiedergefunden: sqrt(m)/sqrt(m_tau) = {np.round(n/n[2], 6)}, K = {Kf(n):.6f}, reelle Achse: {real}")
