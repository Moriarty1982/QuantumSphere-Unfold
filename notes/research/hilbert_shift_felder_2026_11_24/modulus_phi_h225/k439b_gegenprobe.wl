(* k439b: Wolfram-Gegenprobe zu H225 (phi als Modulus), unabhaengig von k439 (FindMinimum statt scipy).
   So ausgefuehrt in drei Auswertungen ueber den Wolfram-Kernel (Ausgabe k439b_out.txt). Ein erster Versuch mit Solve auf einem
   Betragsausdruck und FindMinimum/Brent lief nicht durch (Solve::nsmet, unausgewertete Rueckgabe; ein zweiter mit hoher Praezision
   ueberschritt die Zeitgrenze) und ist hier ersetzt. *)
vIm[d_, p_, q_, r_] := -Cos[2 (d - Pi/4 - p)] + q Cos[3 d] + r Cos[6 d];
vRe[d_, p_, q_, r_] := +Cos[2 (d - p)] + q Cos[3 d] + r Cos[6 d];
(* Auswertung 1 (a1, aus dem ersten Versuch uebernommen) *)
Print["a1 Tauschsymmetrie vRe[-d, Pi/4 - p] - vIm[d, p] = ", Simplify[TrigExpand[vRe[-d, Pi/4 - p, q, r] - vIm[d, p, q, r]]]];
s[p_, w_] := w Abs[Cos[Pi/4 - 3 p]] + Abs[Sin[3 p]];
Print["a4 Datenpunkt x: S(x) = ", N[s[Pi/12 - 0.2222220470731, 1], 8], " ; S(Pi/8) = ", N[s[Pi/8, 1], 8], " = 2 Cos[Pi/8] = ", N[2 Cos[Pi/8], 8]];
(* Auswertung 2 *)
Print["a2 Tan[u] = ", Simplify[Solve[TrigExpand[D[w Cos[Pi/4 - u] + Sin[u], u]] == 0 /. Sin[u] -> t Cos[u], t]]];
Print["a3 Tan[3 Pi/8] - (1+Sqrt[2]) = ", FullSimplify[Tan[3 Pi/8] - (1 + Sqrt[2])]];
emin[f_] := Min[Table[First[Quiet@FindMinimum[f[d], {d, d0}]], {d0, 0, 2 Pi - Pi/6, Pi/6}]];
eTot[p_?NumericQ, q_, r_] := emin[vIm[#, p, q, r] &] + emin[vRe[#, p, q, r] &];
scan[q_, r_, sub_] := Module[{tab, pm, fine, pf},
  tab = Table[{pp, eTot[pp, q, r]}, {pp, 0., N[Pi/3 - Pi/60], N[Pi/60]}];
  pm = First[MinimalBy[tab, Last]][[1]];
  fine = Table[{pp, eTot[pp, q, r]}, {pp, pm - Pi/60, pm + Pi/60, Pi/60/sub}];
  pf = First[MinimalBy[fine, Last]]];
With[{pf = scan[-0.0852, 0., 40]}, Print["b q=-0.0852: phi* = ", pf[[1]], " (Gitter Pi/2400; Pi/8 = ", N[Pi/8], ") E(phi*) = ",
  NumberForm[pf[[2]], 10], " E(x) = ", NumberForm[eTot[Pi/12 - 0.2222220470731, -0.0852, 0.], 10]]];
(* Auswertung 3 *)
Do[With[{pf = scan[qr[[1]], qr[[2]], 20]}, Print["q=", qr[[1]], " r=", qr[[2]], ": phi* = ", pf[[1]], " (Pi/8 = ", N[Pi/8], ", 7Pi/24 = ", N[7 Pi/24],
  ") E(phi*) = ", NumberForm[pf[[2]], 10]]], {qr, {{-0.3, 0.}, {0., 0.001}, {0., -0.001}}}];
