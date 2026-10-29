from pathlib import Path
import json
import numpy as np
root=Path(__file__).parent
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
data=json.loads((root/'OP5_AB_Proportional_Dynamics_Check.json').read_text())
eta=np.diag([-1.,1.,1.,1.])
a0,a1,a2,a3=s.symbols('a0 a1 a2 a3', nonzero=True, real=True)
rr=s.Matrix(s.symbols('r0:4',real=True)); av=s.Matrix([a0,a1,a2,a3])
dd=1+(rr.T*av)[0]; inverse_symbolic=s.eye(4)-av*rr.T/dd
qb=s.Matrix([1/a0,0,0,0])
assert all(s.simplify(vv)==0 for vv in (qb+rr).T*inverse_symbolic-qb.T)
arr=lambda m:np.array(m.tolist(),complex)
out=[]
for pt,previous in zip(points,data):
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 uu=arr(ev(U)).reshape(-1)
 km=[np.eye(4)]+[arr(a) for a in al]
 ju=np.array([np.vdot(uu,K@uu).real for K in km])
 avec=float(Delta.subs(pt))*ju/2
 qbase=np.array([float(th.diff(t).subs(pt)),0,0,0])
 coef=np.array(previous['released_spatial_theta_and_relative_phase']['coefficients'])
 dq=coef[:4]-qbase
 E=np.eye(4)+np.outer(avec,dq)
 det=np.linalg.det(E)
 inv=np.linalg.inv(E)
 inv_formula=np.eye(4)-np.outer(avec,dq)/(1+dq@avec)
 assert np.max(abs(inv-inv_formula))<1e-11
 metric=E.T@eta@E
 inverse_metric=inv@eta@inv.T
 P0=sum(inv[0,a]*km[a] for a in range(4))
 Ps=[sum(inv[mu,a]*km[a] for a in range(4)) for mu in range(4)]
 principal_theta=sum(coef[mu]*Ps[mu] for mu in range(4))
 assert np.max(abs(principal_theta-qbase[0]*np.eye(4)))<1e-10
 ww=arr(ev(W)).reshape(-1)
 aa=sum(float(s.sympify(spin[j]).subs(pt))*Ps[j+1] for j in range(3))
 aa_flat=sum(float(s.sympify(spin[j]).subs(pt))*km[j+1] for j in range(3))
 coupling=float((d*p-c*q).subs(pt))
 mass=float(hm.subs(pt))*arr(beta)@uu
 gate=principal_theta@uu+1j*coef[4]*P0@uu-mass-1j*coupling*aa@ww
 flat_gate=sum(coef[mu]*km[mu]@uu for mu in range(4))+1j*coef[4]*uu-mass-1j*coupling*aa_flat@ww
 assert np.linalg.norm(flat_gate)<1e-10
 evals=np.linalg.eigvalsh(P0)
 assert sum(np.linalg.eigvalsh(metric)<0)==1
 assert abs(np.linalg.det(P0)-inverse_metric[0,0]**2)<1e-7
 # Along linear interpolation of this jet change, check where dt becomes null.
 # n0=1-lambda*a0*dq0/D; ni=-lambda*a0*dqi/D.
 # Multiply g^{00} by D²: -(1+lambda*(dq.a-a0*dq0))²
 #                           +lambda²*a0²*|dq_sp|².
 B=float(dq@avec-avec[0]*dq[0])
 C=float(avec[0]**2*(dq[1:]@dq[1:])-B*B)
 roots=np.roots([C,-2*B,-1])
 real_roots=[float(v.real) for v in roots if abs(v.imag)<1e-10 and 0<v.real<=1]
 # Explicit future normal: row 0 of E is a timelike coordinate covector.
 good_normal=E[0,:]
 assert abs(good_normal@inverse_metric@good_normal+1)<1e-9
 out.append({'point':previous['point'],'theta_derivative_change':dq.tolist(),'coframe':E.tolist(),'det_E':float(det),'inverse_metric_g00':float(inverse_metric[0,0]),'time_principal_eigenvalues':evals.tolist(),'old_t_slice_spacelike':bool(inverse_metric[0,0]<0),'null_crossings_in_jet_interpolation':real_roots,'alternative_timelike_covector':good_normal.tolist(),'alternative_covector_norm':float(good_normal@inverse_metric@good_normal),'flat_transverse_gate_norm2':float(np.vdot(flat_gate,flat_gate).real),'induced_transverse_gate_norm2_fixed_coordinate_connection':float(np.vdot(gate,gate).real),'theta_principal_identity_error':float(np.max(abs(principal_theta-qbase[0]*np.eye(4))))})
 print(json.dumps(out[-1]),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
