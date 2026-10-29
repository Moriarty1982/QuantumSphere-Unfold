from pathlib import Path
import json,numpy as np
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
arr=lambda m:np.array(m.tolist(),complex).reshape(-1)
pack=lambda w:np.r_[w.real,w.imag]
out=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 uu=arr(ev(U)); ww=arr(ev(W))
 K=[s.eye(4)]+al
 ju=np.array([np.vdot(uu,arr(k*ev(U))).real for k in K])
 avec=float(Delta.subs(pt))*ju/2
 sv=np.array([0]+[float(s.sympify(k).subs(pt)) for k in spin])
 assert abs(avec@sv)<1e-12
 q0=float(th.diff(t).subs(pt));h=float(hm.subs(pt));kap=float((d*p-c*q).subs(pt))
 als=sum((s.sympify(spin[j]).subs(pt)*al[j] for j in range(3)),s.zeros(4))
 b0=q0*uu-h*arr(beta*ev(U))-1j*kap*arr(als*ev(W))
 mat=np.column_stack([pack(1j*arr(k*ev(U))) for k in K])
 coef,_,rank,sing=np.linalg.lstsq(mat,-pack(b0),rcond=1e-12)
 residual=pack(b0)+mat@coef
 assert np.linalg.norm(mat.T@residual)<1e-10
 # Instead of changing theta and the time slicing, allow spatial relative
 # phase jets at the original field values and original E=I.
 psi=s.Matrix.vstack(*[ev(f) for f in fields])
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[j]).subs(pt),al[j]) for j in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 old=s.Matrix.vstack(*[sum((I*K[mu]*ev(ds[mu]) for mu in range(4)),s.zeros(4,1)) for ds in derivs])-V*psi
 cv=float(c.subs(pt));dv=float(d.subs(pt))
 oldvec=arr(old);newvec=oldvec.copy()
 phasevector=sum((coef[mu]*arr(K[mu]*ev(U)) for mu in range(4)),np.zeros(4,complex))
 newvec[:4]+=dv*phasevector;newvec[4:8]-=cv*phasevector
 transverse=cv*newvec[4:8]-dv*newvec[:4]
 assert np.linalg.norm(transverse)<1e-10
 assert np.linalg.norm(cv*newvec[:4]+dv*newvec[4:8]-(cv*oldvec[:4]+dv*oldvec[4:8]))<1e-10
 assert np.linalg.norm(newvec[8:]-oldvec[8:])<1e-12
 # Direct cross-coframe variation from the changed derivative jets.
 psin=arr(psi)
 for mu in range(4):
  dpsi=np.r_[-1j*dv*uu*coef[mu],1j*cv*uu*coef[mu],np.zeros(4,complex)]
  for kk in K:
   Q=np.array(s.kronecker_product(S,kk).tolist(),complex)
   assert abs(np.vdot(psin,Q@dpsi).real)<1e-10
 out.append({'point':{str(k):str(vv) for k,vv in pt.items()},'rank':int(rank),'singular_values':sing.tolist(),'relaxed_phase_covector':coef.tolist(),'residual_norm2':float(residual@residual),'original_norm2':float(np.vdot(b0,b0).real),'phase_covector_minkowski_norm':float(-coef[0]**2+coef[1:]@coef[1:]),'a_dot_connection_covector':float(avec@sv)})
 out[-1]['full_residual_norm2_before']=float(np.vdot(oldvec,oldvec).real)
 out[-1]['full_residual_norm2_after_spatial_phase']=float(np.vdot(newvec,newvec).real)
 out[-1]['remaining_species_residual_norms']=[float(np.linalg.norm(newvec[4*j:4*j+4])) for j in range(3)]
 out[-1]['transverse_residual_norm2_after']=float(np.vdot(transverse,transverse).real)
 print(json.dumps(out[-1]))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
