(* k323b (Test H140, Wolfram exakt): Leck von L_x, R_x aus den drei Kopien fuer symbolisches x in Im S; psi Q0 psi^-1 vs Q0; Dimension.
   Konvention wie k253. Ausgabe k323b_out.txt. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
ee = IdentityMatrix[16];
xs = Join[{0}, Array[x, 15]];
Lx = Transpose[Table[ml[xs, ee[[j]]], {j, 16}]];
Rx = Transpose[Table[ml[ee[[j]], xs], {j, 16}]];
f = {{1, 0}, {-1/2, Sqrt[3]/2}, {-1/2, -Sqrt[3]/2}};
basis[fk_] := Join[{ee[[1]]}, Table[Module[{v = ConstantArray[0, 16]}, v[[i + 1]] = fk[[1]]; v[[i + 9]] = fk[[2]]; v], {i, 7}]];
proj = Table[Transpose[basis[f[[k]]]] . basis[f[[k]]], {k, 3}];
leak[M_] := Total[Table[Total[Flatten[((IdentityMatrix[16] - proj[[k]]) . M . proj[[k]])^2]], {k, 3}]];
Print["Leck(L_x) = ", Factor[Simplify[leak[Lx]]]];
Print["Leck(R_x) = ", Factor[Simplify[leak[Rx]]]];
Print["Kreuzterm = ", Factor[Simplify[Total[Table[Total[Flatten[((IdentityMatrix[16] - proj[[k]]) . Lx . proj[[k]]) ((IdentityMatrix[16] - proj[[k]]) . Rx . proj[[k]])]], {k, 3}]]]]];
psi = IdentityMatrix[16]; c = -1/2; s = Sqrt[3]/2;
Do[psi[[i + 1, i + 1]] = c; psi[[i + 9, i + 9]] = c; psi[[i + 1, i + 9]] = -s; psi[[i + 9, i + 1]] = s, {i, 7}];
u0 = ee[[8]];
L0 = Transpose[Table[ml[u0, ee[[j]]], {j, 16}]]; R0 = Transpose[Table[ml[ee[[j]], u0], {j, 16}]];
Q0 = IdentityMatrix[16]/2 - I/6 L0 - I/3 R0;
Print["psi Q0 psi^-1 - Q0 == 0 ? ", Simplify[psi . Q0 . Transpose[psi] - Q0] == ConstantArray[0, {16, 16}], "; max Betrag: ", Max[Abs[N[psi . Q0 . Transpose[psi] - Q0]]]];
Print["dim Summe der Kopien: ", MatrixRank[Join @@ (basis /@ f)]];
