(* k276b (Test H127, Stufe A exakt): Spin-Zerlegung von C = L_e7 je Platz auf H3(C) unter X -> R X R^T.
   Koordinaten orthonormal zur Spurform: Diagonale a_k, Sqrt[2] Re x_s, Sqrt[2] Im x_s (x1 = X23, x2 = X31, x3 = X12), e7 <-> I. *)
toX[u_] := Module[{X = DiagonalMatrix[u[[1 ;; 3]]], x1 = (u[[4]] + I u[[7]])/Sqrt[2], x2 = (u[[5]] + I u[[8]])/Sqrt[2], x3 = (u[[6]] + I u[[9]])/Sqrt[2]},
   X = X + 0 I; X[[2, 3]] = x1; X[[3, 2]] = Conjugate[x1]; X[[3, 1]] = x2; X[[1, 3]] = Conjugate[x2]; X[[1, 2]] = x3; X[[2, 1]] = Conjugate[x3]; X];
toU[X_] := ComplexExpand[{X[[1, 1]], X[[2, 2]], X[[3, 3]], Sqrt[2] Re[X[[2, 3]]], Sqrt[2] Re[X[[3, 1]]], Sqrt[2] Re[X[[1, 2]]], Sqrt[2] Im[X[[2, 3]]], Sqrt[2] Im[X[[3, 1]]], Sqrt[2] Im[X[[1, 2]]]}];
B = IdentityMatrix[9];
gen[{i_, j_}] := Module[{L = ConstantArray[0, {3, 3}]}, L[[i, j]] = -1; L[[j, i]] = 1; Transpose[Table[Simplify[toU[L . toX[B[[k]]] + toX[B[[k]]] . Transpose[L]]], {k, 9}]]];
Ts = gen /@ {{2, 3}, {3, 1}, {1, 2}};
Print["so(3) antisymmetrisch: ", AllTrue[Ts, # + Transpose[#] == 0 &], ", Kommutator [T1,T2] = T3: ", Ts[[1]] . Ts[[2]] - Ts[[2]] . Ts[[1]] == Ts[[3]] || Ts[[1]] . Ts[[2]] - Ts[[2]] . Ts[[1]] == -Ts[[3]]];
Cm = ConstantArray[0, {9, 9}]; Do[Cm[[3 + s, 6 + s]] = -1; Cm[[6 + s, 3 + s]] = 1, {s, 3}];
Print["C^2 auf Offdiagonalen = -1: ", (Cm . Cm)[[4 ;; 9, 4 ;; 9]] == -IdentityMatrix[6]];
id = IdentityMatrix[9];
ads = Table[KroneckerProduct[T, id] - KroneckerProduct[id, Transpose[T]], {T, Ts}];
cas = -Total[# . # & /@ ads];
c = Flatten[Cm];
ls = Range[0, 4];
proj[l_] := Fold[(cas . #1 - #2 (#2 + 1) #1)/(l (l + 1) - #2 (#2 + 1)) &, c, DeleteCases[ls, l]];
comps = Table[proj[l], {l, ls}];
Print["Summe der Komponenten = C: ", Total[comps] == c];
Print["Casimir-Eigenwerte (Multiplizitaet): ", Tally[Eigenvalues[cas]]];
w = Table[Simplify[comps[[l + 1]] . comps[[l + 1]]/(c . c)], {l, ls}];
Print["w_l fuer l = 0..4 (exakt): ", w];
Print["||C||^2 = ", c . c];
Rodd = {{0, 1, 0}, {1, 0, 0}, {0, 0, -1}}; rodd = Transpose[Table[Simplify[toU[Rodd . toX[B[[k]]] . Transpose[Rodd]]], {k, 9}]];
Rcyc = {{0, 0, 1}, {1, 0, 0}, {0, 1, 0}}; rcyc = Transpose[Table[Simplify[toU[Rcyc . toX[B[[k]]] . Transpose[Rcyc]]], {k, 9}]];
Print["zyklisch: rho C rho^T == C: ", rcyc . Cm . Transpose[rcyc] == Cm, ";  ungerade: rho C rho^T == -C: ", rodd . Cm . Transpose[rodd] == -Cm];
