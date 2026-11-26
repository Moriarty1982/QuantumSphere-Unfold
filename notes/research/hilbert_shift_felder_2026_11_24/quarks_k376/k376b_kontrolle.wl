(* k376b: exakte Kontrolle der Identitaeten aus k376 *)
lam[k_] := 1 + Sqrt[2] rho Cos[d + 2 Pi k/3];
s1 = FullSimplify[Sum[lam[k], {k, 0, 2}]];
s2 = FullSimplify[Sum[lam[k]^2, {k, 0, 2}] - 3 (1 + rho^2)];
kk = FullSimplify[Sum[lam[k]^2, {k, 0, 2}]/Sum[lam[k], {k, 0, 2}]^2 - (1 + rho^2)/3];
F = Table[Exp[2 Pi I j k/3], {j, 0, 2}, {k, 0, 2}]/Sqrt[3];
M = Table[If[i == j, a[i], If[i < j, x[i, j] + I y[i, j], x[j, i] - I y[j, i]]], {i, 3}, {j, 3}];
T = {{0, 0, 1}, {1, 0, 0}, {0, 1, 0}};
avg = (M + T . M . Transpose[T] + T . T . M . Transpose[T . T])/3;
G = ConjugateTranspose[F] . M . F // ComplexExpand;
dg = FullSimplify[ComplexExpand[Sum[Abs[G[[i, i]]]^2, {i, 3}] - Tr[avg . ConjugateTranspose[avg]]], Element[_a | _x | _y, Reals]];
Print[{s1, s2, kk, dg, N[Sqrt[9 {0.7477885, 0.8876207} - 6]]}]
