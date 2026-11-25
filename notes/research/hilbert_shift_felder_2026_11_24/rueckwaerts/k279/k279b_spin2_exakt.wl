(* k279b (Erkundung, nicht blind): Spin-2-Feld Z_b = S + b C S im farbneutralen Teil H3(C) (e7 <-> I).
   Konvention k275/k277: x1 = Z23, x2 = Z31, x3 = Z12; Eintraege s_k (1 + I b), Diagonale a_k mit a1 + a2 + a3 = 0. *)
re = Element[{a1, a2, s1, s2, s3, t1, t2, t3, b, g, th}, Reals];
a3 = -a1 - a2;
Z = Module[{z = (1 + I b) {s1, s2, s3}}, {{a1, z[[3]], Conjugate[z[[2]]]}, {Conjugate[z[[3]]], a2, z[[1]]}, {z[[2]], Conjugate[z[[1]]], a3}}];
Z = ComplexExpand[Z];
Print["hermitesch: ", Simplify[Z == ConjugateTranspose[Z], re]];
q = Simplify[ComplexExpand[Tr[Z . Z]], re]; n = Simplify[ComplexExpand[Det[Z]], re];
Print["Tr Z^2 - (|a|^2 + 2(1+b^2)|s|^2) = ", Simplify[q - (a1^2 + a2^2 + a3^2 + 2 (1 + b^2) (s1^2 + s2^2 + s3^2))]];
Print["N - (a1a2a3 + 2(1-3b^2)s1s2s3 - (1+b^2) Sum a_k s_k^2) = ",
  Simplify[n - (a1 a2 a3 + 2 (1 - 3 b^2) s1 s2 s3 - (1 + b^2) (a1 s1^2 + a2 s2^2 + a3 s3^2))]];
M[e_] := {{a1, e t3, e t2}, {e t3, a2, e t1}, {e t2, e t1, a3}};
gam = (1 - 3 b^2)/(1 + b^2)^(3/2);
nt = n /. Thread[{s1, s2, s3} -> {t1, t2, t3}/Sqrt[1 + b^2]];
Print["N - [(1+g) det(D+T) + (1-g) det(D-T)]/2 = ", Simplify[nt - ((1 + gam) Det[M[1]] + (1 - gam) Det[M[-1]])/2, re && b > 0]];
Print["gamma - cos(3 arctan b) = ", FullSimplify[gam - Cos[3 ArcTan[b]], b > 0]];
Print["gamma^2 = 1: ", Solve[gam^2 == 1, b, Reals]];
Print["max det auf |a|^2 + 2|t|^2 = 1 (Eigenwerte l1 + l2 + l3 = 0, Summe l^2 = 1): ",
  Maximize[{l1 l2 (-l1 - l2), l1^2 + l2^2 + (l1 + l2)^2 == 1}, {l1, l2}][[1]], " = 1/Sqrt[54]: ", 1/Sqrt[54] == 1/(3 Sqrt[6])];
(* flache Richtung: Achse u = (cos th, sin th, 0), M = (3 u u^T - 1)/Sqrt[6] *)
u = {Cos[th], Sin[th], 0}; Mu = (3 Outer[Times, u, u] - IdentityMatrix[3])/Sqrt[6];
rule = {a1 -> Mu[[1, 1]], a2 -> Mu[[2, 2]], s1 -> Mu[[2, 3]]/Sqrt[1 + b^2], s2 -> Mu[[3, 1]]/Sqrt[1 + b^2], s3 -> Mu[[1, 2]]/Sqrt[1 + b^2]};
Print["auf dem Grosskreis u3 = 0: Tr Z^2 = ", Simplify[q /. rule], ", N = ", Simplify[n /. rule], " (unabhaengig von th und b)"];
(* allgemeine Achse u auf der det-Bahn: N als Funktion von u *)
uu = {u1, u2, u3}; Mg = (3 Outer[Times, uu, uu] - IdentityMatrix[3])/Sqrt[6];
ruleg = {a1 -> Mg[[1, 1]], a2 -> Mg[[2, 2]], s1 -> Mg[[2, 3]]/Sqrt[1 + b^2], s2 -> Mg[[3, 1]]/Sqrt[1 + b^2], s3 -> Mg[[1, 2]]/Sqrt[1 + b^2]};
ng = Simplify[(n /. ruleg) /. u3^2 -> 1 - u1^2 - u2^2];
Print["auf der det-Bahn (|u| = 1): N - 1/Sqrt[54] = ", FullSimplify[Simplify[(ng - 1/Sqrt[54]) /. u3 -> Sqrt[1 - u1^2 - u2^2], b > 0] /. Sqrt[1 - u1^2 - u2^2]^2 -> u3^2]];
