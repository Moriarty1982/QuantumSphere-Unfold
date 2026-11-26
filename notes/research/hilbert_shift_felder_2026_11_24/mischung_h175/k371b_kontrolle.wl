(* k371b (Test H175, 26.11.2026): unabhaengige Nachrechnung ausgewaehlter Punkte aus k371 in Wolfram. Ausgabe in k371b_out.txt.
   Rueckgabe je Punkt {rho, {s13, s12, s23}}:
   1 bester Punkt H175a bei x (K-1 0,02914, K-2 0,04236); 2 x, K-2 allein, kappa = tan x; 3 x, (K-1 + K-2)/sqrt2, kappa = tan x;
   4 x_R, (K-1 + K-2)/sqrt2, kappa = tan x_R; 5 x_R, K-2 allein, kappa = tan x_R *)
T = {{0, 0, 1}, {-1, 0, 0}, {0, -1, 0}}; T2 = T . T;
cM[rho_, d_] := IdentityMatrix[3] + rho/Sqrt[2] (Exp[I d] T + Exp[-I d] T2);
nh[dnu_] := Module[{l, c, b}, l = SortBy[N[Table[1 + Sqrt[2] Cos[dnu + 2 Pi k/3], {k, 0, 2}], 40], Abs]; c = l[[1]] - 1; b = Sqrt[Max[((l[[2]] - l[[3]])^2 - c^2)/8, 0]]; {{1, b, c}, {b, 1, -b}, {c, -b, 1}}];
es[m_] := Module[{v, u, o}, {v, u} = Eigensystem[N[m, 30]]; o = Ordering[Abs[v]]; {v[[o]], Transpose[Normalize /@ u[[o]]]}];
ang[ue_, un_] := Module[{v = ConjugateTranspose[ue] . un, p, s13}, p = Abs[v]^2; s13 = p[[1, 3]]; {s13, p[[1, 2]]/(1 - s13), p[[2, 3]]/(1 - s13)}];
k1 = I {{0, 0, 1}, {0, 0, 0}, {-1, 0, 0}}; k2 = I {{0, -1, 0}, {1, 0, 1}, {0, -1, 0}}/Sqrt[2];
sq = Sqrt[{51099895/10^8, 1056583755/10^7, 177693/100}]; tg = sq/sq[[3]];
run[x_, a1_, a2_] := Module[{nn = nh[Pi/6 - x], un, pp = a1 k1 + a2 k2, f, sol, rr, dd, dst = Pi/12 - 395773407/10^10},
   un = es[nn][[2]];
   f[r_?NumericQ, d_?NumericQ] := Module[{l = Sort[Abs[Eigenvalues[N[cM[r, d] + pp, 30]]]]}, {l[[1]]/l[[3]] - tg[[1]], l[[2]]/l[[3]] - tg[[2]]}];
   sol = FindRoot[f[r, d] == {0, 0}, {{r, 1}, {d, dst + 2 Pi/3}}, WorkingPrecision -> 20];
   {rr, dd} = {r, d} /. sol; {N[rr, 7], N[ang[es[cM[rr, dd] + pp][[2]], un], 6]}];
xl = 395773407/10^10; xr = 43359/10^6;
{run[xl, 2914/10^5, 4236/10^5], run[xl, 0, Tan[xl]], run[xl, Tan[xl]/Sqrt[2], Tan[xl]/Sqrt[2]], run[xr, Tan[xr]/Sqrt[2], Tan[xr]/Sqrt[2]], run[xr, 0, Tan[xr]]} // InputForm
