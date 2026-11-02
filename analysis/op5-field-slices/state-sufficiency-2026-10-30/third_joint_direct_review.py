"""Independent analytic product-rule check, no Torch or fitted evaluator import."""
from pathlib import Path
import json,itertools,numpy as np,sympy as s
W=Path(__file__).resolve().parent;R=Path(r'C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold')
ns={};exec((R/'analysis/OP5_Counterflow_Full_Residual_Check.py').read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
coords=[ns[v] for v in ('t','x','y','z')];pair=list(itertools.combinations_with_replacement(range(4),2));triple=list(itertools.combinations_with_replacement(range(4),3))
K=np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']]);Q=np.array([np.kron(np.array(ns['S'],complex),v) for v in K]);KK=np.array([np.kron(np.eye(3),v) for v in K]);Y=np.kron(np.array(ns['Y'],complex),np.array(ns['beta'],complex));S=np.kron(np.array(ns['S'],complex),np.eye(4))
Ab=[s.zeros(12)]+[s.kronecker_product(ns['G']*v,s.eye(4)) for v in ns['spin']];bg=s.Matrix([ns['hm']]+[v for m in Ab for v in m]);fbg=s.lambdify(coords,bg,'numpy',cse=True);fdb=s.lambdify(coords,bg.jacobian(coords),'numpy',cse=True);fddb=s.lambdify(coords,s.Matrix.hstack(*[bg.diff(coords[i],coords[j]) for i,j in pair]),'numpy',cse=True)
lower=json.loads((R/'analysis/op5-field-slices/OP5_Joint_Compatibility_Lower_Data.json').read_text())['results'];fit=json.loads((W/'joint-fit-result.json').read_text())['results'];new=json.loads((W/'third-joint-fit-result.json').read_text())['results'];pack=lambda v:np.r_[v.real.ravel(),v.imag.ravel()];rows=[]
for ip,row in enumerate(new):
 p=np.array(row['point']);psi=np.array([complex(*v) for v in lower[ip]['field_values_real_imag']]);jp=np.array(fit[ip]['first_jets_packed']);j=(jp[:48]+1j*jp[48:]).reshape(4,12);hp=np.array(row['symmetric_second_jets']).reshape(10,24);H=np.empty((4,4,12),complex)
 for n,(mu,nu) in enumerate(pair):H[mu,nu]=H[nu,mu]=hp[n,:12]+1j*hp[n,12:]
 tp=np.array(row['tests'][1]['third_jets']).reshape(20,24);T=np.empty((4,4,4,12),complex)
 for ids in itertools.product(range(4),repeat=3):n=triple.index(tuple(sorted(ids)));T[ids]=tp[n,:12]+1j*tp[n,12:]
 b=np.asarray(fbg(*p),complex).ravel();db=np.asarray(fdb(*p),complex);dds=np.asarray(fddb(*p),complex);ddb=np.empty((577,4,4),complex)
 for n,(mu,nu) in enumerate(pair):ddb[:,mu,nu]=ddb[:,nu,mu]=dds[:,n]
 h=b[0].real;dh=db[0].real;ddh=ddb[0].real;A=b[1:].reshape(4,12,12);dA=db[1:].reshape(4,12,12,4).transpose(3,0,1,2);ddA=ddb[1:].reshape(4,12,12,4,4).transpose(3,4,0,1,2)
 cov=j+1j*np.einsum('mij,j->mi',A,psi);dcov=np.empty((4,4,12),complex);ddcov=np.empty((4,4,4,12),complex)
 for nu in range(4):
  dcov[nu]=H[nu]+1j*np.einsum('mij,j->mi',dA[nu],psi)+1j*np.einsum('mij,j->mi',A,j[nu])
 for mu,nu in itertools.product(range(4),repeat=2):ddcov[mu,nu]=T[mu,nu]+1j*np.einsum('aij,j->ai',ddA[mu,nu],psi)+1j*np.einsum('aij,j->ai',dA[mu],j[nu])+1j*np.einsum('aij,j->ai',dA[nu],j[mu])+1j*np.einsum('aij,j->ai',A,H[mu,nu])
 E=np.einsum('i,aij,mj->am',psi.conj(),Q,cov).real;V=np.linalg.inv(E);dE=np.empty((4,4,4));ddE=np.empty((4,4,4,4))
 for mu in range(4):dE[mu]=(np.einsum('i,aij,mj->am',j[mu].conj(),Q,cov)+np.einsum('i,aij,mj->am',psi.conj(),Q,dcov[mu])).real
 for mu,nu in itertools.product(range(4),repeat=2):ddE[mu,nu]=(np.einsum('i,aij,mj->am',H[mu,nu].conj(),Q,cov)+np.einsum('i,aij,mj->am',j[mu].conj(),Q,dcov[nu])+np.einsum('i,aij,mj->am',j[nu].conj(),Q,dcov[mu])+np.einsum('i,aij,mj->am',psi.conj(),Q,ddcov[mu,nu])).real
 dV=np.array([-V@dE[mu]@V for mu in range(4)]);ddV=np.array([[V@dE[mu]@V@dE[nu]@V+V@dE[nu]@V@dE[mu]@V-V@ddE[mu,nu]@V for nu in range(4)] for mu in range(4)])
 kin=lambda v,c:1j*np.einsum('ma,aij,mj->i',v,KK,c)
 F=kin(V,cov)-h*Y@psi;dF=np.array([kin(dV[mu],cov)+kin(V,dcov[mu])-dh[mu]*Y@psi-h*Y@j[mu] for mu in range(4)]);ddF=np.array([kin(ddV[mu,nu],cov)+kin(dV[mu],dcov[nu])+kin(dV[nu],dcov[mu])+kin(V,ddcov[mu,nu])-ddh[mu,nu]*Y@psi-dh[mu]*Y@j[nu]-dh[nu]*Y@j[mu]-h*Y@H[mu,nu] for mu,nu in pair])
 ell=lambda ps:np.r_[-(S@ps).imag,(S@ps).real]
 qscalar=np.vdot(psi,np.kron(np.diag([1,-1,0]),np.array(ns['beta'],complex))@psi).real
 gate=json.loads((W/'third-joint-gate-review-result.json').read_text())['results'][ip];gmat=np.array(gate['ddg']);identity=[]
 for pn,(mu,nu) in enumerate(pair):identity.append(ell(psi)@pack(ddF[pn])+ell(j[mu])@pack(dF[nu])+ell(j[nu])@pack(dF[mu])+ell(H[mu,nu])@pack(F)-gmat[mu,nu])
 out={'point_index':ip,'F_norm':float(np.linalg.norm(F)),'dF_norm':float(np.linalg.norm(dF)),'ddF_symmetric_packed_norm':float(np.linalg.norm(ddF)),'scalar_second_identity_error':float(np.linalg.norm(identity)),'H_norm':float(np.linalg.norm(hp)),'T_norm':float(np.linalg.norm(tp))};rows.append(out);print(out,flush=True)
(W/'third-joint-direct-review-result.json').write_text(json.dumps({'contract':'Independent direct product-rule/inverse-matrix derivative check, original exact background derivatives; no Torch and no optimizer/evaluator import.','results':rows},indent=2))
