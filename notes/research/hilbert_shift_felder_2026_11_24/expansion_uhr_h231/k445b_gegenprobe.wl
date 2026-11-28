(* k445b: Wolfram-Gegenprobe zu H231 (Expansion als Uhr). NDSolve der Feldgleichung in N = ln a fuer drei mu-Werte,
   d ln m_e/d phi symbolisch, Drift beim angepassten mu*. Aufruf: wolframscript -file k445b_gegenprobe.wl > k445b_out.txt *)
om = 315/1000; or = 91/10^6; ol = 1 - om - or; x = Pi/12 - 2222220470731/10^13;
e2[n_] := or Exp[-4 n] + om Exp[-3 n] + ol;
sol[mu_] := NDSolve[{p''[n] + (3 + (-4 or Exp[-4 n] - 3 om Exp[-3 n])/(2 e2[n])) p'[n] + (mu^2/3) Sin[3 (p[n] - Pi/8)]/e2[n] == 0, p[Log[10^-8]] == 0, p'[Log[10^-8]] == 0}, p, {n, Log[10^-8], 0}, WorkingPrecision -> 25, AccuracyGoal -> 18, PrecisionGoal -> 18, MaxSteps -> Infinity];
Do[With[{s = sol[mu]}, Print["mu = ", mu, ": phi(heute) = ", N[p[0] /. s[[1]], 12], ", phi' = ", N[p'[0] /. s[[1]], 8]]], {mu, {97211243/10^8, 1, 827592/10^6}}];
dl = D[Log[(1 + Sqrt[2] Cos[Pi/12 - f + 2 Pi k/3])^2], f];
Print["d ln m_e/d phi bei x (k = 1, Elektron): ", N[dl /. {f -> x, k -> 1}, 10], ";  m-Werte k=0,1,2: ", N[Table[(1 + Sqrt[2] Cos[Pi/12 - x + 2 Pi k/3])^2, {k, 0, 2}], 6]];
h0 = 674/10 * 102271/10^17;
Print["Drift bei mu*: ", N[Abs[(dl /. {f -> x, k -> 1}) (p'[0] /. sol[97211243/10^8][[1]])] h0, 5], " /yr"];
