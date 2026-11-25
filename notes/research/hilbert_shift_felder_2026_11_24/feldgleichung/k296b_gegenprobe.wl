(* k296b: Gegenprobe zu k296 (Test H129) in Wolfram Language. Quaternionen als 2x2-Matrizen.
   Aufruf: wolframscript -file k296b_gegenprobe.wl > k296b_out.txt *)
vars = {x0, x1, x2, x3}; A = x0^2 + x1^2; B = x2^2 + x3^2;
V = lA A^2 + ka A B + lB B^2; H = D[V, {vars, 2}];
rhs = Expand[Tr[H . H]/2];
sol = First[SolveAlways[rhs == bA A^2 + bK A B + bB B^2, vars]];
beta = Factor[{bA, bK, bB} /. sol];
Print["V1 beta (lamA, kappa, lamB), Faktor 16 pi^2: ", beta];
Print["V2 symmetrisch: 16 pi^2 dr/dt = ", Factor[Simplify[((beta[[2]] lam - r lam beta[[1]])/lam^2) /. {lA -> lam, lB -> lam, ka -> r lam}]]];
cls[a0_, k0_, b0_] := Module[{ev = "i", s},
   s = NDSolve[{a'[t] == -beta[[1]], k'[t] == -beta[[2]], b'[t] == -beta[[3]], a[0] == a0, k[0] == k0, b[0] == b0,
       WhenEvent[a[t] < 0, ev = If[a0 == b0, "ii=iii", "iii"]; "StopIntegration"],
       WhenEvent[b[t] < 0, ev = If[a0 == b0, "ii=iii", "ii"]; "StopIntegration"],
       WhenEvent[k[t] + 2 Sqrt[Abs[a[t] b[t]]] < 0, ev = "iv"; "StopIntegration"]} /. {lA -> a[t], ka -> k[t], lB -> b[t]},
     {a, k, b}, {t, 0, 10^4}, PrecisionGoal -> 9, AccuracyGoal -> 13, MaxSteps -> 10^6]; ev];
gl = {1/10, 3/10, 1/2}; gk = DeleteCases[Table[-19/20 + i/20, {i, 0, 49}], 0];
res = Flatten[Table[If[k0 > -2 Sqrt[a0 b0], cls[a0, k0, b0], Nothing], {a0, gl}, {b0, gl}, {k0, gk}]];
Print["V3 Teilgitter lamA, lamB in {0.1, 0.3, 0.5}: ", KeySort[Counts[res]], " ; Punkte ", Length[res]];
(* Zusatzterme *)
e = {IdentityMatrix[2], {{I, 0}, {0, -I}}, {{0, 1}, {-1, 0}}, {{0, I}, {I, 0}}};
q[m_] := Sum[v[m, a] e[[a + 1]], {a, 0, 3}]; nrm[M_] := Simplify[Det[M]];
ip[m_, n_] := Sum[v[m, a] v[n, a], {a, 0, 3}];
prs = Subsets[Range[4], {2}];
K1 = Sum[ip[p[[1]], p[[1]]] ip[p[[2]], p[[2]]] - ip[p[[1]], p[[2]]]^2, {p, prs}];
K2 = Sum[nrm[q[p[[1]]] . q[p[[2]]] - q[p[[2]]] . q[p[[1]]]], {p, prs}];
all = Flatten[Table[v[m, a], {m, 4}, {a, 0, 3}]];
z[K_] := Expand[J/2 Sum[D[K, {s, 2}], {s, all}]];
Print["V4 K1: z_a = ", Table[Coefficient[z[K1], v[1, a], 2], {a, 0, 3}], " ; K2: z_a = ", Table[Coefficient[z[K2], v[1, a], 2], {a, 0, 3}]];
Print["   K2 haengt nur von den Imaginaerteilen ab: ", Simplify[D[K2, v[1, 0]]] === 0];
