"""OP1, Setzung (S2) rueckwaerts: Gibt es im Bestand einen Grund, warum T Straenge fermionisch und M bosonisch liest?
(Erkundung, nicht blind.)

Notwendige Bedingungen an einen Mechanismus (aus r17.5, r17.6, H98):
 N1  Er muss auf dem AUSTAUSCH von Straengen wirken (Sym gegen Lambda), nicht nur auf einem einzelnen Strang.
 N2  Er muss M und T unterscheiden, also von der Tachyon-Abbildung R vertauscht werden (wie die Ports C, A, r28).
 N3  Er darf nicht auf Kramers fuehren (alle halbzahligen j; beta = 0,337 ausgeschlossen).
Kandidaten aus dem Bestand:
 K1  Frame-Abbildungen R, T, J_B je Strang (r17.6: vertauschen mit dem Austausch).
 K2  R^2 = -1 (r17.6: Kramers).
 K3  Port-Paritaet J (C = (1+J)/2 "bosonisch", A = (1-J)/2 "fermionisch", thm:origin(ii), T11): J_B auf (F+, F-).
 K4  Kompensator strangweise (r23.2: selektive Projektion macht rein): C^{(x)n} auf einem Buendel.
"""
import itertools
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
rng = np.random.default_rng(1116)


def swap(n, i, j):
    d = 2 ** n; S = np.zeros((d, d))
    for idx in itertools.product(range(2), repeat=n):
        k = list(idx); k[i], k[j] = k[j], k[i]
        S[int(''.join(map(str, k)), 2), int(''.join(map(str, idx)), 2)] = 1
    return S


def kron(*ms):
    out = np.eye(1)
    for m in ms: out = np.kron(out, m)
    return out


# K3: J_B = (E, B) -> (B, E) auf den Helizitaetsanteilen F+ = E + iB, F- = E - iB
E, B = rng.normal(size=3), rng.normal(size=3)
Fp, Fm = E + 1j * B, E - 1j * B
Fp2, Fm2 = B + 1j * E, B - 1j * E
print("(K3) J_B auf (F+, F-): F+ -> i F-:", np.allclose(Fp2, 1j * Fm), "; F- -> -i F+:", np.allclose(Fm2, -1j * Fp))
print("     also J_B = sigma_y auf dem Helizitaets-Dublett eines Strangs (nach Umphasung F- -> i F-: sigma_x, ein Tausch der")
print("     beiden Helizitaetskomponenten EINES Feldes, kein Tausch zweier Straenge)")

# K1/K3: Wirkung je Strang vertauscht mit dem Strangtausch, fuer n = 2, 3
for n in (2, 3):
    ok = all(np.allclose(kron(*[U] * n) @ swap(n, 0, 1), swap(n, 0, 1) @ kron(*[U] * n)) for U in (sx, sy, sz))
    print(f"(K1/K3) n = {n}: jede strangweise Abbildung U^(x)n vertauscht mit dem Strangtausch: {ok} -> Sym und Lambda bleiben getrennt")

# Lambda^n und Sym^n eines Dubletts
for n in (1, 2, 3):
    P = np.zeros((2 ** n, 2 ** n)); perms = list(itertools.permutations(range(n)))
    for p in perms:
        sign = np.linalg.det(np.eye(n)[list(p)])
        M = np.eye(2 ** n)
        # Permutationsoperator aus Transpositionen
        cur = list(range(n)); Pm = np.eye(2 ** n)
        for i in range(n):
            j = cur.index(p[i])
            if j != i:
                Pm = swap(n, i, j) @ Pm; cur[i], cur[j] = cur[j], cur[i]
        P += sign * Pm
    P /= len(perms)
    print(f"     dim Lambda^{n}(C^2) = {round(np.trace(P).real)}, dim Sym^{n}(C^2) = {n + 1}")

# K4: Kompensator strangweise auf einem Buendel
C = (np.eye(2) + sx) / 2; A = (np.eye(2) - sx) / 2
n = 3; psi = rng.normal(size=2 ** n) + 1j * rng.normal(size=2 ** n); psi /= np.linalg.norm(psi)
out = kron(C, C, C) @ psi
c = np.array([1, 1]) / np.sqrt(2)
aligned = kron(c[:, None], c[:, None], c[:, None]).ravel()
print(f"(K4) C^(x)3 auf einem beliebigen 3-Strang-Zustand: Bild parallel zu |c>^(x)3 (ausgerichtetes Buendel):"
      f" {np.isclose(abs(np.vdot(aligned, out)), np.linalg.norm(out))}")
print(f"     Bild liegt in Sym^3: {np.allclose(swap(3, 0, 1) @ out, out) and np.allclose(swap(3, 1, 2) @ out, out)};"
      " mit A^(x)3 entsprechend |a>^(x)3: beide Ports geben ausgerichtete, symmetrische Buendel, nie Lambda^n")
