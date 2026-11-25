(* k324b (Test H141, Wolfram exakt): Kern der Summenabbildung Phi, Ladungs-Leck, gestauchte Ladung. Konvention wie k253. Ausgabe k324b_out.txt *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
ee = IdentityMatrix[16];
f = {{1, 0}, {-1/2, Sqrt[3]/2}, {-1/2, -Sqrt[3]/2}};
vec[a_, fk_] := Module[{v = ConstantArray[0, 16]}, v[[2 ;; 8]] = fk[[1]] a; v[[10 ;; 16]] = fk[[2]] a; v];
basis[fk_] := Join[{ee[[1]]}, Table[vec[UnitVector[7, i], fk], {i, 7}]];
B = basis /@ f;
Lm[x_] := Transpose[Table[ml[x, ee[[j]]], {j, 16}]]; Rm[x_] := Transpose[Table[ml[ee[[j]], x], {j, 16}]];
U = vec[UnitVector[7, 7], #] & /@ f;
Q = Table[IdentityMatrix[16]/2 - I/6 Lm[U[[k]]] - I/3 Rm[U[[k]]], {k, 3}];
Qc = Table[Simplify[B[[k]] . Q[[k]] . Transpose[B[[k]]]], {k, 3}];
QV = ArrayFlatten[{{Qc[[1]], 0, 0}, {0, Qc[[2]], 0}, {0, 0, Qc[[3]]}}];
Phi = Join[Transpose[B[[1]]], Transpose[B[[2]]], Transpose[B[[3]]], 2];
ker = Orthogonalize[NullSpace[Phi]];
Print["dim Kern: ", Length[ker], ", Rang Phi: ", MatrixRank[Phi]];
PK = Simplify[Transpose[ker] . ker];
Print["Ladungs-Leck exakt (Singulaerwerte): ", Sort[Simplify[SingularValueList[N[(IdentityMatrix[24] - PK) . QV . PK, 30]]]]];
Print["Spektrum P_K Q_V P_K exakt: ", Sort[Simplify[Eigenvalues[Simplify[ker . QV . Transpose[ker]]]]]];
Print["[Q_V, P_K] == 0 ? ", Simplify[QV . PK - PK . QV] == ConstantArray[0, {24, 24}]];
