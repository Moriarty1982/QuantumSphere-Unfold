"""k182 (Erkundung, Autorhinweis 'Grenzwert statt Extremwerte'): Moden bei gemeinsamer Rapiditaet eta, Gewichte aus derselben Rapiditaet.
B: V1, k = m sinh eta, w = m cosh eta, Gewicht p+ = 1/(1+t^2); A: V2 (lam=+1), k = m cosh eta, w = m sinh eta, Gewicht p- = t^2/(1+t^2), t = tanh eta.
Isotrop gemittelt, Feldnorm. Analytisch: Materie-Frame-Gewichte geben p = 0 (w = 0) fuer jedes eta; vertauschte Gewichte rho = 0."""
import numpy as np, json, importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location('k','k181_test_h73.py');src=open('k181_test_h73.py').read().split('for norm in')[0];g={}
with contextlib.redirect_stdout(io.StringIO()): exec(src,g)
T_of=g['T_of'];iso=g['iso'];eta_s=np.arctanh(0.5493);rows=[]
for eta in [1e-3,0.1,0.3,0.5,eta_s,0.8,1.0,2.0,4.0]:
    t=np.tanh(eta);pp,pm=1/(1+t*t),t*t/(1+t*t)
    TB=iso(T_of(np.sinh(eta),1,+1,'feld')[0]);TA=iso(T_of(np.cosh(eta),1,-1,'feld')[0])
    TM=pp*TB+pm*TA;TT=pm*TB+pp*TA
    rows.append(dict(eta=eta,M_rho=TM[0,0],M_p=TM[1,1],T_rho=TT[0,0],T_p=TT[1,1]))
    print(f"eta={eta:.4f}{' (eta_sym)' if eta==eta_s else ''}: Materie-Gewichte rho={TM[0,0]:+.6f} p={TM[1,1]:+.2e} | Tachyon-Gewichte rho={TT[0,0]:+.2e} p={TT[1,1]:+.6f}")
json.dump(rows,open('k182_out.json','w'),indent=1,default=float)
