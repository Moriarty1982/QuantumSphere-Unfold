"""k369 (Erkundung, nicht blind, 26.11.2026): Abweichung bei sin^2 theta_13 aus H173 beziffern und Herkunft eingrenzen.
Auftrag des Autors: "berechne die abweichung und schau nach woher die kommen koennte".
Aufruf aus diesem Ordner: python3 k369_abweichung.py > k369_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import brentq, minimize

X_LEP = 0.0395773407
BETA = 0.5494056410
S13, S13E = 0.02248, 0.00056
S23, S23EU, S23ED = 0.470, 0.017, 0.014
S12J, S12JE = 0.3036, 0.0064
S12N, S12NE = 0.3088, 0.0067
R_OBS, R_ERR = 0.030016, 0.000457
DM21 = 7.53e-5
DM31 = DM21 / R_OBS
ME, MMU, MTAU = 0.51099895, 105.6583755, 1776.93


def lam(d, rho=1.0):
    return np.array([1 + np.sqrt(2) * rho * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def Rratio(d, rho=1.0):
    m = np.sort(lam(d, rho)**2)
    return (m[1]**2 - m[0]**2) / (m[2]**2 - m[0]**2)


def phi_of(d):
    return 0.5 * np.arctan(np.sqrt(3 * np.tan(d + 2 * np.pi / 3)**2 - 1))


s13_of = lambda d: np.sin(phi_of(d))**2 / 3
s12_of_phi = lambda p: np.cos(p)**2 / (3 - np.sin(p)**2)

print("== 1. Abweichung beziffern ==")
d0 = np.pi / 6 - X_LEP
p0 = phi_of(d0); s0 = s13_of(d0)
p_obs = np.arcsin(np.sqrt(3 * S13)); p_err = 3 * S13E / (2 * np.sin(p_obs) * np.cos(p_obs))
x_th = brentq(lambda x: s13_of(np.pi / 6 - x) - S13, 0.01, 0.2)
x_th_hi = brentq(lambda x: s13_of(np.pi / 6 - x) - (S13 + S13E), 0.01, 0.2); x_th_e = x_th_hi - x_th
x_R = brentq(lambda x: Rratio(np.pi / 6 - x) - R_OBS, 0.01, 0.1)
x_R_e = abs(brentq(lambda x: Rratio(np.pi / 6 - x) - (R_OBS - R_ERR), 0.01, 0.1) - x_R)
print(f"sin2 th13: Vorhersage {s0:.6f}, Messung {S13} +- {S13E}; Differenz {s0 - S13:+.6f} ({(s0 - S13)/S13E:+.1f} sigma); Messung/Vorhersage = {S13/s0:.4f} +- {S13E/s0:.4f}")
print(f"Amplitude |U_e3|: Vorhersage {np.sqrt(s0):.5f}, Messung {np.sqrt(S13):.5f} +- {S13E/(2*np.sqrt(S13)):.5f}; Differenz {np.sqrt(S13) - np.sqrt(s0):+.5f}")
print(f"Drehwinkel phi: Vorhersage {p0:.6f} ({np.degrees(p0):.3f} Grad), Messung {p_obs:.6f} +- {p_err:.6f} ({np.degrees(p_obs):.3f} Grad); Verhaeltnis {p_obs/p0:.4f} +- {p_err/p0:.4f}")
print(f"Versatz: Leptonen x = {X_LEP:.6f}; aus R: x_R = {x_R:.6f} +- {x_R_e:.6f}; aus th13: x_th = {x_th:.6f} +- {x_th_e:.6f}")
print(f"   x_th/x = {x_th/X_LEP:.4f} +- {x_th_e/X_LEP:.4f}; x_th/x_R = {x_th/x_R:.4f} +- {x_th/x_R*np.hypot(x_th_e/x_th, x_R_e/x_R):.4f}; x_th - x_R = {x_th - x_R:.6f} ({(x_th - x_R)/np.hypot(x_th_e, x_R_e):.1f} sigma)")
print(f"   Naeherung kleiner Versatz: sin2 th13 ~ 2x/(3 sqrt3) = {2*X_LEP/(3*np.sqrt(3)):.6f} (exakt {s0:.6f})")
print(f"TM1-Beziehung bei gemessenem th13: sin2 th12 = {s12_of_phi(p_obs):.6f} (JUNO {(s12_of_phi(p_obs) - S12J)/S12JE:+.2f} sigma, NuFIT {(s12_of_phi(p_obs) - S12N)/S12NE:+.2f} sigma)")

print("\n== 2. Kandidat: Koide-Wert der Neutrinos (rho frei) ==")
print("tan^2(2 phi) = 3 tan^2(delta + 2pi/3) - 1 haengt nicht von rho ab (exakt in k369b). th13 legt also delta_nu fest, R dann rho.")
d_th = np.pi / 6 - x_th
print(f"delta_nu aus th13: {d_th:.6f} = pi/6 - {x_th:.6f}; R bei rho = 1: {Rratio(d_th):.6f} ({(Rratio(d_th) - R_OBS)/R_ERR:+.1f} sigma)")
sols = []
grid = np.linspace(0.3, 3.0, 2701)
vals = np.array([Rratio(d_th, r) - R_OBS for r in grid])
for i in range(len(grid) - 1):
    if vals[i] * vals[i + 1] < 0 and abs(vals[i]) < 1 and abs(vals[i + 1]) < 1:
        sols.append(brentq(lambda r: Rratio(d_th, r) - R_OBS, grid[i], grid[i + 1]))
for rho in sols:
    l = lam(d_th, rho); o = np.argsort(abs(l)); l = l[o]
    K = (l**2).sum() / l.sum()**2
    sc = np.sqrt(DM31 / (l[2]**4 - l[0]**4))                 # m_i = sc * lambda_i^2 (eV)
    m = sc * l**2
    drho = 1e-5
    dRdrho = (Rratio(d_th, rho + drho) - Rratio(d_th, rho - drho)) / (2 * drho)
    dRdx = (Rratio(d_th - 1e-6, rho) - Rratio(d_th + 1e-6, rho)) / 2e-6
    rho_e = np.hypot(R_ERR, dRdx * x_th_e) / abs(dRdrho)
    print(f"   rho = {rho:.5f} +- {rho_e:.5f}: K_nu = (1 + rho^2)/3 = {K:.5f} (K - 2/3 = {K - 2/3:+.5f} +- {2*rho*rho_e/3:.5f}); lambda = {np.round(l, 5)}; "
          f"Massen = {np.round(1e3*m, 3)} meV, Summe {1e3*m.sum():.2f} meV")
    # reelle Loesung der Ein-Feld-Form pruefen
    a = l.sum() / 3; c = l[0] - a; b2 = ((l[1] - l[2])**2 - c**2) / 8
    print(f"      Ein-Feld-Form: a = {a:.5f}, c = {c:.5f}, b^2 = {b2:.6f}; sin2 th13 = {np.sin(0.5*np.arctan(np.sqrt(8*b2/c**2)))**2/3:.6f}")

print("\n== 3. Kandidat: ungleiche Diagonale (K = 2/3, delta_nu aus R oder aus den Leptonen) ==")
for name, x in (("x (Leptonen)", X_LEP), ("x_R (aus R)", x_R)):
    l = lam(np.pi / 6 - x); l = l[np.argsort(abs(l))]
    for ptar, lab in ((phi_of(np.pi / 6 - x), "Ein-Feld (Kontrolle)"), (p_obs, "gemessenes th13")):
        fc = l[2] * np.cos(ptar)**2 + l[1] * np.sin(ptar)**2
        dd = l[2] * np.sin(ptar)**2 + l[1] * np.cos(ptar)**2
        f = (l[0] + fc) / 2; c = l[0] - f; b = (l[2] - l[1]) * np.sin(ptar) * np.cos(ptar) / np.sqrt(2)
        N = np.array([[f, b, c], [b, dd, -b], [c, -b, f]])
        ev = np.sort(np.linalg.eigvalsh(N))
        print(f"   {name}, {lab}: f = {f:.6f}, d = {dd:.6f}, d - f = {dd - f:+.6f} (relativ zur mittleren Diagonale {3*(dd - f)/(2*f + dd):+.5f}), b = {b:.6f}, c = {c:.6f}; Spektrum ok: {np.allclose(ev, np.sort(l))}")

print("\n== 4. Kandidat: Maske mit freiem eps (Variante A) ==")
src = open("../../frame_h134/k263_test_h134.py").read().split("ETA, HOPF =")[0].replace("STEP = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0", "STEP = 2.0")
ns = {}; exec(src, ns)
charged, angles = ns["charged"], ns["angles"]
ETA = float(np.arctanh(BETA))
egrid = sorted(set(list(np.round(np.arange(0, 1.0001, 0.01), 6)) + [round(ETA, 10)]))
Ce, worst = charged(egrid)


def nu_cases(d):
    l = lam(d); l = l[np.argsort(abs(l))]
    out = []
    for p in range(3):
        q, r_ = [i for i in range(3) if i != p]
        for sgn in (1, -1):
            for sb in (1, -1):
                a = l.sum() / 3; c = l[0] - a
                b = sb * np.sqrt(((l[1] - l[2])**2 - c**2) / 8)
                N = a * np.eye(3); N[q, r_] = N[r_, q] = sgn * c; N[p, q] = N[q, p] = b; N[p, r_] = N[r_, p] = -sgn * b
                v, vec = np.linalg.eigh(N); out.append(vec[:, np.argsort(abs(v))])
    return np.array(out)


def chi2(s12, s23, s13):
    e23 = np.where(s23 > S23, S23EU, S23ED)
    return ((s13 - S13) / S13E)**2 + ((s12 - S12J) / S12JE)**2 + ((s23 - S23) / e23)**2


for name, x in (("x (Leptonen)", X_LEP), ("x_R (aus R)", x_R)):
    UN = nu_cases(np.pi / 6 - x)
    best = []
    for e in egrid:
        if e not in Ce: continue
        s12, s23, s13 = angles(Ce[e], UN)
        c2 = chi2(s12, s23, s13); i = np.unravel_index(np.argmin(c2), c2.shape)
        best.append((c2[i], e, s13[i], s12[i], s23[i], np.min(abs(s13 - S13)) / S13E))
    best.sort()
    print(f"   {name}: Rest der Massenanpassung {worst:.1e}; eps-Raster 0 .. 1 (Schritt 0,01), {len(best)} Werte")
    for c2, e, a13, a12, a23, d13 in best[:3]:
        print(f"      eps = {e:.4f}: chi2(th13, th12 JUNO, th23) = {c2:.1f}; sin2 th13 = {a13:.5f}, th12 = {a12:.5f}, th23 = {a23:.5f}")
    at = [bb for bb in best if abs(bb[1] - round(ETA, 10)) < 1e-9][0]
    print(f"      eps = artanh(beta_sym) = {ETA:.4f}: chi2 = {at[0]:.1f}; kleinster Abstand in th13 ueber alle Faelle {at[5]:.1f} sigma")
    e0 = [bb for bb in best if bb[1] == 0.0][0]
    print(f"      eps = 0: chi2 = {e0[0]:.1f}")

print("\n== 5. Kandidat: kleine Drehung der geladenen Leptonen (e-mu), Z3 gebrochen ==")
T = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]], float)
tv, tvec = np.linalg.eig(T)
w = np.exp(2j * np.pi / 3)


def pmns(UN, order, th_e, alpha):
    o = [int(np.argmin(abs(tv - t))) for t in order]
    Ue = tvec[:, o]
    Rm = np.eye(3, dtype=complex)
    Rm[0, 0] = np.cos(th_e); Rm[0, 1] = np.sin(th_e) * np.exp(-1j * alpha)
    Rm[1, 0] = -np.sin(th_e) * np.exp(1j * alpha); Rm[1, 1] = np.cos(th_e)
    V = (Ue @ Rm).conj().T @ UN
    P = abs(V)**2; s13 = P[0, 2]; s12 = P[0, 1] / (1 - s13); s23 = P[1, 2] / (1 - s13)
    J = np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0]))
    sd = J / (np.sqrt(s12 * (1 - s12) * s23 * (1 - s23) * s13) * (1 - s13))
    return s12, s23, s13, sd


gst = np.sqrt(ME / MMU)
print(f"natuerliche Groesse (Gatto-Sartori-Tonin-artig): sqrt(m_e/m_mu) = {gst:.5f}; sqrt(m_mu/m_tau) = {np.sqrt(MMU/MTAU):.5f}")
for name, x in (("x (Leptonen)", X_LEP), ("x_R (aus R)", x_R)):
    l = lam(np.pi / 6 - x); l = l[np.argsort(abs(l))]
    a = l.sum() / 3; c = l[0] - a; b = np.sqrt(((l[1] - l[2])**2 - c**2) / 8)
    res_all = []
    for sb in (1, -1):
        N = np.array([[a, sb * b, c], [sb * b, a, -sb * b], [c, -sb * b, a]])
        v, vec = np.linalg.eigh(N); UN = vec[:, np.argsort(abs(v))]
        for order in ((1, w, np.conj(w)), (1, np.conj(w), w)):
            # kleinster Winkel, der th13 trifft
            als = np.linspace(0, 2 * np.pi, 721)
            f13 = lambda th, al: pmns(UN, order, th, al)[2] - S13
            thmin = None
            for th in np.linspace(0.0, 0.3, 601):
                vals_ = np.array([f13(th, al) for al in als])
                if vals_.max() >= 0:
                    thmin = th; almin = als[np.argmax(vals_)]; break
            r_ = pmns(UN, order, thmin, almin)
            # bei th_e = sqrt(m_e/m_mu): Phase, die th13 trifft
            vals_ = np.array([f13(gst, al) for al in als]); hits = []
            for i in range(len(als) - 1):
                if vals_[i] * vals_[i + 1] < 0:
                    al = brentq(lambda t: f13(gst, t), als[i], als[i + 1]); hits.append((al,) + pmns(UN, order, gst, al))
            # beste Anpassung (th_e, alpha) an th13, th12 (JUNO), th23
            fun = lambda q: float(chi2(*pmns(UN, order, q[0], q[1])[:3]))
            bestfit = min((minimize(fun, [t0, a0], method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12}) for t0 in (0.03, 0.07, 0.12) for a0 in (0.5, 2.0, 3.5, 5.0)), key=lambda z: z.fun)
            res_all.append((sb, order, thmin, almin, r_, hits, bestfit, pmns(UN, order, bestfit.x[0], bestfit.x[1])))
    for sb, order, thmin, almin, r_, hits, bf, rr in res_all:
        tag = f"b {'+' if sb > 0 else '-'}, mu = {'omega' if abs(order[1] - w) < 1e-9 else 'omega*'}"
        print(f"   {name}, {tag}: kleinster Winkel fuer th13: {thmin:.4f} (alpha = {almin:.3f}): th12 = {r_[0]:.5f}, th23 = {r_[1]:.5f}, sin delta = {r_[3]:+.3f}")
        for h in hits:
            print(f"        th_e = sqrt(m_e/m_mu), alpha = {h[0]:.4f}: th13 = {h[3]:.5f}, th12 = {h[1]:.5f} (JUNO {(h[1]-S12J)/S12JE:+.2f}), th23 = {h[2]:.5f} ({(h[2]-S23)/(S23EU if h[2] > S23 else S23ED):+.2f}), sin delta = {h[4]:+.3f}")
        q = bf.x
        print(f"        beste Anpassung: th_e = {abs(q[0]):.5f}, alpha = {q[1] % (2*np.pi):.4f}, chi2 = {bf.fun:.2f} (3 Messgroessen, 2 Parameter): th13 = {rr[2]:.5f}, th12 = {rr[0]:.5f}, th23 = {rr[1]:.5f}, sin delta = {rr[3]:+.3f}")
