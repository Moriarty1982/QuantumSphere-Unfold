(* k410b (H200): unabhaengige Wolfram-Kontrolle der drei Modell-Fits.
   Stimmt exakt mit der numpy-Rechnung (k410_test_h200.py) ueberein.
   ACHTUNG Fallstrick: N VOR Sort, sonst ordnet Sort die symbolischen
   Ausdrcke 1+Sqrt[2]Cos[...] kanonisch (nicht numerisch) -> Vakuum verdreht. *)
l = Sort[N[Table[1 + Sqrt[2] Cos[2/9 + 2 Pi k/3], {k, 0, 2}]]];
PRS = {{1, 2, 3}, {1, 3, 2}, {2, 3, 1}}; permB = {3, 2, 1};
lk = (l[[#[[3]]]] & /@ PRS)[[permB]];
z = ((l[[#[[1]]]] + l[[#[[2]]]])^2 & /@ PRS)[[permB]];
mu = {7.04*^-6, 3.56*^-3, 0.967}; su = {0.15*^-6, 0.06*^-3, 0.004};
md = {1.54*^-5, 3.06*^-4, 1.630*^-2}; sd = {0.02*^-5, 0.04*^-4, 0.009*^-2};
m6 = Join[mu, md]; s6 = Join[su, sd]; W = 1/s6;
wfit[X_] := Module[{co}, co = LeastSquares[X W, m6 W]; {co, Total[((X.co - m6)/s6)^2]}];
(* (3) voll A,B,C,D *)
X4 = Join[Transpose[{lk/z, lk^2/z, lk/z, lk^2/z}],
    Transpose[{lk/z, lk^2/z, -lk/z, -lk^2/z}]];
(* (2) gradselektiv D=B: Spalten A,C,B; down nur linear *)
X3 = Join[Transpose[{lk/z, lk/z, 2 lk^2/z}], Transpose[{lk/z, -lk/z, 0 lk/z}]];
{co4, chi4} = wfit[X4]; {co3, chi3} = wfit[X3];
(* (1) voll holomorph: up-Fit a,b; down-Vorhersage 0 *)
Wu = 1/su; Xu = Transpose[{lk/z, lk^2/z}]; cou = LeastSquares[Xu Wu, mu Wu];
chi1 = Total[((Xu.cou - mu)/su)^2] + Total[(md/sd)^2];
Print["(3) voll A,B,C,D: chi2 = ", chi4, "   D/B = ", co4[[4]]/co4[[2]]];
Print["(2) D=B strikt:   chi2 = ", chi3, "   p(dof3) = ", 1 - CDF[ChiSquareDistribution[3], chi3]];
Print["(1) voll holo:    chi2 = ", chi1];
