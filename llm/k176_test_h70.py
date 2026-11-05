"""k176: Test der Vorab-Notiz H70 (Commit 54c354a). Versetztes M-T-Paar auf flachem FRW (konforme Zeit), Kandidaten C1 (delta = c/H),
C2 (konformer Versatz konstant), C3 (delta = t - sqrt(t^2 - beta^2)). Masselose Weyl-Felder, psi = a^{-3/2} chi."""
import numpy as np, json
rng=np.random.default_rng(70)
I=np.eye(2);sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]).astype(complex)
s=[I,sx,sy,sz];sbu=[I,-sx,-sy,-sz];sbl=[I,sx,sy,sz];eta=np.diag([1.,-1,-1,-1]);R=-1j*sz
u1=np.array([0,1],complex);u2=np.array([1,0],complex);A1,A2=rng.normal()+1j*rng.normal(),rng.normal()+1j*rng.normal()
out={}
# ---- Kontrolle 1: konforme Invarianz mit FRW-Spin-Verbindung
def chi(tau,z,w1,w2):
    e1=A1*np.exp(-1j*w1*(tau-z))*u1;e2=A2*np.exp(-1j*w2*(tau+z))*u2
    return e1+e2,np.array([-1j*w1*e1-1j*w2*e2,0*e1,0*e1,1j*w1*e1-1j*w2*e2])
aa=lambda t:1+0.3*t+0.1*t*t;ap=lambda t:0.3+0.2*t
best=[]
for sign in (+1,-1):
    worst=0
    for _ in range(50):
        tau,z=rng.uniform(0.2,3,2);w1,w2=rng.uniform(0.5,2,2);c,dc=chi(tau,z,w1,w2);a=aa(tau);H=ap(tau)/a
        psi=a**-1.5*c;dpsi=a**-1.5*dc;dpsi[0]=dpsi[0]-1.5*H*psi
        w=np.zeros((4,4,4))
        for j in (1,2,3): w[j,0,j]=sign*H;w[j,j,0]=-sign*H      # omega_{mu a b}: (mu=j, a=0, b=j) = +-H
        G=[sum(w[m,p,q]*(s[p]@sbu[q]-s[q]@sbu[p]) for p in range(4) for q in range(4))/8 for m in range(4)]
        res=sum(sbu[m]@(dpsi[m]+G[m]@psi) for m in range(4))/a
        worst=max(worst,np.abs(res).max()/np.abs(dpsi).max())
    best.append(worst)
out['konforme_Invarianz_res']=min(best);out['vorzeichen_omega']='+' if best[0]<best[1] else '-'
# ---- Hintergruende und Kandidaten
cur=lambda p:np.array([(p.conj()@m@p).real for m in sbu])
def Tmn(p,dp):
    X=np.array([[p.conj()@sbl[m]@dp[n] for n in range(4)] for m in range(4)]);X=X+X.T;return (1j/4*(X-X.conj())).real
beta=0.5493;c=0.1
def background(kind):
    p,t0=(2/3,2/3) if kind=='Materie' else (0.5,0.5)
    a_t=lambda t:(t/t0)**p
    tau_t=lambda t:t0**p*t**(1-p)/(1-p)
    t_tau=lambda tau:(tau*(1-p)/t0**p)**(1/(1-p))
    return a_t,tau_t,t_tau,(lambda t:p/t),t0,p
def run(kind,cand,flat=False):
    a_t,tau_t,t_tau,H_t,t0,p=background(kind)
    def dtau(tau):
        if flat: return c
        t=t_tau(tau)
        if cand=='C2': return c
        if cand=='C1': d=c/H_t(t)
        else:
            if t<=beta: return np.nan
            d=t-np.sqrt(t*t-beta*beta)
        return tau_t(t+d)-tau
    tau1=tau_t(t0);D1=dtau(tau1);dw=np.pi/D1;w2=1.0;w1=w2+dw
    Lz=2*np.pi/(w1+w2);zs=np.arange(64)*Lz/64
    taus=np.linspace(tau_t(t0*0.5**(1/p)),tau_t(t0*2**(1/p)),121)
    rW=rJ=rT=0;rMean=0;undef=0;h=1e-6
    for tau in taus:
        D=dtau(tau)
        if not np.isfinite(D): undef+=1;continue
        Dp=(dtau(tau+h)-dtau(tau-h))/(2*h)
        if not np.isfinite(Dp): undef+=1;continue
        Tres=[];Tm=[]
        for z in zs:
            cM,dM=chi(tau,z,w1,w2);cT0,dT0=chi(tau+D,z,w1,w2)
            cT=R@cT0;dT=np.array([R@v for v in dT0]);dT[0]=dT[0]*(1+Dp)
            weylT=np.abs(dT[0]-sz@dT[3]).max()/np.abs(dT).max();rW=max(rW,weylT)
            jM=cur(cM);rJ=max(rJ,np.abs(jM-cur(cT)).max()/max(np.abs(jM[1:3]).max(),1e-300))
            TM=Tmn(cM,dM);TT=Tmn(cT,dT);Tres.append(TM-TT);Tm.append(np.abs(TM).max())
        Tres=np.array(Tres);amp=np.abs(Tres).max();rT=max(rT,amp/max(Tm))
        if amp>1e-14*max(Tm): rMean=max(rMean,np.abs(Tres.mean(0)).max()/amp)
    return dict(weyl_T=rW,strom=rJ,energie=rT,mittel_rel=rMean,undefiniert=undef,dw=dw)
out['Kontrolle_flach_H69']=run('Materie','C2',flat=True)
for kind in ('Materie','Strahlung'):
    for cand in ('C1','C2','C3'):
        out[f'{kind}_{cand}']=run(kind,cand)
json.dump(out,open('k176_out.json','w'),indent=1,default=float)
for k,v in out.items():
    if isinstance(v,dict): print(f'{k:16s}',' '.join(f'{a}={b:.2e}' if isinstance(b,float) else f'{a}={b}' for a,b in v.items()))
    else: print(k,v)
