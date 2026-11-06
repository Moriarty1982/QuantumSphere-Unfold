(* k205b: H90d - Gegenprobe des Vorzeichens im schwachen statischen Feld (Wolfram-Connector, 6. November 2026).
   Signatur (+,-,-,-), Riemann R^r_{s m n} = d_m Gamma^r_{n s} - d_n Gamma^r_{m s} + Gamma^r_{m l} Gamma^l_{n s} - Gamma^r_{n l} Gamma^l_{m s},
   Ricci R_{s n} = R^m_{s m n} (wie k205). Erwartung: G_00 = 2 Laplace(Phi) in erster Ordnung; mit G = +kappa T, T_00 = rho
   folgt Laplace(Phi) = (kappa/2) rho = 4 pi G rho (anziehend, g_00 = 1 + 2 Phi). *)
X = {t, x, y, z};
g = DiagonalMatrix[{1 + 2 eps Phi[x, y, z], -(1 - 2 eps Phi[x, y, z]), -(1 - 2 eps Phi[x, y, z]), -(1 - 2 eps Phi[x, y, z])}];
gi = Inverse[g];
Gam = Table[1/2 Sum[gi[[l, s]] (D[g[[s, n]], X[[m]]] + D[g[[s, m]], X[[n]]] - D[g[[m, n]], X[[s]]]), {s, 4}], {l, 4}, {m, 4}, {n, 4}];
Riem[r_, s_, m_, n_] := D[Gam[[r, n, s]], X[[m]]] - D[Gam[[r, m, s]], X[[n]]] + Sum[Gam[[r, m, l]] Gam[[l, n, s]] - Gam[[r, n, l]] Gam[[l, m, s]], {l, 4}];
Ric = Table[Sum[Riem[m, s, m, n], {m, 4}], {s, 4}, {n, 4}];
Rs = Sum[gi[[a, b]] Ric[[a, b]], {a, 4}, {b, 4}];
G00 = Normal[Series[Ric[[1, 1]] - 1/2 g[[1, 1]] Rs, {eps, 0, 1}]];
Simplify[G00 - 2 eps (D[Phi[x, y, z], {x, 2}] + D[Phi[x, y, z], {y, 2}] + D[Phi[x, y, z], {z, 2}])]   (* Ergebnis: 0 *)
