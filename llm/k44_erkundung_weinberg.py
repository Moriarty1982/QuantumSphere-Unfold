"""k44: Erkundung Weinberg-Winkel und Kegel (KEIN Test; Protokoll llm/Erkundungsprotokoll_Weinberg_Kegel.md).

Jede Variante wird gerechnet und im Protokoll eingetragen, auch Fehlschlaege.
Daten (PDG 2024 + Update 2025, Review "Electroweak Model and Constraints on New Physics", Stand 15. April 2026, und
Summary Tables, abgerufen 2026-10-21):
  alpha(0)^-1 = 137.035999084, alpha_hat^(5)(M_Z)^-1 = 127.930 (MS-bar), G_F = 1.1663785e-5 GeV^-2,
  Delta rho_t = 0.00934 (m_t/172.61 GeV)^2 (Gl. 10.16), m_W, m_Z wie k43, s_hat^2_Z = 0.23122.
Leading-order-Abschaetzungen; Genauigkeit etwa 10^-3 in sin^2.
"""
import math

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
b = math.tanh(0.5 * math.acosh(gL))
pred = lambda beta: (1 - beta) / 2
mW, mZ = 80.3692, 91.1880
s2_os = 1 - (mW / mZ) ** 2
s2_ms = 0.23122; c2_ms = 1 - s2_ms
a0 = 1 / 137.035999084; aZ = 1 / 127.930; GF = 1.1663785e-5
drho_t = 0.00934
s2 = lambda: None
print("Referenz: Vorhersage %.5f (beta_sym = %.5f); on-shell %.5f; MS-bar %.5f" % (pred(b), b, s2_os, s2_ms))

print("\nE1  beta_sym durch den Tribonacci-Wert ersetzen")
T = 1.8392867552141612; bT = math.tanh(math.log(T))
print("    beta_T = %.5f -> Vorhersage %.5f; Abstand zu on-shell %+.5f (vorher %+.5f)" % (bT, pred(bT), pred(bT) - s2_os, pred(b) - s2_os))

print("\nE2  on-shell-Winkel ohne den Top-Beitrag Delta rho_t (fuehrende Ordnung: c_W^2 = c_hat^2 (1 + Delta rho))")
s2_os_not = s2_os + c2_ms * drho_t
print("    c_hat^2 Delta rho_t = %.5f; on-shell ohne Top: %.5f; Abstand der Vorhersage %+.5f" % (c2_ms * drho_t, s2_os_not, pred(b) - s2_os_not))
print("    Kontrolle: MS-bar - c_hat^2 Delta rho_t = %.5f (gegen on-shell %.5f; Rest = Higgs/hoehere Ordnungen)" % (s2_ms - c2_ms * drho_t, s2_os))

print("\nE3  Baumgraphen-Winkel aus (alpha, G_F, m_Z): sin^2 2theta = 4 pi alpha / (sqrt2 G_F m_Z^2)")
for name, a in (("alpha(0)", a0), ("alpha_hat(M_Z)", aZ)):
    x = 4 * math.pi * a / (math.sqrt(2) * GF * mZ ** 2)
    s2t = (1 - math.sqrt(1 - x)) / 2
    print("    %-15s sin^2 = %.5f, 2 theta = %.3f Grad; Abstand der Vorhersage %+.5f" % (name, s2t, 2 * math.degrees(math.asin(math.sqrt(s2t))), pred(b) - s2t))

print("\nE4  (beim Rechnen von E2 aufgefallen) welcher Bruchteil f von Delta rho_t gibt genau die Vorhersage?")
f = (pred(b) - s2_os) / (c2_ms * drho_t)
mt_eff = 172.61 * math.sqrt(1 - f)
print("    f = %.3f; entspricht einem Top-Beitrag mit m_t,eff = 172.61 sqrt(1 - f) = %.1f GeV (m_Z = %.1f, m_W = %.1f)" % (f, mt_eff, mZ, mW))

print("\nE5  (Vorschlag des Autors) Neutrinos als fehlender Betrag")
need = (pred(b) - s2_os) / c2_ms                  # noetige Aenderung von Delta rho (negativ = weniger)
dmW = -mZ ** 2 * (pred(b) - s2_os) / (2 * mW)
print("    noetig: Delta rho um %+.5f aendern (Vorzeichen: weniger als im SM); entspricht m_W um %+.1f MeV" % (-need, 1e3 * dmW))
k = 0.00934 / (3 * 172.61 ** 2)                    # G_F/(8 sqrt2 pi^2) in GeV^-2
F = lambda m1, m2: m1 ** 2 + m2 ** 2 - (2 * m1 ** 2 * m2 ** 2 / (m1 ** 2 - m2 ** 2)) * math.log(m1 ** 2 / m2 ** 2)
me, mnu = 0.000511, 0.05e-9
print("    leichtes Neutrino im Dublett mit dem Elektron: Delta rho = %.1e (noetig %.1e)" % (k * F(me, mnu), need))
dm = math.sqrt(need / k)
print("    schweres Dirac-Dublett: Delta rho = k F >= 0 (falsche Richtung); Betrag waere mit Aufspaltung ~%.0f GeV erreicht" % dm)
