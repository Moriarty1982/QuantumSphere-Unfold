Print["Kernel: ", $Version];
pa=DiagonalMatrix[{1,0}]; pj=IdentityMatrix[2]-pa;
basis={{a,b},{c,d}}; mutant=DiagonalMatrix[{sA,sJ}];
read[x_] := Inverse[basis].x.basis;
refl={{daa,daj},{dja,djj}}; cal={{caa,caj},{cja,cjj}};
Print["diagonal-gauge and known cross-standard identities = ", Together[{
 mutant.pa.Inverse[mutant]-pa,
 (mutant.refl.Inverse[mutant])[[1,2]]-daj sA/sJ,
 read[pa].read[refl].read[pj]-(daj/caj) read[pa].read[cal].read[pj]}]];
ref = 1/100;
errD = 1/10^7; errC = 1/10^6; cap = 1/10^6;
Print["same-projection reference ratio: illustrative relative gain uncertainty and absolute entry uncertainty = ",
 N[{errC/ref, (ref errD + cap errC)/(ref-errC)},14]];

Print["fixed cross-phase ambiguity residual = ", Expand[((ss+tshift)+(hh-tshift)+ee)-(ss+hh+ee)]];
echo4 = Total[1/(1-q #)& /@ {1,I,-1,-I}]/4;
Print["four-phase echo rejection residual = ", Together[echo4-1/(1-q^4)]];
printRes = 15210924848694/10^18;
rawSym=52401365665439/10^18;
Print["pilot share and illustrative four-phase symmetric echo product bound = ",
 N[{printRes/4,rawSym^(1/4)},14]];
radialLap[f_] := Expand[4/rad^2 (D[f,s]+s D[f,{s,2}])];
powers=NestList[radialLap,s^4,4];
Print["control core Laplacian jets = ", powers[[3;;5]]];
integrPot=b0 powers[[3]]-b2 powers[[4]]+b4 powers[[5]];
Print["control normalized half-difference, massive transverse Hessian residual = ",
 Expand[{4 s D[integrPot,{s,2}]/rad^2, D[powers[[5]],s]}]];

Print["ordinary axis coefficient after control = ", Expand[integrPot /. s->0]];
Print["two-phase echo identity and isolated round-trip limit in split budget = ",
 {Together[(1/(1-q)+1/(1+q))/2-1/(1-q^2)], N[Sqrt[Sin[6/(8 10^6)]],14]}];
