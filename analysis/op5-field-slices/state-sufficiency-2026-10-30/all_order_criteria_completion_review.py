"""Independent NumPy multivariate completed-series check; no Torch derivatives."""
from pathlib import Path
import importlib.util,itertools,json,math,numpy as np,hashlib
W=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('criteria_model',W/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);model=m.TaylorModel(5)
idx=model.idx;look=model.lookup;fullidx=model.fullidx;full=model.full
Q=model.Q.numpy();KK=model.K.numpy();Y=model.Y.numpy();Z=np.kron(np.diag([1,-1,0]),np.array(model.ns['beta'],complex))
def realmat(C):return np.block([[C.real,-C.imag],[C.imag,C.real]])
Hb=np.array([realmat(-1j*KK[0])]+[realmat(1j*v) for v in KK[1:]])
splits=[]
for a in idx:
 splits.append([(look[b],look[tuple(x-y for x,y in zip(a,b))]) for b in idx if all(y<=x for x,y in zip(a,b))])
def evaluate(coeff,bg,maxorder=4):
 ids=[n for n,a in enumerate(idx) if sum(a)<=maxorder];N=len(ids)
 ps=coeff[:N];js=np.zeros((N,4,12),complex)
 for n,a in enumerate(idx[:N]):
  for mu in range(4):
   b=list(a);b[mu]+=1;js[n,mu]=b[mu]*coeff[full[tuple(b)]]
 conn=bg[:N,1:].reshape(N,4,12,12);cov=js.copy()
 for n in range(N):
  for i,j in splits[n]:cov[n]+=1j*np.einsum('mij,j->mi',conn[i],ps[j])
 E=np.zeros((N,4,4));V=np.zeros_like(E)
 for n in range(N):
  for i,j in splits[n]:E[n]+=np.einsum('i,aij,mj->am',ps[i].conj(),Q,cov[j]).real
 V[0]=np.linalg.inv(E[0])
 for n in range(1,N):V[n]=-V[0]@sum((E[i]@V[j] for i,j in splits[n] if i),np.zeros((4,4)))
 F=np.zeros((N,12),complex)
 for n in range(N):
  for i,j in splits[n]:F[n]+=1j*np.einsum('ma,aij,mj->i',V[i],KK,cov[j])-bg[i,0].real*(Y@ps[j])
 Fp=np.concatenate((F.real,F.imag),axis=1)
 aa=np.einsum('ki,aij->kaj',ps.conj(),Q);Am=np.concatenate((aa.real,-aa.imag),axis=2);bar=np.einsum('kma,aij->kmij',V,Hb)
 K=np.zeros((N,4,4,24))
 for n in range(N):
  for i,j in splits[n]:K[n]+=np.einsum('ai,mij->maj',Am[i],bar[j])
 gp=np.zeros(N)
 for n in range(N):
  for i,j in splits[n]:
   for l,r in splits[j]:gp[n]-=.5*bg[i,0].real*np.vdot(ps[l],Z@ps[r]).real
 gp[0]+=4
 out=np.zeros((len(m.indices(maxorder-1)),32))
 for n,a in enumerate(idx[:len(out)]):
  G=np.zeros(4)
  for i,j in splits[n]:
   aj=idx[j]
   for mu in range(4):
    b=list(aj);b[mu]+=1;G+=K[i,mu]@(b[mu]*Fp[look[tuple(b)]])
  C=np.zeros(4)
  for mu in range(4):
   b=list(a);b[mu]+=1;C[mu]=b[mu]*gp[look[tuple(b)]]
  out[n]=np.r_[Fp[n],G,C]
 return out
raw=json.loads((W/'fifth-window-result.json').read_text())['results'][0];packed=np.array(raw['coefficients_real_imag']);c=packed[:,:12]+1j*packed[:,12:]
for n,a in enumerate(fullidx):
 if sum(a)>3:c[n]=0
bg=model.background(raw['point']).numpy();base=evaluate(c,bg);rows=[n for n,a in enumerate(idx) if sum(a)==3];low=[n for n,a in enumerate(idx) if sum(a)<3]
wpath=W/'completion-omega-witness.npz'
if not wpath.exists():raise FileNotFoundError('Request parent witness serialization first')
w=np.load(wpath);v=w['third_direction'];lam=w['ambient_left_witness'];tests=[]
thirdids=[n for n,a in enumerate(fullidx) if sum(a)==3];vz=v.reshape(20,24);delta=vz[:,:12]+1j*vz[:,12:]
for eps in [1e-3,1e-4,1e-5]:
 cp=c.copy();cm=c.copy();cp[thirdids]+=eps*delta;cm[thirdids]-=eps*delta
 rp=evaluate(cp,bg);rm=evaluate(cm,bg);slope=(rp[rows].flatten()-rm[rows].flatten())/(2*eps)
 tests.append({'step':eps,'left_slope':float(lam@slope),'lower_R_change':float(np.linalg.norm(rp[low]-base[low])),'affine_central_error':float(np.linalg.norm(rp+rm-2*base))})
 print(tests[-1],flush=True)
# Highest fifth-jet dependence must cancel from completed residual degree3.
cancel=[]
for n in [70,100,125]:
 cp=c.copy();cp[n,0]+=.01;cancel.append(float(np.linalg.norm(evaluate(cp,bg)-base)))
out={'contract':'Separate NumPy multivariate convolution and recurrence inverse for completedR, derivative source witness on point0. Uses original background coefficient values but no target AD or completedseries implementation. Fixed lower0..2; finite directional derivative checks and highest cancellation.','inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [W/'recursive_calibrator.py',W/'fifth-window-result.json',wpath,Path(__file__)]},'base_R_norm':float(np.linalg.norm(base[0])),'base_left_source':float(lam@base[rows].flatten()),'tests':tests,'fifth_jet_cancellation_errors':cancel}
(W/'all_order_criteria_completion_review-result.json').write_text(json.dumps(out,indent=2))
