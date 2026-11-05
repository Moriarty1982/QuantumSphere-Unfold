"""k179: Test der Vorab-Notiz H71 (Commit 4a3b802). L = psi^+ i sbar d psi + s chi^+ i sigma d chi - m(psi^+ chi + h.c.), flach.
Ebene Wellen entlang z, sigma_z psi = lam psi. V1: s=+1, V2: s=-1."""
import numpy as np, json
I=np.eye(2);sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]).astype(complex)
sbu=[I,-sx,-sy,-sz];su=[I,sx,sy,sz];sbl=su;sl=sbu;eta=np.diag([1.,-1,-1,-1]);m=1.0;out={}
def mode(k,lam,s,amp=1.0):
    w2=k*k+m*m/s
    if w2<0: return None
    w=np.sqrt(w2);u=amp*(np.array([1,0],complex) if lam>0 else np.array([0,1],complex));v=(w+k*lam)/m*u
    return w,u,v
def fields(x,modes):
    t,_,_,z=x;psi=np.zeros(2,complex);chi=np.zeros(2,complex);dpsi=np.zeros((4,2),complex);dchi=np.zeros((4,2),complex)
    for (k,w,u,v) in modes:
        ph=np.exp(-1j*(w*t-k*z));psi+=u*ph;chi+=v*ph
        for (mu,f) in ((0,-1j*w),(3,1j*k)): dpsi[mu]+=f*u*ph;dchi[mu]+=f*v*ph
    return psi,chi,dpsi,dchi
def Tsym(p,dp,M):
    X=np.array([[p.conj()@M[a]@dp[b] for b in range(4)] for a in range(4)]);X=X+X.T;return (1j/4*(X-X.conj())).real
for name,s in (('V1',+1),('V2',-1)):
    rows=[];res_eq=0
    for kk in (0.1,0.5,1.0,2.0,5.0):
        for lam in (1,-1):
            r=mode(kk,lam,s)
            if r is None or (s<0 and kk<=m): continue
            w,u,v=r;x=np.array([0.3,0,0,0.7]);psi,chi,dpsi,dchi=fields(x,[(kk,w,u,v)])
            e1=sum(1j*sbu[a]@dpsi[a] for a in range(4))-m*chi;e2=s*sum(1j*su[a]@dchi[a] for a in range(4))-m*psi
            res_eq=max(res_eq,np.abs(e1).max(),np.abs(e2).max())
            j=np.array([(psi.conj()@sbu[a]@psi).real for a in range(4)])+s*np.array([(chi.conj()@su[a]@chi).real for a in range(4)])
            T=Tsym(psi,dpsi,sbl)+s*Tsym(chi,dchi,sl);tr=np.trace(eta@T)
            rows.append(dict(k=kk,lam=lam,w2=w*w,disp_res=abs(w*w-(kk*kk+m*m/s)),j=np.round(j,6).tolist(),j_rel=float(np.abs(j).max()/(abs(psi@psi.conj())+abs(chi@chi.conj()))),
                             weight=float(abs(chi@chi.conj())/abs(psi@psi.conj())),T_tt=T[0,0],T_tz=T[0,3],T_zz=T[3,3],T_xx=T[1,1],spur=tr))
    out[name]=dict(eq_res=res_eq,modes=rows)
# Kontrolle Erhaltung: Ueberlagerung zweier Moden (V2 und V1)
for name,s,ks in (('V1',1,(0.5,2.0)),('V2',-1,(1.5,3.0))):
    ms=[(k,)+mode(k,1,s) for k in ks];h=1e-4;worst=0
    for x in np.random.default_rng(1).uniform(-2,2,(10,4)):
        div=np.zeros(4)
        for mu in range(4):
            e=np.zeros(4);e[mu]=h
            Tp=Tsym(*fields(x+e,ms)[0:3:2],sbl)+s*Tsym(*fields(x+e,ms)[1:4:2],sl);Tm=Tsym(*fields(x-e,ms)[0:3:2],sbl)+s*Tsym(*fields(x-e,ms)[1:4:2],sl)
            div+=eta[mu,mu]*(Tp-Tm)[mu]/(2*h)
        T0=Tsym(*fields(x,ms)[0:3:2],sbl)+s*Tsym(*fields(x,ms)[1:4:2],sl);worst=max(worst,np.abs(div).max()/np.abs(T0).max())
    out[name]['conservation_rel']=worst
json.dump(out,open('k179_out.json','w'),indent=1,default=float)
for name in ('V1','V2'):
    o=out[name];print(name,'Feldgl.-Residuum',f"{o['eq_res']:.1e}",'Erhaltung',f"{o['conservation_rel']:.1e}")
    for r in o['modes']: print(f"  k={r['k']:4.1f} lam={r['lam']:+d} w2={r['w2']:+.3f} disp_res={r['disp_res']:.0e} |j|/dicht={r['j_rel']:.3f} j={r['j']} Gewicht={r['weight']:.4f} Ttt={r['T_tt']:+.3f} Tzz={r['T_zz']:+.3f} Txx={r['T_xx']:+.3f} Spur={r['spur']:+.3f}")
