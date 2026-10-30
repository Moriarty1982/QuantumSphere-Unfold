"""Four-direction source gate for fifth completion, fixed field0..3."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import numpy as np,mpmath as mp,sympy as s,itertools,json,time,hashlib
R=Path(__file__).resolve().parent;tic=time.time();env={'__file__':str(R/'precision_fifth_source.py')};exec((R/'precision_fifth_source.py').read_text().split('values=[]')[0],env);ns=env['ns'];dirs=env['dirs'];W=env['W'];mp.mp.dps=70
root=json.loads((R/'precision-omega-repair-result.json').read_text());c0=[mp.mpf(x) for x in root['fourth_coefficients_real_packed']];third=[z for z in ns['terms'] if len(z[0])==3];axes=list(itertools.combinations_with_replacement(range(4),4));a4=np.load(R/'precision-fourth-elimination.npz')['principal'];e4=json.loads((R/'precision-fourth-elimination-result.json').read_text());rows=e4['selected_rows'];cols=e4['selected_columns'];inv=np.linalg.inv(a4[np.ix_(rows,cols)]);u,sv,vh=np.linalg.svd(a4,full_matrices=True);N=vh[528:].T;rng=np.random.default_rng(3010305);J=[[mp.mpf(x) for x in row] for row in json.loads((R/'precision-completed-symbol-result.json').read_text())['matrix_decimal']];low=list(itertools.combinations_with_replacement(range(4),3));look={a:i for i,a in enumerate(axes)}
def apply4(x):
 out=[mp.mpf('0') for _ in range(640)]
 for i,a in enumerate(low):
  for mu in range(4):
   col=look[tuple(sorted((*a,mu)))];w=a.count(mu)+1
   for j in range(32):out[i*32+j]+=w*mp.fsum(J[j][mu*24+k]*x[col*24+k] for k in range(24))
 return out
def source(c):
 ns['terms']=third+[(a,mp.matrix([mp.mpc(c[i*24+k],c[i*24+k+12]) for k in range(12)])) for i,a in enumerate(axes)];values=[mp.diff(lambda t:ns['path'](t,d),mp.mpf('0'),4)/24 for d in dirs]
 return [sum(mp.mpf(str(W[i,j]))*values[j][k] for j in range(35)) for i in range(35) for k in range(32)]
b0=[mp.mpf(x) for x in json.loads((R/'precision-fifth-source-result.json').read_text())['source_real_packed']];directions=[];deltas=[];leaks=[]
for trial in range(4):
 df=N@rng.normal(size=N.shape[1]);df/=np.linalg.norm(df);d=[mp.mpf(float(x)) for x in df]
 for _ in range(7):
  r=apply4(d);dx=-inv@np.array([float(r[i]) for i in rows])
  for col,x in zip(cols,dx):d[col]+=mp.mpf(float(x))
 leak=max(abs(x) for x in apply4(d));bp=source([x+y for x,y in zip(c0,d)]);directions.append(d);deltas.append([x-y for x,y in zip(bp,b0)]);leaks.append(leak);print('direction done',trial,'lower leak',mp.nstr(leak,8),flush=True)
 (R/'precision-fifth-gate-partial.json').write_text(json.dumps({'completed':trial+1,'directions':[[mp.nstr(x,70) for x in d] for d in directions],'source_deltas':[[mp.nstr(x,70) for x in d] for d in deltas],'lower_leaks':[mp.nstr(x,24) for x in leaks]},indent=2))
L=np.load(R/'precision-fifth-quotient.npz')['left'];G=L.T@np.array([[float(deltas[k][i]) for k in range(4)] for i in range(1120)]);q=L.T@np.array([float(x) for x in b0]);sv=np.linalg.svd(G,compute_uv=False);p=np.linalg.lstsq(G,-q,rcond=1e-10)[0];remaining=q+G@p
out={'contract':'Four deterministic random fourth-jet tangent directions, refined against full640 preceding symbol rows; field0..3 fixed. Newdegree4 source is affine in fourthcoefficients. Float64 quotient gate only; not complete gate rank or exact proof.','seed':3010305,'gate_singular_values':sv.tolist(),'gate_rank_cutoffs':[{'cutoff':x,'rank':int(sum(sv>sv[0]*x))} for x in [1e-8,1e-10,1e-12]],'initial_quotient_norm':float(np.linalg.norm(q)),'remaining_quotient_norm_float':float(np.linalg.norm(remaining)),'correction_parameters_float':p.tolist(),'gate':G.tolist(),'seconds':time.time()-tic};(R/'precision-fifth-gate-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k!='gate'},flush=True)
