"""k37: Inventar der Frame-Umrechnungen mit gamma_L im Companion (Strukturrechnung, kein Datenvergleich).

Sucht im Hauptkorpus (vor r94) alle Zeilen mit einer Potenz von \\gL bzw. einem Faktor \\gL
zusammen mit einem Frame-Bezug, und ordnet sie der beschriftenden Umgebung zu.
"""
import re, os, collections
here = os.path.dirname(os.path.abspath(__file__))
src = next(p for p in (os.path.join(here, "..", n) for n in
           ("Quantum_Sphaera_Companion_v4_8_0_source.tex",
            "Quantum_Sphaera_Companion_v4_8_0_r20_working_source.tex")) if os.path.exists(p))
L = open(src, encoding="utf-8").read().split("\n")
END = next(i for i, l in enumerate(L) if "v4.7.0-r94 Source-Only" in l)

pow_pat = re.compile(r"\\gL\^\{?(-?[0-9./]+|k\(X\)|-k\(X\)|k|-k|[0-9]+/[0-9]+)\}?|\\gL\^\{(-?k\([^}]*\)[^}]*)\}")
frame_pat = re.compile(r"photon|matter|frame|tachyon", re.I)

def env(n):
    for j in range(n, max(0, n-120), -1):
        m = re.search(r"\\label\{([^}]+)\}", L[j])
        if m:
            return m.group(1)
    return "?"

hits = []
for i in range(END):
    l = L[i]
    if "\\gL" not in l:
        continue
    ctx = " ".join(L[max(0, i-2):i+3])
    if pow_pat.search(l) or ("\\gL" in l and frame_pat.search(ctx) and re.search(r"(photon|matter)\)\}", ctx)):
        hits.append((i+1, env(i), l.strip()[:110]))

by_env = collections.OrderedDict()
for n, e, t in hits:
    by_env.setdefault(e, []).append((n, t))
print("Zeilen mit gamma_L-Potenz oder Frame-Umrechnung im Hauptkorpus: %d in %d Umgebungen\n" % (len(hits), len(by_env)))
for e, rows in by_env.items():
    print("%-42s %d" % (e, len(rows)))
    for n, t in rows[:3]:
        print("     %6d  %s" % (n, t))

# ---------------------------------------------------------------- Halbschritt, Komposition (v4.9.0-r01)
import math
gL = 0.2375/(math.log(2)/(math.pi*math.sqrt(3)))
eta = math.acosh(gL)/2
b = math.tanh(eta)
half = math.sqrt((1+gL)/2)
print("\nHalbschritt: cosh(eta) = %.5f, sqrt((1+gamma_L)/2) = %.5f, 1/sqrt(1-beta_sym^2) = %.5f  (Archiv bis v2.29.0: 1.197)"
      % (math.cosh(eta), half, 1/math.sqrt(1-b*b)))
print("Komposition Lorentzfaktor-Potenz, k = 1:  Materie->Photon->Tachyon %.4f  gegen direkt %.4f"
      % (math.cosh(eta)**2, gL))
for k in (1, 1.5, 2, 4, 6):
    print("   k = %-4s  zweistufig %.4f   direkt %.4f   Quotient %.4f" % (k, math.cosh(eta)**(2*k), gL**k, gL**k/math.cosh(eta)**(2*k)))
dop = math.exp(eta)
print("Doppler-Faktor je Nachbarschritt e^eta = sqrt((1+b)/(1-b)) = %.5f; zwei Schritte e^(2 eta) = %.5f (komponiert exakt)"
      % (dop, dop**2))
print("Nachbarschritt: Lorentzfaktor %.4f, Doppler %.4f; gamma_L = %.4f (Abstand Doppler-gamma_L %.2f %%, zufaellig)"
      % (math.cosh(eta), dop, gL, 100*(gL-dop)/gL))
print("\nFormeln des Hauptkorpus mit beiden Faktoren (reine Arithmetik, kein Datenvergleich):")
for name, k in (("l_P^(m)/l_P^(photon)  [gamma^{3/2}]", 1.5), ("rho_vac Verhaeltnis  [gamma^6]", 6),
                ("m_nu^(m)/m_nu^(photon)  [gamma^4]", 4), ("Matter-error  [gamma^5]", 5)):
    print("   %-40s  gamma_L: %8.3f   Nachbar (Lorentz): %7.3f   Nachbar (Doppler): %7.3f"
          % (name, gL**k, math.cosh(eta)**k, dop**k))

# Tribonacci: cosh(2 eta) = e^eta  <=>  (x - 1)(x^3 - x^2 - x - 1) = 0 mit x = e^eta
T = 1.8392867552141612
eT = math.log(T)
print("\nTribonacci T = %.10f: e^eta = %.10f, cosh(2 eta) = %.10f, coth(eta) = %.10f, beta = %.6f"
      % (T, math.exp(eT), math.cosh(2*eT), 1/math.tanh(eT), math.tanh(eT)))
print("gamma_L / T = %.5f  (Abstand %.2f %%)" % (gL/T, 100*(gL/T-1)))
