(* k421b: Gegenprobe zu H209. (1) Ueberlappflaeche exakt, (2) unabhaengige Minimierung mit FindMinimum (60 Starts). *)
Print["k421b: (1) Ueberlappflaeche zweier ebener Streifen der Breiten a, b unter Winkel th (eine Raute)"];
area = Simplify[Area[Parallelogram[{0, 0}, {{a/Sin[th], 0}, {b Cos[th]/Sin[th], b}}]], Assumptions -> a > 0 && b > 0 && 0 < th < Pi];
Print["   Flaeche = ", area, "; mal Sin[th]/(a b) = ", Simplify[area Sin[th]/(a b), Assumptions -> a > 0 && b > 0 && 0 < th < Pi]];
d = {1, 2, 4, 8, 16}; pr = Subsets[Range[5], {2}];
nv[i_] := {Sin[t[i]] Cos[p[i]], Sin[t[i]] Sin[p[i]], Cos[t[i]]};
en[W_] := Sum[W[[k]]/Sqrt[1 - (nv[pr[[k, 1]]] . nv[pr[[k, 2]]])^2 + 10^-12], {k, Length[pr]}];
vars = Flatten[Table[{t[i], p[i]}, {i, 5}]];
SeedRandom[209];
run[W_, name_] := Module[{best = Infinity, sol, r},
  Do[r = Quiet[FindMinimum[en[W], Table[{v, RandomReal[{0, Pi}]}, {v, vars}], MaxIterations -> 2000]];
   If[NumericQ[r[[1]]] && r[[1]] < best, best = r[[1]]; sol = r[[2]]], {60}];
  Print["   ", name, ": Energie ", NumberForm[best, 9], "; Winkel RC RH RO RS CH CO CS HO HS OS = ",
   NumberForm[Table[ArcCos[Abs[nv[pr[[k, 1]]] . nv[pr[[k, 2]]]]]/Degree /. sol, {k, Length[pr]}], {5, 2}]]];
Print["(2) unabhaengige Minimierung, Gesetz 1/sin"];
run[Table[Min[d[[q]]], {q, pr}] // N, "N1 min(d_i,d_j)"];
run[Table[Sqrt[Min[d[[q]]]/Max[d[[q]]]], {q, pr}] // N, "N2 sqrt(dmin/dmax)"];
run[Table[Times @@ d[[q]], {q, pr}] // N, "N0 d_i d_j"];
