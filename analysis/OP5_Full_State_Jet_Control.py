from pathlib import Path
import numpy as np, sympy as s,json
from types import SimpleNamespace
def least_squares(fun,start,**kwargs):
 a=start.copy(); count=0
 for iteration in range(100):
  r=fun(a); count+=1
  if np.linalg.norm(r)<1e-10: break
  h=1e-6
  jac=np.column_stack([(fun(a+np.eye(len(a))[k]*h)-fun(a-np.eye(len(a))[k]*h))/(2*h) for k in range(len(a))]); count+=2*len(a)
  step=np.linalg.lstsq(jac,-r,rcond=1e-11)[0]
  for scale in [1,.5,.25,.125,.0625,.03125,.015625,.0078125]:
   candidate=a+scale*step; rr=fun(candidate);count+=1
   if np.linalg.norm(rr)<np.linalg.norm(r):a=candidate;break
  else:break
 return SimpleNamespace(x=a,nfev=count)
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
K=np.array([np.eye(4)]+[np.array(a,complex) for a in al]); Q=np.array([np.kron(np.array(S,complex),k) for k in K]); out=[]
pack=lambda z:np.r_[z.real,z.imag]
unpack=lambda a:a[:48]+1j*a[48:]
for pt in points:
 ev=lambda m:np.array(s.Matrix(m).subs(pt).evalf(30),complex)
 psi=np.concatenate([ev(f).ravel() for f in fields]); jets=np.array([np.concatenate([ev(ds[mu]).ravel() for ds in derivs]) for mu in range(4)])
 gauge=[np.zeros((12,12),complex)]+[np.kron(ev(G)*float(s.sympify(spin[k]).subs(pt)),np.eye(4)) for k in range(3)]
 mass=float(hm.subs(pt))*np.kron(np.array(Y,complex),np.array(beta,complex))
 def evaluate(a):
  js=unpack(a).reshape(4,12)
  dj=np.array([js[mu]+1j*gauge[mu]@psi for mu in range(4)])
  E=np.array([[np.vdot(psi,Q[aa]@dj[mu]).real for mu in range(4)] for aa in range(4)])
  if abs(np.linalg.det(E))<1e-10:return None,E
  inv=np.linalg.inv(E)
  res=sum((1j*np.kron(np.eye(3),sum(inv[mu,aa]*K[aa] for aa in range(4)))@dj[mu] for mu in range(4)),np.zeros(12,complex))-mass@psi
  return res,E
 def fun(a):
  r,E=evaluate(a)
  return pack(r) if r is not None else np.ones(24)*1e8
 old=pack(jets.ravel()); oldres,Eold=evaluate(old)
 # Original flat Hamiltonian proposes fully independent time derivatives.
 spatial=sum((1j*np.kron(np.eye(3),K[k+1])@(jets[k+1]+1j*gauge[k+1]@psi) for k in range(3)),np.zeros(12,complex))
 proposed=-1j*(mass@psi-spatial)
 attempts=[]
 proposed_jets=jets.copy(); proposed_jets[0]=proposed
 for start in [pack(proposed_jets.ravel()),old]:
  fit=least_squares(fun,start,xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=500)
  res,E=evaluate(fit.x); metric=E.T@np.diag([-1,1,1,1])@E
  attempts.append({'residual_norm':float(np.linalg.norm(res)),'detE':float(np.linalg.det(E)),'g_inverse_00':float(np.linalg.inv(metric)[0,0]),'E':E.tolist(),'nfev':fit.nfev,'all_jets':[[float(z.real),float(z.imag)] for z in unpack(fit.x)]})
 out.append({'point':{str(k):str(v) for k,v in pt.items()},'original_E':Eold.tolist(),'original_residual':float(np.linalg.norm(oldres)),'attempts':attempts})
result={'contract':'Fixed field values and original couplings; all 48 complex spacetime derivatives free; cross coframe recomputed inside residual. No extra connection, fixed zero Lorentz spin connection. Numerical pointwise comparison only.','results':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
