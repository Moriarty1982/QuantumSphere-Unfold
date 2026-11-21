Print["Kernel: ", $Version];
vH=aH {1,rH}; vC=aC {1,rC};
Print["optical null vector residual = ", Expand[aC vH-aH vC-aH aC {0,rH-rC}]];
Print["calibration mismatch residual = ", Expand[
 (1+dh) {1,rH}-(1+dc) {1,rC}-{dh-dc,rH-rC+dh rH-dc rC}]];
rh = -997807/10^9; rc={153875/10^8,-353491/10^8};
p = 4/10^4;
eta[c_] := p Abs[rh-c]/(2+p(Abs[rh]+Abs[c]));
Print["conditional H/HCl J remainder and relative optical gain limit = ",
 N[Transpose[{Abs[rh-rc],eta /@ rc}],14]];
m[a_,b_] := (1-a^2-b^2)/((1-(a+b)^2)(1-(a-b)^2))-1;
avg = Sum[1/(1-i a-j b),{i,{-1,1}},{j,{-1,1}}]/4-1;
Print["two-variable echo majorant residual and first coefficients = ",
 {Together[avg-m[a,b]], Normal[Series[m[t a,t b],{t,0,4}]]}];
Print["two tagged echo paths example {normalized rest, eight-read phase bound} = ",
 N[{m[1/2000,1/2000],8 ArcSin[m[1/2000,1/2000]]},14]];

Print["Poisson log-kernel and compensated example moments = ",
 {Integrate[-u Log[u],{u,0,1}],Integrate[u(1-u^2)(1-3u^2),{u,0,1}],
  Integrate[-u(1-u^2)(1-3u^2) Log[u],{u,0,1}]}];
Print["equal tagged-path limit for eight-read 6e-6 budget = ",
 N[Sqrt[Sin[6/(8 10^6)]/(2+4 Sin[6/(8 10^6)])],14]];
Print["signal b4 Weyl to control-axis transfer residual = ",
 Together[(4 s/radius^2)(288 amplitude kap b4 ps/radius^2)/
 (147456 c4 pc b4/radius^8)-amplitude kap ps radius^4 s/(128 c4 pc)]];
