from pathlib import Path
import json,numpy as np
base=Path(__file__).with_name('OP5_Relative_Phase_Integrability_Check.py')
exec(base.read_text().split('out=[]')[0])
als=sum((spin[j]*al[j] for j in range(3)),s.zeros(4))
bs=th.diff(t)*U-hm*beta*U-I*(d*p-c*q)*als*W
exprs=[U,bs,c*d]
derfun=s.lambdify((t,x,y,z),exprs+[e.diff(vv) for vv in (t,x,y,z) for e in exprs],modules='numpy',cse=True)
out=[]
for pos in [(1.,.6,0,0),(1.,.4,.2,.2)]:
 vals=derfun(*pos);uu=np.asarray(vals[0],complex).reshape(-1);bval=np.asarray(vals[1],complex).reshape(-1);cd=float(vals[2])
 M=np.column_stack([pack(1j*k@uu) for k in K]);bv=pack(bval)
 lv=np.linalg.solve(M.T@M,-M.T@bv)
 J=np.zeros((4,4))
 for mu in range(4):
  du=np.asarray(vals[3+3*mu],complex).reshape(-1);db=pack(np.asarray(vals[4+3*mu],complex).reshape(-1));dcd=float(vals[5+3*mu])
  dM=np.column_stack([pack(1j*k@du) for k in K])
  dl=np.linalg.solve(M.T@M,-dM.T@bv-M.T@db-(dM.T@M+M.T@dM)@lv)
  J[:,mu]=dl/cd-lv*dcd/cd**2
 curl=J.T-J
 numeric=derivative(np.array(pos),1e-4,'relative')
 assert np.max(abs(curl-(numeric.T-numeric)))<2e-6
 out.append({'point':pos,'analytic_derivative_d_relative':curl.tolist(),'max_abs':float(np.max(abs(curl)))})
# Internal commutant exact: no numerical rank threshold.
xx=s.symbols('X0:9');X=s.Matrix(3,3,xx)
comm=lambda aa,bb:aa*bb-bb*aa
solSY=s.linsolve(list(comm(X,S))+list(comm(X,Y)),xx)
Gtest=s.Matrix([[0,0,1],[0,0,2],[1,2,0]])
solAll=s.linsolve(list(comm(X,S))+list(comm(X,Y))+list(comm(X,Gtest)),xx)
assert solSY==s.FiniteSet((xx[4],0,0,0,xx[4],0,0,0,xx[8]))
assert solAll==s.FiniteSet((xx[8],0,0,0,xx[8],0,0,0,xx[8]))
result={'analytic_integrability_checks':out,'commutant_S_Y':str(solSY),'commutant_S_Y_G_p1_q2':str(solAll),'generic_argument':'diag(a,a,b) commutes with G only if (a-b)p=(a-b)q=0. Nonzero G implies a=b.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
