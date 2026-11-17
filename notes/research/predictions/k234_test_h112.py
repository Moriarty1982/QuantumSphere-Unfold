"""k234: Test H112 (Vorab-Notiz Vorab_Notiz_H112_Ueberbestimmung_beta.md).

Ueberbestimmung von beta^2 aus zwei unabhaengigen Messungen, ohne den Wert der Zaehlregel:
  Neutrino-Seite:   b_nu = sin^2 theta12 * cos^2 theta13   (|U_e2|^2, Lesart von H9)
  Kosmologie-Seite: b_cos = Omega_m (flaches LambdaCDM)     (Lesart von H96)
Pull z = (b_nu - b_cos) / sqrt(s_nu^2 + s_cos^2); bei asymmetrischen Fehlern die zur anderen Groesse weisende Seite.
Kriterium: |z| < 2 vertraeglich, 2 <= |z| < 3 Spannung, |z| >= 3 widerlegt.

Aufruf mit den Pruefdaten:
  python k234_test_h112.py S12 S12_OBEN S12_UNTEN S13 OMEGA OMEGA_OBEN OMEGA_UNTEN
Ohne Argumente: Vorschau mit dem Datenstand vom 17.11.2026 (kein Test, Werte vor der Festlegung bekannt).
"""
import math
import sys

BETA2_ZAEHLREGEL = 0.30185  # H9/H96; geht in das Kriterium von H112 NICHT ein, nur Bezugszeile


def pull(s12, s12u, s12d, s13, om, omu, omd):
    c13 = 1.0 - s13
    b_nu = s12 * c13
    b_cos = om
    s_nu = (s12u if b_cos > b_nu else s12d) * c13  # Fehler von theta13 vernachlaessigbar (< 2 % von s_nu)
    s_cos = omd if b_nu < b_cos else omu
    z = (b_nu - b_cos) / math.hypot(s_nu, s_cos)
    urteil = "vertraeglich" if abs(z) < 2 else ("Spannung" if abs(z) < 3 else "widerlegt")
    return b_nu, s_nu, b_cos, s_cos, z, urteil


def zeile(name, *werte):
    b_nu, s_nu, b_cos, s_cos, z, urteil = pull(*werte)
    print(f"{name:34s} b_nu {b_nu:.4f}+-{s_nu:.4f}  b_cos {b_cos:.4f}+-{s_cos:.4f}  "
          f"beta_nu {math.sqrt(b_nu):.4f}  beta_cos {math.sqrt(b_cos):.4f}  z {z:+.2f} -> {urteil}")


if len(sys.argv) == 8:
    zeile("PRUEFDATEN (Test H112)", *map(float, sys.argv[1:]))
    sys.exit(0)

print("VORSCHAU, KEIN TEST (Werte vor der Festlegung bekannt)")
s13 = 0.02248  # NuFIT 6.1, normale Ordnung
nufit = (0.3088, 0.0067, 0.0066)
juno = (0.3036, 0.0064, 0.0064)
desi = (0.2975, 0.0086, 0.0086)
planck = (0.3153, 0.0073, 0.0073)
for nn, nu in (("NuFIT 6.1", nufit), ("JUNO 2026", juno)):
    for cn, co in (("DESI DR2 BAO", desi), ("Planck 2018", planck)):
        zeile(f"{nn} gegen {cn}", *nu, s13, *co)
# Trennschaerfe bei den verlangten Genauigkeiten: s(sin^2 t12) = 0,004, s(Omega_m) = 0,006 bzw. 0,0086
for so in (0.006, 0.0086):
    s = math.hypot(0.004 * (1 - s13), so)
    print(f"Trennschaerfe bei s(Omega_m) = {so}: kombiniertes sigma {s:.4f}; widerlegt ab |Delta beta^2| >= {3*s:.4f}")
print(f"Bezug (geht nicht ein): beta_sym^2 aus der Zaehlregel = {BETA2_ZAEHLREGEL}; Hopf-Variante 1/3; TM1 0,3182*cos^2 t13 = {0.3182*(1-s13):.4f}")
