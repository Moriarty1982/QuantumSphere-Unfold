"""K13 / r10: Was sagt Lesart B ueber die Koide-Struktur der Leptonmassen?

(1) Identitaet: Brannen-Form  sqrt(m_k) = A(1 + sqrt2 cos(theta + 2 pi k/3))  ist exakt
      v = t*(1,1,1) + sqrt2 * Re( c*(1, w, w^2) ),   t = A, c = |c| e^{i theta}, w = e^{2 pi i/3},
    also Skalar t plus Realteil einer symmetrischen Triole. K = 2/3  <=>  |c| = t.
(2) Lesart-B-Bedingungen fuer q = it + sum z_k e_k mit z = c(1,w,w^2):
      s = sum z_k^2 = 0 (immer), N(q) = -t^2 (immer)  -> weder |c|/t noch arg c werden festgelegt.
(3) Gegenprobe: kanonische Winkel der Struktur gegen delta_obs = theta_obs - 2pi/3.
    Die Liste wird VOR dem Vergleich festgelegt; der Vergleich ist eine Nachhersage, keine Vorhersage.
(4) Einfachste Lorentz-invariante Lagrangedichte in Lesart B: Re(e^{-i phi} s) = cos(phi)(E^2-B^2) + sin(phi) 2E.B;
    eine Dualitaetsdrehung z -> e^{i a} z verschiebt phi um 2a.
"""
import numpy as np

w = np.exp(2j*np.pi/3); k = np.arange(3)
me, mmu, mtau = 0.51099895, 105.6583755, 1776.93
v = np.sqrt([me, mmu, mtau])

# (1) Identitaet pruefen: aus v die Triolen-Darstellung gewinnen (diskrete Fourier-Zerlegung)
t = v.mean()
c = np.sum(v*np.conj(w**k))/3*2/np.sqrt(2)          # erster Fourier-Modus, so normiert, dass v = t + sqrt2 Re(c w^k)
rec = t + np.sqrt(2)*np.real(c*w**k)
K = v@v/v.sum()**2
print("(1) Rekonstruktion v = t + sqrt2 Re(c w^k):", np.allclose(rec, v))
print(f"    t = {t:.6f}, |c| = {abs(c):.6f}, |c|/t = {abs(c)/t:.6f}  (K = 2/3 <=> |c|/t = 1);  K = {K:.7f}")
th = np.angle(c) % (2*np.pi)
cands = sorted(((th + 2*np.pi*j/3) % (2*np.pi) for j in range(3)))
d_obs = min((x - 2*np.pi/3) % (2*np.pi/3) for x in cands)
print(f"    arg c = {th:.6f} rad; Phase modulo 2pi/3: delta_obs = {d_obs:.6f} (2/9 = {2/9:.6f})")

# Allgemein: |c|/t vs K
r = np.linspace(0.5, 1.5, 5)
print("    K als Funktion von |c|/t:", [round((1 + r_**2)/3, 4) for r_ in r], "fuer |c|/t =", list(r))

# (2) Lesart-B-Bedingungen
z = c*w**k
print(f"(2) s = sum z^2 = {np.round(np.sum(z**2), 12)}  (null fuer jede Triole);  N(q) = -t^2 + s = {-t**2:.4f}")
print("    -> |c|/t und arg c sind durch s und N(q) nicht festgelegt.")

# (3) Kanonische Winkel der Struktur (vorher festgelegte Liste)
gL = 0.2375/(np.log(2)/(np.pi*np.sqrt(3))); b = np.sqrt((gL - 1)/(gL + 1))
canon = {f"{j}pi/12": j*np.pi/12 for j in range(0, 8)}
canon.update({"theta_H/2 = arcsin(bsym)": np.arcsin(b), "theta_H": 2*np.arcsin(b),
              "theta_H,sym/2 = arcsin(1/sqrt3)": np.arcsin(1/np.sqrt(3)), "theta_H,sym": 2*np.arcsin(1/np.sqrt(3)),
              "arctan(bsym)": np.arctan(b), "bsym (rad)": b, "1/sqrt3 (rad)": 1/np.sqrt(3),
              "pi - sqrt2 arcsin(bsym) - 2pi/3 (P2)": np.pi - np.sqrt(2)*np.arcsin(b) - 2*np.pi/3,
              "arccos(1/3)/... Tetraeder 109.47 deg": np.arccos(-1/3), "magischer Winkel arccos(1/sqrt3)": np.arccos(1/np.sqrt(3))})
print("(3) Kanonische Winkel, reduziert modulo 2pi/3, gegen delta_obs =", round(d_obs, 6))
dd = 0.0004*np.pi/180                                  # Messfehler aus r09 (0.0004 Grad)
rows = []
for name, a in canon.items():
    red = a % (2*np.pi/3)
    rows.append((abs(red - d_obs), name, red))
for diff, name, red in sorted(rows)[:6]:
    print(f"    {name:42s} -> {red:.6f}   Abstand {diff:.6f} rad = {diff/dd:.0f} sigma")

# (4) Lagrangedichte und Dualitaet
E = np.array([0.3, -1.1, 0.5]); B = np.array([0.9, 0.2, -0.4]); zz = E + 1j*B
for phi in (0, np.pi/2):
    L = np.real(np.exp(-1j*phi)*np.sum(zz**2))
    print(f"(4) phi = {phi:.3f}: Re(e^-i phi s) = {L:.4f};  cos(phi)(E^2-B^2) + sin(phi)2E.B = {np.cos(phi)*(E@E-B@B) + np.sin(phi)*2*(E@B):.4f}")
a = 0.37
print("    Dualitaetsdrehung z -> e^{ia} z: Re(e^{-i phi} s') = Re(e^{-i(phi-2a)} s):",
      np.isclose(np.real(np.exp(-1j*0.5)*np.sum((np.exp(1j*a)*zz)**2)), np.real(np.exp(-1j*(0.5 - 2*a))*np.sum(zz**2))))
