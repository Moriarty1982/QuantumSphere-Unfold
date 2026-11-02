"""Full R1 tangent projection at point0, exact AD with background through degree3."""
from pathlib import Path
import textwrap,json,hashlib,time,itertools,numpy as np,torch as T
ROOT=Path(__file__).resolve().parent;authoritative=ROOT/'completed_tableau_check.py';source=authoritative.read_text();tic=time.time()
space={'__file__':str(authoritative)}
prefix=source.split("for row in data['results']:")[0].replace('model=m.TaylorModel(3)','model=m.TaylorModel(4)')
exec(prefix,space);space['row']=space['data']['results'][0]
exec(textwrap.dedent(source.split("for row in data['results']:")[1].split(' q=T.tensor')[0]),space)
model=space['model'];row=space['row'];R=space['R'];m=space['m'];psi=space['psi'];j=space['j'];pos=space['pos'];DR=T.func.jacrev(R)
q=np.r_[m.pack(psi),m.pack(j),pos];qt=T.tensor(q);rr=R(qt).detach().numpy();D=DR(qt).detach().numpy();J=D[:,24:120]
uf,sf,vf=np.linalg.svd(D,full_matrices=True);rankFull=int(np.sum(sf>sf[0]*1e-9));Nfull=vf[rankFull:].T
uj,sj,vj=np.linalg.svd(J,full_matrices=True);rankJ=int(np.sum(sj>sj[0]*1e-9));Nvertical=vj[rankJ:].T
pairs=list(itertools.combinations_with_replacement(range(4),2));A=np.zeros((128,240))
for pn,(mu,nu) in enumerate(pairs):
    A[mu*32:(mu+1)*32,pn*24:(pn+1)*24]=J[:,nu*24:(nu+1)*24]
    if mu!=nu:A[nu*32:(nu+1)*32,pn*24:(pn+1)*24]=J[:,mu*24:(mu+1)*24]
ua,sa,va=np.linalg.svd(A,full_matrices=True);rankA=int(np.sum(sa>sa[0]*1e-9));L=ua[:,rankA:]
lookup={tuple(alpha):n for n,alpha in enumerate(row['multiindices'])};packed=np.array(row['coefficients_real_imag']);hp=[]
for mu,nu in pairs:
    alpha=tuple(int(mu==k)+int(nu==k) for k in range(4));hp.append(packed[lookup[alpha]]*m.factorial(alpha))
hp=np.array(hp).ravel()
def unpackH(h):
    hh=h.reshape(10,24);out=np.empty((4,4,24))
    for pn,(mu,nu) in enumerate(pairs):out[mu,nu]=out[nu,mu]=hh[pn]
    return out
def tangent(qvalue,h):
    js=qvalue[24:120].reshape(4,24);H=unpackH(h)
    return np.vstack((js.T,H.transpose(1,2,0).reshape(96,4),np.eye(4)))
def prolonged(qvalue,h):return (DR(T.tensor(qvalue)).detach().numpy()@tangent(qvalue,h)).T.ravel()
initial=prolonged(q,hp);delta=np.linalg.lstsq(A,-initial,rcond=1e-9)[0];H=hp+delta;Ht=T.tensor(unpackH(H));repaired=prolonged(q,H)
def prolonged_full(qvalue):
    tangentT=T.cat((qvalue[24:120].reshape(4,24).T,Ht.permute(1,2,0).reshape(96,4),T.eye(4)),dim=0)
    return (DR(qvalue)@tangentT).T.flatten()
DH=T.func.jacrev(prolonged_full)(qt).detach().numpy();gate=L.T@DH@Nfull;sg=np.linalg.svd(gate,compute_uv=False);vertical=L.T@DH[:,24:120]@Nvertical
paths=[Path(__file__),authoritative,ROOT/'recursive_calibrator.py',ROOT/'fifth-window-result.json',model.source];hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out={'contract':'Point0 full R1 tangent gate, R=(F24,G4,dg4). Background exactTaylor through degree3; multiplication monomials avoid zero-power AD pathology. Fixed repaired symmetricH. Full q=(psi24,jets96,position4) kernel of D_R. No analytic neighborhood or propagation theorem.',
 'seconds':time.time()-tic,'inputs_sha256':hashes,'background_order':3,'R_norm':float(np.linalg.norm(rr)),
 'D_R_shape':list(D.shape),'D_R_rank':rankFull,'D_R_singular_values':sf.tolist(),'full_tangent_dimension':Nfull.shape[1],'D_R_times_N_norm':float(np.linalg.norm(D@Nfull)),
 'J_rank':rankJ,'vertical_tangent_dimension':Nvertical.shape[1],'A2_rank':rankA,'A2_shape':list(A.shape),'A2_singular_values':sa.tolist(),'left_dimension':L.shape[1],
 'initial_prolongation_norm':float(np.linalg.norm(initial)),'repaired_prolongation_norm':float(np.linalg.norm(repaired)),'H_change_norm':float(np.linalg.norm(delta)),
 'full_unprojected_derivative_norm':float(np.linalg.norm(DH)),'gate_shape':list(gate.shape),'gate_norm':float(np.linalg.norm(gate)),'gate_singular_values':sg.tolist(),'gate_matrix':gate.tolist(),
 'gate_norm_relative_to_DH':float(np.linalg.norm(gate)/np.linalg.norm(DH)),'vertical_gate_norm':float(np.linalg.norm(vertical)),
 'rank_sweep':{str(cut):int(np.sum(sg>max(cut*max(sg[0],1),1e-10))) for cut in (1e-7,1e-8,1e-9)}}
(ROOT/'completed_review_full_gate_result.json').write_text(json.dumps(out,indent=2));print('FULL',rankFull,Nfull.shape,'R',np.linalg.norm(rr),'prolong',np.linalg.norm(repaired),'gate',np.linalg.norm(gate),'sv',sg,'relative',out['gate_norm_relative_to_DH'],'vertical',np.linalg.norm(vertical),flush=True)
