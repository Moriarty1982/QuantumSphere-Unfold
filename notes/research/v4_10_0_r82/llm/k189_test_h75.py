"""k189: Test der Vorab-Notiz H75 (Commit 6aa8477). Newtonsche Zwei-Flussigkeiten-Stoerungen und Bondi-Paar."""
import numpy as np, json
from scipy.linalg import expm
out={};x=0.5493**2
def lin(N,T=50.0):
    A=np.zeros((4,4));A[:2,2:]=np.eye(2);A[2:,:2]=N
    ts=np.linspace(0,T,501);X0=np.array([1e-3,-1e-3,0,0]);Y=np.array([expm(A*t)@X0 for t in ts])
    ev=np.linalg.eigvals(A);return ts,Y,float(max(ev.real))
# a Photon-Gewichte
N=np.array([[1.,-1.],[1.,-1.]]);ts,Y,lam=lin(N);rel=np.abs(Y[:,0]-Y[:,1]);out['a']=dict(max_exponent=lam,N2_null=float(np.abs(N@N).max()),rel_mode_t50=float(rel[-1]),rel_ueber_t=float(rel[-1]/50),dA_t50=float(Y[-1,0]))
# b Materie-Gewichte und Kontrolle
N=np.array([[1.,-x],[1.,-x]]);_,_,lam=lin(N);out['b_materie']=dict(rate=lam,vorhergesagt=float(np.sqrt(1-x)))
N=np.array([[1.,x],[1.,x]]);_,_,lam=lin(N);out['b_kontrolle_normal']=dict(rate=lam,vorhergesagt=float(np.sqrt(1+x)))
# c Bondi-Paar: Massen m1=+1 (traege und schwer), m2=-1; a_i = sum_j G m_j (x_j-x_i)/|..|^3 (traege Masse kuerzt sich, a haengt nur von Quellmassen ab)
G=1.0;m=np.array([1.,-1.]);xs=np.array([0.,1.]);vs=np.zeros(2);dt=1e-3;acc=[];dist=[]
def a(xs):
    d=xs[1]-xs[0];return np.array([G*m[1]*np.sign(d)/d**2,-G*m[0]*np.sign(d)/d**2])
for i in range(20000):
    k=a(xs);vs=vs+dt*k;xs=xs+dt*vs;acc.append(k.copy());dist.append(xs[1]-xs[0])
acc=np.array(acc);dist=np.array(dist)
P=np.sum(m*vs);E=0.5*np.sum(m*vs**2)-G*m[0]*m[1]/(xs[1]-xs[0])
out['c']=dict(abstand_abw=float(np.ptp(dist)),beschl=acc[-1].tolist(),beschl_abw=float(np.ptp(acc)),impuls=float(P),energie=float(E),geschw_ende=vs.tolist())
json.dump(out,open('k189_out.json','w'),indent=1,default=float)
for k,v in out.items(): print(k,':',{a:(round(b,8) if isinstance(b,float) else b) for a,b in v.items()})
