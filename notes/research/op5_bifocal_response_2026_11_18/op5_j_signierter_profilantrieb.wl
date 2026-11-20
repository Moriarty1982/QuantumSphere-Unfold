ClearAll["Global`*"];
Print["kernel version = ", $Version];

pStatic = (z0 omega0^2 + alpha q) (m^2+rm q)-2 gm^2 a^2/3;
axial = Factor[pStatic /. a->0];
Print["axial static drive polynomial = ", axial];
Print["axial exponent-root residuals = ",
  Simplify[(axial /. q->#)& /@ {-m^2/rm,-z0 omega0^2/alpha}]];

greenPositive[z_] := Exp[-kap z]/(2 alpha kap);
Print["Green tail homogeneous residual = ",
  Simplify[-alpha D[greenPositive[z],{z,2}]+alpha kap^2 greenPositive[z]]];
Print["Green derivative jump normalization = ",
  Simplify[-2 alpha (D[greenPositive[z],z]/.z->0)]];
leftMoment = wt1 Exp[-kap z1]+wt2 Exp[-kap z2];
rightMoment = wt1 Exp[kap z1]+wt2 Exp[kap z2];
Print["two-source Cauchy difference = ",
  FullSimplify[Expand[leftMoment rightMoment-(wt1+wt2)^2]-
    2 wt1 wt2 (Cosh[kap (z1-z2)]-1), Element[{kap,z1,z2},Reals]]];

targetXi = targetJ[t]/coupling;
drive = inertia D[targetXi,{t,2}]+stiffness targetXi-coupling targetH[t];
Print["actuator force residual = ",
  Simplify[inertia D[targetXi,{t,2}]+stiffness targetXi-drive-coupling targetH[t]]];
Print["coupled scalar source residual = ",Simplify[coupling targetXi-targetJ[t]]];
energy = scalarStiffness h^2/2+stiffness xi^2/2-coupling h xi;
square = stiffness (xi-coupling h/stiffness)^2/2+
  (scalarStiffness-coupling^2/stiffness) h^2/2;
Print["actuator energy square residual = ",Simplify[energy-square]];
