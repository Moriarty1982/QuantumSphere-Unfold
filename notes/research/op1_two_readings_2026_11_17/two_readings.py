"""Lesart (H) gegen (B) der Registerbreite b, an denselben Feldern; dazu die Kandidatenliste fuer (B).  (Erkundung, nicht blind.)

(H) Helizitaetsbreite: b_H = (|s+| - |s-|)/(|s+| + |s-|) aus den komplexen Amplituden (s+- = F+-.F+-), Lorentz-invariant (r16.3).
(B) Beobachtergroesse: phi = |s|/(|E|^2 + |B|^2) mit s = (E + iB)^2 fuer reelle Momentanfelder (r21.8: phi = sech 2 eta_R; R: phi = 1, P: phi = 0).
Bestandsaussagen, gegen die geprueft wird:
  S1 (r21.8c): R = Frame mit E || B, phi = 1, reiner Zustand.   S2 (r21.8c, r69.1): P = Nullfeld, phi = 0, maximal gemischt.
  S3 (Konvention F, r22): M und T haben dieselbe Sichtbarkeit |b| = b_M; T = J_B-Bild (Ports getauscht).
  S4 (r16.3, r16.7): die Breite auf chi ist beobachterunabhaengig.
"""
import numpy as np

def boost(E, B, n, v):
    g = 1 / np.sqrt(1 - v * v)
    return (g * (E + v * np.cross(n, B)) - (g - 1) * np.dot(n, E) * n,
            g * (B - v * np.cross(n, E)) - (g - 1) * np.dot(n, B) * n)

def bH(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    a, c = abs(Fp @ Fp), abs(Fm @ Fm)
    return np.nan if a + c < 1e-14 else (a - c) / (a + c)

def phiB(E, B):   # nur fuer reelle Momentanfelder
    s = (E + 1j * B) @ (E + 1j * B)
    return abs(s) / (E @ E + B @ B)

beta = 0.549406; eta = np.arctanh(beta); bM = 1 / np.cosh(2 * eta)
x, y, z = np.eye(3)
E_R, B_R = 1.0 * x, 0.4 * x                      # E || B: Bezugsframe R (r21.8c)
E_M, B_M = boost(E_R, B_R, z, beta)               # Beobachter mit Rapiditaet eta
E_T, B_T = B_M.copy(), E_M.copy()                 # J_B-Bild
E_P, B_P = 1.0 * x, 1.0 * y                       # ebene Welle (Nullfeld, Momentanwert)
E_sd, B_sd = np.array([1, 0.3j, 0]), -1j * np.array([1, 0.3j, 0])   # selbstdual, komplexe Amplitude (F- = 0)
rows = [("R (E || B, reell)", E_R, B_R, True), ("M (R geboostet, eta)", E_M, B_M, True), ("T (J_B-Bild von M)", E_T, B_T, True),
        ("P (Nullfeld)", E_P, B_P, True), ("Pol (selbstdual, komplex)", E_sd, B_sd, False)]
print(f"b_M = 1/gamma_L = {bM:.4f}")
print("Feld | (B) phi | (H) b_H")
for name, E, B, real in rows:
    print(f"{name:28s} | {phiB(E, B) if real else float('nan'):.4f} | {bH(E, B):.4f}")
print("Bestandsaussagen: S1 R hat Breite 1 (rein); S2 P hat 0; S3 |b_M| = |b_T| = 0,5363; S4 Breite beobachterunabhaengig.")
print("  (B): S1 ja (phi = 1), S2 ja (0), S3 ja (0,5363 fuer M und T), S4 nein (phi haengt vom Beobachter ab).")
print("  (H): S1 nein (reelles R liegt bei 0 = Lage von P), S2 unbestimmt (Nullfeld ohne Punkt), S3 nein fuer reelle Felder (0), S4 ja.")

# Kandidatenliste (B)
target = beta
cands = [("1 Photonring-Kreisbahn", 1.0), ("2 ISCO-Kreisbahn", 0.5), ("3 freier Fall bei 6M", 1 / np.sqrt(3)),
         ("4 freier Fall bei 3M", np.sqrt(2 / 3)), ("5 marginal gebundene Kreisbahn 4M", 1 / np.sqrt(2)),
         ("6 freier Fall bei 4M", 1 / np.sqrt(2)), ("7 Energiedichte x2", np.tanh(0.5 * np.arccosh(2))),
         ("9a tanh(gamma_M)", np.tanh(0.237533)), ("9b tanh(gamma_P)", np.tanh(0.274067))]
hits = 0
print(f"Kandidatenliste (B), Ziel v = {target:.6f}, Treffer bei rel. Abstand <= 1e-3:")
for nme, v in cands:
    d = abs(v - target) / target; hits += d <= 1e-3
    print(f"  {nme:36s} {v:.6f}  rel. Abstand {d:.3f}{'  TREFFER' if d <= 1e-3 else ''}")
print(f"Treffer: {hits} von {len(cands)}")
