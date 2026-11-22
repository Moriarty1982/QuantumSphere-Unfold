ClearAll["Global`*"];
Print["Kernel: ", $Version, " | ", $SystemID];
results = {};
check[label_, residual_] := Module[{r, ok},
  r = FullSimplify[residual];
  ok = And @@ (TrueQ[# == 0] & /@ Flatten[{r}]);
  AppendTo[results, ok]; Print[label, ": ", If[ok, "PASS", "FAIL"], " residual = ", InputForm[r]];
];

cp[j_] := (1+j)/2;
pm[j_] := (1-j)/2;
check["HC polynomial identities modulo J^2-I",
  Last[PolynomialReduce[#, {j^2-1}, j]] & /@
    {cp[j]^2-cp[j], pm[j]^2-pm[j], cp[j] pm[j], cp[j]+pm[j]-1,
     j cp[j]-cp[j], j pm[j]+pm[j]}];

ee=Array[el,3]; bb=Array[mag,3];
z=ee+I bb; swap[w_]:=I Conjugate[w]; hc[w_]:=(w+swap[w])/2;
anti[w_]:=(w-swap[w])/2;
fieldForm[w_]:=w.w;
check["Generic field ports and bilinear invariant",
 ComplexExpand[{swap[z]-(bb+I ee),hc[z]-(1+I)(ee+bb)/2,
   anti[z]-(1-I)(ee-bb)/2,fieldForm[z]-(ee.ee-bb.bb+2 I ee.bb),
   fieldForm[swap[z]]+Conjugate[fieldForm[z]],fieldForm[I z]+fieldForm[z]}]];
plane=amp {1,I,0};
check["Plane wave, its output invariants and port norms",
 ComplexExpand[{fieldForm[plane], fieldForm[hc[plane]]-I amp^2,
   fieldForm[anti[plane]]+I amp^2,hc[plane]+anti[plane]-plane,
   Conjugate[plane].plane-2 amp^2,Conjugate[hc[plane]].hc[plane]-amp^2,
   Conjugate[anti[plane]].anti[plane]-amp^2}]];
gg=Transpose[{ee,bb}].{Transpose[{ee,bb}][[1]],Transpose[{ee,bb}][[2]]};
gram={ee,bb}.Transpose[{ee,bb}]; energy=Tr[gram]/2;
stokes={ee.ee-bb.bb,2 ee.bb};
check["Field Gram disk numerator and area identity",
  Expand[{stokes.stokes+4 Det[gram]-4 energy^2,
    Det[gram]-Cross[ee,bb].Cross[ee,bb]}]];
rot=Array[rr,{3,3}];
check["Transposed Lorentz norm obligation and transported exchange",
  Expand[fieldForm[rot.z]-fieldForm[z]-z.(Transpose[rot].rot-IdentityMatrix[3]).z]];
check["Order of complex field transport and exchange",
  Expand[rot.swap[z]-swap[rot.z]-I (rot-Conjugate[rot]).Conjugate[z]]];

basis=Prepend[Table[-I PauliMatrix[k],{k,3}],IdentityMatrix[2]];
quat[v_]:=Total[MapThread[Times,{v,basis}]];
qq=Array[qc,4]; pp=Array[pc,4];
qb=quat[qq]; qp=quat[pp];
bar=quat[qq {1,-1,-1,-1}];
check["Biquaternion norm and product on the ambient algebra",
 Expand[{qb.bar-(qq.qq) IdentityMatrix[2],
   Det[qb]-(qq.qq), Det[qb.qp]-Det[qb] Det[qp]}]];
check["Restricted scalar coordinate it",
 Expand[Det[quat[{I t,z1,z2,z3}]]-(-t^2+z1^2+z2^2+z3^2)]];
spinor[a_,b_]:={a^2-b^2,I (a^2+b^2),-2 a b};
sp=spinor[aa,bb0];
check["Null spinor map, inverse coordinates and sample",
 Expand[{sp.sp,(sp[[1]]-I sp[[2]])/2-aa^2,-(sp[[1]]+I sp[[2]])/2-bb0^2,
    -sp[[3]]/2-aa bb0,spinor[Sqrt[amp],0]-plane}]];
check["Null lifting compatibility for either nonzero square",
 Expand[((z1-I z2)/2)(-(z1+I z2)/2)-(-z3/2)^2+(z1^2+z2^2+z3^2)/4]];

Pc=DiagonalMatrix[{1,1,1,0}];
T0=Transpose[{{1/Sqrt[2],0,0,1/Sqrt[2]},{0,1,0,0},{0,0,1,0}}];
A0=ConjugateTranspose[T0].Pc.T0;
invroot=DiagonalMatrix[(1/Sqrt[#]&)/@Diagonal[A0]];
seed=Pc.T0.invroot;
check["Exact nontrivial closure seed, isometry and image",
 {ConjugateTranspose[T0].T0-IdentityMatrix[3],ConjugateTranspose[seed].seed-IdentityMatrix[3],Pc.seed-seed}];
rp=Array[rc,{4,4}]; bperp=(IdentityMatrix[4]-Pc).rp.seed;
comm=rp.Pc-Pc.rp;
check["Generic defect residual and vanishing expectation on sample closed states",
 Expand[{comm.seed-bperp,ConjugateTranspose[seed].comm.seed}]];
rankone=ConstantArray[1/3,{3,3}];
ko[x_]:=Total[x^2]/Total[x]^2;
check["Rank-one comparison, characteristic polynomial and distinct K",
 {CharacteristicPolynomial[rankone,l]-l^2(l-1),ko[Sqrt[Diagonal[rankone]]]-1/3,
  ko[Sqrt[Eigenvalues[rankone]]]-1}];

swap2={{0,1},{1,0}}; c2=(IdentityMatrix[2]+swap2)/2; g2=DiagonalMatrix[{1,0}];
check["Counterexample to autonomous HC readout, exact sample",
 {c2.{1,-1},c2.g2.{1,-1}-{1/2,1/2}}];
tm={{1,t}}; rm={{1},{0}}; zker={-t,1}; gmat=Array[g,{2,2}];
u0=rm.{r0}+b0 zker;
readDerivative=D[tm,t]+tm.gmat;
check["Time-dependent readout, exact parametrized 2-to-1 model",
 Expand[{tm.u0-{r0},tm.zker,readDerivative.u0-readDerivative.rm.{r0}-b0 readDerivative.zker}]];
uu={{1,t},{0,1}}; av=Array[al,{2,2}]; ps={f1[t],f2[t]};
avNew=uu.av.Inverse[uu]-D[uu,t].Inverse[uu];
check["Local gauge law, general connection and one time-dependent matrix",
 Expand[D[uu.ps,t]+avNew.(uu.ps)-uu.(D[ps,t]+av.ps)]];
ell={{1,0},{1,1},{0,2}}; it=PseudoInverse[ell];
check["Full-column source reduction, compatible and incompatible examples",
 {(IdentityMatrix[3]-ell.it).ell,it.ell-IdentityMatrix[2],
  (IdentityMatrix[3]-ell.it).{0,0,1}-{2/9,-2/9,1/9}}];
sym={{a11,a12,a13},{a12,a22,a23},{a13,a23,a33}}; xi={x1,x2,x3}; bet={b1,b2,b3};
symmetrizer=ArrayFlatten[{{{{1}},ConstantArray[0,{1,3}]},{ConstantArray[0,{3,1}],sym}}];
principal=-(bet.xi) IdentityMatrix[4]+lapse ArrayFlatten[{{{{0}},{sym.xi}},{Transpose[{xi}],ConstantArray[0,{3,3}]}}];
check["Cartan subsidiary principal-symbol symmetrizer conditional on positive slice metric",
 Expand[symmetrizer.principal-Transpose[symmetrizer.principal]]];
coframe={{1,a,0,0},{0,1,b,0},{0,0,1,c},{0,0,0,2}};
check["Coframe determinant, exact symbolic triangular family",
 Expand[Det[Transpose[coframe].DiagonalMatrix[{-1,1,1,1}].coframe]+Det[coframe]^2]];
Print["SUMMARY: ", Count[results,True], "/", Length[results], " checks passed"];
And@@results
