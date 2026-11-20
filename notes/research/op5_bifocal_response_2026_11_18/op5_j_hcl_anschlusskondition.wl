ClearAll["Global`*"];
Print["Wolfram kernel version = ", $Version];

assumptions = Element[{a,b,p,q,uR,uI,vR,vI,t}, Reals];
direction = {{1,p},{0,q}};
gain = DiagonalMatrix[{a,b}];
overlap = {{1,uR+I uI},{vR+I vI,1}};
transmit = direction.gain.overlap;
gram = ConjugateTranspose[transmit].transmit;
traceExpected = a^2 (1+uR^2+uI^2) + b^2 (1+vR^2+vI^2) +
  2 a b p (uR+vR);
detExpected = a^2 b^2 q^2 Abs[1-(uR+I uI)(vR+I vI)]^2;
Print["complex overlap trace residual (unit vectors) = ",
  FullSimplify[Tr[gram]-traceExpected, assumptions && p^2+q^2==1]];
Print["complex overlap determinant residual = ",
  FullSimplify[Det[gram]-detExpected, assumptions]];
idealGram = Transpose[direction.gain].(direction.gain);
thresholdDet = b^2 (a^2 q^2-t^2)-t^2(a^2-t^2);
Print["ideal shifted Gram determinant residual = ",
  FullSimplify[Det[idealGram-t^2 IdentityMatrix[2]]-thresholdDet,
    assumptions && p^2+q^2==1]];

sigmaMin[m_] := Module[{trace,det},
  trace = Total[Abs[Flatten[m]]^2];
  det = Abs[Det[m]]^2;
  If[trace==0, 0, Sqrt[2 det/(trace+Sqrt[trace^2-4 det])]]
];
sample = transmit /. {a->1,b->1/5,p->3/5,q->4/5,uR->1/10,uI->0,vR->0,vI->1/20};
Print["complex sample minimum singular value = ", N[sigmaMin[sample],10]];
Print["complex sample direct SVD residual = ",
  ScientificForm[Abs[sigmaMin[sample]-Last[SingularValueList[N[sample,50]]]],3]];
Print["equal-gain orthogonal case = ", sigmaMin[IdentityMatrix[2]]];
Print["singular overlap and zero gain cases = ",
  {sigmaMin[{{1,1},{1,1}}],sigmaMin[DiagonalMatrix[{1,0}]]}];

radial[r_] := r+r^2/2;
Print["hydrogen first-order radial equation residual = ",
  FullSimplify[-(D[radial[r],{r,2}]+(2/r-2) D[radial[r],r]-2 radial[r]/r^2)/2-r,
    r>0]];
alphaH = 8/3 Integrate[r^3 radial[r] Exp[-2r],{r,0,Infinity}];
Print["hydrogen static polarizability [a.u., infinite nuclear mass] = ",alphaH];
dipoleAU = (719426/10^7) (333564/10^5)/(84783536198/10^10)/Sqrt[3];
hartreeEV = 27211386245981/10^12;
coefficientEV = dipoleAU^2 hartreeEV/alphaH;
Print["polarized HCl electric transition dipole [a.u.] = ", N[dipoleAU,8]];
Print["HCl/H strength coefficient [eV], before population and overlap = ",
  N[coefficientEV,8]];

hSlope = -1+4/1824;
clSlopeSigns = {153875/100000,-353491/100000};
angleSine[k_, slope_] := Abs[k (slope-hSlope)]/
  Sqrt[(1+(k hSlope)^2)(1+(k slope)^2)];
requiredGain[tau_, sine_] := tau Sqrt[(1-tau^2)/(sine^2-tau^2)];
Print["angle sines for g/e=1, two signs = ", N[angleSine[1,#]& /@ clSlopeSigns,8]];
Print["angle sines for g/e=0.001, two signs = ",
  N[angleSine[1/1000,#]& /@ clSlopeSigns,8]];
Print["minimum b/a for sigmaMin/a=0.1 without overlap, g/e=1 = ",
  N[requiredGain[1/10,angleSine[1,#]]& /@ clSlopeSigns,8]];
