from pathlib import Path
import numpy as np,json
ns={};exec(Path('OP5_Temporal_Compatibility_Identity_Check.py').read_text().split("for p in ns['points']:")[0],ns)
T=ns['T'];compute=ns['compute'];old=ns['old'];out=[]
for p in ns['ns']['points']:
 psi=compute(T.tensor(p[None]))[3].detach().numpy()[0];hf=1e-6;jets=np.array([(compute(T.tensor((p+hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0]-compute(T.tensor((p-hf*np.eye(4)[mu])[None]))[3].detach().numpy()[0])/(2*hf) for mu in range(4)])
 gg,hh,spin=old['back'](*p);gauge=[np.zeros((12,12),complex)]+[np.kron(np.asarray(gg)*np.asarray(spin).ravel()[mu-1],np.eye(4)) for mu in range(1,4)];cov=jets+np.array([1j*gauge[mu]@psi for mu in range(4)])
 Q=old['QQ'];E0=np.array([np.vdot(psi,q@cov[0]).real for q in Q]);mass=float(hh)*old['YY']@psi
 pack=lambda z:np.r_[z.real.ravel(),z.imag.ravel()]
 v0=pack(jets[1:])
 def evaluate(v):
  js=(v[:36]+1j*v[36:]).reshape(3,12);ds=js+np.array([1j*gauge[mu]@psi for mu in range(1,4)])
  E=np.column_stack([E0]+[np.array([np.vdot(psi,q@d).real for q in Q]) for d in ds]);inv=np.linalg.inv(E);Ps=[sum(inv[mu,a]*old['KK'][a] for a in range(4)) for mu in range(4)];b=sum((1j*Ps[mu]@ds[mu-1] for mu in range(1,4)),np.zeros(12,complex))-mass
  dt=np.linalg.solve(1j*Ps[0],-b);C=np.array([np.vdot(psi,q@dt).real for q in Q])-E0
  return C,np.vstack([dt,js]),E
 h=1e-5;J=np.column_stack([(evaluate(v0+h*np.eye(72)[k])[0]-evaluate(v0-h*np.eye(72)[k])[0])/(2*h) for k in range(72)]);u,sv,vh=np.linalg.svd(J,full_matrices=False);rank=int(sum(sv>sv[0]*1e-7))
 reduced=u[:,:3].T@J;selected=[];remaining=reduced.copy()
 for k in range(3):
  idx=int(np.argmax(np.linalg.norm(remaining,axis=0)));selected.append(idx);direction=remaining[:,idx]/np.linalg.norm(remaining[:,idx]);remaining-=direction[:,None]*(direction@remaining)[None,:]
 v=v0.copy();history=[]
 for it in range(12):
  C,js,E=evaluate(v);r=u[:,:3].T@C;history.append(float(np.linalg.norm(C)))
  if np.linalg.norm(C)<1e-10:break
  jac=np.column_stack([u[:,:3].T@(evaluate(v+h*np.eye(72)[k])[0]-evaluate(v-h*np.eye(72)[k])[0])/(2*h) for k in selected]);step=np.linalg.solve(jac,-r)
  for fac in [1,.5,.25,.125,.0625]:
   trial=v.copy();trial[selected]+=fac*step
   if np.linalg.norm(evaluate(trial)[0])<np.linalg.norm(C):v=trial;break
  else:break
 C,js,E=evaluate(v);full=old['residual'](p,psi,js);metric=E.T@np.diag([-1,1,1,1])@E
 out.append({'field_values_real_imag':[[float(z.real),float(z.imag)] for z in psi],'point':p.tolist(),'constraint_J_singular_values':sv.tolist(),'rank':rank,'selected_real_spatial_parameters':selected,'history':history,'final_constraint_norm':float(np.linalg.norm(C)),'full_equation_residual':float(np.linalg.norm(full)),'spatial_correction_norm':float(np.linalg.norm(v-v0)),'detE':float(np.linalg.det(E)),'g_inverse00':float(np.linalg.inv(metric)[0,0]),'all_jets_real_imag':[[float(z.real),float(z.imag)] for z in js.ravel()]})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
