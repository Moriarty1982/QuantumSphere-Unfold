ClearAll["Global`*"];
Print["kernel version = ",$Version];

coords={x,y,z};
grad[f_] := Table[D[f,coords[[i]]],{i,3}];
div[v_] := Total[Table[D[v[[i]],coords[[i]]],{i,3}]];
tensorDiv[m_] := div /@ m;
u=grad[phi[x,y,z]];
id=IdentityMatrix[3];
g=Table[D[u[[i]],coords[[j]]],{i,3},{j,3}];
sigma=mu (g+Transpose[g])+lame div[u] id;
product=Outer[Times,u,u];
rawFlux=amp sigma.u+massFactor tensorDiv[product]/2;
superPotential=amp (mu-lame/2) (u.u) id+(amp lame+massFactor/2) product;
Print["direct density flux decomposition residual = ",
  Expand[rawFlux-tensorDiv[superPotential]]];

general={{a11[x,y,z],a12[x,y,z],a13[x,y,z]},
  {a12[x,y,z],a22[x,y,z],a23[x,y,z]},
  {a13[x,y,z],a23[x,y,z],a33[x,y,z]}};
v=tensorDiv[general];
dens=-switch[t] div[v];
mom=switch'[t] v;
stressTensor=-switch''[t] general;
Print["conserved compensator residual = ",
  Expand[Join[{D[dens,t]+div[mom]},D[mom,t]+tensorDiv[stressTensor]]]];
shift=switch[t] v/rho;
Print["elastic displacement to density and momentum residual = ",
  Expand[Join[{-rho div[shift]-dens},rho D[shift,t]-mom]]];
Print["required active Cauchy stress divergence residual = ",
  Expand[rho D[shift,{t,2}]-tensorDiv[-stressTensor]]];

quad=z^2-(x^2+y^2)/2;
hess=Table[D[quad,coords[[i]],coords[[j]]],{i,3},{j,3}];
Print["isotropic conduction moment = ",Tr[kappa id.hess]];
Print["uniaxial conduction moment coefficient = ",
  Tr[DiagonalMatrix[{kp,kp,kz}].hess]];
Print["compensated plateau direct density residual = ",
  Expand[div[rawFlux]-div[tensorDiv[superPotential]]]];
