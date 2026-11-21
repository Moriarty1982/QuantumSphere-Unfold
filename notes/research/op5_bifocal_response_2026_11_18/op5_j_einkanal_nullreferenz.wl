Print["Kernel: ", $Version];
projected = (taa + alpha tja + beta taj + alpha beta tjj)/(1 + alpha beta);
Print["projected correction residual = ", Together[projected - taa -
 (alpha tja + beta taj + alpha beta (tjj - taa))/(1 + alpha beta)]];
logGain[t_] := intercept + slope t + curve t^2/2;
Print["linear log drift and exact quadratic residual = ",
 Expand[logGain[0] - (logGain[-h] + logGain[h])/2 + curve h^2/2]];
Print["null branch ambiguity example = ", FullSimplify[Exp[I Pi {-1, 0, 1}]]];
scalarBudget = 4596/10^9;
tempBudget = 2/10^6;
leakBudget = 2/10^6;
m = 317/10^5;
limit[m_] := leakBudget/(m + Sqrt[m^2 + (2 + leakBudget) leakBudget]);
eps = 25/10^8;
switchLog = 5/10^7;
hSec = 1;
kMax = 2 (Log[1 + tempBudget/(1 + leakBudget)] - switchLog + 2 Log[1 - eps])/hSec^2;
Print["max symmetric amplitude leakage, full marker and diagonal witness = ", N[{limit[m], limit[0]}, 14]];
Print["log drift curvature per s^2 for one second half-window = ", N[kMax, 14]];
Print["remaining reference budget for other effects = ", N[scalarBudget - tempBudget - leakBudget, 14]];
Print["example conservative limits pass = ",
 {((2 m leak + 2 leak^2)/(1 - leak^2) /. leak -> 289/10^6) <= leakBudget,
  N[(1 + leakBudget) (Exp[switchLog + (1999/10^9) hSec^2/2 - 2 Log[1 - eps]] - 1), 30] <= tempBudget}];
