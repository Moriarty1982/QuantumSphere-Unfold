"""k394 (Erkundung, nicht blind, alles angepasst): Uebersicht, welche Eingabe welche Ausgabe bewegt und welche Einstellungen
einzelne Ausgaben oder Paare von Ausgaben treffen. Mechanismen aus H184 bis H190. Kein Test, keine Vorhersage.
Aufruf: python k394_uebersicht.py > k394_out.txt"""
import itertools
import numpy as np
from scipy.optimize import minimize_scalar
l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)]); prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
Rdef = [("l_k", lambda i, j, k: k), ("l_k^2", lambda i, j, k: k * k), ("l_i l_j", lambda i, j, k: i * j), ("l_i l_j - l_k^2/2", lambda i, j, k: i * j - k * k / 2),
        ("1", lambda i, j, k: 1.0), ("l_i + l_j", lambda i, j, k: i + j), ("l_i^2 + l_j^2", lambda i, j, k: i * i + j * j),
        ("(l_i^2 + l_j^2)/2 + l_i l_j", lambda i, j, k: (i * i + j * j) / 2 + i * j), ("l_k (l_i + l_j)", lambda i, j, k: k * (i + j))]
FR = np.array([[f(l[i], l[j], l[k]) for (i, j, k) in prs] for _, f in Rdef]); fn_ = lambda n: f"f{n + 1}"
G2 = np.array([2 * (l[i] - l[j])**2 for (i, j, k) in prs]); G4 = np.array([-2 * (l[i]**2 + l[j]**2) - 4 * l[k]**2 for (i, j, k) in prs])
mass = {"e": (np.array([0.51099895, 105.6583755, 1776.86]), np.array([1.5e-10, 2.3e-6, 0.12])),
        "d": (np.array([1.54e-5, 3.06e-4, 1.630e-2]), np.array([0.02e-5, 0.04e-4, 0.009e-2])), "u": (np.array([7.04e-6, 3.56e-3, 0.967]), np.array([0.15e-6, 0.06e-3, 0.004]))}
print("Erkundung k394: alles in dieser Ausgabe ist ANGEPASST oder eine Empfindlichkeit, keine Vorhersage.")
print(f"Vakuum (Eingabe): a = 1, r = 1/sqrt(2) (K = 2/3), delta = 2/9; Eigenwerte l = {np.round(l, 6)}")
print("Funktionen je Paar (R aus H187): " + "; ".join(f"{fn_(n)} = {nm}" for n, (nm, _) in enumerate(Rdef)))

print("\n== Teil A: drei Eingaben je Sektor treffen drei Massen exakt (Brannen-Form sqrt(m_g) = M (1 + sqrt(2) rho cos(delta + 2 pi g/3))) ==")
print("   Eingaben: M (Skala), rho (K = (1 + rho^2)/3), delta (Phase). Empfindlichkeit = d ln m_g / d Eingabe am angepassten Punkt.")
for nm in ("e", "d", "u"):
    m, s = mass[nm]; sq = np.sqrt(m); M = sq.sum() / 3; K = m.sum() / sq.sum()**2; rho = np.sqrt(3 * K - 1); c = (sq / M - 1) / (np.sqrt(2) * rho)
    best = None
    for perm in itertools.permutations(range(3)):
        for sg in (1, -1):
            d0 = sg * np.arccos(np.clip(c[perm[0]], -1, 1)); th = d0 + 2 * np.pi * np.arange(3) / 3; err = np.abs(np.cos(th) - c[list(perm)]).max()
            if best is None or err < best[0]: best = (err, d0, perm, th)
    err, d0, perm, th = best; dlt = abs(((d0 + np.pi / 3) % (2 * np.pi / 3)) - np.pi / 3); x = 1 + np.sqrt(2) * rho * np.cos(th); inv = np.argsort(perm)
    J = np.array([2 * np.ones(3), 2 * np.sqrt(2) * np.cos(th) / x, -2 * np.sqrt(2) * rho * np.sin(th) / x])[:, inv]
    print(f"   Sektor {nm}: M = {M:.6g}, rho = {rho:.5f} (K = {K:.5f}), delta = {dlt:.5f} (Rest {err:.1e})")
    print(f"      d ln(m1, m2, m3) / d ln M = {np.round(J[0], 2)};  / d rho = {np.round(J[1], 2)};  / d delta = {np.round(J[2], 2)}")
