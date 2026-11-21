Print["Kernel: ", $Version];
v = {vA, vJ}; x = {xA, xJ};
Print["passive candidate mapping residual = ",
 Together[Outer[Times,x,Conjugate[v]].v/(Conjugate[v].v) - x]];
rMax = 3512/10^9; jMax = 317/10^5;
amp = 1/50; uNormMax = 1;
diagJBound = jMax + rMax uNormMax/(1-rMax);
requiredJ = Sqrt[3] amp/2;
Print["diagonal J maximum and triangle requirement = ", N[{diagJBound, requiredJ}, 14]];
Print["general mixing sufficient radius for norm 0.99 = ", N[(99/100)/(1+rMax), 14]];
eps = 1/10^8; minor = 3/1000;
ellipError = 2 eps/(1-Sqrt[2] eps/minor);
Print["illustrative elliptic measurement error = ", N[ellipError, 14]];

hbarc = 1973269804/10^16; e0 = 360329/10^6; half100 = 2067833848/10^16;
mass2 = e0^2 (1-(9999/10000)^2);
g[e_] := (Sqrt[e^2-mass2]-e)/hbarc;
diff[b_] := g[e0+b half100]-g[e0-b half100];
phaseErr = 2 ArcSin[1/10000]+2/10^6;
Print["baseline criteria in m, centered and uniform = ", N[{2,4} phaseErr/diff[1], 14]];
widthRatio[n_] := b /. FindRoot[N[diff[b]/100-n phaseErr, 38] == 0, {b, N[100 n, 38]}, WorkingPrecision -> 35];
Print["bandwidth criteria in GHz at one cm = ", N[{widthRatio[2],widthRatio[4]}/10, 12]];
Print["cm anchor condition at four m = ", N[(400+1) phaseErr, 12]];
q1 = Outer[Times, {-e, j}, {-e,j}];
kk = {{ka,kaj},{kaj,kj}};
Print["rank-one determinant residual = ", Expand[Det[q1]]];
qs = {{2/3, 1/Sqrt[3]}, {-1/3, 1/Sqrt[3]}, {0,1/Sqrt[3]}, {-1,1/Sqrt[3]}};
thresholds = Total[MapThread[#1 Outer[Times,#2,#2] &, {{3,3,1,1},qs}]];
Print["equal-weight counterexample residual = ", FullSimplify[thresholds - (8/3) IdentityMatrix[2]]];
electronNu = we q1 + wn DiagonalMatrix[{0,j^2}];
align = electronNu - (we e^2/ka) kk;
Print["electron-neutrino mixed and J diagonal alignment residuals = ",
 Together[{align[[1,2]],align[[2,2]]} /. {kaj -> -ka j/e, kj -> ka (j/e)^2 (1+wn/we)}]];
