"""k55: Warum sechs Kicks pro Schwebung? Auslese-Richtungen aus Triole und Umkehrwalze (Erkundung K8, Deutung).

In der s-Ebene (s = z.z, arg s = 2 alpha): Triole arg s in {0, 120, 240} Grad (r06.2: Phasen 1, w, w^2);
J_B (r02.3) wirkt als s -> -conj(s). Vereinigung = Sechseck. Geprueft: Sechseck, Stufenwinkel, Schwebung = ein Umlauf von s.
"""
import cmath
import math

tri = [cmath.exp(2j * math.pi * k / 3) for k in range(3)]
img = [-z.conjugate() for z in tri]
ang = lambda z: round(math.degrees(cmath.phase(z)) % 360, 6)
S = sorted(set(ang(z) for z in tri + img))
print("1. Triole in der s-Ebene:", sorted(ang(z) for z in tri), "Grad")
print("   J_B-Bild (s -> -conj s):", sorted(ang(z) for z in img), "Grad")
print("   Vereinigung:", S, "-> Sechseck, Abstand 60 Grad in arg s = 30 Grad im Dualitaetswinkel")
print("   enthaelt Materie (0) und Tachyon (180):", 0.0 in S and 180.0 in S)

print("\n2. Stufenfaktor beim Durchlaufen der Richtungen: cos^2(Dualitaetsschritt)")
for name, step in (("nur Triole (120 Grad in s)", 60.0), ("Triole + J_B (60 Grad in s)", 30.0), ("Viertelraster (90 Grad in s)", 45.0)):
    print("   %-30s Dualitaetsschritt %4.0f Grad -> q = %.4f" % (name, step, math.cos(math.radians(step)) ** 2))

print("\n3. Ein Umlauf von s um das Photon (arg s: 0 -> 360) = 6 Kicks = Dualitaet pi = z -> -z (r02) = eine Schwebung (r13)")
z = 1 + 0j
for k in range(6):
    z *= cmath.exp(1j * math.pi / 6)
print("   z nach 6 Dualitaetsschritten zu 30 Grad:", complex(round(z.real, 12), round(z.imag, 12)))

print("\n4. (Bemerkung) Wurzelsystem A2 von SU(3): 6 Wurzeln im Abstand 60 Grad, Weylgruppe S3 = Triole-Permutationen")
