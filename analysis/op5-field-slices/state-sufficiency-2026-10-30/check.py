"""Exact state-sufficiency comparison; run: python check.py. Not native OP5."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, platform, sys, time
import sympy as s

root = Path(__file__).resolve().parent
started = datetime.now(timezone.utc).isoformat()
tic = time.perf_counter()
source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
x,y,z,t,a,k = s.symbols('x y z t a k', real=True)
E=s.Matrix([2,-a*s.cos(k*x)*s.sin(k*t),0])
B=s.Matrix([0,1,a*s.sin(k*x)*s.cos(k*t)])
coords=(x,y,z)
def curl(v):
    return s.Matrix([s.diff(v[2],y)-s.diff(v[1],z),s.diff(v[0],z)-s.diff(v[2],x),s.diff(v[1],x)-s.diff(v[0],y)])
def div(v):
    return sum(s.diff(v[i],coords[i]) for i in range(3))
def zero(v):
    return all(s.simplify(q)==0 for q in v)
G=s.Matrix([[E.dot(E),E.dot(B)],[E.dot(B),B.dot(B)]])
rho=G/s.trace(G)
assert zero(s.diff(E,t)-curl(B)) and zero(s.diff(B,t)+curl(E))
assert div(E)==div(B)==0
assert zero((G.subs(a,1)-G.subs(a,-1)).subs(t,0))
assert zero((rho.subs(a,1)-rho.subs(a,-1)).subs(t,0))
p={x:0,t:0}
assert E.subs(p)==s.Matrix([2,0,0]) and B.subs(p)==s.Matrix([0,1,0])
assert s.diff(G,t).subs(p)==s.Matrix([[0,-a*k],[-a*k,0]])
assert s.diff(rho,t).subs(p)==s.Matrix([[0,-a*k/5],[-a*k/5,0]])
assert zero(s.diff(G,x).subs(p))
assert s.diff(B,x).subs(p)==s.Matrix([0,0,a*k])
# Full oriented field plus spatial first jets recovers the next Gram derivative.
pred=s.Matrix([[2*E.dot(curl(B)),curl(B).dot(B)-E.dot(curl(E))],
               [curl(B).dot(B)-E.dot(curl(E)),-2*B.dot(curl(E))]])
assert zero(s.diff(G,t)-pred)
result={
 'assertion_tested':'Exact vacuum Maxwell comparison c=1: a=+/-1 have identical entire initial Gram/rho fields but distinct time derivatives for k nonzero.',
 'E':str(E),'B':str(B),'initial_G':str(s.simplify(G.subs(t,0))),
 'point_Gdot':str(s.diff(G,t).subs(p)), 'point_rhodot':str(s.diff(rho,t).subs(p)),
 'point_B_x':str(s.diff(B,x).subs(p)),
 'checks':['both curl evolution equations identically zero','both divergence constraints identically zero','same initial G and rho for all spatial points','same full E and B at origin','different nonzero next Gram/rho derivative','oriented spatial first jets recover Gdot exactly'],
 'scope':'smooth local fields or periodic comparison; no finite-total-energy claim; no native QSC equations or GR constraints tested',
 'outcome':'counterexample to autonomous Gram-field evolution on this comparison family; no counterexample to full-field Cauchy determinism'}
out=root/'result.json';out.write_text(json.dumps(result,indent=2),encoding='utf-8')
manifest={'schema_version':2,'claim_id':'state-sufficiency-maxwell-comparison',
 'repository':{'commit':'f98b29ba8eeb87c053a39285ca348c4d2ef76081','dirty':True},
 'command':[sys.executable,str(Path(__file__).resolve())],
 'environment':{'software':[{'name':'Python','version':platform.python_version()},{'name':'SymPy','version':s.__version__}],'hardware':platform.machine()},
 'mathematics':{'assertion_tested':result['assertion_tested'],'coefficient_domain':'exact symbolic real variables and trigonometric functions','conventions':'c=1; dt E=curl B; dt B=-curl E; G=F^T F; rho=G/trG','inputs':['explicit E,B in check.py'],'bounds':{'family':'a=+1,-1; real k nonzero; local smooth chart'},'non_claims':['native OP5 solution','unified dynamics','finite total energy','regional QSC existence']},
 'randomness':{'used':False,'generator':'','seed':None},
 'run':{'started_at':started,'runtime_seconds':time.perf_counter()-tic,'exit_status':0,'status':'completed','resource_limits':{'memory_bytes':None,'cpu_seconds':None,'max_cores':None,'max_threads':None}},
 'outputs':[{'path':'result.json','sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'kind':'result'}],
 'checks':result['checks'],'result':result['outcome'],'residual_risks':['comparison family is not native OP5; self-review, not independent proof audit'],
 'input_artifacts':[{'path':'check.py','sha256':source_hash,'sha256_after':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}],
 'declared_results':['result.json']}
(root/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
