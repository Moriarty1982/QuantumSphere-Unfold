"""Rank-revealing fourth-jet elimination with high-precision residual refinement."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import numpy as np,mpmath as mp,itertools,json,time,hashlib
R=Path(__file__).resolve().parent;tic=time.time();mp.mp.dps=70;src=json.loads((R/'precision-fourth-source-result.json').read_text());jdata=json.loads((R/'precision-completed-symbol-result.json').read_text());J=np.array(jdata['matrix_decimal'],float);low=list(itertools.combinations_with_replacement(range(4),3));high=list(itertools.combinations_with_replacement(range(4),4));lookup={a:i for i,a in enumerate(high)};A=np.zeros((640,840));entries=[]
for i,alpha in enumerate(low):
 for mu in range(4):
  col=lookup[tuple(sorted((*alpha,mu)))];weight=alpha.count(mu)+1;A[i*32:(i+1)*32,col*24:(col+1)*24]+=weight*J[:,mu*24:(mu+1)*24];entries.append((i,col,mu,weight))
u,s,vh=np.linalg.svd(A,full_matrices=True);rank=int(sum(s>s[0]*1e-10));print('rank',rank,flush=True)
assert rank==528
# Complete-pivot Gaussian elimination selects one invertible rank-size minor.
work=A.copy();rp=np.arange(640);cp=np.arange(840)
for k in range(rank):
 ii,jj=np.unravel_index(np.argmax(np.abs(work[k:,k:])),work[k:,k:].shape);ii+=k;jj+=k
 work[[k,ii]]=work[[ii,k]];rp[[k,ii]]=rp[[ii,k]];work[:,[k,jj]]=work[:,[jj,k]];cp[[k,jj]]=cp[[jj,k]]
 work[k+1:,k+1:]-=np.outer(work[k+1:,k]/work[k,k],work[k,k+1:]);work[k+1:,k]=0
rows=rp[:rank].tolist();cols=cp[:rank].tolist();B=A[np.ix_(rows,cols)];Binv=np.linalg.inv(B);b=mp.matrix([mp.mpf(x) for x in src['source_real_packed']]);jm=[[mp.mpf(x) for x in row] for row in jdata['matrix_decimal']]
def apply(x):
 out=[mp.mpf('0') for _ in range(640)]
 for i,col,mu,w in entries:
  block=x[col*24:(col+1)*24]
  for j in range(32):out[i*32+j]+=w*mp.fsum(jm[j][mu*24+k]*block[k] for k in range(24))
 return mp.matrix(out)
x=[mp.mpf('0') for _ in range(840)];history=[]
for iteration in range(7):
 res=apply(x)+b;r=np.array([float(res[i]) for i in rows]);dx=-Binv@r
 for c,z in zip(cols,dx):x[c]+=mp.mpf(float(z))
 res=apply(x)+b;selected=max(abs(res[i]) for i in rows);history.append({'iteration':iteration+1,'selected_residual_max':mp.nstr(selected,24),'full_residual_max':mp.nstr(max(abs(z) for z in res),24)});print(history[-1],flush=True)
# A complete orthogonal left quotient provides a scaling-independent float
# comparison; no identification of all112 quotient rows with a single Omega.
left=u[:,rank:];bf=np.array([float(z) for z in b]);projected=left.T@bf;xr=np.linalg.lstsq(A,-bf,rcond=1e-10)[0];best=A@xr+bf
out={'contract':'Eliminate fourth field jet at fixed repaired lower germ. Complete-pivot minor selects528 equations/variables; iterative refinement checks them at70digits. Full640 residual and orthogonal left quotient retained. Numerical rank/refinement, not exact theorem or automatic identification as Omega.','rank':rank,'left_quotient_dimension':640-rank,'minor_condition_float':float(np.linalg.cond(B)),'history':history,'orthogonal_quotient_norm_float':float(np.linalg.norm(projected)),'least_squares_full_residual_norm_float':float(np.linalg.norm(best)),'max_selected_residual':mp.nstr(selected,24),'remaining_residual_max':mp.nstr(max(abs(z) for z in res),24),'remaining_residual_real_packed':[mp.nstr(z,70) for z in res],'fourth_coefficients_real_packed':[mp.nstr(z,70) for z in x],'selected_rows':rows,'selected_columns':cols,'seconds':time.time()-tic,'inputs_sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['precision-fourth-source-result.json','precision-completed-symbol-result.json']}}
(R/'precision-fourth-elimination-result.json').write_text(json.dumps(out,indent=2));np.savez_compressed(R/'precision-fourth-elimination.npz',left_quotient=left,source=bf,principal=A)
print({k:z for k,z in out.items() if k not in ['remaining_residual_real_packed','fourth_coefficients_real_packed','selected_rows','selected_columns']},flush=True)
