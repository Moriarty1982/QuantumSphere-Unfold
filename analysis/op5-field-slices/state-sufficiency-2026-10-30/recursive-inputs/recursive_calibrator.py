"""Reusable finite-order Taylor-jet calibrator for the declared OP5 comparison.

Coefficients are derivatives / multiindex factorial, not raw derivatives.
Run: python recursive_calibrator.py --order 4 --points 0 1 2
Only finite numerical compatibility is claimed, never recursive convergence.
"""
from pathlib import Path
import os
os.environ.setdefault('OMP_NUM_THREADS','2');os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import argparse,itertools,math,json,time,hashlib,platform
from datetime import datetime,timezone
import numpy as np,torch as T,sympy as s
T.set_default_dtype(T.float64);T.set_num_threads(2)
ROOT=Path(__file__).resolve().parent
def locate_repo():
 for path in [Path.cwd(),*ROOT.parents]:
  if (path/'analysis/OP5_Counterflow_Full_Residual_Check.py').exists():return path
 raise FileNotFoundError('Run from QuantumSphere-Unfold repository or place artifact inside it')
def indices(order,dim=4):
 out=[]
 for degree in range(order+1):
  for axes in itertools.combinations_with_replacement(range(dim),degree):out.append(tuple(axes.count(mu) for mu in range(dim)))
 return out
def factorial(alpha):return math.prod(math.factorial(v) for v in alpha)
def degree(alpha):return sum(alpha)
def pack(z):return np.concatenate((z.real,z.imag),axis=-1).ravel()
def unpack(v):
 h=v.reshape(-1,24)
 return T.complex(h[:,:12],h[:,12:])
