"""k213 (Erkundung, Abschaetzung): Gravitonen am Urknall unter G2, Delta <~ l_P, und Delta N_eff.
Annahme: Gravitonen (2 Polarisationen) tragen Materie-Gewichte wie die uebrigen erzeugten Bosonen und bekommen n0 je Mode
bis k_max; alle erzeugten Bosonen haben dasselbe Spektrum. Die nicht-gravitativen Bosonen thermalisieren (zusammen mit den
dann erzeugten Fermionen, g* = 106.75), die Gravitonen nicht. Entropieerhaltung: rho_rad a^4 ~ g*^{-1/3}.
Delta N_eff = (8/7)(11/4)^{4/3} rho_GW/rho_gamma bei der BBN (g* = 10.75, rho_rad/rho_gamma = 10.75/2).
Aufruf: python k213_gravitonen_neff.py
"""
g_init_thermal, g_bbn = 106.75, 10.75
pref = (8/7)*(11/4)**(4/3)
print('g_B (erzeugte Bosonen ohne Gravitonen) | Anteil GW anfangs | rho_GW/rho_gamma (BBN) | Delta N_eff')
for gB in (0, 4, 28, 100, 300, 1000):
    f0 = 2/(2 + gB)                       # Energieanteil der Gravitonen anfangs
    r_rad = f0/(1 - f0) if gB > 0 else float('inf')   # rho_GW/rho_rest anfangs
    r_bbn = r_rad*(g_init_thermal/g_bbn)**(1/3)      # rho_GW/rho_rad bei der BBN
    r_gam = r_bbn*g_bbn/2
    print(f'{gB:5d} | {f0:.3f} | {r_gam:.3f} | {pref*r_gam:.2f}')
print('Grenze (Vorwissen, nicht nachgeschlagen): Delta N_eff <~ 0.3')
