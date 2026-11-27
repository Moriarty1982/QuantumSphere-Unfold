"""k423: Test H210. Baender als Grosskreis-Streifen mit Muster, das sich m = 16/d-mal wiederholt.
Aufruf: python k423_test_h210.py > k423_out.txt"""
import itertools, math, sys, numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize
names = ["R", "C", "H", "O", "S"]; dim = np.array([1.0, 2, 4, 8, 16]); mrep = (16 / dim).astype(int)
P5 = list(itertools.combinations(range(5), 2)); P4 = list(itertools.combinations(range(4), 2))
targets = [90.0, math.degrees(math.acos(1/3)), math.degrees(math.acos(1/math.sqrt(5))), 60.0, 57.569, math.degrees(math.acos(1/math.sqrt(3))), 45.0]

def frame(n):
    a = np.cross(n, [0.0, 0.0, 1.0])
    if np.linalg.norm(a) < 1e-8: a = np.array([1.0, 0, 0])
    a /= np.linalg.norm(a); return a, np.cross(n, a)
def unit(x): v = x.reshape(-1, 3); return v / np.linalg.norm(v, axis=1, keepdims=True)
def phi(x, n, m, al, sig, wave=True):
    e1, e2 = frame(n); t = np.arcsin(np.clip(x @ n, -1, 1)); w = np.exp(-t * t / (2 * sig * sig))
    return w * np.cos(m * np.arctan2(x @ e2, x @ e1) - al) if wave else w
TG, TW = np.polynomial.legendre.leggauss(15)
def cross_full(ni, nj, mi, mj, ai, aj, sig, wave=True, ns=5760):
    """Kreuzterm ueber das ganze Band i (ohne Symmetrieannahme)."""
    e1, e2 = frame(ni); s = (np.arange(ns) + 0.5) * 2 * math.pi / ns; tot = 0.0
    for tg, tw in zip(TG * 4 * sig, TW * 4 * sig):
        x = math.cos(tg) * (np.outer(np.cos(s), e1) + np.outer(np.sin(s), e2)) + math.sin(tg) * ni
        fi = math.exp(-tg * tg / (2 * sig * sig)) * (np.cos(mi * s - ai) if wave else 1.0)
        tot += tw * math.cos(tg) * np.sum(fi * phi(x, nj, mj, aj, sig, wave)) * 2 * math.pi / ns
    return tot
SG, SW = np.polynomial.legendre.leggauss(240)
def cross_even(ni, nj, mi, mj, ai, aj, sig):
    """Kreuzterm zweier Wellen mit geradem m: Fenster um eine Kreuzung, mal 2 (Gegenpunkt traegt gleich bei)."""
    p = np.cross(ni, nj); sn = np.linalg.norm(p)
    if sn < 1e-6: return 0.0 if mi != mj else None
    p /= sn; e1, e2 = frame(ni); s0 = math.atan2(p @ e2, p @ e1); Lh = min(math.pi / 2, 6 * sig / sn + 6 * sig)
    s = s0 + SG * Lh; tot = 0.0
    for tg, tw in zip(TG * 4 * sig, TW * 4 * sig):
        x = math.cos(tg) * (np.outer(np.cos(s), e1) + np.outer(np.sin(s), e2)) + math.sin(tg) * ni
        tot += tw * math.cos(tg) * np.sum(SW * Lh * math.exp(-tg * tg / (2 * sig * sig)) * np.cos(mi * s - ai) * phi(x, nj, mj, aj, sig))
    return 2 * tot
def e_wave(z, sig, amp):
    v = unit(z[:12]); al = z[12:]; e = 0.0
    for i, j in P4:
        c = cross_even(v[i], v[j], mrep[i], mrep[j], al[i], al[j], sig); e += amp[i] * amp[j] * c
    return e
def run_start(args):
    seed, sig, amp = args; r = np.random.default_rng(seed)
    z0 = np.concatenate([r.standard_normal(12), r.uniform(0, 2 * math.pi, 4)])
    res = minimize(e_wave, z0, args=(sig, amp), method="BFGS", options={"maxiter": 300, "gtol": 1e-7})
    return res.fun, res.x
def angles(v): return np.degrees(np.arccos(np.clip(np.abs(v @ v.T), 0, 1)))

def e_fill(x, w, n):
    v = unit(x); e = 0.0
    for i, j in itertools.combinations(range(n), 2):
        c = abs(np.clip(v[i] @ v[j], -1, 1)); e += w[i] * w[j] / max(math.sqrt(1 - c * c), 1e-9)
    return e