class TaylorModel:
 def __init__(self,order):
  self.order=order;self.m=order-1;self.idx=indices(self.m);self.fullidx=indices(order)
  self.lookup={a:i for i,a in enumerate(self.idx)};self.full={a:i for i,a in enumerate(self.fullidx)}
  pairs=[]
  for ia,a in enumerate(self.idx):
   for ib,b in enumerate(self.idx):
    c=tuple(x+y for x,y in zip(a,b))
    if sum(c)<=self.m:pairs.append((ia,ib,self.lookup[c]))
  self.left=T.tensor([v[0] for v in pairs]);self.right=T.tensor([v[1] for v in pairs]);self.dest=T.tensor([v[2] for v in pairs])
  self.repo=locate_repo();self.source=self.repo/'analysis/OP5_Counterflow_Full_Residual_Check.py'
  ns={};exec(self.source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns);self.ns=ns
  self.coords=[ns[v] for v in ('t','x','y','z')]
  K=np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']]);self.K=T.tensor(np.array([np.kron(np.eye(3),v) for v in K]))
  self.Q=T.tensor(np.array([np.kron(np.array(ns['S'],complex),v) for v in K]));self.Y=T.tensor(np.kron(np.array(ns['Y'],complex),np.array(ns['beta'],complex)))
  conn=[s.zeros(12)]+[s.kronecker_product(ns['G']*v,s.eye(4)) for v in ns['spin']]
  bg=s.Matrix([ns['hm']]+[v for mat in conn for v in mat]);cols=[]
  for a in self.idx:
   z=bg
   for mu,n in enumerate(a):
    if n:z=z.diff(self.coords[mu],n)
   cols.append(z/factorial(a))
  self.bgfun=s.lambdify(self.coords,s.Matrix.hstack(*cols),'numpy',cse=True)
  self.deriv_indices=[];self.deriv_weights=[]
  for mu in range(4):
   ids=[];weights=[]
   for a in self.idx:
    b=list(a);b[mu]+=1;ids.append(self.full[tuple(b)]);weights.append(b[mu])
   self.deriv_indices.append(T.tensor(ids));self.deriv_weights.append(T.tensor(weights,dtype=T.float64))
 def conv(self,a,b,equation):
  terms=T.einsum(equation,a.index_select(0,self.left),b.index_select(0,self.right))
  return T.zeros((len(self.idx),)+terms.shape[1:],dtype=terms.dtype).index_add(0,self.dest,terms)
 def background(self,pos):return T.tensor(np.asarray(self.bgfun(*pos),complex).T.copy())
 def evaluate(self,coeff,bg,coframe=False):
  ps=coeff[:len(self.idx)];js=T.stack([coeff.index_select(0,ids)*weights[:,None] for ids,weights in zip(self.deriv_indices,self.deriv_weights)],dim=1)
  cov=js+1j*self.conv(bg[:,1:].reshape(-1,4,12,12),ps,'kmij,kj->kmi')
  E=self.conv(ps.conj(),T.einsum('aij,kmj->kaim',self.Q,cov),'ki,kaim->kam').real
  inv0=T.linalg.inv(E[0]);nonconstant=E-T.cat((E[:1],T.zeros_like(E[1:])),dim=0)
  X=T.einsum('ij,kjl->kil',inv0.to(T.complex128),nonconstant.to(T.complex128))
  eye=T.cat((T.eye(4,dtype=T.complex128)[None],T.zeros((len(self.idx)-1,4,4),dtype=T.complex128)))
  series=eye;power=eye
  for n in range(1,self.m+1):
   power=self.conv(power,X,'kij,kjl->kil');series=series+(-1)**n*power
  inverse=T.einsum('kij,jl->kil',series,inv0.to(T.complex128))
  kin=1j*self.conv(inverse,T.einsum('aij,kmj->kami',self.K,cov),'kma,kami->ki')
  mass=self.conv(bg[:,:1].real.to(T.complex128),T.einsum('ij,kj->ki',self.Y,ps),'ka,ki->ki')
  F=kin-mass
  return E if coframe else T.cat((F.real,F.imag),dim=1)
 def raw_coeff(self,point_index):
  data=json.loads((self.repo/'analysis/op5-field-slices/OP5_Joint_Compatibility_Lower_Data.json').read_text())['results'][point_index]
  fit=json.loads((ROOT/'joint-fit-result.json').read_text())['results'][point_index]
  newer=json.loads((ROOT/'third-joint-fit-result.json').read_text())['results'][point_index]
  c=np.zeros((len(self.fullidx),12),complex);c[0]=[complex(*v) for v in data['field_values_real_imag']]
  jp=np.array(fit['first_jets_packed']);j=(jp[:48]+1j*jp[48:]).reshape(4,12)
  for mu in range(4):a=tuple(int(k==mu) for k in range(4));c[self.full[a]]=j[mu]
  for d,values in [(2,newer['symmetric_second_jets']),(3,newer['tests'][1]['third_jets'])]:
   if d>self.order:continue
   vals=np.array(values).reshape(-1,24);z=vals[:,:12]+1j*vals[:,12:]
   for a,v in zip(indices(d)[len(indices(d-1)):],z):c[self.full[a]]=v/factorial(a)
  # Reuse the preceding calibrated level when present, retaining lower-order freedom.
  seed=ROOT/f'recursive-order-{self.order-1}-result.json'
  if seed.exists():
   prior=next((r for r in json.loads(seed.read_text())['results'] if r['point_index']==point_index),None)
   if prior is not None:
    vals=np.array(prior['coefficients_real_imag']);zz=vals[:,:12]+1j*vals[:,12:]
    for alpha,value in zip(prior['multiindices'],zz):
     if tuple(alpha) in self.full:c[self.full[tuple(alpha)]]=value
  return np.array(newer['point']),c
 def top_operator(self,coeff,bg):
  """Highest homogeneous block is linear; its coefficients depend only on psi/first jets."""
  top_start=len(indices(self.order-1));row_start=len(indices(self.m-1)) if self.m else 0
  fixed=T.tensor(coeff)
  def principal(z):
   full=T.cat((fixed[:1],unpack(z),fixed[5:]),dim=0)
   return self.evaluate(full,bg)[0]
  J=T.func.jacrev(principal)(T.tensor(pack(coeff[1:5]))).detach().numpy()
  A=np.zeros(((len(self.idx)-row_start)*24,(len(self.fullidx)-top_start)*24))
  for ri,alpha in enumerate(self.idx[row_start:]):
   for mu in range(4):
    beta=list(alpha);beta[mu]+=1;ci=self.full[tuple(beta)]-top_start
    A[ri*24:(ri+1)*24,ci*24:(ci+1)*24]+=(alpha[mu]+1)*J[:,mu*24:(mu+1)*24]
  return A,top_start,row_start
