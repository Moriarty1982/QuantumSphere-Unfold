"""k108: Erkundung (nicht vorab festgelegt) - Lambda als Mischung ueber Kreuzungen der Sektoren.

Frage (Autor, 28.10.): Gibt es ein Lambda je Kreuzung der Sektoren, und ist unser Wert eine Mischung?

Lesarten (endliche Klasse, vor dem Lauf hier festgehalten):
  Gewichtsquellen (zwei Parteien je Lesart):
    W1  Eigenwerte des M/T-Zustands, |b| = 1/gamma_L (r17):   p = ((1+|b|)/2, (1-|b|)/2)
    W2  Zaehlgewichte aus r63/r67:                            p = (g_M, g_T)/(g_M+g_T), g_M/g_T = gamma_L
    W3  Zerlegung rein + Photon P = I/2 (r24):                p = (|b|, 1-|b|)
  Linear:    Omega_Lambda = p_1 oder p_2                       (2 Moeglichkeiten je Quelle)
  Bilinear:  Kreuzungen 11, 12, 22 mit Gewichten p1^2, 2 p1 p2, p2^2;
             jede nichttriviale Teilmenge als 'Vakuum-Kreuzungen' (6 Moeglichkeiten je Quelle)
  Zusaetzlich die operator-natuerliche Form (zerlegungsunabhaengig, SU(2)-invariant):
             Singulett-Gewicht (1-|b|^2)/4, Triplett-Gewicht (3+|b|^2)/4      (2 Moeglichkeiten)
  Insgesamt 3*2 + 3*6 + 2 = 26 Lesarten.
Daten: Planck 2018 (TT,TE,EE+lowE+lensing) Omega_m = 0.315 +- 0.007; DESI DR2 BAO allein Omega_m = 0.2975 +- 0.0086 (flach).
Treffer: Omega_Lambda innerhalb 2 sigma von Planck oder DESI.
"""
import itertools, math, json, sys
import mpmath as mp
mp.mp.dps = 30

# gamma_L aus dem ungerundeten beta_sym = 0.549406 (r68): gamma_L = (1 + beta^2)/(1 - beta^2), |b| = 1/gamma_L (r17)
beta = mp.mpf('0.549406')
gL = (1 + beta**2) / (1 - beta**2)
b = 1/gL

data = {"Planck": (0.315, 0.007), "DESI": (0.2975, 0.0086)}
def hit(oL):
    out = {}
    for k, (om, s) in data.items():
        z = (1 - oL - om) / s     # Omega_m = 1 - Omega_Lambda (flach)
        out[k] = float(z)
    return out

sources = {
    "W1 Eigenwerte": ((1 + b)/2, (1 - b)/2),
    "W2 Zaehlgewichte": (gL/(gL + 1), 1/(gL + 1)),
    "W3 rein+P": (b, 1 - b),
}
rows = []
for name, (p1, p2) in sources.items():
    for i, p in enumerate((p1, p2), 1):
        rows.append({"Quelle": name, "Form": f"linear p{i}", "Omega_L": float(p)})
    w = {"11": p1*p1, "12": 2*p1*p2, "22": p2*p2}
    for k in range(1, 3):
        for sub in itertools.combinations(["11", "12", "22"], k):
            rows.append({"Quelle": name, "Form": "Kreuzungen " + "+".join(sub), "Omega_L": float(sum(w[s] for s in sub))})
rows.append({"Quelle": "Operator SU(2)", "Form": "Singulett", "Omega_L": float((1 - b*b)/4)})
rows.append({"Quelle": "Operator SU(2)", "Form": "Triplett", "Omega_L": float((3 + b*b)/4)})
for r in rows:
    z = hit(r["Omega_L"])
    r["z_Planck"], r["z_DESI"] = z["Planck"], z["DESI"]
    r["Treffer"] = abs(z["Planck"]) <= 2 or abs(z["DESI"]) <= 2

print(f"gamma_L = {float(gL):.6f}, |b| = 1/gamma_L = {float(b):.6f}, beta^2 = {float(beta**2):.6f}")
print(f"{'Quelle':18s} {'Form':22s} {'Omega_L':>8s} {'Omega_m':>8s} {'z Planck':>9s} {'z DESI':>8s}")
for r in rows:
    print(f"{r['Quelle']:18s} {r['Form']:22s} {r['Omega_L']:8.4f} {1-r['Omega_L']:8.4f} {r['z_Planck']:9.2f} {r['z_DESI']:8.2f} {'TREFFER' if r['Treffer'] else ''}")
n = len(rows); h = sum(r["Treffer"] for r in rows)
# Zufallserwartung: Anteil des Trefferbereichs an [0,1]
lo = min(1 - om - 2*s for om, s in data.values()); hi = max(1 - om + 2*s for om, s in data.values())
print(f"Lesarten: {n}, Treffer: {h}; Trefferbereich Omega_L in [{lo:.4f}, {hi:.4f}] (Breite {hi-lo:.3f}); "
      f"Zufallserwartung bei gleichverteilten Werten etwa {n*(hi-lo):.1f}")
print("Vergleich: thm:dark-energy Omega_m = beta^2 =", round(float(beta**2), 4), " z Planck", round((float(beta**2)-0.315)/0.007, 2),
      " z DESI", round((float(beta**2)-0.2975)/0.0086, 2))
json.dump(rows, open(sys.argv[1] if len(sys.argv) > 1 else "k108_out.json", "w"), indent=1)
