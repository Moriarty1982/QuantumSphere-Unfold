"""k46: H15 (Vorab-Notiz llm/Vorab_Notiz_H15_W_Masse_gamma_L.md, Commit 62c505d).

Schritt 1 (sofort nach dem Commit): Vorhersage festlegen, kein Vergleich.
Schritt 2 (spaeter): Vergleich mit der ersten m_W-Weltmittelung nach 2026-10-21; Werte unten eintragen.
"""
import math


def meissner_sum(g):
    s, j = 0.0, 0.5
    while True:
        term = 2 * math.exp(-2 * math.pi * g * math.sqrt(j * (j + 1)))
        s += term
        if term < 1e-17:
            return s
        j += 0.5


lo, hi = 0.1, 0.5                     # Summe faellt monoton in g
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if meissner_sum(mid) > 1:
        lo = mid
    else:
        hi = mid
gBI = 0.5 * (lo + hi)
gstr = math.log(2) / (math.pi * math.sqrt(3))
gL = gBI / gstr
mZ, sZ = 91.1880, 0.0020
cos_t = gL / math.sqrt(1 + gL * gL)
mW_pred = mZ * cos_t
s_pred = cos_t * sZ
print("Schritt 1: gamma_BI = %.12f (Summe - 1 = %.1e)" % (gBI, meissner_sum(gBI) - 1))
print("           gamma_string = %.12f, gamma_L = %.10f" % (gstr, gL))
print("           Vorhersage m_W = %.4f +- %.4f GeV  (sin^2 theta_W = %.6f)" % (mW_pred, s_pred, 1 - cos_t ** 2))

# Schritt 2: erst eintragen, wenn die erste Weltmittelung nach 2026-10-21 vorliegt
MEAS = None                            # (m_W, sigma, Quelle, Datum, m_W_SM)
if MEAS:
    mW, sW, src, date, mSM = MEAS
    z = (mW - mW_pred) / math.hypot(sW, s_pred)
    print("Schritt 2: %s (%s): m_W = %.4f +- %.4f, z = %+.2f; SM %.4f, Abstand Vorhersage-SM = %.1f sigma_meas"
          % (src, date, mW, sW, z, mSM, abs(mW_pred - mSM) / sW))