print("   Lesehilfe: M bewegt alle drei gleich; rho und delta bewegen fast nur die leichteste Masse (grosse Zahlen in der ersten Spalte).")

print("\n== Teil B: Mechanismen aus H184 bis H190 gegen die vier Quark-Verhaeltnisse ==")
T = {}
for nm in ("u", "d"):
    m, s = mass[nm]; r = m[:2] / m[2]; T[nm] = (r, r * np.sqrt((s[:2] / m[:2])**2 + (s[2] / m[2])**2))
tg = [("u", 0, "m_u/m_t"), ("u", 1, "m_c/m_t"), ("d", 0, "m_d/m_b"), ("d", 1, "m_s/m_b")]
print("   Ausgaben: " + ", ".join(f"{n} = {T[s][0][i]:.4g} +- {T[s][1][i]:.2g}" for s, i, n in tg) + "; dazu je Sektor die Skala (m_t, m_b), die immer eine eigene freie Zahl A ist.")
zu = {"A": [0, 1, 2], "B": [2, 1, 0]}; pw = {"X = sqrt(m)": 2.0, "X = m": 1.0, "X = m^2": 0.5}
def rat(X):
    """X (N, 3) -> Verhaeltnisse (N, 2), nan falls Vorzeichen gemischt oder null."""
    ok = (np.sign(X[:, 0]) == np.sign(X[:, 2])) & (np.sign(X[:, 1]) == np.sign(X[:, 2])) & (X[:, 2] != 0) & np.all(np.isfinite(X), axis=1)
    with np.errstate(all='ignore'): r = np.stack([X[:, 0] / X[:, 2], X[:, 1] / X[:, 2]], axis=1)
    r[~ok] = np.nan; return r
lg = lambda lo, hi, st: 10 ** np.arange(lo, hi, st)
sym = np.concatenate([-lg(-8, 8, 0.002)[::-1], [0.0], lg(-8, 8, 0.002)])
def dev(Rm, sec, idx):
    r, sr = T[sec]; return np.abs(Rm[..., idx] - r[idx]) / sr[idx]
def best_pair(opts, sec):
    """bester gemeinsamer Abstand beider Verhaeltnisse eines Sektors ueber alle Optionen (Raster, dann verfeinert)."""
    out = None
    for lab, fn, th in opts:
        Rm = fn(th, sec); d = np.maximum(dev(Rm, sec, 0), dev(Rm, sec, 1)); d[~np.isfinite(d)] = np.inf; k = int(np.argmin(d))
        if out is None or d[k] < out[0]: out = (d[k], lab, fn, th, k)
    d0, lab, fn, th, k = out; lo, hi = th[max(k - 1, 0)], th[min(k + 1, len(th) - 1)]
    def z(x):
        Rm = fn(np.array([x]), sec); v = max(dev(Rm, sec, 0)[0], dev(Rm, sec, 1)[0]); return v if np.isfinite(v) else 1e9
    res = minimize_scalar(z, bounds=(lo, hi), method="bounded", options={"xatol": 1e-13 * max(abs(hi), 1e-12)}); return (res.fun, lab, res.x) if res.fun < d0 else (d0, lab, th[k])
def reach(opts, sec, idx):
    """Zahl der Optionen, die das eine Verhaeltnis exakt treffen (Vorzeichenwechsel auf dem Raster)."""
    n = 0; r = T[sec][0][idx]
    for lab, fn, th in opts:
        y = fn(th, sec)[:, idx] - r; ok = np.isfinite(y[:-1]) & np.isfinite(y[1:]); n += bool(np.any(ok & (np.sign(y[:-1]) != np.sign(y[1:]))))
    return n
