"""First symbol/source identities; no nonlinear formal-integrability claim."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,itertools,hashlib
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(2);old=json.loads((ROOT/'fifth-window-result.json').read_text());rows=[]
def realmat(z):return np.block([[z.real,-z.imag],[z.imag,z.real]])
Gamma=model.K.numpy();H=np.array([realmat(1j*k) for k in Gamma]);Hb=H.copy();Hb[0]*=-1
S=np.kron(np.array(model.ns['S'],complex),np.eye(4));pairs=list(itertools.combinations_with_replacement(range(4),2))
for row in old['results']:
 pos=np.array(row['point']);packed=np.array(row['coefficients_real_imag']);coeff=packed[:,:12]+1j*packed[:,12:];psi=coeff[0];jets=coeff[1:5]
 bg=model.background(pos).numpy();bt=T.tensor(bg[0]);db=T.tensor(bg[1:5].T.copy());pt=T.tensor(pos)
 def F(q):
  ps=m.unpack(q[:24])[0];j=m.unpack(q[24:120]);b=bt+db@(q[120:]-pt).to(T.complex128)
  cov=j+1j*T.einsum('mij,j->mi',b[1:].reshape(4,12,12),ps)
  E=T.einsum('i,aij,mj->am',ps.conj(),model.Q,cov).real
  f=1j*T.einsum('ma,aij,mj->i',T.linalg.inv(E).to(T.complex128),model.K,cov)-b[0].real*(model.Y@ps)
  return T.cat((f.real,f.imag))
 q=T.tensor(np.r_[m.pack(psi),m.pack(jets),pos]);D=T.func.jacrev(F)(q).detach().numpy();f=F(q).detach().numpy()
 conn=bg[0,1:].reshape(4,12,12);cov=jets+1j*np.einsum('mij,j->mi',conn,psi)
 E=np.einsum('i,aij,mj->am',psi.conj(),model.Q.numpy(),cov).real;V=np.linalg.inv(E)
 basis=np.r_[np.eye(12,dtype=complex),1j*np.eye(12,dtype=complex)]
 A=np.array([[np.vdot(psi,qq@v).real for v in basis] for qq in model.Q.numpy()]);B=m.pack(cov).reshape(4,24).T;P=np.eye(24)-B@V@A
 ell=np.r_[-(S@psi).imag,(S@psi).real];Hm=np.einsum('ma,aij->mij',V,H);Hbm=np.einsum('ma,aij->mij',V,Hb)
 K=np.einsum('ai,mij->maj',A,Hbm)
 # Real spinor principal blocks are packed per coefficient/coordinate.
 J=D[:,24:120];factor_error=np.linalg.norm(J-np.hstack([hh@P for hh in Hm]))
 b=np.array([D[:,120+mu]+D[:,:24]@m.pack(jets[mu]) for mu in range(4)]).ravel()
 AA=np.zeros((96,240))
 for n,(mu,nu) in enumerate(pairs):
  AA[mu*24:(mu+1)*24,n*24:(n+1)*24]=J[:,nu*24:(nu+1)*24]
  if mu!=nu:AA[nu*24:(nu+1)*24,n*24:(n+1)*24]=J[:,mu*24:(mu+1)*24]
 scalar=np.zeros((4,96))
 for mu in range(4):scalar[mu,mu*24:(mu+1)*24]=ell
 linear=np.hstack([K[mu] for mu in range(4)]);identities=np.vstack((scalar,linear))
 U,sv,vh=np.linalg.svd(AA,full_matrices=False);rank=int(sum(sv>sv[0]*1e-9));left=U[:,rank:]
 ui,si,vi=np.linalg.svd(identities,full_matrices=False);irank=int(sum(si>si[0]*1e-9));proj=vi[:irank].T@vi[:irank]
 nullchecks=[]
 for eta in [[1,1,0,0],[1,0,1,0],[1,0,0,1],[5,3,4,0]]:
  km=A@np.einsum('a,aij->ij',eta,Hb);ss=np.linalg.svd(km,compute_uv=False)
  nullchecks.append({'eta':eta,'rank':int(sum(ss>ss[0]*1e-9)),'singular_values':ss.tolist()})
 out={'point_index':row['point_index'],'A_rank':int(np.linalg.matrix_rank(A)),'principal_factorization_error':float(factor_error),'ell_H_minus_A':float(np.linalg.norm(np.array([ell@hh for hh in H])-A)),'second_symbol_rank':rank,'identity_rank':irank,'identity_annihilation':float(np.linalg.norm(identities@AA)),'left_projector_difference':float(np.linalg.norm(proj-left@left.T)),'g_derivative_source_rows':(scalar@b).tolist(),'new_first_order_sources_G':(linear@b).tolist(),'F_norm':float(np.linalg.norm(f)),'nullcone_checks':nullchecks}
 rows.append(out);print(out,flush=True)
(ROOT/'all-order-source-constraints-result.json').write_text(json.dumps({'contract':'Construct4 scalar derivative rows and4 first-order K source rows at savedgerms. Verify complete second-symbol left space numerically. No all-order nonlinear constraint propagation theorem.','results':rows},indent=2))
