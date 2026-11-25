(* k282b (Erkundung, nicht blind): quadratische Formen eines Elements W in H3(C) mit Ladungsmischung c; sigma = komplexe Konjugation (e7 -> -e7). *)
H[d_, z_] := {{d[[1]], z[[3]], Conjugate[z[[2]]]}, {Conjugate[z[[3]]], d[[2]], z[[1]]}, {z[[2]], Conjugate[z[[1]]], d[[3]]}};
W = ComplexExpand[H[{d1, d2, -d1 - d2}, (1 + I c) ({s1, s2, s3} + I {v1, v2, v3})]];
Wc = ComplexExpand[Conjugate[W]];
dd = d1^2 + d2^2 + (d1 + d2)^2; ss = s1^2 + s2^2 + s3^2; vv = v1^2 + v2^2 + v3^2; sv = s1 v1 + s2 v2 + s3 v3;
Print["Tr W^2 - (|d|^2 + 2(1+c^2)(|s|^2+|v|^2)) = ", Simplify[ComplexExpand[Tr[W . W]] - (dd + 2 (1 + c^2) (ss + vv))]];
Print["Tr(W sigma W) - (|d|^2 + 2[(1-c^2)(|s|^2-|v|^2) - 4 c s.v]) = ", Simplify[ComplexExpand[Tr[W . Wc]] - (dd + 2 ((1 - c^2) (ss - vv) - 4 c sv))]];
Print["c = 0: Tr W^2 - Tr(W sigma W) = ", Simplify[ComplexExpand[Tr[W . W] - Tr[W . Wc]] /. c -> 0]];
