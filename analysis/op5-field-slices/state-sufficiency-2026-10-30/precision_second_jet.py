"""70-digit second-jet compatibility at the repaired completed first jet."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
import precision_completed_rebuild as m
import mpmath as mp,numpy as np,json,itertools,time,hashlib
R=m.ROOT;tic=time.time();root=json.loads((R/'precision-completed-root-result.json').read_text());v=mp.matrix([mp.mpf(x) for x in root['first_derivatives_real_packed']]);js=[mp.matrix([mp.mpc(v[mu*24+k],v[mu*24+k+12]) for k in range(12)]) for mu in range(4)]
# Total coordinate derivative with the second jet set to zero. Only first-order
# Taylor dependence of each background argument is needed by mp.diff.
orig={k:getattr(m,k) for k in ['psi','h','dh','conn','dc','A']};d2h=[[m.cm(m.ns['hm'].diff(x,y).subs(m.subs)).real for y in m.coords] for x in m.coords];d2c=[[[m.mat(c.diff(x,y).subs(m.subs)) for c in m.cs] for y in m.coords] for x in m.coords]
def coordinate(t,mu):
 try:
  m.psi=orig['psi']+t*js[mu];m.h=orig['h']+t*orig['dh'][mu];m.dh=[orig['dh'][nu]+t*d2h[mu][nu] for nu in range(4)];m.conn=[orig['conn'][nu]+t*orig['dc'][mu][nu] for nu in range(4)];m.dc=[[orig['dc'][nu][a]+t*d2c[mu][nu][a] for a in range(4)] for nu in range(4)]
  m.A=mp.matrix([[mp.re(z) for z in (m.psi.conjugate().T*q)]+[-mp.im(z) for z in (m.psi.conjugate().T*q)] for q in m.Q]);return m.evaluate(v)
 finally:
  for k,z in orig.items():setattr(m,k,z)
b=mp.matrix([x for mu in range(4) for x in mp.diff(lambda t:coordinate(t,mu),mp.mpf('0'))]);J=mp.matrix([[mp.mpf(x) for x in row] for row in json.loads((R/'precision-completed-symbol-result.json').read_text())['matrix_decimal']]);pairs=list(itertools.combinations_with_replacement(range(4),2));A=mp.zeros(128,240)
for mu in range(4):
 for nu in range(4):
  col=pairs.index(tuple(sorted((mu,nu))));weight=2 if mu==nu else 1
  for i in range(32):
   for k in range(24):A[mu*32+i,col*24+k]+=weight*J[i,nu*24+k]
# Independent row candidates selected by twice-reorthogonalized Gram-Schmidt;
# precision solve and full residual decide compatibility, not the selection.
a=np.array(A.tolist(),float);basis=[];keep=[]
for i,row in enumerate(a):
 z=row.copy()
 for _ in range(2):
  for q in basis:z-=q@z*q
 n=np.linalg.norm(z)
 if n>1e-9:basis.append(z/n);keep.append(i)
print('row_rank',len(keep),flush=True)
if len(keep)!=113:raise RuntimeError('Unexpected row selection')
old=json.loads((R/'fifth-window-result.json').read_text(),parse_float=str)['results'][0];oldmap={tuple(alpha):value for alpha,value in zip(old['multiindices'],old['coefficients_real_imag'])};c=[]
for pair in pairs:
 alpha=tuple(pair.count(mu) for mu in range(4));c.extend(mp.mpf(x) for x in oldmap[alpha])
c=mp.matrix(c);initial=A*c+b;B=mp.matrix([[A[i,j] for j in range(240)] for i in keep]);rhs=mp.matrix([-initial[i] for i in keep]);dx=B.T*((B*B.T)**-1)*rhs;c+=dx;res=A*c+b
out={'contract':'Fixed repaired completed first jet; all symmetric normalized second Taylor coefficients free, closest correction to recorded old coefficients. Full 128 differentiated R equations tested. Numerical finite jet only; no third jet, Omega, convergence or exact rank certificate.','digits':70,'selected_row_count':len(keep),'initial_full_residual_max':mp.nstr(m.norm(initial),24),'final_full_residual_max':mp.nstr(m.norm(res),24),'correction_max_real_coefficient':mp.nstr(m.norm(dx),24),'second_coefficient_packing':'pairs combinations_with_replacement(0..3,2), each real12 then imag12; diagonal raw derivative=2*coefficient','pairs':pairs,'second_coefficients_real_packed':[mp.nstr(x,70) for x in c],'seconds':time.time()-tic,'input_sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['precision-completed-root-result.json','precision-completed-symbol-result.json','fifth-window-result.json']}}
(R/'precision-second-jet-result.json').write_text(json.dumps(out,indent=2));print({k:z for k,z in out.items() if k!='second_coefficients_real_packed'},flush=True)
