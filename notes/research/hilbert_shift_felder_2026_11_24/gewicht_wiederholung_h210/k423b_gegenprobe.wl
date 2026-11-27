(* k423b: Gegenprobe zu H210. (1) Paritaetsregel symbolisch, (2) Kreuzterme unabhaengig integriert (Trapez statt Gauss-Legendre). *)
Print["k423b: (1) Paritaet: Cos[m (s + Pi) - al] - (-1)^m Cos[m s - al] = ", FullSimplify[Cos[m (s + Pi) - al] - (-1)^m Cos[m s - al], Assumptions -> Element[m, Integers]]];
sig = 5. Degree; th = 50. Degree;
ni = {0., 0., 1.}; e1i = {1., 0., 0.}; e2i = {0., 1., 0.};
nj = {Sin[th], 0., Cos[th]}; e1j = {0., -1., 0.}; e2j = {Cos[th], 0., -Sin[th]};
nt = 81; tg = N[Subdivide[-5 sig, 5 sig, nt - 1]]; dt = 10 sig/(nt - 1);
ns = 1440; ss = N[(Range[ns] - 1/2) 2 Pi/ns]; cs = Cos[ss]; sn = Sin[ss];
cr[mi_, mj_, ai_, aj_] := Sum[Module[{t = tg[[k]], xs, tj, sj},
    xs = Transpose[{Cos[t] cs, Cos[t] sn, ConstantArray[Sin[t], ns]}];
    tj = ArcSin[xs . nj]; sj = ArcTan[xs . e1j, xs . e2j];
    dt Cos[t] Exp[-t^2/(2 sig^2)] Total[Cos[mi ss - ai] Exp[-tj^2/(2 sig^2)] Cos[mj sj - aj]] 2 Pi/ns], {k, nt}];
Print["(2) Kreuzterm (Trapez 81 quer ueber +-5 sigma, 1440 laengs), sigma = 5 Grad, theta = 50 Grad, Phasen (0.3, 1.1)"];
Do[Print["   m = ", mm, ": ", NumberForm[cr[mm[[1]], mm[[2]], 0.3, 1.1], 10]], {mm, {{4, 2}, {16, 8}, {2, 1}, {16, 1}}}];
