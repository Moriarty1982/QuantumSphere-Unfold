"""Refine a full left compatibility witness, not just selected equations."""
import os
os.environ['OPENBLAS_NUM_THREADS']='2'
from pathlib import Path
import json,numpy as np,mpmath as mp,itertools,hashlib
R=Path(__file__).resolve().parent;mp.mp.dps=70;raw=json.loads((R/'precision-fourth-elimination-result.json').read_text());inp=json.loads((R/'precision-completed-symbol-result.json').read_text());jm=[[mp.mpf(x) for x in row] for row in inp['matrix_decimal']];cache=np.load(R/'precision-fourth-elimination.npz');A=cache['principal'];rows=raw['selected_rows'];cols=raw['selected_columns'];inv=np.linalg.inv(A[np.ix_(rows,cols)]);res=[mp.mpf(x) for x in raw['remaining_residual_real_packed']];target=max(range(640),key=lambda i:abs(res[i]));lam=[mp.mpf('0') for _ in range(640)];lam[target]=1
for i,c in zip(rows,-A[target,cols]@inv):lam[i]=mp.mpf(float(c))
low=list(itertools.combinations_with_replacement(range(4),3));hi=list(itertools.combinations_with_replacement(range(4),4));lookup={a:i for i,a in enumerate(hi)}
def leftapply(l):
 out=[mp.mpf('0') for _ in range(840)]
 for i,alpha in enumerate(low):
  for mu in range(4):
   col=lookup[tuple(sorted((*alpha,mu)))];w=alpha.count(mu)+1
   for k in range(24):out[col*24+k]+=w*mp.fsum(l[i*32+j]*jm[j][mu*24+k] for j in range(32))
 return out
for _ in range(7):
 z=leftapply(lam);d=-np.array([float(z[c]) for c in cols])@inv
 for i,v in zip(rows,d):lam[i]+=mp.mpf(float(v))
z=leftapply(lam);b=[mp.mpf(x) for x in json.loads((R/'precision-fourth-source-result.json').read_text())['source_real_packed']];source=mp.fsum(l*v for l,v in zip(lam,b));ln=mp.sqrt(mp.fsum(v*v for v in lam));old=np.load(R/'completion-omega-witness.npz')['ambient_left_witness'];lf=np.array([float(x/ln) for x in lam]);cos=float(abs(lf@old)/np.linalg.norm(old))
out={'contract':'Numerical 70-digit left witness at repaired common lower germ. Full840 columns tested, nonzero source separates fixed lower data from fourth-jet completion. Not exact algebra or an interval certificate; does not rule out adjusting third jets.','target_row':target,'full_left_annihilation_max':mp.nstr(max(abs(v) for v in z),24),'left_source':mp.nstr(source,24),'normalized_left_source':mp.nstr(source/ln,24),'witness_norm':mp.nstr(ln,24),'cosine_old_ambient_witness':cos,'left_witness':[mp.nstr(v,70) for v in lam],'inputs_sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['precision-fourth-source-result.json','precision-completed-symbol-result.json','precision-fourth-elimination-result.json']}}
(R/'precision-fourth-left-witness-result.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items() if k!='left_witness'})
