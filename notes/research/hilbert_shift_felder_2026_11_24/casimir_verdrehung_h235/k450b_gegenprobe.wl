(* k450b: unabhaengige Wolfram-Gegenprobe zu H235. Minimierung in delta mit FindMinimum (16 Startwerte),
   Verdrehung exakt ueber PolyLog (nicht Bernoulli-Form), Ableitung der Baumenergie ueber die Einhuellende. *)
(* Teil 1 *)
q0 = -0.0852; x = Pi/12 - 0.2222220470731; xnu = 0.04336; sx = 0.00213;
vI[d_, p_] := -Cos[2 (d - Pi/4 - p)] + q0 Cos[3 d];
vR[d_, p_] := Cos[2 (d - p)] + q0 Cos[3 d];
gmin[f_, p_] := First@SortBy[Table[Quiet@FindMinimum[f[d, p], {d, s}], {s, 0., 2 Pi - 0.1, 2 Pi/16}], First];
fold[d_] := With[{m = Mod[d, 2 Pi/3]}, Min[m, 2 Pi/3 - m]];
dI[p_?NumericQ] := d /. Last@gmin[vI, p]; dR[p_?NumericQ] := d /. Last@gmin[vR, p];
oI[p_?NumericQ] := Pi/12 - fold[dI[p]]; oR[p_?NumericQ] := Pi/6 - fold[dR[p]];
px = p /. FindRoot[oI[p] == x, {p, 0.001}];
Sp[a_] := -Im[PolyLog[3, Exp[I a]]]; Sv[a_] := Re[PolyLog[4, Exp[I a]]];
Ct[p_] := 2 Sv[Pi/2 - 2 p] + Sv[2 p];
Cpr[p_] := -4 Sp[Pi/2 - 2 p] + 2 Sp[2 p];
dEt = -2 Sin[2 (dI[px] - Pi/4 - px)] + 2 Sin[2 (dR[px] - px)];
kap = -dEt/Cpr[px];
Et[p_?NumericQ] := First[gmin[vI, p]] + First[gmin[vR, p]];
EE[p_?NumericQ] := Et[p] + kap Ct[p];
grid = Table[{p, EE[p]}, {p, 0., 2 Pi/3 - 0.005, 0.005}];
gm = First@SortBy[grid, Last];
pg = p /. Last@FindMinimum[EE[p], {p, gm[[1]]}];
Print["phi_x = ", px, "  oI = ", oI[px], "  x_nu,pred = oR = ", oR[px], "  z = ", (oR[px] - xnu)/sx];
Print["dE_tree/dphi = ", dEt, "  kappa* = ", kap, "  kappa*/|q| = ", kap/Abs[q0]];
Print["E(phi_x) = ", EE[px], "  global min at phi = ", pg, " E = ", EE[pg], "  oI there = ", oI[pg], " oR there = ", oR[pg]];
(* Teil 2: zweite Ableitung aus der Einhuellenden, 30 Stellen *)
dI2[p_?NumericQ] := d /. Last@FindMinimum[vI[d, p], {d, 3.9666 + p}, WorkingPrecision -> 30];
dR2[p_?NumericQ] := d /. Last@FindMinimum[vR[d, p], {d, 1.6337 + p}, WorkingPrecision -> 30];
dE[p_, k_] := -2 Sin[2 (dI2[p] - Pi/4 - p)] + 2 Sin[2 (dR2[p] - p)] + k (-4 Sp[Pi/2 - 2 p] + 2 Sp[2 p]);
px2 = 0.000022294`30; k2 = 0.105559`30; h = 10^-6;
Print["d2E (aus Einhuellender) = ", N[(dE[px2 + h, k2] - dE[px2 - h, k2])/(2 h), 8], "   dE(phi_x) = ", N[dE[px2, k2], 6]];
