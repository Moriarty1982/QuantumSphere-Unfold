"""k237: OP1, T-Regel. Fuer welche Einheit gamma_0 gibt die Dimensionsleiter (Moran-Lesart) T, M, P auf d = 1, 2, 3?

Regel R passt in R^d genau dann, wenn sum g exp(-2 pi gamma_0 a(j) d) <= 1, also gamma_R <= d * gamma_0 (Summe faellt im Exponenten).
Reichste passende Regel = groesstes gamma_R <= d * gamma_0. gamma-Werte der neun Regeln aus k218 (v4_10_0_r09/llm/k218_out.txt).
"""
import math
G = {"A,g=2 (M)": 0.237532957966, "A,g=2j+1 (P)": 0.274066858233, "H,g=2": 0.189138418126, "H,g=2j+1": 0.222865260235,
     "I,g=2": 0.137726864676, "I,g=2j+1": 0.190205620344, "S1/2,g=2 (T)": 0.127384023141, "S1,g=2": 0.0780064645196,
     "S1,g=2j+1": 0.123637321077}
gT, gM = G["S1/2,g=2 (T)"], G["A,g=2 (M)"]


def ladder(g0):
    return [max((v, k) for k, v in G.items() if v <= d * g0 + 1e-15)[1] if any(v <= d * g0 + 1e-15 for v in G.values()) else "-" for d in (1, 2, 3)]


# Fenster abtasten
grid = [0.05 + i * 1e-6 for i in range(200001)]
ok = [g for g in grid if ladder(g) == ["S1/2,g=2 (T)", "A,g=2 (M)", "A,g=2j+1 (P)"]]
lo, hi = min(ok), max(ok)
print(f"Leiter (T, M, P) fuer gamma_0 in [{lo:.6f}; {hi:.6f}], also [{lo/gT:.4f}; {hi/gT:.4f}] * gamma_T")
for name, g0 in (("gamma_T (T-Quant als Einheit, Moran-Notiz)", gT), ("gamma_M/2 (M fuellt die Ebene, D_M = 2)", gM / 2),
                 ("gamma_P/3 (P fuellt den Raum)", G["A,g=2j+1 (P)"] / 3), ("1/(2 pi)", 1 / (2 * math.pi))):
    print(f"  Einheit {name:44s} gamma_0 = {g0:.6f}: d=1,2,3 -> {ladder(g0)}")
