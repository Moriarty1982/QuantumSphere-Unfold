"""k447 (Test H233): Rasten die feinen Winkel auf 8 Stellungen (pi/4) mit Bit-Verfeinerung ein? (F18)
Vorab-Notiz Vorab_H233_Einrastung_acht_Stellungen.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k447_test_h233.py > k447_out.txt
"""
import math

X, SX = math.pi / 12 - 0.2222220470731, 7.8e-7
BETA, SB = 0.549405640974529, 0.00018
GL = 1.864699764609373


def th(s2, e):
    t = math.asin(math.sqrt(s2))
    dt = e / (2 * math.sqrt(s2 * (1 - s2)))  # d theta / d s2
    return t, dt


Q = {
    "phi = x": (X, SX),
    "x_nu": (0.04336, 0.00213),
    "theta12": th(0.3036, 0.0064),
    "theta13": th(0.02248, 0.00056),
    "theta23": th(0.470, 0.015),
    "delta_CP": (math.radians(212), math.radians(34)),
    "arctan beta": (math.atan(BETA), SB / (1 + BETA ** 2)),
    "arcsin beta": (math.asin(BETA), SB / math.sqrt(1 - BETA ** 2)),
}
GRIDS = {"A (pi/4)": math.pi / 4, "B (pi/12)": math.pi / 12}

print("=" * 96)
print("H233 (k447)  Einrastung auf 8 Stellungen mit Bit-Verfeinerung, k = 0..8")
print("=" * 96)
print("\nTeil A (nicht blind)  Kontrolle: Baumwerte")
for nm, v in (("pi/12", math.pi / 12), ("pi/6", math.pi / 6), ("pi/4", math.pi / 4)):
    for g, s in GRIDS.items():
        n = v / s
        print(f"  {nm:5s} auf Gitter {g}: Vielfaches {n:.12f} (k = 0)")

print("\nTeil B (blind)  je Groesse, Gitter, k: Rest zum naechsten Gitterpunkt; zulaessig nur bei Delta >= 10 sigma")
lam_all = 0.0
hits_all = []
lam_phi = 0.0
hits_phi = 0
for nm, (v, s) in Q.items():
    print(f"\n  {nm}: Wert {v:.10f}, sigma {s:.3e}")
    for g, base in GRIDS.items():
        for k in range(9):
            d = base / 2 ** k
            m = round(v / d)
            r = v - m * d
            ok = d >= 10 * s
            hit = ok and abs(r) <= 2 * s
            p = 4 * s / d if ok else None
            if ok:
                lam_all += p
                if nm == "phi = x":
                    lam_phi += p
            if hit:
                hits_all.append((nm, g, k, m, r / s))
                if nm == "phi = x":
                    hits_phi += 1
            if ok:
                print(f"    {g:9s} k={k}: Abstand {d:.6f}, naechster Punkt {m:4d}*Delta, Rest {r:+.3e} = {r/s:+10.2f} sigma"
                      f"{'  TREFFER' if hit else ''}")
        n_bad = sum(1 for k in range(9) if base / 2 ** k < 10 * s)
        if n_bad:
            print(f"    {g:9s}: {n_bad} feinste Stufen unzulaessig (Delta < 10 sigma)")


def pois_ge(n, lam):
    return 1 - sum(math.exp(-lam) * lam ** j / math.factorial(j) for j in range(n)) if n else 1.0


print(f"\n  Treffer gesamt: {len(hits_all)} {hits_all}")
print(f"  Zufallserwartung gesamt lambda = {lam_all:.4f}, P(>= {len(hits_all)}) = {pois_ge(len(hits_all), lam_all):.3g}")
print(f"  phi: Treffer {hits_phi}, lambda_phi = {lam_phi:.3e}, P = {pois_ge(hits_phi, lam_phi):.3g}")
oth = [h for h in hits_all if h[0] != "phi = x"]
lam_oth = lam_all - lam_phi
p_oth = pois_ge(len(oth), lam_oth)
print(f"  uebrige Groessen: Treffer {len(oth)}, lambda = {lam_oth:.4f}, P = {p_oth:.3g}")

print("\nTeil C (blind)  phi als Rastfehler: Rest eines natuerlichen Winkels nach Einrasten")
E0 = math.atanh(BETA)
CAND = {"arctan beta": math.atan(BETA), "arcsin beta": math.asin(BETA), "arccos beta": math.acos(BETA), "eps0": E0,
        "2 eps0": 2 * E0, "1/gamma_L": 1 / GL, "beta (rad)": BETA}
rows = []
for nm, a in CAND.items():
    for sn, s in (("pi/4", math.pi / 4), ("pi/12", math.pi / 12)):
        r = a % s
        for lab, val in (("r", r), ("s-r", s - r)):
            rows.append((abs(val - X), nm, sn, lab, val))
rows.sort()
hitC = any(rw[0] <= 2 * SX for rw in rows)
loose = [rw for rw in rows if rw[0] <= 0.01 * X]
for rw in rows[:8]:
    print(f"  {rw[1]:12s} mod {rw[2]:5s} ({rw[3]:3s}): {rw[4]:.8f}  Abstand {rw[4]-X:+.3e} = {(rw[4]-X)/SX:+12.1f} sigma ({(rw[4]-X)/X*100:+.2f} %)")
# Zufall: Reste gleichverteilt auf [0, s/2] je Paar (r, s-r zusammen = Abstand zum naechsten Raster); Wahrscheinlichkeit fuer 1 %-Fenster
lamC = sum(2 * 0.02 * X / s for s in (math.pi / 4, math.pi / 12)) * len(CAND)
pC = pois_ge(len(loose), lamC)
print(f"  Treffer 2 sigma: {hitC}; locker (1 %): {len(loose)}; Zufallserwartung lambda = {lamC:.3f}, P(>= {len(loose)}) = {pC:.3g}")

print("\n" + "=" * 96)
trg = (hits_phi > 0 and pois_ge(hits_phi, lam_phi) < 0.05) or hitC
part = (len(oth) > 0 and p_oth < 0.05) or (len(loose) > 0 and pC < 0.05)
v = "TRAEGT" if trg else ("TRAEGT TEILWEISE" if part else "WIDERLEGT")
print(f"H233 Gesamturteil: {v}")
