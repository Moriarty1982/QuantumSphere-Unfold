(* k250: Traegt a - b ein Vorzeichen, das den Drehsinn waehlt? Erkundung, nicht blind (24.11.2026).
   Referenzwahl r14.2: Grundzustand von H = -(a Q + b R), Q = |e0><e0|, R = |u><u|, u = (1,1,1)/Sqrt[3];
   Orbit unter S = diag(1, w, w). Matter-Gewichte werden bewusst NICHT eingesetzt (Betrag bleibt fuer einen
   moeglichen blinden Test offen). Lauf: wolframscript -file k250_drehsinn_lichtgewicht.wl *)
w = Exp[2 Pi I/3]; e0 = {1, 0, 0}; u = {1, 1, 1}/Sqrt[3];
qq = Outer[Times, e0, e0]; rr = Outer[Times, u, u];
hh = -(a qq + b rr);
gs = Simplify[Eigensystem[hh], a > 0 && b > 0];
Print["Eigenwerte: ", Simplify[gs[[1]], a > 0 && b > 0]];
Print["Eigenvektoren: ", Simplify[gs[[2]], a > 0 && b > 0]];
ss = DiagonalMatrix[{1, w, w}];
barg[x_] := Module[{v = {x, 1, 1}, v1, v2}, v1 = ss.v; v2 = ss.v1; Conjugate[v].v1 Conjugate[v1].v2 Conjugate[v2].v];
Print["Bargmann (x reell): ", FullSimplify[barg[x], x \[Element] Reals]];
Print["Im(x^2+2w) fuer reelles x: ", ComplexExpand[Im[x^2 + 2 w]]];
Print["Ueberlapp |<v|Sv>|^2/|v|^4: ", FullSimplify[ComplexExpand[Abs[x^2 + 2 w]^2/(x^2 + 2)^2], x \[Element] Reals]];
Print["Ueberlapp = 1/2 loesen: ", Solve[(x^2 - 1)^2 + 3 == (x^2 + 2)^2/2 && x > 0, x]];
Print["a=b: Grundzustand ", Simplify[Eigensystem[hh /. b -> a][[2]]]];
Print["konjugiertes S: Im(x^2+2 w^2) = ", ComplexExpand[Im[x^2 + 2 w^2]]];
rho = IdentityMatrix[2]/2; uy = MatrixExp[-I k {{0, -I}, {I, 0}}];
Print["U (I/2) U^dagger - I/2 = ", Simplify[uy.rho.ConjugateTranspose[uy] - rho, k \[Element] Reals]];
