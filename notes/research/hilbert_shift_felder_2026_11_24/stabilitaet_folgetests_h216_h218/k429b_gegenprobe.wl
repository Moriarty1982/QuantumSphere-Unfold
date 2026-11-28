(* H216/H217 (k429b/k430b): Gegenprobe in Wolfram Language.
   a) die drei gamma der Flaechenvarianten unabhaengig (Summe bis k = 400);
   b) geschlossene Formen: j+1/2 -> gamma = 2, j -> gamma = log2 3; exakter Fixpunkt von E^-1 G bei 1/Sqrt3 symbolisch;
   c) Kontrolle der Gleichwertigkeit "anziehend in der Umkehrklasse <=> abstossend in der Vorwaertsklasse" an RGRE. *)
Fz[g_?NumericQ, a_] := Sum[2^(1 - g a[k]), {k, 1, 400}] - 1;
var = {"Casimir" -> (Sqrt[# (# + 2)/3] &), "j+1/2" -> ((# + 1)/2 &), "j" -> (# &)};
res = Table[With[{g = g /. FindRoot[Fz[g, v[[2]]], {g, 18/10}, WorkingPrecision -> 40]},
    {v[[1]], N[g, 15], N[Sqrt[(g - 1)/(g + 1)], 15]}], {v, var}];
Print[res];
Print["j: gamma = log2 3 ? ", N[res[[3, 2]] - Log[2, 3], 5], ";  j+1/2: gamma - 2 = ", N[res[[2, 2]] - 2, 5]];
Einv[y_] := Sqrt[(-Log[2, y])/(2 - Log[2, y])]; G[b_] := (1 - b^2)/(1 + b^2); Ef[b_] := 2^(1 - (1 + b^2)/(1 - b^2));
Print["E^-1 G (1/Sqrt3) - 1/Sqrt3 = ", FullSimplify[Einv[G[1/Sqrt[3]]] - 1/Sqrt[3]]];
Print["E(1/Sqrt3) = ", FullSimplify[Ef[1/Sqrt[3]]], ",  G(1/Sqrt3) = ", G[1/Sqrt[3]]];
bj = Sqrt[(Log[2, 3] - 1)/(Log[2, 3] + 1)];
Print["E(beta_j) = ", FullSimplify[Ef[bj]], ";  E^-1(2/3) - beta_j = ", FullSimplify[Einv[2/3] - bj]];
d = D[Einv[G[x]], x] /. x -> 1/Sqrt[3];
Print["(E^-1 G)'(1/Sqrt3) = ", FullSimplify[d], " = ", N[d, 8]];
rgre[b_] := Sqrt[G[Sqrt[Ef[b]]]];
Print["RGRE(1/Sqrt3) - 1/Sqrt3 = ", FullSimplify[rgre[1/Sqrt[3]] - 1/Sqrt[3]], ",  RGRE'(1/Sqrt3) = ",
  N[D[rgre[x], x] /. x -> 1/Sqrt[3], 8], " (Log[4] = ", N[Log[4], 8], ")"];
