(* k277b (Erkundung, nicht blind): Flavon v in den e7-Anteilen von H3(O), farbneutral = H3(C) mit e7 <-> I.
   Konvention k275: x1 = X23, x2 = X31, x3 = X12. C = L_e7 je Platz. Jordan-Produkt (AB + BA)/2 (C ist assoziativ). *)
X = {{0, I v3, -I v2}, {-I v3, 0, I v1}, {I v2, -I v1, 0}};
Print["X hermitesch: ", Simplify[X == ConjugateTranspose[X], Element[{v1, v2, v3}, Reals]]];
cX[M_] := Module[{Y = M}, Y[[2, 3]] = I M[[2, 3]]; Y[[3, 1]] = I M[[3, 1]]; Y[[1, 2]] = I M[[1, 2]]; Y[[3, 2]] = Conjugate[Y[[2, 3]]]; Y[[1, 3]] = Conjugate[Y[[3, 1]]]; Y[[2, 1]] = Conjugate[Y[[1, 2]]]; Y];
Y = ComplexExpand[cX[X]];
Print["Y = C X: ", Y];
jo[A_, B_] := (A . B + B . A)/2;
Print["det X = ", Simplify[Det[X]], ",  Tr X^2 = ", Simplify[ComplexExpand[Tr[X . X]]]];
Print["det Y = ", Factor[Det[Y]], ",  Tr Y = ", Tr[Y], ",  Tr Y^2 = ", Expand[Tr[Y . Y]]];
Print["Tr(X o Y) = ", Simplify[ComplexExpand[Tr[jo[X, Y]]]]];
Print["Tr((X o Y)^2) = ", Expand[ComplexExpand[Tr[jo[jo[X, Y], jo[X, Y]]]]]];
Print["Tr(X^2 o Y^2) = ", Expand[ComplexExpand[Tr[jo[X . X, Y . Y]]]]];
Print["Tr((Y^2)^2) = ", Factor[Expand[Tr[Y . Y . Y . Y]]]];
s = v1^2 + v2^2 + v3^2;
Print["Kontrolle Tr((XoY)^2) - (s^2 - Sum v^4) = ", Expand[ComplexExpand[Tr[jo[jo[X, Y], jo[X, Y]]]] - (s^2 - (v1^4 + v2^4 + v3^4))]];
Print["Extrema von v1 v2 v3 auf der Einheitssphaere: ", Solve[{v2 v3 == 2 l v1, v1 v3 == 2 l v2, v1 v2 == 2 l v3, s == 1, l != 0}, {v1, v2, v3, l}] // Length, " Loesungen, Betraege: ", Union[Abs[{v1, v2, v3} /. Solve[{v2 v3 == 2 l v1, v1 v3 == 2 l v2, v1 v2 == 2 l v3, s == 1, l != 0}, {v1, v2, v3, l}]]]];
