"""k444 (Test H230): Symmetriepunkt pi/8 (und 0) in den Materie-Frame uebertragen.
Vorab-Notiz Vorab_H230_Symmetriepunkt_Materie_Frame.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k444_test_h230.py > k444_out.txt
"""
import math
import numpy as np

X = math.pi / 12 - 0.2222220470731
SIG = 7.8e-7
XNU, SXNU = 0.04336, 0.00213
BETA = 0.549405640974529
GL = 1.864699764609373
EPS0 = math.atanh(BETA)
B2 = math.tanh(2 * EPS0)          # Geschwindigkeit zur Rapiditaet 2 eps0
print("=" * 92)
print("H230 (k444)  Symmetriepunkt in den Materie-Frame")
print("=" * 92)
print(f"beta_sym = {BETA}, eps0 = {EPS0:.10f}, 2 eps0 = {2*EPS0:.10f}, cosh 2eps0 = {math.cosh(2*EPS0):.10f} (gamma_L = {GL}),"
      f" tanh 2eps0 = {B2:.10f}, cosh eps0 = {math.cosh(EPS0):.10f}")
print(f"Ziel x = {X:.10f} (sigma {SIG}), x_nu = {XNU} +- {SXNU};  Datenphasen delta*_Im = {math.pi/12 - X:.10f}, delta*_Re = {math.pi/6 - XNU:.6f}")

# ---------------- Teil A ----------------
P = np.roll(np.eye(3), 1, axis=0)
RHO = 1 / math.sqrt(2)


def Cmat(d0):
    z = RHO * np.exp(1j * d0)
    return np.eye(3) + z * P + np.conj(z) * P.T


def Dm(eps):
    return np.diag(np.exp(eps * np.array([0.0, 0.0, -3.0])))


def fK(C, e):
    return Dm(e) @ C @ Dm(e)


def flin(C, e):
    W = np.diag([0.0, 0.0, -3.0])
    return C + e * (W @ C + C @ W)


def fS(C, e):
    return Dm(e) @ C @ np.linalg.inv(Dm(e))


def K_delta(M, herm=True):
    ev = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2)) if herm else np.sort(np.linalg.eigvals(M).real)
    neg = int((ev < 0).sum())
    K = (ev ** 2).sum() / ev.sum() ** 2
    td = math.sqrt(3) * (ev[1] - ev[0]) / (2 * ev[2] - ev[1] - ev[0])
    return K, math.atan(td), neg


print("\nTeil A  Maske auf das R-Spektrum; Auslesen (K', delta') in der Klasse [0, pi/3); Vergleich mit den Datenphasen")
print("  Kontrolle eps = 0: ", end="")
ctrl = []
for d0 in (math.pi / 12 - math.pi / 8, math.pi / 6 - math.pi / 8, math.pi / 12, math.pi / 6):
    K, d, n = K_delta(fK(Cmat(d0), 0.0))
    ctrl.append((round(K, 12), round(d, 10), round(abs(d0), 10)))
print(ctrl, " (delta' = |delta0| in der Klasse)")
hitA = False
rowsA = []
for phiR, lab in ((math.pi / 8, "pi/8"), (0.0, "0 (schon H166d, nur Kontrolle)")):
    for fn, f in (("K", fK), ("lin", flin), ("S", fS)):
        for en, e in (("+eps0", EPS0), ("-eps0", -EPS0), ("+2eps0", 2 * EPS0), ("-2eps0", -2 * EPS0)):
            KI, dI, nI = K_delta(f(Cmat(math.pi / 12 - phiR), e), herm=(fn != "S"))
            KR, dR, nR = K_delta(f(Cmat(math.pi / 6 - phiR), e), herm=(fn != "S"))
            zI = (dI - (math.pi / 12 - X)) / SIG
            zR = (dR - (math.pi / 6 - XNU)) / SXNU
            hit = abs(KI - 2 / 3) <= 1e-4 and abs(KR - 2 / 3) <= 1e-4 and abs(zI) <= 2 and abs(zR) <= 2
            if phiR > 0:
                hitA |= hit
            rowsA.append((abs(dI - (math.pi / 12 - X)), lab, fn, en))
            print(f"  phi_R = {lab:30s} Form {fn:3s} {en:6s}: Im K' = {KI:.6f}, delta' = {dI:.6f} ({zI:+.2e} sigma), neg {nI} |"
                  f" Re K' = {KR:.6f}, delta' = {dR:.6f} ({zR:+.1f} sigma_nu), neg {nR}{'  TREFFER' if hit else ''}")
