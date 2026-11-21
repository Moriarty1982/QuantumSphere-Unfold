ClearAll["Global`*"];
Print["Kernel: ", $Version];
u = DiagonalMatrix[{zj, za}];
proj = {{w, c}, {cc, 1 - w}};
sum = Tr[u]; weighted = Tr[proj.u];
decode[a_, b_, h_] := {((1 - h) a - b)/(1 - 2 h), (b - h a)/(1 - 2 h)};
Print["Rank-one modal reconstruction residual: ", Together[decode[sum, weighted, w] - {zj, za}]];
Print["Misestimated weight residual: ", Together[decode[sum, weighted, wh] - {zj, za} -
   (wh - w) (zj - za) {1, -1}/(1 - 2 wh)]];
sender = {{1, 0}, {a, 1}}; receiver = {{1, b}, {0, 1}};
tag = IdentityMatrix[2] + beta proj;
ref = receiver.sender;
Print["Contemporaneous null and tag trace residuals: ", Simplify[{
 Tr[Inverse[ref].receiver.u.sender] - sum,
 Tr[(Inverse[ref].receiver.tag.sender - IdentityMatrix[2]).Inverse[ref].receiver.u.sender]/beta - weighted}]];
contrast[x_] := (1 - x^2)/(1 + x^2);
Print["Illustrative H, HCl weight contrasts: ", N[contrast /@ ({997807/10^6, 153875/10^5, 353491/10^5}/1000), 10]];
ez = Sin[2 Pi 10^8/(32 10^12)];
rmax[betaAbs_] := 2 ez/(1 + 2/betaAbs + Sqrt[(1 + 2/betaAbs)^2 + 8 ez/betaAbs]);
rr = rmax[2];
Print["Equal quotient allocations, strong and weak marker: ", N[{rr, rmax[1/10]}, 9]];
Print["Strong-marker minimum end gain and max per-matrix error at 0.00254: ",
 N[{Sqrt[(2 + rr)/(rr 10^8)], (254/10^5)^2 rr/(2 + rr)}, 9]];
