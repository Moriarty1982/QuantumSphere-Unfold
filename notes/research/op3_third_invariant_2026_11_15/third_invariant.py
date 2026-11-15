"""Die dritte Lorentz-Invariante w = F+ . conj(F-) und die invariante Matrix S (Erkundung, nicht blind).

Fuer zeitharmonische Felder mit komplexen Amplituden E, B (E(t) = Re(E e^{-i w t}) usw.), F+- = E +- iB.
(1) Invarianz von s+, s-, w unter Boosts; F+.F- nicht invariant. Generische Bahndimension (Zahl der Invarianten).
(2) s(t) = (E(t) + i B(t))^2 = [s+ e^{-2iwt} + 2w + conj(s-) e^{2iwt}] / 4.
(3) S = Phi^T Phi mit Phi = [F+, conj F-] ist die komplexe symmetrische 2x2-Matrix [[s+, w], [w, conj s-]]; unter Boosts
    Phi -> M Phi (M in SO(3,C)), also S invariant. Wirkung von Dualitaet, Zeitverschiebung, R, T, J_B auf S.
(4) Rang von S: die sechs Pole von r16.7 haben Rang 1 (koharenter Sektor); allgemeine komplexe Felder Rang 2.
    Takagi-Werte sigma1 >= sigma2 >= 0 (S = U diag(sigma) U^T) als Mass der Abweichung vom Rang 1.
"""
import numpy as np

rng = np.random.default_rng(1527)


def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    return (g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n,
            g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n)


def parts(E, B):
    return E + 1j * B, E - 1j * B


def S_of(E, B):
    Fp, Fm = parts(E, B); Phi = np.column_stack([Fp, np.conj(Fm)]); return Phi.T @ Phi


def rnd():
    return rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)


# (1)
dev = np.zeros(4)
for _ in range(400):
    E, B = rnd(); Fp, Fm = parts(E, B); a = np.array([Fp @ Fp, Fm @ Fm, Fp @ np.conj(Fm), Fp @ Fm])
    E2, B2 = boost(E, B, rng.uniform(.05, .95), rng.normal(size=3)); Gp, Gm = parts(E2, B2)
    b = np.array([Gp @ Gp, Gm @ Gm, Gp @ np.conj(Gm), Gp @ Gm]); dev = np.maximum(dev, abs(a - b) / max(1, abs(a).max()))
print(f"(1) rel. Abweichung unter 400 Boosts: s+ {dev[0]:.1e}, s- {dev[1]:.1e}, w {dev[2]:.1e}; F+.F- {dev[3]:.1e} (nicht invariant)")
E, B = rnd()
def gen(k):
    e = np.eye(3)[k % 3]
    return (np.cross(e, E), np.cross(e, B)) if k < 3 else (np.cross(e, B), -np.cross(e, E))
Tm = np.array([np.concatenate([np.r_[x.real, x.imag] for x in gen(k)]) for k in range(6)])
r = np.linalg.matrix_rank(Tm, 1e-9)
print(f"    generische Bahndimension {r} von 12 reellen -> {12 - r} reelle Invarianten = Re/Im von s+, s-, w")

# (2)
Fp, Fm = parts(E, B); sp, sm, w = Fp @ Fp, Fm @ Fm, Fp @ np.conj(Fm); err = 0
for t in np.linspace(0, 7, 60):
    z = (E * np.exp(-1j * t)).real + 1j * (B * np.exp(-1j * t)).real
    err = max(err, abs(z @ z - (sp * np.exp(-2j * t) + 2 * w + np.conj(sm) * np.exp(2j * t)) / 4))
print(f"(2) s(t) = [s+ e^(-2iwt) + 2w + conj(s-) e^(2iwt)]/4: max. Abweichung {err:.1e}")

# (3)
S = S_of(E, B)
print(f"(3) S = [[s+, w], [w, conj s-]]: {np.allclose(S, [[sp, w], [w, np.conj(sm)]])}; symmetrisch: {np.allclose(S, S.T)}")
al = 0.37
Sd = S_of(*(lambda F: ((F[0] + F[1]) / 2, (F[0] - F[1]) / 2j))((np.exp(-1j * al) * Fp, np.exp(1j * al) * Fm)))
print(f"    Dualitaet um alpha: S -> e^(-2i alpha) S (Skalar): {np.allclose(Sd, np.exp(-2j * al) * S)}")
tau = 0.53; U = np.diag([np.exp(-1j * tau), np.exp(1j * tau)])
St = S_of(E * np.exp(-1j * tau), B * np.exp(-1j * tau))
print(f"    Zeitverschiebung um tau: S -> U S U mit U = diag(e^(-i tau), e^(i tau)) (Gewichte -1, 0, +1 auf s+, w, conj s-):"
      f" {np.allclose(St, U @ S @ U)}")
maps = {"R": lambda E, B: (-B, E), "T": lambda E, B: (E, -B), "J_B": lambda E, B: (B, E)}
X = np.array([[0, 1], [1, 0]])
print(f"    R: S -> -S: {np.allclose(S_of(*maps['R'](E, B)), -S)}")
print(f"    T: S -> X conj(S) X (antilinear, tauscht s+ und conj s-): {np.allclose(S_of(*maps['T'](E, B)), X @ np.conj(S) @ X)}")
print(f"    J_B: S -> -X conj(S) X: {np.allclose(S_of(*maps['J_B'](E, B)), -X @ np.conj(S) @ X)}")

# (4)
e1 = np.array([1, 0, 0.])
poles = {"Materie": (e1, 0 * e1), "Tachyon": (0 * e1, e1), "Seite+": (e1 / np.sqrt(2), e1 / np.sqrt(2)),
         "Seite-": (e1 / np.sqrt(2), -e1 / np.sqrt(2)), "selbstdual": (1j * e1, e1), "antiselbstdual": (-1j * e1, e1)}
def takagi(S):
    sv = np.linalg.svd(S, compute_uv=False); return sv  # Takagi-Werte = Singulaerwerte einer komplexen symmetrischen Matrix
for k, (E0, B0) in poles.items():
    Sk = S_of(E0, B0); print(f"(4) {k:15s}: S = {np.round(Sk, 3).tolist()}, Takagi-Werte {np.round(takagi(Sk), 4)}")
print("    Materie und Tachyon: S und -S, also derselbe Strahl; das Vorzeichen steckt nur in den Wurzeln (chi, r16.3)")
r2 = [ (lambda s: s[1] / s[0])(takagi(S_of(*rnd()))) for _ in range(2000)]
print(f"    zufaellige komplexe Felder: sigma2/sigma1 im Mittel {np.mean(r2):.3f}, Minimum {np.min(r2):.3f} -> generisch Rang 2")
