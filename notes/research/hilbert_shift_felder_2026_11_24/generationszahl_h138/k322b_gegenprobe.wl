(* k322b (Test H139, Wolfram-Gegenprobe, exakt): Basis-Diagonal-Nullteiler von S, ihr Kopienprofil, det L_x entlang einer Familie.
   Konvention wie k253. Ausgabe: k322b_out.txt. *)
cj[x_] := Prepend[-Rest[x], First[x]];
ml[x_, y_] := If[Length[x] == 1, x y, Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
e[i_] := UnitVector[16, i + 1];
Lm[x_] := Transpose[Table[ml[x, e[j]], {j, 0, 15}]];
zd = Select[Flatten[Table[{i, j, s}, {i, 1, 15}, {j, i + 1, 15}, {s, {1, -1}}], 2], MatrixRank[Lm[e[#[[1]]] + #[[3]] e[#[[2]]]]] < 16 &];
Print["Basis-Diagonalen als Nullteiler: ", Length[zd]];
prof[x_] := Module[{M = Transpose[{x[[2 ;; 8]], x[[10 ;; 16]]}]}, {Transpose[M] . M, x[[{1, 9}]]}];
Print["Profile (M^T M, Singulett) verschieden: ", Union[prof[e[#[[1]]] + #[[3]] e[#[[2]]]] & /@ zd]];
Print["Typ der Paare (i<8, j>8 ?): ", Union[{#[[1]] < 8 && #[[2]] > 8, #[[2]] - #[[1]] != 8} & /@ zd]];
x = c e[1] + s e[10];
Print["det L_x fuer x = c e1 + s e10: ", Factor[Det[Lm[x]]]];
y = c e[1] + s e[9];
Print["det L_x fuer x = c e1 + s e9 (paralleles Paar, Rang 1): ", Factor[Det[Lm[y]]]];
