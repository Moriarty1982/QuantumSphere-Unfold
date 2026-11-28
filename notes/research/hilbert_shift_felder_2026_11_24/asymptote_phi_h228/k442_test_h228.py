"""k442 (Test H228): phi als Asymptote.

Teil A: Ist phi = x anziehender Fixpunkt einer kurzen Schleife aus Winkeloperationen des Rahmens (Methode H215)?
Teil B: Ist phi der Stand des Gradientenflusses der Vakuumenergie (H225) von 0 nach pi/8 zu einer natuerlichen Uhrzeit?
Vorab-Notiz: Vorab_H228_Asymptote_phi.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k442_test_h228.py > k442_out.txt
"""
import itertools
import math
import numpy as np
from mpmath import mp, mpf, atan, tan, pi as mpi, findroot, nsum, inf, sqrt as msqrt, floor as mfloor
from scipy.optimize import minimize_scalar

mp.dps = 30
Fz = lambda g: nsum(lambda k: 2 ** (1 - g * msqrt(k * (k + 2) / mpf(3))), [1, inf]) - 1
GL_M = findroot(Fz, 1.86)
BETA_M = msqrt((GL_M - 1) / (GL_M + 1))
GL, BETA = float(GL_M), float(BETA_M)

DSTAR = 0.2222220470731
X = math.pi / 12 - DSTAR
SIG = 7.8e-7
W2 = 2 * SIG
RELC = 1e-3
P4, P2 = math.pi / 4, math.pi / 2


def fold(y):
    y = np.mod(y, P2)
    return np.where(y > P4, P2 - y, y)


OPS = {
    "h": lambda t: t / 2,
    "d": lambda t: fold(2 * t),
    "s": lambda t: t / 3,
    "t": lambda t: fold(3 * t),
    "X": lambda t: P4 - t,
    "Y": lambda t: fold(math.pi / 12 - t),
    "Z": lambda t: fold(math.pi / 6 - t),
    "B": lambda t: np.arctan(BETA * np.tan(t)),
    "U": lambda t: fold(np.arctan(np.tan(t) / BETA)),
    "G": lambda t: np.arctan(np.tan(t) / GL),
}
NAMES = list(OPS)
LINEAR = set("hdstXYZ")


def mfold(y):
    y = y - (mpi / 2) * mfloor(y / (mpi / 2))
    return (mpi / 2 - y) if y > mpi / 4 else y


MOPS = {
    "h": lambda t: t / 2, "d": lambda t: mfold(2 * t), "s": lambda t: t / 3, "t": lambda t: mfold(3 * t),
    "X": lambda t: mpi / 4 - t, "Y": lambda t: mfold(mpi / 12 - t), "Z": lambda t: mfold(mpi / 6 - t),
    "B": lambda t: atan(BETA_M * tan(t)), "U": lambda t: mfold(atan(tan(t) / BETA_M)), "G": lambda t: atan(tan(t) / GL_M),
}


def mapply(word, x):
    for c in reversed(word):
        x = MOPS[c](x)
    return x


NG = 4001
XG = np.linspace(0, P4, NG)
H = XG[1] - XG[0]


def fixpoints_from_grid(y):
    d = y - XG
    if np.mean(np.abs(d) < 1e-12) > 0.01:
        return None
    s = np.sign(d)
    idx = np.nonzero(s[:-1] * s[1:] < 0)[0]
    a, b = d[idx], d[idx + 1]
    p = XG[idx] - a * H / (b - a)
    slope = (y[idx + 1] - y[idx]) / H
    z = np.nonzero(d[1:-1] == 0)[0] + 1
    if len(z):
        p = np.concatenate([p, XG[z]])
        slope = np.concatenate([slope, (y[z + 1] - y[z - 1]) / (2 * H)])
    return p, slope


