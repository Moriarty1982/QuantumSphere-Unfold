"""k300 (Erkundung, nicht blind): Wie schlimm sind 9,8 GeV statt 125 GeV, und woran haengt die Zahl?
Formel (Gildener-Weinberg, eine Schleife): m_s^2 = (1/(8 pi^2 v^2)) * [ Summe_Bosonen n m^4 - Summe_Fermionen n m^4 ]
Eingaben aus dem Gedaechtnis (nicht nachgeschlagen): m_W, m_Z, m_t, m_h, v in GeV.
Aufruf: python k300_skala_9_8_GeV.py > k300_out.txt
"""
import math

mW, mZ, mt, mh, v = 80.37, 91.19, 172.6, 125.2, 246.22
pref = 1 / (8 * math.pi ** 2 * v ** 2)
SB = 3 * (2 * mW ** 4 + mZ ** 4)          # W+, W-, Z mit je 3 Polarisationen
SF = 12 * mt ** 4                         # Top: 4 Spinzustaende x 3 Farben

print("== 1  Die Zahl ==")
ms2 = pref * SB
print(f"  nur Eichfelder: Summe = {SB:.4e} GeV^4, m_s = {math.sqrt(ms2):.2f} GeV")
print(f"  gemessen: {mh} GeV. Faktor in der Masse {mh / math.sqrt(ms2):.1f}, im Massenquadrat {mh ** 2 / ms2:.0f}")
print("  Die Formel enthaelt nur m_W, m_Z und v (oder g, g', v). Keine Setzung dieses Fadens geht ein.")

print("\n== 2  Empfindlichkeit ==")
for d in (-0.05, 0.05):
    print(f"  alle Eichfeldmassen {d:+.0%}: m_s = {math.sqrt(pref * SB * (1 + d) ** 4):.2f} GeV")
print(f"  m_s waechst wie (Masse)^2/v: fuer 125 GeV muessten die Eichfeldmassen um den Faktor {math.sqrt(mh / math.sqrt(ms2)):.2f} groesser sein")

print("\n== 3  Mit dem Top-Quark ==")
print(f"  Fermionen zaehlen negativ: 12 m_t^4 = {SF:.4e} GeV^4, das {SF / SB:.1f}-fache der Eichfelder")
print(f"  Summe = {SB - SF:.4e} GeV^4 < 0: m_s^2 = {pref * (SB - SF):.0f} GeV^2, also kein Minimum mehr")

print("\n== 4  Was fehlt ==")
need = mh ** 2 / pref
miss = need - SB + SF
print(f"  fuer m_s = {mh} GeV noetig: Summe = {need:.4e} GeV^4; es fehlen an Bosonen {miss:.4e} GeV^4")
for n in (1, 2, 4, 8):
    print(f"  {n} reelle(s) Zusatzfeld(er) gleicher Masse: m = {(miss / n) ** 0.25:.0f} GeV")
print(f"  ohne Top gerechnet (nur zum Vergleich): es fehlten {need - SB:.4e} GeV^4, ein Feld mit {(need - SB) ** 0.25:.0f} GeV")

print("\n== 5  Die Aehnlichkeit mit g = 9,81 m/s^2 ==")
g = 9.80665
ms = math.sqrt(ms2)
print(f"  m_s = {ms:.3f} GeV gegen g = {g} m/s^2: Abweichung der Ziffern {abs(ms - g) / g:.2%}")
J = ms * 1.602176634e-10
print(f"  dieselbe Masse in anderen Einheiten: {J:.3e} J, {J / 2.99792458e8 ** 2:.3e} kg, {ms / 0.93827:.2f} Protonmassen")
print(f"  dieselbe Beschleunigung in anderen Einheiten: {g / 0.3048:.2f} ft/s^2, {g * 100:.0f} Gal")
hbar, c = 1.054571817e-34, 2.99792458e8
Eg = hbar * g / c / 1.602176634e-19
print(f"  g als Energie in natuerlichen Einheiten: hbar g / c = {Eg:.2e} eV; Verhaeltnis zu m_s: {ms * 1e9 / Eg:.1e}")
print(f"  mit g = 0.652, g' = 0.357, v = 246 (k299): {math.sqrt(3 * (2 * 0.652 ** 4 + (0.652 ** 2 + 0.357 ** 2) ** 2) / (128 * math.pi ** 2)) * 246:.2f} GeV; die dritte Ziffer haengt an den Eingaben")
print(f"  bekannte halbe Erklaerung fuer g selbst: pi^2 = {math.pi ** 2:.4f} (das Sekundenpendel ist fast einen Meter lang); das betrifft den Meter, nicht das GeV")
