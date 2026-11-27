(* k391b: Gegenprobe zu k391/k391c in Wolfram Language. H188a symbolisch an allgemeinen 3x3-Matrizen (27 freie Symbole);
   Nachtrag (gemeinsame Form) mit 30 Stellen. Ausgabe: k391b_out.txt *)
A = Array[a, {3, 3}]; B = Array[b, {3, 3}]; B0 = Array[c, {3, 3}];
nn[X_] := Total[Flatten[X]^2]; ip[X_, Y_] := Total[Flatten[X*Y]];
k1[X_, Y_] := nn[X] nn[Y] - ip[X, Y]^2; k2[X_, Y_] := nn[X . Y - Y . X]; k4[X_, Y_] := nn[X . Y] - nn[X] nn[Y];
Print["H188a, symbolische 3x3-Matrizen (27 freie Symbole), Koeffizienten eps^0..eps^3 von K(eps A, eps B):"];
Do[Print[n, ": ", Expand /@ CoefficientList[k[eps A, eps B], eps][[1 ;; 4]], "; Grad in eps: ", Exponent[Expand[k[eps A, eps B]], eps, List]], {n, {"K1", "K2", "K4"}}, {k, {Switch[n, "K1", k1, "K2", k2, "K4", k4]}}];
Print["Gegenstueck mit Hintergrund X_t = B0: eps^2-Koeffizient von K1(B0 + eps A, eps B) minus [N(B0) N(B) - <B0,B>^2] = ", Expand[Coefficient[Expand[k1[B0 + eps A, eps B]], eps, 2] - (nn[B0] nn[B] - ip[B0, B]^2)]];
l = Sort[Table[1 + Sqrt[2] Cos[2/9 + 2 Pi k/3], {k, 0, 2}], N[#1, 30] < N[#2, 30] &];
prs = {{1, 2, 3}, {1, 3, 2}, {2, 3, 1}};
f1 = l[[#[[3]]]] & /@ prs; f2 = l[[#[[3]]]]^2 & /@ prs; f8 = (l[[#[[1]]]] + l[[#[[2]]]])^2/2 & /@ prs;
perm = {3, 2, 1}; {g1, g2, z} = N[#[[perm]], 30] & /@ {f1, f2, f8};
Print["l = ", N[l, 12]];
fit[m_, s_] := Module[{M = Transpose[{g1/z, g2/z}]/s, co, mod}, co = LeastSquares[M, m/s]; mod = (co[[1]] g1 + co[[2]] g2)/z; {N[co, 7], N[co[[2]]/co[[1]], 6], N[mod, 5], N[(mod - m)/s, 3], N[Total[((mod - m)/s)^2], 4]}];
Print["Up   {a,b}, b/a, Modell, Abstaende, chi2: ", fit[{704/10^8, 356/10^5, 967/1000}, {15/10^8, 6/10^5, 4/1000}]];
Print["Down {a,b}, b/a, Modell, Abstaende, chi2: ", fit[{154/10^7, 306/10^6, 1630/10^5}, {2/10^7, 4/10^6, 9/10^5}]];
det[m_, s_] := Module[{cc = Cross[g1, g2]}, N[Abs[cc . (z m)]/Sqrt[Total[cc^2 z^2 s^2]], 4]];
Print["Determinantenabstand (f1, f2)/f8, Zuordnung B, X = m: Up ", det[{704/10^8, 356/10^5, 967/1000}, {15/10^8, 6/10^5, 4/1000}], " sigma, Down ", det[{154/10^7, 306/10^6, 1630/10^5}, {2/10^7, 4/10^6, 9/10^5}], " sigma"];
