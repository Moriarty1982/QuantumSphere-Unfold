import sympy as s
from pathlib import Path
import json
t=s.symbols('t',positive=True)
W=[s.zeros(4) for _ in range(4)]
for i in range(1,4): W[i][i,0]=W[i][0,i]=1/t
R={}; T={}
for mu in range(4):
 for nu in range(4):
  R[mu,nu]=(s.diff(W[nu],t) if mu==0 else s.zeros(4))-(s.diff(W[mu],t) if nu==0 else s.zeros(4))+W[mu]*W[nu]-W[nu]*W[mu]
  for c in range(4): T[c,mu,nu]=W[mu][c,nu]-W[nu][c,mu]
trace=[sum(T[b,a,b] for b in range(4)) for a in range(4)]
Cartan={(a,b,c):s.simplify(T[c,a,b]+int(a==c)*trace[b]-int(b==c)*trace[a]) for a in range(4) for b in range(4) for c in range(4)}
lam=s.diag(0,1/t**2,1/t**2,1/t**2); jl=[-2*t,0,0,0]
assert all(s.simplify(val-(lam[a,c]*jl[b]-lam[b,c]*jl[a]))==0 for (a,b,c),val in Cartan.items())
Ric=s.Matrix(4,4,lambda b,nu:s.simplify(sum(R[a,nu][a,b] for a in range(4))))
eta=s.diag(-1,1,1,1)
scalar=s.trace(eta*Ric)
assert Ric==s.diag(3,1,1,1)/t**2
assert scalar==0
result={'torsion_trace':str(trace),'normalized_source_lambda':str(lam),'Ricci_independent_connection':str(Ric),'scalar_independent_connection':str(scalar),'scope':'source shape normalized; not the action-fixed physical multiplier'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
