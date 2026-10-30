"""High-precision separating witness for the fifth extension with lower4 fixed."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import numpy as np,mpmath as mp,json,itertools,time
R=Path(__file__).resolve().parent;mp.mp.dps=70;tic=time.time();cache=np.load(R/'precision-fifth-quotient.npz');A=cache['principal'];L=cache['left'];bf=cache['source'];q=L.T@bf;lf=L@q/np.linalg.norm(q);rank=907;work=A.copy();rp=np.arange(1120);cp=np.arange(1344)
for k in range(rank):
 i,j=np.unravel_index(np.argmax(abs(work[k:,k:])),work[k:,k:].shape);i+=k;j+=k;work[[k,i]]=work[[i,k]];rp[[k,i]]=rp[[i,k]];work[:,[k,j]]=work[:,[j,k]];cp[[k,j]]=cp[[j,k]];work[k+1:,k+1:]-=np.outer(work[k+1:,k]/work[k,k],work[k,k+1:]);work[k+1:,k]=0
rows=rp[:rank];cols=cp[:rank];inv=np.linalg.inv(A[np.ix_(rows,cols)]);lam=[mp.mpf(float(x)) for x in lf];jm=[[mp.mpf(x) for x in row] for row in json.loads((R/'precision-completed-symbol-result.json').read_text())['matrix_decimal']];low=list(itertools.combinations_with_replacement(range(4),4));hi=list(itertools.combinations_with_replacement(range(4),5));look={a:i for i,a in enumerate(hi)}
def apply(l):
 out=[mp.mpf('0') for _ in range(1344)]
 for i,a in enumerate(low):
  for mu in range(4):
   col=look[tuple(sorted((*a,mu)))];w=a.count(mu)+1
   for k in range(24):out[col*24+k]+=w*mp.fsum(l[i*32+j]*jm[j][mu*24+k] for j in range(32))
 return out
for _ in range(7):
 z=apply(lam);delta=-np.array([float(z[c]) for c in cols])@inv
 for i,x in zip(rows,delta):lam[i]+=mp.mpf(float(x))
z=apply(lam);b=[mp.mpf(x) for x in json.loads((R/'precision-fifth-source-result.json').read_text())['source_real_packed']];pair=mp.fsum(x*y for x,y in zip(lam,b));norm=mp.sqrt(mp.fsum(x*x for x in lam));out={'contract':'Refined70-digit numerical left annihilator of all1344 fifth-jet columns, at fixed repaired lower4. Nonzero source indicates finite frozen-lower incompatibility; no general no-go, exact rank or interval certificate.','annihilation_max':mp.nstr(max(abs(x) for x in z),24),'normalized_source_pairing':mp.nstr(pair/norm,24),'witness_norm':mp.nstr(norm,24),'left_witness':[mp.nstr(x,70) for x in lam],'selected_rows':rows.tolist(),'selected_columns':cols.tolist(),'seconds':time.time()-tic}
(R/'precision-fifth-left-witness-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k not in ['left_witness','selected_rows','selected_columns']})
