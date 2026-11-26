(* k377b: unabhaengige Kontrolle der stationaeren Punkte aus k377 (H178b, c); sa = sin^2 alpha, t = sin^2 theta *)
V = A sa t + B sa^2 t^2 + kap (1 - sa) t (1 - t);
ts = t /. First[Solve[D[V, t] == 0, t]];
r0 = Simplify[ts /. sa -> 0];
curv = Simplify[D[V, {t, 2}]];
dA = Simplify[D[ts, A]];
td = Sin[48.114 Degree]^2; tu = Sin[52.207 Degree]^2;
sol[sd_, su_] := NSolve[{(ts /. {sa -> sd, kap -> -1}) == td, (ts /. {sa -> su, kap -> -1}) == tu}, {A, B}];
s1 = sol[2/3, 1/3]; s2 = sol[1/3, 2/3];
q0 = ts /. {sa -> 1, kap -> -1} /. First[s1];
Print[{r0, curv, dA, s1, s2, q0, ArcSin[Sqrt[q0]]/Degree, curv /. {sa -> {2/3, 1/3}, kap -> -1} /. First[s1], curv /. {sa -> {1/3, 2/3}, kap -> -1} /. First[s2]}]
