"""Exact null-cone minor certificates and bounded tableau character check.

Run python all_order_criteria_symbol.py from repository root.
This is not nonlinear formal integrability or an existence proof.
"""
from pathlib import Path
import sympy as s,numpy as np,json,itertools,hashlib,time
W=Path(__file__).resolve().parent
R=next(p for p in [Path.cwd(),*W.parents] if (p/'analysis/OP5_Counterflow_Full_Residual_Check.py').exists())
source=R/'analysis/OP5_Counterflow_Full_Residual_Check.py'
ns={};exec(source.read_text(encoding='utf-8-sig').split('results=[]')[0],ns)
K=[s.eye(4)]+ns['al'];KK=[s.kronecker_product(s.eye(3),v) for v in K]
SS=s.kronecker_product(ns['S'],s.eye(4));QQ=[SS*v for v in KK]
def realify(C):return s.re(C).row_join(-s.im(C)).col_join(s.im(C).row_join(s.re(C)))
H=[realify(s.I*v) for v in KK];Hb=[realify(-s.I*KK[0])]+[realify(s.I*v) for v in KK[1:]]
for mu in range(4):
 assert H[mu]*Hb[mu]==(1 if mu==0 else -1)*s.eye(24)
 for nu in range(mu+1,4):assert H[mu]*Hb[nu]+H[nu]*Hb[mu]==s.zeros(24)
def select_columns(M,n):
 chosen=[];a=np.array(M,float)
 for col in range(a.shape[1]):
  if np.linalg.matrix_rank(a[:,chosen+[col]],tol=1e-10)>len(chosen):chosen.append(col)
  if len(chosen)==n:return chosen
 raise RuntimeError('insufficient numerical rank for exact candidate minor')
def certificate(psi):
 Ac=[]
 for Q in QQ:
  z=psi.conjugate().T*Q;Ac.append([s.re(v) for v in z]+[-s.im(v) for v in z])
 A=s.Matrix(Ac);w=SS*psi;ell=s.Matrix([[-s.im(v) for v in w]+[s.re(v) for v in w]])
 assert all(ell*H[mu]==A[mu:mu+1,:] for mu in range(4))
 cols=select_columns(A,4);minorA=A[:,cols].det();assert minorA!=0
 Kn=A*(Hb[0]+Hb[1]);assert Kn[0:1,:]+Kn[1:2,:]==s.zeros(1,24)
 rows=select_columns(Kn.T,3);colsK=select_columns(Kn[rows,:],3);minorK=Kn[rows,colsK].det();assert minorK!=0
 an=np.array(A,float);P=np.eye(24)-an.T@np.linalg.solve(an@an.T,an)
 J=np.column_stack([np.array(v,float)@P for v in H]);U,sv,Vh=np.linalg.svd(J,full_matrices=True);rank=int(sum(sv>sv[0]*1e-9));N=Vh[rank:].T
 flags=[]
 for seed in [None,11,23,47]:
  rotation=np.eye(4) if seed is None else np.linalg.qr(np.random.default_rng(seed).normal(size=(4,4)))[0]
  restricted=np.einsum('ma,mik->aik',rotation,N.reshape(4,24,-1));dims=[]
  for k in range(1,5):
   svf=np.linalg.svd(restricted[:k].reshape(24*k,-1),compute_uv=False);dims.append(int(sum(svf>svf[0]*1e-9)))
  flags.append({'seed':seed,'restriction_dims':dims,'characters':[int(v) for v in np.diff([0]+dims)]})
 pairs=list(itertools.combinations_with_replacement(range(4),2));A2=np.zeros((96,240))
 for pn,(mu,nu) in enumerate(pairs):
  A2[mu*24:(mu+1)*24,pn*24:(pn+1)*24]=J[:,nu*24:(nu+1)*24]
  if nu!=mu:A2[nu*24:(nu+1)*24,pn*24:(pn+1)*24]=J[:,mu*24:(mu+1)*24]
 sv2=np.linalg.svd(A2,compute_uv=False);rank2=int(sum(sv2>sv2[0]*1e-9))
 return {'A_minor_columns':cols,'A_minor_exact':str(minorA),'null_covector':[1,1,0,0],'K_minor_rows':rows,'K_minor_columns':colsK,'K_minor_exact':str(minorK),'A_rank_exact':4,'K_null_rank_exact':3,'ell_H_equals_A_exact':True,'symbol_rank_numerical':rank,'symbol_kernel_dimension':96-rank,'flags':flags,'first_prolongation_rank':rank2,'first_prolongation_kernel_dimension':240-rank2,'Cartan_bound_from_coordinate_flag':sum((i+1)*v for i,v in enumerate(flags[0]['characters']))}
rawpath=W/'fifth-window-result.json';raw=json.loads(rawpath.read_text(),parse_float=str);out=[];tic=time.time()
for row in raw['results']:
 val=row['coefficients_real_imag'][0];psi=s.Matrix([s.Rational(val[j])+s.I*s.Rational(val[j+12]) for j in range(12)])
 cert=certificate(psi);cert['point_index']=row['point_index'];out.append(cert)
 print(row['point_index'],'A4 Knull3 exact; chars',cert['flags'][0]['characters'],'g1',cert['symbol_kernel_dimension'],'g2',cert['first_prolongation_kernel_dimension'],flush=True)
example=certificate(s.Matrix([1]+[0]*11))
result={'contract':'Exact rational certificate for decimal-recorded field values and simple generic example; realified Clifford symbol. Numerical Cartan flag checks only, canonical projector onto kerA is symbol-equivalent to any projector with that image. No nonlinear integrability or regional existence claimed.','inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,rawpath,Path(__file__)]},'seconds':time.time()-tic,'Clifford_coefficients_exact':True,'states':out,'generic_example':example,'conditional_rank_formula':'d_p=C(p+2,3)+4C(p+1,3)-C(p,3); rankA_p=24C(p+2,3)-d_p','predicted_deficits':{str(p):p*(p+2)*(2*p-1)//3 for p in range(1,9)}}
(W/'all_order_criteria_symbol-result.json').write_text(json.dumps(result,indent=2))
