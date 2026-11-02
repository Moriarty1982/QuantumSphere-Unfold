"""Prolongations of rebuilt completed symbol; deliberately no old Omega row."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
from pathlib import Path
import numpy as np,json,itertools,hashlib
R=Path(__file__).resolve().parent;f=R/'precision-completed-symbol-result.json';data=json.loads(f.read_text());J=np.array(data['matrix_decimal'],float);rows=[]
for p in range(1,5):
 low=list(itertools.combinations_with_replacement(range(4),p-1));hi=list(itertools.combinations_with_replacement(range(4),p));lookup={a:i for i,a in enumerate(hi)};A=np.zeros((32*len(low),24*len(hi)))
 for i,a in enumerate(low):
  for mu in range(4):
   j=lookup[tuple(sorted((*a,mu)))];A[32*i:32*(i+1),24*j:24*(j+1)]+=(a.count(mu)+1)*J[:,24*mu:24*(mu+1)]
 sv=np.linalg.svd(A,compute_uv=False);tests=[{'cutoff':c,'rank':int(sum(sv>sv[0]*c))} for c in [1e-8,1e-10,1e-12]];r=tests[1]['rank'];rows.append({'degree':p,'dimension':A.shape[1]-r,'tests':tests,'singular_boundary':sv[max(0,r-2):r+2].tolist()})
print(rows)
(R/'precision-symbol-prolongation-result.json').write_text(json.dumps({'contract':'Float64 prolongations from newly reconstructed 70-digit completed symbol at new root. Omega deliberately excluded: old Omega cannot be identified at changed root. Not high-precision SVD or exact rank proof.','input_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'results':rows},indent=2))
