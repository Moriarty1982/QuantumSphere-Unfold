"""Finite Spencer2 cohomology diagnostic of the Ω-augmented frozen symbol."""
from pathlib import Path
import itertools,numpy as np,json,time,math
ROOT=Path(__file__).resolve().parent
w=np.load(ROOT/'completion-omega-witness.npz');J=w['completed_first_symbol'];theta=w['theta_normalized'];tic=time.time()
def idx(d):return list(itertools.combinations_with_replacement(range(4),d))
def fac(a):return math.prod(math.factorial(a.count(mu)) for mu in range(4))
bases={};lists={};ranks={}
for p in range(2,7):
 ri=idx(p-1);ci=idx(p);lookup={a:n for n,a in enumerate(ci)};A=np.zeros((len(ri)*32,len(ci)*24))
 for rn,a in enumerate(ri):
  for mu in range(4):
   cn=lookup[tuple(sorted((*a,mu)))];A[rn*32:(rn+1)*32,cn*24:(cn+1)*24]+=(a.count(mu)+1)*J[:,mu*24:(mu+1)*24]
 if p>=3:
  om=np.zeros((len(idx(p-3)),len(ci)*24))
  for rn,gamma in enumerate(idx(p-3)):
   for bn,beta in enumerate(idx(3)):
    delta=tuple(sorted((*beta,*gamma)));cn=lookup[delta]
    om[rn,cn*24:(cn+1)*24]+=theta[bn*24:(bn+1)*24]*fac(delta)/(fac(beta)*fac(gamma))
  A=np.vstack((A,om))
 u,sv,vh=np.linalg.svd(A,full_matrices=True);r=int(sum(sv>sv[0]*1e-9));bases[p]=vh[r:].T;lists[p]=ci;ranks[p]=r
def contractions(p):
 low=lists[p-1];high=lists[p];look={a:n for n,a in enumerate(high)};N=bases[p];out=[]
 for mu in range(4):
  blocks=[]
  for alpha in low:
   cn=look[tuple(sorted((*alpha,mu)))];blocks.append((alpha.count(mu)+1)*N[cn*24:(cn+1)*24])
  C=np.vstack(blocks)
  out.append(bases[p-1].T@C)
 return out
def delta(p,q):
 # g_p tensor exterior^(q-1) -> g_(p-1) tensor exterior^q.
 C=contractions(p);ins=list(itertools.combinations(range(4),q-1));outs=list(itertools.combinations(range(4),q));di=bases[p].shape[1];do=bases[p-1].shape[1];A=np.zeros((do*len(outs),di*len(ins)))
 for ii,I in enumerate(ins):
  for mu in range(4):
   if mu in I:continue
   out=tuple(sorted((mu,*I)));oi=outs.index(out);sgn=(-1)**sum(v<mu for v in I)
   A[oi*do:(oi+1)*do,ii*di:(ii+1)*di]+=sgn*C[mu]
 return A
rows=[]
for p in [3,4,5]:
 d1=delta(p+1,2);d2=delta(p,3);s1=np.linalg.svd(d1,compute_uv=False);s2=np.linalg.svd(d2,compute_uv=False);tests=[]
 for cut in [1e-8,1e-9,1e-10,1e-11]:
  r1=int(sum(s1>s1[0]*cut));r2=int(sum(s2>s2[0]*cut));tests.append({'rcond':cut,'incoming_rank':r1,'outgoing_rank':r2,'H2_dimension':bases[p].shape[1]*6-r1-r2})
 near1=s1[max(0,tests[1]['incoming_rank']-4):tests[1]['incoming_rank']+4];near2=s2[max(0,tests[1]['outgoing_rank']-3):tests[1]['outgoing_rank']+3]
 out={'symbol_degree':p,'dimension':bases[p].shape[1],'delta_complex_error':float(np.linalg.norm(d2@d1)),'tests':tests,'incoming_rank_boundary_singular_values':near1.tolist(),'outgoing_rank_boundary_singular_values':near2.tolist(),'incoming_largest':float(s1[0]),'outgoing_largest':float(s2[0])};rows.append(out);print(out,flush=True)
 (ROOT/'omega-spencer-result.json').write_text(json.dumps({'contract':'Frozen-symbol finite Spencer H^(p,2) checks only, Ωaugmented. No formalintegrability/existence theorem fromfinitecohomologytests.','seconds':time.time()-tic,'results':rows},indent=2))
