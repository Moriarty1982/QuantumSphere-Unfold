from pathlib import Path
import json,numpy as np
src=Path(__file__).resolve().with_name('OP5_Counterflow_Full_Residual_Check.py')
exec(src.read_text(encoding='utf-8-sig').split('results=[]')[0])
g5=s.zeros(2).row_join(s.eye(2)).col_join(s.eye(2).row_join(s.zeros(2)))
outputs=[]
for pt in points:
 ev=lambda m:s.Matrix(m).subs(pt).evalf(30)
 fs=[ev(f) for f in fields];psi=s.Matrix.vstack(*fs)
 kin=[I*ev(ds[0])+sum((I*al[k]*ev(ds[k+1]) for k in range(3)),s.zeros(4,1)) for ds in derivs]
 V=sum((s.kronecker_product(ev(G)*s.sympify(spin[k]).subs(pt),al[k]) for k in range(3)),s.zeros(12))+s.kronecker_product(Y,beta)*hm.subs(pt).evalf(30)
 w=I*(s.Matrix.vstack(*kin)-V*psi)
 rate=lambda O:float(s.re(2*(psi.conjugate().T*O*w)[0]))
 J=[rate(s.kronecker_product(s.eye(3),K)) for K in [s.eye(4)]+al]
 ax=[rate(s.kronecker_product(s.eye(3),K*g5)) for K in [s.eye(4)]+al]
 cross=[rate(s.kronecker_product(S,K)) for K in [s.eye(4)]+al]
 species_spin=[[float(s.re(2*(fs[k].conjugate().T*K*g5*w[4*k:4*k+4,0])[0])) for K in [s.eye(4)]+al] for k in range(3)]
 E=np.eye(4);E[:,0]+=np.array(cross)/2
 g=E.T@np.diag([-1,1,1,1])@E
 out={'point':{str(k):str(val) for k,val in pt.items()},'total_current_rate_difference':J,'total_axial_rate_difference':ax,'cross_current_rate_difference':cross,'species_axial_rate_difference':species_spin,'instantaneous_coframe':E.tolist(),'metric':g.tolist(),'det_E':float(np.linalg.det(E)),'metric_eigenvalues':np.linalg.eigvalsh(g).tolist()}
 position=np.array([float(pt[x]),float(pt[y]),float(pt[z])]);axis=position/np.linalg.norm(position)
 rotation=2*np.outer(axis,axis)-np.eye(3);L=np.eye(4);L[1:,1:]=rotation
 partner=L@E@L.T;meanE=(E+partner)/2
 meanmetric=(g+partner.T@np.diag([-1,1,1,1])@partner)/2
 metricofmean=meanE.T@np.diag([-1,1,1,1])@meanE
 out['paired_ensemble']={'rotation':rotation.tolist(),'mean_axial_rate':((np.array(ax)+L@np.array(ax))/2).tolist(),'mean_current_rate':((np.array(J)+L@np.array(J))/2).tolist(),'mean_cross_rate':((np.array(cross)+L@np.array(cross))/2).tolist(),'mean_coframe_det':float(np.linalg.det(meanE)),'mean_metric_minus_metric_of_mean':(meanmetric-metricofmean).tolist()}
 assert abs(np.linalg.det(rotation)-1)<1e-12
 assert np.linalg.norm(out['paired_ensemble']['mean_axial_rate'])<1e-10
 assert np.linalg.norm(out['paired_ensemble']['mean_current_rate'][1:])>1
 assert abs(np.linalg.det(meanE)-1)<1e-12
 assert sum(np.linalg.eigvalsh(g)<0)==1
 outputs.append(out);print(json.dumps(out),flush=True)
Path(str(src.parent/'OP5_Constraint_Set_And_Ensemble_Check.json')).write_text(json.dumps(outputs,indent=2))
