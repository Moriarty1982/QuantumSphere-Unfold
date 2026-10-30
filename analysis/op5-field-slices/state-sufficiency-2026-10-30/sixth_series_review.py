"""Fixed0..3 sixth-order window independent NumPy directional formal-series validation. No optimization."""
ORDER=6
from pathlib import Path
import json,itertools,math,hashlib,importlib.util,numpy as np,sympy as s
W=Path(__file__).resolve().parent;R=next(q for q in [Path.cwd(),*W.parents] if (q/'analysis/OP5_Counterflow_Full_Residual_Check.py').exists())
source=R/'analysis/OP5_Counterflow_Full_Residual_Check.py';ns={};exec(source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
coords=[ns[v] for v in ('t','x','y','z')];K=np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']]);Q=np.array([np.kron(np.array(ns['S'],complex),v) for v in K]);KK=np.array([np.kron(np.eye(3),v) for v in K]);Y=np.kron(np.array(ns['Y'],complex),np.array(ns['beta'],complex));Z=np.kron(np.diag([1,-1,0]),np.array(ns['beta'],complex))
idx=[]
for d in range(ORDER):
 for axes in itertools.combinations_with_replacement(range(4),d):idx.append(tuple(axes.count(mu) for mu in range(4)))
fac=lambda a:math.prod(math.factorial(v) for v in a)
conn=[s.zeros(12)]+[s.kronecker_product(ns['G']*v,s.eye(4)) for v in ns['spin']];bg=s.Matrix([ns['hm']]+[v for m in conn for v in m]);cols=[]
for a in idx:
 z=bg
 for mu,n in enumerate(a):
  if n:z=z.diff(coords[mu],n)
 cols.append(z/fac(a))
fbg=s.lambdify(coords,s.Matrix.hstack(*cols),'numpy',cse=True)
spec=importlib.util.spec_from_file_location('reviewed_model',W/'recursive_calibrator.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);model=mod.TaylorModel(ORDER)
resultpath=W/'sixth-frozen-third-result.json';data=json.loads(resultpath.read_text());assert len(data['results'])==3;rows=[]
inputpaths=[source,resultpath,W/'fifth-window-result.json',W/'recursive_calibrator.py',Path(__file__)]
inputhashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputpaths}
directions=[np.eye(4)[mu] for mu in range(4)]+[np.array([1.,.2,-.3,.4]),np.array([-.3,.7,.2,-.4])]
for row in data['results']:
 pos=np.array(row['point']);mi=[tuple(a) for a in row['multiindices']];lookup={a:n for n,a in enumerate(mi)};packed=np.array(row['coefficients_real_imag']);coeff=packed[:,:12]+1j*packed[:,12:];bgc=np.asarray(fbg(*pos),complex).T
 parentF=model.evaluate(mod.T.tensor(coeff),model.background(pos)).detach().numpy();Fcoeff=parentF[:,:12]+1j*parentF[:,12:];direction_checks=[]
 for v in directions:
  ps=np.zeros((ORDER,12),complex);dc=np.zeros((ORDER,4,12),complex);bs=np.zeros((ORDER,577),complex)
  for ia,a in enumerate(idx):
   d=sum(a);weight=np.prod(v**np.array(a));ps[d]+=coeff[lookup[a]]*weight;bs[d]+=bgc[ia]*weight
   for mu in range(4):
    beta=list(a);beta[mu]+=1;dc[d,mu]+=(a[mu]+1)*coeff[lookup[tuple(beta)]]*weight
  A=bs[:,1:].reshape(ORDER,4,12,12);cov=dc.copy()
  for n in range(ORDER):
   for l in range(n+1):cov[n]+=1j*np.einsum('mij,j->mi',A[l],ps[n-l])
  E=np.zeros((ORDER,4,4));V=np.zeros((ORDER,4,4),complex)
  for n in range(ORDER):
   for l in range(n+1):E[n]+=np.einsum('i,aij,mj->am',ps[l].conj(),Q,cov[n-l]).real
  V[0]=np.linalg.inv(E[0])
  for n in range(1,ORDER):V[n]=-V[0]@sum((E[l]@V[n-l] for l in range(1,n+1)),np.zeros((4,4),complex))
  F=np.zeros((ORDER,12),complex)
  for n in range(ORDER):
   for l in range(n+1):F[n]+=1j*np.einsum('ma,aij,mj->i',V[l],KK,cov[n-l])-bs[l,0].real*Y@ps[n-l]
  target=np.zeros((ORDER,12),complex)
  for ia,a in enumerate(idx):target[sum(a)]+=Fcoeff[ia]*np.prod(v**np.array(a))
  invcheck=[]
  for n in range(ORDER):
   left=sum((E[l]@V[n-l] for l in range(n+1)),np.zeros((4,4),complex));right=sum((V[l]@E[n-l] for l in range(n+1)),np.zeros((4,4),complex));identity=np.eye(4) if n==0 else np.zeros((4,4));invcheck.append(max(np.linalg.norm(left-identity),np.linalg.norm(right-identity)))
  # Scalar g along the same direction, independent of F evaluator.
  q=np.array([sum(np.vdot(ps[l],Z@ps[n-l]).real for l in range(n+1)) for n in range(ORDER)]);g=np.array([(4 if n==0 else 0)-.5*sum(bs[l,0].real*q[n-l] for l in range(n+1)) for n in range(ORDER)])
  direction_checks.append({'direction':v.tolist(),'F_coefficient_difference_by_degree':[float(np.linalg.norm(F[n]-target[n])) for n in range(ORDER)],'inverse_both_orders_errors':list(map(float,invcheck)),'g_direction_actual_derivatives':(g*np.array([math.factorial(d) for d in range(ORDER)])).tolist()})
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
 scalar_norms={str(d):float(np.linalg.norm([gfield[n]*fac(alpha) for n,alpha in enumerate(idx) if sum(alpha)==d])) for d in range(ORDER)}
 olddata=json.loads((W/'fifth-window-result.json').read_text())
 oldrow=next(v for v in olddata['results'] if v['point_index']==row['point_index'])
 oldmi=[tuple(a) for a in oldrow['multiindices']];oldlookup={a:n for n,a in enumerate(oldmi)};oldp=np.array(oldrow['coefficients_real_imag']);oldc=oldp[:,:12]+1j*oldp[:,12:];movement={};growth={}
 for d in range(ORDER+1):
  ids=[n for n,a in enumerate(mi) if sum(a)==d];factors=np.array([fac(mi[n]) for n in ids]);block=coeff[ids]
  growth[str(d)]={'normalized_coefficient_norm':float(np.linalg.norm(block)),'actual_derivative_norm':float(np.linalg.norm(block*factors[:,None]))}
  if d<=ORDER-1:
   oldblock=np.array([oldc[oldlookup[mi[n]]] for n in ids]);delta=block-oldblock
   movement[str(d)]={'normalized_change':float(np.linalg.norm(delta)),'actual_derivative_change':float(np.linalg.norm(delta*factors[:,None])),'relative_normalized_change':float(np.linalg.norm(delta)/max(np.linalg.norm(oldblock),1e-300))}
   if d<=3:assert np.array_equal(block,oldblock), 'Declared frozen coefficient changed'
 rows.append({'point_index':row['point_index'],'direction_checks':direction_checks,'top_operator_checks':topchecks,'scalar_actual_derivative_norms':scalar_norms,'movement_from_window5':movement,'jet_growth':growth});print('POINT',row['point_index'],'max F diff',max(max(v['F_coefficient_difference_by_degree']) for v in direction_checks),'toperror',max(v['norm_error'] for v in topchecks),flush=True)
out={'contract':'Independent NumPy directional formal power series with recurrence inverse, original symbolic normalized backgrounds. Six directions per point, both inverse multiplication orders, scalar directional derivatives, and sampled generic topoperator columns. No optimization.','inputs_sha256':inputhashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==inputhashes[str(p)] for p in inputpaths),'results':rows}
(W/'sixth-series-review-result.json').write_text(json.dumps(out,indent=2))
