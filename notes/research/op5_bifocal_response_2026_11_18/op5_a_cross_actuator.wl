ClearAll[k, t, b, dt, db, a, c, d, u, v, p, q, lambda, s];
k[x_] := x[[1]] x[[4]]/(x[[2]] x[[3]]);
t = Array[Unique["t"] &, 4]; b = Array[Unique["b"] &, 4];
dt = Array[Unique["dt"] &, 4]; db = Array[Unique["db"] &, 4];
s = {a c, a d, u c, u d};
Print["Wolfram: ", $Version];
Print["Separable multiplicative factors, residual: ", Together[k[t s] - k[t]]];
Print["Relative disk factorization, residual: ",
  Together[(k[t + dt]/k[b + db])/(k[t]/k[b]) - k[1 + dt/t]/k[1 + db/b]]];
Print["Additive example cross ratio before/after: ", InputForm[{k[{1, 2, 3, 6}], k[{1, 2, 3, 6} + 1/10]}]];
p = Join[Map[Join[#, {0, 0, 0}] &, IdentityMatrix[3]], {
  {1/2, 1/2, 0, 1/Sqrt[2], 0, 0},
  {1/2, 0, 1/2, 0, 1/Sqrt[2], 0},
  {0, 1/2, 1/2, 0, 0, 1/Sqrt[2]}}];
q = Transpose[p].p;
Print["Kelvin reconstruction Gram characteristic polynomial: ", InputForm[Factor[CharacteristicPolynomial[q, lambda]]]];
Print["Kelvin reconstruction determinant, minimum singular value: ",
  InputForm[{Det[p], N[Sqrt[Min[Eigenvalues[q]]], 14], N[1/Sqrt[Min[Eigenvalues[q]]], 14]}]];
