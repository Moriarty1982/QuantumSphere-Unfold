"""Recursive balanced prolongation diagnostic; no existence claim."""
from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='2';os.environ['OMP_NUM_THREADS']='2'
import numpy as np,json,time,hashlib
ROOT=Path(__file__).resolve().parent
a={"__file__":str(ROOT/"balanced_spencer_check.py")};exec((ROOT/'balanced_spencer_check.py').read_text().split('def run_variant')[0],a)
idx=a['idx'];matrix=a['matrix'];tic=time.time();bases={};complements={};symbols=[]
for p in range(2,7):
 ci=idx(p)
 if p<=3:
  X=matrix(p)[1];rn=np.linalg.norm(X,axis=1);X=X/np.maximum(rn,1e-300)[:,None]
 else:
  low=idx(p-1);lookup={v:i for i,v in enumerate(ci)};Q=complements[p-1];blocks=[]
  for mu in range(4):
   B=np.zeros((Q.shape[0],len(ci)*24))
   for i,alpha in enumerate(low):
    j=lookup[tuple(sorted((*alpha,mu)))];B[:,j*24:(j+1)*24]+=(alpha.count(mu)+1)**.5*Q[:,i*24:(i+1)*24]
   blocks.append(B)
  X=np.vstack(blocks)
 U,s,V=np.linalg.svd(X,full_matrices=True);r=int(sum(s>s[0]*1e-9));bases[p]=V[r:].T;complements[p]=V[:r]
 row={'degree':p,'rank':r,'dimension':len(ci)*24-r,'boundary':s[max(0,r-3):r+3].tolist()};symbols.append(row);print(row,flush=True)
def contractions(p):
 low=idx(p-1);look={v:i for i,v in enumerate(idx(p))};out=[]
 for mu in range(4):
  C=np.vstack([(v.count(mu)+1)**.5*bases[p][look[tuple(sorted((*v,mu)))]*24:(look[tuple(sorted((*v,mu)))]+1)*24] for v in low]);out.append(bases[p-1].T@C)
 return out
def delta(p,q):
 import itertools
 C=contractions(p);ins=list(itertools.combinations(range(4),q-1));outs=list(itertools.combinations(range(4),q));di=bases[p].shape[1];do=bases[p-1].shape[1];D=np.zeros((do*len(outs),di*len(ins)))
 for i,I in enumerate(ins):
  for mu in range(4):
   if mu in I:continue
   j=outs.index(tuple(sorted((mu,*I))));D[j*do:(j+1)*do,i*di:(i+1)*di]+=(-1)**sum(v<mu for v in I)*C[mu]
 return D
results=[]
for p in [3,4,5]:
 A=delta(p+1,2);B=delta(p,3);s=np.linalg.svd(A,compute_uv=False);t=np.linalg.svd(B,compute_uv=False);tests=[]
 for cut in [1e-8,1e-9,1e-10,1e-11]:
  ra=int(sum(s>s[0]*cut));rb=int(sum(t>t[0]*cut));tests.append({'cut':cut,'incoming':ra,'outgoing':rb,'putative_H2':6*bases[p].shape[1]-ra-rb})
 r=tests[1]['incoming'];row={'degree':p,'complex_error':float(np.linalg.norm(B@A)),'tests':tests,'incoming_boundary':s[r-5:r+5].tolist()};results.append(row);print(row,flush=True)
 (ROOT/'recursive-spencer-result.json').write_text(json.dumps({'input_sha256':hashlib.sha256((ROOT/'completion-omega-witness.npz').read_bytes()).hexdigest(),'contract':'Numerical recursive prolongation from rounded third symbol; not exact original PDE or existence proof','symbols':symbols,'results':results,'seconds':time.time()-tic},indent=2))

