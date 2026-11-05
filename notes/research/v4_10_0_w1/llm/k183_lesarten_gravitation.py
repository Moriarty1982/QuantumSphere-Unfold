"""k183 (Erkundung, I3 / Autorfrage 'sieht die Gravitation alle Frames oder nur M?'): dieselbe Materie-Tachyon-Mischung bei gemeinsamer
Rapiditaet eta_sym (k182) in zwei Lesarten: M-Lesart (Staub) und T-Lesart (Spannung). Die Gravitation sieht a*T_M + b*T_T.
Ein Beobachter zerlegt das Ergebnis als Staub + Lambda: rho_L = -p, rho_m = rho + p. Ausgabe Omega_m, Omega_L, w, q0 = (1+3w)/2."""
import numpy as np, json, importlib.util, io, contextlib
src=open('k182_rapiditaet.py').read().split('rows=[]')[0];g={}
with contextlib.redirect_stdout(io.StringIO()): exec(src,g)
T_of,iso=g['T_of'],g['iso'];eta=np.arctanh(0.5493);t=np.tanh(eta);pp,pm=1/(1+t*t),t*t/(1+t*t)
TB=iso(T_of(np.sinh(eta),1,+1,'feld')[0]);TA=iso(T_of(np.cosh(eta),1,-1,'feld')[0])
TM=pp*TB+pm*TA;TT=pm*TB+pp*TA
def split(a,b):
    T=a*TM+b*TT;rho,p=T[0,0],T[1,1];w=p/rho;rL=-p;rm=rho+p
    return dict(rho=rho,p=p,w=w,q0=(1+3*w)/2,Omega_m=rm/rho,Omega_L=rL/rho)
cases={'G1 nur M-Lesart (a=1,b=0)':(1,0),'G2 beide gleich (a=b=1)':(1,1),'G3 Frame-Gewichte (a=p+, b=p-)':(pp,pm),'G4 vertauscht (a=p-, b=p+)':(pm,pp)}
out={k:split(*v) for k,v in cases.items()}
# welches b/a gaebe die Daten (Omega_L = 0.69)?  Omega_L/Omega_m = b/(3a-b)
OL=0.69;r=3*OL/(1)  # b/(3a-b)=OL/(1-OL) -> b/a = 3*OL
out['b/a fuer Omega_L=0.69']=3*OL
out['Kontrolle M-Lesart p']=TM[1,1];out['Kontrolle T-Lesart rho']=TT[0,0]
json.dump(out,open('k183_out.json','w'),indent=1,default=float)
for k,v in out.items(): print(k,':',{a:round(b,4) for a,b in v.items()} if isinstance(v,dict) else round(v,6))
