ClearAll["Global`*"];
totalMass = mp + me;
particleMap = {{1, me/totalMass}, {1, -mp/totalMass}};
charges = {{3 g, g}, {e, -e}};
dipoleMap = FullSimplify[charges . particleMap];
chi = DiagonalMatrix[{chiR, chiRrel}];
response = dipoleMap . chi . Transpose[dipoleMap];
rigid = FullSimplify[response /. chiR -> 0];
clampNull = {e, -dipoleMap[[1, 2]]};
zBefore = kappa - mass omega^2 - I eta omega;
zAfter = zBefore + delta;
phaseSlope = FullSimplify[
  ComplexExpand[Im[D[zBefore, omega]/zBefore - D[zAfter, omega]/zAfter]] /. omega -> 0,
  Assumptions -> kappa > 0 && kappa + delta > 0
];
Print["atomic charge = ", charges . {1, 1}];
Print["determinant of dipole map = ", InputForm[Factor[Det[dipoleMap]]]];
Print["internal dipole coefficient, simplified = ", InputForm[dipoleMap[[1, 2]]]];
Print["determinant of driven response = ", InputForm[Factor[Det[response]]]];
Print["clamped-center dark residual = ", FullSimplify[rigid . clampNull]];
Print["electric drive center force = ", dipoleMap[[2, 1]]];
Print["electric drive relative force per field = ", dipoleMap[[2, 2]]];
Print["center loading time shift at zero frequency = ", InputForm[Factor[phaseSlope]]];
