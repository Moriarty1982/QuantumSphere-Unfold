(* k245: Hopf-Luecke als Nullpunkt der Flaeche (Erkundung, nicht blind) *)
(* Zaehlgleichung: Sum_j g(j) Exp[-2 Pi gam a(j)] == 1; M: alle j >= 1/2, g = 2; T: nur j = 1/2, g = 2 *)
specs = {{"jj1", Sqrt[#(# + 1)] &}, {"jplushalf", # + 1/2 &}, {"j", # &}};
gT[a_] := Log[2]/(2 Pi a[1/2]);
gMexact[a_] := Module[{g, y, s},
   s = Simplify[Sum[2 y^(2 a[n/2]), {n, 1, Infinity}], 0 < y < 1];
   y /. Solve[s == 1 && 0 < y < 1, y, Reals]];
Print["--- exakt (y = Exp[-Pi gam]) ---"];
Do[With[{a = sp[[2]]},
   If[sp[[1]] =!= "jj1",
    Module[{ys = gMexact[a], gm},
     gm = -Log[First[ys]]/Pi;
     Print[sp[[1]], ": y_M = ", ys, ", gamma_M = ", gm, ", gamma_T = ", gT[a],
      ", gamma_L = ", FullSimplify[gm/gT[a]],
      ", beta = ", FullSimplify[Sqrt[(gm/gT[a] - 1)/(gm/gT[a] + 1)]],
      ", beta^2 = ", N[(gm/gT[a] - 1)/(gm/gT[a] + 1), 12]]]]], {sp, specs}];
Print["--- numerisch, heute sqrt(j(j+1)) ---"];
gm0 = g /. FindRoot[Sum[2 Exp[-2 Pi g Sqrt[n/2 (n/2 + 1)]], {n, 1, 4000}] == 1, {g, 0.24}, WorkingPrecision -> 30];
Print["gamma_M = ", N[gm0, 12], ", gamma_T = ", N[gT[Sqrt[#(# + 1)] &], 12],
  ", gamma_L = ", N[gm0/gT[Sqrt[#(# + 1)] &], 12],
  ", beta = ", N[Sqrt[(gm0/gT[Sqrt[#(# + 1)] &] - 1)/(gm0/gT[Sqrt[#(# + 1)] &] + 1)], 12]];
Print["--- Abstand der Spektren (Langer) ---"];
Print["j+1/2 - Sqrt[j(j+1)] Reihe: ", Normal[Series[j + 1/2 - Sqrt[j (j + 1)], {j, Infinity, 3}]]];
Print["bei j = 1/2: ", N[1 - Sqrt[3]/2, 12]];
