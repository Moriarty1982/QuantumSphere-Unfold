(* k278b (Erkundung, nicht blind): ein Feld Z_a = X(v) + a C X(v) im farbneutralen Teil H3(C) (e7 <-> I).
   Konvention k275/k277: x1 = Z23, x2 = Z31, x3 = Z12; Eintraege (-a + I) v_k. *)
Z[a_] := Module[{z = {(-a + I) v1, (-a + I) v2, (-a + I) v3}}, {{0, z[[3]], Conjugate[z[[2]]]}, {Conjugate[z[[3]]], 0, z[[1]]}, {z[[2]], Conjugate[z[[1]]], 0}}];
re = Element[{v1, v2, v3, a}, Reals];
Za = ComplexExpand[Z[a]];
Print["hermitesch: ", Simplify[Za == ConjugateTranspose[Za], re]];
Print["Tr Z^2 = ", Factor[Simplify[ComplexExpand[Tr[Za . Za]], re]]];
Print["N(Z) = det Z = ", Factor[Simplify[ComplexExpand[Det[Za]], re]]];
Print["Tr Z^4 = ", Factor[Simplify[ComplexExpand[Tr[Za . Za . Za . Za]], re]]];
Print["Nullstellen von N in a: ", Solve[3 a - a^3 == 0, a]];
s = v1^2 + v2^2 + v3^2; c = v1 v2 v3;
Print["Tr Z^4 - (Tr Z^2)^2/2 = ", Simplify[ComplexExpand[Tr[Za . Za . Za . Za] - Tr[Za . Za]^2/2], re]];
