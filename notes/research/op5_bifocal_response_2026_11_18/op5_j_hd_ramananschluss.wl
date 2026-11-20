ClearAll["Global`*"];
assumptions = Element[{phiT, phiR, dT, dR, cT, cR, tau, omega}, Reals];
pumpTx = Exp[I (phiT + dT omega)];
pumpRx = Exp[I (phiR + dR omega)];
transfer = FullSimplify[Conjugate[pumpTx] pumpRx Exp[I tau omega], assumptions];
slope = FullSimplify[Im[D[transfer, omega]/transfer], assumptions];
parity = DiagonalMatrix[{1, -1, 1}];
raman = {{r0, 0, r2}, {0, r1, 0}, {r2, 0, r3}};
dipole = {{0, j1, 0}, {j1, 0, j2}, {0, j2, 0}};
sameInitial = {1, 0, 0};
Print["Raman parity residual = ", parity . raman . parity - raman];
Print["dipole parity residual = ", parity . dipole . parity + dipole];
Print["unoriented cross overlap = ", sameInitial . dipole . raman . sameInitial];
Print["first-order oriented rotor overlap = ", 
  InputForm[FullSimplify[(f/(2 b0 Sqrt[3]) + f/(2 b1 Sqrt[3]))/Sqrt[3]]]];
Print["phase slope including both pump paths = ", InputForm[slope]];
Print["HD Q(0) energy in eV = ", NumberForm[3632.16052 1.239841984*^-4, 9]];
