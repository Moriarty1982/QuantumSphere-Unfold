"""Independent NumPy univariate formal-series validation of multivariate Taylor model."""
from pathlib import Path
import json,itertools,math,hashlib,importlib.util,numpy as np,sympy as s
W=Path(__file__).resolve().parent;R=next(q for q in [Path.cwd(),*W.parents] if (q/'analysis/OP5_Counterflow_Full_Residual_Check.py').exists())
source=R/'analysis/OP5_Counterflow_Full_Residual_Check.py';ns={};exec(source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
coords=[ns[v] for v in ('t','x','y','z')];K=np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']]);Q=np.array([np.kron(np.array(ns['S'],complex),v) for v in K]);KK=np.array([np.kron(np.eye(3),v) for v in K]);Y=np.kron(np.array(ns['Y'],complex),np.array(ns['beta'],complex));Z=np.kron(np.diag([1,-1,0]),np.array(ns['beta'],complex))
idx=[]
for d in range(4):
 for axes in itertools.combinations_with_replacement(range(4),d):idx.append(tuple(axes.count(mu) for mu in range(4)))
fac=lambda a:math.prod(math.factorial(v) for v in a)
conn=[s.zeros(12)]+[s.kronecker_product(ns['G']*v,s.eye(4)) for v in ns['spin']];bg=s.Matrix([ns['hm']]+[v for m in conn for v in m]);cols=[]
for a in idx:
 z=bg
 for mu,n in enumerate(a):
  if n:z=z.diff(coords[mu],n)
 cols.append(z/fac(a))
fbg=s.lambdify(coords,s.Matrix.hstack(*cols),'numpy',cse=True)
spec=importlib.util.spec_from_file_location('reviewed_model',W/'recursive_calibrator.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);model=mod.TaylorModel(4)
resultpath=W/'recursive-order-4-result.json';data=json.loads(resultpath.read_text());rows=[]
directions=[np.eye(4)[mu] for mu in range(4)]+[np.array([1.,.2,-.3,.4]),np.array([-.3,.7,.2,-.4])]
for row in data['results']:
 pos=np.array(row['point']);mi=[tuple(a) for a in row['multiindices']];lookup={a:n for n,a in enumerate(mi)};packed=np.array(row['coefficients_real_imag']);coeff=packed[:,:12]+1j*packed[:,12:];bgc=np.asarray(fbg(*pos),complex).T
 parentF=model.evaluate(mod.T.tensor(coeff),model.background(pos)).detach().numpy();Fcoeff=parentF[:,:12]+1j*parentF[:,12:];direction_checks=[]
 for v in directions:
  ps=np.zeros((4,12),complex);dc=np.zeros((4,4,12),complex);bs=np.zeros((4,577),complex)
  for ia,a in enumerate(idx):
   d=sum(a);weight=np.prod(v**np.array(a));ps[d]+=coeff[lookup[a]]*weight;bs[d]+=bgc[ia]*weight
   for mu in range(4):
    beta=list(a);beta[mu]+=1;dc[d,mu]+=(a[mu]+1)*coeff[lookup[tuple(beta)]]*weight
  A=bs[:,1:].reshape(4,4,12,12);cov=dc.copy()
  for n in range(4):
   for l in range(n+1):cov[n]+=1j*np.einsum('mij,j->mi',A[l],ps[n-l])
  E=np.zeros((4,4,4));V=np.zeros((4,4,4),complex)
  for n in range(4):
   for l in range(n+1):E[n]+=np.einsum('i,aij,mj->am',ps[l].conj(),Q,cov[n-l]).real
  V[0]=np.linalg.inv(E[0])
  for n in range(1,4):V[n]=-V[0]@sum((E[l]@V[n-l] for l in range(1,n+1)),np.zeros((4,4),complex))
  F=np.zeros((4,12),complex)
  for n in range(4):
   for l in range(n+1):F[n]+=1j*np.einsum('ma,aij,mj->i',V[l],KK,cov[n-l])-bs[l,0].real*Y@ps[n-l]
  target=np.zeros((4,12),complex)
  for ia,a in enumerate(idx):target[sum(a)]+=Fcoeff[ia]*np.prod(v**np.array(a))
  invcheck=[]
  for n in range(4):
   left=sum((E[l]@V[n-l] for l in range(n+1)),np.zeros((4,4),complex));right=sum((V[l]@E[n-l] for l in range(n+1)),np.zeros((4,4),complex));identity=np.eye(4) if n==0 else np.zeros((4,4));invcheck.append(max(np.linalg.norm(left-identity),np.linalg.norm(right-identity)))
  # Scalar g along the same direction, independent of F evaluator.
  q=np.array([sum(np.vdot(ps[l],Z@ps[n-l]).real for l in range(n+1)) for n in range(4)]);g=np.array([(4 if n==0 else 0)-.5*sum(bs[l,0].real*q[n-l] for l in range(n+1)) for n in range(4)])
  direction_checks.append({'direction':v.tolist(),'F_coefficient_difference_by_degree':[float(np.linalg.norm(F[n]-target[n])) for n in range(4)],'inverse_both_orders_errors':list(map(float,invcheck)),'g_direction_actual_derivatives':(g*np.array([1,1,2,6])).tolist()})
 # Generic highest operator checked against actual evaluator perturbation, one column in each top multiset class.
 A,topstart,rowstart=model.top_operator(coeff,model.background(pos));base=model.evaluate(mod.T.tensor(coeff),model.background(pos)).detach().numpy()[rowstart:].ravel();topchecks=[]
 for ci in [0,1,13,24,40*24+23]:
  if ci>=A.shape[1]:continue
  delta=np.zeros((len(mi)-topstart,24));delta.ravel()[ci]=.01;dcplx=delta[:,:12]+1j*delta[:,12:];changed=coeff.copy();changed[topstart:]+=dcplx
  diff=model.evaluate(mod.T.tensor(changed),model.background(pos)).detach().numpy()[rowstart:].ravel()-base;topchecks.append({'column':ci,'norm_error':float(np.linalg.norm(diff-.01*A[:,ci]))})
 qfield=np.zeros(len(idx));gfield=np.zeros(len(idx))
 for ia,alpha in enumerate(idx):
  for ib,beta in enumerate(idx):
   gamma=tuple(a-b for a,b in zip(alpha,beta))
   if min(gamma)<0 or gamma not in lookup:continue
   qfield[ia]+=np.vdot(coeff[lookup[beta]],Z@coeff[lookup[gamma]]).real
 for ia,alpha in enumerate(idx):
  gfield[ia]=4 if sum(alpha)==0 else 0
  for ib,beta in enumerate(idx):
   gamma=tuple(a-b for a,b in zip(alpha,beta))
   if min(gamma)<0 or gamma not in idx:continue
   gfield[ia]-=.5*bgc[ib,0].real*qfield[idx.index(gamma)]
 scalar_norms={str(d):float(np.linalg.norm([gfield[n]*fac(alpha) for n,alpha in enumerate(idx) if sum(alpha)==d])) for d in range(4)}
 rows.append({'point_index':row['point_index'],'direction_checks':direction_checks,'top_operator_checks':topchecks,'scalar_actual_derivative_norms':scalar_norms});print('POINT',row['point_index'],'max F diff',max(max(v['F_coefficient_difference_by_degree']) for v in direction_checks),'toperror',max(v['norm_error'] for v in topchecks),flush=True)
out={'contract':'Independent NumPy directional formal power series with recurrence inverse, original symbolic normalized backgrounds. Six directions per point, both inverse multiplication orders, scalar directional derivatives, and sampled generic topoperator columns. No optimization.','inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,resultpath,W/'recursive_calibrator.py',Path(__file__)]},'results':rows}
(W/'recursive-review-coefficients-result.json').write_text(json.dumps(out,indent=2))
