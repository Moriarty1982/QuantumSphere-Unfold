Print["Kernel: ", $Version];
unit={{ca,sa},{-sa,ca}}; pa=DiagonalMatrix[{1,0}]; pj=IdentityMatrix[2]-pa;
dr=Transpose[unit].pa.unit-pj;
Print["lossless conversion mismatch square residual = ",
 FullSimplify[dr.dr-ca^2 IdentityMatrix[2],ca^2+sa^2==1]];
m=3/1000; escape=9/10^6; gam=1/2; rr=1/10; noise=5/10^8;
dt=escape+m(1-Sqrt[1-escape^2]);
budget=2 m dt+dt^2+(m+dt)^2 (gam rr)^2/(1-(gam rr)^2)+noise/gam;
Print["converter example {projector error, product bound, one-percent root budget} = ",
 N[{escape,budget,m^2(1-(99/100)^2)},14]];

bl = 1/10^8;
mon = ((1+bl)^3-1+bl)/(1-bl);
ect =33346568111499/10^20;
vv = Sin[6/(8 10^6)]-ect;
Print["blank monitor relative bound and acceptance in normalized display = ",
N[{mon,(vv-ect-mon)/(1+mon)},14]];
b0hat=b0 (1+sb); m0hat=g0 b0 (1+e0); m1hat=g0(1+gg) b1(1+e1);
Print["blank transfer ratio residual = ",Together[b0hat m1hat/(b1 m0hat)-(1+sb)(1+gg)(1+e1)/(1+e0)]];

cutPoly=Expand[Sum[Binomial[25,i] xx^i(1-xx)^(25-i),{i,0,12}]];
op[f_] := Expand[u D[f,{u,2}]+D[f,u]];
fAnn=Expand[D[u^5 (cutPoly/.xx->2u-1/2),u]/5];
density=Nest[op,fAnn,5];
bernAbs[p_] := Module[{co=CoefficientList[p,z],n},n=Length[co]-1;
 Max[Abs[Table[Sum[co[[j+1]] Binomial[k,j]/Binomial[n,j],{j,0,k}],{k,0,n}]]]];
bounds[poly_,n_] := Table[bernAbs[Expand[poly /. u->1/4+(i+z)/(2n)]],{i,0,n-1}];
g[n_] := Table[1/4+i/(2n),{i,0,n}];
form[a_,b_] := (b^2-a^2)/4-a b Log[b/a]/2;
ff[x_] := x(1-Log[x]);
wing[n_] := MapThread[form,{Most[g[n]],Rest[g[n]]}];
Print["32-ring global/local form bounds = ",
 N[{544565/10^5 10^15 Total[wing[32]],bounds[D[density,u],32].wing[32]}/576,12]];
Print["128-ring local form and direct absolute-weight amplification upper = ",
 N[{bounds[D[density,u],128].wing[128],bounds[density,128].Differences[ff /@ g[128]]}/576,12]];
