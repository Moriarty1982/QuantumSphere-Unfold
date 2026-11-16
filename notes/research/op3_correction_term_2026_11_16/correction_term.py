"""Zeitabhaengiger Korrekturterm, rueckwaerts rekonstruiert (Methoden_Notiz.md, festgelegt vor der Rechnung, Commit 85e975b).

Basis (s+, w, s-bar) = m = (+1, 0, -1); H0 = 2 diag(-1, 0, +1) (r16.8); Zyklus U = diag(w-bar, 1, w) (r16.9).
phi = 3 arg sum_k p_k u_k, K = sum p_k^2 (nur Populationen).
Unitaer: H = H0 + sum u_k G_k, G = {Jx, Jy, Q1, Q2}; dissipativ: Raten gamma_k >= 0 fuer J-, J+, J-^2, J+^2 (Ratengleichung der Populationen).
Hauptlauf: minimaler Eingriff; V1 glattester Verlauf; V2 tau = pi/3, 3 pi; V3 Start S1, S2.  200 Schritte, 20 Zufallsstarts.
Aufruf: python correction_term.py [--quick]
"""
import json
import sys
import numpy as np
from scipy.optimize import minimize

QUICK = "--quick" in sys.argv
N = 200
RESTARTS = 4 if QUICK else 20
PHI_T, EPS_K, EPS_PHI = 0.666674, 1e-4, 2e-4
W3 = np.exp(2j * np.pi / 3)
UC = np.array([np.conj(W3), 1, W3])
H0 = 2 * np.diag([-1.0, 0.0, 1.0]).astype(complex)

s2 = np.sqrt(2)
Jp = np.array([[0, s2, 0], [0, 0, s2], [0, 0, 0]], complex)       # J+ in Basis m = +1, 0, -1
Jm = Jp.conj().T
Jx, Jy = (Jp + Jm) / 2, (Jp - Jm) / 2j
Q1, Q2 = (Jp @ Jp + Jm @ Jm) / 2, (Jp @ Jp - Jm @ Jm) / 2j
GEN = [Jx, Jy, Q1, Q2]
GNAMES = ["D1 Jx", "D2 Jy", "Q1", "Q2"]
CONST = {"gamma_M/2": 0.237533 / 2, "gamma_M": 0.237533, "pi/4 - phi_t": np.pi / 4 - PHI_T, "gamma_T/2": 0.127384 / 2,
         "1/(4 pi)": 1 / (4 * np.pi)}


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def phi_K(p):
    z = np.sum(p * UC)
    return wrap(3 * np.angle(z)), np.sum(p ** 2), z


def pops_from_argz(a):
    """Populationen auf dem Kreis K = 2/3 mit arg(sum p u) = a: sum p u = e^{i a}/sqrt2, sum p = 1."""
    z = np.exp(1j * a) / np.sqrt(2)
    A = np.array([UC.real, UC.imag, np.ones(3)])
    return np.linalg.solve(A, [z.real, z.imag, 1.0])


def coherent(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([c * c, np.sqrt(2) * c * s, s * s], complex)


# Nachtrag zur Methoden-Notiz (vor der Rechnung): Ziel und S2 im selben Sektor (derselben zyklischen Benennung) wie S1.
S1 = coherent(np.radians(38.6763))
phi_s1, _, z_s1 = phi_K(np.abs(S1) ** 2)
SGN = np.sign(phi_s1)
a1 = np.angle(z_s1)
P_T = pops_from_argz(a1 + (SGN * PHI_T - phi_s1) / 3)
p_s2 = pops_from_argz(a1 + (SGN * np.pi / 4 - phi_s1) / 3)
p_s2 = np.clip(p_s2, 0, None); p_s2 /= p_s2.sum()
S2 = np.sqrt(p_s2).astype(complex)
STARTS = {"S1 Spin-1-Dreieck": S1, "S2 flacher Oktant": S2}


def expm_herm(H, dt):
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w * dt)) @ V.conj().T


def penalty_and_grad_p(p, mu):
    phi, K, z = phi_K(p)
    dphi = 3 * np.imag(UC / z)
    dK = 2 * p
    rk, rp = (K - 2 / 3) / EPS_K, (phi - SGN * PHI_T) / EPS_PHI
    C = mu * (rk ** 2 + rp ** 2)
    g = mu * (2 * rk / EPS_K * dK + 2 * rp / EPS_PHI * dphi)
    return C, g


