from pathlib import Path
import torch as T,numpy as np,json,sympy as s,time,itertools
T.set_num_threads(1);T.set_default_dtype(T.float64)
exec(Path('OP5_State_Second_Jet_Check.py').read_text().split('data=json.loads')[0])
center=np.array([1.,.6,0.,0.]); radius=.01
pt=dict(zip((t,x,y,z),center)); seed=np.concatenate([np.array(f.subs(pt).evalf(),complex).ravel() for f in fields]);data=json.loads(Path('OP5_State_Constraint_Fit.json').read_text()); jets=np.array([complex(*v) for v in data['results'][0]['attempts'][1]['all_jets']]).reshape(4,12)
# Two oscillatory modes with independent affine amplitudes.
k=T.tensor([[1.,1.,0.,0.],[-1.,0.,1.,1.]])
raw=np.array(json.loads(Path('OP5_Multimode_Causal_Field_Check.json').read_text())['coefficients_real_imag']);c0=raw[...,0]+1j*raw[...,1]
params=T.nn.Parameter(T.view_as_real(T.tensor(c0)).clone())
KT=T.tensor(KK); QT=T.tensor(QQ); MT=T.tensor(YY); Z=T.tensor(np.kron(np.diag([1,-1,0]),np.array(beta,complex)));Gtemplate=lambda p,q:T.stack([T.stack([p*0,p*0,p],-1),T.stack([p*0,p*0,q],-1),T.stack([p,q,p*0],-1)],-2)
def compute(pos):
 delta=(pos-T.tensor(center))/radius; basis=T.cat([T.ones((len(pos),1)),delta],1); coeff=T.view_as_complex(params.contiguous());phase=T.exp(1j*((pos-T.tensor(center))@k.T));amp=T.einsum('nf,mfj->nmj',basis.to(T.complex128),coeff)
 chi=T.einsum('nm,nmj->nj',phase,amp)
 dc=T.stack([T.einsum('nm,nmj->nj',phase,1j*k[:,mu][None,:,None]*amp+coeff[:,mu+1][None]/radius) for mu in range(4)],1)
 tt=pos[:,0];xyz=pos[:,1:];rho=T.sqrt((xyz[:,:2]**2).sum(1));v2=(xyz**2).sum(1)/tt**2;gam=(1-v2).rsqrt();dd=T.sqrt(1-tt**2/4);h=gam/dd
 logdh=T.cat([(-((xyz**2).sum(1))/(tt**3*(1-v2))+tt/(4*(1-tt**2/4)))[:,None],xyz/(tt[:,None]**2*(1-v2[:,None]))],1)
 q=T.einsum('ni,ij,nj->n',chi.conj(),Z,chi).real; dq=2*T.einsum('ni,ij,nmj->nm',chi.conj(),Z,dc).real
 f=T.sqrt(8/(h*T.clamp(q,min=1e-6)));psi=f[:,None]*chi; derivatives=f[:,None,None]*(dc-.5*(logdh+dq/T.clamp(q,min=1e-6)[:,None])[:,:,None]*chi[:,None,:])
 theta=T.asin(tt/2)/2;p=3*T.cos(theta)/(2*rho*dd);qq=-3*T.sin(theta)/(2*rho*dd);gg=Gtemplate(p,qq).to(T.complex128);sp=T.stack([-xyz[:,1]/rho,xyz[:,0]/rho,tt*0],1)
 gauge=T.stack([T.kron(g.contiguous(),T.eye(4,dtype=T.complex128)) for g in gg]);cov=derivatives.clone();cov[:,1:]+=1j*sp[:,:,None]*T.einsum('nij,nj->ni',gauge,psi)[:,None,:]
 E=T.einsum('ni,aij,nmj->nam',psi.conj(),QT,cov).real;inv=T.linalg.inv(E); kinetic=1j*T.einsum('nma,aij,nmj->ni',inv.to(T.complex128),KT,cov);res=kinetic-h[:,None]*(psi@MT.T)
 return res,E,q,psi
train=T.tensor(center+radius*np.array(list(itertools.product([-1.,0.,1.],repeat=4))))
rng=np.random.default_rng(291026);validation=T.tensor(center+radius*rng.uniform(-1,1,(128,4)))

def metrics(pos):
 with T.no_grad():
  r,E,q,psi=compute(pos);g=T.einsum('nai,ab,nbj->nij',E,T.diag(T.tensor([-1.,1.,1.,1.])),E);return {'max_residual':float(T.linalg.vector_norm(r,dim=1).max()),'rms_residual':float(T.sqrt((r.abs()**2).sum(1).mean())),'min_abs_detE':float(T.linalg.det(E).abs().min()),'max_inverse_g00':float(T.linalg.inv(g)[:,0,0].max()),'min_q':float(q.min())}
before={'train':metrics(train),'validation':metrics(validation)};calls=0;opt=T.optim.LBFGS([params],lr=.5,max_iter=400,tolerance_grad=1e-10,tolerance_change=1e-13,line_search_fn='strong_wolfe')
def closure():
 global calls
 opt.zero_grad();r,E,q,psi=compute(train);loss=(r.abs()**2).sum(1).mean()+100*T.relu(1e-4-q).square().mean();metric=T.einsum('nai,ab,nbj->nij',E,T.diag(T.tensor([-1.,1.,1.,1.])),E); g00=T.linalg.inv(metric)[:,0,0];loss=loss+100*T.relu(g00+.05).square().mean();loss.backward();calls+=1;return loss
start=time.time();opt.step(closure);out={'contract':'Two modes with independent affine complex amplitudes; common positive amplitude enforces h psi†Zbeta psi=8. Fixed original couplings and zero Lorentz spin connection. 81 collocation/128 held-out points, radius .01 about P1; no regional proof.','before':before,'after':{'train':metrics(train),'validation':metrics(validation)},'calls':calls,'seconds':time.time()-start,'coefficients_real_imag':params.detach().tolist(),'center':center.tolist(),'radius':radius}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='coefficients_real_imag'},indent=2))
