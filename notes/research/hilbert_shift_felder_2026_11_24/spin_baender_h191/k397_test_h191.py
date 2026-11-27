"""k397: Test H191 auf der Maschine (Baustufe 2). Aufruf aus dem Repo-Wurzelverzeichnis:
   python notes/research/hilbert_shift_felder_2026_11_24/spin_baender_h191/k397_test_h191.py > .../k397_out.txt"""
import math, os, sys, time, numpy as np
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.abspath(os.path.join(here, "..", "..", "..", "..")))
from qam.examples.coprocessor.stufe2.qtape import QTape

def band(alpha, mu, lam, n):
    return f"""QTAPE 2
KMAX 60
BUDGET {6 * n + 50}
ALLOW INIT ROT HC ADD DROP LOOP END HALT
INIT 1 1
LOOP {n}
  ROT {alpha!r}
  HC
  ADD {mu}
  DROP {lam}
END
HALT"""
def station(alpha, mu, lam, n0=400):
    n = n0; prev = None
    while True:
        m = QTape(band(alpha, mu, lam, n), trace_every=0).run(); res = m.result()
        assert res["stopgrund"] == "halted", res["stopgrund"]
        p = np.array([res["baender"].get(k, 0.0) for k in range(61)])
        if prev is not None and np.abs(p - prev).max() < 1e-12: return p, n, m
        prev = p; n *= 2
        if n > 30000: return p, -n, m
def profile(p):
    live = [k for k in range(1, 60) if p[k] > 1e-13]
    if len(live) < 10: return None, None, live                         # kein Schwanz: Verteilung endet nach wenigen Baendern
    with np.errstate(divide="ignore", invalid="ignore"): d = np.log(p[1:-1] / p[2:])       # d[i] gehoert zu k = i + 1
    ks = [k for k in range(12, 17) if p[k + 1] > 1e-13]
    if len(ks) < 5: top = max(k for k in range(1, 59) if p[k + 1] > 1e-13); ks = list(range(top - 4, top + 1))
    dinf = np.mean([d[k - 1] for k in ks]); return d, dinf, ks
cas = np.array([math.sqrt(3) * (math.sqrt((k + 1) * (k + 3) / 3) - math.sqrt(k * (k + 2) / 3)) for k in range(1, 9)])
print("Zielprofile r_k (k = 1..8): Casimir", np.round(cas, 4), "; glatt: alle 1")

print("\n== H191a (nicht blind): alpha = 0 ==")
oka = True
for mu, lam in [(0.25, 0.5), (0.5, 1.0), (0.2, 0.6), (0.4, 0.6)]:
    p, n, _ = station(0.0, mu, lam); d, dinf, ks = profile(p)
    if d is None: print(f"   mu = {mu}, lam = {lam}: Runden {n}, kein Schwanz: nur die Baender 0..{max(ks, default=0)} sind besetzt (p_0 = {p[0]:.6f}, p_1 = {p[1]:.6f}); Gitterpunkt entartet, zaehlt nicht"); continue
    r = d[:8] / dinf; oka &= np.abs(r - 1).max() < 1e-6
    print(f"   mu = {mu}, lam = {lam}: Runden {n}, p_0 = {p[0]:.6f}, p_1 = {p[1]:.6f}, p_(k+1)/p_k = {math.exp(-dinf):.8f}, groesste Abweichung |r_k - 1| = {np.abs(r - 1).max():.1e}")
print("   H191a:", "bestaetigt (nicht blind)" if oka else "NICHT bestaetigt")

print("\n== H191b, H191c: Gitter ==")
hitb = hitc = nd = 0; rows = []; t0 = time.time()
for alpha, an in [(math.pi / 6, "pi/6"), (math.pi / 4, "pi/4"), (math.pi / 3, "pi/3")]:
    for mu, lam in [(0.25, 0.5), (0.5, 1.0), (0.2, 0.6), (0.4, 0.6)]:
        p, n, m = station(alpha, mu, lam); d, dinf, ks = profile(p)
        if d is None: print(f"   alpha = {an}, mu = {mu}, lam = {lam}: Runden {n}, kein Schwanz: nur die Baender 0..{max(ks, default=0)} besetzt (p_0 = {p[0]:.5f}, p_1 = {p[1]:.5f}); entartet, kann kein Fenster erfuellen"); nd += 1; continue
        r = d[:8] / dinf
        db, dc = np.abs(r[:4] - cas[:4]).max(), np.abs(r[:4] - 1).max(); hitb += db <= 0.015; hitc += dc <= 0.015; rows.append((an, mu, lam, r, dinf))
        print(f"   alpha = {an}, mu = {mu}, lam = {lam}: Runden {n}, p_0 = {p[0]:.5f}, p_1 = {p[1]:.5f}, d_inf = {dinf:.6f} (Baender {ks[0]}..{ks[-1]}), Streuung dort {np.ptp([d[k-1] for k in ks]):.1e}")
        print(f"      r_1..r_8 = {np.round(r, 4)};  Abstand zu Casimir {db:.4f}, zu glatt {dc:.4f}; mittlere Polarisation b = {m.pol():.5f}", flush=True)
print(f"   Laufzeit {time.time() - t0:.0f} s")
verd = lambda h: "bestaetigt" if h == 12 else ("teilweise" if h > 0 else "widerlegt")
print(f"\n   entartete Gitterpunkte (lam = 1, kein Schwanz): {nd} von 12; sie koennen kein Fenster erfuellen (Fehler im vorab gesetzten Gitter, offen benannt)")
print(f"   H191b (Casimir-Profil): {hitb} von 12 Gitterpunkten im Fenster -> {verd(hitb)}")
print(f"   H191c (glattes Profil): {hitc} von 12 Gitterpunkten im Fenster -> {verd(hitc)}")
R = np.array([r for *_, r, _ in rows]); print("   H191d: Spannweite von r_1 ueber das Gitter:", f"{R[:, 0].min():.4f} bis {R[:, 0].max():.4f}; von d_inf: {min(x[4] for x in rows):.4f} bis {max(x[4] for x in rows):.4f}")
print("   Abfall der Abweichung: (r_k - 1) * k und (r_k - 1) * k^2 fuer den ersten Gitterpunkt:", np.round((R[0] - 1) * np.arange(1, 9), 4), np.round((R[0] - 1) * np.arange(1, 9) ** 2, 4))

print("\n== Protokoll eines kurzen Laufs (alpha = pi/6, mu = 0.25, lam = 0.5, 3 Runden) ==")
m = QTape(band(math.pi / 6, 0.25, 0.5, 3)).run(); m.write_trace(os.path.join(here, "k397_protokoll_3_runden.jsonl"))
for row in m.trace[4:]: print(f"   {row['schritt']:3d} | {row['zelle']:28s} | {row['getan']} | weil: {row['warum']} | Baender {row['baender']}")
