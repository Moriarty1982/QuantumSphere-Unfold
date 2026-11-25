(* k334b (H151): Gegenprobe in Wolfram Language zu k334_verschiebung_setzungen.py (Wolfram-Cloud-Kernel, ein Aufruf) *)
b12 = {4 (k^2 + 18 x^2), 8 k (2 k + 3 x + 4), 2 (k^2 + 40)};
b17 = {2 (7 k^2 + 36 x^2), 8 k (2 k + 3 x + 9), 2 (k^2 + 60)};
Print["Fixstrahlen (1,2): ", N[Select[Solve[{b12[[1]] == x b12[[3]], b12[[2]] == k b12[[3]]}, {x, k}, Reals], (x /. #) > 0 &], 7]];
Print["Fixstrahlen (1,7): ", N[Select[Solve[{b17[[1]] == x b17[[3]], b17[[2]] == k b17[[3]]}, {x, k}, Reals], (x /. #) > 0 &], 7]];
K2 = (1 + Sqrt[10/9])/3; K7 = (1 + Sqrt[5/3])/3;
Print["K-Grenzwerte: ", {K2, N[K2, 10], K7, N[K7, 10]}];
th2 = ArcTan[(10/9)^(1/4)] - Pi/4;
Print["theta*-pi/4 (n_B=2) = ", N[th2, 10], " ; gamma_M/18 = ", N[0.2375329/18, 10], " ; relativ ", N[th2/(0.2375329/18) - 1, 4]];
Print["Boost: ", Simplify[(Cosh[e] Cos[t] + Sinh[e] Sin[t])^2 - (Sinh[e] Cos[t] + Cosh[e] Sin[t])^2], " ; bei pi/4: ", Simplify[(Sinh[e] + Cosh[e])/(Cosh[e] + Sinh[e])]];
bs = Sqrt[(1.8647 - 1)/(1.8647 + 1)]; t0 = ArcTan[Sqrt[3 K2 - 1]];
Kb[e_] := (1 + ((Sinh[e] Cos[t0] + Cosh[e] Sin[t0])/(Cosh[e] Cos[t0] + Sinh[e] Sin[t0]))^2)/3;
Print["n_B=2 Boost +-artanh beta: ", N[{Kb[ArcTanh[bs]], Kb[-ArcTanh[bs]]}, 7]];
Print["n_B=7 -ln gamma_L, K'-2/3 = ", N[Module[{t7 = ArcTan[Sqrt[3 K7 - 1]], e = -Log[1.8647]}, (1 + ((Sinh[e] Cos[t7] + Cosh[e] Sin[t7])/(Cosh[e] Cos[t7] + Sinh[e] Sin[t7]))^2)/3 - 2/3], 7], " ; Sqrt[gamma_M] = ", N[Sqrt[0.2375329], 7]];
