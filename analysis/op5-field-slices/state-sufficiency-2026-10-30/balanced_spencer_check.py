"""Pinned frozen Ω-symbol Spencer test in raw and tensor-balanced symmetric bases."""
from pathlib import Path
import os
os.environ.setdefault('OMP_NUM_THREADS','2');os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import itertools,math,time,hashlib,json,platform,numpy as np
ROOT=Path(__file__).resolve().parent;witness=ROOT/'completion-omega-witness.npz';sha=hashlib.sha256(witness.read_bytes()).hexdigest();tic=time.time()
w=np.load(witness,allow_pickle=False);J=w['completed_first_symbol'];theta=w['theta_normalized']
def idx(d):return list(itertools.combinations_with_replacement(range(4),d))
def fac(alpha):return math.prod(math.factorial(alpha.count(mu)) for mu in range(4))
def matrix(p):
    ri=idx(p-1);ci=idx(p);look={a:n for n,a in enumerate(ci)};A=np.zeros((len(ri)*32,len(ci)*24))
    for rn,alpha in enumerate(ri):
        for mu in range(4):
            cn=look[tuple(sorted((*alpha,mu)))];A[rn*32:(rn+1)*32,cn*24:(cn+1)*24]+=(alpha.count(mu)+1)*J[:,mu*24:(mu+1)*24]
    rowweights=np.repeat([math.sqrt(fac(a)) for a in ri],32)
    if p>=3:
        om=np.zeros((len(idx(p-3)),len(ci)*24))
        for rn,gamma in enumerate(idx(p-3)):
            for bn,beta in enumerate(idx(3)):
                delta=tuple(sorted((*beta,*gamma)));cn=look[delta]
                om[rn,cn*24:(cn+1)*24]+=theta[bn*24:(bn+1)*24]*fac(delta)/(fac(beta)*fac(gamma))
        A=np.vstack((A,om));rowweights=np.r_[rowweights,[math.sqrt(fac(a)) for a in idx(p-3)]]
    colweights=np.repeat([math.sqrt(fac(a)) for a in ci],24)
    B=rowweights[:,None]*A/colweights[None,:]
    # Separate direct factorial-balanced assembly, including the higher Ω equation.
    direct=np.zeros_like(B)
    for rn,alpha in enumerate(ri):
        for mu in range(4):
            cn=look[tuple(sorted((*alpha,mu)))];direct[rn*32:(rn+1)*32,cn*24:(cn+1)*24]+=math.sqrt(alpha.count(mu)+1)*J[:,mu*24:(mu+1)*24]
    if p>=3:
        off=len(ri)*32
        for rn,gamma in enumerate(idx(p-3)):
            for bn,beta in enumerate(idx(3)):
                delta=tuple(sorted((*beta,*gamma)));cn=look[delta]
                factor=math.sqrt(fac(delta))/(fac(beta)*math.sqrt(fac(gamma)))
                direct[off+rn,cn*24:(cn+1)*24]+=theta[bn*24:(bn+1)*24]*factor
    return A,B,float(np.linalg.norm(B-direct)),rowweights,colweights

