"""k370 (Test H174, Vorab-Notiz d1aebfe vom 26.11.2026): kleine Drehung der geladenen Leptonen aus einer Beimischung der neutralen Form.
Aufruf aus diesem Ordner: python3 k370_test_h174.py > k370_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import least_squares, brentq, minimize

X_LEP, X_R = 0.0395773407, 0.043359
DSTAR = np.pi / 12 - X_LEP
ME, MMU, MTAU, MTAU_E = 0.51099895, 105.6583755, 1776.93, 0.09
S13, S13E = 0.02248, 0.00056
S12, S12E = 0.3036, 0.0064
S23, S23EU, S23ED = 0.470, 0.017, 0.014
T = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]], float)
T2 = T @ T
SQ = np.sqrt(np.array([ME, MMU, MTAU]))


def C(rho, d):
    return np.eye(3) + rho / np.sqrt(2) * (np.exp(1j * d) * T + np.exp(-1j * d) * T2)


def Nhat(dnu, sb):
    l = np.array([1 + np.sqrt(2) * np.cos(dnu + 2 * np.pi * k / 3) for k in range(3)])
    l = l[np.argsort(abs(l))]
    c = l[0] - 1
    b2 = ((l[1] - l[2])**2 - c**2) / 8
    b = sb * np.sqrt(max(b2, 0.0))
    return np.array([[1, b, c], [b, 1, -b], [c, -b, 1]])


def eig_sorted(M):
    v, U = np.linalg.eigh(M)
    o = np.argsort(abs(v))
    return v[o], U[:, o]


def pmns(Ue, Un):
    V = Ue.conj().T @ Un
    P = abs(V)**2
    s13 = P[0, 2]; s12 = P[0, 1] / (1 - s13); s23 = P[1, 2] / (1 - s13)
    J = np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0]))
    sd = J / (np.sqrt(s12 * (1 - s12) * s23 * (1 - s23) * s13) * (1 - s13)) if s13 > 1e-14 else np.nan
    return s12, s23, s13, sd


def z(s12, s23, s13):
    return ((s13 - S13) / S13E, (s12 - S12) / S12E, (s23 - S23) / (S23EU if s23 > S23 else S23ED))


def line(r):
    zz = z(*r[:3])
    return f"th13 = {r[2]:.5f} ({zz[0]:+.1f}), th12 = {r[0]:.5f} ({zz[1]:+.1f}), th23 = {r[1]:.5f} ({zz[2]:+.1f}), sin delta = {r[3]:+.3f}"


print("== Kontrolle: eta = 0 gibt H173 (Elektron auf dem T-Eigenwert 1: delta = +-delta* + 2pi/3 bzw. 4pi/3) ==")
DE = DSTAR + 2 * np.pi / 3
for k in range(3):
    for sg in (1, -1):
        d = sg * DSTAR + 2 * np.pi * k / 3
        N = Nhat(np.pi / 6 - X_LEP, 1); _, Un = eig_sorted(N); _, Ue = eig_sorted(C(1.0, d))
        print(f"   delta = {'+' if sg > 0 else '-'}delta* + {k}*2pi/3: " + line(pmns(Ue, Un)))
lc = np.sort(abs(np.linalg.eigvalsh(C(1.0, DE))))
print(f"   Zirkulant bei delta*: Verhaeltnisse {lc[0]/lc[2]:.6f}, {lc[1]/lc[2]:.6f}; gemessen {SQ[0]/SQ[2]:.6f}, {SQ[1]/SQ[2]:.6f}")
print("   Hinweis: Die erste Fassung dieses Skripts benutzte in der Kontrolle und in Teil a den Zweig delta = delta* (Elektron nicht auf dem T-Eigenwert 1);")
print("   das wurde vor der Auswertung berichtigt. Teile b und c durchlaufen ohnehin alle sechs Zweige und sind unveraendert.")

print("\n== H174a: noetiger Term (aus k369, nicht blind) ==")
for name, x in (("x", X_LEP), ("x_R", X_R)):
    for sb in (1, -1):
        N = Nhat(np.pi / 6 - x, sb); _, Un = eig_sorted(N)
        C0 = C(1.0, DE); l0, U0 = eig_sorted(C0)
        def rot(q):
            R = np.eye(3, dtype=complex)
            R[0, 0] = np.cos(q[0]); R[0, 1] = np.sin(q[0]) * np.exp(-1j * q[1]); R[1, 0] = -np.sin(q[0]) * np.exp(1j * q[1]); R[1, 1] = np.cos(q[0])
            return U0 @ R
        fun = lambda q: float(sum(np.array(z(*pmns(rot(q), Un)[:3]))**2))
        best = min((minimize(fun, [t0, a0], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13}) for t0 in (0.03, 0.07) for a0 in np.arange(0.3, 6.3, 0.75)), key=lambda r: r.fun)
        Ue = rot(best.x)
        dM = Ue @ np.diag(l0) @ Ue.conj().T - C0          # Stoerung in der Platzbasis, gleiche Eigenwerte
        # Zerlegung: zirkulanter Anteil = Mittel ueber Z3
        circ = (dM + T @ dM @ T.T + T2 @ dM @ T2.T) / 3
        nc = dM - circ
        v2, U2 = eig_sorted(C0 + dM)
        chk = max(abs(np.array(pmns(U2, Un)[:3]) - np.array(pmns(Ue, Un)[:3])))
        # reell-symmetrischer Anteil (wie N) gegen imaginaer-antisymmetrischen Anteil
        re_part, im_part = np.linalg.norm(nc.real), np.linalg.norm(nc.imag)
        # Projektion des nicht zirkulanten Anteils auf die A-invariante reelle Form N (ohne Einheitsmatrix)
        N0 = N - np.eye(3); N0nc = N0 - (N0 + T @ N0 @ T.T + T2 @ N0 @ T2.T) / 3
        proj = np.sum(nc.real * N0nc) / np.sum(N0nc * N0nc)
        ang = np.sum(nc.real * N0nc) / (np.linalg.norm(nc) * np.linalg.norm(N0nc))
        print(f"   {name}, b {'+' if sb > 0 else '-'}: th_e = {abs(best.x[0]):.5f}, chi2 = {best.fun:.2f}; |dM| = {np.linalg.norm(dM):.5f}, zirkulant {np.linalg.norm(circ):.5f}, nicht zirkulant {np.linalg.norm(nc):.5f} (reell {re_part:.5f}, imaginaer {im_part:.5f}); Rekonstruktion {chk:.1e}")
        el = (U0.conj().T @ dM @ U0)[0, 1]; elN = (U0.conj().T @ N @ U0)[0, 1]
        print(f"        e-mu-Element der Stoerung in der Z3-Basis: Betrag/(lambda_mu - lambda_e) = {abs(el)/abs(l0[1] - l0[0]):.5f}; Phasendifferenz zum e-mu-Element von N: {np.angle(el/elN):+.4f} rad; |N_emu| = {abs(elN):.4f}, |N_ee| = {abs((U0.conj().T @ N @ U0)[0, 0]):.4f}")
        print(f"        Projektion auf den nicht zirkulanten Teil von N: Koeffizient eta_eff = {proj:+.5f}, Kosinus des Winkels zwischen beiden = {ang:+.4f}")

print("\n== H174b: Beimischung mit festem eta, Massen angepasst (blind) ==")
tgt = SQ / SQ[2]


def fit_branches(eta, N):
    out = []
    for k in range(3):
        for sg in (1, -1):
            d0 = sg * DSTAR + 2 * np.pi * k / 3
            f = lambda p: np.sort(abs(np.linalg.eigvalsh(C(p[0], p[1]) + eta * N)))
            res = lambda p: (f(p)[:2] / f(p)[2] - tgt[:2]) / tgt[:2]
            r = least_squares(res, [1.0, d0], xtol=1e-15, ftol=1e-15, gtol=1e-15)
            if np.max(abs(r.fun)) < 1e-9:
                rho, d = r.x
                key = (round(rho, 7), round(np.mod(d, 2 * np.pi), 7))
                if key not in [o[0] for o in out]:
                    out.append((key, rho, d))
    return out


for name, x in (("x", X_LEP), ("x_R (Kontrolle)", X_R)):
    print(f" Versatz {name} = {x}")
    nb = 0; verdicts = []; seen = set()
    for lab, eta0 in (("tan x", np.tan(x)), ("tan 2x", np.tan(2 * x))):
        for se in (1, -1):
            eta = se * eta0
            for sb in (1, -1):
                N = Nhat(np.pi / 6 - x, sb); _, Un = eig_sorted(N)
                br = fit_branches(eta, N)
                for key, rho, d in br:
                    _, Ue = eig_sorted(C(rho, d) + eta * N)
                    r = pmns(Ue, Un); zz = z(*r[:3]); nb += 1
                    verdicts.append((lab, se, zz))
                    dfold = np.mod(d, 2 * np.pi / 3); dfold = min(dfold, 2 * np.pi / 3 - dfold)
                    sig = (lab, se, round(rho, 6), round(r[2], 6))
                    if sig in seen: continue
                    seen.add(sig)
                    print(f"   eta = {'+' if se > 0 else '-'}{lab} = {eta:+.5f}, b {'+' if sb > 0 else '-'}: rho = {rho:.6f} (K = {(1 + rho**2)/3:.5f}), delta gefaltet = {dfold:.6f} (pi/12 = {np.pi/12:.6f}); " + line(r))
                if not br:
                    print(f"   eta = {'+' if se > 0 else '-'}{lab}, b {'+' if sb > 0 else '-'}: kein Zweig trifft die Massen")
    ok = [v for v in verdicts if abs(v[2][0]) < 2 and abs(v[2][1]) < 2 and abs(v[2][2]) < 3]
    in3 = [v for v in verdicts if abs(v[2][0]) < 3]
    print("   (gleiche Zweige mit anderem Vorzeichen von b oder sin delta sind zusammengefasst)")
    print(f"   Zweige insgesamt: {nb}; vertraeglich (2s/2s/3s): {len(ok)}; th13 innerhalb 3 sigma: {len(in3)}; kleinster |z(th13)|: {min(abs(v[2][0]) for v in verdicts):.1f}")

print("\n== H174b, Zusatz (nicht vorab festgelegt, nur zur Einordnung): welches eta wuerde passen? ==")
for name, x in (("x", X_LEP), ("x_R", X_R)):
    for sb in (1, -1):
        N = Nhat(np.pi / 6 - x, sb); _, Un = eig_sorted(N)
        rows = []
        for eta in np.linspace(-0.2, 0.2, 401):
            for key, rho, d in fit_branches(eta, N):
                _, Ue = eig_sorted(C(rho, d) + eta * N); r = pmns(Ue, Un); zz = z(*r[:3])
                rows.append((sum(np.array(zz)**2), eta, rho, r))
        rows.sort(key=lambda t: t[0])
        c2, eta, rho, r = rows[0]
        print(f"   {name}, b {'+' if sb > 0 else '-'}: bestes eta = {eta:+.4f} (Raster 0,001), chi2 = {c2:.1f}, rho = {rho:.5f}; " + line(r))

print("\n== H174c: Baumpunkt plus Beimischung (blind) ==")
Ntree = Nhat(np.pi / 6, 1); _, Un = eig_sorted(Ntree)
print(f"   N am Baumpunkt: {np.round(Ntree, 6).tolist()}; Eigenwerte {np.round(np.linalg.eigvalsh(Ntree), 6).tolist()}")
r0 = SQ[0] / SQ[1]; nc_ = 0; allz = []
for k in range(3):
    for sg in (1, -1):
        d = sg * np.pi / 12 + 2 * np.pi * k / 3
        C0 = C(1.0, d)
        g = lambda eta: (lambda l: l[0] / l[1] - r0)(np.sort(abs(np.linalg.eigvalsh(C0 + eta * Ntree))))
        etas = np.linspace(-0.5, 0.5, 4001); vals = np.array([g(e) for e in etas]); sols = []
        for i in range(len(etas) - 1):
            if vals[i] * vals[i + 1] < 0 and abs(vals[i] - vals[i + 1]) < 0.05:
                sols.append(brentq(g, etas[i], etas[i + 1], xtol=1e-14))
        l0 = np.sort(abs(np.linalg.eigvalsh(C0)))
        print(f"   delta = {'+' if sg > 0 else '-'}pi/12 + {k}*2pi/3: Eigenwerte am Baumpunkt {np.round(l0, 6).tolist()}; Loesungen eta: {[round(s, 6) for s in sols]}")
        for eta in sols:
            l, Ue = eig_sorted(C0 + eta * Ntree); l = abs(l)
            mt_pred = MMU * (l[2] / l[1])**2; r = pmns(Ue, Un); zz = z(*r[:3]); nc_ += 1; allz.append((zz, mt_pred))
            print(f"        eta = {eta:+.6f}: m_tau vorhergesagt {mt_pred:.2f} MeV (gemessen {MTAU}; relativ {mt_pred/MTAU - 1:+.4f}); " + line(r))
print(f"   Faelle: {nc_}; th13 innerhalb 3 sigma: {sum(abs(a[0][0]) < 3 for a in allz)}; Winkel 2s/2s/3s: {sum(abs(a[0][0]) < 2 and abs(a[0][1]) < 2 and abs(a[0][2]) < 3 for a in allz)}; m_tau auf 1e-3: {sum(abs(a[1]/MTAU - 1) < 1e-3 for a in allz)}")
