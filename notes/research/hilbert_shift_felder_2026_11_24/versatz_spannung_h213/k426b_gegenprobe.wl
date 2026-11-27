(* k426b (H213): unabhaengige Wolfram-Gegenprobe zu k426.
   a) x_nu aus R (FindRoot, Zweig pi/12..pi/6), sigma aus R +- sigma_R
   c) delta aus drei Massen, exakt per erster Fourier-Harmonischer (Pol- und M_Z-Massen)
   Aufruf: wolframscript -file k426b_gegenprobe.wl > k426b_out.txt *)
dm21 = 7.537*^-5; s21 = 0.097*^-5; dm31 = 2.511*^-3; s31 = 0.0205*^-3;
rObs = dm21/dm31; sR = rObs Sqrt[(s21/dm21)^2 + (s31/dm31)^2];
roots[d_] := Table[1 + Sqrt[2] Cos[d + 2 Pi k/3], {k, 0, 2}];
rNO[d_?NumericQ] := Module[{m = Sort[N[roots[d]^2]]}, (m[[2]]^2 - m[[1]]^2)/(m[[3]]^2 - m[[1]]^2)];
xnu[r_] := Pi/6 - (d /. FindRoot[rNO[d] == r, {d, 0.48, Pi/12 + 0.001, Pi/6}, WorkingPrecision -> 30]);
x0 = xnu[rObs]; xlo = xnu[rObs + sR]; xhi = xnu[rObs - sR]; snu = Abs[xhi - xlo]/2;
Print["a) R_obs = ", NumberForm[rObs, 8], " +- ", NumberForm[sR, 6]];
Print["a) x_nu = ", NumberForm[x0, 8], " +- ", NumberForm[snu, 6]];
deltaOf[m_List] := Module[{s = Sqrt[m], best},
  best = First@SortBy[
     Table[Module[{sp = s[[p]], mu, c}, mu = Mean[sp];
       c = (2/3) Total[Table[sp[[k + 1]] Exp[-2 Pi I k/3], {k, 0, 2}]]/mu;
       {p, Abs[c], Mod[Arg[c], 2 Pi]}], {p, Permutations[{1, 2, 3}]}],
     Abs[#[[3]] - 0.2222] &]; best];
pole = {0.51099895`30, 105.6583755`30, 1776.93`30};
mz = {0.486570161`30, 102.7181359`30, 1746.24`30};
{pp, ap, dp} = deltaOf[pole]; {pz, az, dz} = deltaOf[mz];
xlep = Pi/12 - dp; xlepZ = Pi/12 - dz;
Print["c) Pol:  a = ", NumberForm[N[ap], 9], "  delta = ", NumberForm[N[dp], 12], "  x_lepton = ", NumberForm[N[xlep], 10]];
Print["c) M_Z:  a = ", NumberForm[N[az], 9], "  delta = ", NumberForm[N[dz], 12], "  x_lepton(M_Z) = ", NumberForm[N[xlepZ], 10]];
Print["a) T_a (Pol) = ", NumberForm[N[Abs[x0 - xlep]/snu], 4], " sigma;  mit Nenner 0.00091: ", NumberForm[N[Abs[x0 - xlep]/0.00091], 4]];
Print["c) T (M_Z) = ", NumberForm[N[Abs[x0 - xlepZ]/snu], 4], " sigma;  Verschiebung = ", NumberForm[N[(xlepZ - xlep)/snu], 4], " sigma_nu"];
Print["Pruefung K: Pol ", NumberForm[N[Total[pole]/Total[Sqrt[pole]]^2], 10], "  M_Z ", NumberForm[N[Total[mz]/Total[Sqrt[mz]]^2], 10]];