def report(name, knob, opts, hint):
    print(f"\n   -- {name} --\n      Stellgroesse: {knob}; Optionen (diskrete Wahlen): {len(opts)}. {hint}")
    for sec, i, n in tg: print(f"      {n} allein exakt erreichbar in {reach(opts, sec, i)} von {len(opts)} Optionen")
    for sec, nm in (("u", "Up (m_u/m_t und m_c/m_t zusammen)"), ("d", "Down (m_d/m_b und m_s/m_b zusammen)")):
        d, lab, th = best_pair(opts, sec); print(f"      {nm}: bester Abstand {d:.2f} sigma mit {lab}, Stellgroesse = {th:.6g}")
    print("      Paare ueber die Sektoren (je ein Verhaeltnis aus Up und Down): je Sektor eigene Stellgroesse, also so gut wie die Einzelwerte.", flush=True)

# M1: eine Potentialfunktion, keine Stellgroesse
print("\n   -- M1: eine Potentialfunktion (H184 bis H187), keine Stellgroesse --")
for sec, i, n in tg:
    bl = None
    for f in range(9):
        for zn, pm in zu.items():
            for ln, p in pw.items():
                Rm = rat(FR[f][pm][None, :])**p; d = dev(Rm, sec, i)[0]
                if np.isfinite(d) and (bl is None or d < bl[0]): bl = (d, f"{fn_(f)}, Zuordnung {zn}, {ln}", Rm[0, i])
    print(f"      {n}: naechste Funktion {bl[1]}: Modell {bl[2]:.4g}, Abstand {bl[0]:.1f} sigma")
for sec in ("u", "d"):
    bl = None
    for f in range(9):
        for zn, pm in zu.items():
            for ln, p in pw.items():
                Rm = rat(FR[f][pm][None, :])**p; d = max(dev(Rm, sec, 0)[0], dev(Rm, sec, 1)[0])
                if np.isfinite(d) and (bl is None or d < bl[0]): bl = (d, f"{fn_(f)}, Zuordnung {zn}, {ln}")
    print(f"      beide Verhaeltnisse {sec}: {bl[1]}, Abstand {bl[0]:.0f} sigma")

phi = np.linspace(0, np.pi, 40001)
o2 = [(f"({fn_(f)}, {fn_(g)}), Zuordnung {zn}, {ln}; Stellgroesse phi mit X = cos(phi) {fn_(f)} + sin(phi) {fn_(g)}",
       (lambda th, sec, f=f, g=g, pm=pm, p=p: rat(np.cos(th)[:, None] * FR[f][pm] + np.sin(th)[:, None] * FR[g][pm])**p), phi)
      for f, g in itertools.combinations(range(9), 2) for zn, pm in zu.items() for ln, p in pw.items()]
report("M2: zwei Potentialfunktionen (H187c)", "Mischung b/a = tan(phi), je Sektor", o2, "Eine Zahl je Sektor fuer zwei Verhaeltnisse.")
o3 = [(f"({fn_(f)}, {fn_(g)})/{fn_(z)}, Zuordnung {zn}, {ln}; phi",
       (lambda th, sec, f=f, g=g, z=z, pm=pm, p=p: rat((np.cos(th)[:, None] * FR[f][pm] + np.sin(th)[:, None] * FR[g][pm]) / FR[z][pm])**p), phi[::4])
      for z in range(9) if z != 4 for f, g in itertools.combinations(range(9), 2) for zn, pm in zu.items() for ln, p in pw.items()]
report("M3: zwei Potentialfunktionen ueber einer kinetischen (H188c)", "Mischung b/a = tan(phi), je Sektor", o3, "Wie M2, mit Nenner aus R.")
def gyro(th, f, s, g, p):
    h = s * FR[f]; o = [x for x in range(3) if x != g]; ha, hb = h[o[0]], h[o[1]]; sm = (ha + hb) / 2 + th; dsc = (ha - hb)**2 / 4 + 2 * th * (ha + hb)
    with np.errstate(all='ignore'): sq = np.sqrt(dsc); X = np.sort(np.stack([np.full_like(th, h[g]), sm - sq, sm + sq], axis=1), axis=1)
    X[(dsc < 0) | (X[:, 0] <= 0)] = np.nan; return rat(X)**p