def unitary_cost(x, psi0, tau, mode, mu):
    u = x.reshape(4, N); dt = tau / N
    psis = [psi0]; Us = []
    for n in range(N):
        U = expm_herm(H0 + sum(u[k, n] * GEN[k] for k in range(4)), dt)
        Us.append(U); psis.append(U @ psis[-1])
    p = np.abs(psis[-1]) ** 2
    C, gp = penalty_and_grad_p(p, mu)
    lam = gp * psis[-1]                       # dC/dpsi* (bis auf Faktor), C reell
    grad = np.zeros_like(u)
    for n in range(N - 1, -1, -1):
        psi_n = psis[n + 1]
        for k in range(4):
            grad[k, n] = 2 * np.real(np.vdot(lam, -1j * dt * GEN[k] @ psi_n))
        lam = Us[n].conj().T @ lam
    if mode == "min":
        A = np.sum(u ** 2) * dt; gA = 2 * u * dt
    else:  # glatt
        du = np.diff(u, axis=1)
        A = np.sum(du ** 2) / dt + 1e-3 * np.sum(u ** 2) * dt
        gA = 2e-3 * u * dt
        gA[:, 1:] += 2 * du / dt; gA[:, :-1] -= 2 * du / dt
    return A + C, (grad + gA).ravel()


def propagate_unitary(u, psi0, tau):
    dt = tau / N; psi = psi0.copy(); traj = [np.abs(psi) ** 2]
    for n in range(N):
        psi = expm_herm(H0 + sum(u[k, n] * GEN[k] for k in range(4)), dt) @ psi
        traj.append(np.abs(psi) ** 2)
    return psi, np.array(traj)


# dissipative Ratengleichung: M_k Uebergangsmatrizen (Spalten = von, Zeilen = nach), Basis m = +1, 0, -1 -> Index 0, 1, 2
def rate_matrix(trans):
    M = np.zeros((3, 3))
    for (i, j, c) in trans:      # von i nach j mit Faktor c
        M[j, i] += c; M[i, i] -= c
    return M


MD = [rate_matrix([(0, 1, 2), (1, 2, 2)]),   # J-
      rate_matrix([(2, 1, 2), (1, 0, 2)]),   # J+
      rate_matrix([(0, 2, 4)]),              # J-^2
      rate_matrix([(2, 0, 4)])]              # J+^2
DNAMES = ["J-", "J+", "J-^2", "J+^2"]


def expm_real(M, dt):
    from scipy.linalg import expm
    return expm(M * dt)


def diss_cost(x, p0, tau, mode, mu):
    y = x.reshape(4, N); g = y ** 2; dt = tau / N
    ps = [p0]; Es = []
    for n in range(N):
        E = expm_real(sum(g[k, n] * MD[k] for k in range(4)), dt)
        Es.append(E); ps.append(E @ ps[-1])
    C, lam = penalty_and_grad_p(ps[-1], mu)
    grad = np.zeros_like(y)
    for n in range(N - 1, -1, -1):
        for k in range(4):
            grad[k, n] = lam @ (MD[k] @ ps[n + 1]) * dt * 2 * y[k, n]
        lam = Es[n].T @ lam
    if mode == "min":
        A = np.sum(g) * dt; gA = 2 * y * dt
    else:
        dg = np.diff(g, axis=1)
        A = np.sum(dg ** 2) / dt + 1e-3 * np.sum(g) * dt
        gg = 1e-3 * dt * np.ones_like(g); gg[:, 1:] += 2 * dg / dt; gg[:, :-1] -= 2 * dg / dt
        gA = gg * 2 * y
    return A + C, (grad + gA).ravel()


NACHLAUF = "--nachlauf" in sys.argv          # Nachtrag N1: Startfeld nahe null, nur tau = 3 pi
INIT_SIGMA = 1e-3 if NACHLAUF else 0.3


def solve(kind, start, tau, mode, seed):
    rng = np.random.default_rng(seed)
    x0 = rng.normal(0, INIT_SIGMA, 4 * N)
    best = None
    for mu in (1.0, 10.0, 100.0):
        f = (lambda x: unitary_cost(x, start, tau, mode, mu)) if kind == "u" else (lambda x: diss_cost(x, np.abs(start) ** 2, tau, mode, mu))
        r = minimize(f, x0, jac=True, method="L-BFGS-B", options={"maxiter": 3000 if not QUICK else 600})
        x0 = r.x; best = r
    return best.x


