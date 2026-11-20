ClearAll["Global`*"];
Print["kernel version = ", $Version];

(* f is a polynomial check on 0<=t<=1, with derivatives through order 9 flat. *)
rate = t^9 (1-t)^9;
ramp = Integrate[Expand[s^9 (1-s)^9],{s,0,t}]/Integrate[rate,{t,0,1}];
timeFactors = Table[Integrate[Expand[D[ramp,{t,2 n}] D[ramp,{t,2 m+1}]],{t,0,1}],
  {n,0,4},{m,0,4}];
Print["polynomial ramp flux matrix = ",timeFactors];

springExtension = u[t]-w[t]-d[t];
springRate = D[spring springExtension^2/2,t];
internalPower = -spring springExtension u'[t]+spring springExtension w'[t];
Print["spring power residual = ",Expand[springRate+internalPower+spring springExtension d'[t]]];

coords = {x,y,z};
grad[f_] := Table[D[f,coords[[i]]],{i,3}];
div[v_] := Total[Table[D[v[[i]],coords[[i]]],{i,3}]];
displacement = grad[potential[x,y,z]];
quad = z^2-(x^2+y^2)/2;
qGrad = grad[quad];
qHess = Table[D[quad,coords[[i]],coords[[j]]],{i,3},{j,3}];
g = Table[D[displacement[[i]],coords[[j]]],{i,3},{j,3}];
sigma = mu (g+Transpose[g])+lame div[displacement] IdentityMatrix[3];
Print["longitudinal stress times displacement residual = ",
  Expand[sigma.displacement-mu grad[displacement.displacement]-lame displacement div[displacement]]];
fluxVector = (qGrad.displacement) displacement-(displacement.displacement) qGrad/2;
Print["harmonic quadrupole integration-by-parts residual = ",
  Expand[div[fluxVector]-displacement.qHess.displacement-
    (qGrad.displacement) div[displacement]]];
quadShifted = quad /. Thread[coords->coords+eps {v1,v2,v3}];
Print["quadrupole pushforward coefficient at order two = ",
  Expand[Coefficient[quadShifted,eps,2]]];
Print["combined direct-energy coefficient residual = ",
  Simplify[(rho1+rho2/c^2)/2+(1+1/c) lame/2-
    (rho1+rho2/c^2+(1+1/c) lame)/2]];