def wgrid(f, s, g):
    h = s * FR[f]; o = [x for x in range(3) if x != g]; ws = [np.array([0.0]), np.abs(h).max() * lg(-8, 8, 0.002)]
    for t in (h[o[0]], h[o[1]]):
        if t > 0: u = lg(-10, 0, 0.004); ws += [t * (1 - u), t * (1 + u)]
    return np.unique(np.concatenate(ws))
o5 = [(f"{'+' if s > 0 else '-'}{fn_(f)}, Ebene {prs[g][:2]}, {ln}; w = omega^2/A", (lambda th, sec, f=f, s=s, g=g, p=p: gyro(th, f, s, g, p)), wgrid(f, s, g))
      for f in range(9) for s in (1, -1) for g in range(3) for ln, p in pw.items()]
report("M5: Drehung in den Generationen (H190)", "w = omega^2/A, je Sektor", o5, "Die Drehung macht eine Frequenz klein; Zuordnung nach Groesse.")

def shared(name, knob, opts, hint):
    print(f"\n   -- {name} --\n      Stellgroesse: {knob} (fuer beide Sektoren dieselbe); Optionen: {len(opts)}. {hint}")
    sets = [((a,), tg[a][2]) for a in range(4)] + [((a, b), tg[a][2] + " und " + tg[b][2]) for a, b in itertools.combinations(range(4), 2)] + [((0, 1, 2, 3), "alle vier")]
    for idxs, nm in sets:
        bl = None
        for lab, fn, th in opts:
            Ru, Rd = fn(th); d = np.zeros(len(th))
            for a in idxs:
                sec, i, _ = tg[a]; d = np.maximum(d, dev(Ru if sec == "u" else Rd, sec, i))
            d[~np.isfinite(d)] = np.inf; k = int(np.argmin(d))
            if bl is None or d[k] < bl[0]: bl = (d[k], lab, th[k])
        print(f"      {nm}: bester Abstand {bl[0]:.2f} sigma mit {bl[1]}, Stellgroesse = {bl[2]:.6g}")
    print("", end="", flush=True)
def m4(th, fu, fd, pm, gv, tf):
    h = (gv - gv[pm[2]])[pm]; D = 1 + th[:, None] * h; D[np.any(D <= 0, axis=1)] = np.nan; return rat(tf(FR[fu][pm]) / D), rat(tf(FR[fd][pm]) / D)
pos = [n for n in range(9) if FR[n].min() > 0]
o4 = [(f"Up {fn_(fu)}, Down {fn_(fd)}, Zuordnung {zn}, {gn}, {tn}", (lambda th, fu=fu, fd=fd, pm=pm, gv=gv, tf=tf: m4(th, fu, fd, pm, gv, tf)), sym)
      for fu in pos for fd in pos for zn, pm in zu.items() for gn, gv in (("K2: 2(l_i - l_j)^2", G2), ("K4: -2(l_i^2 + l_j^2) - 4 l_k^2", G4)) for tn, tf in (("m = A sqrt(f)/c^2", np.sqrt), ("m = A f/c^2", lambda x: x))]
shared("M4: Ausbreitung aus K2 oder K4 bei drehendem Vakuum (H189)", "a mit c^2_g = 1 + a (g_g - g_3), entspricht kappa", o4, "Je Sektor eine Potentialfunktion, eine gemeinsame Kopplung.")
def m6(th, f, g, pm, p): return rat(FR[f][pm] + th[:, None] * FR[g][pm])**p, rat(FR[f][pm] - th[:, None] * FR[g][pm])**p
o6 = [(f"X = {fn_(f)} +- c {fn_(g)} (Up +, Down -), Zuordnung {zn}, {ln}", (lambda th, f=f, g=g, pm=pm, p=p: m6(th, f, g, pm, p)), sym)
      for f in range(9) for g in range(9) if f != g for zn, pm in zu.items() for ln, p in pw.items()]
shared("M6: gemeinsamer Term plus Ladungsterm (H182, H186)", "c (Staerke des ladungsungeraden Terms)", o6, "Dieselben zwei Funktionen fuer Up und Down, nur das Vorzeichen von c wechselt.")
