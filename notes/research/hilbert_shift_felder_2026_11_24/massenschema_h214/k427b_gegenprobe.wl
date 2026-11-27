(* k427b (H214): unabhaengige Wolfram-Gegenprobe zu k427 (Teile a, b, c).
   K, z, Amplitude a und x je Schema exakt aus den Massen; Rueckwaertssuche bei K = 2/3.
   Aufruf: wolframscript -file k427b_gegenprobe.wl > k427b_out.txt *)
kk[m_] := Total[m]/Total[Sqrt[m]]^2;
deltaAmp[m_List] := Module[{s = Sqrt[m]}, First@SortBy[Table[Module[{sp = s[[p]], mu, c}, mu = Mean[sp];
  c = (2/3) Total[Table[sp[[k + 1]] Exp[-2 Pi I k/3], {k, 0, 2}]]/mu; {Abs[c], Mod[Arg[c], 2 Pi]}], {p, Permutations[{1, 2, 3}]}], Abs[#[[2]] - 0.2222] &]];
pole = {0.51099895`30, 105.6583755`30, 1776.93`30}; poleE = {1.5*^-10, 2.3*^-6, 0.09};
mz = {0.486570161`30, 102.7181359`30, 1746.24`30}; mzE = {4.2*^-8, 9.2*^-6, 0.20};
sigK[m_, e_] := Sqrt[Total[Table[(D[kk[{a1, a2, a3}], {a1, a2, a3}[[i]]] /. Thread[{a1, a2, a3} -> m])^2 e[[i]]^2, {i, 3}]]];
ainv[mu_] := 137.035999 - If[mu > pole[[1]], 2/(3 Pi) Log[mu/pole[[1]]], 0] - If[mu > pole[[2]], 2/(3 Pi) Log[mu/pole[[2]]], 0] - If[mu >= pole[[3]], 1.2, 0];
common[mu_] := pole/(1 + (1/ainv[mu])/Pi (1 + 3/4 Log[mu^2/pole^2]));
own = Table[pole[[i]]/(1 + (1/ainv[pole[[i]]])/Pi), {i, 3}];
Do[{nm, m, e} = s; {a, d} = deltaAmp[m];
  Print[nm, ": K = ", NumberForm[N[kk[m]], 10], "  z = ", NumberForm[N[(kk[m] - 2/3)/sigK[m, e]], 4], "  a = ", NumberForm[N[a], 8], "  x = ", NumberForm[N[Pi/12 - d], 9]],
 {s, {{"Pol", pole, poleE}, {"M_Z (XZZ)", mz, mzE}, {"gemeinsam m_tau", common[pole[[3]]], poleE}, {"eigene Skala", own, poleE}}}];
roots[d_] := Table[1 + Sqrt[2] Cos[d + 2 Pi k/3], {k, 0, 2}];
rat[x_] := Module[{m = Sort[N[roots[Pi/12 - x]^2]]}, {m[[1]]/m[[2]], m[[2]]/m[[3]]}];
xp = Pi/12 - deltaAmp[pole][[2]]; xnu = 0.043359035;
Print["Rueckwaerts: Verhaeltnisse bei x_Pol ", rat[xp], " bei x_nu ", rat[xnu], " relative Aenderung ", NumberForm[rat[xnu]/rat[xp] - 1, 5]];
