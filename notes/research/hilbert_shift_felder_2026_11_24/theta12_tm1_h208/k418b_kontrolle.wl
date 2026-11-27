(* H208 k418b: exakte Gegenpruefung (Wolfram Language)
   (i) v0=(1,0,1)/Sqrt2 ist Eigenvektor von N_hat fuer JEDES b,c (feste TM1-Spalte).
   (ii) exakte TM1-Beziehung sin^2 th12 = (1-3 s13)/(3(1-s13)) aus |U_e1|^2 = 2/3. *)

Nhat = {{1, b, c}, {b, 1, -b}, {c, -b, 1}};
v0 = {1, 0, 1}/Sqrt[2];
resid = Simplify[Nhat . v0 - ((v0 . (Nhat . v0))) v0];
Print["(i) N.v0 - lambda v0 (soll {0,0,0} fuer alle b,c) = ", resid];
lam = Simplify[v0 . (Nhat . v0)];
Print["    Eigenwert zu v0: lambda = ", lam, "  (unabhaengig von b)"];

(* Standard-PMNS: |U_e1|^2 = cos^2 th12 cos^2 th13 = (1-s12)(1-s13); setze = 2/3 *)
sol = Solve[(1 - s12) (1 - s13) == 2/3, s12] // Simplify;
Print["(ii) |U_e1|^2 = (1-s12)(1-s13) = 2/3  =>  sin^2 th12 = ", s12 /. sol[[1]]];
tm1 = (1 - 3 s13)/(3 (1 - s13));
Print["     Differenz zu (1-3 s13)/(3(1-s13)) = ", Simplify[(s12 /. sol[[1]]) - tm1]];
Print["     Wert bei s13 = 0.02248: sin^2 th12 = ", N[tm1 /. s13 -> 0.02248, 8]];
