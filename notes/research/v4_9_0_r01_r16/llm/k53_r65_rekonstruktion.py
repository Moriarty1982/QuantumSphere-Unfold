"""k53: Rekonstruktion der Schranke Delta_gamma < 1/5 (r65 fehlt) aus Daten der Quelle (r14, r15, r23) und r11.

Praemissen: P1 Chart-Daten r14; P2 Ueberleben = strikte Relaisbedingung G (1 - Delta) S > 16 (r23 strikt);
P3 Delta = multiplikativer Verlust je Auslese (r11: Export sin^2 der Dualitaetsdrift); P4 Kette R_A = {V3, V5} (r15/r92).
"""
import math
from fractions import Fraction as Fr

charts = {  # V: (N, kappa, G) aus r14
    "V0": (4, Fr(0), Fr(1)), "V1": (16, Fr(0), Fr(1)), "V2": (7, Fr(1, 4), Fr(1)), "V3": (5, Fr(1, 4), Fr(2)),
    "V4": (6, Fr(1, 2), Fr(1)), "V5": (4, Fr(1, 2), Fr(5, 2)), "V6": (3, Fr(3, 4), Fr(3, 2)), "V7": (4, Fr(1), Fr(1)),
    "V8": (3, Fr(1), Fr(2)), "V9": (2, Fr(1, 2), Fr(3)),
}
S = lambda N, k: N + k * N * (N - 1)
print("1. Zulaessiger relativer Verlust je Chart: Delta_max = 1 - 16/(G S)  (strikt: Delta < Delta_max)")
for v, (N, k, G) in charts.items():
    H = G * S(N, k)
    print("   %s: N=%2d kappa=%-4s G=%-4s S=%-6s H=%-6s Delta_max=%s%s" %
          (v, N, k, G, S(N, k), H, (1 - Fr(16) / H) if H > 16 else "-",
           "   <- ausgeglichen: kappa(N-1) = 1" if k * (N - 1) == 1 else ""))
RA = [1 - Fr(16) / (charts[v][2] * S(*charts[v][:2])) for v in ("V3", "V5")]
print("   Minimum ueber R_A = {V3, V5}: %s" % min(RA))
print("   Grenzfall Delta = 1/5 an V3: H(1 - Delta) = %s = 16 -> strikte Bedingung verletzt -> Delta < 1/5" %
      (charts["V3"][2] * S(5, Fr(1, 4)) * (1 - Fr(1, 5))))

print("\n2. Folge unter r11: Verlust je Auslese = sin^2(alpha) der Dualitaetsdrift")
amax = math.asin(math.sqrt(0.2))
print("   sin^2 alpha < 1/5  <=>  tan alpha < 1/2  <=>  alpha < %.3f Grad" % math.degrees(amax))
for name, export in (("C5-Stufe (strikte Zeile, 3/4)", Fr(1, 4)), ("Toleranzzeile r05 (5/6)", Fr(1, 6)),
                     ("Uhrensaat-Kopplung als Export (kappa = 3/4)", Fr(3, 4))):
    print("   %-45s Export %-5s -> %s" % (name, export, "innerhalb" if export < Fr(1, 5) else "ausserhalb"))

print("\n3. r05-Zeilen mit Phi = 0 (mix-cancel, all-cancel): Delta = -3/4 wandert nach A_4 bzw. U_6 (blockiert C4/C6)")
print("   = Vierteldrehung von r10.2: C-Port leer, Inhalt in einem anderen Slot")
