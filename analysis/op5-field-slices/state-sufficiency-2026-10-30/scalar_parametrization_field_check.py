"""Check impact of scalar-only normalization on original full field equations; no fitting."""
from pathlib import Path
import importlib.util,json,hashlib,math,numpy as np
ROOT=Path(__file__).resolve().parent
paths=[ROOT/'recursive_calibrator.py',ROOT/'scalar_parametrization_order7_result.json',ROOT/'fifth-window-result.json',Path(__file__)]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
spec=importlib.util.spec_from_file_location('scalar_field_check_model',paths[0]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);model=m.TaylorModel(5)
norm=json.loads(paths[1].read_text());old=json.loads(paths[2].read_text());rows=[]
for row,baseline in zip(norm['results'],old['results']):
 mi=[tuple(a) for a in row['multiindices']];lookup={a:n for n,a in enumerate(mi)};values=np.array(row['normalized_coefficients_real_imag'],float);packed=np.array([values[lookup[a]] for a in model.fullidx]);coeff=packed[:,:12]+1j*packed[:,12:]
 oldp=np.array(baseline['coefficients_real_imag']);oc=oldp[:,:12]+1j*oldp[:,12:];bg=model.background(row['point']);f=model.evaluate(m.T.tensor(coeff),bg).detach().numpy();E=model.evaluate(m.T.tensor(coeff),bg,True).detach().numpy()[0];Eold=model.evaluate(m.T.tensor(oc),bg,True).detach().numpy()[0]
 blocks={}
 for d in range(5):
  ids=[n for n,a in enumerate(model.idx) if sum(a)==d];weights=np.array([math.prod(math.factorial(v) for v in model.idx[n]) for n in ids]);blocks[str(d)]=float(np.linalg.norm(f[ids]*weights[:,None]))
 out={'point_index':row['point_index'],'normalized_full_F_actual_derivative_blocks':blocks,'coframe_value_change':float(np.linalg.norm(E-Eold)),'coframe_determinant':float(np.linalg.det(E))};rows.append(out);print(out,flush=True)
(ROOT/'scalar_parametrization_field_check_result.json').write_text(json.dumps({'contract':'Scalar normalized field fed into previously reviewed full comparator; floating evaluation of scalar construction, no solve. Scalar normalization alone need not preserve full PDE.','inputs_sha256':hashes,'inputs_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==hashes[str(p)] for p in paths),'results':rows},indent=2))
