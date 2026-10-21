"""k43: Test H14 (Vorab-Notiz llm/Vorab_Notiz_H14_Kegelwinkel_Weinberg.md, Commit 5911161).

H14: theta_c = 2 theta_W  <=>  sin^2 theta_W = (1 - beta_sym)/2.
Daten: PDG, S. Navas et al., Phys. Rev. D 110, 030001 (2024) and 2025 update, abgerufen 2026-10-21:
  Summary Tables "Gauge and Higgs Bosons" (erstellt 2025-05-30): m_W = 80.3692 +- 0.0133 GeV, m_Z = 91.1880 +- 0.0020 GeV,
  sin^2 theta_eff = 0.23148 +- 0.00013.
  Review "Electroweak Model and Constraints on New Physics" (rpp2025-rev-standard-model): MS-bar s^2_Z = 0.23122 +- 0.00006;
  dort zusaetzlich on-shell s^2_W = 0.22342 +- 0.00009 aus dem globalen SM-Fit (nur berichtet, nicht Verfahren).
"""
import math

# ---------------------------------------------------------------- Eingaben (Notiz, verbindlich)
gBI = 0.2375; gstr = math.log(2) / (math.pi * math.sqrt(3))
gL = gBI / gstr
b = math.tanh(0.5 * math.acosh(gL))
b_doc = 1 / 1.820
mW, sW = 80.3692, 0.0133
mZ, sZ = 91.1880, 0.0020
s2_ms, s_ms = 0.23122, 0.00006
s2_eff, s_eff = 0.23148, 0.00013
s2_fit, s_fit = 0.22342, 0.00009

# ---------------------------------------------------------------- Schritt 1-3
pred = (1 - b) / 2
pred_doc = (1 - b_doc) / 2
s2_os = 1 - (mW / mZ) ** 2
sig_os = math.hypot(2 * mW / mZ ** 2 * sW, 2 * mW ** 2 / mZ ** 3 * sZ)
D = pred - s2_os; z = D / sig_os
print("gamma_L = %.5f, beta_sym = %.5f (Dokumentwert 1/1.820 = %.5f)" % (gL, b, b_doc))
print("Vorhersage s2_pred = (1 - beta_sym)/2 = %.5f (mit Dokumentwert %.5f)" % (pred, pred_doc))
print("On-shell aus Massen: s2_OS = 1 - mW^2/mZ^2 = %.5f +- %.5f" % (s2_os, sig_os))
print("Delta = %+.5f, z = %+.1f" % (D, z))

# ---------------------------------------------------------------- Schritt 4: Band
lo = min(s2_os - 3 * sig_os, s2_ms - 3 * s_ms); hi = max(s2_os + 3 * sig_os, s2_ms + 3 * s_ms)
inB = lo <= pred <= hi
print("Band B = [%.5f, %.5f]; s2_pred in B: %s" % (lo, hi, inB))

# ---------------------------------------------------------------- Schritt 5: Winkel
thc = math.degrees(math.acos(b))
print("theta_c = %.3f Grad" % thc)
for name, s2 in (("on-shell (Massen)", s2_os), ("MS-bar", s2_ms), ("effektiv", s2_eff), ("on-shell (SM-Fit, nur berichtet)", s2_fit)):
    tw = math.degrees(math.asin(math.sqrt(s2)))
    print("   %-34s sin2 = %.5f, theta_W = %.3f, 2 theta_W = %.3f, cos 2theta_W = %.5f, Abstand zu beta_sym %+.5f"
          % (name, s2, tw, 2 * tw, 1 - 2 * s2, 1 - 2 * s2 - b))

# ---------------------------------------------------------------- Schritt 6: Look-elsewhere
w = hi - lo; p1 = w / 0.5; p5 = 1 - (1 - p1) ** 5
print("Look-elsewhere: Bandbreite %.5f, Trefferwahrscheinlichkeit je Beziehung %.3f, fuer fuenf Kandidaten %.3f" % (w, p1, p5))

# ---------------------------------------------------------------- Entscheidung
A = "verträglich" if abs(z) < 2 else "Spannung" if abs(z) < 3 else "widerlegt"
B = "nicht entscheidbar auf Baumgraphen-Niveau" if inB else "widerlegt"
print("\nEntscheidung (A) exakt, on-shell: %s (|z| = %.1f)" % (A, abs(z)))
print("Entscheidung (B) Baumgraphen:     %s" % B)
