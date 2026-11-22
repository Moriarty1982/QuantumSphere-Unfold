ClearAll[z, a, m, g, color, neutral, diag, cyc, newDiag, mats, traceMap];
z = (-1 + I Sqrt[3])/2;
m = IdentityMatrix[3];
a = IdentityMatrix[4];
cyc = {{0, 0, 1}, {1, 0, 0}, {0, 1, 0}};
g = KroneckerProduct[m, DiagonalMatrix[{z, z, z, 1}]];
color = Transpose[Flatten[Table[Flatten[Outer[Times, m[[i]], a[[j]]]], {i, 3}, {j, 3}], 1]];
neutral = Transpose[Table[Flatten[Outer[Times, m[[i]], a[[4]]]], {i, 3}]];
diag = Transpose[Table[Flatten[Outer[Times, m[[i]], a[[i]]]], {i, 3}]];
newDiag = KroneckerProduct[m, ArrayFlatten[{{cyc, ConstantArray[0, {3, 1}]},
    {ConstantArray[0, {1, 3}], {{1}}}}]].diag;
mats = Table[Outer[Times, m[[i]], m[[j]]], {i, 3}, {j, 3}];
traceMap = {Tr /@ Flatten[mats, 1]};
Print["Wolfram: ", $Version];
Print["Center nontrivial, unitary, determinant one: ", {Re[z] != 1, Expand[Conjugate[z] z] === 1, Expand[z^3] === 1}];
Print["Rank of (center-I) on colored block and neutral block: ",
  {MatrixRank[FullSimplify[(g - IdentityMatrix[12]).color]],
   MatrixRank[FullSimplify[(g - IdentityMatrix[12]).neutral]]}];
Print["Rank of (center-I) on literal diagonal: ",
  MatrixRank[FullSimplify[(g - IdentityMatrix[12]).diag]]];
Print["Farbzyklus: Det, residual against unitarity, overlap with old diagonal: ",
  {Det[cyc], Transpose[cyc].cyc - m, Transpose[diag].newDiag}];
Print["Dual pairing: trace on E11,E22,E33 and trace rank: ",
  {Tr /@ Table[mats[[i, i]], {i, 3}], MatrixRank[traceMap]}];
Print["Dual pairing: trace defect for cyclic conjugation on nine matrix units: ",
  Union[Tr[cyc.#.Transpose[cyc]] - Tr[#] & /@ Flatten[mats, 1]]];
Print["Dual pairing with independent generations: rank ",
  MatrixRank[KroneckerProduct[m, traceMap]]];
