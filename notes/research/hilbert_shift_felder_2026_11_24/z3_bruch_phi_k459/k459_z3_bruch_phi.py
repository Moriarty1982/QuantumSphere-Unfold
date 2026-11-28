"""k459 (Erkundung, nicht blind): Ist der Versatz phi eine kleine Z3-Brechung? Leck-Energie (H238/H241) der Lepton-Phasen als Potential fuer phi.
Aufruf aus diesem Ordner: python3 k459_z3_bruch_phi.py > k459_out.txt
Lepton-Phasen (H225/H236, q -> 0-): fold(delta_Im) = pi/12 - phi, fold(delta_Re) = pi/6 - phi. Messwert phi = x = 0,0395773.
Leck je Sektor (H238, normiert): sin^2(3 delta); periodisch mit pi/3 und gerade, haengt also nur von fold(delta) ab.
"""
import numpy as np

x = 0.0395773
dIm, dRe = 0.2222220470731, 0.48399
print("=" * 96)
print("k459  Z3-Brechung und Versatz phi (Erkundung, nicht blind)")
print("=" * 96)
print("\n1) Abstand der gemessenen Phasen zum naechsten Z3-geschlossenen Punkt (3 delta = 0 mod pi)")
for n, d in (("delta_Im", dIm), ("delta_Re", dRe)):
    dist = min(d % (np.pi / 3), np.pi / 3 - d % (np.pi / 3))
    print(f"  {n} = {d:.7f}: Abstand {dist:.5f} rad = {np.degrees(dist):.3f} Grad; Bruch |sin 3 delta| = {abs(np.sin(3*d)):.5f};  phi = {x:.5f} rad = {np.degrees(x):.3f} Grad")
print("  Basislagen ohne Versatz: pi/12 -> |sin 3 delta| = %.5f, pi/6 -> %.5f (schon ohne phi weit von Z3-Schluss)" % (abs(np.sin(np.pi/4)), abs(np.sin(np.pi/2))))


def E(phi, wI, wR):
    return wI * np.sin(3 * (np.pi / 12 - phi)) ** 2 + wR * np.sin(3 * (np.pi / 6 - phi)) ** 2


print("\n2) Leck-Energie E(phi) = w_I sin^2(3(pi/12-phi)) + w_R sin^2(3(pi/6-phi)); Baum mit q -> 0- ist in phi flach (reine Drehung)")
print("   dE/dphi = -3 (w_I cos 6phi + w_R sin 6phi)  ->  stationaer bei tan 6phi = -w_I/w_R")
ph = np.linspace(-np.pi / 12, np.pi / 4, 200001)
for wI, wR, lab in ((1, 1, "gleich"), (2, 1, "Zaehlgewichte Dirac:Majorana (H235)"), (1, 2, "umgekehrt"), (1, 0, "nur Im"), (0, 1, "nur Re")):
    e = E(ph, wI, wR)
    i = np.argmin(e); j = np.argmax(e)
    dE = -3 * (wI * np.cos(6 * x) + wR * np.sin(6 * x))
    print(f"  ({wI},{wR}) {lab:36s}: Minimum bei phi = {ph[i]:+.5f} ({ph[i]/np.pi:+.4f} pi), Maximum bei {ph[j]:+.5f}; dE/dphi(x) = {dE:+.4f}")
r = -np.tan(6 * x)
print(f"\n3) Gewichte, fuer die phi = x stationaer waere: w_I/w_R = -tan(6x) = {r:.6f} (entgegengesetzte Vorzeichen noetig)")
print(f"   naechster einfacher Bruch -1/4 gaebe phi* = {np.arctan(0.25)/6:.7f} ({abs(np.arctan(0.25)/6-x)/x*100:.2f} % daneben; phi ist auf ~1e-7 bekannt)")

print("\n4) Zufallskontrolle: zufaellige Gewichte (w_I, w_R) gleichverteilt in [-1,1]^2; Anteil mit Minimum innerhalb 1 % von x")
rng = np.random.default_rng(459); hit = 0
for _ in range(20000):
    wI, wR = rng.uniform(-1, 1, 2)
    p = np.arctan2(-wI, wR) / 6  # tan 6phi = -wI/wR
    cands = (p + np.arange(-3, 4) * np.pi / 6)
    mins = [c for c in cands if -18 * (wR * np.cos(6 * c) - wI * np.sin(6 * c)) > 0]
    hit += any(abs(c - x) < 0.01 * x for c in mins)
print(f"   {hit}/20000 = {hit/20000:.4f}  (Breite des Fensters / Periode = {2*0.01*x/(np.pi/6):.4f})")
print("\n" + "=" * 96)
