"""Suche nach einem blinden Test aus r16/r17: Neutrino-Kandidaten gegen bekannte Daten (Erkundung, nicht blind).

Daten: NuFIT 6.0, normale Ordnung (mit SK): Delta m^2_21 = 7.49e-5 eV^2, Delta m^2_31 = 2.513e-3 eV^2 (aus Vorwissen,
wie in k222/H100 verwendet); R_obs ~ 0.0298.
(1) Zeitzyklus mit positiven Gewichten (Auslesungen eines Objekts): erreichbare Koide-Werte K fuer Neutrinos bei
    normaler und invertierter Ordnung (m_lightest von 0 bis 0.1 eV).
(2) Kandidat "Majorana: p+ = p-" mit K = 2/3: delta = 0 -> Massenspektrum, R.
(3) Kandidat "nur eine Helizitaet: p- = 0" (flaches Oktant) mit K = 2/3: R.
"""
import numpy as np

dm21, dm31 = 7.49e-5, 2.513e-3
print(f"R_obs = {dm21/dm31:.4f}")


def K(m):
    m = np.asarray(m, float); return m.sum() / np.sqrt(m).sum() ** 2


ml = np.linspace(0, 0.1, 2001)
no = [K([x, np.sqrt(x**2 + dm21), np.sqrt(x**2 + dm31)]) for x in ml]
io = [K([np.sqrt(x**2 + dm31), np.sqrt(x**2 + dm31 + dm21), x]) for x in ml]
print(f"(1) positive Wurzeln: K_max normal = {max(no):.4f} (bei m_1 = {ml[int(np.argmax(no))]:.4f} eV),"
      f" K_max invertiert = {max(io):.4f}; K = 2/3 nicht erreichbar")


def masses_from(delta):
    s = 1 + np.sqrt(2) * np.cos(delta + 2 * np.pi * np.arange(3) / 3)   # sqrt(m) bis auf Faktor
    m = np.sort(s ** 2); return m, s


for label, delta in (("(2) Majorana p+ = p- (delta = 0)", 0.0), ("(3) eine Helizitaet p- = 0 (delta = pi/12)", np.pi / 12)):
    m, s = masses_from(delta)
    R = (m[1]**2 - m[0]**2) / (m[2]**2 - m[0]**2)   # m sind Massen
    print(f"{label}: sqrt(m) ~ {np.round(np.sort(s), 4)}, R = {R:.4f} gegen {dm21/dm31:.4f}")
