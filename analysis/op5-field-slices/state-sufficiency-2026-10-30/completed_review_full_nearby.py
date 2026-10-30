"""Two bounded nearby full-R1 reprojections, then exact-location symmetric-H completion."""
from pathlib import Path
import hashlib,json,time,numpy as np,torch as T,itertools
ROOT=Path(__file__).resolve().parent;prior=ROOT/'completed_review_full_gate.py';ns={'__file__':str(prior)}
exec(prior.read_text().split('DH=T.func.jacrev')[0],ns)
space=ns['space'];model=ns['model'];R=ns['R'];DR=ns['DR'];q0=ns['q'];N=ns['Nfull'];H0=ns['H'];pairs=ns['pairs'];prolonged=ns['prolonged'];rows=[];rng=np.random.default_rng(20261030);tic=time.time()
def refresh(q):
    # Recenter exact original background Taylor coefficients at every evaluation.
    # This avoids using a cubic truncation centered at the old point off-center.
    space['pt']=T.tensor(q[120:]);space['bg']=model.background(q[120:])
def evaluate(q,derivative=False):
    refresh(q);qt=T.tensor(q);r=R(qt).detach().numpy()
    return (r,DR(qt).detach().numpy()) if derivative else r
for trial in range(2):
    coeff=rng.normal(size=N.shape[1]);coeff/=np.linalg.norm(coeff);direction=N@coeff;start=q0+1e-3*direction;q=start.copy();history=[]
    for iteration in range(5):
        r,D=evaluate(q,True);history.append({'iteration':iteration,'R_norm':float(np.linalg.norm(r))})
        if np.linalg.norm(r)<1e-12:break
        correction=np.linalg.lstsq(D,-r,rcond=1e-9)[0];q+=correction
    r,D=evaluate(q,True);J=D[:,24:120];A=np.zeros((128,240))
    for pn,(mu,nu) in enumerate(pairs):
        A[mu*32:(mu+1)*32,pn*24:(pn+1)*24]=J[:,nu*24:(nu+1)*24]
        if mu!=nu:A[nu*32:(nu+1)*32,pn*24:(pn+1)*24]=J[:,mu*24:(mu+1)*24]
    initial=prolonged(q,H0);correction,_,rank,sv=np.linalg.lstsq(A,-initial,rcond=1e-9);H=H0+correction;final=prolonged(q,H)
    ps,js,b,V,f=space['pieces'](T.tensor(q));V=V.detach().numpy();g00=float(V[0]@np.diag([-1,1,1,1])@V[0]);detE=float(1/np.linalg.det(V))
    row={'trial':trial,'epsilon':1e-3,'random_seed':20261030,'position':q[120:].tolist(),'R_history':history,'final_R_norm':float(np.linalg.norm(r)),
      'R1_reprojection_correction_norm':float(np.linalg.norm(q-start)),'total_germ_movement_norm':float(np.linalg.norm(q-q0)),
      'completed_prolongation_residual_before':float(np.linalg.norm(initial)),'completed_prolongation_residual_after':float(np.linalg.norm(final)),'H_correction_norm':float(np.linalg.norm(correction)),'A2_rank':int(rank),'A2_singular_values':sv.tolist(),'detE':detE,'g00':g00}
    rows.append(row);print(row,flush=True)
paths=[Path(__file__),prior,ROOT/'completed_tableau_check.py',ROOT/'recursive_calibrator.py',ROOT/'fifth-window-result.json',model.source]
(ROOT/'completed_review_full_nearby_result.json').write_text(json.dumps({'contract':'Two random fullR1 tangent perturbations at epsilon1e-3, nonlinearR1 reprojection then symmetricsecondjet completion. Exact original background recentered for each evaluation. Finite samples only, no analytic neighborhood/existence proof.','seconds':time.time()-tic,'inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'results':rows},indent=2))
