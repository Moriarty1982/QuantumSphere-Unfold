from pathlib import Path
import sympy as s, numpy as np,json
base=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(base.read_text(encoding='utf-8-sig').split('results=[]')[0])
out=[]
for pt in points:
 ev=lambda m:np.array(s.Matrix(m).subs(pt).evalf(30),dtype=complex).reshape(-1)
 u=ev(U); w=ev(W); cs=float(c.subs(pt)); ds=float(d.subs(pt)); ps=float(p.subs(pt)); qs=float(q.subs(pt)); hs=float(hm.subs(pt))
 asp=sum(float(s.sympify(spin[k]).subs(pt))*np.array(al[k],dtype=complex) for k in range(3))
 bvec=hs*np.array(beta,dtype=complex)@u+1j*(ds*ps-cs*qs)*asp@w
 lam=np.vdot(u,bvec)/np.vdot(u,u); perp=bvec-lam*u
 out.append({'point':{str(k):str(v) for k,v in pt.items()},'complex_proportional_residual_squared':float(np.vdot(perp,perp).real),'normalized_transverse_speed_squared':float(np.vdot(perp,perp).real/np.vdot(u,u).real)})
e=s.symbols('epsilon',real=True)
# A=c e1-d epsilon e2, B=d e1+c epsilon e2: species/Dirac rank grows.
M=s.Matrix([[c,-d*e],[d,c*e]])
assert s.simplify(s.det(M)-e)==0
purity=(1+e**4)/(1+e**2)**2
assert s.simplify(1-purity-2*e**2/(1+e**2)**2)==0
result={'actual_initial_data':out,'toy_exact_minor':'epsilon','toy_normalized_reduced_purity':str(purity),'scope':'Classical component-rank test. Tensor-product quantum interpretation not established; no regional solution.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
