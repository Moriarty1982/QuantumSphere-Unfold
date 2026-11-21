(* Symbolic control of the finite-beam two-run calibration. *)
ClearAll["Global`*"];
Print["Kernel: ", $Version];
radLap[f_] := Expand[4 (D[f, s] + s D[f, {s, 2}])/rad^2];
drive[f_] := Expand[b0 f - b2 radLap[f] + b4 Nest[radLap, f, 2]];
ordinaryPotential[f_] := -kg drive[Nest[radLap, f, 2]];
opTide[f_] := -Nest[radLap, f, 5]/(4 m^2);
gTide[f_] := radLap[ordinaryPotential[f]];
gDelay[f_] := -2 ordinaryPotential[f];
signal = -amp rad^6 pInt (s^5 - kappa s^6)/230400;
cal = pInt (36 b2 c3 s^2/(b0 rad^2) + c3 s^3);
calOld = cal + pInt c6 s^6;
calValue = -kg b0 2304 c3 pInt/rad^6;
Print["Signal finite-beam OP5 polynomial residual: ",
  Expand[opTide[signal] - 16 amp pInt (1 - 36 kappa s)/(m^2 rad^4)]];
Print["Original calibration leakage residual: ",
  Expand[opTide[calOld] + 132710400 c6 pInt s/(m^2 rad^10)]];
Print["Annular calibration core residuals: ",
  Expand[{opTide[cal], gTide[cal] - calValue, gDelay[cal] + calValue rad^2 s/2}]];
Print["Signal ordinary degrees: ", {Exponent[gTide[signal], s], Exponent[gDelay[signal], s]}];
Print["Signal-to-calibration axial match residual: ",
  Simplify[((gTide[signal] /. s -> 0) - calValue) /. c3 -> -amp b4 rad^2/(36 b0)]];

mean[f_, base_] := Sum[Coefficient[f, s, j] (base[j] /. base[0] -> 1), {j, 0, Exponent[f, s]}];
mix = lJ mean[gTide[signal], jMom] - lA mean[gTide[signal], aMom];
meanTide = (mean[gTide[signal], jMom] + mean[gTide[signal], aMom])/2;
diffTide = mean[gTide[signal], jMom] - mean[gTide[signal], aMom];
Print["Unequal-mode mean-coupling residual: ",
  Expand[mix - (lJ - lA) meanTide - (lJ + lA) diffTide/2]];
Print["Calibration bias from unmatched first moments residual: ",
  Expand[(mean[gDelay[cal], jMom] - mean[gDelay[cal], aMom]) +
   calValue rad^2 (jMom[1] - aMom[1])/2]];

ratioHat = gsHat/gcHat;
Print["Calibration ratio perturbation residual: ", Together[
  (gsHat + dgs)/(gcHat + dgc) - ratioHat -
  (dgs - ratioHat dgc)/(gcHat + dgc)]];
rho = gs/gc;
normFactor = os - rho oc;
rowS = os lo + gs lg;
rowC = oc lo + gc lg;
Print["Two-run elimination residual: ", Together[rowS - rho rowC - normFactor lo]];
Print["Quotient estimate perturbation residual: ", Together[
  (numHat + dnum)/(denHat + dden) - numHat/denHat -
  (dnum - (numHat/denHat) dden)/(denHat + dden)]];

band = 2 Pi 100000000;
allowance = 1/(4 10^12);
cut = Sin[band allowance/8];
additive = 1/10^8;
endGain = Sqrt[(2 + cut) additive/cut];
idealGain = 254/100000;
Print["Two-run equal-share example {radius, minimum end gain, maximum per-matrix error at 0.00254}: ",
  N[{cut, endGain, idealGain^2 cut/(2 + cut)}, 9]];
