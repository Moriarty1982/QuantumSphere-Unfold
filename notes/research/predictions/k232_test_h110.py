"""k232: Test H110 (Vorab-Notiz Vorab_Notiz_H110_Betrachter_HS7_Haelfte.md).

Betrachter o = koharenter Zustand auf +-n (n = (1,1,1)/sqrt3); Auslesungen e_k = +1-Eigenzustaende von sigma_z, sigma_x, sigma_y.
HS(7)-Haelfte {1, F}: |Phi_F> ~ |e_F>|o> + |o>|e_F>; rho_F = Tr_Betrachter.
Varianten: A nur R gepaart; B alle gepaart; C Mittel 1/3 Paar + 2/3 rein.
Vorhersage: phi = |arg Tr(rho0 rho1 rho2)|, K = Tr S^2 / (Tr S)^2, S = sum rho.
Treffer: |phi - 0.666665| <= 2e-4 und |K - 2/3| <= 1e-3.
"""
import numpy as np

TARGET, TOL, KTOL = 0.666665, 2e-4, 1e-3
n = np.ones(3) / np.sqrt(3)
E = [np.array(v, float) for v in ([0, 0, 1], [1, 0, 0], [0, 1, 0])]


def coh(v):
    v = np.asarray(v, float) / np.linalg.norm(v)
    th, ph = np.arccos(np.clip(v[2], -1, 1)), np.arctan2(v[1], v[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def pure(v):
    return np.outer(v, v.conj())


def pair_reduced(e, o, sign=+1):
    phi = np.kron(e, o) + sign * np.kron(o, e)
    phi = phi / np.linalg.norm(phi)
    M = phi.reshape(2, 2)                       # Index 1 = Auslesung, Index 2 = Betrachter
    return M @ M.conj().T


def K_phase(rho):
    S = sum(rho)
    return np.trace(S @ S).real / np.trace(S).real ** 2, abs(np.angle(np.trace(rho[0] @ rho[1] @ rho[2])))


def states(variant, s, paired_index=0, sign=+1):
    o = coh(s * n); ek = [coh(e) for e in E]
    pr = [pair_reduced(ek[k], o, sign) for k in range(3)]
    if variant == "A":
        return [pr[k] if k == paired_index else pure(ek[k]) for k in range(3)]
    if variant == "B":
        return pr
    if variant == "C":
        return [pr[k] / 3 + 2 * pure(ek[k]) / 3 for k in range(3)]
    if variant == "rein":
        return [pure(e) for e in ek]


K0, p0 = K_phase(states("rein", +1)); print(f"Kontrolle rein: K = {K0:.6f}, phi = {p0:.6f}")
Ks, ps = K_phase(states("B", +1, sign=-1)); print(f"Kontrolle Singulett (B, +n): K = {Ks:.6f}, phi = {ps:.6f}")
hits, attempts = [], 0
for variant in ("A", "B", "C"):
    for s, sname in ((+1, "+n"), (-1, "-n")):
        K, ph = K_phase(states(variant, s)); attempts += 1
        ok = abs(ph - TARGET) <= TOL and abs(K - 2 / 3) <= KTOL
        if ok: hits.append(f"{variant}{sname}")
        extra = ""
        if variant == "A":
            alt = [K_phase(states("A", s, paired_index=j)) for j in (1, 2)]
            extra = f" | Kontrolle T/J_B gepaart: " + ", ".join(f"K = {a:.6f}, phi = {b:.6f}" for a, b in alt)
        print(f"{variant} {sname}: K = {K:.6f} (K - 2/3 = {K - 2/3:+.6f}), phi = {ph:.6f} (phi - Ziel = {ph - TARGET:+.6f})"
              + ("  -> TREFFER" if ok else "") + extra)
verdict = "bestaetigt" if len(hits) == 1 else ("mehrdeutig" if hits else "widerlegt")
print(f"Versuche: {attempts}; Treffer: {hits}; Urteil: {verdict}")
