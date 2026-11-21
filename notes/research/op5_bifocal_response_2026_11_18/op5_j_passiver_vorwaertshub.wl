ClearAll["Global`*"];
Print["Kernel: ", $Version];
$Assumptions = delta > 0 && gamma > 0 && strength > 0;
response = -strength/(delta + I gamma);
Print["Lorentz phase/loss residual: ", FullSimplify[gamma Re[response] + delta Im[response]]];
transfer = t (1 - r^2)/(1 - r^2 p);
reflection = r (1 - p)/(1 - r^2 p);
Print["Slab transmission and reflection residuals: ", Together[{
 transfer - t - t r^2 (p - 1)/(1 - r^2 p),
 reflection - (r + (-r) (1 - r^2) p/(1 - r^2 p))
}]];
loss = 1/100;
bound = Pi/(-Log[1 - loss]);
e = 360329/10^6;
hs = (662607015/10^42)/(1602176634/10^28);
lambda = hs 299792458/e;
bohr = 529177210544/10^22;
Print["Illustrative {detuning/width, peak/minimum gain, half-band eV}: ",
 N[{bound, Sqrt[1 + bound^2], hs 10^8/2}, 10]];
Print["Ideal atomic H {wavelength m, pi-phase column m^-2}: ",
 N[{lambda, lambda/(4 Pi bohr^3 (9/2))}, 10]];
rr = 981742885/10^14;
Print["Sufficient interface amplitude bound for unmodeled multiple transmission: ",
 N[Sqrt[rr/(2 + rr)], 9]];
