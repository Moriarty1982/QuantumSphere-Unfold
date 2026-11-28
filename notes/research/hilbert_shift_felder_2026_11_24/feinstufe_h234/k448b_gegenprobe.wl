(* k448b: Wolfram-Gegenprobe zu H234 (gemeinsame Feinstufe). Exakte Eingaben; beste (c, n) je Feinwert fuer eps = phi und die zwei besten B-Lesarten.
   Ausgefuehrt ueber den Wolfram-Evaluator; Ausgabe in k448b_out.txt. Das Monte Carlo ist nur in Python gerechnet. *)
phi = Pi/12 - 2222220470731/10^13; f2 = 549405640974529/10^15 - 1/2; f3 = 85/10^4; f4 = 4336/10^5 - phi;
sig = {18/10^5, 1/1000, 213/10^5}; vals = {f2, f3, f4};
cs = {1, 2, 3, 4, 1/2, 1/3, 1/4, 2/3, 3/2, Sqrt[2], 1/Sqrt[2], Sqrt[3], 1/Sqrt[3], Pi, 1/Pi};
best[v_, s_, e_] := First@SortBy[Flatten[Table[{N[Abs[v - c e^n]/s], c, n}, {c, cs}, {n, 1, 3}], 1], First];
Print["A (eps=phi): ", Table[best[vals[[i]], sig[[i]], phi], {i, 3}]];
Print["B (eps^2=phi): ", Table[best[vals[[i]], sig[[i]], Sqrt[phi]], {i, 3}]];
Print["B (4 eps^2=phi): ", Table[best[vals[[i]], sig[[i]], Sqrt[phi/4]], {i, 3}]];
Print["(beta-1/2)/phi = ", N[f2/phi, 10], "  Abstand zu 5/4 in sigma_beta: ", N[(f2 - 5/4 phi)/(18/10^5), 4]];
