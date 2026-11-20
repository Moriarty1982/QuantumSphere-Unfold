ClearAll["Global`*"];
kinetic = {{1, 1/4}, {1/4, 1}};
electron = {1, -2};
delay = g Outer[Times, electron, electron];
reference = {1, 0};
ports = Transpose[{electron, reference}];
left = {{2, 1}, {1, 1}};
right = {{1, I}, {1, 2}};
propagation = {{a, b}, {c, d}};
measured = Inverse[left . right] . (left . propagation . right);
Print["K eigenvalues = ", InputForm[Sort[Eigenvalues[kinetic]]]];
Print["electron K^-1 norm squared = ", InputForm[electron . Inverse[kinetic] . electron]];
Print["normalized generalized characteristic polynomial = ",
  InputForm[Factor[Det[t kinetic - delay]/Det[kinetic]]]];
Print["rank one electron port = ", MatrixRank[Outer[Times, electron, {1, 2}]]];
Print["two-port Gram determinant = ", InputForm[Det[Transpose[ports] . Inverse[kinetic] . ports]]];
Print["similarity residual = ", Simplify[measured - Inverse[right] . propagation . right]];
Print["characteristic polynomial residual = ",
  Expand[CharacteristicPolynomial[measured, z] - CharacteristicPolynomial[propagation, z]]];
