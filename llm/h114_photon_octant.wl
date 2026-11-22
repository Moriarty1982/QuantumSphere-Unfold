ClearAll[gram, minors, phi, r, photon, endpoint, realify, p5, p4, j, lminus, lplus];
gram[q_] := {{1, 1/Sqrt[2], Conjugate[q]/Sqrt[2]},
  {1/Sqrt[2], 1, 1/Sqrt[2]}, {q/Sqrt[2], 1/Sqrt[2], 1}};
minors[m_] := Table[Union[FullSimplify[Det[m[[#, #]]] & /@
   Subsets[Range[Length[m]], {k}]]], {k, Length[m]}];
photon = IdentityMatrix[2]/2;
endpoint = gram[(1 + I)/Sqrt[2]];
Print["Wolfram: ", $Version];
Print["Photon density rank and spectrum: ", InputForm[{MatrixRank[photon], Eigenvalues[photon]}]];
Print["Equal overlap squares for both phases: ", InputForm[Function[g, FullSimplify[Abs[#]^2 & /@ {g[[1, 2]], g[[2, 3]], g[[3, 1]]}]] /@ {gram[1], endpoint}]];
Print["Principal minors at Gram phase 0: ", InputForm[minors[gram[1]]]];
Print["Principal minors at Gram phase Pi/4: ", InputForm[minors[endpoint]]];
Print["Two allowed Gram ranks for same P data: ",
  {MatrixRank[FullSimplify[gram[1]]], MatrixRank[FullSimplify[endpoint]]}];
Print["General Gram determinant residual: ",
  FullSimplify[Det[gram[Exp[I phi]]] - (Sqrt[2] Cos[phi] - 1)/2,
    Element[phi, Reals]]];
Print["Bures identification determinant residual on 0 <= r <= 1: ",
  FullSimplify[(Sqrt[2] Cos[ArcCos[r]/2] - 1)/2 - (Sqrt[1 + r] - 1)/2,
    0 <= r <= 1]];
Print["Conditional determinant / r, limit from above: ",
  Limit[1/(2 (Sqrt[1 + r] + 1)), r -> 0, Direction -> "FromAbove"]];
realify[m_] := ArrayFlatten[{{Re[m], -Im[m]}, {Im[m], Re[m]}}];
Print["Underlying real Gram ranks: ",
  {MatrixRank[realify[gram[1]]], MatrixRank[realify[endpoint]]}];
j = KroneckerProduct[IdentityMatrix[3], {{0, -1}, {1, 0}}];
p5 = DiagonalMatrix[{1, 1, 1, 1, 1, 0}];
p4 = DiagonalMatrix[{1, 1, 1, 1, 0, 0}];
Print["Five/four projections: ranks and commutator ranks with J: ",
  {MatrixRank[p5], MatrixRank[p4], MatrixRank[p5.j - j.p5],
   MatrixRank[p4.j - j.p4], p4.p5 == p4}];
lminus = -IdentityMatrix[5];
lplus = DiagonalMatrix[{-1, -1, -1, -1, 1}];
Print["Invariant four-plane common spectrum: ",
  Eigenvalues[lminus[[1 ;; 4, 1 ;; 4]]]];
Print["Five-space spectra: ", {Eigenvalues[lminus], Sort[Eigenvalues[lplus]]}];
Print["Invariant plane and equal plane dynamics for both generators: ",
  {lminus[[5, 1 ;; 4]] == lplus[[5, 1 ;; 4]] == ConstantArray[0, 4],
   lminus[[1 ;; 4, 1 ;; 4]] == lplus[[1 ;; 4, 1 ;; 4]]}];
