(* k440b: Wolfram-Gegenprobe zu H226 (tauschbrechender Term fuer den Modulus phi), unabhaengig von k440 (FindMinimum statt scipy).
   So in zwei Auswertungen ueber den Wolfram-Kernel ausgefuehrt; Ausgabe in k440b_out.txt. *)
x = Pi/12 - 0.2222220470731`20;
vI[d_, p_, q_, a_] := -Cos[2 (d - Pi/4 - p)] + a Cos[2 d] + q Cos[3 d];
vR[d_, p_, q_] := Cos[2 (d - p)] + q Cos[3 d];
mn[f_] := First[MinimalBy[Table[Quiet@FindMinimum[f[d], {d, d0}], {d0, 0, 2 Pi - Pi/6, Pi/6}], First]];
eT[p_?NumericQ, q_, a_] := First[mn[vI[#, p, q, a] &]] + First[mn[vR[#, p, q] &]];
fold[d_] := Module[{m = Mod[d, 2 Pi/3]}, Min[m, 2 Pi/3 - m]];
(* Auswertung 1 *)
r1 = 3 (Sin[Pi/4 - 3 u] + Cos[3 u])/(2 Cos[2 u]);
Print["A1 fuehrende Ordnung T1: alpha/q = 3(Sin[Pi/4-3x]+Cos[3x])/(2Cos[2x]) = ", N[r1 /. u -> x, 8]];
Print["A2 fuehrende Ordnung T2: lambda = -Sin[Pi/4-3x]/Cos[3x] = ", N[-Sin[Pi/4 - 3 x]/Cos[3 x], 8]];
With[{q = -0.0001, a = -2.424781*0.0001},
 tab = Table[{p, eT[p, q, a]}, {p, -Pi/2., Pi/2. - Pi/120, Pi/120}];
 pm = First[MinimalBy[tab, Last]];
 Print["A3 T1 Verhaeltnis -2.424781: E(x) = ", NumberForm[eT[x, q, a], 12], " ; grobes globales Minimum bei phi = ", pm[[1]], " mit E = ", NumberForm[pm[[2]], 12],
  " ; dE/dphi(x) = ", (eT[x + 10^-5, q, a] - eT[x - 10^-5, q, a])/(2 10^-5)]];
(* Auswertung 2 *)
With[{q = -0.0852, a = 0.120069},
 tab = Table[{p, eT[p, q, a]}, {p, -Pi/2., Pi/2. - Pi/120, Pi/120}];
 pm = First[MinimalBy[tab, Last]][[1]];
 fine = Table[{p, eT[p, q, a]}, {p, pm - Pi/120, pm + Pi/120, Pi/120/30}];
 pf = First[MinimalBy[fine, Last]][[1]];
 dI = fold[d /. Last[mn[vI[#, pf, q, a] &]]]; dR = fold[d /. Last[mn[vR[#, pf, q] &]]];
 Print["B T1 alpha=0.120069, q=-0.0852: phi* = ", pf, " ; delta_Im = ", dI, " ; delta_Re = ", dR, " ; x_nu,pred = Pi/6 - delta_Re = ", N[Pi/6] - dR]];
