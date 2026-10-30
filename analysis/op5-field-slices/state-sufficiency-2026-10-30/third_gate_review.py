"""Independent scalar attribution of frozen2jet third-order failure. python third_gate_review.py"""
from pathlib import Path
import json,numpy as np,sympy as s,hashlib,time
W=Path(__file__).resolve().parent
R=Path(r'C:/Users/marcb/OneDrive/Dokumente/GitHub/QuantumSphere-Unfold')
source=R/'analysis/OP5_Counterflow_Full_Residual_Check.py'
ns={};exec(source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
coords=[ns[v] for v in ('t','x','y','z')]
hf=s.lambdify(coords,ns['hm'],'numpy');dhf=s.lambdify(coords,[s.diff(ns['hm'],v) for v in coords],'numpy');hhf=s.lambdify(coords,s.hessian(ns['hm'],coords),'numpy')
K=np.array([np.eye(4)]+[np.array(v,complex) for v in ns['al']]);QQ=np.array([np.kron(np.array(ns['S'],complex),v) for v in K]);KK=np.array([np.kron(np.eye(3),v) for v in K]);YY=np.kron(np.array(ns['Y'],complex),np.array(ns['beta'],complex))
back=s.lambdify(coords,(ns['G'],ns['hm'],s.Matrix(ns['spin'])),'numpy',cse=True)
Z=np.kron(np.diag([1,-1,0]),np.array(ns['beta'],complex));S=np.kron(np.array(ns['S'],complex),np.eye(4))
lower=json.loads((R/'analysis/op5-field-slices/OP5_Joint_Compatibility_Lower_Data.json').read_text())['results'];fit=json.loads((W/'joint-fit-result.json').read_text())['results'];third=json.loads((W/'third-check-result.json').read_text())['results']
pairs=[(i,j) for i in range(4) for j in range(i,4)];picker=np.empty((4,4),int)
for n,(i,j) in enumerate(pairs):picker[i,j]=picker[j,i]=n
pack=lambda v:np.r_[v.real.ravel(),v.imag.ravel()]
def unpack(v):return (v[:48]+1j*v[48:]).reshape(4,12)
def residual(p,psi,j):
 gg,hh,spin=back(*p);ss=np.asarray(spin).ravel();cov=j.copy()
 for mu in range(1,4):cov[mu]+=1j*np.kron(gg*ss[mu-1],np.eye(4))@psi
 ee=np.einsum('i,aij,mj->am',psi.conj(),QQ,cov).real
 f=1j*np.einsum('ma,aij,mj->i',np.linalg.inv(ee),KK,cov)-float(hh)*YY@psi
 return pack(f)
rows=[]
for ip,r in enumerate(fit):
 p=np.array(r['point']);psi=np.array([complex(*v) for v in lower[ip]['field_values_real_imag']]);jp=np.array(r['first_jets_packed']);j=unpack(jp);hp=np.array(r['symmetric_second_jets']).reshape(10,24);H=(hp[:,:12]+1j*hp[:,12:])[picker]
 q=np.vdot(psi,Z@psi).real;h=float(hf(*p));dh=np.array(dhf(*p));hh=np.array(hhf(*p));dq=np.array([2*np.vdot(psi,Z@v).real for v in j]);ddq=np.array([[2*np.real(np.vdot(j[mu],Z@j[nu])+np.vdot(psi,Z@H[mu,nu])) for nu in range(4)] for mu in range(4)]);ddg=-.5*(hh*q+np.outer(dh,dq)+np.outer(dq,dh)+h*ddq);gpack=np.array([ddg[mu,nu] for mu,nu in pairs])
 w=S@psi;ell=np.r_[-w.imag,w.real];bound=float(np.linalg.norm(gpack)/np.linalg.norm(ell))
 eps=1e-5;eye=np.eye(96);J=np.column_stack([(residual(p,psi,unpack(jp+eps*v))-residual(p,psi,unpack(jp-eps*v)))/(2*eps) for v in eye]);left_error=float(np.linalg.norm(ell@J))
 controls=[]
 def direct(dx):return residual(p+dx,psi+np.einsum('m,mi->i',dx,j)+.5*np.einsum('m,n,mni->i',dx,dx,H),j+np.einsum('n,mni->mi',dx,H))
 f0=direct(np.zeros(4))
 for eps in (3e-4,1e-4):
  contracted=[]
  for mu,nu in pairs:
   u=np.eye(4)[mu]*eps;v=np.eye(4)[nu]*eps
   b=(direct(u)-2*f0+direct(-u))/eps**2 if mu==nu else (direct(u+v)-direct(u-v)-direct(-u+v)+direct(-u-v))/(4*eps**2)
   contracted.append(ell@b)
  controls.append({'step':eps,'norm_ell_b_minus_ddg':float(np.linalg.norm(np.array(contracted)-gpack))})
 out={'point_index':ip,'ddg':ddg.tolist(),'ddg_packed_norm':float(np.linalg.norm(gpack)),'ell_norm':float(np.linalg.norm(ell)),'necessary_ddF_lower_bound':bound,'finite_difference_ell_J_norm':left_error,'source_contraction_controls':controls}
 if ip<len(third):
  tr=third[ip];sym=tr['tests'][1]['residual_norm'];unsym=tr['unrestricted_residual'];out.update({'observed_unrestricted_residual':unsym,'unrestricted_minus_scalar_bound':unsym-bound,'observed_symmetric_residual':sym,'scalar_bound_squared_fraction_of_symmetric':bound**2/sym**2})
 rows.append(out);print(json.dumps(out),flush=True)
(W/'third-gate-review-result.json').write_text(json.dumps({'contract':'Independent scalar gate and finite-difference left/source attribution; no optimization or full thirdjet SVD rerun.','inputs_sha256':{str(v):hashlib.sha256(v.read_bytes()).hexdigest() for v in [source,W/'joint-fit-result.json',W/'third-check-result.json',Path(__file__)]},'results':rows},indent=2))
