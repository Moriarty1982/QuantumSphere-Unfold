"""k180: Test der Vorab-Notiz H72 (Commit bc85519). Isotropes, inkohaerentes Gas von Moden aus k179 (V2 tachyonisch, V1 Kontrolle)."""
import numpy as np, json, importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location('k','k179_test_h71.py');k=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(k)
eta=k.eta;out={}
def Tmode(kk,lam,s):
    w,u,v=k.mode(kk,lam,s);nrm=np.sqrt(1+abs(v[0]+v[1])**2*0+np.vdot(v,v).real);u=u/nrm;v=v/nrm
    p,c,dp,dc=k.fields(np.zeros(4),[(kk,w,u,v)]);T=k.Tsym(p,dp,k.sbl)+s*k.Tsym(c,dc,k.sl)
    pv=np.array([w,0,0,kk]);N=T[0,0]/w**2;ppres=np.abs(T-N*np.outer(pv,pv)).max()/np.abs(T).max()
    return T,N,ppres,w
def iso(T):  # Mittel ueber +-x,+-y,+-z
    acc=np.zeros((4,4))
    for ax in (1,2,3):
        for sg in (1,-1):
            P=np.eye(4);P[[3,ax]]=P[[ax,3]];S=np.diag([1,1,1,1.]);S[ax,ax]=sg
            R=S@P;acc+=R@T@R.T
    return acc/6
# Kontrollen
pp=max(Tmode(kk,l,-1)[2] for kk in (1.5,2,5) for l in (1,-1));out['T_prop_pp']=pp
Ti=iso(Tmode(2.0,1,-1)[0]);out['iso_offdiag']=float(np.abs(Ti-np.diag(np.diag(Ti))).max()/np.abs(Ti).max());out['iso_aniso']=float(np.ptp([Ti[1,1],Ti[2,2],Ti[3,3]])/np.abs(Ti).max())
# H72a: Beispiel kA=1.2 (lam=+1), kB=3.0 (lam=-1)
TA=iso(Tmode(1.2,1,-1)[0]);TB=iso(Tmode(3.0,-1,-1)[0]);fA=TA[1,1]+TA[0,0];fB=TB[1,1]+TB[0,0]
wB=-fA/fB;T=TA+wB*TB;rho=T[0,0];out['H72a']=dict(wB_over_wA=wB,rho=rho,res=float(np.abs(T-rho*eta).max()/abs(rho)),fA=fA,fB=fB,NA=Tmode(1.2,1,-1)[1],NB=Tmode(3.0,-1,-1)[1])
# H72b: Familie kB variiert
fam=[]
for kb in (1.05,1.5,2.0,3.0,5.0,10.0):
    for (la,lb) in ((1,-1),(-1,1)):
        TA=iso(Tmode(1.2,la,-1)[0]);TB=iso(Tmode(kb,lb,-1)[0]);fA=TA[1,1]+TA[0,0];fB=TB[1,1]+TB[0,0]
        if fA*fB<0:
            wb=-fA/fB;T=TA+wb*TB;fam.append((kb,la,lb,float(wb),float(T[0,0]),float(np.abs(T-T[0,0]*eta).max()/abs(T[0,0]))))
out['H72b_family']=fam
# Kontrolle V1: w = Txx/Ttt >= 0
wv1=[iso(Tmode(kk,l,1)[0]) for kk in (0.1,0.5,1,2,5,20) for l in (1,-1)];out['V1_w_min']=float(min(T[1,1]/T[0,0] for T in wv1))
wv2=[(kk,l,iso(Tmode(kk,l,-1)[0])) for kk in (1.05,2,5,20) for l in (1,-1)];out['V2_single_w']=[(kk,l,float(T[1,1]/T[0,0])) for kk,l,T in wv2]
# H72c
x=0.5493**2;pM=(1/(1+x),x/(1+x))
def wgas(kk,weights,assign):
    lp,lm=assign;T=weights[0]*iso(Tmode(kk,lp,-1)[0])+weights[1]*iso(Tmode(kk,lm,-1)[0]);return T[1,1]/T[0,0],T[0,0]
ks=np.concatenate([np.linspace(1.0005,2,400),np.linspace(2,20,900)])
for wname,W in (('M',pM),('P',(0.5,0.5))):
    for aname,A in (('(i) p+ auf lam=-1',(-1,1)),('(ii) p+ auf lam=+1',(1,-1))):
        vals=np.array([wgas(kk,W,A)[0] for kk in ks]);g=vals+1;roots=[]
        for i in range(len(ks)-1):
            if np.isfinite(g[i]) and np.isfinite(g[i+1]) and g[i]*g[i+1]<0:
                a,b=ks[i],ks[i+1]
                for _ in range(80):
                    c=(a+b)/2
                    if (wgas(a,W,A)[0]+1)*(wgas(c,W,A)[0]+1)<=0: b=c
                    else: a=c
                roots.append(dict(k_star=(a+b)/2,rho=wgas((a+b)/2,W,A)[1]))
        out[f'H72c_{wname}_{aname}']=dict(roots=roots,w_range=[float(np.nanmin(vals)),float(np.nanmax(vals))])
json.dump(out,open('k180_out.json','w'),indent=1,default=float)
for kk,v in out.items(): print(kk,':',v)
