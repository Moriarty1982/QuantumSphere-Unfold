"""k145 (Erkundung): Wo wirken die vier Bedingungen? Ebene Wellen xi^6 (x) u in der Symbolfaser G6 (Punkt 1), xi auf
Lichtkegel, den Ebenen Pi0, Pi1 oder generisch. Aufruf: python k145_charakteristik.py <Ordner>"""
import sys,math,numpy as np
from pathlib import Path
here=Path(__file__).parent;D=Path(sys.argv[1]);sys.path.insert(0,str(here));import k138_tps_d as T
w=np.load(D/'completion-omega-witness.npz');J=w['completed_first_symbol'];th=w['theta_normalized'];wg=np.load(here/'k136_eichdaten.npy')[1]
p,psi=T.load_germ(D,5);G6=np.load(here/'k144_p1'/'G6.npy');Wc=np.load(here/'k144_p1'/'w.npy')
n5=len([a for a in T.monos(5) if sum(a)==5])*24;c6=[a for a in T.monos(6) if sum(a)==6]
# Koframe am Keim
bg=T.Background(p,0);I=T.index(5);ps=psi[0];j=[psi[I[tuple(1 if k==m else 0 for k in range(4))]] for m in range(4)]
cov=[j[m]+1j*bg.conn[m][0]@ps for m in range(4)];E=np.array([[np.real(ps.conj()@T.Qm[a]@cov[m]) for m in range(4)] for a in range(4)]);V=np.linalg.inv(E)
eta=np.diag([1,-1,-1,-1.]);q=lambda x:(V.T@x)@eta@(V.T@x)
i3=[tuple(sorted(c)) for c in __import__('itertools').combinations_with_replacement(range(4),3)]
def thx(x): return sum(th[b*24:(b+1)*24]*math.prod(x[m] for m in bt)/math.prod(math.factorial(bt.count(m)) for m in range(4)) for b,bt in enumerate(i3))
def S(x): return np.vstack([sum(x[m]*J[:,m*24:(m+1)*24] for m in range(4)),thx(x)[None],wg[None]])
def wave(x,u):  # ausgeglichene Koordinaten: b_alpha = x^alpha/sqrt(alpha!) u
    v=np.concatenate([math.prod(x[m]**a[m] for m in range(4))/math.sqrt(math.prod(math.factorial(k) for k in a))*u for a in c6])
    return np.r_[np.zeros(n5),v]
def probe(x,label):
    x=x/np.linalg.norm(x);s,Vt=np.linalg.svd(S(x))[1:];k=int(np.sum(s/s[0]<1e-7))
    if k==0: print(f'{label:12s} q={q(x):+.2e}  sigma_min={s[-1]/s[0]:.1e}  kein Kern');return
    out=[]
    for u in Vt[-k:]:
        b=wave(x,u);b/=np.linalg.norm(b);res=np.linalg.norm(b-G6@(G6.T@b));out.append((res,np.abs(Wc.T@b)))
    print(f'{label:12s} q={q(x):+.2e}  Kern {k}; Rest in G6 {max(o[0] for o in out):.1e}; |Bedingungen| max {max(o[1].max() for o in out):.2e}',flush=True)
rng=np.random.default_rng(3)
for i in range(3): probe(rng.normal(size=4),'generisch')
for i in range(4):  # Kegel: xi0 aus q = 0
    sp=rng.normal(size=3);f=lambda t:q(np.r_[t,sp]);a=(f(1)+f(-1)-2*f(0))/2;b=(f(1)-f(-1))/2;c=f(0)
    for t in np.roots([a,b,c]).real[:1]: probe(np.r_[t,sp],'Kegel')
# Ebenen: Minimum von sigma_min abseits des Kegels
from scipy.optimize import minimize
pts=[]
for i in range(60):
    x0=rng.normal(size=4);r=minimize(lambda x:np.linalg.svd(S(x/np.linalg.norm(x)),compute_uv=False)[-1]/np.linalg.svd(S(x/np.linalg.norm(x)),compute_uv=False)[0],x0,method='Nelder-Mead',options=dict(xatol=1e-12,fatol=1e-16,maxiter=4000))
    x=r.x/np.linalg.norm(r.x)
    if r.fun<1e-9 and abs(q(x))>1e-3: pts.append(x)
