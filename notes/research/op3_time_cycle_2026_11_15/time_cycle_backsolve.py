"""Rueckwaertssuche: Zeitverschiebung um ein Drittel der Periode von s(t) als Dreierzyklus auf S (Erkundung, nicht blind).

Vorab im Skript festgelegt (vor dem ersten Lauf):
- Zyklus U = diag(w^-1, 1, w) auf den Anteilen (s+, w, conj s-), w = e^{2 pi i/3}. Ein Zustand mit Gewichten (p-, p0, p+)
  (p- auf s+, p+ auf conj s-; Konvention) hat <psi|U psi> = p0 + p- w^-1 + p+ w. Bargmann-Phase der Bahn = 3 arg <psi|U psi>.
- Ziel: |<psi|U psi>|^2 = 1/2 (Koide) und Bargmann-Phase phi = 2/3 (Projektkonvention r14.5; Brannen delta = 2/9).
  Zum Vergleich auch delta aus Massen (PDG 2024: m_e, m_mu, m_tau = 1776.86 MeV).
- Zwei Skalarprodukte, beide gerechnet, keines nachtraeglich bevorzugt:
  HS (Spin-1-Darstellung): p ~ (|s+|^2, 2|w|^2, |s-|^2);  Parseval (Zeitsignal s(t)): p ~ (|s+|^2, 4|w|^2, |s-|^2).
- Abgeleitete Groessen (genau diese vier, je Skalarprodukt dort, wo sie abhaengen):
  P0 = p0;  A = (p+ - p-)/(p+ + p-) (Helizitaets-Asymmetrie);  r = |s-|/|s+|;  c = |w|^2/(|s+||s-|) (c = 1: Rang 1 moeglich).
- Kandidaten (vorab, 24 Werte): gamma_M, gamma_T, gamma_L, 1/gamma_L, beta_sym, beta_sym^2, eta_sym, 2 eta_sym, tanh(2 eta),
  e^-2eta, 1/3, 2/3, 1/2, 1/4, 3/4, 1/sqrt2, sqrt2 - 1, 2 - sqrt2, 1/sqrt3, sqrt(2/3), (1+sqrt2)/3, 2/9, pi/4 - 2/3, gamma_M/2.
  Treffer: relative Abweichung <= 0,5 %. Zufallserwartung ueber dieselbe Liste bei gleichverteilten Zielwerten im
  Bereich der Kandidaten wird mit angegeben.
"""
import numpy as np

W3 = np.exp(2j * np.pi / 3)
GAMMA_M, GAMMA_T = 0.237533, np.log(2) / (np.pi * np.sqrt(3))
GAMMA_L = GAMMA_M / GAMMA_T
two_eta = np.arccosh(GAMMA_L); eta = two_eta / 2; beta = np.tanh(eta)
cands = {"gamma_M": GAMMA_M, "gamma_T": GAMMA_T, "gamma_L": GAMMA_L, "1/gamma_L": 1 / GAMMA_L, "beta_sym": beta,
         "beta_sym^2": beta ** 2, "eta_sym": eta, "2 eta_sym": two_eta, "tanh 2eta": np.tanh(two_eta), "e^-2eta": np.exp(-two_eta),
         "1/3": 1 / 3, "2/3": 2 / 3, "1/2": .5, "1/4": .25, "3/4": .75, "1/sqrt2": 2 ** -.5, "sqrt2-1": 2 ** .5 - 1,
         "2-sqrt2": 2 - 2 ** .5, "1/sqrt3": 3 ** -.5, "sqrt(2/3)": (2 / 3) ** .5, "(1+sqrt2)/3": (1 + 2 ** .5) / 3,
         "2/9": 2 / 9, "pi/4-2/3": np.pi / 4 - 2 / 3, "gamma_M/2": GAMMA_M / 2}


def weights(delta):
    p0 = (1 + np.sqrt(2) * np.cos(delta)) / 3
    d = np.sqrt(2 / 3) * np.sin(delta)            # p+ - p-
    return (1 - p0 - d) / 2, p0, (1 - p0 + d) / 2


def delta_from_masses(me, mmu, mtau):
    r = np.sqrt([me, mmu, mtau]); a = r.mean(); b = r / a - 1     # sqrt m_k = a (1 + sqrt2 K cos(delta + 2 pi k/3))
    c = np.fft.fft(b) / 3; return np.angle(c[1]), np.sqrt(2) * abs(c[1]) * 1  # Phase und Amplitude (Konvention)


for label, delta in (("phi = 2/3 (delta = 2/9)", 2 / 9),):
    pm, p0, pp = weights(delta)
    g = p0 + pm / W3 + pp * W3
    print(f"[{label}] Gewichte p- = {pm:.6f}, p0 = {p0:.6f}, p+ = {pp:.6f}; |<psi|U psi>|^2 = {abs(g)**2:.6f},"
          f" Bargmann-Phase 3 arg = {3*np.angle(g):.6f}")
    # Kontrolle: Gram-Matrix der Bahn und Koide
    psi = np.sqrt([pm, p0, pp]).astype(complex); U = np.diag([1 / W3, 1, W3])
    states = [psi, U @ psi, U @ U @ psi]
    G = np.array([[np.vdot(a, b) for b in states] for a in states])
    ev = np.sort(np.linalg.eigvalsh(G))
    print(f"    Kontrolle: Eigenwerte der Gram-Matrix {np.round(ev, 6)}, K = {np.sum(ev**2)/np.sum(ev)**2:.6f},"
          f" Verhaeltnisse der Quadrate 1 : {ev[1]**2/ev[0]**2:.2f} : {ev[2]**2/ev[0]**2:.2f}")
    A = (pp - pm) / (pp + pm); r = np.sqrt(pm / pp)
    derived = {"P0": p0, "A": A, "r": r}
    for name, f in (("HS", 2), ("Parseval", 4)):
        # p ~ (|s+|^2, f |w|^2, |s-|^2) -> |w|^2 / (|s+||s-|) = (p0/f) / sqrt(p- p+)
        derived[f"c_{name}"] = (p0 / f) / np.sqrt(pm * pp)
    print("    abgeleitete Groessen: " + ", ".join(f"{k} = {v:.6f}" for k, v in derived.items()))
    hits = []
    for k, v in derived.items():
        for cn, cv in cands.items():
            if abs(v / cv - 1) <= 0.005: hits.append((k, cn, v, cv))
    print(f"    Treffer (<= 0,5 %): {hits if hits else 'keine'}")
    # Zufallserwartung: Anteil der logarithmischen Achse, den 24 Fenster von +-0,5 % abdecken, im Bereich der Kandidaten
    lo, hi = min(cands.values()), max(cands.values())
    cover = len(cands) * np.log(1.005 / 0.995) / np.log(hi / lo)
    print(f"    Zufallserwartung je abgeleiteter Groesse im Bereich [{lo:.3f}, {hi:.3f}]: {cover:.3f};"
          f" fuer {len(derived)} Groessen: {len(derived)*cover:.2f}")

dm, amp = delta_from_masses(0.51099895, 105.6583755, 1776.86)
dm = np.mod(abs(dm), 2 * np.pi / 3)   # Nummerierung der Generationen verschiebt delta um Vielfache von 2 pi/3
print(f"\nZum Vergleich aus Massen (PDG 2024): delta = {abs(dm):.6f} (2/9 = {2/9:.6f}), Bargmann-Phase 3 delta = {3*abs(dm):.6f}")
