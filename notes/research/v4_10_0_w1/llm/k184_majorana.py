"""k184 (Erkundung, I4): Kann der eichinvariante Majorana-Term fuer nu^c (r44) tachyonisch werden?
Ein linkshaendiges Weyl-Feld psi mit L = s*psi^+ i sbar^mu d_mu psi - (M/2)(psi^T eps psi + c.c.), eps = i sigma_2, M = |M| e^{i phi}.
Feldgleichung: s*i sbar^mu d_mu psi = M^* eps psi^* (bis auf Konvention). Ebene Welle entlang z: psi = u e^{-i(wt-kz)} + v^* e^{+i(wt-kz)};
reelles lineares System in (u, v); omega aus der Bedingung det = 0. Prueft s = +1 und s = -1 und Phasen phi."""
import numpy as np
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]);eps=1j*sy
def omegas(k,M,s):
    # Ansatz psi = u e^{-i theta} + conj(v) e^{+i theta}, theta = w t - k z
    # i sbar.d e^{-i theta} -> (w + k sz) ; i sbar.d e^{+i theta} -> -(w + k sz)
    # s(w + k sz) u = conj(M) eps v ;  s(-(w + k sz)) conj(v) = conj(M) eps conj(u)  ->  conj: -s(w + k sz) v = M eps^* u = M eps u (eps reell)
    # => u = conj(M)/s (w+k sz)^{-1} eps v ;  v = -M/s (w+k sz)^{-1} eps u
    # => u = -|M|^2/s^2 A eps A eps u mit A=(w+k sz)^{-1}; Eigenbedingung det(I + |M|^2 A eps A eps) = 0
    res=[]
    for w in np.linspace(-6,6,240001):
        A=np.linalg.inv(w*np.eye(2)+k*sz) if abs(abs(w)-abs(k))>1e-9 else None
        if A is None: continue
        res.append((w,abs(np.linalg.det(np.eye(2)+abs(M)**2/s**2*A@eps@A@eps))))
    w,d=np.array(res).T;idx=[i for i in range(1,len(d)-1) if d[i]<d[i-1] and d[i]<d[i+1] and d[i]<1e-3]
    return sorted(set(np.round(w[idx],4)))
for s in (1,-1):
    for phi in (0,np.pi/2):
        M=1.0*np.exp(1j*phi)
        for k in (0.0,0.5,2.0):
            ws=omegas(k,M,s);print(f's={s:+d} phi={phi:.2f} k={k}: omega^2 = {[round(w*w,4) for w in ws if w>0]}  (k^2+|M|^2 = {k*k+1:.4f}, k^2-|M|^2 = {k*k-1:.4f})')
