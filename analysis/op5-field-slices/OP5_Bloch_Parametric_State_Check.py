from pathlib import Path
import json,numpy as np,sympy as s
rows=json.loads(Path('OP5_Parametric_Jet_Family_Check.json').read_text());out=[]
for row in rows:
 psi=np.array([complex(*v) for v in row['field_values_real_imag']]);A=psi[:4];B=psi[4:8];N=np.vdot(A,A).real+np.vdot(B,B).real;z=np.vdot(A,B);rho=np.array([[np.vdot(A,A),z.conjugate()],[z,np.vdot(B,B)]])/N;r=np.array([2*z.real,2*z.imag,np.vdot(A,A).real-np.vdot(B,B).real])/N
 err=abs((1-r@r)-4*np.linalg.det(rho).real);assert err<1e-12
 out.append({'point':row['point'],'bloch_vector':r.tolist(),'bloch_radius':float(np.linalg.norm(r)),'purity':float(np.trace(rho@rho).real),'identity_error':float(err),'rho_eigenvalues':np.linalg.eigvalsh(rho).tolist()})
theta=s.symbols('theta',real=True);c=s.cos(theta);d=s.sin(theta);beta=s.diag(1,1,-1,-1);e1=s.eye(4)[:,0];e3=s.eye(4)[:,2]
def gram(a,b):return s.Matrix([[s.conjugate(a).dot(a),s.conjugate(b).dot(a)],[s.conjugate(a).dot(b),s.conjugate(b).dot(b)]])
assert gram(c*e1,d*e1)==gram(c*e3,d*e3)
v1=s.simplify((c*e1).T*beta*(c*e1)-(d*e1).T*beta*(d*e1));v2=s.simplify((c*e3).T*beta*(c*e3)-(d*e3).T*beta*(d*e3));assert s.simplify(v1+v2)==s.zeros(1)
Path(__file__).with_suffix('.json').write_text(json.dumps({'actual_states':out,'same_bloch_different_beta_counterexample':{'first':str(v1),'second':str(v2)},'scope':'Internal Gram/Bloch representation. No fundamental tensor-product quantum interpretation or PDE closure proved.'},indent=2));print(out);print(v1,v2)
