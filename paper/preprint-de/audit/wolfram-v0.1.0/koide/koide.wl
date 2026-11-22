(* Independent exact audit of section 3, Quantum Sphaera Preprint 0.1.0. *)
ClearAll["Global`*"];
checks = {};
check[label_, statement_] := (AppendTo[checks, {label, TrueQ[statement]}]; Print[label, ": ", If[TrueQ[statement], "PASS", "FAIL"]]);
same[a_, b_] := TrueQ[FullSimplify[a - b] === 0];
zero[a_] := And @@ (same[#, 0] & /@ Flatten[{a}]);
ratio[v_] := (v.v)/Total[v]^2;
Print["Kernel: ", $Version];

roots = {x1, x2, x3}; mean = Total[roots]/3; dev = roots - mean;
check["eq:koide constant-deviation orthogonality", zero[Total[dev]]];
check["eq:equal-norm Koide decomposition", same[ratio[roots], 1/3 + dev.dev/(9 mean^2)]];
check["eq:equal-norm benchmarks and scale", ratio[{1, 2, 3}] == 7/18 && ratio[{2, 2, 2}] == 1/3 && same[ratio[sc roots], ratio[roots]]];
fwc = Cos[2 Pi Range[0, 2]/3]; fws = Sin[2 Pi Range[0, 2]/3];
check["eq:koide-radius-phase Fourier orthogonality", fwc.fws == 0 && fwc.fwc == 3/2 && fws.fws == 3/2 && Total[fwc] == Total[fws] == 0];
phaseRoots[angle_, radius_] := aa (1 + radius (Cos[angle] fwc - Sin[angle] fws));
check["eq:koide-radius-phase radius identity", same[ratio[phaseRoots[theta, rad]], 1/3 + rad^2/6]];
boundaryRoots = RootReduce[phaseRoots[Pi/12, Sqrt[2]]/aa];
outsideRoots = RootReduce[phaseRoots[Pi/6, Sqrt[2]]/aa];
check["Principal roots beyond the positive arc change Koide", And @@ Thread[boundaryRoots >= 0] && MemberQ[boundaryRoots, 0] && Min[outsideRoots] < 0 && !same[ratio[Abs[outsideRoots]], 2/3]];

ee = {1, 1, 1}/Sqrt[3]; vv = {2, -1, -1}/Sqrt[6]; id = IdentityMatrix[3];
swap = id - Outer[Times, ee - vv, ee - vv]; proj = (id + swap)/2;
check["eq:hc-criterion swap orthogonal involution", zero[Transpose[swap].swap - id] && zero[swap.swap-id] && zero[swap.ee-vv] && zero[swap.vv-ee]];
check["eq:hc-criterion projector and example spectrum", zero[proj.proj-proj] && zero[proj.ee - {1+Sqrt[2],1-1/Sqrt[2],1-1/Sqrt[2]}/(2 Sqrt[3])] && same[ratio[proj.ee],2/3]];
check["eq:hc-criterion scalar reduction conditional on h > -1", same[(1+hh)/2/(3 ((1+hh)/2)^2), 2/(3 (1+hh))]];
bm = ArrayFlatten[{{id, ConstantArray[0,{3,1}]}}];
jbig=ArrayFlatten[{{swap, ConstantArray[0,{3,1}]},{ConstantArray[0,{1,3}],{{-1}}}}];
cbig=(IdentityMatrix[4]+jbig)/2;
check["HC coisometry benchmark (dimension 4 to 3)", zero[bm.Transpose[bm]-id] && zero[bm.jbig.Transpose[bm]-swap] && zero[bm.cbig-proj.bm] && zero[cbig.{0,0,0,1}]];

u12 = ur + I ui; u13 = vr + I vi; u23 = wr + I wi;
generalGram = {{1,u12,u13},{ur-I ui,1,u23},{vr-I vi,wr-I wi,1}};
check["eq:overlap generic unit diagonal Hermitian Gram", Tr[generalGram] == 3 && same[Tr[generalGram.generalGram],3+2 (ur^2+ui^2+vr^2+vi^2+wr^2+wi^2)]];
check["eq:overlap Koide condition", same[(3+6 rr)/9-2/3,(2 rr-1)/3]];
cyc={{0,1,0},{0,0,1},{1,0,0}};
g[zz_] := id + (zz cyc + Transpose[cyc]/zz)/Sqrt[2];
om=(-1+I Sqrt[3])/2;
fv[k_] := om^(k Range[0,2]);
eigen[z_, k_] := 1 + (z om^k + (z om^k)^(-1))/Sqrt[2];
check["eq:koide-gram-spectrum Fourier diagonalization (all three columns)", And @@ Table[zero[g[z].fv[k]-eigen[z,k] fv[k]],{k,0,2}]];
check["eq:koide-gram-spectrum normalized mean and norm", same[Tr[g[z]],3] && same[Tr[g[z].g[z]],6]];
check["Bargmann phase and its rephasing invariance", same[g[z][[1,2]] g[z][[2,3]] g[z][[3,1]],z^3/(2 Sqrt[2])] && same[Exp[I (be-al)] Exp[I (ga-be)] Exp[I (al-ga)],1]];
check["eq:det determinant and all second principal minors",same[Det[g[z]],(Sqrt[2] (z^3+z^(-3))/2-1)/2] && And @@ (same[Det[g[z][[#,#]]],1/2] & /@ Subsets[Range[3],{2}])];
check["eq:det threshold in principal phase interval", same[(Sqrt[2] Cos[Pi/4]-1)/2,0] && (Sqrt[2] Cos[0]-1)/2 >0 && (Sqrt[2] Cos[Pi/2]-1)/2<0];
kSpectrum[p_] := 1+Sqrt[2] Cos[p/3+2 Pi Range[0,2]/3];
check["Interior strict ordering and sign symmetry", zero[TrigExpand[Differences[kSpectrum[3 theta][[{2,3,1}]]] - Sqrt[6] {Sin[theta], Sin[Pi/3-theta]}]] && zero[TrigExpand[kSpectrum[-3 theta] - kSpectrum[3 theta][[{1,3,2}]]]]];
check["Reference and octant endpoint eigenvalues and rank", zero[kSpectrum[0]-{1+Sqrt[2],1-1/Sqrt[2],1-1/Sqrt[2]}] && zero[kSpectrum[Pi/4]-{(3+Sqrt[3])/2,0,(3-Sqrt[3])/2}] && MatrixRank[RootReduce[g[Exp[I Pi/12]]]]==2];
oct = Transpose[{{1,0},{1,1}/Sqrt[2],{1,I}/Sqrt[2]}]; go=ConjugateTranspose[oct].oct;
check["Bloch-octant direct C^2 Gram and oriented product", zero[Diagonal[go]-{1,1,1}] && zero[Abs[{go[[1,2]],go[[2,3]],go[[3,1]]}]^2-1/2] && same[go[[1,2]]go[[2,3]]go[[3,1]],(1+I)/4] && MatrixRank[go]==2];

check["eq:koide-mixture root average", zero[(phaseRoots[theta+half,Sqrt[2]]+phaseRoots[theta-half,Sqrt[2]])/2-phaseRoots[theta,Sqrt[2] Cos[half]]]];
check["eq:koide-mixture averaged K and mass variance", same[ratio[phaseRoots[theta,Sqrt[2] Cos[half]]],(1+Cos[half]^2)/3] && same[(xp^2+xm^2)/2,((xp+xm)/2)^2+(xp-xm)^2/4]];
mA={{1,I},{2,1-I}}; mB={{1+I,3},{I,-1}}; hhPhase=Exp[I phase];
mat=mA+hhPhase mB;
check["Coherent cross terms and common phase cancellation", zero[ComplexExpand[ConjugateTranspose[mat].mat-ConjugateTranspose[mA].mA-ConjugateTranspose[mB].mB-hhPhase ConjugateTranspose[mA].mB-Exp[-I phase] ConjugateTranspose[mB].mA]] && zero[ComplexExpand[ConjugateTranspose[hhPhase mA].(hhPhase mA)-ConjugateTranspose[mA].mA]]];

block={{0,mu sig},{mu sig,gap}};
check["eq:gap characteristic equation at negative eigenvalue", same[Det[block+mass IdentityMatrix[2]],mass (mass+gap)-mu^2 sig^2]];
vlight={1,-mu sig/(gap+mass)};
check["eq:gap light eigenvector direction", zero[Expand[(block+mass IdentityMatrix[2]).vlight] /. mu^2 sig^2 -> mass (mass+gap)]];
check["eq:gap normalized heavy probability", same[(mu^2 sig^2/((gap+mass)^2+mu^2 sig^2)) /. mu -> Sqrt[mass (mass+gap)]/sig,mass/(gap+2 mass)]];
mexact[gg_, eta_, qq_] := gg (Sqrt[1+4 eta^2 qq]-1)/2;
check["eq:koide-scale-gap positive light mass and uniform scaling", same[mexact[gap,eta,q] (mexact[gap,eta,q]+gap),eta^2 gap^2 q] && same[mexact[sc gap,eta,q],sc mexact[gap,eta,q]] && TrueQ[FullSimplify[mexact[gap,eta,q]>0,gap>0 && eta>0 && q>0]]];
check["eq:koide-scale-gap weak-mixing coefficient", same[SeriesCoefficient[mexact[gap,eta,q],{eta,0,2}],gap q]];
check["eq:koide-scale-gap shape depends on eta for unequal singular values", !same[mexact[1,1,1]/mexact[1,1,4],mexact[1,2,1]/mexact[1,2,4]]];
Print["COUNTS: ", Count[checks,{_,True}],"/",Length[checks]," passed"];
Print["FAILED: ", Cases[checks,{label_, False}:>label]];
