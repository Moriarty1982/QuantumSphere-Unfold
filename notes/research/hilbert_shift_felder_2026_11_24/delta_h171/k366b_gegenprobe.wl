(* k366b (H171): Gegenprobe zu a, b, d. Teil c (Sedenionen) nur in Python (k366). *)
lam = Table[A + Sqrt[2] B Cos[d + 2 Pi k/3], {k, 0, 2}];
K = FullSimplify[Total[lam^2]/Total[lam]^2];
Print["a1 K: ", K, "; dK/dd: ", FullSimplify[D[K, d]], "; K(theta): ", FullSimplify[K /. {A -> R Cos[th], B -> R Sin[th]}], "; K(Pi/4): ", FullSimplify[K /. {A -> 1, B -> 1}]];
Rpol[t_] := {{Cos[t], -Sin[t], 0}, {Sin[t], Cos[t], 0}, {0, 0, 1}}; Raz[t_] := {{1, 0, 0}, {0, Cos[t], -Sin[t]}, {0, Sin[t], Cos[t]}};
Print["a2 Raz.Rpol.e: ", Simplify[Raz[d] . Rpol[th] . {1, 0, 0}]];
S = {{0, 1, 0}, {0, 0, 1}, {1, 0, 0}};
Do[W = a IdentityMatrix[3] + z S + Conjugate[z] Transpose[S];
 Print["b ", z, ": |z|/a = ", Simplify[Abs[z]/a, a > 0], ", Arg = ", Simplify[Arg[z], a > 0], ", K = ", Simplify[Tr[W . W]/Tr[W]^2, a > 0], ", EW/a = ", Sort[FullSimplify[Eigenvalues[W]/a, a > 0], N[#1] < N[#2] &], ", det/a^3 = ", Simplify[Det[W]/a^3, a > 0]], {z, {a (1 + I)/2, a (-1 + I)/2}}];
Print["b3 z - a/Sqrt2 Exp[I Pi/4]: ", FullSimplify[a (1 + I)/2 - a/Sqrt[2] Exp[I Pi/4]], "; zweiter Zweig: ", FullSimplify[a (-1 + I)/2 - I a/Sqrt[2] Exp[I Pi/4]]];
Print["b4 n*: ", Simplify[Raz[Pi/4] . Rpol[Pi/4] . {1, 0, 0}], "; Quadrate: ", Simplify[(Raz[Pi/4] . Rpol[Pi/4] . {1, 0, 0})^2]];
M = Raz[Pi/4] . Rpol[Pi/4];
Print["d1 cos Theta: ", FullSimplify[(Tr[M] - 1)/2], "; minus (2 Sqrt2 - 1)/4: ", FullSimplify[(Tr[M] - 1)/2 - (2 Sqrt[2] - 1)/4], "; Theta Grad: ", N[ArcCos[(Tr[M] - 1)/2]/Degree, 12]];
Print["d2 Kommutatornorm: ", N[Norm[Flatten[Raz[Pi/4] . Rpol[Pi/4] - Rpol[Pi/4] . Raz[Pi/4]]], 12]];
