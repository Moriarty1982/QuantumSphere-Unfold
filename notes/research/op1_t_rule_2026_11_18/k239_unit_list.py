"""k239: Einheitenliste (Einheitenliste.md, Commit c64caff) gegen das Fenster der Dimensionsleiter [gamma_T; gamma_P/2)."""
import math
G = {"A,g=2 (M)": 0.237532957966, "A,g=2j+1 (P)": 0.274066858233, "H,g=2": 0.189138418126, "H,g=2j+1": 0.222865260235,
     "I,g=2": 0.137726864676, "I,g=2j+1": 0.190205620344, "S1,g=2": 0.0780064645196, "S1,g=2j+1": 0.123637321077}
gT = 0.127384023141
LO, HI = gT, G["A,g=2j+1 (P)"] / 2
C = {"1": 1.0, "1/2": 0.5, "ln2": math.log(2), "ln3": math.log(3), "2ln2": 2 * math.log(2), "pi": math.pi}
A = {"sqrt3/2": math.sqrt(3) / 2, "sqrt2": math.sqrt(2), "1/2": 0.5, "1": 1.0}
units = []
for cn, c in C.items():
    for an, a in A.items():
        if cn == "ln2" and an == "sqrt3/2":
            continue
        units.append((f"L1 {cn}/(2 pi {an})", c / (2 * math.pi * a)))
for rn, g in G.items():
    for d in (1, 2, 3):
        units.append((f"L2 gamma[{rn}]/{d}", g / d))
assert len(units) == 47
hits = [(n, u) for n, u in units if LO <= u < HI]
vals = [u for _, u in units]
span = math.log(max(vals) / min(vals)); frac = math.log(HI / LO) / span
print(f"Fenster [{LO:.6f}; {HI:.6f}), 47 Einheiten von {min(vals):.4f} bis {max(vals):.4f}")
print(f"Zufallserwartung: Fensteranteil {frac:.4f} der log-Spannweite, erwartet {47 * frac:.2f} Treffer")
print(f"Treffer: {len(hits)}")
for n, u in hits:
    print(f"  {n}: {u:.6f} = {u / gT:.4f} gamma_T")
near = sorted(units, key=lambda x: abs(math.log(x[1] / math.sqrt(LO * HI))))[:5]
print("Naechste Eintraege:")
for n, u in near:
    print(f"  {n:34s} {u:.6f} ({u / gT:.4f} gamma_T){'  TREFFER' if LO <= u < HI else ''}")
