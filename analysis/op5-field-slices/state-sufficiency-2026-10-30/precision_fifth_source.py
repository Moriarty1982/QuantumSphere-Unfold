"""Degree-four source and fifth-symbol quotient at fixed repaired fourth jet."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import json,mpmath as mp,sympy as s,itertools,numpy as np,time,hashlib
R=Path(__file__).resolve().parent;tic=time.time();env={'__file__':str(R/'precision_omega_repair_check.py')};exec((R/'precision_omega_repair_check.py').read_text().split(';res=[')[0],env);ns=env['ns'];mp.mp.dps=70
low=list(itertools.combinations_with_replacement(range(4),4));exponents=[[a.count(mu) for mu in range(4)] for a in low];dirs=exponents;M=s.Matrix([[s.prod(s.Integer(d[mu])**a[mu] for mu in range(4)) for a in exponents] for d in dirs]);assert M.det()==43115616168696989527091804682766516224;W=M.inv();assert W*M==s.eye(35)
values=[]
for i,d in enumerate(dirs):
 values.append(mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),4)/24)
 if i%10==0:print('source direction',i,flush=True)
b=[sum(mp.mpf(str(W[i,j]))*values[j][k] for j in range(35)) for i in range(35) for k in range(32)]
checks=[]
for d in [[1,-2,3,-1],[2,1,-1,3]]:
 actual=mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),4)/24;pred=mp.matrix([sum(b[i*32+k]*mp.fprod(mp.mpf(d[mu])**exponents[i][mu] for mu in range(4)) for i in range(35)) for k in range(32)]);checks.append({'direction':d,'interpolation_error_max':mp.nstr(max(abs(x) for x in actual-pred),24)})
source={'contract':'Normalized degree4 R source at fixed repaired common fourth field jet; fifth jet zero. Exact quartic interpolation checked by Wolfram and locally rational arithmetic.','digits':70,'quadruples':low,'source_real_packed':[mp.nstr(x,70) for x in b],'checks':checks,'seconds':time.time()-tic,'lower_germ_sha256':hashlib.sha256((R/'precision-omega-repair-result.json').read_bytes()).hexdigest()};(R/'precision-fifth-source-result.json').write_text(json.dumps(source,indent=2))
J=np.array(json.loads((R/'precision-completed-symbol-result.json').read_text())['matrix_decimal'],float);hi=list(itertools.combinations_with_replacement(range(4),5));look={a:i for i,a in enumerate(hi)};A=np.zeros((1120,1344))
for i,a in enumerate(low):
 for mu in range(4):
  col=look[tuple(sorted((*a,mu)))];A[i*32:(i+1)*32,col*24:(col+1)*24]+=(a.count(mu)+1)*J[:,mu*24:(mu+1)*24]
u,sv,vh=np.linalg.svd(A,full_matrices=True);tests=[];bf=np.array([float(x) for x in b])
for cut in [1e-8,1e-10,1e-12]:
 rank=int(sum(sv>sv[0]*cut));L=u[:,rank:];q=L.T@bf;tests.append({'cutoff':cut,'rank':rank,'left_quotient_norm':float(np.linalg.norm(q))})
rank=tests[1]['rank'];out={'contract':'Float64 complete left-quotient test of free fifth-jet symbol using new70-digit source. No exact or highprecision left witness yet; fixed fourth jet only, not general impossibility.','tests':tests,'singular_boundary':sv[rank-3:rank+3].tolist(),'source_norm':float(np.linalg.norm(bf)),'seconds':time.time()-tic,'source_sha256':hashlib.sha256((R/'precision-fifth-source-result.json').read_bytes()).hexdigest()};(R/'precision-fifth-quotient-result.json').write_text(json.dumps(out,indent=2));np.savez_compressed(R/'precision-fifth-quotient.npz',principal=A,left=u[:,rank:],source=bf);print(out,flush=True)
