ClearAll["Global`*"];
Print["kernel version = ", $Version];

(* The inverse in the pencil is removed before checking its residual. *)
noiseA = {{a11,a12},{a21,a22}};
noiseB = {{b11,b12},{b21,b22}};
unitary = DiagonalMatrix[{z1,z2}];
Print["weighted pencil residual = ",
  Expand[unitary+noiseB-(IdentityMatrix[2]+noiseA).unitary-(noiseB-noiseA.unitary)]];
Print["endpoint drift expansion residual = ",
  Expand[(IdentityMatrix[2]+noiseA).unitary.(IdentityMatrix[2]+noiseB)-
    unitary-noiseA.unitary-unitary.noiseB-noiseA.unitary.noiseB]];

(* Tangency from the origin to the radius-r disk about 1. *)
tangent = 1-r^2+I r Sqrt[1-r^2];
conditions = Element[r,Reals] && 0<r<1;
Print["phase disk tangency residuals = ",
  FullSimplify[{Abs[tangent-1]^2-r^2, Im[tangent]/Abs[tangent]-r},conditions]];

rotation = {{3/5,-4/5},{4/5,3/5}};
u = rotation.DiagonalMatrix[{1,I}].Transpose[rotation];
na = {{0,1/1000},{-I/2000,0}};
nb = {{1/800,I/1600},{0,-1/900}};
weighted = LinearSolve[IdentityMatrix[2]+na,u+nb];
opNorm[m_] := First[SingularValueList[N[m,40]]];
bound = (opNorm[na]+opNorm[nb])/(1-opNorm[na]);
eig = Eigenvalues[N[weighted,40]];
Print["sample norm error and bound = ", N[{opNorm[weighted-u],bound},8]];
Print["sample matched chord errors = ",
  N[Min /@ Transpose[Table[Abs[ev-exact],{ev,eig},{exact,{1,I}}]],8]];
Print["sample checks = ", {opNorm[weighted-u]<=bound, Max[Min /@
  Transpose[Table[Abs[ev-exact],{ev,eig},{exact,{1,I}}]]]<=bound, 2 bound<Abs[1-I]}];

bandwidthHz = 10^8;
delayToleranceSeconds = 1/(4 10^12);
splitRad = 1/10;
radius = Min[Sin[splitRad/2],Sin[2 Pi bandwidthHz delayToleranceSeconds/4]];
errorEach = 1/10^8;
minimumProduct[drift_] := ((1+radius) errorEach+errorEach)/(radius-drift);
maxSine = 25370859/10^10;
hclGainProductCeiling = maxSine^2;
maxMatrixError = hclGainProductCeiling radius/(2+radius);
Print["illustrative allowed radius = ", N[radius,8]];
Print["minimum gain products for drift 0, 0.00001 = ",
  N[minimumProduct /@ {0,1/10^5},8]];
Print["equal end gains for drift 0, 0.00001 = ",
  N[Sqrt[minimumProduct[#]]& /@ {0,1/10^5},8]];
Print["HCl/H illustrative gain product ceiling and equal error ceiling = ",
  N[{hclGainProductCeiling,maxMatrixError},8]];