def run_variant(name):
    bases={};lists={};symbol_rows=[];balanced=name!='raw'
    for p in range(2,7):
        A,B,assemblyerror,rw,cw=matrix(p);X=A if not balanced else B
        if name=='balanced_row_equilibrated':
            rowscale=np.linalg.norm(X,axis=1);X=X/np.maximum(rowscale,1e-300)[:,None]
        U,sv,Vh=np.linalg.svd(X,full_matrices=True);r=int(np.sum(sv>sv[0]*1e-9));N=Vh[r:].T;bases[p]=N;lists[p]=idx(p)
        symbol_rows.append({'degree':p,'shape':list(X.shape),'rank_relative1e-9':r,'kernel_dimension':N.shape[1],'largest':float(sv[0]),'smallest_retained':float(sv[r-1]),'largest_discarded':float(sv[r]) if r<len(sv) else 0.,'relative_null_residual':float(np.linalg.norm(X@N)/np.linalg.norm(X)),'balanced_direct_assembly_error':assemblyerror})
    leaks={}
    def contractions(p):
        low=lists[p-1];high=lists[p];look={a:n for n,a in enumerate(high)};out=[];vals=[]
        for mu in range(4):
            C=np.vstack([(math.sqrt(alpha.count(mu)+1) if balanced else alpha.count(mu)+1)*bases[p][look[tuple(sorted((*alpha,mu)))]*24:(look[tuple(sorted((*alpha,mu)))]+1)*24] for alpha in low])
            projected=bases[p-1].T@C;vals.append(float(np.linalg.norm(C-bases[p-1]@projected)));out.append(projected)
        leaks[p]=max(vals);return out
    def delta(p,q):
        C=contractions(p);ins=list(itertools.combinations(range(4),q-1));outs=list(itertools.combinations(range(4),q));di=bases[p].shape[1];do=bases[p-1].shape[1];D=np.zeros((do*len(outs),di*len(ins)))
        for ii,I in enumerate(ins):
            for mu in range(4):
                if mu in I:continue
                target=tuple(sorted((mu,*I)));oi=outs.index(target);sign=(-1)**sum(v<mu for v in I)
                D[oi*do:(oi+1)*do,ii*di:(ii+1)*di]+=sign*C[mu]
        return D
    rows=[]
    for p in (3,4,5):
        incoming=delta(p+1,2);outgoing=delta(p,3);s1=np.linalg.svd(incoming,compute_uv=False);s2=np.linalg.svd(outgoing,compute_uv=False);tests=[]
        for cut in (1e-8,1e-9,1e-10,1e-11,1e-12):
            r1=int(np.sum(s1>s1[0]*cut));r2=int(np.sum(s2>s2[0]*cut));tests.append({'relative_cutoff':cut,'incoming_rank':r1,'outgoing_rank':r2,'putative_H2_dimension':bases[p].shape[1]*6-r1-r2})
        r1=tests[1]['incoming_rank'];r2=tests[1]['outgoing_rank'];err=np.linalg.norm(outgoing@incoming)
        row={'degree':p,'g_dimension':bases[p].shape[1],'incoming_shape':list(incoming.shape),'outgoing_shape':list(outgoing.shape),'complex_product_norm':float(err),'complex_product_relative':float(err/(np.linalg.norm(incoming)*np.linalg.norm(outgoing))),
             'incoming_largest':float(s1[0]),'outgoing_largest':float(s2[0]),'incoming_boundary':s1[max(0,r1-7):r1+9].tolist(),'outgoing_boundary':s2[max(0,r2-5):r2+6].tolist(),'tests':tests,
             'contraction_leak_incoming':leaks[p+1],'contraction_leak_outgoing':leaks[p]}
        rows.append(row);print(name,'p',p,'complex',err,'tests',tests,flush=True)
    return {'name':name,'symbols':symbol_rows,'spencer':rows}

if __name__=='__main__':
    rng=np.random.default_rng(20261030);raw=rng.normal(size=480);weights=np.repeat([math.sqrt(fac(a)) for a in idx(3)],24);balanced=weights*raw;thetab=theta/weights;polyerror=float(abs(theta@raw-thetab@balanced))
    variants=[]
    for name in ('raw','balanced','balanced_row_equilibrated'):
        variants.append(run_variant(name))
        out={'contract':'Frozen pinned Ω-augmented symbol only, tensor-balanced basis y_alpha=sqrt(alpha!) c_alpha. Invertible coefficient/row changes, identical polynomial constraints. Numerical cohomology diagnostics are not analyticrank/cohomology certificates.','seconds':time.time()-tic,'witness_sha256':sha,'witness_unchanged':hashlib.sha256(witness.read_bytes()).hexdigest()==sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'software':{'python':platform.python_version(),'numpy':np.__version__},'theta_polynomial_coordinate_change_error':polyerror,'variants':variants}
        (ROOT/'balanced_spencer_result.json').write_text(json.dumps(out,indent=2))
