(* k420b: Gegenprobe zur Verformung (k420). Unabhängige Auswertung von u(x) = Sum_i w_i G(n_i.x). Normalen aus k420 (Gewicht = Dimension, 1/sin). *)
V = {{-0.4191644262, 0.8287483447, 0.3707794021}, {0.4496471441, -0.8606902465, 0.2388090145}, {0.3419256387, 0.9395663762, 0.0173747581}, {-0.9999677143, 0., 0.0080355638}, {0., 0., 1.}};
w = {1., 2., 4., 8., 16.};
co[m2_, lmax_] := Table[N[(2 l + 1)/2 LegendreP[l, 0]/(l (l + 1) + m2)], {l, 2, lmax, 2}];
g[c_?NumericQ, cf_, lmax_] := cf . Table[LegendreP[l, N[c]], {l, 2, lmax, 2}];
u[x_, cf_, lmax_] := Sum[w[[i]] g[V[[i]] . x, cf, lmax], {i, 5}];
Print["k420b Gegenprobe: u auf den Achsen x (Pol von O), y (Kreuzung O/S), z (Pol von S)"];
Do[With[{cf = co[m2, lm]}, Print["m2 = ", m2, ", lmax = ", lm, ": ", NumberForm[u[#, cf, lm] & /@ N[IdentityMatrix[3]], 10]]], {m2, {2, 6, 20}}, {lm, {80, 200}}];
cf6 = co[6, 80];
Print["Mittel von u auf Band S (m2 = 6): ", Mean[Table[u[{Cos[t], Sin[t], 0.}, cf6, 80], {t, 0., 2 Pi - 0.001, 2 Pi/360}]]];
e2 = Normalize[Cross[V[[4]], {0., 1., 0.}]];
Print["Mittel von u auf Band O (m2 = 6): ", Mean[Table[u[Cos[t] {0., 1., 0.} + Sin[t] e2, cf6, 80], {t, 0., 2 Pi - 0.001, 2 Pi/360}]]];
