(* k294b (Erkundung, nicht blind): unabhaengige Gegenprobe zu k294 in Wolfram Language, Quaternionen als 2x2-Matrizen. *)
s = PauliMatrix /@ {1, 2, 3}; qi = I s[[3]]; qj = I s[[2]]; id = IdentityMatrix[2];
ex[x_] := Cos[x] id + Sin[x] qi;
psi = a ex[p1] + b (Cos[th] id + Sin[th] qj) . ex[-p2];
k1v = {k, -k, 0}; k2v = {kp, -kp Cos[al], -kp Sin[al]};
nq[m_] := Simplify[ComplexExpand[Det[m]]];
ip[x_, y_] := ComplexExpand[Re[Tr[ConjugateTranspose[x] . y]]/2];
av[e_] := Simplify[Integrate[Integrate[TrigReduce[e], {p1, 0, 2 Pi}], {p2, 0, 2 Pi}]/(4 Pi^2)];
X = Table[k1v[[m]] D[psi, p1] + k2v[[m]] D[psi, p2], {m, 3}];
w = a^2 b^2 k^2 kp^2 (4 - (1 + Cos[al])^2);
nn = nq[psi];
Print["Z1 Streuung von N: ", FullSimplify[av[nn^2] - av[nn]^2]];
Print["Z2 freie Energie: ", av[1/2 Sum[nq[X[[m]]], {m, 3}]]];
g1 = av[Sum[nq[X[[m]]] nq[X[[n]]] - ip[X[[m]], X[[n]]]^2, {m, 3}, {n, m + 1, 3}]];
g2 = av[Sum[nq[X[[m]] . X[[n]] - X[[n]] . X[[m]]], {m, 3}, {n, m + 1, 3}]];
Print["Z3 K1/w - (1+Sin[th]^2)/2, K2/w - 2 Sin[th]^2: ", FullSimplify[{g1/w - (1 + Sin[th]^2)/2, g2/w - 2 Sin[th]^2}]];
Print["Z4 Schwelle: ", Solve[-2 lam + (c1/2 + 2 c2) Q == 0, Q]];
