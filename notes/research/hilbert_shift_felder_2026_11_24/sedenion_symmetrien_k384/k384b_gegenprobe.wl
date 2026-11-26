(* k384b (Erkundung, Wolfram exakt): Gegenprobe zu k384. Eigene Cayley-Dickson-Multiplikation (Konvention wie k253). Ausgabe k384b_out.txt. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
ee = IdentityMatrix[16];
fam[a_, s8_] := Module[{m = ConstantArray[0, {16, 16}]}, m[[1, 1]] = 1; m[[9, 9]] = s8;
   Do[m[[i + 1, i + 1]] = a[[1, 1]]; m[[i + 1, i + 9]] = a[[1, 2]]; m[[i + 9, i + 1]] = a[[2, 1]]; m[[i + 9, i + 9]] = a[[2, 2]], {i, 7}]; m];
defect[m_] := DeleteDuplicates[Flatten[Table[m . ml[ee[[i]], ee[[j]]] - ml[m . ee[[i]], m . ee[[j]]], {i, 16}, {j, 16}]]];
(* 1. Drehung mit symbolischem (c, s), c^2 + s^2 = 1 *)
eqR = Simplify[defect[fam[{{c, -s}, {s, c}}, 1]]];
Print["Drehung, e8 -> +e8: Loesungen (c, s) = ", Solve[Join[Thread[eqR == 0], {c^2 + s^2 == 1}], {c, s}, Reals]];
eqR2 = Simplify[defect[fam[{{c, -s}, {s, c}}, -1]]];
Print["Drehung, e8 -> -e8: Loesungen = ", Solve[Join[Thread[eqR2 == 0], {c^2 + s^2 == 1}], {c, s}, Reals]];
eqS = Simplify[defect[fam[{{c, s}, {s, -c}}, -1]]];
Print["Spiegelung, e8 -> -e8: Loesungen (c, s) = ", Solve[Join[Thread[eqS == 0], {c^2 + s^2 == 1}], {c, s}, Reals]];
eqS2 = Simplify[defect[fam[{{c, s}, {s, -c}}, 1]]];
Print["Spiegelung, e8 -> +e8: Loesungen = ", Solve[Join[Thread[eqS2 == 0], {c^2 + s^2 == 1}], {c, s}, Reals]];
psi = fam[{{-1/2, -Sqrt[3]/2}, {Sqrt[3]/2, -1/2}}, 1]; eps = fam[{{1, 0}, {0, -1}}, -1];
Print["psi^3 == 1: ", MatrixPower[psi, 3] == ee, "; eps psi eps == psi^-1: ", eps . psi . eps == Transpose[psi]];
(* 2. U, J *)
u = ee[[8]]; jm = Transpose[Table[ml[u, cj[ee[[i]]]], {i, 16}]];
Print["psi U = ", psi . u, "; eps U == U: ", eps . u == u];
Print["eps J eps == J: ", eps . jm . eps == jm, "; psi J psi^-1 == J: ", Simplify[psi . jm . Transpose[psi]] == jm];
(* 3. Form mit getrennten Koeffizienten: q = Diag(a0, a7, a8, a15; c1 auf e1..e6; c2 auf e9..e14); Bedingungen aus psi und aus J *)
q = DiagonalMatrix[Join[{a0}, ConstantArray[c1, 6], {a7}, {a8}, ConstantArray[c2, 6], {a15}]];
Print["Invarianz unter psi verlangt: ", Reduce[Thread[DeleteDuplicates[Flatten[Simplify[Transpose[psi] . q . psi - q]]] == 0], {a0, a7, a8, a15, c1, c2}]];
Print["Invarianz unter J verlangt: ", Reduce[Thread[DeleteDuplicates[Flatten[Simplify[Transpose[jm] . q . jm - q]]] == 0], {a0, a7, a8, a15, c1, c2}]];
j1 = Simplify[psi . jm . Transpose[psi]];
Print["Invarianz unter psi, J und psi J psi^-1 verlangt: ", Reduce[Thread[DeleteDuplicates[Flatten[Simplify[{Transpose[psi] . q . psi - q, Transpose[jm] . q . jm - q, Transpose[j1] . q . j1 - q}]]] == 0], {a0, a7, a8, a15, c1, c2}]];
(* 4. Ladung Q0 = 1/2 - i/6 L_U - i/3 R_U auf den Bloecken *)
lu = Transpose[Table[ml[u, ee[[j]]], {j, 16}]]; ru = Transpose[Table[ml[ee[[j]], u], {j, 16}]];
q0 = IdentityMatrix[16]/2 - I/6 lu - I/3 ru;
blk[ix_] := Sort[Eigenvalues[q0[[ix, ix]]]];
Print["Q0 auf {e0, e7}: ", blk[{1, 8}], "; Block 1: ", blk[Range[2, 7]], "; {e8, e15}: ", blk[{9, 16}], "; Block 2: ", blk[Range[10, 15]]];
Print["[Q0, eps] == 0: ", q0 . eps == eps . q0];
