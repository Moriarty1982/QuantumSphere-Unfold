"""AD crosscheck of near-noise finite-difference completed projection gate, point0."""
from pathlib import Path
import hashlib,json,time,numpy as np,torch as T
ROOT=Path(__file__).resolve().parent;source=ROOT/'completed_review_projection_gate.py'
space={'__file__':str(source)};exec(source.read_text().split('gates=[]')[0],space)
R=space['R'];DR=space['DR'];q=space['q'];H=space['unpackH'](space['H']);L=space['L'];N=space['N'];qt=T.tensor(q);Ht=T.tensor(H);tic=time.time()
def prolonged_jets(jets):
    value=T.cat((qt[:24],jets,qt[120:]));tangent=T.cat((jets.reshape(4,24).T,Ht.permute(1,2,0).reshape(96,4),T.eye(4)),dim=0)
    return (DR(value)@tangent).T.flatten()
derivative=T.func.jacrev(prolonged_jets)(qt[24:120]).detach().numpy();gate=L.T@derivative@N;sv=np.linalg.svd(gate,compute_uv=False)
fd=json.loads((ROOT/'completed_review_projection_gate_result.json').read_text());diffs=[{'step':row['step'],'difference_from_AD':float(np.linalg.norm(np.array(row['matrix'])-gate))} for row in fd['gates']]
paths=[Path(__file__),source,ROOT/'completed_tableau_check.py',ROOT/'recursive_calibrator.py',ROOT/'fifth-window-result.json']
out={'contract':'Point0 completed projection gate AD crosscheck, fixed repairedH, firstjet tangentkerJ; same authoritative R, no finite differences or fitting. AD is floating, not analytic rank proof.','seconds':time.time()-tic,'inputs_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'matrix_shape':list(gate.shape),'matrix':gate.tolist(),'norm':float(np.linalg.norm(gate)),'singular_values':sv.tolist(),'full_unprojected_derivative_norm':float(np.linalg.norm(derivative)),'FD_comparisons':diffs}
(ROOT/'completed_review_ad_gate_result.json').write_text(json.dumps(out,indent=2));print('AD GATE',out['norm'],'sv',sv,'fullnorm',out['full_unprojected_derivative_norm'],'FD',diffs,flush=True)