if __name__ == "__main__":
    print("== H210a (nicht blind): Belegung ohne Phase, Gesetz 1/sin ==")
    rng = np.random.default_rng(210)
    for lab, w in (("Inhalt je Wiederholung, w_i = m_i", mrep.astype(float)), ("Inhalt je Band, w_i = 1", np.ones(5))):
        best = min((minimize(e_fill, rng.standard_normal(15), args=(w, 5), method="BFGS") for _ in range(300)), key=lambda r: r.fun)
        M = angles(unit(best.x)); print(f"   {lab}: Energie {best.fun:.4f}; " + "  ".join(f"{names[i]}{names[j]} {M[i,j]:.2f}" for i, j in P5))
    print("   Vergleich: k422 Teil 3 (322.1532; RC 89.54 ... OS 35.59) und k399 (fuenf gleiche Baender 59.14/74.03).")

    print("\n== H210b (nicht blind): Welle, Kreuzterme fuer Zufallslagen (volle Integration, sigma = 5 Grad) ==")
    sig = math.radians(5); worst_odd = 0.0; typ_even = []
    for trial in range(6):
        v = unit(rng.standard_normal(15)); al = rng.uniform(0, 2 * math.pi, 5)
        for i, j in P5:
            c = cross_full(v[i], v[j], mrep[i], mrep[j], al[i], al[j], sig)
            if (mrep[i] + mrep[j]) % 2: worst_odd = max(worst_odd, abs(c))
            else: typ_even.append(abs(c))
    print(f"   groesster |Kreuzterm| mit S (m_i + m_j ungerade): {worst_odd:.3e}; Median |Kreuzterm| der geraden Paare: {np.median(typ_even):.3e}; Verhaeltnis {worst_odd/np.median(typ_even):.2e}")
    v = unit(rng.standard_normal(15)); al = rng.uniform(0, 2 * math.pi, 5); dmax = 0.0
    for i, j in P4:
        a, b = cross_full(v[i], v[j], mrep[i], mrep[j], al[i], al[j], sig), cross_even(v[i], v[j], mrep[i], mrep[j], al[i], al[j], sig); dmax = max(dmax, abs(a - b))
    print(f"   Kontrolle der Fensterintegration (gerade Paare) gegen die volle: groesste Abweichung {dmax:.2e}")

    out = {}
    for amp, alab in ((np.ones(4), "A_i = 1 (H210c, Test)"), (mrep[:4].astype(float), "A_i = m_i (H210d, Bericht)")):
        for sdeg in (2.0, 5.0):
            sig = math.radians(sdeg)
            with Pool(4) as pool: res = pool.map(run_start, [(1000 + k, sig, amp) for k in range(240)])
            res.sort(key=lambda r: r[0]); f0, z = res[0]; M = angles(unit(z[:12])); out[(alab, sdeg)] = M
            nb = sum(1 for r in res if r[0] < f0 + 1e-4 * abs(f0))
            print(f"\n== Welle, {alab}, sigma = {sdeg} Grad ==\n   Energie {f0:.6e}; {nb} von 240 Starts im besten Minimum; Energien der fuenf besten: " + ", ".join(f"{r[0]:.4e}" for r in res[:5]))
            print("   " + "  ".join(f"{names[i]}{names[j]} {M[i,j]:.2f}" for i, j in P4))
            for r in res[1:4]:
                Mk = angles(unit(r[1][:12])); print("      naechstes: " + "  ".join(f"{names[i]}{names[j]} {Mk[i,j]:.2f}" for i, j in P4) + f"  (E = {r[0]:.4e})")
            sys.stdout.flush()
    A = "A_i = 1 (H210c, Test)"; M2, M5 = out[(A, 2.0)], out[(A, 5.0)]
    d = max(abs(M2[i, j] - M5[i, j]) for i, j in P4); tm = math.degrees(math.acos(1/3))
    allc = all(abs(M[i, j] - tm) <= 1 for M in (M2, M5) for i, j in P4); coll = any(M[i, j] < 5 for M in (M2, M5) for i, j in P4)
    verd = "bestaetigt" if allc else ("teilweise" if (d < 3 and not coll) else "widerlegt")
    print(f"\n   H210c: groesste Aenderung eines Winkels zwischen sigma = 2 und 5 Grad: {d:.2f}; alle bei 70.53 +- 1: {'ja' if allc else 'nein'}; zusammenfallende Baender: {'ja' if coll else 'nein'}")
    print(f"   H210c: {verd}")
    for key, M in out.items():
        hits = [(names[i] + "-" + names[j], round(float(M[i, j]), 2)) for i, j in P4 if min(abs(M[i, j] - t) for t in targets) <= 1]
        print(f"   H210d Treffer auf der Zielliste (nachtraeglich) {key}: {hits}")