print(f"Treffer A (phi_R = pi/8): {hitA}")

# ---------------- Teil B ----------------
print("\nTeil B  Winkel-Abbildungen des Symmetriepunkts pi/8 in den Lesarten theta = phi, 2phi, 3phi;  phi' = theta'/n")


def aberr(beta, sgn):
    return lambda t: math.acos((math.cos(t) - sgn * beta) / (1 - sgn * beta * math.cos(t)))


def tanmul(k):
    return lambda t: math.atan(k * math.tan(t))


MAPS = {
    "Aberration -beta_sym": aberr(BETA, +1), "Aberration +beta_sym": aberr(BETA, -1),
    "Aberration -tanh2e": aberr(B2, +1), "Aberration +tanh2e": aberr(B2, -1),
    "tan/cosh e0": tanmul(1 / math.cosh(EPS0)), "tan*cosh e0": tanmul(math.cosh(EPS0)),
    "tan/gamma_L": tanmul(1 / GL), "tan*gamma_L": tanmul(GL),
    "tan*beta_sym": tanmul(BETA), "tan/beta_sym": tanmul(1 / BETA),
    "tan*tanh2e": tanmul(B2), "tan/tanh2e": tanmul(1 / B2),
}
cands = []
for n in (1, 2, 3):
    th = n * math.pi / 8
    for mn, m in MAPS.items():
        tp = m(th)
        ph = tp / n
        cands.append((ph, mn, n))
cands.sort(key=lambda c: abs(c[0] - X))
hitB = False
loose = 0
for ph, mn, n in cands:
    d = ph - X
    hitB |= abs(d) <= 2 * SIG
    loose += abs(d) <= 0.01 * X
for ph, mn, n in cands[:10]:
    print(f"  {mn:22s} Lesart {n}phi: phi' = {ph:.8f}  Abstand {ph - X:+.3e} = {(ph - X)/SIG:+11.1f} sigma ({(ph-X)/X*100:+.1f} %)")
allph = np.array([c[0] for c in cands])
print(f"  Spannweite der 36 Bilder: {allph.min():.4f} bis {allph.max():.4f}; Bilder unter 0,1: {int((allph < 0.1).sum())}")
dens = 36 / (allph.max() - allph.min())
lam = dens * 0.02 * X
pl = 1 - math.exp(-lam) * sum(lam ** k / math.factorial(k) for k in range(loose)) if loose else 1.0
print(f"  lockere Treffer (< 1 %): {loose}; Zufallserwartung (gleichverteilt ueber die Spannweite) lambda = {lam:.4f}, P(>= {loose}) = {pl:.3g}")
print("  Grenzfaelle: Lichtpunkt (beta -> 1): Aberration -> 0 bzw. pi, Kontraktion -> 0; Dual-Frame z -> iz: theta -> theta + pi/2"
      " (pi/8 -> 5pi/8, rationale Vielfache von pi); Punkt 0 ist unter allen Abbildungen fest.")
print(f"Treffer B: {hitB}")

print("\n" + "=" * 92)
if hitA or hitB:
    v = "TRAEGT"
elif loose and pl < 0.05:
    v = "TRAEGT TEILWEISE"
else:
    v = "WIDERLEGT"
print(f"H230 Gesamturteil: {v}   (A {hitA}, B {hitB}, lockere B {loose})")
