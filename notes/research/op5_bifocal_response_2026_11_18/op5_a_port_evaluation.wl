Print["Kernel: ", $Version];
fit[x1_,x2_,y1_,y2_] := (x2 y1-x1 y2)/(x2-x1);
Print["measured two-load intercept error residual = ", Together[
 fit[x1,x2,t+r x1+e1,t+r x2+e2]-t-(x2 e1-x1 e2)/(x2-x1)]];
cross[v_] := v[[1]] v[[4]]/(v[[2]] v[[3]]);
v={q00,q01,q10,q11};
Print["separable common multiplier residual and additive counterexample = ",
 {Together[cross[v {a0 b0,a0 b1,a1 b0,a1 b1}]-cross[v]],
 cross[{1,2,3,6}+1]-cross[{1,2,3,6}]}];
radius=(4000+2001+3000)/10^11/(99/100-3/10^8);
Print["one-endpoint log and phase bounds with conservative true reference floor = ",
 N[{-4 Log[1-radius],4 ArcSin[radius]},15]];
ps=grav dr len rad^2; lo=(1+rk) noise/(bet-rk);
Print["dimensionless mechanical bounds and window residuals = ", Together[{
 {grav dr len rad hmax/cu,grav dr len rad^2 strain/ce,grav rad^2 sig/cs,
 grav dr rad^3 force/(elas cf),grav dr len rad acc tt^2/(4 cu)}/ps-
 {hmax/(cu rad),strain/ce,sig/(cs dr len),rad force/(cf elas len),acc tt^2/(4 cu rad)},
 rk+(1+rk)(noise/ps)/(lo/ps)-bet}]];
Print["indicative displacement readout fraction for one-percent isolated model = ", N[(1/100)/(9591531/100),15]];

points={{1,0,0},{0,1,0},{0,0,1},{1,1,0},{1,0,1},{0,1,1}};
quad[{x_,y_,z_}] := {x^2,y^2,z^2,2x y,2x z,2y z};
mat=Array[metricElement,{3,3}]; ident=IdentityMatrix[3];
Print["Hessian rank determinant and compatible metric first-order residual = ",
 {Det[quad /@ points], Map[Expand,
  (D[Transpose[ident+s mat].(ident+s mat),s]/.s->0)-mat-Transpose[mat],{2}]}];
