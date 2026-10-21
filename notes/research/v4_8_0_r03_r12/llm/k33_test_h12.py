"""k33: Rechnung zur Vorab-Notiz H12 (Commit a593f5d), Verfahren 1-3 der Notiz.

R1  cosh(eta_+ + eta_s) = gamma_L
R2  Omega_M = tanh^2(eta_s)
R3  sin^2 theta_12 = tanh^2(eta_+) / cos^2 theta_13
"""
import math

g_string = math.log(2)/(math.pi*math.sqrt(3))
g_BI = 0.2375
gL = g_BI/g_string
s13, ds13 = 0.02215, 0.00057            # NuFIT 6.0
OM, dOM = 0.3111, 0.0056                 # Planck 2018 TT,TE,EE+lowE+lensing+BAO (festgelegt)
OM_alt, dOM_alt = 0.3153, 0.0073         # Planck 2018 ohne BAO (nur berichtet)
H9 = 0.30862                             # Vorab-Notiz H9
JUNO26, dJUNO26 = 0.3036, 0.0064         # gelesen, zaehlt nicht
SIGMA_KUENFTIG = 0.004                   # Mindestgenauigkeit der zaehlenden Messung

def model(om, s):
    eta_s = math.atanh(math.sqrt(om))
    eta_p = math.acosh(gL) - eta_s
    P = math.tanh(eta_p)**2/(1-s)
    return eta_p, eta_s, P

def pred(om, dom):
    eta_p, eta_s, P = model(om, s13)
    h = 1e-6
    dP_om = (model(om+h, s13)[2]-model(om-h, s13)[2])/(2*h)
    dP_s = (model(om, s13+h)[2]-model(om, s13-h)[2])/(2*h)
    sP = math.hypot(dP_om*dom, dP_s*ds13)
    return eta_p, eta_s, P, sP

eta_p, eta_s, P, sP = pred(OM, dOM)
print("gamma_L = %.5f, arcosh(gamma_L) = %.5f" % (gL, math.acosh(gL)))
print("eta_s = %.5f  beta_s = %.5f   (Tachyon-Seite, aus Omega_M)" % (eta_s, math.tanh(eta_s)))
print("eta_+ = %.5f  beta_+ = %.5f   (Materie-Seite)" % (eta_p, math.tanh(eta_p)))
print("zum Vergleich symmetrisch: eta = %.5f, beta_sym = %.5f" % (math.acosh(gL)/2, math.tanh(math.acosh(gL)/2)))
print()
print("P12 = sin^2 theta_12 = %.5f +- %.5f" % (P, sP))
_, _, Pa, sPa = pred(OM_alt, dOM_alt)
print("Variante ohne BAO (entscheidet nicht): %.5f +- %.5f" % (Pa, sPa))
print("Abstand zu H9: P12 - H9 = %+.5f" % (P-H9))
print()
z = (P-JUNO26)/math.hypot(dJUNO26, sP); z9 = (H9-JUNO26)/math.hypot(dJUNO26, 0.00018)
print("JUNO 2026 (zaehlt nicht): z12 = %+.2f, z9 = %+.2f, Delta chi2 = %+.2f" % (z, z9, z9**2-z**2))
sig = math.hypot(SIGMA_KUENFTIG, sP)
print("Trennbarkeit bei sigma_x = %.3f: sigma = %.5f, |P12-H9| / sigma = %.2f  (trennbar ab 2)"
      % (SIGMA_KUENFTIG, sig, abs(P-H9)/sig))
# Bestfall je Richtung: Messwert genau auf einer Hypothese.  |Delta chi2| = (P-H9)^2 / (sigma_x^2 + sigma_andere^2)
d2 = (P-H9)**2
for name, s_other in (("Messwert auf H12 (H12 bevorzugt)", 0.00018), ("Messwert auf H9 (H9 bevorzugt)", sP)):
    need = d2/4 - s_other**2
    print("%-34s |Delta chi2| bei sigma_x = 0.004: %.2f;  fuer 4 noetig: sigma_x <= %s"
          % (name, d2/(SIGMA_KUENFTIG**2 + s_other**2),
             "%.5f" % math.sqrt(need) if need > 0 else "nicht erreichbar"))