print('Punkte abseits des Kegels mit Kern:',len(pts))
for x in pts[:6]: probe(x,'Ebene?')
np.save(here/'k145_ebenenpunkte.npy',np.array(pts))
# Wie viele der Kegel-Polarisationen legen die Bedingungen fest? Rang der 4 x k-Matrix je Richtung
print('Kegel: Rang der Bedingungen auf den Polarisationen je Richtung')
for i in range(8):
    sp=rng.normal(size=3);f=lambda t:q(np.r_[t,sp]);a=(f(1)+f(-1)-2*f(0))/2;b=(f(1)-f(-1))/2;c=f(0)
    for t in np.roots([a,b,c]).real:
        x=np.r_[t,sp];x/=np.linalg.norm(x);s,Vt=np.linalg.svd(S(x))[1:];k=int(np.sum(s/s[0]<1e-7))
        Mx=np.array([Wc.T@(lambda b:b/np.linalg.norm(b))(wave(x,u)) for u in Vt[-k:]]).T
        sv=np.linalg.svd(Mx,compute_uv=False);print(f'   Kern {k}, Singulaerwerte {np.array2string(sv/ max(sv[0],1e-300),precision=2)} (abs. {sv[0]:.1e})')
# Vektorstruktur: Bildrichtung n(xi) (4-Vektor in der Bedingungsbasis) proportional zu L xi fuer festes L?
ns=[];xs=[]
while len(ns)<40:
    sp=rng.normal(size=3);f=lambda t:q(np.r_[t,sp]);a=(f(1)+f(-1)-2*f(0))/2;b=(f(1)-f(-1))/2;c=f(0)
    for t in np.roots([a,b,c]).real:
        x=np.r_[t,sp];x/=np.linalg.norm(x);s,Vt=np.linalg.svd(S(x))[1:];k=int(np.sum(s/s[0]<1e-7))
        Mx=np.array([Wc.T@(lambda b:b/np.linalg.norm(b))(wave(x,u)) for u in Vt[-k:]]).T;U,sv,_=np.linalg.svd(Mx)
        if sv[0]>1e-2: ns.append(U[:,0]);xs.append(x)
def fitL(ns,xs):
    rows=[]
    for n,x in zip(ns,xs):
        P=np.eye(4)-np.outer(n,n)          # (I - n n^T) L x = 0
        rows.append(np.kron(P,x[None,:]))
    A=np.vstack(rows);s,Vt=np.linalg.svd(A)[1:];return Vt[-1].reshape(4,4),s
L,s=fitL(ns[:30],xs[:30]);print('Fit L an 30 Nullrichtungen: kleinste Singulaerwerte',np.array2string(s[-3:]/s[0],precision=2))
for n,x in list(zip(ns,xs))[30:34]:
    y=L@x;print('   Test: |sin(n, L xi)| =',f'{np.linalg.norm(y-n*(n@y))/np.linalg.norm(y):.1e}')
Vr=np.linalg.inv(V);print('L in Rahmenkomponenten (eta = V^T xi):\n',np.array2string((L@np.linalg.inv(V.T))/np.max(abs(L@np.linalg.inv(V.T))),precision=3,suppress_small=True))
np.save(here/'k145_L.npy',L)
# Quadratische Struktur: n(xi) proportional zu M m2(xi), m2 = die 10 quadratischen Monome
m2=lambda x:np.array([x[i]*x[j] for i in range(4) for j in range(i,4)])
def fitM(ns,xs,deg):
    f=m2 if deg==2 else (lambda x:x)
    A=np.vstack([np.kron(np.eye(4)-np.outer(n,n),f(x)[None,:]) for n,x in zip(ns,xs)]);s,Vt=np.linalg.svd(A)[1:]
    return Vt[-1].reshape(4,-1),s
while len(ns)<70:
    sp=rng.normal(size=3);f=lambda t:q(np.r_[t,sp]);a=(f(1)+f(-1)-2*f(0))/2;b=(f(1)-f(-1))/2;c=f(0)
    for t in np.roots([a,b,c]).real:
        x=np.r_[t,sp];x/=np.linalg.norm(x);s,Vt=np.linalg.svd(S(x))[1:];k=int(np.sum(s/s[0]<1e-7))
        Mx=np.array([Wc.T@(lambda b:b/np.linalg.norm(b))(wave(x,u)) for u in Vt[-k:]]).T;U,sv,_=np.linalg.svd(Mx)
        if sv[0]>1e-2: ns.append(U[:,0]);xs.append(x)
