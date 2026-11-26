(* k370b (Test H174, 26.11.2026): unabhaengige Nachrechnung der Hauptfaelle aus k370 in Wolfram. Ausgabe in k370b_out.txt.
   Rueckgabe: {Kontrolle eta = 0 {s13, s12, s23}, Teil b fuer eta = tan x, -tan x, tan 2x, -tan 2x je {eta, rho, {s13, s12, s23}},
   Teil c fuer delta = pi/12 + 2pi/3 {eta, m_tau in MeV, {s13, s12, s23}}} *)
T = {{0, 0, 1}, {-1, 0, 0}, {0, -1, 0}}; T2 = T . T;
cM[rho_, d_] := IdentityMatrix[3] + rho/Sqrt[2] (Exp[I d] T + Exp[-I d] T2);
nh[dnu_, sb_] := Module[{l, c, b}, l = SortBy[N[Table[1 + Sqrt[2] Cos[dnu + 2 Pi k/3], {k, 0, 2}], 40], Abs]; c = l[[1]] - 1; b = sb Sqrt[Max[((l[[2]] - l[[3]])^2 - c^2)/8, 0]]; {{1, b, c}, {b, 1, -b}, {c, -b, 1}}];
es[m_] := Module[{v, u, o}, {v, u} = Eigensystem[N[m, 30]]; o = Ordering[Abs[v]]; {v[[o]], Transpose[Normalize /@ u[[o]]]}];
ang[ue_, un_] := Module[{v = ConjugateTranspose[ue] . un, p, s13}, p = Abs[v]^2; s13 = p[[1, 3]]; {s13, p[[1, 2]]/(1 - s13), p[[2, 3]]/(1 - s13)}];
x = 395773407/10^10; dst = Pi/12 - x; sq = Sqrt[{51099895/10^8, 1056583755/10^7, 177693/100}]; tg = sq/sq[[3]];
nn = nh[Pi/6 - x, 1]; un = es[nn][[2]];
resB = Table[Module[{eta = e, f, sol, rr, dd},
   f[r_?NumericQ, d_?NumericQ] := Module[{l = Sort[Abs[Eigenvalues[N[cM[r, d] + eta nn, 30]]]]}, {l[[1]]/l[[3]] - tg[[1]], l[[2]]/l[[3]] - tg[[2]]}];
   sol = FindRoot[f[r, d] == {0, 0}, {{r, 1}, {d, dst + 2 Pi/3}}, WorkingPrecision -> 20];
   {rr, dd} = {r, d} /. sol;
   {N[eta, 6], N[rr, 8], N[ang[es[cM[rr, dd] + eta nn][[2]], un], 6]}], {e, {Tan[x], -Tan[x], Tan[2 x], -Tan[2 x]}}];
nt = nh[Pi/6, 1]; unt = es[nt][[2]]; c0 = cM[1, Pi/12 + 2 Pi/3];
g[e_?NumericQ] := Module[{l = Sort[Abs[Eigenvalues[N[c0 + e nt, 30]]]]}, l[[1]]/l[[2]] - sq[[1]]/sq[[2]]];
ec = e /. FindRoot[g[e], {e, -14/100, -12/100}, WorkingPrecision -> 20];
lc = es[c0 + ec nt];
resC = {N[ec, 8], N[sq[[2]]^2 (Abs[lc[[1, 3]]]/Abs[lc[[1, 2]]])^2, 8], N[ang[lc[[2]], unt], 6]};
ctl = N[ang[es[cM[1, dst + 2 Pi/3]][[2]], un], 8];
{ctl, resB, resC} // InputForm
