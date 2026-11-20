ClearAll["Global`*"];
Print["kernel version = ", $Version];

coords = {x,y,z};
u = {ux[x,y,z],uy[x,y,z],uz[x,y,z]};
w = -u/c;
gradient[v_] := Table[D[v[[i]],coords[[j]]],{i,3},{j,3}];
div[v_] := Tr[gradient[v]];
strain[v_] := With[{g=gradient[v]},(g+Transpose[g])/2];
stress[v_] := 2 mu strain[v]+lame div[v] IdentityMatrix[3];
force[s_] := Table[Total[Table[D[s[[i,j]],coords[[j]]],{j,3}]],{i,3}];
solidStress = stress[u];
holderStress = c stress[w];
restSetting = (1+1/c) u-force[solidStress]/spring;
springForce = -spring (u-w-restSetting);
Print["static force residuals, source and holder = ",
  Simplify[{force[solidStress]+springForce,force[holderStress]-springForce}]];
Print["combined linear Cauchy stress = ", Simplify[solidStress+holderStress]];

densityShift = -rho1 div[u]-rho2 div[w];
sourceShift = gamma1 div[u]+gamma2 div[w];
Print["direct density-source residual in the rest-mass W2 approximation = ",
  Simplify[(densityShift+higgs sourceShift)/.{gamma1->rho1/higgs,gamma2->rho2/higgs}]];
Print["joint density and source at compensated rest-mass ratio = ",
  Simplify[{densityShift,sourceShift} /.
    {rho2->c rho1,gamma1->rho1/higgs,gamma2->c rho1/higgs}]];
Print["sum of prescribed inertias for opposite displacement = ",
  Factor[rho1 acc-rho2 acc/c]];
Print["static spring energy residual = ",
  Simplify[spring (u-w-restSetting).(u-w-restSetting)/2-
    force[solidStress].force[solidStress]/(2 spring)]];

b = {bx[x,y,z],by[x,y,z],bz[x,y,z]};
lap[f_] := D[f,{x,2}]+D[f,{y,2}]+D[f,{z,2}];
Print["divergence of a vector Laplacian residual = ",
  Expand[div[lap /@ b]-lap[div[b]]]];
Print["elastic stress with Laplace displacement residual = ",
  Expand[stress[lap /@ b]-Map[lap,stress[b],{2}]]];
