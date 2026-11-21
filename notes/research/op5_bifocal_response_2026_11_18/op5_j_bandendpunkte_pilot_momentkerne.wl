Print["Kernel: ", $Version];
den=(g-I a)(g-I b)+g^2; num=den-2g(g-I b);
Print["separate-detuning reflection numerator and norm residuals = ", Expand[
 {num+a b-I g(b-a),
 (den Conjugate[den]/.{Conjugate[a]->a,Conjugate[b]->b,Conjugate[g]->g})
 -(4 g^4+a^2 b^2+g^2(a-b)^2)}]];
ghz=87131520945535/10^7; p=9/10^6;
common=ghz (4 p^2/(1-p^2))^(1/4);
diff=ghz Sqrt[8(1/Sqrt[1-p^2]-1)];
Print["ideal endpoint single-error tuning ceilings in Hz {common, split} = ",N[{common,diff},15]];
alpha=50000/20001; eta=99/100;
jout=(1/eta-1)/alpha; aout=alpha+1/jout;
la=aout+alpha; lj=jout; d0=la lj+1;
bb=(aout-alpha-lj)^2-p^2 ((la+lj)^2-2d0);
ferr=ghz Sqrt[2 p^2 d0^2/(bb+Sqrt[bb^2+4(1-p^2)p^2 d0^2])];
Print["critically coupled old A-loss example {J withdrawal Hz, detuning Hz, J intrinsic-loss ceiling Hz} = ",
 N[{ghz jout,ferr,ghz (1-eta)^2/(4 eta alpha)},15]];
Print["critical coupling residual = ",Together[
 1 -2 ka (kj+aj)/((ka+aa)(kj+aj)+g^2) /.ka->aa+g^2/(kj+aj)]];

Print["cooperativity condition for eta=0.99 =",4 eta/(1-eta)^2];
lam=aj+Sqrt[aj^2+aj g^2/aa];
Print["outcoupling optimum derivative residual = ",
 FullSimplify[D[(1-aj/x) g^2/(g^2+aa x),x]/.x->lam,aa>0&&aj>0&&g>0]];

en=3/10^10; rev=104/10^6; kin=100/99; ain=Sqrt[2];
errE=kin en ain; errF=en ain;
errA=((errF+errE) Sqrt[1+rev^2]+(1+errF)kin en)/(1-errE);
Print["bidirectional pilot norm and ratio errors = ",N[{errE,errA,2 errA/(1-errA)},15]];
nodes={7500000000000000,7209621281667645,6417758663930909,5332332566518210,
 4213952187581498,3289847239741027,2700089336263926,2500000000000000}/10^16;
tiny=1/10^9;
lpoly=Sum[(-1)^(j+1) z^j/j,{j,1,60}];
test=Join[Table[x^j,{j,0,5}],{x,x^2}(lpoly/.z->2x-1)];
mom[k_] := If[OddQ[k],0,Pochhammer[1/2,k/2]/Pochhammer[27/2,k/2]];
average[poly_,cent_,hh_] := Module[{co=CoefficientList[Expand[poly/.x->cent+hh tt],tt]},
 co.Table[mom[j],{j,0,Length[co]-1}]];
results[hh_] := Module[{xs,m,iv,ws,rho,e,tu,pk},
 xs=ReplacePart[nodes,{1->3/4-hh-tiny,8->1/4+hh+tiny}];
 m=Round[10^25 Table[average[test[[i]],xs[[j]],hh],{i,1,8},{j,1,8}]]/10^25;
 iv=Inverse[m]; ws=iv.Join[{-1},ConstantArray[0,7]];
 rho=Norm[iv,Infinity] 8 (1/(61 2^60)+1/(2 10^25)+16 tiny^2);
 e=rho Norm[ws,Infinity]/(1-rho);
 tu=Total[Abs[ws]]+8 e;
 pk=Sqrt[3] (Norm[ws,Infinity]+e)/(hh Beta[1/2,13]);
 {rho,tu,pk}];
Print["finite smooth moment profiles {inverse factor, TV upper, scaled peak gradient upper} = ",
 N[results /@ {1/10000,1/1000,1/200},14]];
Print["gradient absolute one-percent budget over annulus = ",N[1/100/(Sqrt[3/4]-1/2),14]];