M,s=fitM(ns[:50],xs[:50],2);print('Fit M (4x10) an 50 Nullrichtungen: kleinste Singulaerwerte',np.array2string(s[-3:]/s[0],precision=2))
print('   Gegenprobe |sin(n, M m2(xi))| an 20 neuen:',np.array2string(np.array([np.linalg.norm(M@m2(x)-n*(n@(M@m2(x))))/np.linalg.norm(M@m2(x)) for n,x in zip(ns[50:70],xs[50:70])]),precision=1))
np.save(here/'k145_M.npy',M)
# Ebenen Pi0, Pi1 unabhaengig: J(xi) (ohne theta, ohne Eichung) mit zweidimensionalem Kern abseits des Kegels
JJ=lambda x:sum(x[m]*J[:,m*24:(m+1)*24] for m in range(4))
def s2(x): x=x/np.linalg.norm(x);s=np.linalg.svd(JJ(x),compute_uv=False);return s[-2]/s[0]
P=[]
for i in range(150):
    r=minimize(s2,rng.normal(size=4),method='Nelder-Mead',options=dict(xatol=1e-12,fatol=1e-18,maxiter=6000));x=r.x/np.linalg.norm(r.x)
    if r.fun<1e-8 and abs(q(x))>1e-3: P.append(x)
P=np.array(P);print('Punkte mit zweitem Kernvektor abseits des Kegels:',len(P))
best=[]
for i in range(len(P)):
    for j in range(i+1,len(P)):
        B=np.linalg.qr(np.c_[P[i],P[j]])[0];res=np.linalg.norm(P-(P@B)@B.T,axis=1);inl=res<1e-6
        if inl.sum()>2 and np.linalg.svd(np.c_[P[i],P[j]],compute_uv=False)[-1]>1e-3: best.append((inl.sum(),i,j,inl))
best.sort(key=lambda t:-t[0]);planes=[];used=np.zeros(len(P),bool)
for n,i,j,inl in best:
    if used[i] or used[j]: continue
    planes.append(np.linalg.qr(np.c_[P[i],P[j]])[0]);used|=inl
    if len(planes)==2: break
if len(planes)==1:
    rest=P[np.linalg.norm(P-(P@planes[0])@planes[0].T,axis=1)>1e-6]
    if len(rest)>=2 and np.linalg.svd(rest[:2].T,compute_uv=False)[-1]>1e-3:
        B=np.linalg.qr(rest[:2].T)[0];chk=[s2(B@rng.normal(size=2)) for _ in range(6)];print('zweite Ebene aus',len(rest),'Restpunkten; s2 an Zufallskombinationen:',np.array2string(np.array(chk),precision=1))
        if max(chk)<1e-7: planes.append(B)
    chk1=[s2(planes[0]@rng.normal(size=2)) for _ in range(6)];print('erste Ebene: s2 an Zufallskombinationen:',np.array2string(np.array(chk1),precision=1))
print('Ebenen gefunden:',len(planes),' Punkte je Ebene:',[int(np.sum(np.linalg.norm(P-(P@B)@B.T,axis=1)<1e-6)) for B in planes],' von',len(P))
if len(planes)==2:
    A0=np.linalg.svd(planes[0].T)[2][2:];A1=np.linalg.svd(planes[1].T)[2][2:]   # je zwei Linearformen, die die Ebene ausschneiden
    sym=lambda l,m:np.array([(l[i]*m[j]+l[j]*m[i]) if i!=j else l[i]*m[i] for i in range(4) for j in range(i,4)])
    Dq=np.array([sym(l,m) for l in A0 for m in A1])
    qc=np.array([(lambda Qm:(Qm[i,j]*(2 if i!=j else 1)))(V@eta@V.T) for i in range(4) for j in range(i,4)])
    Mq=np.vstack([M,qc]);r1=np.linalg.svd(Mq,compute_uv=False);r2=np.linalg.svd(np.vstack([Mq,Dq]),compute_uv=False)
    print('Singulaerwerte [M; q]:',np.array2string(r1/r1[0],precision=2),' [M; q; D]:',np.array2string(r2/r2[0],precision=2))
    proj=Dq-(Dq@np.linalg.pinv(Mq))@Mq;print('Anteil von D ausserhalb span(M, q):',f'{np.linalg.norm(proj)/np.linalg.norm(Dq):.1e}')
