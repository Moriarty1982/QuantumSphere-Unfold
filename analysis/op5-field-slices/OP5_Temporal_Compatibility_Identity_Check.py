from pathlib import Path
import numpy as np,json
# Reuse definitions, but compute three diagnostic points ourselves.
ns={};exec(Path('OP5_Temporal_Coframe_Gauge_Check.py').read_text().split('for p in points:')[0],ns)
T=ns['T'];compute=ns['ns']['compute'];old=ns['old'];out=[]
for p in ns['points']:
 psi=compute(T.tensor(p[None]))[3].detach().numpy()[0];hf=1e-6;jets=np.array([(compute(T.tensor((p+hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0]-compute(T.tensor((p-hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0])/(2*hf) for mu in range(4)])
 gg,hh,spin=old['back'](*p);cov=jets.copy()
 for mu in range(1,4):cov[mu]+=1j*np.kron(np.asarray(gg)*np.asarray(spin).ravel()[mu-1],np.eye(4))@psi
 Q=old['QQ'];pack=lambda z:np.r_[z.real,z.imag];B=np.column_stack([pack(v) for v in cov]);A=np.column_stack([[np.vdot(psi,q@(np.eye(12,dtype=complex)[k%12]*(1 if k<12 else 1j))).real for q in Q] for k in range(24)])
 E=np.array([[np.vdot(psi,q@cov[mu]).real for mu in range(4)] for q in Q]);inv=np.linalg.inv(E);P=np.eye(24)-B@np.linalg.solve(E,A)
 Hc=1j*sum(inv[0,a]*old['KK'][a] for a in range(4));H=np.block([[Hc.real,-Hc.imag],[Hc.imag,Hc.real]]);L=np.linalg.solve(H.T,A.T).T
 h=1e-5;cols=[]
 for k in range(24):
  delta=np.zeros((4,12),complex);delta[0,k%12]=1 if k<12 else 1j;cols.append((old['residual'](p,psi,jets+h*delta)-old['residual'](p,psi,jets-h*delta))/(2*h))
 J=np.column_stack(cols);u,sv,vh=np.linalg.svd(J,full_matrices=True);left=u[:,20:].T
 w=np.kron(np.array(old['S'],complex),np.eye(4))@psi;ell=np.r_[-w.imag,w.real];coeff=np.linalg.lstsq(L.T,ell,rcond=1e-12)[0];r=old['residual'](p,psi,jets)
 rowproj=L.T@np.linalg.solve(L@L.T,L);orth=left.T@left
 out.append({'point':p.tolist(),'J_minus_HP_relative':float(np.linalg.norm(J-H@P)/np.linalg.norm(J)),'LJ_norm':float(np.linalg.norm(L@J)),'rankL':int(np.linalg.matrix_rank(L)),'left_projector_difference':float(np.linalg.norm(rowproj-orth)),'scalar_row_reconstruction_error':float(np.linalg.norm(coeff@L-ell)),'scalar_combination_coefficients':coeff.tolist(),'constraint_vector':(L@r).tolist(),'known_scalar_constraint':float(ell@r),'best_unrepairable_time_residual':float(np.linalg.norm(rowproj@r)),'full_residual':float(np.linalg.norm(r))})
 assert out[-1]['J_minus_HP_relative']<1e-7 and out[-1]['left_projector_difference']<1e-7
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
