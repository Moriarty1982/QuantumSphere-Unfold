"""Bounded simultaneous full-field fit in scalar-normalized state coordinates."""
from pathlib import Path
import os
os.environ.setdefault('OMP_NUM_THREADS','2');os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import argparse,importlib.util,json,time,hashlib,platform,numpy as np,torch as T
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('chart_model',ROOT/'scalar_chart_model.py');cm=importlib.util.module_from_spec(spec);spec.loader.exec_module(cm)
T.set_default_dtype(T.float64);T.set_num_threads(2)

def run(order=4,point_index=0,maxsteps=15):
    tic=time.time();started=datetime.now(timezone.utc).isoformat();seedpath=ROOT/'fifth-window-result.json';seed=next(row for row in json.loads(seedpath.read_text())['results'] if row['point_index']==point_index)
    model=cm.ChartModel(order,seed['point']);u0=model.coefficients_from_row(seed);A,topstart,rowstart=model.top_operator(T.tensor(u0));U,sv,Vh=np.linalg.svd(A,full_matrices=False);rank=int(np.sum(sv>sv[0]*1e-9));L=T.tensor(U[:,rank:])
    paths=[Path(__file__),ROOT/'scalar_chart_model.py',ROOT/'scalar_parametrization.py',ROOT/'recursive_calibrator.py',seedpath,model.base.source];hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    start=5;fixed=T.tensor(u0);z0=u0[start:topstart].ravel();z=z0.copy();history=[];damp=1e-7
    def full(lower,top=None):return T.cat((fixed[:start],lower.reshape(-1,23),T.zeros_like(fixed[topstart:]) if top is None else top.reshape(-1,23)),dim=0)
    def source(lower):return model.evaluate(full(lower))
    def objective(lower):
        f=source(lower);return T.cat((f[:rowstart].ravel(),L.T@f[rowstart:].ravel()))
    fun=lambda lower:objective(T.tensor(lower)).detach().numpy();jac=T.func.jacrev(objective);initial=fun(z)
    print('START',order,point_index,'shape',A.shape,'rank',rank,'initial',np.linalg.norm(initial),flush=True)
    for it in range(maxsteps):
        r=fun(z)
        if np.linalg.norm(r)<1e-10:break
        J=jac(T.tensor(z)).detach().numpy();JJ=J@J.T;accepted=False
        for trial in range(10):
            step=-J.T@np.linalg.solve(JJ+damp*np.eye(len(r)),r);candidate=z+step
            try:nr=fun(candidate);good=np.isfinite(nr).all() and np.linalg.norm(nr)<np.linalg.norm(r) and np.linalg.norm(candidate)<100*max(np.linalg.norm(z0),1)
            except Exception:good=False
            if good:z=candidate;accepted=True;damp=max(damp/3,1e-14);break
            damp*=10
        history.append({'iteration':it,'accepted':accepted,'objective_norm':float(np.linalg.norm(fun(z))),'step_norm':float(np.linalg.norm(step)),'damping':damp});print(history[-1],flush=True)
        if not accepted:break
    fsource=source(T.tensor(z)).detach().numpy();b=fsource[rowstart:].ravel();tests=[]
    for cut in [1e-8,1e-9,1e-11]:
        top,_,rnk,svals=np.linalg.lstsq(A,-b,rcond=cut);tests.append({'rcond':cut,'rank':int(rnk),'residual_norm':float(np.linalg.norm(A@top+b)),'top_nonpivot_coefficient_norm':float(np.linalg.norm(top))})
    top=np.linalg.lstsq(A,-b,rcond=1e-9)[0];nonpivot=full(T.tensor(z),T.tensor(top));coeff=model.from_nonpivot(nonpivot);realcoeff=model.from_nonpivot(nonpivot,real=True);fnorm,gnorm=model.residual_norms(nonpivot)
    E=model.base.evaluate(coeff,model.bg,True).detach().numpy()[0];iv=np.linalg.inv(E);fullnp=realcoeff.detach().numpy();fullseed=np.array(seed['coefficients_real_imag']);lookup={tuple(a):n for n,a in enumerate(seed['multiindices'])};lowchanges={}
    for d in [0,1]:
        ids=[n for n,a in enumerate(model.idx) if sum(a)==d];old=np.array([fullseed[lookup[model.idx[n]]] for n in ids]);lowchanges[str(d)]={'full_coefficient_change':float(np.linalg.norm(fullnp[ids]-old)),'nonpivot_exactly_fixed':bool(np.array_equal(nonpivot.detach().numpy()[ids],u0[ids]))}
    column_checks=[];zero=full(T.tensor(z));base=model.evaluate(zero).detach().numpy()[rowstart:].ravel()
    for ci in [0,1,22,A.shape[1]-1]:
        delta=np.zeros_like(top);delta[ci]=.01;value=model.evaluate(full(T.tensor(z),T.tensor(delta))).detach().numpy()[rowstart:].ravel();column_checks.append({'column':ci,'error':float(np.linalg.norm(value-base-.01*A[:,ci]))})
    growth={str(d):float(np.linalg.norm(np.array([fullnp[n]*cm.base.factorial(a) for n,a in enumerate(model.idx) if sum(a)==d]))) for d in range(order+1)}
    out={'contract':'Scalar chart substituted before full field evaluation, all induced pivot derivatives included. Fixed nonpivot values/first derivatives; variable nonpivot degrees2..order-1; eliminate/recover nonpivot highest coefficients. Original background/couplings. Finite float64 result, not all-order PDE existence.',
      'order':order,'point_index':point_index,'point':seed['point'],'started_at':started,'seconds':time.time()-tic,'inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in paths),
      'matrix_shape':list(A.shape),'highest_rank':rank,'singular_values':sv.tolist(),'initial_objective':float(np.linalg.norm(initial)),'final_objective':float(np.linalg.norm(fun(z))),'history':history,'top_tests':tests,'full_F_blocks':fnorm,'scalar_g_blocks':gnorm,
      'coframe':{'determinant':float(np.linalg.det(E)),'inverse_metric_g00':float(iv[0]@np.diag([-1,1,1,1])@iv[0]),'pivot_positive':float(fullnp[0,0]),'radicand_central':float(fullnp[0,0]**2)},
      'low_changes':lowchanges,'lower_nonpivot_coefficient_change':float(np.linalg.norm(z-z0)),'raw_full_jet_norms':growth,'top_column_controls':column_checks,'multiindices':model.idx,'coefficients_real_imag':fullnp.tolist(),'nonpivot_coefficients':nonpivot.detach().numpy().tolist(),
      'software':{'python':platform.python_version(),'numpy':np.__version__,'torch':T.__version__}}
    (ROOT/f'scalar_chart_fit_order{order}_point{point_index}.json').write_text(json.dumps(out,indent=2));print('FINAL',order,'F',fnorm,'g',gnorm,'geometry',out['coframe'],flush=True)
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--order',type=int,default=4,choices=[4,5]);p.add_argument('--point',type=int,default=0);p.add_argument('--maxsteps',type=int,default=15);a=p.parse_args();run(a.order,a.point,a.maxsteps)
