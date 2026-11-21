Print["Kernel: ", $Version];
u = (2067833848/10^16)/(360329/10^6);
a0 = 10000 Pi; halfHz = 50 10^6;
tol = 1/(4 10^6);
aCenter = a0 (1 + tol); aMax = aCenter (1 + u);
v = Sqrt[(1/10000 + tol)^2 + tol^2];
rho = v/(2 + 1/10000 - tol);
interface = 2 rho^2/(1 - rho^2);
theta = 3152/10^6;
f0 = (1 + rho)/(1 - rho);
offDiag = f0 theta/(1 - theta);
diagContrastCorrection = f0 ((theta 10^-3) + 2 theta^2/(1 - theta));
aCorrection = f0 theta^2/(1 - theta);
phase = Pi (u + tol + u tol) + aMax tol;
minContrast = 1 + Exp[-aMax tol] Cos[phase] - interface - diagContrastCorrection;
rQ = 981742885/10^14; eZ = Sin[2 Pi 10^8/(32 10^12)];
returnError = 3513/10^9;
floorContrast = 1992/1000; ceilOffDiag = 317/10^5;
referenceBudget = (floorContrast (eZ - rQ) - 2 ceilOffDiag rQ)/(2 (1 + rQ)) - returnError;
unavoidableInBound = u aCenter v + 2 interface;
indexBudget[measurement_] := (referenceBudget - unavoidableInBound - measurement)/aMax;
slopeBudget = indexBudget[2/10^6]/halfHz;
curvatureBudget = 8 (referenceBudget - 2/10^6)/(2 halfHz)^2;
transport = DiagonalMatrix[{zj, za}];
tag = {{tj, c}, {cc, ta}};
misread = {(Tr[tag.transport] - ah Tr[transport])/(jh - ah),
    (jh Tr[transport] - Tr[tag.transport])/(jh - ah)};
Print["diagonal calibration identity residual = ", Together[misread - {zj, za} -
    {1, -1} ((tj - jh) zj + (ta - ah) za)/(jh - ah)]];
Print["contrast lower bound, offdiagonal upper bound, scalar A to full A diagonal error bound = ",
 N[{minContrast, offDiag, aCorrection}, 13]];
Print["contrast and offdiagonal checks = ", {minContrast > floorContrast, offDiag < ceilOffDiag}];
Print["reference budget, nondispersive and interface term = ", N[{referenceBudget, unavoidableInBound}, 13]];
Print["max complex index excursion for zero and 2e-6 measurement error = ", N[indexBudget /@ {0, 2/10^6}, 13]];
Print["index slope per Hz, complex transmission curvature per Hz^2 at 2e-6 measurement error = ",
 N[{slopeBudget, curvatureBudget}, 13]];
scalar[a_, n_] := With[{r = (n - 1)/(n + 1)},
  Exp[I a (n - 1)] (1 - r^2)/(1 - r^2 Exp[2 I a n])];
Print["linear index example, absolute edge drift of scalar tA = ",
 N[Abs[scalar[a0 (1 + u), 1 + 1/10000 + tol] - scalar[a0, 1 + 1/10000]], 13]];
