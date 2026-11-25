(* k280b (Erkundung, nicht blind): gemischte Invarianten von Z_v (Spin 1, Eintraege (-a + I) v_k) und Z_S (Spin 2, Diagonale, Eintraege (1 + I b) s_k)
   im farbneutralen Teil H3(C) (e7 <-> I). Konvention k275/k277: x1 = Z23, x2 = Z31, x3 = Z12. *)
re = Element[{a1, a2, s1, s2, s3, v1, v2, v3, a, b, th, v0}, Reals];
H[d_, z_] := {{d[[1]], z[[3]], Conjugate[z[[2]]]}, {Conjugate[z[[3]]], d[[2]], z[[1]]}, {z[[2]], Conjugate[z[[1]]], d[[3]]}};
Zv = ComplexExpand[H[{0, 0, 0}, (-a + I) {v1, v2, v3}]];
ZS = ComplexExpand[H[{a1, a2, -a1 - a2}, (1 + I b) {s1, s2, s3}]];
T[x__] := Simplify[ComplexExpand[Tr[Dot[x]]], re];
Print["I11 = Tr(Zv ZS) = ", Factor[T[Zv, ZS]]];
Print["I21 = Tr(Zv^2 ZS) = ", Collect[T[Zv, Zv, ZS], {s1, s2, s3, a1, a2}, Factor]];
Print["I12 = Tr(Zv ZS^2) = ", Collect[T[Zv, ZS, ZS], {v1, v2, v3}, Factor]];
u = {Cos[th], Sin[th], 0}; Mu = (3 Outer[Times, u, u] - IdentityMatrix[3])/Sqrt[6];
circ = {a1 -> Mu[[1, 1]], a2 -> Mu[[2, 2]], s1 -> 0, s2 -> 0, s3 -> Mu[[1, 2]]/Sqrt[1 + b^2], v1 -> v0, v2 -> v0, v3 -> v0};
Print["auf dem Kreis u3 = 0, v = v0 (1,1,1):"];
Print["  I11 = ", FullSimplify[T[Zv, ZS] /. circ]];
Print["  I21 = ", FullSimplify[T[Zv, Zv, ZS] /. circ]];
Print["  I12 = ", FullSimplify[T[Zv, ZS, ZS] /. circ]];
Print["  d/dth = 0: I11 ", Solve[D[Sin[2 th], th] == 0 && 0 <= th < Pi, th], "; I21 bei a = b: ", FullSimplify[(T[Zv, Zv, ZS] /. circ) /. a -> b]];
om = Exp[2 Pi I/3]; Uw = Table[om^(j k), {j, 0, 2}, {k, 0, 2}]/Sqrt[3];
col[chi_] := FullSimplify[ComplexExpand[Abs[ConjugateTranspose[Uw] . {1, Exp[I chi], 0}/Sqrt[2]]^2]];
Print["Spalte |Uw^+ (1, e^{i chi}, 0)/Sqrt2|^2: chi = 0: ", col[0], ", chi = Pi: ", col[Pi], ", allgemein: ", col[chi]];
