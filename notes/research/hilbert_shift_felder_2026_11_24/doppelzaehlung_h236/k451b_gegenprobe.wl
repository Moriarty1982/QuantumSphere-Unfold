(* k451b: unabhaengige Wolfram-Gegenprobe zu H236 Teil A. Lokale Minima am Datenzweig per FindMinimum, Mischfit per FindRoot in (phi, q). *)
x = Pi/12 - 0.2222220470731; xnu = 0.04336; sx = 0.00213;
dI[p_?NumericQ, q_?NumericQ] := d /. Last@FindMinimum[-Cos[2 (d - Pi/4 - p)] + q Cos[3 d], {d, 5 Pi/4 - Pi/12 + p + 0.0}, WorkingPrecision -> 25];
dR[p_?NumericQ, q_?NumericQ] := d /. Last@FindMinimum[Cos[2 (d - p)] + q Cos[3 d], {d, Pi/2 + p}, WorkingPrecision -> 25];
fold[d_] := With[{m = Mod[d, 2 Pi/3]}, Min[m, 2 Pi/3 - m]];
oI[p_?NumericQ, q_?NumericQ] := Pi/12 - fold[dI[p, q]];
oR[p_?NumericQ, q_?NumericQ] := Pi/6 - fold[dR[p, q]];
qQ = -0.0852`25; pQ = p /. FindRoot[oI[p, qQ] == x, {p, 0.001`25}, WorkingPrecision -> 20];
Print["Q: phi = ", pQ, "  x_nu,pred = ", oR[pQ, qQ], "  z = ", (oR[pQ, qQ] - xnu)/sx];
sol[t_] := FindRoot[{oI[p, q] == x, oR[p, q] == t}, {{p, 0.033`25}, {q, -0.013`25}}, WorkingPrecision -> 20];
s0 = sol[xnu]; s2 = sol[xnu + 2 sx];
Print["M Mittelwert: ", s0, "   Anteil q am Im-Versatz: ", 100 (x - (p /. s0))/x, " %"];
Print["M x_nu+2sigma: ", s2];
Print["Phi (q -> 0): x_nu,pred = ", oR[x, -10^-12], "  z = ", (oR[x, -10^-12] - xnu)/sx];
