"""Erkundung (nicht blind): Generationsstruktur von C(x)S unter der e8-Ladung Q_* (14.11.2026).

Gemeinsame Zerlegung von C(x)S nach Ladung Q_*, Farbtyp (1, 3, 3bar) und psi-Eigenwert (1, omega, omegabar).
Danach: Welche psi-Sektoren enthalten eine vollstaendige Generation (nu, e+, 3 u, 3 dbar)? Vergleich mit Q_S auf O.
Aufruf: python op3_sedenion_generations_estar_2026_11_14.py
"""
import importlib.util
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ho = load("ho", os.path.join(HERE, "op3_hopf_octant_2026_11_13.py"))
sr = load("sr", os.path.join(HERE, "op3_sedenion_reference_2026_11_13.py"))
ch = load("ch", os.path.join(HERE, "op3_sedenion_charge_2026_11_13.py"))
smul, su, psi_matrix = sr.smul, sr.su, sr.psi_matrix
W = np.exp(2j * np.pi / 3)

if __name__ == "__main__":
    e7, e8 = su(7), su(8)
    P = psi_matrix(2 * np.pi / 3).astype(complex)
    DS = [np.kron(np.eye(2), d) for d in ho.derivations()]
    c = ch.null_space(np.array([D @ e7 for D in DS]).T)
    SU3 = [sum(c[k, j] * DS[k] for k in range(14)).real for j in range(c.shape[1])]
    H = [0, 7, 8, 15]
    P0 = np.zeros((16, 16)); P0[H, H] = 1
    Pc = np.eye(16) - P0
    L = lambda x: np.array([smul(x, su(b)) for b in range(16)]).T
    R = lambda x: np.array([smul(su(b), x) for b in range(16)]).T
    QS = 0.5 * np.eye(16) - (1j / 6) * L(e7) - (1j / 3) * R(e7)
    w, V = np.linalg.eig(QS[1:7, 1:7])
    V3 = []
    for k in range(6):
        if abs(w[k] - 2 / 3) < 1e-9:
            v = np.zeros(16, complex); v[1:7] = V[:, k]; V3.append(v)
    V3 = V3 + [P @ v for v in V3] + [P @ P @ v for v in V3]
    P3 = ch.proj(V3)
    P3b = Pc - P3
    Qs = P0 @ (0.5 * np.eye(16) - 0.5j * L(e8)) @ P0 + (2 / 3) * P3 + (1 / 3) * P3b
    # gemeinsame Eigenbasis: Q_* + kleiner Anteil psi-Phase + Farbtyp
    table = {}
    for qv in (0.0, 1 / 3, 2 / 3, 1.0):
        for ptype, Pp in (("1", P0), ("3", P3), ("3bar", P3b)):
            for k, lam in enumerate((1, W, W ** 2)):
                # Projektor auf Q_* = qv, Farbtyp, psi = lam
                Pq = np.eye(16, dtype=complex)
                for q2 in (0.0, 1 / 3, 2 / 3, 1.0):
                    if q2 != qv:
                        Pq = Pq @ (Qs - q2 * np.eye(16)) / (qv - q2)
                Pl = np.eye(16, dtype=complex)
                for m, l2 in enumerate((1, W, W ** 2)):
                    if m != k:
                        Pl = Pl @ (P - l2 * np.eye(16)) / (lam - l2)
                d = int(round(np.trace(Pq @ Pp @ Pl).real))
                if d:
                    table[(qv, ptype, ("1", "w", "wbar")[k])] = d
    print("(1) Gemeinsame Zerlegung von C(x)S unter (Q_*, Farbtyp, psi-Eigenwert), Dimensionen:")
    for (qv, ptype, lam), d in sorted(table.items()):
        nm = {(0.0, "1"): "nu", (1.0, "1"): "e+", (2 / 3, "3"): "u", (1 / 3, "3bar"): "dbar"}.get((qv, ptype), "?")
        print(f"    Q = {qv:.3f}  {ptype:5s} psi = {lam:5s}: {d}  ({nm})")
    print(f"    Summe {sum(table.values())}")
    print("\n(2) Inhalt je psi-Sektor (Generation = nu + e+ + 3 u + 3 dbar):")
    for lam in ("1", "w", "wbar"):
        content = {}
        for (qv, ptype, l2), d in table.items():
            if l2 == lam:
                nm = {(0.0, "1"): "nu", (1.0, "1"): "e+", (2 / 3, "3"): "u", (1 / 3, "3bar"): "dbar"}[(qv, ptype)]
                content[nm] = content.get(nm, 0) + d
        full = content.get("nu") == 1 and content.get("e+") == 1 and content.get("u") == 3 and content.get("dbar") == 3
        qsum = sum({"nu": 0, "e+": 1, "u": 2 / 3, "dbar": 1 / 3}[n] * d for n, d in content.items())
        print(f"    psi = {lam:5s}: {content}; vollstaendige Generation {full}; Ladungssumme {qsum:.3f} (Generation: 4)")
    # (3) Vergleich: Q_S auf O (eine Generation, k85)
    QO = QS[:8, :8]
    ev = np.round(np.linalg.eigvals(QO).real, 6)
    vals, cnt = np.unique(ev, return_counts=True)
    print(f"\n(3) Q_S auf O: Spektrum {dict(zip(vals.tolist(), cnt.tolist()))} (eine vollstaendige Generation)")
    # (4) Antiteilchen-Paarung: komplexe Konjugation bildet Q -> 1 - Q und psi-Eigenwert lam -> conj(lam)
    print(f"(4) conj(Q_*) = 1 - Q_*: {np.allclose(Qs.conj(), np.eye(16) - Qs)}; psi reell: {np.allclose(P.imag, 0)}"
          " -> Konjugation paart (Q, psi = w) mit (1 - Q, psi = wbar)")
