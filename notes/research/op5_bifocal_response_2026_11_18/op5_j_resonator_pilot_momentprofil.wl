Print["Kernel: ", $Version];
den=(ka-I w)(kj-I w)+g^2;
num=den-2ka(kj-I w);
Print["matched cavity reflection numerator and denominator norm residuals = ",
 Expand[{num-(g^2-ka kj-w^2+I w(ka-kj)),
 (den Conjugate[den] /. {Conjugate[ka]->ka,Conjugate[kj]->kj,Conjugate[w]->w,Conjugate[g]->g})-
 ((ka kj+g^2-w^2)^2+w^2(ka+kj)^2)}]];
p=9/10^6; bandwidth=10^8; c0=299792458;
center=360329/10^6; hc=1973269804/10^16;
a0=10000 Pi; u0=10001 Pi;
l0=a0 hc/center; gL=(u0^2-a0^2)/(2 a0 1000);
gPrev=c0 gL/l0;
gNeed=(Pi bandwidth) ((1-p^2)/(4 p^2))^(1/4);
ratio=(a0/(4 10^6))/(2 gL);
Print["old and required temporal coupling (Hz), multiplier, old band-edge residual = ",
 N[{gPrev/(2 Pi),gNeed/(2 Pi),gNeed/gPrev,(Pi bandwidth)^2/Sqrt[4 gPrev^4+(Pi bandwidth)^4]},14]];
Print["on-resonance symmetric-extraction amplitude and A reflection at maximum loss = ",
 N[{1/(1+ratio),ratio/(1+ratio)},14]];
Print["symmetric extraction stationarity residual = ",
 Together[D[2 x g/(x^2+alpha x+g^2),x]/.x->g]];

nodes=Table[1/2+Cos[Pi k/5]/4,{k,0,5}];
weight[k_] := -(Times@@Table[-nodes[[j]]/(nodes[[k]]-nodes[[j]]),{j,DeleteCases[Range[6],k]}]);
weights=RootReduce[weight /@ Range[6]];
Print["Chebyshev-Lobatto potential-step moments and total variation = ",
 {RootReduce[Table[weights.(nodes^j),{j,0,5}]],RootReduce[Total[Abs[weights]]]}];
ee=25/10^10; leak=(104/10^6)/10^5;
fact=((1+ee)^6+(1+ee)^4-2)/(1-ee)^4;
lr=2 leak/(1-leak); err=fact+lr+fact lr;
Print["ten-factor, directional leakage, combined and display budgets = ",
 N[{fact,lr,err,(Sin[6/(8 10^6)]-2 (33346568111499/10^20)-err)/(1+err)},14]];
Print["local pilot transfer residual = ",Together[
 (h1 k1 a1 h0 c0)/(h0 k0 a0 h1 c1) (c1 k0)/(c0 k1)-a1/a0]];
eight=N[Table[1/2+Cos[Pi i/7]/4,{i,0,7}],80];
mt = Join[Table[eight^j,{j,0,5}],{eight Log[eight],eight^2 Log[eight]}];
rhs=Join[{-1},ConstantArray[0,7]];
ws=LinearSolve[mt,rhs];
Print["eight-node two-log example {absolute moment residual, total variation} = ",
 N[{Max[Abs[mt.ws-rhs]],Total[Abs[ws]]},15]];

mt2=Join[Table[eight^j,{j,0,5}],{eight Log[2 eight],eight^2 Log[2 eight]}];
dual=Round[10^18 LinearSolve[Transpose[mt2],Table[(-1)^j,{j,0,7}]]]/10^18;
seriesLog=Sum[(-1)^(j+1) tt^j/j,{j,1,44}];
loc=(1+tt)/2;
dualPoly=Expand[dual.Join[Table[loc^j,{j,0,5}],{loc seriesLog,loc^2 seriesLog}]];
bernAbs[poly_] := Module[{co=CoefficientList[poly,zz],n},n=Length[co]-1;
 Max[Abs[Table[Sum[co[[j+1]] Binomial[k,j]/Binomial[n,j],{j,0,k}],{k,0,n}]]]];
supDual=Max[Table[bernAbs[Expand[dualPoly/.tt->-1/2+(i+zz)/32]],{i,0,31}]]+
 (3 Abs[dual[[7]]]/4+9 Abs[dual[[8]]]/16)/(45 2^44);
Print["rational two-log dual bound {sup-norm ceiling, TV floor} = ",
 N[{supDual,Abs[First[dual]]/supDual},16]];
Print["two-log certified floor exceeds 87172.5 = ", Abs[First[dual]]/supDual>174345/2];

xn={7500000000000000,7209621281667645,6417758663930909,5332332566518210,
 4213952187581498,3289847239741027,2700089336263926,2500000000000000}/10^16;
bas[x_] := Join[Table[x^j,{j,0,5}],{x Log[2x],x^2 Log[2x]}];
dualT=Round[10^18 LinearSolve[bas /@ N[xn,90],Table[(-1)^j,{j,0,7}]]]/10^18;
polT=Expand[dualT.Join[Table[loc^j,{j,0,5}],{loc seriesLog,loc^2 seriesLog}]];
supT=Max[Table[bernAbs[Expand[polT/.tt->-1/2+(i+zz)/64]],{i,0,63}]]+
 (3 Abs[dualT[[7]]]/4+9 Abs[dualT[[8]]]/16)/(45 2^44);
ser60=Sum[(-1)^(j+1) tt^j/j,{j,1,60}];
appt[x_] := Join[Table[x^j,{j,0,5}],{x,x^2}(ser60/.tt->2x-1)];
matT=Round[10^25 Transpose[appt /@ xn]]/10^25;
invT=Inverse[matT]; wT=invT.rhs;
rhoT=Norm[invT,Infinity] 8(1/(61 2^60)+1/(2 10^25));
upperT=Total[Abs[wT]]+8 rhoT Norm[wT,Infinity]/(1-rhoT);
Print["tight rational-node variation certificate {lower, upper, inverse perturbation factor} = ",
 N[{Abs[First[dualT]]/supT,upperT,rhoT},17]];
Print["rounded certificate checks = ",{Abs[First[dualT]]/supT>9591531/100,upperT<96013776/1000,rhoT<1}];
