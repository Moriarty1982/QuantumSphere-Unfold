Print["Kernel: ", $Version];
cross[v_] := v[[1]] v[[4]]/(v[[2]] v[[3]]);
y = {a0 b0 w00, a0 b1 w01, a1 b0 w10, a1 b1 w11 q};
z = {c0 d0 v00, c0 d1 v01, c1 d0 v10, c1 d1 v11};
Print["cross quotient and witness residuals = ", Together[{
 cross[y] - q cross[{w00, w01, w10, w11}],
 cross[y]/cross[z] - q cross[{w00, w01, w10, w11}]/cross[{v00, v01, v10, v11}],
 cross[y /. {q -> k q, w11 -> w11/k}] - cross[y]}]];
c4 = {1, -1, -1, 1};
c8 = {1, -1, -1, 1, -1, 1, 1, -1}/2;
Print["difference kernel residuals = ", Expand[{
 c4 . w^Range[0, 3] - (1 - w) (1 - w^2),
 c8 . w^Range[0, 7] - (1 - w) (1 - w^2) (1 - w^4)/2}]];
Print["drift moments {four up to order two, eight up to order three} = ",
 {Table[c4 . ((Range[4] - 5/2)^i), {i, 0, 2}],
  Table[c8 . ((Range[8] - 9/2)^i), {i, 0, 3}]}];
budget = 2/10^6;
qMax = 1 + 2/10^6;
noise = 1/10^7;
mismatch = 5/10^7;
step = 1/4;
logBudget = Log[1 + budget/qMax] - mismatch + 8 Log[1 - noise];
Print["differential gain budgets {log drift, second derivative per s^2, third derivative per s^3} = ",
 N[{logBudget, logBudget/(2 step^2), logBudget/(4 step^3)}, 13]];
Print["rounded bounds pass = ",
 N[qMax (Exp[mismatch - 8 Log[1 - noise] + #] - 1), 30] <= budget & /@
  {2 step^2 (559/10^8), 4 step^3 (1119/10^8)}];
