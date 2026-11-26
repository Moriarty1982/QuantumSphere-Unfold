(* k363b (H168): unabhaengige Gegenprobe in Wolfram Language. Ausgabe: k363b_out.txt *)
out = {}; pr[x__] := AppendTo[out, StringJoin[ToString /@ {x}]];
fold[d_] := Module[{m = Mod[d, 2 Pi/3]}, Min[m, 2 Pi/3 - m]];
pr["a: c=0: ", FullSimplify[Table[fold[0 + k Pi/2], {k, 0, 3}]], "; c=1: ", FullSimplify[Table[fold[Pi/4 + k Pi/2], {k, 0, 3}]]];
ds = 2222220470731/10^13; x = Pi/12 - ds;
rts[d_?NumericQ] := Sort[Table[N[1 + Sqrt[2] Cos[d + 2 Pi k/3], 30], {k, 0, 2}]];
R[d_?NumericQ] := Module[{m = Sort[rts[d]^2]}, (m[[2]]^2 - m[[1]]^2)/(m[[3]]^2 - m[[1]]^2)];
robs = 7537/251100; sr = robs Sqrt[(97/7537)^2 + (205/25110)^2];
pr["b: x = ", N[x, 12], "; Tan[Pi/4 - x] = ", N[Tan[Pi/4 - x], 12], "; Tan[-x] = ", N[Tan[-x], 12]];
pr["c: R_obs = ", N[robs, 7], " +- ", N[sr, 4], "; R(Pi/6) = ", N[R[Pi/6], 8], " (", N[(R[Pi/6] - robs)/sr, 4], " sigma); R(Pi/6 - x) = ", N[R[Pi/6 - x], 8],
   " (", N[(R[Pi/6 - x] - robs)/sr, 4], " sigma); R(Pi/12) = ", N[R[Pi/12], 8], " (", N[(R[Pi/12] - robs)/sr, 4], " sigma)"];
pr["d: ", Table[{b, sg, N[R[N[fold[b + sg x], 30]], 6], N[(R[N[fold[b + sg x], 30]] - robs)/sr, 4]}, {b, {0, Pi/12, Pi/6, Pi/4}}, {sg, {-1, 1}}]];
dn = d /. FindRoot[R[d] == robs, {d, 0.47, 0.49}, WorkingPrecision -> 20];
pr["d: delta_nu(Daten) = ", N[dn, 8], "; x_nu = ", N[Pi/6 - dn, 6]];
StringRiffle[out, "\n"]
