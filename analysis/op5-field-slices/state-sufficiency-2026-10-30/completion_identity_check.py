"""Tableau/prolongation of F,G,dg, not an analytic existence certificate."""
from pathlib import Path
import importlib.util,json,numpy as np,torch as T,itertools,time
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('complete_model',ROOT/'recursive_calibrator.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
model=m.TaylorModel(3);data=json.loads((ROOT/'fifth-window-result.json').read_text());rows=[];tic=time.time()
def realmat(z):return np.block([[z.real,-z.imag],[z.imag,z.real]])
H=np.array([realmat(1j*k) for k in model.K.numpy()]);Hb=H.copy();Hb[0]*=-1;Hb=T.tensor(Hb)
Z=T.tensor(np.kron(np.diag([1,-1,0]),np.array(model.ns['beta'],complex)));pairs=list(itertools.combinations_with_replacement(range(4),2))
for row in data['results']:
 pos=np.array(row['point']);pp=np.array(row['coefficients_real_imag']);c=pp[:,:12]+1j*pp[:,12:];psi=c[0];j=c[1:5]
 bg=model.background(pos);pt=T.tensor(pos)
 def back(q):
  dx=q[120:]-pt
  terms=[]
  for alpha in model.idx:
   term=T.ones(())
   for mu,n in enumerate(alpha):
    for _ in range(n):term=term*dx[mu]
   terms.append(term)
  mon=T.stack(terms)
  return mon.to(T.complex128)@bg
 def pieces(q):
  ps=m.unpack(q[:24])[0];js=m.unpack(q[24:120]);b=back(q);cov=js+1j*T.einsum('mij,j->mi',b[1:].reshape(4,12,12),ps)
  E=T.einsum('i,aij,mj->am',ps.conj(),model.Q,cov).real;V=T.linalg.inv(E)
  f=1j*T.einsum('ma,aij,mj->i',V.to(T.complex128),model.K,cov)-b[0].real*(model.Y@ps)
  return ps,js,b,V,T.cat((f.real,f.imag))
 def F(q):return pieces(q)[4]
 DF=T.func.jacrev(F)
 def g(q):
  ps,js,b,V,f=pieces(q);return 4-.5*b[0].real*T.vdot(ps,Z@ps).real
 Dg=T.func.jacrev(g)
 def R(q):
  ps,js,b,V,f=pieces(q);D=DF(q)
  aa=T.einsum('i,aij->aj',ps.conj(),model.Q);A=T.cat((aa.real,-aa.imag),dim=1)
  K=T.einsum('ai,mij->maj',A,T.einsum('ma,aij->mij',V,Hb))
  bmu=T.stack([D[:,120+mu]+D[:,:24]@T.cat((js[mu].real,js[mu].imag)) for mu in range(4)])
  G=T.einsum('mai,mi->a',K,bmu);gg=Dg(q)
  dg=T.stack([gg[120+mu]+gg[:24]@T.cat((js[mu].real,js[mu].imag)) for mu in range(4)])
  return T.cat((f,G,dg))
 q=T.tensor(np.r_[m.pack(psi),m.pack(j),pos]);DR=T.func.jacrev(R)(q).detach().numpy();DFF=DF(q).detach().numpy();JF=DFF[:,24:120]
 AF=np.zeros((96,240));AC=np.zeros((128,240))
 for pn,(mu,nu) in enumerate(pairs):
  AF[mu*24:(mu+1)*24,pn*24:(pn+1)*24]=JF[:,nu*24:(nu+1)*24]
  AC[mu*32:(mu+1)*32,pn*24:(pn+1)*24]=DR[:,24+nu*24:24+(nu+1)*24]
  if mu!=nu:
   AF[nu*24:(nu+1)*24,pn*24:(pn+1)*24]=JF[:,mu*24:(mu+1)*24]
   AC[nu*32:(nu+1)*32,pn*24:(pn+1)*24]=DR[:,24+mu*24:24+(mu+1)*24]
 bf=np.concatenate([DFF[:,120+mu]+DFF[:,:24]@m.pack(j[mu]) for mu in range(4)])
 z=np.linalg.lstsq(AF,-bf,rcond=1e-9)[0];hp=z.reshape(10,24);hh=hp[:,:12]+1j*hp[:,12:];tangent=np.zeros((124,4));tangent[:24]=np.array([m.pack(v) for v in j]).T;tangent[120:]=np.eye(4)
 for mu in range(4):
  for nu in range(4):tangent[24+nu*24:24+(nu+1)*24,mu]=m.pack(hh[pairs.index(tuple(sorted((mu,nu))))])
 def Kfun(q):
  ps,js,b,V,f=pieces(q);aa=T.einsum('i,aij->aj',ps.conj(),model.Q);A=T.cat((aa.real,-aa.imag),dim=1)
  return T.einsum('ai,mij->maj',A,T.einsum('ma,aij->mij',V,Hb))
 K0=Kfun(q).detach().numpy();DK=T.func.jacrev(Kfun)(q).detach().numpy();V=pieces(q)[3].detach().numpy();metric=V@np.diag([1,-1,-1,-1])@V.T
 S=np.kron(np.array(model.ns['S'],complex),np.eye(4));ell=np.r_[-(S@psi).imag,(S@psi).real];dell=np.array([np.r_[-(S@v).imag,(S@v).real] for v in j]);M=[]
 for nu in range(4):M.append(sum((V[mu,a]*(DK[nu,a]@tangent[:,mu]) for mu in range(4) for a in range(4)),np.zeros(24))-2*sum((metric[mu,nu]*dell[mu] for mu in range(4)),np.zeros(24)))
 identities=[]
 for mu in range(4):
  rr=np.zeros((4,32));rr[mu,:24]=ell;identities.append(rr.ravel())
 for a in range(4):
  rr=np.zeros((4,32))
  for mu in range(4):rr[mu,:24]=K0[mu,a]
  identities.append(rr.ravel())
 for mu,nu in itertools.combinations(range(4),2):
  rr=np.zeros((4,32));rr[mu,28+nu]=1;rr[nu,28+mu]=-1;identities.append(rr.ravel())
 last=np.zeros((4,32))
 for mu in range(4):last[mu,:24]=-M[mu];last[mu,24:28]=V[mu];last[mu,28:]=-metric[mu]
 identities.append(last.ravel());L=np.array(identities);u,sv,vh=np.linalg.svd(AC,full_matrices=False);rank=int(sum(sv>sv[0]*1e-9));left=u[:,rank:];ul,sl,vl=np.linalg.svd(L,full_matrices=False);lr=int(sum(sl>sl[0]*1e-9));P=vl[:lr].T@vl[:lr]
 bc=np.concatenate([DR[:,120+mu]+DR[:,:24]@m.pack(j[mu]) for mu in range(4)])
 rowout={'point_index':row['point_index'],'Rnorm':float(np.linalg.norm(R(q).detach().numpy())),'reference_dF_norm':float(np.linalg.norm(AF@z+bf)),'completed_symbol_rank':rank,'identity_rank':lr,'annihilation_norm':float(np.linalg.norm(L@AC)),'projector_difference':float(np.linalg.norm(P-left@left.T)),'source_identity_norm':float(np.linalg.norm(L@bc)),'fifteenth_row_norm':float(np.linalg.norm(last))}
 rows.append(rowout);print(rowout,flush=True)
 (ROOT/'completion-identity-result.json').write_text(json.dumps({'contract':'Explicit15 leftidentities for first completedprojection, including reference-secondjet lifted scalar/linear symbolrelation. Numerical check of conditional algebraic proof, not allhigher projections.','results':rows},indent=2))
