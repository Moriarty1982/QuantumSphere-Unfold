(* k293b (Erkundung, nicht blind): unabhaengige Gegenprobe zu k293 in Wolfram Language, Quaternionen als 2x2-Matrizen. *)
s = PauliMatrix /@ {1, 2, 3}; qi = I s[[3]]; qj = I s[[2]]; id = IdentityMatrix[2];
ex[x_] := Cos[x] id + Sin[x] qi;
psiC = a ex[p1] + b ex[-p2]; psiJ = a ex[p1] + b qj . ex[-p2];
k1v = {k, -k, 0}; k2v = {kp, -kp Cos[al], -kp Sin[al]};
nq[m_] := Simplify[ComplexExpand[Det[m]]];
ip[x_, y_] := ComplexExpand[Re[Tr[ConjugateTranspose[x] . y]]/2];
av[e_] := Simplify[Integrate[Integrate[TrigReduce[e], {p1, 0, 2 Pi}], {p2, 0, 2 Pi}]/(4 Pi^2)];
calc[psi_] := Module[{X, h2, g1, g2},
   X = Table[k1v[[m]] D[psi, p1] + k2v[[m]] D[psi, p2], {m, 3}];
   h2 = av[1/2 Sum[nq[X[[m]]], {m, 3}]];
   g1 = av[Sum[nq[X[[m]]] nq[X[[n]]] - ip[X[[m]], X[[n]]]^2, {m, 3}, {n, m + 1, 3}]];
   g2 = av[Sum[nq[X[[m]] . X[[n]] - X[[n]] . X[[m]]], {m, 3}, {n, m + 1, 3}]];
   {av[nq[psi]], h2, Factor[g1], Factor[g2]}];
rc = calc[psiC]; rj = calc[psiJ];
Print["Y1 S_C {<N>, <H2>, <H4 K1>, <H4 K2>}: ", rc];
Print["Y2 S_J {<N>, <H2>, <H4 K1>, <H4 K2>}: ", rj];
Print["Y3 Unterschied / (a^2 b^2 k^2 kp^2 (4 - (1+Cos[al])^2)): ", Simplify[(rj - rc)[[3 ;; 4]]/(a^2 b^2 k^2 kp^2 (4 - (1 + Cos[al])^2))]];
