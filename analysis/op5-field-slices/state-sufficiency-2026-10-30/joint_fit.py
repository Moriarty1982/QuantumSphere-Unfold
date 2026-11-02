"""Bounded simultaneous finite 2-jet fit. Run python joint_fit.py; no repo writes."""
from pathlib import Path
import os
os.environ['OMP_NUM_THREADS']='2'
os.environ['OPENBLAS_NUM_THREADS']='2'
import numpy as np, torch as T, sympy as s, json,time,hashlib,sys,platform
from datetime import datetime,timezone
T.set_num_threads(2); T.set_default_dtype(T.float64)
ROOT=Path(__file__).resolve().parent
REPO=Path(r'C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold')
AREA=REPO/'analysis/op5-field-slices'
paths=[REPO/'analysis/OP5_Counterflow_Full_Residual_Check.py',AREA/'OP5_Joint_Compatibility_Lower_Data.json',AREA/'OP5_Joint_Compatibility_Second_Jet_Check.json',Path(__file__).resolve()]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
ns={};exec(paths[0].read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
coords=[ns[v] for v in ('t','x','y','z')]
K=np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']])
QQ=np.array([np.kron(np.array(ns['S'],complex),v) for v in K])
KK=np.array([np.kron(np.eye(3),v) for v in K]);YY=np.kron(np.array(ns['Y'],complex),np.array(ns['beta'],complex))
Ag=[s.zeros(12)]+[s.kronecker_product(ns['G']*v,s.eye(4)) for v in ns['spin']]
bg=s.Matrix([ns['hm']]+[v for mat in Ag for v in mat])
bgfun=s.lambdify(coords,bg,'numpy',cse=True)
bgjac=s.lambdify(coords,bg.jacobian(coords),'numpy',cse=True)
data=json.loads(paths[1].read_text()); prev=json.loads(paths[2].read_text())
pairs=[(i,j) for i in range(4) for j in range(i,4)]
picker=np.empty((4,4),int)
for n,(i,j) in enumerate(pairs):picker[i,j]=picker[j,i]=n
Q=T.tensor(QQ);Kt=T.tensor(KK);Y=T.tensor(YY)
pack=lambda v:np.r_[v.real.ravel(),v.imag.ravel()]
def c24(v):return T.complex(v[:12],v[12:])
def c96(v):return T.complex(v[:48],v[48:]).reshape(4,12)
def tcpack(v):return T.cat((v.real.flatten(),v.imag.flatten()))
rows=[];start=time.time();started=datetime.now(timezone.utc).isoformat()
for ip,row in enumerate(data['results']):
 pos=np.array([float(s.sympify(row['point'][str(v)])) for v in coords])
 psi=np.array([complex(*v) for v in row['field_values_real_imag']])
 jets=np.array([complex(*v) for v in row['attempts'][0]['all_jets']]).reshape(4,12)
 bg0=np.asarray(bgfun(*pos),complex).ravel(); db=np.asarray(bgjac(*pos),complex)
 bt=T.tensor(bg0);dt=T.tensor(db);pt=T.tensor(pos);psit=T.tensor(pack(psi))
 def evaluate(q,coframe=False):
  p=c24(q[:24]);j=c96(q[24:120]);b=bt+dt@(q[120:]-pt).to(T.complex128)
  h=b[0].real;conn=b[1:].reshape(4,12,12)
  cov=j+1j*T.einsum('mij,j->mi',conn,p)
  E=T.einsum('i,aij,mj->am',p.conj(),Q,cov).real
  inv=T.linalg.inv(E)
  F=1j*T.einsum('ma,aij,mj->i',inv.to(T.complex128),Kt,cov)-h*(Y@p)
  return E if coframe else tcpack(F)
 q0=T.cat((psit,T.tensor(pack(jets)),pt));E0=evaluate(q0,True)[:,0].detach()
 D=T.func.jacrev(evaluate)
 def equations(z):
  j=c96(z[:96]);q=T.cat((psit,z[:96],pt));H=z[96:].reshape(10,24)
  hc=T.complex(H[:,:12],H[:,12:])[T.tensor(picker)]
  # Column mu is derivative of packed q along coordinate mu.
  tangent=T.cat((T.cat((j.real.T,j.imag.T),dim=0),T.cat((hc.real.permute(1,2,0).reshape(48,4),hc.imag.permute(1,2,0).reshape(48,4)),dim=0),T.eye(4)),dim=0)
  return T.cat((evaluate(q),(D(q)@tangent).T.flatten(),evaluate(q,True)[:,0]-E0))
 saved=next(v for v in prev['results'] if v['point_index']==ip and v['attempt']==0)['tests'][1]['symmetric_second_jets']
 z=np.r_[pack(jets),saved];initial=z.copy();history=[]
 fun=lambda v:equations(T.tensor(v)).detach().numpy()
 jac=T.func.jacrev(equations)
 initial_r=fun(z);print('point',ip,'initial',np.linalg.norm(initial_r[:24]),np.linalg.norm(initial_r[24:120]),flush=True)
 damp=1e-7
 for it in range(16):
  rr=fun(z);J=jac(T.tensor(z)).detach().numpy();JJ=J@J.T
  accepted=False
  for trial in range(9):
   step=-J.T@np.linalg.solve(JJ+damp*np.eye(len(rr)),rr)
   cand=z+step
   try:
    rn=fun(cand);q=T.cat((psit,T.tensor(cand[:96]),pt));ee=evaluate(q,True).detach().numpy();iv=np.linalg.inv(ee);g00=float(iv[0]@np.diag([-1,1,1,1])@iv[0])
    good=np.linalg.norm(rn)<np.linalg.norm(rr) and abs(np.linalg.det(ee))>1e-5 and g00<-.01
   except Exception:good=False
   if good:z=cand;damp=max(damp/3,1e-14);accepted=True;break
   damp*=10
  history.append({'iteration':it,'accepted':accepted,'norm':float(np.linalg.norm(fun(z))),'damping':damp,'step_norm':float(np.linalg.norm(step))})
  print(ip,it,history[-1],flush=True)
  (ROOT/'joint-fit-progress.json').write_text(json.dumps({'point':ip,'history':history},indent=2))
  if np.linalg.norm(fun(z))<1e-9 or not accepted:break
 # Independent NumPy direct evaluator and Taylor finite-difference prolongation.
 jj=(z[:48]+1j*z[48:96]).reshape(4,12);hh=z[96:].reshape(10,24);hc=(hh[:,:12]+1j*hh[:,12:])[picker]
 def original(pp,ps,js):
  bb=np.asarray(bgfun(*pp),complex).ravel();cov=js+1j*np.einsum('mij,j->mi',bb[1:].reshape(4,12,12),ps)
  ee=np.einsum('i,aij,mj->am',ps.conj(),QQ,cov).real;iv=np.linalg.inv(ee)
  f=1j*np.einsum('ma,aij,mj->i',iv,KK,cov)-bb[0].real*YY@ps
  return pack(f),ee
 f,ee=original(pos,psi,jj);controls=[]
 for eps in [1e-4,1e-5,1e-6]:
  deriv=[]
  for mu in range(4):
   dx=np.eye(4)[mu]*eps
   fp=original(pos+dx,psi+eps*jj[mu]+.5*eps**2*hc[mu,mu],jj+eps*hc[mu])[0]
   fm=original(pos-dx,psi-eps*jj[mu]+.5*eps**2*hc[mu,mu],jj-eps*hc[mu])[0]
   deriv.append((fp-fm)/(2*eps))
  controls.append({'step':eps,'full_derivative_norm':float(np.linalg.norm(deriv)),'difference_from_AD':float(np.linalg.norm(np.array(deriv).ravel()-fun(z)[24:120]))})
 rr=fun(z);iv=np.linalg.inv(ee)
 rows.append({'point':pos.tolist(),'initial_F_norm':float(np.linalg.norm(initial_r[:24])),'initial_prolongation_norm':float(np.linalg.norm(initial_r[24:120])),'F_norm':float(np.linalg.norm(f)),'AD_prolongation_norm':float(np.linalg.norm(rr[24:120])),'E0_fix_norm':float(np.linalg.norm(rr[120:])),'detE':float(np.linalg.det(ee)),'g00':float(iv[0]@np.diag([-1,1,1,1])@iv[0]),'first_jet_change':float(np.linalg.norm(z[:96]-initial[:96])),'second_jet_norm':float(np.linalg.norm(z[96:])),'history':history,'controls':controls,'first_jets_packed':z[:96].tolist(),'symmetric_second_jets':z[96:].tolist()})
 out={'contract':'Fixed psi, original backgrounds and couplings; vary 96 real first jets and240 real symmetric second jets; fit full F24+prolongation96+time coframe4; no derivatives of time coframe prescribed. Float64 bounded damped minimum-norm steps. No regional existence claim.','results':rows,'started_at':started,'seconds':time.time()-start,'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in paths),'software':{'python':platform.python_version(),'torch':T.__version__,'numpy':np.__version__,'sympy':s.__version__}}
 (ROOT/'joint-fit-result.json').write_text(json.dumps(out,indent=2))
 print('DONE POINT',ip,rows[-1]['F_norm'],rows[-1]['AD_prolongation_norm'],controls,flush=True)
