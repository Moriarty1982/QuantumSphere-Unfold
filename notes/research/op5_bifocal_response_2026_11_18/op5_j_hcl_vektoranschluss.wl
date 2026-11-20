ClearAll["Global`*"];
weights = {massH + electronMass, massCl + 17 electronMass};
charges = {4, 122};
positions = {weights[[2]] rel + electronMass dip, -weights[[1]] rel + electronMass dip}/Total[weights];
Print["center-of-mass residual = ", Simplify[weights.positions - electronMass dip]];
Print["relative-coordinate residual = ", Simplify[Subtract @@ positions - rel]];
coeff = Coefficient[charges.positions, rel];
correction = Coefficient[charges.positions, dip];
molecular = {g (b radial + (c - 1) electricLength), e electricLength};
electronic = {-g, e};
columns = Transpose[{electronic, molecular}];
Print["two-column determinant = ", Factor[Det[columns]]];
Print["one-line Gram determinant = ", Factor[Det[Outer[Times, molecular, molecular]]]];
address = {{s11, s12}, {s21, s22}};
Print["drive determinant residual = ", Expand[Det[columns.address] - Det[columns] Det[address]]];
angular = Integrate[3 Cos[theta]^2 Sin[theta]/(2 Sqrt[3]), {theta, 0, Pi}];
Print["rotational projection = ", angular];
(* Mass-number approximation for neutral fragment weights. The radial
   oscillator uses the same reduced mass to leading order. *)
masses = {massH -> 1, massCl -> 35, electronMass -> 1/1823};
b0 = coeff /. masses;
c0 = correction /. masses;
mu = 35/36 (166053906660/10^38);
hbar = 1054571817/10^43;
speed = 299792458;
frequency = 29909463/10000;
radialAngstrom = 10^10 Sqrt[hbar/(2 mu 2 Pi speed 100 frequency)];
dipoleDebye = 719426/10^7;
electronAngstromDebye = (1602176634/10^28) 10^-10/(3335640952/10^39);
electricAngstrom = dipoleDebye/electronAngstromDebye;
waveNumber = 2906246352/10^6;
energyEV = 662607015/10^42 speed 100 waveNumber/(1602176634/10^28);
Print["b and c (mass-number approximation) = ", N[{b0, c0}, 7]];
Print["harmonic radial matrix element [angstrom] = ", N[radialAngstrom, 7]];
Print["electric matrix element length [angstrom], magnitude = ", N[electricAngstrom, 7]];
Print["absolute reduced J/A ratios for signs +,-, in units |g/e| = ", N[Abs[b0 radialAngstrom/(# electricAngstrom) + c0 - 1]& /@ {1,-1}, 6]];
Print["R(0) energy [eV] = ", N[energyEV, 8]];

recoil = 4 electronMass/(massH + electronMass);
hydrogen = {g (recoil - 1), e};
Print["hydrogen and HCl determinant = ", Factor[Det[Transpose[{hydrogen, molecular}]]]];
Print["H recoil factor (mass-number approximation) = ", N[recoil /. masses, 7]];
Print["fractional determinant correction bound for either dipole sign = ",
 N[Abs[(recoil /. masses) - c0] electricAngstrom/(b0 radialAngstrom), 7]];
Print["upper bound on H dynamic/static dipole polarizability ratio = ",
 N[1/(1 - (energyEV/(102/10))^2), 9]];
