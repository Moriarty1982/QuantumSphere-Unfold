"""k42: Tachyon-Trefferkette, Kreisschluss und Beschleunigung (spezielle Relativitaet, c = 1; kein Datenvergleich).

Geprueft wird (v4.9.0-r06):
  1. Kreisschluss: Photon O -> P (Dauer d), Tachyon zurueck: Luecke d(1 - 1/v); zwei Tachyonen (Tolman) schliessen.
  2. Trefferkette mit fester Geschwindigkeit v > 1: Huygens-Huellkurve = Kegel cos th = 1/v; Gleichzeitigkeitsframe u = 1/v;
     Rapiditaet artanh v = eta + i pi/2, Boost um eta laesst i pi/2.
  3. Tachyon mit konstanter Eigenbeschleunigung: t = R cosh sig, x = R sinh sig; v = coth sig, dv/dt divergiert bei sig = 0,
     Eigenbeschleunigung 1/R; Trefferrate pro Laborzeit divergiert.
  4. Energieabgabe an die Treffer: E = mu sinh chi, p = mu cosh chi, v = coth chi; E -> 0 bei endlich vielen Treffern, v -> inf,
     Kegel oeffnet sich auf 90 Grad.
"""
import numpy as np

beta = 0.2375 / (np.log(2) / (np.pi * np.sqrt(3)))           # gamma_L
eta = np.arccosh(beta) / 2; b = np.tanh(eta); v = 1 / b; d = 1.0
print("Eingabe: eta = %.4f, beta_sym = %.4f, v = 1/beta_sym = %.4f" % (eta, b, v))

print("\n1. Kreisschluss")
print("   Photon 0 -> d: Dauer d; Tachyon d -> 0, rueckwaerts gezaehlt: -d/v; Luecke d(1 - 1/v) = %.4f d" % (1 - 1 / v))
for u in (0.3, b, 0.8):
    # zweites Tachyon im Frame u gleichzeitig (unendlich schnell) von B = (d/v, d) nach x = 0
    t_back = d / v - u * d
    print("   Tolman: Rueckweg gleichzeitig im Frame u = %.4f -> Ankunft bei x = 0 zur Zeit %+.4f d%s" %
          (u, t_back, "  (= Start: gleiche raumartige Linie zurueck)" if np.isclose(t_back, 0) else ""))

print("\n2. Trefferkette mit fester Geschwindigkeit v")
xs = np.linspace(0, 50, 5001); te = xs / v                    # Treffer bei (te, xs), je ein Lichtsignal
obs = np.array([40.0, 30.0])                                  # Beobachter in (x, y)
arr = te + np.hypot(obs[0] - xs, obs[1])
k = np.argmin(arr); ang = np.degrees(np.arctan2(obs[1], obs[0] - xs[k]))
print("   Huygens: zuerst ankommender Treffer unter %.2f Grad zur Bahn; arccos(1/v) = %.2f Grad" % (ang, np.degrees(np.arccos(1 / v))))
for u in (0.0, 1 / v, 0.9):
    g = 1 / np.sqrt(1 - u * u); tp = g * (te - u * xs)
    dt = tp[-1] - tp[0]
    print("   Frame u = %.4f: Zeitspanne der Treffer %+.3f (%s)" % (u, dt, "gleichzeitig" if abs(dt) < 1e-9 else "von 0 nach n" if dt > 0 else "von n nach 0"))
r = np.arctanh(complex(v))
print("   artanh v = %s; eta + i pi/2 = %s; nach Boost um eta: %s" % (np.round(r, 4), np.round(eta + 1j * np.pi / 2, 4), np.round(r - eta, 4)))
th = np.pi / 2; cp = (np.cos(th) + b) / (1 + b * np.cos(th))
print("   Aberration: senkrechte Welle im Frame u = beta, im Labor cos th' = %.4f -> %.2f Grad" % (cp, np.degrees(np.arccos(cp))))

print("\n3. konstante Eigenbeschleunigung 1/R, R = 1")
R = 1.0
for sig in (2.0, 0.5, 0.1, 0.01):
    t, x = R * np.cosh(sig), R * np.sinh(sig); vv = 1 / np.tanh(sig)
    dvdt = -1 / np.sinh(sig) ** 2 / (R * np.sinh(sig))        # dv/dsig / (dt/dsig)
    rate = 1 / (R * np.sinh(sig))                             # Treffer je Eigenlaenge 1 -> je Laborzeit
    print("   sig = %5.2f: t = %.4f, x = %.4f, v = %8.3f, dv/dt = %10.2f, Treffer/Laborzeit = %8.2f" % (sig, t, x, vv, dvdt, rate))
ds = 1e-5; sig = 0.7
p = lambda s: np.array([R * np.cosh(s), R * np.sinh(s)])
acc = (p(sig + ds) - 2 * p(sig) + p(sig - ds)) / ds ** 2 / R ** 2   # d2X/ds2 mit s = R sig
print("   Eigenbeschleunigung |d2X/ds2| = %.6f = 1/R" % np.sqrt(abs(acc[0] ** 2 - acc[1] ** 2)))
print("   sig < 0: t nimmt mit dem Parameter ab -> Umdeutung als Partner, Paarereignis bei (t, x) = (R, 0)")

print("\n4. Energieabgabe an die Treffer, mu = 1, Startgeschwindigkeit 1/beta_sym")
mu = 1.0; E0 = mu * np.sinh(eta); eps = E0 / 6
print("   E0 = mu sinh eta = %.4f, p0 = mu cosh eta = %.4f, p^2 - E^2 = %.4f" % (E0, mu * np.cosh(eta), (mu * np.cosh(eta)) ** 2 - E0 ** 2))
for n in range(7):
    E = E0 - n * eps; p_ = np.sqrt(E * E + mu * mu)
    vv = np.inf if E == 0 else p_ / E
    thc = 90.0 if E == 0 else np.degrees(np.arccos(1 / vv))
    print("   nach %d Treffern: E = %.4f, p = %.4f, v = %8.4f, Kegel %.2f Grad, Gleichzeitigkeitsframe u = %.4f" %
          (n, E, p_, vv, thc, 0 if E == 0 else 1 / vv))
