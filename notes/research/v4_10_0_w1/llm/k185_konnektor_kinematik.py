"""k185 (Erkundung, Autorfrage Higgs als Tachyonfeld): Massenquadrat eines Konnektors zwischen einem Materiezustand (p_M = m(cosh a, sinh a) entlang z)
und einem Tachyonbild (Fortsetzung eta -> eta + i pi/2: p_T = m(sinh b, +-cosh b)). Fuer ebene Wellen traegt das Bilinear den Impuls
q = p_M + p_T (Paar) bzw. q = p_M - p_T (Uebergang); Massenquadrat q^2. Analytisch: p_M.p_T = m^2(cosh a sinh b -+ sinh a cosh b)."""
import numpy as np
m=1.0;eta_s=np.arctanh(0.5493)
def q2(a,b,richtung,art):
    pM=m*np.array([np.cosh(a),np.sinh(a)]);pT=m*np.array([np.sinh(b),richtung*np.cosh(b)])
    q=pM+pT if art=='Paar' else pM-pT;return q[0]**2-q[1]**2
print('gemeinsame Rapiditaet a = b = eta:')
for eta in (0.0,0.3,eta_s,1.5):
    r={f'{"gleich" if d>0 else "gegen"}/{art}':round(q2(eta,eta,d,art),6) for d in (1,-1) for art in ('Paar','Uebergang')}
    print(f'  eta={eta:.4f}: {r}   2 sinh 2eta = {2*np.sinh(2*eta):.6f}')
print('Kontrolle Massenschalen: p_M^2 =',round(np.cosh(.7)**2-np.sinh(.7)**2,12),' p_T^2 =',round(np.sinh(.7)**2-np.cosh(.7)**2,12))
