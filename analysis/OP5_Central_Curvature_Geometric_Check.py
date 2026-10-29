from pathlib import Path
import sympy as s,numpy as np,json
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text().split('results=[]')[0])
psi=s.Matrix.vstack(*fields);ks=[s.eye(4)]+al
Ps=[s.eye(4)/2]+[al[j]-v[j]*s.eye(4)/2 for j in range(3)]
nvec=s.Matrix([c,-d,0]);mvec=s.Matrix([d,c,0]);zz=s.Matrix([0,0,1])
basis=[mvec*mvec.T,nvec*nvec.T,zz*zz.T,(nvec*zz.T+zz*nvec.T)/s.sqrt(2),I*(nvec*zz.T-zz*nvec.T)/s.sqrt(2)]
M=s.Matrix.hstack(*[-s.kronecker_product(B,Ps[mu])*psi for mu in range(4) for B in basis])
# The canonical transport change cancels exactly on this homogeneous seed.
V=sum((s.kronecker_product(G*spin[j],al[j]) for j in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm
res=s.Matrix.vstack(*[sum((I*ks[mu]*ds[mu] for mu in range(4)),s.zeros(4,1)) for ds in derivs])-V*psi
variables=(t,x,y,z)
print('Preparing analytic derivatives',flush=True)
f=s.lambdify(variables,[M,res]+[e.diff(q) for q in variables for e in [M,res]],modules='numpy',cse=True)
def realmat(a):return np.vstack([a.real,a.imag])
def realvec(a):
 a=np.asarray(a).reshape(-1);return np.r_[a.real,a.imag]
out=[]
for pos in [(1.,.6,0.,0.),(1.,.4,.2,.2),(.9,.3,.2,.1),(1.1,.2,-.3,-.15)]:
 vals=f(*pos);m=realmat(vals[0]);r=realvec(vals[1])
 A=np.zeros((120,100));rhs=np.zeros(120)
 A[:24,:20]=m;rhs[:24]=-r
 for k in range(4):
  rows=slice(24*(k+1),24*(k+2))
  A[rows,:20]=realmat(vals[2+2*k]);A[rows,20+20*k:40+20*k]=m
  rhs[rows]=-realvec(vals[3+2*k])
 T=np.zeros((6,100))
 ij=[(i,j) for i in range(4) for j in range(i+1,4)]
 for row,(i,j) in enumerate(ij):
  # central c_mu=tr(C_mu)/3: derivative coefficients include basis derivative,
  # whose trace vanishes identically (basis traces 1,1,1,0,0 constant).
  T[row,20+20*i+5*j:20+20*i+5*j+3]=1/3
  T[row,20+20*j+5*i:20+20*j+5*i+3]=-1/3
 _,_,vt=np.linalg.svd(T,full_matrices=True);Z=vt[6:].T
 cases={}
 for name,L in [('free',np.eye(100)),('closed_central',Z)]:
  mat=A@L
  co,_,rank,sv=np.linalg.lstsq(mat,rhs,rcond=1e-10)
  sol=L@co;rem=A@sol-rhs
  cases[name]={'rank':int(rank),'residual_norm':float(np.linalg.norm(rem)),'trace_curl_norm':float(np.linalg.norm(T@sol)),'singular_values':sv.tolist()}
  assert np.linalg.norm(mat.T@rem)<1e-7
 out.append({'point':pos,'cases':cases})
 ua,sa,vha=np.linalg.svd(A,full_matrices=True)
 ra=int(np.sum(sa>sa[0]*1e-10));NA=vha[ra:].T
 sol0=np.linalg.lstsq(A,rhs,rcond=1e-10)[0]
 TN=T@NA
 correction=np.linalg.lstsq(TN,-T@sol0,rcond=1e-10)[0]
 mincurl=T@(sol0+NA@correction)
 assert np.linalg.norm(A@(sol0+NA@correction)-rhs)<1e-9
 uc,sc,vhc=np.linalg.svd(TN,full_matrices=True)
 rc=int(np.sum(sc>1e-10))
 out[-1]['curvature_freedom']={'rank':rc,'pairs':ij,'singular_values':sc.tolist(),'minimal_curl_vector':mincurl.tolist(),'minimal_curl_norm':float(np.linalg.norm(mincurl)),'left_constraints':uc[:,rc:].T.tolist(),'left_constraint_values':(uc[:,rc:].T@T@sol0).tolist()}
 tv,xv,yv,zv=pos
 vel=np.array([xv,yv,zv])/tv
 polar=np.array([-xv*zv/(xv*xv+yv*yv),-yv*zv/(xv*xv+yv*yv),1.])
 V0=np.r_[1.,-vel];W0=np.r_[0.,polar]
 biv=np.array([V0[i]*W0[j]-V0[j]*W0[i] for i,j in ij])
 left=uc[:,rc:].T
 assert left.shape[0]==1
 defect=np.linalg.norm(biv-left.T@(left@biv))/np.linalg.norm(biv)
 out[-1]['geometric_test']={'bivector':biv.tolist(),'relative_projection_error':float(defect),'required_contraction':float(biv@T@sol0),'polar_vector':polar.tolist()}
 print(json.dumps({'point':pos,'cases':{k:{a:b for a,b in v.items() if a!='singular_values'} for k,v in cases.items()}}),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
