"""Bounded projection gate of completed R2->R1 at point0, no model or old result writes."""
from pathlib import Path
import textwrap,json,hashlib,time,itertools,numpy as np,torch as T
ROOT=Path(__file__).resolve().parent
authoritative=ROOT/'completed_tableau_check.py';text=authoritative.read_text()
inputs=[Path(__file__).resolve(),authoritative,ROOT/'recursive_calibrator.py',ROOT/'fifth-window-result.json']
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs};tic=time.time()
ns={'__file__':str(authoritative)};exec(text.split("for row in data['results']:")[0],ns)
ns['row']=ns['data']['results'][0]
exec(textwrap.dedent(text.split("for row in data['results']:")[1].split(' q=T.tensor')[0]),ns)
model=ns['model'];row=ns['row'];R=ns['R'];m=ns['m'];psi=ns['psi'];j=ns['j'];pos=ns['pos']
q=np.r_[m.pack(psi),m.pack(j),pos];qT=T.tensor(q);DR=T.func.jacrev(R);D=DR(qT).detach().numpy();J=D[:,24:120]
U,sv,Vh=np.linalg.svd(J,full_matrices=True);rankJ=int(np.sum(sv>sv[0]*1e-9));N=Vh[rankJ:].T
pairs=list(itertools.combinations_with_replacement(range(4),2));A=np.zeros((128,240))
for pn,(mu,nu) in enumerate(pairs):
    A[mu*32:(mu+1)*32,pn*24:(pn+1)*24]=J[:,nu*24:(nu+1)*24]
    if mu!=nu:A[nu*32:(nu+1)*32,pn*24:(pn+1)*24]=J[:,mu*24:(mu+1)*24]
u,svA,v=np.linalg.svd(A,full_matrices=True);rankA=int(np.sum(svA>svA[0]*1e-9));L=u[:,rankA:]
lookup={tuple(a):n for n,a in enumerate(row['multiindices'])};packed=np.array(row['coefficients_real_imag']);oldH=[]
for mu,nu in pairs:
    alpha=tuple(int(mu==k)+int(nu==k) for k in range(4));oldH.append(packed[lookup[alpha]]*m.factorial(alpha))
oldH=np.array(oldH).ravel()
def unpackH(h):
    hh=h.reshape(10,24);full=np.empty((4,4,24))
    for pn,(mu,nu) in enumerate(pairs):full[mu,nu]=full[nu,mu]=hh[pn]
    return full
def tangent(qvalue,h):
    js=qvalue[24:120].reshape(4,24);H=unpackH(h)
    return np.vstack((js.T,H.transpose(1,2,0).reshape(96,4),np.eye(4)))
def prolonged(qvalue,h):return (DR(T.tensor(qvalue)).detach().numpy()@tangent(qvalue,h)).T.ravel()
actual=prolonged(q,oldH);delta,_,_,_=np.linalg.lstsq(A,-actual,rcond=1e-9);H=oldH+delta;repaired=prolonged(q,H)
print('BASE',rankJ,rankA,'R',np.linalg.norm(R(qT).detach().numpy()),'dRold',np.linalg.norm(actual),'dRrepair',np.linalg.norm(repaired),'Hchange',np.linalg.norm(delta),flush=True)
gates=[]
for eps in [1e-4,1e-5]:
    columns=[];tangency=[]
    for k in range(N.shape[1]):
        dq=np.zeros(124);dq[24:120]=N[:,k];qp=q+eps*dq;qm=q-eps*dq
        columns.append(L.T@(prolonged(qp,H)-prolonged(qm,H))/(2*eps))
        rp=R(T.tensor(qp)).detach().numpy();rm=R(T.tensor(qm)).detach().numpy();tangency.append(float(max(np.linalg.norm(rp),np.linalg.norm(rm))))
    gate=np.column_stack(columns);sg=np.linalg.svd(gate,compute_uv=False)
    gates.append({'step':eps,'matrix':gate.tolist(),'singular_values':sg.tolist(),'norm':float(np.linalg.norm(gate)),'max_tangent_R_after_step':max(tangency),'nominal_rank_relative1e-8':int(np.sum(sg>sg[0]*1e-8))})
    print('GATE',eps,'norm',np.linalg.norm(gate),'sv',sg,flush=True)
diff=np.linalg.norm(np.array(gates[0]['matrix'])-np.array(gates[1]['matrix']));sg=np.array(gates[1]['singular_values']);noise_cut=max(sg[0]*1e-8,10*diff)
out={'contract':'Point0 completed R=(F24,G4,dg4) projection gate. Fixedpsi,position; tangent firstjet variations kerJ, fixed repaired symmetricH; complete leftkernel of base A2. Finite differences all65directions. No analyticrank/propagation theorem.',
 'seconds':time.time()-tic,'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in inputs),
 'R_norm':float(np.linalg.norm(R(qT).detach().numpy())),'J_shape':list(J.shape),'J_rank':rankJ,'J_singular_values':sv.tolist(),'tangent_dimension':N.shape[1],
 'A2_shape':list(A.shape),'A2_rank':rankA,'A2_singular_values':svA.tolist(),'left_dimension':L.shape[1],
 'saved_H_prolongation_norm':float(np.linalg.norm(actual)),'repaired_H_prolongation_norm':float(np.linalg.norm(repaired)),'H_correction_norm':float(np.linalg.norm(delta)),'H_repaired_norm':float(np.linalg.norm(H)),
 'J_times_N_norm':float(np.linalg.norm(J@N)),'left_times_A2_norm':float(np.linalg.norm(L.T@A)),
 'gates':gates,'step_matrix_difference_norm':float(diff),'empirical_noise_aware_rank_cutoff':float(noise_cut),'empirical_stable_gate_rank_lower_bound':int(np.sum(sg>noise_cut))}
(ROOT/'completed_review_projection_gate_result.json').write_text(json.dumps(out,indent=2));print('DIFFERENCE',diff,'noise-awarerank',out['empirical_stable_gate_rank_lower_bound'],flush=True)
