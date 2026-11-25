"""k263c (zu H134, nachtraeglich fuer Kontrolle iv): einen Trefferpunkt der Variante B (eps = artanh(beta_sym), Klasse TM1, Raster 2 Grad) mit Matrizen ausgeben.
Aufruf: python3 k263c_trefferpunkt.py"""
import io, contextlib, itertools, numpy as np
from scipy.optimize import least_squares
with contextlib.redirect_stdout(io.StringIO()):
    import k263_test_h134 as k
c = round(k.ETA, 10); D = np.diag(np.exp(c*k.Wl))
# geladene Leptonen: Matrizen in derselben Reihenfolge wie k.charged
m = np.array(k.me_)/max(k.me_); ME = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        if sg[0] == -1: continue
        lam = np.array([sg[i]*m[p[i]] for i in range(3)])
        for e in k.grid:
            Mf = lambda x: np.diag(np.exp(e*k.Wl))@(k.F@np.diag(x)@k.F.conj().T)@np.diag(np.exp(-e*k.Wl))
            r = least_squares(lambda x: (k.sv_sorted(Mf(x))[0] - m)/m, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
            if np.max(abs(r.fun)) > k.TOL: break
            lam = r.x
            if abs(e - c) < 1e-12: ME.append(Mf(lam)); break
ME = np.array(ME); assert len(ME) == len(k.Ce[c]) and max(np.abs(k.sv_sorted(M)[1] - U).max() for M, U in zip(ME, k.Ce[c])) < 1e-9
PHI = np.deg2rad(np.arange(0, 180, 2)); found = None
for m1 in k.M1:
    tgt = k.nu(m1)/k.nu(m1).max(); den = np.where(tgt > 0, tgt, 1.0)
    for p in range(3):
        for phi in PHI:
            Q = k.Qphi_odd(p, 1, phi)
            for order in k.ORD:
                for sgs in itertools.product((1, -1), repeat=2):
                    mu = np.zeros(3); sgn = (1,) + sgs
                    for col, kk in enumerate(order): mu[col] = sgn[col]*tgt[kk]
                    ok = True
                    for e in k.gridB:
                        if e > c + 1e-12: break
                        De = np.diag(np.exp(e*k.Wl)); Mf = lambda x: De@Q@np.diag(x)@Q.T@De
                        r = least_squares(lambda x: (np.sort(abs(np.linalg.eigvalsh(Mf(x)))) - tgt)/den, mu, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14)
                        if np.max(abs(r.fun)) > 1e-7: ok = False; break
                        mu = r.x
                    if not ok: continue
                    Mn = D@Q@np.diag(mu)@Q.T@D; w, V = np.linalg.eigh(Mn); V = V[:, np.argsort(abs(w))]
                    s12, s23, s13 = k.angles(k.Ce[c], V[None])
                    hit = k.in_(s13, k.R13) & k.in_(s23, k.R23) & k.in_(s12, k.J26_1)
                    if hit.any():
                        n = int(np.argwhere(hit)[0][0]); sd = k.delta_of(k.Ce[c], V[None], hit)[0]
                        found = dict(m1=m1, p=p, phi=float(np.rad2deg(phi)), order=order, sgs=sgs, mu=mu, n=n, s12=float(s12[n, 0]), s23=float(s23[n, 0]), s13=float(s13[n, 0]), sd=float(sd), Mn=Mn, Me=ME[n])
                        break
                if found: break
            if found: break
        if found: break
    if found: break
np.set_printoptions(precision=16, linewidth=200)
f = found
print(f"Trefferpunkt: m1 = {f['m1']} eV, fester Platz p = {f['p']}, Vorzeichen +, phi = {f['phi']:.1f} Grad, Zuordnung {f['order']}, Vorzeichen {f['sgs']}, Zweig der geladenen Leptonen Nr. {f['n']}")
print(f"mu = {f['mu']}")
print(f"sin^2 12 = {f['s12']:.10f}, sin^2 23 = {f['s23']:.10f}, sin^2 13 = {f['s13']:.10f}, sin delta = {f['sd']:.10f}")
wl = lambda M: "{" + ", ".join("{" + ", ".join((f"{x.real:.16f}" + (f" + ({x.imag:.16f}) I" if abs(x.imag) > 0 else "")) for x in row) + "}" for row in M) + "}"
print("Mnu = " + wl(f['Mn'].astype(complex).real) + ";")
print("Me = " + wl(f['Me']) + ";")
