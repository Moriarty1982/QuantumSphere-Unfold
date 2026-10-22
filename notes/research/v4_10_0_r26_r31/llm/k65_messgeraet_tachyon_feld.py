"""k65: Wer misst in der Dynamik von v4.9.0-r27? Tachyon als Messgeraet oder Selbststabilisierung des Feldes.

Vorbefund (Algebra r04): C_HC = (1 + J_B)/2 mit J_B = sigma_x. J_B laesst die Kompensator-Ports fest (Eigenwert +1 auf C,
-1 auf A) und kehrt nur b_z = Re s/2u um. Die Abbildung, die Konvention F (r22) und r21/r27 dem Tachyon zuschreiben
(b -> -b, Ports getauscht, x -> 1/x), ist die Dualitaetsdrehung z -> i z (v4.8.0-r07.2), auf Zustaenden rho -> sy rho sy.

Vorab festgelegte Varianten (alle werden berichtet; Tachyonbild = sy rho sy):
 T1 Tachyon = Bild des Systems, Kopplung "Port A -> W auf dem Tachyon", W in {J_B = sx, T = sz}.
 T2 Tachyon im reinen Bezugszustand auf seiner Kompensatorachse (b = (-1, 0)), W in {J_B, T, C = -1}.
 T3 Tachyon als Reservoir: teilweiser Tausch (theta) mit frischem Tachyon im Bezugszustand, nach jeder pi/6-Drehung.
 T4 Tausch mit dem eigenen Tachyonbild (theta), ohne fremdes Reservoir.
 S1 Feld selbst, zwei Frequenzen, Kickabstand T_b/6 (r13).
 S2 Feld selbst, 40 Frequenzen (Nullstellenhoehen als Uhrfrequenzen, nur Uhrenmodell).
Kriterium Messgeraet: Dekohaerenzfaktor D = 0 (ideal) bzw. |D| < 1. Kriterium selbststabilisierend: Fixpunkt 0 < |b| < 1,
von beliebigen Starts erreicht.
"""
import math
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2); C = (I2 + sx) / 2; A = (I2 - sx) / 2
U = lambda a: np.cos(a) * I2 - 1j * np.sin(a) * sy
rho_of = lambda bx, bz: (I2 + bx * sx + bz * sz) / 2
bvec = lambda r: (np.trace(r @ sx).real, np.trace(r @ sz).real)
tach = lambda r: sy @ r @ sy
a6 = math.pi / 6
SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
ptr = lambda tot: np.einsum("ijkj->ik", tot.reshape(2, 2, 2, 2))

print("0. Vorbefund")
print("   J_B C J_B = C: %s;  sy C sy = A: %s;  J_B: b -> %s;  z -> iz: b -> %s"
      % (np.allclose(sx @ C @ sx, C), np.allclose(sy @ C @ sy, A),
         tuple(round(v, 3) for v in bvec(sx @ rho_of(0.3, 0.5) @ sx)), tuple(round(v, 3) for v in bvec(tach(rho_of(0.3, 0.5))))))

def meter(rho, rhoT, W):
    V = np.kron(C, I2) + np.kron(A, W)
    return ptr(V @ np.kron(rho, rhoT) @ V.conj().T)
coh = lambda r: abs((np.array([1, 1]) / math.sqrt(2)) @ r @ (np.array([1, -1]) / math.sqrt(2)))
rho = U(a6) @ rho_of(1, 0) @ U(a6).conj().T
c0 = coh(rho)
print("\n1. Tachyon als Messgeraet (System nach einer pi/6-Drehung aus R, b = (%.3f, %.3f))" % bvec(rho))
for name, W in (("J_B", sx), ("T", sz)):
    print("   T1 Tachyon = Bild des Systems, Kopplung %-3s: D = %.4f" % (name, coh(meter(rho, tach(rho), W)) / c0))
tR = rho_of(-1, 0)
for name, W in (("J_B", sx), ("T", sz), ("C", -I2)):
    print("   T2 Tachyon im Bezugszustand, Kopplung %-3s: D = %.4f" % (name, coh(meter(rho, tR, W)) / c0))
