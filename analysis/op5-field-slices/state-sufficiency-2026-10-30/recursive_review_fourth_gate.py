"""Frozen successful3jets: independent scalar third-derivative gate for fourth completion."""
from pathlib import Path
import json,itertools,math,hashlib,numpy as np,sympy as s
W=Path(__file__).resolve().parent;R=next(q for q in [Path.cwd(),*W.parents] if (q/'analysis/OP5_Counterflow_Full_Residual_Check.py').exists())
source=R/'analysis/OP5_Counterflow_Full_Residual_Check.py'
ns={};exec(source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
coords=[ns[v] for v in ('t','x','y','z')];pair=list(itertools.combinations_with_replacement(range(4),2));triple=list(itertools.combinations_with_replacement(range(4),3))
Z=np.kron(np.diag([1,-1,0]),np.array(ns['beta'],complex));S=np.kron(np.array(ns['S'],complex),np.eye(4))
hf=s.lambdify(coords,ns['hm'],'numpy');dhf=s.lambdify(coords,[s.diff(ns['hm'],v) for v in coords],'numpy');hhf=s.lambdify(coords,s.hessian(ns['hm'],coords),'numpy');hhhf=s.lambdify(coords,[s.diff(ns['hm'],coords[i],coords[j],coords[k]) for i,j,k in triple],'numpy',cse=True)
lp=R/'analysis/op5-field-slices/OP5_Joint_Compatibility_Lower_Data.json';fp=W/'joint-fit-result.json';tp=W/'third-joint-fit-result.json'
lower=json.loads(lp.read_text())['results'];fit=json.loads(fp.read_text())['results'];new=json.loads(tp.read_text())['results'];rows=[]
def multi(ids):return tuple(ids.count(i) for i in range(4))
zero=(0,0,0,0)
def binomial(alpha,beta):return math.prod(math.comb(a,b) for a,b in zip(alpha,beta))
for ip,row in enumerate(new):
 p=np.array(row['point']);psi=np.array([complex(*v) for v in lower[ip]['field_values_real_imag']]);jp=np.array(fit[ip]['first_jets_packed']);J=(jp[:48]+1j*jp[48:]).reshape(4,12);hp=np.array(row['symmetric_second_jets']).reshape(10,24);H=np.empty((4,4,12),complex)
 for n,(i,j) in enumerate(pair):H[i,j]=H[j,i]=hp[n,:12]+1j*hp[n,12:]
 tpack=np.array(row['tests'][1]['third_jets']).reshape(20,24);T=np.empty((4,4,4,12),complex)
 for ids in itertools.product(range(4),repeat=3):n=triple.index(tuple(sorted(ids)));T[ids]=tpack[n,:12]+1j*tpack[n,12:]
 q=np.vdot(psi,Z@psi).real;dq=np.array([2*np.vdot(psi,Z@v).real for v in J]);ddq=np.array([[2*np.real(np.vdot(J[i],Z@J[j])+np.vdot(psi,Z@H[i,j])) for j in range(4)] for i in range(4)])
 dddq=np.array([2*np.real(np.vdot(psi,Z@T[i,j,k])+np.vdot(J[i],Z@H[j,k])+np.vdot(J[j],Z@H[i,k])+np.vdot(J[k],Z@H[i,j])) for i,j,k in triple])
 # Orthogonal combinatorial check: full multivariate Leibniz derivative on actual derivatives.
 pd={zero:psi}
 for i in range(4):pd[multi((i,))]=J[i]
 for i,j in pair:pd[multi((i,j))]=H[i,j]
 for i,j,k in triple:pd[multi((i,j,k))]=T[i,j,k]
 cq=[]
 for ids in triple:
  alpha=multi(ids);val=0j
  for beta in itertools.product(*[range(n+1) for n in alpha]):
   gamma=tuple(a-b for a,b in zip(alpha,beta));val+=binomial(alpha,beta)*np.vdot(pd[beta],Z@pd[gamma])
  cq.append(val.real)
 assert np.linalg.norm(dddq-np.array(cq))<1e-10
 h=float(hf(*p));dh=np.array(dhf(*p));hh=np.array(hhf(*p));hhh=np.array(hhhf(*p))
 dddg=np.array([-.5*(hhh[n]*q+hh[i,j]*dq[k]+hh[i,k]*dq[j]+hh[j,k]*dq[i]+dh[i]*ddq[j,k]+dh[j]*ddq[i,k]+dh[k]*ddq[i,j]+h*dddq[n]) for n,(i,j,k) in enumerate(triple)])
 ddg=-.5*(hh*q+np.outer(dh,dq)+np.outer(dq,dh)+h*ddq)
 ellpsi=S@psi;ellnorm=np.linalg.norm(ellpsi)
 result={'point_index':ip,'point':p.tolist(),'d3g_packed':dddg.tolist(),'d3g_norm':float(np.linalg.norm(dddg)),'d2g_packed_norm':float(np.linalg.norm([ddg[i,j] for i,j in pair])),'ell_norm':float(ellnorm),'raw_d3g_scaled_norm':float(np.linalg.norm(dddg)/ellnorm),'dddq_leibniz_check_error':float(np.linalg.norm(dddq-np.array(cq))),'warning':'raw scaled gate approximates a lower bound only when F,dF,ddF negligible; retain lower-product terms at numerical floor.'}
 rows.append(result);print(result,flush=True)
(W/'recursive-review-fourth-gate-result.json').write_text(json.dumps({'contract':'Independent necessary scalar gate for frozen successful3jet fourth completion, no full fourth-jet solve. Actual derivatives, unweighted symmetric packing.','inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,lp,fp,tp,Path(__file__))},'results':rows},indent=2))
