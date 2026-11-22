ClearAll[realify, reflect, projector, rvec, v, g, u, n, ni, d, jPhase, cN, cNi];
realify[m_] := ArrayFlatten[{{Re[m], -Im[m]}, {Im[m], Re[m]}}];
rvec[w_] := Join[Re[w], Im[w]];
reflect[w_] := IdentityMatrix[Length[w]] - 2 Outer[Times, w, w]/(w.w);
projector[j_] := (IdentityMatrix[Length[j]] + j)/2;
v = Transpose[{{1, 1}/Sqrt[2], {1, I}/Sqrt[2], {1, 0}}];
g = FullSimplify[ConjugateTranspose[v].v];
u = {-I, 1, -(1 - I)/Sqrt[2]};
n = rvec[u];
ni = rvec[I u];
d = realify[v];
jPhase = realify[I IdentityMatrix[3]];
cN = projector[reflect[n]];
cNi = projector[reflect[ni]];
Print["Wolfram: ", $Version];
Print["Bargmann triple product, Gram rank, kernel residual: ",
  InputForm[{FullSimplify[g[[1, 2]] g[[2, 3]] g[[3, 1]]], MatrixRank[g], FullSimplify[g.u]}]];
Print["Oktant rank and real null pair check: ",
  {MatrixRank[d], FullSimplify[d.n == d.ni == ConstantArray[0, 4]], FullSimplify[n.ni]}];
Print["Odd input rank, antiunitary representative rank, complex-linear projection ranks: ",
  {MatrixRank[projector[-IdentityMatrix[6]]],
   MatrixRank[projector[DiagonalMatrix[{1, 1, 1, -1, -1, -1}]]],
   Table[MatrixRank[projector[realify[DiagonalMatrix[Join[ConstantArray[1, k],
      ConstantArray[-1, 3-k]]]]]], {k, 0, 3}]}];
Print["Selective projectors: ranks, lost half, preserved half, factorization: ",
  {MatrixRank[cN], MatrixRank[cNi],
   FullSimplify[cN.n == cNi.ni == ConstantArray[0, 6]],
   FullSimplify[cN.ni == ni && cNi.n == n],
   FullSimplify[d.cN == d.cNi == d]}];
Print["Quarter-turn exchanges the two choices: ",
  FullSimplify[jPhase.cN.Transpose[jPhase] == cNi]];
ambient = Transpose[{{1, I, 0, 0, 0}/Sqrt[2], {0, 0, 1, I, 0}/Sqrt[2], {0, 0, 0, 0, 1}}];
ambientOut = Take[realify[ambient], 5];
Print["Supplementary ambient conjugation, rank and kernel: ",
  {MatrixRank[ambientOut], NullSpace[ambientOut]}];
