"""High precision primitive-symbol reconstruction, not the completed Omega symbol."""
from pathlib import Path
import json,mpmath as mp,sympy as s,hashlib,time
ROOT=Path(__file__).resolve().parent
repo=Path('C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold')
source=repo/'analysis/OP5_Counterflow_Full_Residual_Check.py'
ns={};exec(source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
raw=json.loads((ROOT/'fifth-window-result.json').read_text(),parse_float=str)['results'][0]
def cm(v):
 z=s.N(v,85);return mp.mpc(str(s.re(z)),str(s.im(z)))
def mat(M):return mp.matrix([[cm(M[i,j]) for j in range(M.cols)] for i in range(M.rows)])
def realmat(M):
 return mp.matrix([[mp.re(M[i,j]) if i<M.rows and j<M.cols else -mp.im(M[i,j-M.cols]) if i<M.rows else mp.im(M[i-M.rows,j]) if j<M.cols else mp.re(M[i-M.rows,j-M.cols]) for j in range(2*M.cols)] for i in range(2*M.rows)])
def realvec(z):return mp.matrix([mp.re(v) for v in z]+[mp.im(v) for v in z])
def norm(M):return max(abs(v) for v in M)
results=[]
for digits in [40,70]:
 mp.mp.dps=digits
 pos=[s.Rational(str(v)) for v in raw['point']];subs=dict(zip([ns[v] for v in ['t','x','y','z']],pos))
 KK=[s.kronecker_product(s.eye(3),v) for v in [s.eye(4)]+ns['al']];QQ=[s.kronecker_product(ns['S'],v) for v in [s.eye(4)]+ns['al']]
 K=[mat(v) for v in KK];Q=[mat(v) for v in QQ];Y=mat(s.kronecker_product(ns['Y'],ns['beta']));Z=mat(s.kronecker_product(s.diag(1,-1,0),ns['beta']));h=cm(ns['hm'].subs(subs)).real
 ps=mp.matrix([mp.mpc(raw['coefficients_real_imag'][0][j],raw['coefficients_real_imag'][0][j+12]) for j in range(12)])
 js=[mp.matrix([mp.mpc(raw['coefficients_real_imag'][i][j],raw['coefficients_real_imag'][i][j+12]) for j in range(12)]) for i in range(1,5)]
 conn=[mp.zeros(12)]+[mat(s.kronecker_product(ns['G']*v,s.eye(4)).subs(subs)) for v in ns['spin']]
 def evaluate(psi,details=False):
  cov=[js[mu]+mp.j*conn[mu]*psi for mu in range(4)]
  E=mp.matrix([[mp.re((psi.conjugate().T*Q[a]*cov[mu])[0]) for mu in range(4)] for a in range(4)]);V=E**-1
  A=mp.matrix([[mp.re(v) for v in (psi.conjugate().T*Q[a])]+[-mp.im(v) for v in (psi.conjugate().T*Q[a])] for a in range(4)])
  B=mp.matrix([[realvec(cov[mu])[i] for mu in range(4)] for i in range(24)]);P=mp.eye(24)-B*V*A
  F=mp.zeros(12,1)
  for mu in range(4):
   for a in range(4):F+=mp.j*V[mu,a]*K[a]*cov[mu]
  F-=h*Y*psi
  H=[realmat(mp.j*k) for k in K];J=[sum((V[mu,a]*H[a] for a in range(4)),mp.zeros(24))*P for mu in range(4)]
  S=mat(s.kronecker_product(ns['S'],s.eye(4)));w=S*psi;ell=mp.matrix([[-mp.im(v) for v in w]+[mp.re(v) for v in w]])
  g=4-h*(psi.conjugate().T*Z*psi)[0].real/2
  result={'F':norm(F),'g':abs(g),'AP':norm(A*P),'P2minusP':norm(P*P-P),'ellJ':max(norm(ell*j) for j in J),'ellFminusg':abs((ell*realvec(F))[0]-g),'detE':abs(mp.det(E))}
  return (result,J,F,ell) if details else result
 old=evaluate(ps);pivot=ps[0].real
 # Exact scalar-chart repair at this precision, with every other real component fixed.
 rad=pivot*pivot+2*(4-h*(ps.conjugate().T*Z*ps)[0].real/2)/h
 ps[0]=mp.mpc(mp.sqrt(rad),ps[0].imag);new=evaluate(ps)
 repaired_start=[v.copy() for v in js];steps=[]
 for iteration in range(4):
  state,J,F,ell=evaluate(ps,True);drop=max(range(24),key=lambda i:abs(ell[i]));keep=[i for i in range(24) if i!=drop]
  A=mp.matrix([[J[mu][i,j] for mu in range(4) for j in range(24)] for i in keep]);f=realvec(F);rhs=mp.matrix([f[i] for i in keep]);dx=-A.T*((A*A.T)**-1)*rhs
  for mu in range(4):
   for j in range(12):js[mu][j]+=mp.mpc(dx[mu*24+j],dx[mu*24+j+12])
  steps.append(mp.nstr(evaluate(ps)['F'],20))
 (ROOT/('precision-first-jet-'+str(digits)+'.json')).write_text(json.dumps({'digits':digits,'point':[str(v) for v in pos],'psi':[[mp.nstr(mp.re(v),digits),mp.nstr(mp.im(v),digits)] for v in ps],'first_derivatives':[[[mp.nstr(mp.re(v),digits),mp.nstr(mp.im(v),digits)] for v in row] for row in js],'scope':'F=0 and g=0 numerical first jet; completed G,dg constraints not solved'},indent=2))
 final=evaluate(ps);shift=max(norm(js[i]-repaired_start[i]) for i in range(4))
 results.append({'newton_F_residuals':steps,'first_derivative_change_max':mp.nstr(shift,20),'repaired_first_jet':{k:mp.nstr(v,20) for k,v in final.items()},'digits':digits,'original':{k:mp.nstr(v,20) for k,v in old.items()},'scalar_repaired':{k:mp.nstr(v,20) for k,v in new.items()},'pivot_change':mp.nstr(abs(ps[0].real-pivot),20)})
 print(results[-1],flush=True)
(ROOT/'precision-primitive-result.json').write_text(json.dumps({'contract':'Reconstruction from decimal-recorded lower data, exact symbolic background at recorded coordinates. Fixed comparison; first F symbol only. No completed JR or Omega reconstruction yet. Scalar repair changes psi only; derivatives held fixed, so full F is rechecked.','results':results,'inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,ROOT/'fifth-window-result.json',Path(__file__)]}},indent=2))

