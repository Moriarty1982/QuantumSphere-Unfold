(* k381b: unabhaengige Kontrolle von k381 an zwei Punkten (kappa = 0): R, Mischung, Eigenwerte der Ein-Feld-Form *)
T = {{0, 0, 1}, {-1, 0, 0}, {0, -1, 0}}; T2 = T . T;
cm[rho_, d_] := IdentityMatrix[3] + rho/Sqrt[2] (Exp[I d] T + Exp[-I d] T2);
lam[rho_, d_] := Table[1 + Sqrt[2] rho Cos[d + 2 Pi k/3], {k, 0, 2}];
nh[rho_, d_] := Module[{l = SortBy[N[lam[rho, d]], Abs], c, b}, c = l[[1]] - 1; b = Sqrt[((l[[2]] - l[[3]])^2 - c^2)/8]; {{1, b, c}, {b, 1, -b}, {c, -b, 1}}];
es[m_] := Module[{v, u, o}, {v, u} = Eigensystem[N[m]]; o = Ordering[Abs[v]]; Transpose[Normalize /@ u[[o]]]];
rr[rho_, d_] := Module[{m = Sort[N[lam[rho, d]]^2]}, (m[[2]]^2 - m[[1]]^2)/(m[[3]]^2 - m[[1]]^2)];
pm[rho_, d_] := Module[{ue = es[cm[1.0, 0.2222220470731 + 2 Pi/3]], un = es[nh[rho, d]], v, p, s13}, v = ConjugateTranspose[ue] . un; p = Abs[v]^2; s13 = p[[1, 3]]; {p[[1, 2]]/(1 - s13), p[[2, 3]]/(1 - s13), s13}];
Print[{rr[0.9416, 0.45847], pm[0.9416, 0.45847], rr[1.0, 0.4801], pm[1.0, Pi/6], Sort[Eigenvalues[nh[0.9416, 0.45847]]], Sort[N[lam[0.9416, 0.45847]]]}]
