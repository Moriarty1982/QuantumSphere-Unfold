"""k181: Test der Vorab-Notiz H73 (Commit 623a080). B = V1 in Ruhe (k=0, w=m), Gewicht p+; A = V2 an der Schwelle (|k|=m, w=0), Gewicht p-,
isotrop ueber +-x,+-y,+-z. Normierung |psi|^2+|chi|^2 = 1 (Hauptlinie) und |psi|^2 = 1 (Empfindlichkeit)."""
import numpy as np, json, importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location('k','k179_test_h71.py');k=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(k)
src=open('k180_test_h72.py').read().split('# Kontrollen')[0];g={};
with contextlib.redirect_stdout(io.StringIO()): exec(src,g)
iso=g['iso'];eta=k.eta;x=0.5493**2;pp,pm=1/(1+x),x/(1+x);out={}
def T_of(kk,lam,s,norm):
    w,u,v=k.mode(kk,lam,s)
    n=np.sqrt(np.vdot(u,u).real+np.vdot(v,v).real) if norm=='feld' else np.sqrt(np.vdot(u,u).real)
    u=u/n;v=v/n;p,c,dp,dc=k.fields(np.zeros(4),[(kk,w,u,v)])
    e1=sum(1j*k.sbu[a]@dp[a] for a in range(4))-k.m*c;e2=s*sum(1j*k.su[a]@dc[a] for a in range(4))-k.m*p
    return k.Tsym(p,dp,k.sbl)+s*k.Tsym(c,dc,k.sl),max(np.abs(e1).max(),np.abs(e2).max())
for norm in ('feld','psi'):
    TB,eB=T_of(0.0,1,+1,norm);res={'eq':eB,'B_raeumlich':float(np.abs(TB[1:,1:]).max()),'B_rho':TB[0,0]}
    As={}
    for lam in (1,-1):
        TA,eA=T_of(1.0,lam,-1,norm);TAi=iso(TA);res['eq']=max(res['eq'],eA)
        As[lam]=dict(T_tt=TAi[0,0],p=TAi[1,1],aniso=float(np.ptp([TAi[1,1],TAi[2,2],TAi[3,3]])),offd=float(np.abs(TAi-np.diag(np.diag(TAi))).max()))
    res['A']=As
    neg=[l for l in (1,-1) if As[l]['p']<0]
    if neg:
        l=neg[0];TA=iso(T_of(1.0,l,-1,norm)[0]);T=pp*TB+pm*TA;rho=T[0,0];pr=T[1,1]
        res.update(lam_A=l,rho=rho,p=pr,w_eff=pr/rho,r_star=-TB[0,0]/TA[1,1] if False else float(-TA[1,1]/TB[0,0])**-1*1.0,ratio_frame=pp/pm)
        # r*: Gewicht B/A fuer w=-1: wB*rhoB = -wA*pA  ->  wB/wA = -pA/rhoB
        res['r_star']=float(-TA[1,1]/TB[0,0])
    else: res['kein_negativer_Druck']=True
    out[norm]=res
json.dump(out,open('k181_out.json','w'),indent=1,default=float)
for n,r in out.items(): print(n,':',r)
