"""k32: Rollen von \\bsym im Companion.

Ordnet jede Zeile mit \\bsym nach dem Kontext (+-3 Zeilen) einer Rolle zu:
  F  Frame/Beobachter: Umrechnung ueber gamma_L, Lorentzfaktor, Beobachterposition z_-, k-Werte
  K  Kaskade/Kosmologie: Verzweigung P(S^8 -> S^4), Omega-Anteile, Lambda, Markov
  H  Geometrie: Hopf-Winkel, Kontinuumswert 1/sqrt(3)
Mehrfachtreffer werden als Mischstellen gezaehlt.  Heuristik, keine Beweisfuehrung; die Mischstellen
sind die, an denen zwei Rollen in einem Satz verbunden werden.
"""
import re, os, collections
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "..", "Quantum_Sphaera_Companion_v4_8_0_source.tex")
L = open(src, encoding="utf-8").read().split("\n")
START_ROUNDS = next(i for i, l in enumerate(L) if "v4.7.0-r94 Source-Only" in l)

pat = {
    "F": re.compile(r"\\gL|Lorentz|frame[- ]factor|observer|\\zminus\s*=|k\(|frame offset|photon[- ]frame value|matter frame", re.I),
    "K": re.compile(r"\\Omega|Omega_|P\(S\^|cascade|Markov|dark energy|\\Lambda|cosmolog|matter dominated", re.I),
    "H": re.compile(r"Hopf|theta_H|arcsin|1/\\sqrt\{?3", re.I),
}
rows = []
for i, l in enumerate(L):
    if "bsym" not in l or i >= START_ROUNDS:
        continue
    ctx = "\n".join(L[max(0, i-3):i+4])
    roles = "".join(r for r, p in pat.items() if p.search(ctx)) or "-"
    rows.append((i+1, roles))

c = collections.Counter(r for _, r in rows)
print("Hauptkorpus (vor r94): %d Zeilen mit \\bsym" % len(rows))
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print("  %-4s %3d" % (k, v))

# Mischstellen F+K: dort werden Frame-Rolle und Kaskaden-Rolle verbunden
fk = [n for n, r in rows if "F" in r and "K" in r]
print("\nMischstellen F+K (Zeilen):", fk)

# Labels der Umgebungen, in denen die Mischstellen stehen
def env(n):
    for j in range(n-1, max(0, n-80), -1):
        m = re.search(r"\\label\{([^}]+)\}", L[j])
        if m:
            return m.group(1)
    return "?"
print("\nUmgebungen der Mischstellen:")
for lab, cnt in collections.Counter(env(n) for n in fk).most_common():
    print("  %-40s %d" % (lab, cnt))

# ---------------------------------------------------------------- Drei Frames, Kreuzterme (r18)
import math
print("\nDrei Frames + (Materie), 0 (Photon), - (Tachyon) in Rapiditaeten")
gBI, gstr = 0.2375, math.log(2)/(math.pi*math.sqrt(3))
gL = gBI/gstr
b = math.sqrt((gL-1)/(gL+1))
eta = math.atanh(b)
pos = {"+": eta, "0": 0.0, "-": -eta}
print("gamma_L = %.4f, beta_sym = %.4f, eta = artanh(beta_sym) = %.4f" % (gL, b, eta))
for a in "+0-":
    print("  " + "   ".join("%s%s: beta=%+.4f gamma=%.4f" % (a, c, math.tanh(pos[a]-pos[c]), math.cosh(pos[a]-pos[c]))
                           for c in "+0-"))
print("(a) cosh(2 eta) = %.4f = gamma_L (Kreuzterm +-);  cosh(eta) = %.4f (Kreuzterm +0);  cosh(eta)^2 = %.4f"
      % (math.cosh(2*eta), math.cosh(eta), math.cosh(eta)**2))
print("(b) Halbierung des +- Versatzes: in Geschwindigkeit %.4f, in Rapiditaet %.4f"
      % (math.tanh(2*eta)/2, math.tanh(eta)))
print("(c) tanh^2(eta) = %.4f, sech^2(eta) = %.4f, Summe %.6f"
      % (math.tanh(eta)**2, 1/math.cosh(eta)**2, math.tanh(eta)**2 + 1/math.cosh(eta)**2))
print("Drei Werte: LQG %.4f, Planck sqrt(Omega_M) %.4f, Hopf 1/sqrt3 %.4f; Abstand LQG-Planck %.2f %%"
      % (b, math.sqrt(0.3111), 1/math.sqrt(3), 100*(math.sqrt(0.3111)-b)/b))
