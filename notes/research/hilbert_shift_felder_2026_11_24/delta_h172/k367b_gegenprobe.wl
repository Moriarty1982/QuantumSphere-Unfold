(* k367b (H172): Gegenprobe der Zentralwerte K, delta (ohne Monte Carlo) und der Vorhersagewerte. *)
kd[m_, neg_] := Module[{v = Sqrt[m], c, d, w = Exp[2 Pi I/3]}, If[neg, v = v {-1, 1, 1}]; c = Total[v Conjugate[w^{0, 1, 2}]]; d = Mod[Arg[c], 2 Pi/3]; d = Min[d, 2 Pi/3 - d]; {Total[m]/Total[v]^2, d}];
dat = {"up MZ" -> {7.04*^-6, 3.56*^-3, 0.967}, "up PDG" -> {2.16*^-3, 1.2730, 172.4}, "down MZ" -> {1.54*^-5, 3.06*^-4, 1.630*^-2}, "down PDG" -> {4.70*^-3, 93.5*^-3, 4.183}, "lept" -> {0.51099895*^-3, 105.6583755*^-3, 1776.93*^-3}};
Do[Print[d[[1]], ": pos ", NumberForm[kd[d[[2]], False], 8], "; neg ", NumberForm[kd[d[[2]], True], 8]], {d, dat}];
x = 0.0395773407; Print["Vorhersagen down: ", N[{Pi/12, Pi/12 - x, Pi/12 + x}, 8], "; up: ", N[{0, x, Pi/6, Pi/6 - x, Pi/6 + x}, 8]];