def analyse(kind, start, tau, mode, x):
    dt = tau / N; t = (np.arange(N) + 0.5) * dt
    if kind == "u":
        u = x.reshape(4, N)
        psi, traj = propagate_unitary(u, start, tau); p = np.abs(psi) ** 2
        A = np.sum(u ** 2) * dt
        share_D = np.sum(u[:2] ** 2) / max(np.sum(u ** 2), 1e-30)
        amp = np.sqrt(np.sum(u ** 2, axis=0))
        area = np.sum(amp) * dt
        spec = {}
        for k in range(4):
            F = np.abs(np.fft.rfft(u[k])); fr = np.fft.rfftfreq(N, dt) * 2 * np.pi
            spec[GNAMES[k]] = float(fr[np.argmax(F[1:]) + 1]) if F[1:].max() > 0 else 0.0
        env_D = np.sqrt(np.sum(u[:2] ** 2, axis=0)); env_Q = np.sqrt(np.sum(u[2:] ** 2, axis=0))
        extra = {"Anteil Dipol": float(share_D), "Spektralspitzen (Kreisfrequenz)": spec,
                 "Huelle Dipol: Mittel, Streuung/Mittel, Schwerpunkt t/tau": [float(env_D.mean()), float(env_D.std() / max(env_D.mean(), 1e-12)),
                                                                            float(np.sum(t * env_D) / max(np.sum(env_D), 1e-12) / tau)],
                 "Huelle Quadrupol: Mittel, Streuung/Mittel, Schwerpunkt t/tau": [float(env_Q.mean()), float(env_Q.std() / max(env_Q.mean(), 1e-12)),
                                                                                 float(np.sum(t * env_Q) / max(np.sum(env_Q), 1e-12) / tau)]}
    else:
        g = x.reshape(4, N) ** 2
        p = np.abs(start) ** 2
        for n in range(N):
            p = expm_real(sum(g[k, n] * MD[k] for k in range(4)), dt) @ p
        A = np.sum(g) * dt; area = A
        extra = {"Anteile je Sprung": {DNAMES[k]: float(np.sum(g[k]) / max(np.sum(g), 1e-30)) for k in range(4)},
                 "Schwerpunkt t/tau": float(np.sum(t * g.sum(0)) / max(g.sum(), 1e-12) / tau)}
    phi, K, _ = phi_K(p)
    ok = abs(K - 2 / 3) <= EPS_K and abs(phi - SGN * PHI_T) <= EPS_PHI
    return {"A": float(A), "Pulsflaeche": float(area), "phi": float(phi), "K": float(K), "im Spielraum": bool(ok), **extra}


def d_fs(p1, p2):
    return float(np.arccos(np.clip(np.sum(np.sqrt(p1 * p2)), -1, 1)))


if __name__ == "__main__":
    out = {"Start": {}, "Ziel": P_T.tolist()}
    print(f"Ziel-Populationen (m = +1, 0, -1): {np.round(P_T, 6)}, phi = {phi_K(P_T)[0]:+.6f}, K = {phi_K(P_T)[1]:.6f}")
    for name, s in STARTS.items():
        p = np.abs(s) ** 2; ph, K, _ = phi_K(p)
        out["Start"][name] = {"p": p.tolist(), "phi": float(ph), "K": float(K), "d_FS zum Ziel": d_fs(p, P_T)}
        print(f"{name}: p = {np.round(p, 6)}, phi = {ph:+.6f}, K = {K:.6f}, Fubini-Study-Abstand zum Ziel = {d_fs(p, P_T):.6f}")
    # Kontrolle: J_z, J_z^2 aendern die Populationen nicht
    Jz = np.diag([1.0, 0, -1]).astype(complex)
    ps = expm_herm(H0 + 0.7 * Jz + 0.3 * Jz @ Jz, np.pi) @ S1
    print(f"Kontrolle J_z, J_z^2: Populationen unveraendert: {np.allclose(np.abs(ps) ** 2, np.abs(S1) ** 2)}")
    if "--selftest" in sys.argv:
        sys.exit(0)
    runs = []
    for sname, s in STARTS.items():
        for kind in ("u", "d"):
            variants = (("V0 Haupt", np.pi, "min"), ("V1 glatt", np.pi, "smooth"), ("V2 tau=pi/3", np.pi / 3, "min"), ("V2 tau=3pi", 3 * np.pi, "min"))
            if NACHLAUF:
                variants = (("N1 V2 tau=3pi", 3 * np.pi, "min"),)
            for label, tau, mode in variants:
                res = []
                for seed in range(RESTARTS):
                    x = solve(kind, s, tau, mode, seed)
                    res.append(analyse(kind, s, tau, mode, x))
                okres = [r for r in res if r["im Spielraum"]] or res
                b = min(okres, key=lambda r: r["A"])
                As = np.array([r["A"] for r in okres])
                b["Streuung A ueber Starts (rel.)"] = float(As.std() / max(As.mean(), 1e-12))
                b["Starts im Spielraum"] = f"{sum(r['im Spielraum'] for r in res)}/{len(res)}"
                b["Treffer Konstantenliste (Pulsflaeche, d_FS; rel. <= 1e-3)"] = [
                    f"{q}~{c}" for q, val in (("Pulsflaeche", b["Pulsflaeche"]), ("d_FS", out["Start"][sname]["d_FS zum Ziel"]))
                    for c, cv in CONST.items() if abs(val - cv) / cv <= 1e-3]
                runs.append({"Start": sname, "Art": "unitaer" if kind == "u" else "dissipativ", "Variante": label, **b})
                print(json.dumps(runs[-1], ensure_ascii=False))
    out["Laeufe"] = runs
    with open("run/correction_term_nachlauf.json" if NACHLAUF else "run/correction_term_result.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
