(* Exact checks for the initial plateau and a regularized action. *)
ClearAll["Global`*"];
Print["Kernel: ", $Version];
dust = {{0, n0}, {0, 0}};
Print["Pressureless symbol rank and nilpotence: ", {MatrixRank[dust], dust.dust}];
Print["Pressureless Fourier propagator residual: ",
  Simplify[MatrixExp[-I k t dust] - (IdentityMatrix[2] - I k t dust)]];

carrierEnergy = m n + kap (n - n0)^2/(2 n0);
pressure = n D[carrierEnergy, n] - carrierEnergy;
Print["Pressure penalty value, derivative and acoustic-speed residuals: ",
  Simplify[{carrierEnergy - m n, D[carrierEnergy - m n, n], pressure,
    D[pressure, n]/D[carrierEnergy, n] - kap/m} /. n -> n0]];

displacement = u[t, x];
phase = q[t, x];
lagrangian = rho D[displacement, t]^2/2 - modulus D[displacement, x]^2/2 +
  inertia D[phase, t]^2/2 - gradCost (D[phase, x] + D[displacement, t])^2/2;
pU = D[lagrangian, D[displacement, t]];
pQ = D[lagrangian, D[phase, t]];
equation[field_, momentum_] := D[momentum, t] + D[D[lagrangian, D[field, x]], x];
plane = Exp[I (k x - omega t)];
symbol = Table[
  Simplify[D[equation[pair[[1]], pair[[2]]] /.
      {u -> Function[{tt, xx}, amplitudeU Exp[I (k xx - omega tt)]],
       q -> Function[{tt, xx}, amplitudeQ Exp[I (k xx - omega tt)]]}, amp]/plane],
  {pair, {{displacement, pU}, {phase, pQ}}}, {amp, {amplitudeU, amplitudeQ}}];
wanted = {{modulus k^2 - (rho - gradCost) omega^2, -gradCost k omega},
  {-gradCost k omega, gradCost k^2 - inertia omega^2}};
poly = (rho - gradCost) inertia z^2 -
  (modulus inertia + rho gradCost) z + modulus gradCost;
Print["Longitudinal symbol and characteristic polynomial residuals: ",
  Simplify[{symbol - wanted, (Det[symbol] /. {omega^4 -> z^2 k^4, omega^2 -> z k^2}) - k^4 poly}]];
Print["Quadratic energy residual: ", Expand[
  pU D[displacement, t] + pQ D[phase, t] - lagrangian -
  ((rho - gradCost) D[displacement, t]^2 + inertia D[phase, t]^2 +
   modulus D[displacement, x]^2 + gradCost D[phase, x]^2)/2]];
Print["Positive discriminant identity residual: ", Expand[
  Discriminant[poly, z] - (modulus inertia - rho gradCost)^2 -
  4 modulus inertia gradCost^2]];
example = {rho -> 1, modulus -> 1/2, inertia -> 1, gradCost -> 1/8};
Print["Example longitudinal squared-speed polynomial residual: ",
  Expand[(poly /. example) - 7/8 (z - (5 + Sqrt[11])/14) (z - (5 - Sqrt[11])/14)]];

(* Metric derivatives at rest, to first order in phase and matrix velocity errors. *)
metric = {{-1 + h00, h01}, {h01, 1}};
timelike = {1, vel}/Sqrt[-{1, vel}.metric.{1, vel}];
phaseGrad = {1 + rate, slope};
clockArg = timelike.phaseGrad - 1;
perpNorm = phaseGrad.Inverse[metric].phaseGrad + (timelike.phaseGrad)^2;
clockDensity = Sqrt[-Det[metric]] Sqrt[(Inverse[metric])[[2, 2]] -
  2 vel (Inverse[metric])[[1, 2]] + vel^2 (Inverse[metric])[[1, 1]]];
clockL = clockDensity (inertia clockArg^2 - gradCost perpNorm)/2;
clockT = {2 D[clockL, h00], D[clockL, h01]} /. {h00 -> 0, h01 -> 0};
linearize[expr_] := Simplify[SeriesCoefficient[expr /. {vel -> e vel, rate -> e rate, slope -> e slope}, {e, 0, 1}]];
Print["Clock energy and momentum density residuals: ",
  Simplify[Map[linearize, clockT] - {inertia rate, -gradCost (slope + vel)}]];
Print["Static quadrupole kernel residual: ", FullSimplify[
  D[1/Sqrt[x^2 + y^2 + zz^2], {zz, 2}] -
  (3 zz^2 - (x^2 + y^2 + zz^2))/(x^2 + y^2 + zz^2)^(5/2)]];