out = meter(rho, tR, sz)
print("   T2 mit T: Port-Gewichte (%.4f, %.4f) unveraendert -> ideale nicht-selektive Kompensator-Messung"
      % (np.trace(C @ out).real, np.trace(A @ out).real))

def swap(rho, rhoT, th):
    V = math.cos(th) * np.eye(4) - 1j * math.sin(th) * SW
    return ptr(V @ np.kron(rho, rhoT) @ V.conj().T)

print("\n2. T3: Reservoir aus frischen Tachyonen im Bezugszustand, Drehung pi/6 -> Tausch theta")
def t3_fix(th, n=600):
    ends = []
    for b0 in ((1, 0), (0, 1), (-0.6, 0.3), (0.1, -0.9), (0, 0)):
        r = rho_of(*b0)
        for _ in range(n):
            r = swap(U(a6) @ r @ U(a6).conj().T, tR, th)
        ends.append(bvec(r))
    return ends[0], max(math.dist(e, ends[0]) for e in ends)
for th in (math.pi / 12, math.pi / 6, math.pi / 4, math.pi / 3):
    b, sp = t3_fix(th)
    print("   theta = %4.1f Grad: Fixpunkt b = (%+.4f, %+.4f), |b| = %.4f, Streuung ueber Starts %.1e"
          % (math.degrees(th), b[0], b[1], math.hypot(*b), sp))
lo, hi = 0.01, math.pi / 2 - 0.01
f = lambda th: math.hypot(*t3_fix(th, 300)[0])
for target in (0.5, 1 / (0.2375 / (math.log(2) / (math.pi * math.sqrt(3))))):
    a, c = 0.05, math.pi / 2 - 0.05
    if (f(a) - target) * (f(c) - target) < 0:
        for _ in range(40):
            m = (a + c) / 2
            (a, c) = (m, c) if (f(a) - target) * (f(m) - target) > 0 else (a, m)
        print("   |b| = %.4f bei theta = %.3f Grad" % (target, math.degrees((a + c) / 2)))

print("\n3. T4: Tausch mit dem eigenen Tachyonbild")
for th in (math.pi / 12, a6, math.pi / 4):
    r = swap(rho_of(1, 0), tach(rho_of(1, 0)), th)
    print("   theta = %4.1f Grad, aus R: |b| = %.4f = cos 2 theta = %.4f" % (math.degrees(th), math.hypot(*bvec(r)), math.cos(2 * th)))
r = rho_of(0.3, 0.6); r2 = swap(r, tach(r), a6)
print("   allgemeiner Zustand: b = (0.3, 0.6) -> (%.4f, %.4f) = cos(pi/3) b" % bvec(r2))
r = rho_of(1, 0)
for k in range(40):
    r = U(a6) @ r @ U(a6).conj().T; r = swap(r, tach(r), a6)
print("   Drehung pi/6 plus Selbsttausch, 40 Schritte: |b| = %.2e (Fluss zum Photon)" % math.hypot(*bvec(r)))

print("\n4. S1: Feld selbst, zwei Frequenzen")
print("   Kohaerenz |D|^2 nach k Kickabstaenden: " + ", ".join("%d: %.2f" % (k, abs(0.5 * (1 + np.exp(1j * k * math.pi / 3))) ** 2) for k in range(7)))
print("   -> 3/4 nach einem Abstand (derselbe Winkel wie r13, keine unabhaengige Bestaetigung); volle Wiederkehr nach 6: reversibel")

print("\n5. S2: Feld selbst, 40 Frequenzen")
try:
    import mpmath
    g = np.array([float(mpmath.zetazero(n).imag) for n in range(1, 41)])
except Exception:
    g = np.array([14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719, 43.327073, 48.005151, 49.773832])
tau = (2 * math.pi / (g[1] - g[0])) / 6
Ks = [abs(np.mean(np.exp(1j * g * k * tau))) for k in range(50, 5000)]
print("   K nach 1, 6, 30 Abstaenden: %.3f, %.3f, %.3f; Mittel 50..5000: %.3f (1/sqrt N = %.3f), Maximum %.3f"
      % tuple([abs(np.mean(np.exp(1j * g * k * tau))) for k in (1, 6, 30)] + [np.mean(Ks), 1 / math.sqrt(len(g)), max(Ks)]))
