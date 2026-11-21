Print["Kernel: ", $Version];
v[r_] := {1,r};
mat[r_] := Outer[Times,v[r],v[r]]/(1+r^2);
lambda[r_,s_,t_] := (1+r^2)/((r-s)(r-t));
Print["three-load synthesis residual = ", Together[
 lambda[r,s,t] mat[r]+lambda[s,r,t] mat[s]+lambda[t,r,s] mat[t]-DiagonalMatrix[{0,1}]]];
rh=-997807/10^9; rc={153875/10^8,-353491/10^8};
gmax[x_] := 1/Max[Abs[{lambda[0,rh,x],lambda[rh,0,x],lambda[x,0,rh]}]];
loads=gmax /@ rc;
Print["additive model J load ceilings and max per-state A readout error for 1 percent root = ",
 N[Transpose[{loads,loads (3/1000)^2 (1-(99/100)^2)}],14]];
Print["two unnormalized A and cross constraints determinant = ",Det[{{1,1},{r,s}}]];

phaseRemain=(6/10^6-266772544892/10^17)/8;
Print["remaining normalized visible V budget per read = ",N[Sin[phaseRemain],14]];
op[f_] := Expand[u D[f,{u,2}]+D[f,u]];
derivCheck[n_] := Expand[D[Nest[op,u^14,n],u]-
 Sum[(n!/j!) Binomial[n+1,j+1] u^j D[u^14,{u,n+j+1}],{j,0,n}]];
Print["annulus derivative coefficient checks for monomial n=3,4,5 = ", derivCheck /@ {3,4,5}];
Print["two examples with invisible unmodulated V residuals = ", {
 Together[1/(1-v)-1-v/(1-v)],
 {1,0}.Inverse[DiagonalMatrix[{1,1-v}]].{1,0}-1}];

cutPoly=Expand[Sum[Binomial[25,i] xx^i(1-xx)^(25-i),{i,0,12}]];
cut[x_] := cutPoly /. xx->x;
Print["cutoff endpoint values and derivative jets through order 12 = ",
 {cut[0],cut[1],Table[{D[cut[x],{x,k}]/.x->0,D[cut[x],{x,k}]/.x->1},{k,1,12}]}];
Print["cutoff derivative beta-kernel residual = ",
 Expand[D[cut[x],x]+25 Binomial[24,12] x^12(1-x)^12]];

epsE=33346568111499/10^20; epsM=5/10^8;
vcap=Sin[6/(8 10^6)]-epsE;
Print["monitor difference acceptance with unit measured direct amplitude = ",
 N[vcap (1-epsM)-epsE-epsM,14]];

fu=Expand[D[u^5 cut[2 u-1/2],u]/5];
bz[p_] := Module[{co = CoefficientList[p,zz],n},n=Length[co]-1;
 Max[Abs[Table[Sum[co[[j+1]] Binomial[k,j]/Binomial[n,j],{j,0,k}],{k,0,n}]]]];
jets[m_] := D[Nest[op,fu,m],u];
jetBound[m_] := Max[Table[bz[Expand[jets[m]/.u->1/4+(i+zz)/64]],{i,0,31}]];
Print["exact rational Bernstein bounds, rounded {m3,m4,m5} = ", N[jetBound /@ {3,4,5},12]];
Print["core derivative factors = ", D[Nest[op,u^4,#],u]& /@ {3,4,5}];
Print["zero mass from primitive endpoint = ", {cut[0],cut[1]}.{0, (3/4)^5/5}];
