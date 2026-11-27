(* k422b: Gegenprobe zu k422 (exakte Summen der Perlenkette, Bedingung der Stufe, Polwinkel). *)
Print["k422b: (1) Perlenkette, Radien d/16 fuer d = 1,2,4,8,16"];
r = {1, 2, 4, 8, 16}/16;
Print["   Flaeche/4Pi = ", Total[r^2], " = ", N[Total[r^2], 8], "; Grenzwert ", Sum[4^-k, {k, 0, Infinity}]];
Print["   Volumen/(4Pi/3) = ", Total[r^3], " = ", N[Total[r^3], 8], "; Grenzwert ", Sum[8^-k, {k, 0, Infinity}]];
Print["   Hoehe/2 = ", Total[r], "; Grenzwert ", Sum[2^-k, {k, 0, Infinity}]];
Print["(2) Stufe: rho(t) = Sin[t] - Cos[t0] (t - t0) Exp[-(t - t0)^2/(2 s^2)]"];
rho[t_] := Sin[t] - Cos[t0] (t - t0) Exp[-(t - t0)^2/(2 s^2)];
Print["   rho(t0) - Sin[t0] = ", Simplify[rho[t0] - Sin[t0]], "; rho'(t0) = ", Simplify[rho'[t0]], "; rho''(t0) = ", Simplify[rho''[t0]]];
Print["(3) Polwinkel der Kleinkreise in Grad: ", N[ArcSin[r]/Degree, 6]];
Print["(4) Kreuzungsbedingung koaxial: Abstand der Achsen 0, |th_i - th_j| > 0 fuer alle Paare: ", AllTrue[Subsets[ArcSin[r], {2}], Abs[#[[1]] - #[[2]]] > 0 &]];
