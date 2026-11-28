(* k455b (Test H239): unabhaengige Wolfram-Gegenprobe, exakt. Produkt wie k253/k321/k453 (g = -1 an jeder Wand). *)
cj[x_] := Join[{First[x]}, -Rest[x]];
ml[x_, y_] := If[Length[x] == 1, x y,
  Module[{h = Length[x]/2, p, q, r, s},
   p = x[[;; h]]; q = x[[h + 1 ;;]]; r = y[[;; h]]; s = y[[h + 1 ;;]];
   Join[ml[p, r] - ml[cj[s], q], ml[s, p] + ml[q, cj[r]]]]];
ee[i_] := UnitVector[16, i + 1];
Lm[x_] := Transpose[Table[ml[x, ee[j]], {j, 0, 15}]];
z1 = Flatten[Table[If[j == i + 8, Nothing, ee[i] + sg ee[j]], {i, 1, 7}, {j, 9, 15}, {sg, {1, -1}}], 2];
Print["Z1 Anzahl: ", Length[z1], "; Raenge: ", Union[MatrixRank /@ Lm /@ z1]];
(* dim(C cap unten) = rank(L) - rank(L[[oben-Zeilen]]) ; dim(C cap oben) = rank(L) - rank(L[[unten-Zeilen]]) *)
wd[x_] := With[{M = Lm[x]}, {MatrixRank[M] - MatrixRank[M[[9 ;; 16]]], MatrixRank[M] - MatrixRank[M[[1 ;; 8]]]}];
Print["Z1 Wand (C cap unten, C cap oben): ", Union[wd /@ z1]];
a = {0, 1, 1, 1, 1, 0, 0, 0}/2; b = {0, 1, -1, 0, 0, 1, 1, 0}/2; x2 = Join[a, b];
Print["allgemeiner Nullteiler x2: Rang = ", MatrixRank[Lm[x2]], "; Wand = ", wd[x2]];
H = NullSpace[Transpose[Lm[x2]]];
Print["Paritaetspruefung (", Length[H], " Zeilen), ungeschuetzte Koordinaten (Spalte = 0): ",
  Select[Range[0, 15], AllTrue[H[[All, # + 1]], # == 0 &] &]];
Print["Kern von L_x2 exakt: ", NullSpace[Lm[x2]]];
