"""k175: Test der Vorab-Notiz H69 (Commit dbcc40d). Versetztes M-T-Paar in W1, flach, A = 0.
psi_M = a e^{-i w1 (t-z)} u1 + b e^{-i w2 (t+z)} u2 (linkshaendig, sigmabar = (1,-sigma)), psi_T(x) = -i sigma_z psi_M(x + delta e_t), s_T = -1."""
import numpy as np, json
rng=np.random.default_rng(69)
I=np.eye(2);sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1]).astype(complex)
sbu=[I,-sx,-sy,-sz];sbl=[I,sx,sy,sz];eta=np.diag([1.,-1,-1,-1])
u1=np.array([0,1],complex);u2=np.array([1,0],complex)
a,b=rng.normal()+1j*rng.normal(),rng.normal()+1j*rng.normal();w1,w2=rng.uniform(0.5,2.0,2)
def field(x,d=0.):
    t,_,_,z=x;t=t+d
    e1=a*np.exp(-1j*w1*(t-z))*u1;e2=b*np.exp(-1j*w2*(t+z))*u2
    psi=e1+e2
    dpsi=np.array([-1j*w1*e1-1j*w2*e2,0*psi,0*psi,1j*w1*e1-1j*w2*e2])   # d_t, d_x, d_y, d_z
    return psi,dpsi
R=-1j*sz
def MT(x,delta):
    pM,dM=field(x);pT0,dT0=field(x,delta);pT=R@pT0;dT=np.array([R@v for v in dT0]);return pM,dM,pT,dT
cur=lambda p:np.array([(p.conj()@m@p).real for m in sbu])
def Tmn(p,dp):
    X=np.array([[p.conj()@sbl[m]@dp[n] for n in range(4)] for m in range(4)]);X=X+X.T
    return (1j/4*(X-X.conj())).real
weyl=lambda p,dp:np.abs(sum(sbu[m]@dp[m] for m in range(4))).max()
pts=rng.uniform(-5,5,size=(400,4));sT=-1;out={'params':dict(w1=w1,w2=w2,a=str(a),b=str(b))}
# Kontrollen
dw=w1-w2;delta=np.pi/dw
out['weyl_res']=max(max(weyl(*MT(x,delta)[:2]),weyl(*MT(x,delta)[2:])) for x in pts[:50])
out['einframe_j0_min']=min(cur(MT(x,delta)[0])[0] for x in pts)
out['T_sym']=max(np.abs(Tmn(*MT(x,delta)[:2])-Tmn(*MT(x,delta)[:2]).T).max() for x in pts[:20])
h=1e-4;cons=[]
for x in pts[:20]:
    div=np.zeros(4)
    for m in range(4):
        e=np.zeros(4);e[m]=h;Tp=Tmn(*field(x+e));Tm=Tmn(*field(x-e));div+=eta[m,m]*(Tp-Tm)[m]/(2*h)
    cons.append(np.abs(div).max()/np.abs(Tmn(*field(x))).max())
out['conservation_rel']=max(cons)
# H69a
def resid_a(delta):
    r=[];amp=[]
    for x in pts:
        pM,dM,pT,dT=MT(x,delta);jm=cur(pM);r.append(np.abs(jm+sT*cur(pT)).max());amp.append(np.abs(jm[1:3]).max())
    return max(r)/max(amp)
out['H69a']={k:resid_a(v) for k,v in (('dwd=pi',np.pi/dw),('dwd=3pi',3*np.pi/dw),('dwd=0',0.0),('dwd=pi/2',np.pi/(2*dw)))}
# H69b
rb=[];nm=[]
for x in pts:
    pM,dM,pT,dT=MT(x,delta);TM=Tmn(pM,dM);TT=Tmn(pT,dT);rb.append(np.abs(TM+sT*TT).max());nm.append(np.abs(TM).max())
out['H69b_rel']=max(rb)/max(nm)
# Bericht: welche Komponenten bleiben (bei einem Punkt)
pM,dM,pT,dT=MT(pts[0],delta);out['H69b_rest_example']=np.round(Tmn(pM,dM)+sT*Tmn(pT,dT),6).tolist();out['TM_example']=np.round(Tmn(pM,dM),6).tolist()
json.dump(out,open('k175_out.json','w'),indent=1,default=float)
for k,v in out.items():
    if k not in('H69b_rest_example','TM_example','params'): print(k,v)
print('Rest T bei einem Punkt:\n',np.round(np.array(out['H69b_rest_example']),4),'\nT^M:\n',np.round(np.array(out['TM_example']),4))
