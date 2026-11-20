ClearAll["Global`*"];
Print["kernel version = ",$Version];

id=IdentityMatrix[3];
h={{h11,h12,h13},{h12,h22,h23},{h13,h23,h33}};
h2=Array[a,{3,3}];
lin[e_]:=lame Tr[e] id+2 mu e;
sym[m_]:=(m+Transpose[m])/2;
f=id+eps h+eps^2 h2;
e=(Transpose[f].f-id)/2;
p=f.lin[e];
p2=Map[Coefficient[Expand[#],eps,2]&,p,{2}];
n=(lame Tr[h.h]/2) id+3 mu h.h+lame Tr[h] h;
Print["quadratic first Piola coefficient residual = ",Expand[p2-lin[sym[h2]]-n]];
Print["trace integrated coefficient residual = ",
  Expand[Tr[n]-(5 lame/2+3 mu) Tr[h.h]-lame (Tr[h]^2-Tr[h.h])]];
Print["positive trace coefficient at Lamé lower edge = ",
  Simplify[(5 lame/2+3 mu)/.lame->-2 mu/3]];
materialCauchy2=Expand[p2+lin[h].Transpose[h]-Tr[h] lin[h]];
expectedCauchy=lin[sym[h2]]+n+Transpose[h.lin[h]]-Tr[h] lin[h];
Print["material-point Cauchy conversion residual = ",Expand[materialCauchy2-expectedCauchy]];

coords={x,y,z};
grad[g_] := Table[D[g,coords[[i]]],{i,3}];
div[v_] := Total[Table[D[v[[i]],coords[[i]]],{i,3}]];
u=grad[phi[x,y,z]];
hess=Table[D[u[[i]],coords[[j]]],{i,3},{j,3}];
Print["Hessian integration-by-parts residual = ",
  Expand[div[Tr[hess] u-hess.u]-Tr[hess]^2+Tr[hess.hess]]];
Print["scaled counterbody quadratic factor residual = ",
  Expand[(1+c (1/c)^2)-(1+1/c)]];
