from pathlib import Path
import sympy as s,json
I=s.I
S=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,0]])
Y=s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])
Z=s.diag(1,-1,0);P=s.diag(1,1,0)
assert I*(S*Y-Y*S)==-Z
cv,dv=s.symbols('c d',nonzero=True,real=True)
B=s.diag(-dv/cv,cv/dv,0)
assert s.simplify(B-((cv/dv-dv/cv)/2*P-(cv/dv+dv/cv)/2*Z))==s.zeros(3)
# P is in the associative algebra (not automatically the Lie algebra).
assert 4*S*S==P
# Spatial connection A_mu=s_mu G always has zero commutator curvature.
p,q,pm,qm,pn,qn,sm,sn,dsm,dsn=s.symbols('p q pm qm pn qn sm sn dsm dsn',real=True)
G=s.Matrix([[0,0,p],[0,0,q],[p,q,0]])
Gm=s.Matrix([[0,0,pm],[0,0,qm],[pm,qm,0]])
Gn=s.Matrix([[0,0,pn],[0,0,qn],[pn,qn,0]])
F=dsm*G+sn*Gm-dsn*G-sm*Gn+I*(sm*G*sn*G-sn*G*sm*G)
assert all(F[j,j]==0 for j in range(3))
R=s.eye(3)-2*G*G/(p*p+q*q)
assert s.simplify(R*R-s.eye(3))==s.zeros(3)
assert s.simplify(R*G-G*R)==s.zeros(3)
assert s.simplify(R*Y+Y*R)==s.zeros(3)
assert s.simplify(R*S-S*R)!=s.zeros(3)
result={'frozen_sector_involution':'R=I-2G^2/(p^2+q^2); R^2=I, [R,G]=0, {R,Y}=0; J=R tensor gamma5', 'relative_connection_generator':str(B),'decomposition':'B=((c/d-d/c)/2)P_AB-((c/d+d/c)/2)Z_AB',
'Z_from_commutator':'Z=-i[S,Y]','P_from_product':'P=4 S^2; associative closure only',
'trace_B':str(s.trace(B)),'original_curvature_diagonal':[str(F[j,j]) for j in range(3)],
'interpretation':'Algebraic expressibility does not authorize a new gauge connection. Nonzero trace requires central U(1) extension if assumed algebra is su(3).'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
