(* k388b (H185): exakte Gegenprobe der Zaehlung. Nach Schur genuegt je Farbkomponente die komplexe Struktur L_U:
   Raum = (A, B) (x) drei Plaetze (x) C_U-Struktur, 12 reelle Dimensionen. *)
J = {{0, -1}, {1, 0}}; i2 = IdentityMatrix[2]; i3 = IdentityMatrix[3]; sh = {{0, 1, 0}, {0, 0, 1}, {1, 0, 0}};
Ii = KroneckerProduct[J, i3, i2]; L = KroneckerProduct[i2, i3, J]; S = KroneckerProduct[i2, sh, i2]; Cc = KroneckerProduct[DiagonalMatrix[{1, -1}], i3, i2];
vars = Flatten[Table[x[i, j], {i, 12}, {j, i, 12}]]; X = Table[If[i <= j, x[i, j], x[j, i]], {i, 12}, {j, 12}];
cnt[eqs_] := Length[vars] - MatrixRank[Normal[CoefficientArrays[Flatten[eqs], vars][[2]]]];
base = {X . L - L . X, Transpose[S] . X . S - X};
Print["Formen mit Farbe (Schur: vertauschen mit L_U) und P: ", cnt[base]];
Print["davon vertauschend mit i: ", cnt[Join[base, {X . Ii - Ii . X}]], "; antivertauschend: ", cnt[Join[base, {X . Ii + Ii . X}]]];
Print["mit C: ", cnt[Join[base, {Cc . X . Cc - X}]], "; vertauschend mit i und C: ", cnt[Join[base, {X . Ii - Ii . X, Cc . X . Cc - X}]]];
sol = First[Solve[Flatten[Join[base, {X . Ii - Ii . X}]] == 0, vars] // Quiet]; Xq = X /. sol; free = Variables[Xq];
Print["freie Groessen der ladungserhaltenden Form: ", Length[free]];
Q = IdentityMatrix[12]/2 + Ii . L/6; Print["Ladungen: ", Tally[Eigenvalues[Q]]];
p13 = 3 (2/3 IdentityMatrix[12] - Q); p23 = 3 (Q - 1/3 IdentityMatrix[12]);
Print["Projektoren: ", Simplify[p13 . p13 - p13] === ConstantArray[0, {12, 12}], " ", Simplify[p13 . Xq - Xq . p13] === ConstantArray[0, {12, 12}]];
e13 = Factor[CharacteristicPolynomial[p13 . Xq, z]]; e23 = Factor[CharacteristicPolynomial[p23 . Xq, z]];
Print["char. Polynom auf Ladung 1/3: ", e13]; Print["char. Polynom auf Ladung 2/3: ", e23];
sol2 = First[Solve[Flatten[Join[base, {X . Ii - Ii . X, Cc . X . Cc - X}]] == 0, vars] // Quiet]; Xc = X /. sol2;
Print["mit C: Differenz der char. Polynome fuer 1/3 und 2/3 = ", Simplify[CharacteristicPolynomial[p13 . Xc, z] - CharacteristicPolynomial[p23 . Xc, z]]];
sol3 = First[Solve[Flatten[Join[base, {X . Ii + Ii . X}]] == 0, vars] // Quiet]; Xm = X /. sol3;
Print["ladungsmischende Form: p13.Xm.p13 = 0? ", Simplify[p13 . Xm . p13] === ConstantArray[0, {12, 12}], "; p13.Xm.p23 = 0? ", Simplify[p13 . Xm . p23] === ConstantArray[0, {12, 12}]];
