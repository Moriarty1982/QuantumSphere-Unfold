(* k438b (H224): unabhaengige Wolfram-Gegenprobe zu k438; omega aus der Komposition zweier 4x4-Boostmatrizen (Abspaltung des Gesamtboosts),
   nicht aus der Formel. Aufruf: wolframscript -file k438b_gegenprobe.wl > k438b_out.txt *)
beta = 0.5494056410`30; gl = 1.8646997646`30; eps = ArcTanh[beta];
Print["eps = ", N[eps, 12], ";  2eps - ArcCosh[gamma_L] = ", N[2 eps - ArcCosh[gl], 3]];
bst[r_, th_] := Module[{n = {Cos[th], Sin[th], 0}, g = Cosh[r], bg = Sinh[r]}, ArrayFlatten[{{{{g}}, {bg n}}, {Transpose[{bg n}], IdentityMatrix[3] + (g - 1) Outer[Times, n, n]}}]];
om[a_, b_, th_] := Module[{L = bst[b, th].bst[a, 0], g, v, rap, ang, R}, g = L[[1, 1]]; v = L[[2 ;; 4, 1]]/g; rap = ArcTanh[Norm[v]]; ang = ArcTan[v[[1]], v[[2]]]; R = Inverse[bst[rap, ang]].L; Abs[ArcTan[R[[2, 2]], R[[3, 2]]]]];
xj = Pi/12 - 0.2222220470731`20;
pairs = {{"(e,e)", eps, eps}, {"(2e,2e)", 2 eps, 2 eps}, {"(e,2e)", eps, 2 eps}};
ths = {{"pi/2", Pi/2}, {"pi/4", Pi/4}, {"2pi/3", 2 Pi/3}, {"pi/3", Pi/3}};
rows = Flatten[Table[With[{w = om[p[[2]], p[[3]], t[[2]]]}, Table[{p[[1]], t[[1]], n, N[w/n, 12]}, {n, {1, 2, 3, 6}}]], {p, pairs}, {t, ths}], 2];
Print["omega (n=1) je Kombination: ", Select[rows, #[[3]] == 1 &][[All, {1, 2, 4}]]];
best = First@SortBy[rows, Abs[#[[4]] - xj] &];
Print["naechster: ", best, "  relativ ", N[(best[[4]] - xj)/xj, 4], ";  in sigma (7.8e-7): ", N[(best[[4]] - xj)/7.8*^-7, 4]];
Print["lockere Treffer (<1%): ", Select[rows, Abs[#[[4]] - xj]/xj < 0.01 &]];
Print["Formel-Kontrolle (e,e,pi/4): ", N[2 ArcTan[Sin[Pi/4]/(Coth[eps/2]^2 + Cos[Pi/4])], 12]];
