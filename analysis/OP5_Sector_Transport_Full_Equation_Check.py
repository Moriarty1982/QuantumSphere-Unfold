from pathlib import Path
import json,numpy as np
src=Path(__file__).with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
arr=lambda m:np.array(m.tolist(),complex)
out=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 psi=arr(s.Matrix.vstack(*[ev(f) for f in fields])).reshape(-1)
 ds=[arr(s.Matrix.vstack(*[ev(dfs[mu]) for dfs in derivs])).reshape(-1) for mu in range(4)]
 km=[np.eye(4)]+[arr(a) for a in al]
 tm=float(pt[t]);vv=np.array([float(vj.subs(pt)) for vj in v])
 E=np.eye(4);E[0,0]=2;E[1:,0]=vv
 ei=np.linalg.inv(E)
 Ps=[sum((ei[mu,a]*km[a] for a in range(4)),np.zeros((4,4),complex)) for mu in range(4)]
 assert abs(np.linalg.det(E)-2)<1e-12
 q0=float(th.diff(t).subs(pt));Am=[-q0*arr(Y)]+[float(s.sympify(spin[j]).subs(pt))*arr(ev(G)) for j in range(3)]
 mass=float(hm.subs(pt))*np.kron(arr(Y),arr(beta))@psi
 res=sum((1j*np.kron(np.eye(3),Ps[mu])@ds[mu]-np.kron(Am[mu],Ps[mu])@psi for mu in range(4)),np.zeros(12,complex))-mass
 # Independent LC completion. Standard spin connection preserves vector bilinear.
 # omega^i_0 = H Ei, H=-1/(2t).
 gam=[arr(beta)]+[arr(beta)*0+arr(beta*a) for a in al]
 H=-1/(2*tm)
 Gamma=[]
 for mu in range(4):
  Gamma.append(sum((H*E[i+1,mu]/2*arr(al[i]) for i in range(3)),np.zeros((4,4),complex)))
 contracted=sum((Ps[mu]@Gamma[mu] for mu in range(4)),np.zeros((4,4),complex))
 assert np.max(abs(contracted-3*H/2*np.eye(4)))<1e-12
 lcres=res+1j*np.kron(np.eye(3),contracted)@psi
 deltaE=np.zeros((4,4))
 for mu in range(4):
  dpsi=np.kron(np.eye(3),Gamma[mu])@psi
  for a in range(4):
   deltaE[a,mu]=np.vdot(psi,np.kron(arr(S),km[a])@dpsi).real
 expected=np.zeros((4,4)); expected[1:,:]=-E[1:,:]/2
 expected[0,:]=-np.array([float(pt[x]),float(pt[y]),float(pt[z])])@E[1:,:]/(2*tm)
 assert np.max(abs(deltaE-expected))<1e-11
 item={'point':{str(k):str(val) for k,val in pt.items()},'E':E.tolist(),'zero_spin_connection_full_residual_norm2':float(np.vdot(res,res).real),'zero_spin_ABC_norms':[float(np.linalg.norm(res[4*j:4*j+4])) for j in range(3)],'LC_full_residual_norm2':float(np.vdot(lcres,lcres).real),'LC_ABC_norms':[float(np.linalg.norm(lcres[4*j:4*j+4])) for j in range(3)],'LC_dictionary_defect':deltaE.tolist(),'LC_dictionary_defect_frobenius':float(np.linalg.norm(deltaE))}
 out.append(item);print(json.dumps(item))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
