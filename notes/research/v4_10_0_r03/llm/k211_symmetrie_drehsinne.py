"""k211 (Erkundung, keine Vorab-Notiz): exakte Symmetrie der beiden Drehsinne am Urknall-Uebergang.
Transfermatrix M(L) in der Basis (e^{ikt}, e^{-ikt}): Spalten = Ausgang fuer Eingang e^{ikt} bzw. e^{-ikt}.
Hergeleitet: M(Lbar) = [[conj d, conj b], [conj c, conj a]] mit M(L) = [[a, b], [c, d]], det M(L) = e^{-L}.
Folgen: C(Lbar) = conj C(L) (|C+| = |C-|), D(L) conj(D(Lbar)) - b(L) C(L) = e^{-L} (Produktregel aus H86).
Lokal: M = [[1, 0], [r, 1]] exakt, r(lam bar) = conj r(lam).
Aufruf (aus llm/): python k211_symmetrie_drehsinne.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from k210_norm_uebergang import wfun, a, b, Dlt, Lb


def Mfull(kD, sgn):
    k = kD/Dlt
    def rhs(t, y):
        w, dw = wfun(t, sgn); return [y[1], -(dw/w)*y[1] - k**2*y[0]]
    cols = []
    for s0 in (+1, -1):
        c0 = np.exp(s0*1j*k*(-Lb))
        s = solve_ivp(rhs, (-Lb, Lb), np.array([c0, s0*1j*k*c0], complex), method='DOP853', rtol=1e-12, atol=1e-15)
        y, d = s.y[0, -1], s.y[1, -1]
        Ap = (y + d/(1j*k))/2*np.exp(-1j*k*Lb); Am = (y - d/(1j*k))/2*np.exp(1j*k*Lb)
        cols.append([Ap, Am])
    return np.array(cols).T


if __name__ == '__main__':
    Lp = np.log(a/b) - 1j*np.pi
    worst = dict(det=0, C=0, mat=0, prod=0)
    for kD in (0.01, 0.3, 1.0, 2.0, 5.0):
        Mp, Mm = Mfull(kD, +1), Mfull(kD, -1)
        A, B, Cc, Dd = Mp[0, 0], Mp[0, 1], Mp[1, 0], Mp[1, 1]
        pred = np.array([[np.conj(Dd), np.conj(B)], [np.conj(Cc), np.conj(A)]])
        worst['det'] = max(worst['det'], abs(np.linalg.det(Mp)/np.exp(-Lp) - 1))
        worst['C'] = max(worst['C'], abs(Mm[1, 0] - np.conj(Cc))/abs(Cc))
        worst['mat'] = max(worst['mat'], np.max(np.abs(Mm - pred))/np.max(np.abs(Mp)))
        worst['prod'] = max(worst['prod'], abs(A*np.conj(Mm[0, 0]) - B*Cc - np.exp(-Lp))/abs(np.exp(-Lp)))
        print(f'kD={kD}: |D+|={abs(A):.6f} |D-|={abs(Mm[0,0]):.6f} |C|={abs(Cc):.3e} |b|={abs(B):.3e}')
    print('max. relative Abweichungen:', {k: f'{v:.1e}' for k, v in worst.items()})
