(* k336b (H153): unabhaengige Gegenprobe in Wolfram Language (Vorab-Notiz fd4c7f3).
   beta ueber direkte Koeffizienten (mit Restpruefung), Kovarianz unter B = s|y|^2, Fluss mit WhenEvent (WorkingPrecision 30). *)
coef[rhs_, x_, y_] := Module[{x1 = x[[1]], y1 = y[[1]]},
  {Coefficient[rhs, x1, 4] /. Thread[Join[x, y] -> 0],
   Coefficient[Coefficient[rhs, x1, 2], y1, 2] /. Thread[Join[x, y] -> 0],
   Coefficient[rhs, y1, 4] /. Thread[Join[x, y] -> 0]}];
betasW[nA_, nB_, sw_] := Module[{xv = Array[xx, nA], yv = Array[yy, nB], aa0, bb0, vv, hh, rr, cf},
  aa0 = Total[xv^2]; bb0 = sw Total[yv^2]; vv = la aa0^2 + ka aa0 bb0 + lb bb0^2;
  hh = D[vv, {Join[xv, yv], 2}]; rr = Expand[Tr[hh.hh]/2];
  cf = coef[rr, xv, yv];
  {Factor[cf {1, 1/sw, 1/sw^2}], Simplify[rr - Expand[(cf[[1]] aa0^2 + cf[[2]]/sw aa0 bb0 + cf[[3]]/sw^2 bb0^2)]]}];
{b12, r12} = betasW[1, 2, 1]; {b11, r11} = betasW[1, 1, 1]; {bw, rw} = betasW[1, 2, s];
Print["beta(1,2) = ", b12, "  Rest ", r12]; Print["beta(1,1) = ", b11, "  Rest ", r11];
conj = (b12 /. {ka -> s ka, lb -> s^2 lb}) {1, 1/s, 1/s^2};
Print["beta(Bhat = s|y|^2) Rest ", rw, "; minus konjugiert: ", Simplify[bw - conj]];
Print["Tausch (1,1) bei la = lb: ", Simplify[(b11[[1]] - b11[[3]]) /. lb -> la]];
flow[bet_, g0_] := Module[{sol, t, te},
  sol = First@NDSolve[{fa'[t] == -(bet[[1]] /. {la -> fa[t], ka -> fk[t], lb -> fb[t]}),
     fk'[t] == -(bet[[2]] /. {la -> fa[t], ka -> fk[t], lb -> fb[t]}),
     fb'[t] == -(bet[[3]] /. {la -> fa[t], ka -> fk[t], lb -> fb[t]}),
     fa[0] == g0[[1]], fk[0] == g0[[2]], fb[0] == g0[[3]],
     WhenEvent[fk[t] + 2 Sqrt[fa[t] fb[t]] == 0, "StopIntegration"]}, {fa, fk, fb}, {t, 0, 10^4},
    WorkingPrecision -> 30, PrecisionGoal -> 15, AccuracyGoal -> 20];
  te = (fa /. sol)["Domain"][[1, 2]];
  {te, (1 + Sqrt[(fa /. sol)[te]/(fb /. sol)[te]])/3}];
abl = {"N1" -> {1, 2}, "N2" -> {1/3, 2/3}, "N3" -> {1, 2/3}};
Do[With[{aa = nm[[2, 1]], bb = nm[[2, 2]]},
   Print[nm[[1]], " lam=0.2 k/lam=", N[kr], ": tau, K = ", N[flow[b12, {1/5/aa^2, kr/5/(aa bb), 1/5/bb^2}], 10]]], {nm, abl}, {kr, {-19/10, -1/2, -1/10}}];
Do[Print["N4 lam=0.2 k/lam=", N[kr], ": tau, K = ", N[flow[b11, {1/5, kr/5, 1/5}], 12], "; K - 2/3 = ", N[flow[b11, {1/5, kr/5, 1/5}][[2]] - 2/3, 3]], {kr, {-19/10, -1/2, -1/10}}];
