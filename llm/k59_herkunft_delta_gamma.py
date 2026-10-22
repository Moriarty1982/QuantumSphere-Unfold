"""k59: Herkunft der Schranke Delta_gamma < 1/5 (r65 verloren) - Hypothese: Photon-Frame-Uhrgewinn am Hopf-Punkt.

r14 nennt G die Verstaerkung der Photon-Frame-Uhr ("photon-frame timing-assisted relay charts").
Bindende Karte V3 (r12): N = 5, kappa = 1/4, G = 2; Uhrsaat (N, kappa, G) = (5, 3/4, 1).
Pruefung: sind diese Zahlen Werte des Dublettzustands (r17) am Hopf-Punkt beta = 1/sqrt3, und was ergibt die Schranke
beim gemessenen Abstand?
"""
from fractions import Fraction as F
import math

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta = 0.5 * math.acosh(gL)
D = math.exp(eta)

def state(b2):
    """Dublettzustand bei beta^2: gamma = cosh 2 eta = (1+b2)/(1-b2), p+ = 1/(1+b2), p- = b2/(1+b2)."""
    return (1 + b2) / (1 - b2), 1 / (1 + b2), b2 / (1 + b2)

print("1. V3 und Uhrsaat als Hopf-Daten (beta^2 = 1/3, exakt)")
b2 = F(1, 3)
g, pp, pm = state(b2)
print("   gamma_L = %s (V3: G = 2), p- = %s (V3: kappa = 1/4), p+ = %s (Uhrsaat: kappa = 3/4)" % (g, pm, pp))
Nbal = 1 + 1 / pm
print("   balancierte Karte kappa (N-1) = 1: N = 1 + 1/p- = 2 + 1/beta^2 = %s (V3: N = 5)" % Nbal)
S = Nbal + pm * Nbal * (Nbal - 1)
print("   S = %s, Schranke 1 - 16/(G S) = %s" % (S, 1 - F(16) / (g * S)))
print("   Kollarzeile r05: Verhaeltnis 5/6 = 1/(1 + 1/5); C5-Faktor 3/4 = p+ (r17)")

print("\n2. Gegenprobe: Haeufigkeit von G = 2 und kappa = 1/4 in der r14-Familie")
charts = {"V0": (4, F(0), F(1)), "V1": (16, F(0), F(1)), "V2": (7, F(1, 4), F(1)), "V3": (5, F(1, 4), F(2)),
          "V4": (6, F(1, 2), F(1)), "V5": (4, F(1, 2), F(5, 2)), "V6": (3, F(3, 4), F(3, 2)), "V7": (4, F(1), F(1)),
          "V8": (3, F(1), F(2)), "V9": (2, F(1, 2), F(3))}
for n, (N, k, G) in charts.items():
    S = N + k * N * (N - 1)
    tag = "Fenster" if S < 16 <= G * S else ("direkt" if S >= 16 else "blockiert")
    extra = "  Schranke %s" % (1 - F(16) / (G * S)) if tag == "Fenster" else ""
    print("   %s N = %2d kappa = %-4s G = %-4s S = %-5s %s%s" % (n, N, k, G, S, tag, extra))
print("   Nur V3 vereinigt G = gamma_L(Hopf), kappa = p-(Hopf) und kappa (N-1) = 1; die Werte liegen aber auf einem Viertel-/Halbgitter")

print("\n3. Schranke von V3 beim gemessenen Abstand (16 und die Kartenform fest)")
b2m = math.tanh(eta) ** 2
gm, ppm, pmm = state(b2m)
rows = [("Hopf (Quelle)", 2.0, 0.25, 5),
        ("G = gamma_L, kappa, N fest", gL, 0.25, 5),
        ("G = e^eta (Uhr = Skala, r19), kappa, N fest", D, 0.25, 5),
        ("G = gamma_L, kappa = p-(gemessen), N = 5", gL, pmm, 5),
        ("G = e^eta, kappa = p-(gemessen), N = 5", D, pmm, 5),
        ("G = gamma_L, balanciert N = 1 + 1/p-", gL, pmm, 1 + 1 / pmm)]
for name, G, k, N in rows:
    S = N + k * N * (N - 1)
    d = 1 - 16 / (G * S)
    print("   %-46s G = %.4f kappa = %.4f N = %.3f S = %.3f  Schranke %.4f  tan alpha < %.4f (%.1f Grad)"
          % (name, G, k, N, S, d, math.sqrt(d / (1 - d)), math.degrees(math.atan(math.sqrt(d / (1 - d))))))

print("\n4. Folgen fuer r12.2 (Kollarzeile exportiert 1/6 = %.4f, C5-Stufe 1/4)" % (1 / 6))
for name, d in (("Hopf", 0.2), ("gemessen, G = gamma_L", 1 - 16 / (gL * 10)), ("gemessen, G = e^eta", 1 - 16 / (D * 10))):
    print("   %-24s Schranke %.4f: Kollarzeile %s, C5-Stufe %s" % (name, d, "innen" if 1 / 6 < d else "aussen", "innen" if 0.25 < d else "aussen"))

print("\n5. Alternative Verallgemeinerung tan alpha < 1/gamma_L (= 1/2 am Hopf-Punkt): sin^2 = 1/(1+gamma^2)")
print("   Hopf %.4f, gemessen %.4f (r90-Kohaerenzwert 2/9 = %.4f)" % (1 / 5, 1 / (1 + gL ** 2), 2 / 9))
