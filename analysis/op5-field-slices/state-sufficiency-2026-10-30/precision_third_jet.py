"""Third jet completion with all repaired lower jets fixed."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import numpy as np,mpmath as mp,json,itertools,time,hashlib
R=Path(__file__).resolve().parent;mp.mp.dps=70;tic=time.time();source=json.loads((R/'precision-third-source-result.json').read_text());J=mp.matrix([[mp.mpf(x) for x in row] for row in json.loads((R/'precision-completed-symbol-result.json').read_text())['matrix_decimal']]);low=list(itertools.combinations_with_replacement(range(4),2));high=list(itertools.combinations_with_replacement(range(4),3));lookup={a:i for i,a in enumerate(high)};A=mp.zeros(320,480)
for i,alpha in enumerate(low):
 for mu in range(4):
  col=lookup[tuple(sorted((*alpha,mu)))];weight=alpha.count(mu)+1
  for j in range(32):
   for k in range(24):A[i*32+j,col*24+k]+=weight*J[j,mu*24+k]
a=np.array(A.tolist(),float);basis=[];keep=[]
for i,row in enumerate(a):
 z=row.copy()
 for _ in range(2):
  for q in basis:z-=q@z*q
 n=np.linalg.norm(z)
 if n>1e-9:basis.append(z/n);keep.append(i)
print('selected',len(keep),flush=True)
if len(keep)!=271:raise RuntimeError('Unexpected third rank')
old=json.loads((R/'fifth-window-result.json').read_text(),parse_float=str)['results'][0];oldmap={tuple(alpha):value for alpha,value in zip(old['multiindices'],old['coefficients_real_imag'])};c=mp.matrix([mp.mpf(x) for axes in high for x in oldmap[tuple(axes.count(mu) for mu in range(4))]]);b=mp.matrix([mp.mpf(x) for x in source['source_real_packed']]);initial=A*c+b;B=mp.matrix([[A[i,j] for j in range(480)] for i in keep]);rhs=mp.matrix([-initial[i] for i in keep]);dx=B.T*((B*B.T)**-1)*rhs;c+=dx;res=A*c+b
out={'contract':'70-digit finite third jet of completed system; repaired field through degree2 fixed. All degree3 coefficients free. Full320 degree2 R residuals checked, not only271 selected rows. No fourth jet, Omega, regional existence or certified exact rank.','row_count':len(keep),'initial_residual_max':mp.nstr(max(abs(x) for x in initial),24),'full_residual_max':mp.nstr(max(abs(x) for x in res),24),'correction_max':mp.nstr(max(abs(x) for x in dx),24),'triples':high,'third_coefficients_real_packed':[mp.nstr(x,70) for x in c],'seconds':time.time()-tic,'input_sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['precision-third-source-result.json','precision-completed-symbol-result.json','precision-second-jet-result.json']}}
(R/'precision-third-jet-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k!='third_coefficients_real_packed'},flush=True)
