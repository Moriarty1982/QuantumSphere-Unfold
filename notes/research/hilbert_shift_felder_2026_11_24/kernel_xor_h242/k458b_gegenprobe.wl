(* k458b (Test H242): symbolische Gegenprobe. Produkt wie k253/k321/k453-k457. *)
cj[x_] := Join[{First[x]}, -Rest[x]];
ml[x_, y_] := If[Length[x] == 1, x y,
  Module[{h = Length[x]/2, p, q, r, s},
   p = x[[;; h]]; q = x[[h + 1 ;;]]; r = y[[;; h]]; s = y[[h + 1 ;;]];
   Join[ml[p, r] - ml[cj[s], q], ml[s, p] + ml[q, cj[r]]]]];
e[k_] := UnitVector[8, k + 1];
KK[t_, k_] := Join[Cos[t] e[k], Sin[t] e[k]];
Print["e1 e2 = e3: ", ml[e[1], e[2]] == e[3]];
Print["K1 K2 - u_-(a1+a2)(e3) = ", Union[Simplify[TrigExpand[ml[KK[a1, 1], KK[a2, 2]] - KK[-(a1 + a2), 3]]]]];
S = {UnitVector[16, 1], KK[a1, 1], KK[a2, 2], KK[a3, 3]};
P = Transpose[S] . S;
resid = Table[Simplify[TrigReduce[(# - P . #) . (# - P . #)] &[ml[S[[i]], S[[j]]]]], {i, 4}, {j, 4}];
Print["Quadrat des Schlussrests je Produkt (S_i S_j): ", resid // MatrixForm // ToString];
Print["unter a3 = -(a1+a2): ", Union[Flatten[Simplify[resid /. a3 -> -(a1 + a2)]]]];
Print["Kopien-Belegungen mit Schluss: ", Select[Tuples[{0, 1, 2}, 3], Simplify[Sin[2 Pi Total[#]/3]] == 0 &]];
