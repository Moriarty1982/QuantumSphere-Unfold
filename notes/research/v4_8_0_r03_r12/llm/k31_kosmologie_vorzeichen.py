"""k31: Konsistenz von thm:dark-energy mit prop:H0-tension und prop:saturation.

Keine neue Vorhersage, sondern Abgleich vorhandener Aussagen mit der gemessenen Expansionsgeschichte;
deshalb ohne Vorab-Notiz.  Zuordnung aus thm:dark-energy: Omega_Lambda = 1 - beta^2, also
beta^2 = 1 - Omega_Lambda = Anteil von allem, was nicht Lambda ist.
"""
import numpy as np

# Planck 2018 (TT,TE,EE+lowE+lensing), flach
Om, OL, Or = 0.3111, 0.6889, 9.1e-5
OL = 1.0 - Om - Or            # flach mit Strahlung

def omega_lambda(z):
    a = 1.0/(1.0+z)
    E2 = Or*a**-4 + Om*a**-3 + OL
    return OL/E2

def beta_needed(z):
    return np.sqrt(1.0 - omega_lambda(z))

print("Zuordnung Omega_Lambda = 1 - beta_sym^2, Expansionsgeschichte LCDM (Planck 2018)")
print("     z    Omega_Lambda     benoetigtes beta_sym")
for z in [-0.5, 0, 0.5, 1, 2, 5, 1100]:
    print("%6g    %.3e        %.4f" % (z, omega_lambda(z), beta_needed(z)))

# Aussagen des Dokuments
b0, b_cmb = 0.5493, 0.527                     # prop:H0-tension
print()
print("prop:H0-tension:  beta(0) = %.4f, beta(1100) = %.3f" % (b0, b_cmb))
print("  -> Omega_Lambda(1100) = 1 - beta^2 = %.4f   (LCDM: %.2e, Faktor %.1e)"
      % (1-b_cmb**2, omega_lambda(1100), (1-b_cmb**2)/omega_lambda(1100)))
print("  Vorzeichen d beta / d t:  Dokument > 0 (0.527 -> 0.5493),  LCDM-Zuordnung < 0 (%.4f -> %.4f)"
      % (beta_needed(1100), beta_needed(0)))
print("prop:saturation:  beta -> 1  =>  Omega_M -> 1, Omega_Lambda -> 0 (Zukunft materiedominiert)")
print("  LCDM-Zukunft (z -> -1): Omega_Lambda -> 1  =>  beta -> 0;  bei z = -0.5: beta = %.4f" % beta_needed(-0.5))

# Gegenprobe: heutiger Wert der Zuordnung
print()
print("Heute: 1 - beta_sym^2 = %.4f gegen Omega_Lambda = %.4f (Abweichung %.1f %%)"
      % (1-b0**2, OL, 100*abs(1-b0**2-OL)/OL))
