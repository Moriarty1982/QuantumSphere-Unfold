"""k368 (H173): Drehwinkel der Mischung aus dem Spektrum (Ein-Feld-Form, gleiche Diagonale), mit und ohne Maske.
Vorab-Notiz Vorab_Notiz_H173_Drehwinkel_aus_Spektrum.md (Commit 93bdc7f).
Funktionen charged, angles, delta_of unveraendert aus ../frame_h134/k263_test_h134.py (dort aus k100).
Aufruf aus diesem Ordner: python3 k368_test_h173.py > k368_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import least_squares, minimize_scalar

X_LEP = 0.0395773407
BETA = 0.5494056410
S13, S13E = 0.02248, 0.00056
R23 = (0.430, 0.596)
J26 = (0.2908, 0.3164)
S12_NUFIT, S12_NUFIT_E = 0.3088, 0.0067
S12_JUNO, S12_JUNO_E = 0.3036, 0.0064
R_OBS, R_ERR = 0.030016, 0.000457
XNU, XNU_E = 0.04336, 0.00213

T = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]], float)
A = np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]], float)


def brannen(d):
    return np.array([1 + np.sqrt(2) * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def Rratio(d):
    m = np.sort(brannen(d)**2)
    return (m[1]**2 - m[0]**2) / (m[2]**2 - m[0]**2)


def field(lam_fixed, lam_rest, sign=+1):
    """N = [[a,b,c],[b,a,-b],[c,-b,a]] mit Eigenwert a + c = lam_fixed auf w = (1,0,1)/sqrt2 und den beiden anderen lam_rest."""
    a = (lam_fixed + sum(lam_rest)) / 3
    c = lam_fixed - a
    b2 = ((lam_rest[0] - lam_rest[1])**2 - c**2) / 8
    if b2 < -1e-14:
        return None
    b = sign * np.sqrt(max(b2, 0.0))
    return np.array([[a, b, c], [b, a, -b], [c, -b, a]])


def Ue_T():
    vals, vecs = np.linalg.eig(T)
    o = [int(np.argmin(abs(vals - t))) for t in (1, np.exp(2j * np.pi / 3), np.exp(-2j * np.pi / 3))]
    return vecs[:, o]


def mixing(N, Ue):
    vals, vecs = np.linalg.eigh(N)
    o = np.argsort(abs(vals))
    V = Ue.conj().T @ vecs[:, o]
    P = abs(V)**2
    s13 = P[0, 2]; s12 = P[0, 1] / (1 - s13); s23 = P[1, 2] / (1 - s13)
    J = np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0]))
    sd = J / np.sqrt(s12 * (1 - s12) * s23 * (1 - s23) * s13) / (1 - s13) if s13 > 1e-14 else np.nan
    return s12, s23, s13, sd, vals[o]


def closed(d):
    psi = d + 2 * np.pi / 3
    t2 = 3 * np.tan(psi)**2 - 1
    if t2 < 0:
        return None
    phi = 0.5 * np.arctan(np.sqrt(t2))
    return phi, np.sin(phi)**2 / 3, np.cos(phi)**2 / (3 - np.sin(phi)**2)


Ue = Ue_T()
print("== H173a: Winkel aus dem Spektrum (Zahlenprobe; exakt in k368b) ==")
for name, d in (("pi/6 (Baumwert)", np.pi / 6), ("pi/6 - x", np.pi / 6 - X_LEP), ("pi/6 - 0.02", np.pi / 6 - 0.02), ("pi/6 + x", np.pi / 6 + X_LEP)):
    lam = brannen(d); o = np.argsort(abs(lam)); lam = lam[o]
    N = field(lam[0], lam[1:])
    cf = closed(d)
    if N is None:
        print(f"delta_nu = {name}: keine reelle Loesung (b^2 < 0); geschlossene Form: {cf}")
        continue
    s12, s23, s13, sd, vals = mixing(N, Ue)
    print(f"delta_nu = {name}: lambda = {np.round(lam, 6)}, N-Eigenwerte = {np.round(vals, 6)}, A-invariant: {np.allclose(A.T @ N @ A, N)}, Diagonale gleich: {np.allclose(np.diag(N), N[0, 0])}")
    print(f"     sin2 th13 = {s13:.8f}, sin2 th12 = {s12:.8f}, sin2 th23 = {s23:.8f}, sin delta = {sd:+.6f}; geschlossene Form: phi = {cf[0]:.8f}, {cf[1]:.8f}, {cf[2]:.8f}; "
          f"Rest {abs(s13 - cf[1]):.1e}, {abs(s12 - cf[2]):.1e}")

print("\n== H173b: Test ohne Maske ==")
phi, s13p, s12p = closed(np.pi / 6 - X_LEP)
print(f"x = {X_LEP} (Leptonen): sin2 th13 = {s13p:.6f} gegen {S13} +- {S13E}: z = {(s13p - S13) / S13E:+.1f}; "
      f"sin2 th12 = {s12p:.6f}: NuFIT z = {(s12p - S12_NUFIT) / S12_NUFIT_E:+.2f}, JUNO z = {(s12p - S12_JUNO) / S12_JUNO_E:+.2f}; R = {Rratio(np.pi/6 - X_LEP):.6f}")
h = 1e-6
ds13 = (closed(np.pi / 6 - XNU - h)[1] - closed(np.pi / 6 - XNU + h)[1]) / (2 * h)
s13n = closed(np.pi / 6 - XNU)[1]; e13n = abs(ds13) * XNU_E
print(f"x_nu = {XNU} +- {XNU_E} (Neutrino-Daten, aus R): sin2 th13 = {s13n:.6f} +- {e13n:.6f}; z = {(s13n - S13) / np.hypot(e13n, S13E):+.2f}")
xs = minimize_scalar(lambda x: (closed(np.pi / 6 - x)[1] - S13)**2, bounds=(0.01, 0.1), method='bounded', options={'xatol': 1e-12}).x
print(f"Rueckwaerts: sin2 th13 = {S13} verlangt x = {xs:.6f}; dort R = {Rratio(np.pi/6 - xs):.6f} (z = {(Rratio(np.pi/6 - xs) - R_OBS) / R_ERR:+.2f}), sin2 th12 = {closed(np.pi/6 - xs)[2]:.6f}")

print("\n== H173d: gemeinsame Anpassung (x frei; R und sin2 th13) ==")
chi2 = lambda x: ((Rratio(np.pi / 6 - x) - R_OBS) / R_ERR)**2 + ((closed(np.pi / 6 - x)[1] - S13) / S13E)**2
r = minimize_scalar(chi2, bounds=(0.01, 0.1), method='bounded', options={'xatol': 1e-12})
print(f"chi2_min = {r.fun:.2f} bei x = {r.x:.6f} (ein Freiheitsgrad; Schwelle 3.84): R = {Rratio(np.pi/6 - r.x):.6f} ({(Rratio(np.pi/6 - r.x) - R_OBS)/R_ERR:+.2f} sigma), "
      f"sin2 th13 = {closed(np.pi/6 - r.x)[1]:.6f} ({(closed(np.pi/6 - r.x)[1] - S13)/S13E:+.2f} sigma) -> {'vertraeglich' if r.fun < 3.84 else 'nicht vertraeglich'}")

print("\n== H173e: Varianten (Bericht) ==")
d = np.pi / 6 - X_LEP
lam = brannen(d); lam = lam[np.argsort(abs(lam))]
for fix in range(3):
    rest = [lam[i] for i in range(3) if i != fix]
    N = field(lam[fix], rest)
    if N is None:
        print(f"Feldebene, feste Spalte = nu_{fix+1}: keine reelle Loesung"); continue
    s12, s23, s13, sd, _ = mixing(N, Ue)
    print(f"Feldebene, feste Spalte = nu_{fix+1}: sin2 th13 = {s13:.6f}, th12 = {s12:.6f}, th23 = {s23:.6f}")
mm = lam**2
for fix in range(3):
    rest = [mm[i] for i in range(3) if i != fix]
    N = field(mm[fix], rest)
    if N is None:
        print(f"Massenebene (gleiche Diagonale auf N^2-Spektrum), feste Spalte = nu_{fix+1}: keine reelle Loesung"); continue
    s12, s23, s13, sd, _ = mixing(N, Ue)
    print(f"Massenebene, feste Spalte = nu_{fix+1}: sin2 th13 = {s13:.6f}, th12 = {s12:.6f}, th23 = {s23:.6f}")

print("\n== H173c: Frame-Uebertragung mit der Maske ==")
src = open("../frame_h134/k263_test_h134.py").read().split("ETA, HOPF =")[0].replace("STEP = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0", "STEP = 2.0")
ns = {}; exec(src, ns)
charged, angles, delta_of, Wl = ns["charged"], ns["angles"], ns["delta_of"], ns["Wl"]
ETA = float(np.arctanh(BETA))
grid = sorted(set(list(np.round(np.arange(0, ETA, 0.01), 6)) + [round(ETA, 10)]))
Ce, worst = charged(grid)
print(f"eps = artanh(beta_sym) = {ETA:.7f}; Massen der geladenen Leptonen: groesster Rest {worst:.1e}; Zweige bei eps = 0: {len(Ce[0.0])}, bei eta: {len(Ce[round(ETA, 10)]) if round(ETA, 10) in Ce else 0}")


def nu_cases(d, level="feld"):
    lam = brannen(d); lam = lam[np.argsort(abs(lam))]
    out = []
    for p in range(3):
        q, r_ = [i for i in range(3) if i != p]
        for sgn in (1, -1):
            for sb in (1, -1):
                a = lam.sum() / 3; c = lam[0] - a
                b2 = ((lam[1] - lam[2])**2 - c**2) / 8
                if b2 < 0: continue
                b = sb * np.sqrt(b2)
                # Ein-Feld-Form in allgemeiner Lage: w = (e_q + sgn e_r)/sqrt2 Eigenvektor zu a + c; gleiche Diagonale a
                N = a * np.eye(3)
                N[q, r_] = N[r_, q] = sgn * c
                N[p, q] = N[q, p] = b
                N[p, r_] = N[r_, p] = -sgn * b
                vals, vecs = np.linalg.eigh(N); o = np.argsort(abs(vals))
                w = np.zeros(3); w[q] = 1 / np.sqrt(2); w[r_] = sgn / np.sqrt(2)
                assert abs(abs(vecs[:, o[0]] @ w) - 1) < 1e-9 and np.allclose(np.diag(N), a)
                out.append(((p, sgn, sb), N, vecs[:, o]))
    return out


cases = nu_cases(np.pi / 6 - X_LEP)
UN = np.array([c[2] for c in cases])
for e, lab in ((0.0, "eps = 0 (Kontrolle)"), (round(ETA, 10), "eps = artanh(beta_sym), Variante A")):
    UE = Ce[e]
    s12, s23, s13 = angles(UE, UN)
    ok13_2 = abs(s13 - S13) < 2 * S13E; ok13_3 = abs(s13 - S13) < 3 * S13E
    ok = ok13_2 & (s23 >= R23[0]) & (s23 <= R23[1]) & (s12 >= J26[0]) & (s12 <= J26[1])
    print(f"{lab}: Faelle {s13.size} ({UE.shape[0]} Zweige x {UN.shape[0]} Neutrino-Faelle); sin2 th13 Spanne [{s13.min():.6f}, {s13.max():.6f}]; "
          f"innerhalb 3 sigma: {int(ok13_3.sum())}, innerhalb 2 sigma: {int(ok13_2.sum())}, alle drei Bedingungen: {int(ok.sum())}")
    vals_ = np.unique(np.round(np.stack([s13.ravel(), s12.ravel(), s23.ravel()], 1), 6), axis=0)
    print(f"     verschiedene (th13, th12, th23): {len(vals_)}; naechste an th13 = {S13}:")
    for row in vals_[np.argsort(abs(vals_[:, 0] - S13))][:6]:
        print(f"        sin2 th13 = {row[0]:.6f} ({(row[0] - S13) / S13E:+.1f} sigma), sin2 th12 = {row[1]:.6f}, sin2 th23 = {row[2]:.6f}")
    if e == 0.0:
        print(f"     Kontrolle: kleinster Abstand zu b (sin2 th13 = {s13p:.8f}): {np.min(abs(s13 - s13p)):.1e}")
    if ok.any():
        sd = delta_of(UE, UN, ok)
        print(f"     Treffer: sin delta zwischen {sd.min():+.4f} und {sd.max():+.4f}")
# Variante B (Bericht): M_nu = D N^2 D ohne Nachanpassung
D = np.diag(np.exp(ETA * Wl))
UNB, RB = [], []
for key, N, _ in cases:
    M = D @ (N @ N) @ D
    vals, vecs = np.linalg.eigh(M); o = np.argsort(abs(vals)); UNB.append(vecs[:, o]); mv = abs(vals[o])
    RB.append((mv[1]**2 - mv[0]**2) / (mv[2]**2 - mv[0]**2))
UNB = np.array(UNB); s12, s23, s13 = angles(Ce[round(ETA, 10)], UNB)
print(f"Variante B (Bericht, ohne Nachanpassung): R nach Maske zwischen {min(RB):.3e} und {max(RB):.3e} (R_obs = {R_OBS}); sin2 th13 Spanne [{s13.min():.6f}, {s13.max():.6f}]; "
      f"innerhalb 3 sigma: {int((abs(s13 - S13) < 3 * S13E).sum())}")
