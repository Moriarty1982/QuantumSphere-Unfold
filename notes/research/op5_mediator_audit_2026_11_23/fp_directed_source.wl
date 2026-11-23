(* Audit 23.11.2026: N_m als Fierz-Pauli-Austausch der gerichteten Quelle aus
   notes/research/op5_bifocal_response_2026_11_18/OP5_J_Stabilitaet_Doppelkopplung.md
   (T^00/h = -a, T^0i/h = -w (P k)_i, T^ij/h = -x P^ij, P = diag(1, 1, 0)). Erkundung ohne Kriterium, Ergebnis analytisch bekannt. *)
eta = DiagonalMatrix[{1, -1, -1, -1}];
P = DiagonalMatrix[{1, 1, 0}]; kv = {k1, k2, k3}; Pk = P . kv;
S = ConstantArray[0, {4, 4}];
S[[1, 1]] = -a; Do[S[[1, i + 1]] = S[[i + 1, 1]] = -w Pk[[i]], {i, 3}]; Do[S[[i + 1, j + 1]] = -x P[[i, j]], {i, 3}, {j, 3}];
rep = {a -> k1^2 + k2^2, x -> w^2};
p = {w, k1, k2, k3};
pl = eta . p;
Print["Erhaltung p_mu S^{mu nu} = ", Simplify[(pl . S) /. rep]];
Sl = eta . S . eta;
Print["S.S = ", Collect[Expand[Total[Flatten[Sl S]]] /. {w -> Sqrt[x]} /. {k1^2 -> a - k2^2}, {x, a}], ";  tr S = ", Expand[Tr[eta . S]]];
Nexpr = Expand[(Total[Flatten[Sl S]] - Tr[eta . S]^2/3) /. w -> Sqrt[x] /. k1 -> Sqrt[a - k2^2]];
Print["Fierz-Pauli-Zaehler S.S - (trS)^2/3 = ", Factor[Nexpr], ";  minus N_m = ", Simplify[Nexpr - 2/3 (x^2 - a x + a^2)]];
Print["Beitrag der Zeit-Quer-Komponenten -2 S_0i S^0i = ", Simplify[Expand[-2 Sum[S[[1, i + 1]]^2, {i, 3}]] /. w -> Sqrt[x] /. k1 -> Sqrt[a - k2^2]]];
Print["ohne Zeit-Quer-Komponenten waere der Zaehler: ", Factor[Simplify[Nexpr + 2 Expand[Sum[S[[1, i + 1]]^2, {i, 3}]] /. w -> Sqrt[x] /. k1 -> Sqrt[a - k2^2]]]];
