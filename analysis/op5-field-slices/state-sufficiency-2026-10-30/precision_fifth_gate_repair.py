"""High-precision repair through the measured four-direction fifth source gate."""
from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
import json,mpmath as mp,numpy as np,itertools,time
R=Path(__file__).resolve().parent;tic=time.time();env={'__file__':str(R/'precision_fifth_gate.py')};exec((R/'precision_fifth_gate.py').read_text().split('b0=[')[0],env);mp.mp.dps=70;J=env['J'];partial=json.loads((R/'precision-fifth-gate-partial.json').read_text());assert partial['completed']==4;ds=[[mp.mpf(x) for x in d] for d in partial['directions']];db=[[mp.mpf(x) for x in d] for d in partial['source_deltas']];b0=[mp.mpf(x) for x in json.loads((R/'precision-fifth-source-result.json').read_text())['source_real_packed']];cache=np.load(R/'precision-fifth-quotient.npz');A=cache['principal'];L=cache['left'];gate=L.T@np.array([[float(db[k][i]) for k in range(4)] for i in range(1120)]);U,sv,vh=np.linalg.svd(gate,full_matrices=False);old=json.loads((R/'precision-fifth-left-witness-result.json').read_text());rows=old['selected_rows'];cols=old['selected_columns'];inv=np.linalg.inv(A[np.ix_(rows,cols)]);low=list(itertools.combinations_with_replacement(range(4),4));high=list(itertools.combinations_with_replacement(range(4),5));look={a:i for i,a in enumerate(high)}
def leftapply(l):
 out=[mp.mpf('0') for _ in range(1344)]
 for i,a in enumerate(low):
  for mu in range(4):
   col=look[tuple(sorted((*a,mu)))];w=a.count(mu)+1
   for k in range(24):out[col*24+k]+=w*mp.fsum(l[i*32+j]*J[j][mu*24+k] for j in range(32))
 return out
witnesses=[];errors=[]
for k in range(4):
 l=[mp.mpf(float(x)) for x in L@U[:,k]]
 for _ in range(7):
  z=leftapply(l);dx=-np.array([float(z[c]) for c in cols])@inv
  for i,x in zip(rows,dx):l[i]+=mp.mpf(float(x))
 witnesses.append(l);errors.append(max(abs(x) for x in leftapply(l)))
C=mp.matrix([[mp.fsum(l[i]*db[k][i] for i in range(1120)) for k in range(4)] for l in witnesses]);rhs=mp.matrix([-mp.fsum(l[i]*b0[i] for i in range(1120)) for l in witnesses]);params=mp.lu_solve(C,rhs);c0=env['c0'];c=[c0[i]+mp.fsum(params[k]*ds[k][i] for k in range(4)) for i in range(840)];pred=[b0[i]+mp.fsum(params[k]*db[k][i] for k in range(4)) for i in range(1120)];actual=env['source'](c);afferr=max(abs(x-y) for x,y in zip(actual,pred));print('actual source affine error',mp.nstr(afferr,12),flush=True)
def apply5(x):
 out=[mp.mpf('0') for _ in range(1120)]
 for i,a in enumerate(low):
  for mu in range(4):
   col=look[tuple(sorted((*a,mu)))];w=a.count(mu)+1
   for j in range(32):out[i*32+j]+=w*mp.fsum(J[j][mu*24+k]*x[col*24+k] for k in range(24))
 return out
x=[mp.mpf('0') for _ in range(1344)]
for _ in range(7):
 r=[a+b for a,b in zip(apply5(x),actual)];dx=-inv@np.array([float(r[i]) for i in rows])
 for col,y in zip(cols,dx):x[col]+=mp.mpf(float(y))
r=[a+b for a,b in zip(apply5(x),actual)];lower_leak=max(abs(v) for v in env['apply4']([a-b for a,b in zip(c,c0)]));out={'contract':'Four-direction highprecision fifth completion attempt: fixedfield0..3, fourth tangent correction, allfifth coefficientsfree. Full1120residuals decide finite compatibility; not general or exact existence.','parameter_scaled_lower_equation_leak':mp.nstr(lower_leak,24),'gate_singular_values_float':sv.tolist(),'left_witness_errors':[mp.nstr(x,24) for x in errors],'correction_parameters':[mp.nstr(x,70) for x in params],'fourth_coefficient_change_max':mp.nstr(max(abs(x-y) for x,y in zip(c,c0)),24),'actual_source_affine_error':mp.nstr(afferr,24),'full1120_completion_residual_max':mp.nstr(max(abs(x) for x in r),24),'selected907_residual_max':mp.nstr(max(abs(r[i]) for i in rows),24),'fourth_coefficients_real_packed':[mp.nstr(x,70) for x in c],'fifth_coefficients_real_packed':[mp.nstr(y,70) for y in x],'seconds':time.time()-tic};(R/'precision-fifth-gate-repair-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if 'packed' not in k})
