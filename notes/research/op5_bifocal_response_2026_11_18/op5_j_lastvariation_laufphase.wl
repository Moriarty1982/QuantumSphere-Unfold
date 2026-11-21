Print["Kernel: ", $Version];
m = {{1, 1, 0}, {1, -1/2, Sqrt[3]/2}, {1, -1/2, -Sqrt[3]/2}};
Print["triangle Gram and intercept residuals = ",
 FullSimplify[{Transpose[m].m - DiagonalMatrix[{3, 3/2, 3/2}], {1,1,1}.m/3 - {1,0,0}}]];
xj = gamma (uj + rja xa)/(1 - gamma rjj);
Print["fixed J load residual = ", Together[xj - gamma (uj + rja xa + rjj xj)]];
Print["A-only intercept bias residual = ", Together[(t + raj xj /. xa -> 0) - t - raj gamma uj/(1-gamma rjj)]];
amp = 1/50; eps = 1/10^8;
eT = 2 eps/(1 - Sqrt[2] eps/amp);
logTotal = -4 Log[1 - eT/(99/100)] + 4/10^7;
Print["triangle through and full illustrative log error = ", N[{eT, logTotal}, 14]];
b = 1/10^7;
prod = (317/10^5)^2;
Print["illustrative sufficient fixed-J reflection magnitude = ", N[b/(prod+b), 12]];

hbarc = 1973269804/10^16; e0 = 360329/10^6; dh = 2067833848/10^16;
mass2 = e0^2 (1 - (9999/10000)^2);
phaseErr = 2 ArcSin[1/10000] + 2/10^6;
short = 17/10^7; long = 1/100;
g[e_] := (Sqrt[e^2 - mass2] - e)/hbarc;
bandSignal = Abs[long (g[e0 + dh] - g[e0 - dh])];
Print["short and long branch criteria = ", N[{short e0/(2 hbarc) + phaseErr, long phaseErr/short + phaseErr}, 12]];
Print["long phase, band variation and two-edge error = ",
 N[{long g[e0], bandSignal, 2 phaseErr}, 12]];
ke = {{p,c},{c,s}};
principal = (ksq - omega^2) ke;
massmat = {{m1, m12},{m12, m2}};
Print["minimal mass term absent from homogeneous principal part = ",
 Expand[Coefficient[Det[(lambda^2 principal + massmat)], lambda, 4] - Det[principal]]];
Print["proportional kinetic common characteristic root = ",
 Together[Inverse[ke].ke - IdentityMatrix[2]]];

profile[l_] := l^2 (1-l)^2;
Print["gradient amplitude order and compact Hessian integral = ",
 {Exponent[Expand[epsilon^2 D[profile[l],l]^2],epsilon], Integrate[D[profile[l],{l,2}],{l,0,1}]}];