def run(order,points,maxsteps=15):
 started=datetime.now(timezone.utc).isoformat();tic=time.time();model=TaylorModel(order);rows=[]
 inputpaths=[Path(__file__).resolve(),ROOT/'joint-fit-result.json',ROOT/'third-joint-fit-result.json',model.source,model.repo/'analysis/op5-field-slices/OP5_Joint_Compatibility_Lower_Data.json']
 seed=ROOT/f'recursive-order-{order-1}-result.json'
 if seed.exists():inputpaths.append(seed)
 hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputpaths}
 for ip in points:
  pos,c=model.raw_coeff(ip);bg=model.background(pos);A,topstart,rowstart=model.top_operator(c,bg)
  U,sv,Vh=np.linalg.svd(A,full_matrices=False);rank=int(np.sum(sv>sv[0]*1e-9));L=T.tensor(U[:,rank:])
  # Keep value and all first derivatives fixed. All lower degrees2..order-1 remain adjustable.
  start=len(indices(1));lower0=pack(c[start:topstart]);fixed=T.tensor(c)
  def source(z):
   full=T.cat((fixed[:start],unpack(z),T.zeros_like(fixed[topstart:])),dim=0)
   return model.evaluate(full,bg)
  def objective(z):
   ff=source(z);return T.cat((ff[:rowstart].flatten(),L.T@ff[rowstart:].flatten()))
  fres=lambda z:objective(T.tensor(z)).detach().numpy();lower=lower0.copy();hist=[];damp=1e-7
  initial=fres(lower);jac=T.func.jacrev(objective)
  print('ORDER',order,'POINT',ip,'A',A.shape,'rank',rank,'initial',np.linalg.norm(initial),flush=True)
  for it in range(maxsteps):
   r=fres(lower);J=jac(T.tensor(lower)).detach().numpy();normal=J@J.T;accepted=False
   for trial in range(10):
    step=-J.T@np.linalg.solve(normal+damp*np.eye(len(r)),r);cand=lower+step;nr=fres(cand)
    if np.linalg.norm(nr)<np.linalg.norm(r) and np.linalg.norm(cand)<100*max(np.linalg.norm(lower0),1):
     lower=cand;accepted=True;damp=max(damp/3,1e-14);break
    damp*=10
   hist.append({'iteration':it,'accepted':accepted,'objective_norm':float(np.linalg.norm(fres(lower))),'step_norm':float(np.linalg.norm(step)),'damping':damp})
   print(ip,hist[-1],flush=True)
   if np.linalg.norm(fres(lower))<1e-9 or not accepted:break
  ff=source(T.tensor(lower)).detach().numpy();b=ff[rowstart:].flatten();tests=[]
  for cut in [1e-8,1e-9,1e-11]:
   top,_,rnk,svals=np.linalg.lstsq(A,-b,rcond=cut)
   tests.append({'rcond':cut,'rank':int(rnk),'residual':float(np.linalg.norm(A@top+b)),'top_coefficient_norm':float(np.linalg.norm(top))})
  top=np.linalg.lstsq(A,-b,rcond=1e-9)[0];full=T.cat((fixed[:start],unpack(T.tensor(lower)),unpack(T.tensor(top))),dim=0)
  final=model.evaluate(full,bg).detach().numpy();norms={}
  for d in range(model.m+1):
   ids=[n for n,a in enumerate(model.idx) if sum(a)==d];weights=np.array([factorial(model.idx[n]) for n in ids])
   norms[str(d)]={'coefficient_norm':float(np.linalg.norm(final[ids])),'raw_derivative_norm':float(np.linalg.norm(final[ids]*weights[:,None]))}
  coeff=full.detach().numpy();rawnorms={str(d):float(np.linalg.norm(np.array([coeff[n]*factorial(a) for n,a in enumerate(model.fullidx) if sum(a)==d]))) for d in range(order+1)}
  frozen_b=model.evaluate(T.tensor(c),bg).detach().numpy()[rowstart:].flatten();frozen_top=np.linalg.lstsq(A,-frozen_b,rcond=1e-9)[0]
  rows.append({'point_index':ip,'point':pos.tolist(),'initial_objective':float(np.linalg.norm(initial)),'frozen_lower_top_fit_residual':float(np.linalg.norm(A@frozen_top+frozen_b)),'matrix_shape':list(A.shape),'rank':rank,'singular_values':sv.tolist(),'history':hist,'final_blocks':norms,'raw_jet_norms':rawnorms,'lower_coefficient_change':float(np.linalg.norm(lower-lower0)),'tests':tests,'multiindices':model.fullidx,'coefficients_real_imag':np.concatenate((coeff.real,coeff.imag),axis=1).tolist()})
  out={'contract':'Finite-order numerical calibrator, Taylor coefficients normalized by multiindex factorial. Fixed psi/firstjets and background; variable lower jets degree2..order-1; eliminate/recover highest order. No convergence/existence theorem.','order':order,'started_at':started,'seconds':time.time()-tic,'software':{'python':platform.python_version(),'torch':T.__version__,'numpy':np.__version__,'sympy':s.__version__},'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in inputpaths),'results':rows}
  (ROOT/f'recursive-order-{order}-result.json').write_text(json.dumps(out,indent=2))
  print('FINAL',ip,norms,'growth',rawnorms,flush=True)
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--order',type=int,default=4);p.add_argument('--points',type=int,nargs='+',default=[0,1,2]);p.add_argument('--maxsteps',type=int,default=15);args=p.parse_args()
 if args.order<3 or args.maxsteps<1:p.error('order must be at least3 and maxsteps positive')
 run(args.order,args.points,args.maxsteps)