def main():
    print("=" * 92)
    print("H228 (k442)  phi als Asymptote")
    print("=" * 92)
    print(f"beta_sym = {mp.nstr(BETA_M, 18)}, gamma_L = {mp.nstr(GL_M, 18)}")
    print(f"Ziel x = {X:.10f}, sigma = {SIG:.1e}, W2 = +-{W2:.2e}, Wc = x(1 +- {RELC:.0e}) = +-{RELC*X:.2e}")

    # ---------------- Teil A ----------------
    print("\n" + "=" * 92)
    print("Teil A  Schleifen der Laenge 1..5 ueber {h,d,s,t,X,Y,Z,B,U,G}, anziehende Fixpunkte in (0, pi/4)")
    print("=" * 92)
    store = {"": XG.copy()}
    words_by_len = {0: [""]}
    allp, allw = [], []
    nwords = degen = 0
    for L in range(1, 6):
        cur = []
        for c in NAMES:
            for w in words_by_len[L - 1]:
                word = c + w
                y = OPS[c](store[w])
                nwords += 1
                fp = fixpoints_from_grid(y)
                if fp is None:
                    degen += 1
                else:
                    p, sl = fp
                    m = (np.abs(sl) < 1 - 1e-9) & (p > 1e-6) & (p < P4 - 1e-6)
                    if m.any():
                        allp.append(p[m])
                        allw.extend([word] * int(m.sum()))
                if L < 5:
                    store[word] = y
                    cur.append(word)
        words_by_len[L] = cur
        print(f"  Laenge {L}: Woerter bisher {nwords}, identitaetsartig {degen}, anziehende Fixpunkte bisher {sum(len(a) for a in allp)}")
    del store
    P = np.concatenate(allp)
    W = np.array(allw)
    print(f"Woerter gesamt {nwords} (erwartet 111110), identitaetsartig ausgeschlossen {degen}, anziehende Fixpunkte {len(P)}")

    def Nc(x0):
        return int(np.sum(np.abs(P - x0) <= RELC * x0))

    nx = Nc(X)
    rng = np.random.default_rng(228)
    ctrl = rng.uniform(0.02, 0.06, 2000)
    nc = np.array([Nc(c) for c in ctrl])
    p99 = np.percentile(nc, 99)
    print(f"\nHaeufung N_c(x) = {nx};  Kontrollen: Mittel {nc.mean():.2f}, Median {np.median(nc):.0f}, 95. Perz. {np.percentile(nc,95):.0f},"
          f" 99. Perz. {p99:.0f}; Anteil Kontrollen mit N_c >= N_c(x): {np.mean(nc >= nx)*100:.1f} %")
    # Dichte im Bereich [0,02; 0,06] fuer die Poisson-Erwartung in W2
    dens = np.sum((P >= 0.02) & (P <= 0.06)) / 0.04
    lam = dens * 2 * W2
    print(f"Dichte der Fixpunkte in [0,02; 0,06]: {dens:.1f} pro rad  ->  Erwartung in W2 (Breite {2*W2:.2e}): lambda = {lam:.4f}")

    # Kandidaten nahe x exakt nachrechnen
    near = np.nonzero(np.abs(P - X) <= 3 * RELC * X)[0]
    print(f"\nKandidaten mit |x* - x| <= 3e-3 x (Gitterwert): {len(near)}; exakte Nachrechnung (mpmath, 30 Stellen):")
    hits = []
    rows = []
    for i in near:
        w = str(W[i])
        g = lambda t: mapply(w, t) - t
        try:
            r = findroot(g, (mpf(P[i]) - mpf(2e-4), mpf(P[i]) + mpf(2e-4)), solver="anderson")
        except Exception:
            try:
                r = findroot(g, mpf(P[i]))
            except Exception:
                continue
        hd = mpf(10) ** -12
        der = (mapply(w, r + hd) - mapply(w, r - hd)) / (2 * hd)
        dist = float(r) - X
        rows.append((abs(dist), w, float(r), float(der)))
        if abs(dist) <= W2 and abs(der) < 1:
            hits.append((w, float(r), float(der)))
    rows.sort()
    seen = set()
    for ad, w, r, der in rows:
        if w in seen:
            continue
        seen.add(w)
        lin = "stueckweise linear" if set(w) <= LINEAR else ""
        print(f"  {w:6s} x* = {r:.10f}  Abstand {ad:.2e} = {ad/SIG:9.1f} sigma  f' = {der:+.4f}  {lin}")
        if len(seen) >= 15:
            break
    print(f"Treffer in W2 (anziehend): {len(hits)}  {hits}")
    pA = 1 - math.exp(-lam) * sum(lam ** k / math.factorial(k) for k in range(len(hits))) if hits else 1.0
    print(f"Poisson-Wahrscheinlichkeit fuer >= {len(hits)} Treffer bei lambda = {lam:.4f}: {pA:.3g}")
    if hits and pA < 0.01:
        vA = "TRAEGT"
    elif nx > p99:
        vA = "TRAEGT TEILWEISE"
    else:
        vA = "WIDERLEGT"
    print(f"Urteil Teil A: {vA}")
    named = {"pi/8": math.pi / 8, "pi/12": math.pi / 12, "pi/24": math.pi / 24, "pi/16": math.pi / 16, "atan(beta)": math.atan(BETA),
             "eps/8": math.atanh(BETA) / 8}
    print("Benannte Vergleichswerte N_c: " + ", ".join(f"{k} {Nc(v)}" for k, v in named.items()))

    # ---------------- Teil B ----------------
    print("\n" + "=" * 92)
    print("Teil B  Gradientenfluss von 0 nach pi/8, phi(t) = pi/8 - (2/3) atan(tan(3pi/16) e^(-t/tau))  [nicht blind]")
    print("=" * 92)
    t0 = mp.tan(3 * mpi / 16)
    phi_t = lambda T: mpi / 8 - mpf(2) / 3 * atan(t0 * mp.e ** (-T))
    u = mpi / 8 - mpf(X)
    tx = -mp.log(tan(mpf(3) / 2 * u) / t0)
    u2 = u - mpf(SIG)
    stx = -mp.log(tan(mpf(3) / 2 * u2) / t0) - tx
    print(f"t_x/tau = {mp.nstr(tx, 12)}  (sigma_t = {mp.nstr(stx, 4)});  Probe phi(t_x) = {mp.nstr(phi_t(tx), 12)}")
    clocks = {"1": mpf(1), "1/2": mpf(1) / 2, "1/3": mpf(1) / 3, "1/8": mpf(1) / 8, "ln 2": mp.log(2), "eps=artanh beta": mp.atanh(BETA_M),
              "beta_sym": BETA_M, "beta_sym^2": BETA_M ** 2, "1/gamma_L": 1 / GL_M, "1/gamma_L^2": 1 / GL_M ** 2}
    hitB = False
    for k, T in clocks.items():
        ph = phi_t(T)
        dd = float(ph) - X
        hitB |= abs(dd) <= W2
        print(f"  t*/tau = {k:16s} = {mp.nstr(T, 8):>10s}: phi(t*) = {mp.nstr(ph, 10):>12s}  Abstand {dd:+.3e} = {dd/SIG:+12.1f} sigma")
    Tn = mpi / 8 / 3
    phn = phi_t(Tn)
    print(f"  nachtraeglich k t* = pi/8 (t*/tau = pi/24 = {mp.nstr(Tn, 8)}): phi = {mp.nstr(phn, 10)}, Abstand {(float(phn)-X)/SIG:+.1f} sigma;"
          f" 3 t_x/tau / (pi/8) - 1 = {mp.nstr(3*tx/(mpi/8)-1, 5)}")

    # Pruefung der Ordnung: exaktes H225-Modell mit endlichem q
    print("\nPruefung mit exakter Minimierung in delta (H225-Modell, w = 1):")
    DG = np.linspace(0, 2 * np.pi, 4001)

    def V(d, ap, chi, q):
        return -ap * np.cos(2 * (d - chi)) + q * np.cos(3 * d)

    def vmin(ap, chi, q):
        f = lambda d: V(d, ap, chi, q)
        v = f(DG)
        best = np.inf
        for kk in np.argsort(v)[:8]:
            res = minimize_scalar(f, bounds=(DG[max(kk - 1, 0)], DG[min(kk + 1, len(DG) - 1)]), method="bounded",
                                  options={"xatol": 1e-13})
            best = min(best, res.fun)
        return best

    def E(phi, q):
        return vmin(1.0, P4 + phi, q) + vmin(-1.0, phi, q)

    for q in (-0.01, -0.0852, -0.3):
        hh = 1e-3
        curv = (E(math.pi / 8 + hh, q) - 2 * E(math.pi / 8, q) + E(math.pi / 8 - hh, q)) / hh ** 2
        tau = 1 / curv
        # Fluss-Zeit t(x) = int_0^x dphi / (-E'(phi))
        ph = np.linspace(1e-9, X, 801)
        dE = np.array([(E(p + 1e-6, q) - E(p - 1e-6, q)) / 2e-6 for p in ph])
        tt = np.trapezoid(1 / (-dE), ph) if hasattr(np, "trapezoid") else np.trapz(1 / (-dE), ph)
        print(f"  q = {q:+.4f}: E''(pi/8) = {curv:.6f}, t_x/tau = {tt/tau:.6f}  (fuehrende Ordnung {float(tx):.6f})")
    vB = "TRAEGT" if hitB else "WIDERLEGT"
    print(f"Urteil Teil B: {vB}")

    print("\n" + "=" * 92)
    if "TRAEGT" == vA or vB == "TRAEGT":
        v = "TRAEGT"
    elif vA == "TRAEGT TEILWEISE":
        v = "TRAEGT TEILWEISE"
    else:
        v = "WIDERLEGT"
    print(f"H228 Gesamturteil: {v}   (A: {vA}, B: {vB})")


if __name__ == "__main__":
    main()
