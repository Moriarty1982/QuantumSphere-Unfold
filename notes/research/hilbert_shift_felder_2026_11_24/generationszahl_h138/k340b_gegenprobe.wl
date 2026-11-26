(* k340b (H157): unabhaengige Gegenprobe. Allgemeine Polynome in (phi, y1, y2) je Ordnung d,
   Invarianz unter Drehung um 2Pi/3 und Spiegelung y2 -> -y2 direkt gefordert, dann
   J in der Ebene: P(phi, r x, r s) == P(r, phi x, phi s) mit x^2 + s^2 = 1.
   k-Inhalt: Grad in x nach Umschreiben auf cos(3 delta) wird ueber die Potenz von C3 gelesen. *)
ClearAll["Global`*"];
rot = {{-1/2, -Sqrt[3]/2}, {Sqrt[3]/2, -1/2}};
res = Table[
  Module[{mons, cs, P, eqRot, eqRef, sol1, P1, Pplane, PJ, diff, red, eqJ, sol2, P2, free, dimInv, dimJ, kmax, C3poly},
    mons = Flatten[Table[If[a + b <= d, phi^(d - a - b) y1^a y2^b, Nothing], {a, 0, d}, {b, 0, d}]];
    cs = Array[z, Length[mons]];
    P = cs . mons;
    eqRot = Flatten[CoefficientList[Expand[(P /. Thread[{y1, y2} -> rot . {y1, y2}]) - P], {phi, y1, y2}]];
    eqRef = Flatten[CoefficientList[Expand[(P /. y2 -> -y2) - P], {phi, y1, y2}]];
    sol1 = Quiet[Solve[Thread[Join[eqRot, eqRef] == 0], cs]];
    P1 = Expand[P /. First[sol1]];
    dimInv = Length[Variables[P1] \[Intersection] cs];
    Pplane = Expand[P1 /. {y1 -> r x, y2 -> r s}];
    PJ = Expand[P1 /. {phi -> r, y1 -> phi x, y2 -> phi s}];
    diff = Expand[Pplane - PJ];
    red = Last[PolynomialReduce[diff, {s^2 + x^2 - 1}, {s, x, phi, r}]];
    eqJ = Flatten[CoefficientList[red, {phi, r, x, s}]];
    sol2 = Quiet[Solve[Thread[eqJ == 0], Variables[P1] \[Intersection] cs]];
    P2 = Expand[P1 /. First[sol2]];
    free = Variables[P2] \[Intersection] cs;
    dimJ = Length[free];
    (* k-Inhalt: Ebene mit x = Cos[t], s = Sin[t]; Fourier-Ordnung in t / 3 *)
    kmax = If[dimJ == 0, -1,
      Max[Exponent[TrigReduce[Expand[P2 /. {y1 -> r Cos[t], y2 -> r Sin[t]}]] /. Cos[n_. t] :> Q^(n/3), Q]]];
    {d, dimInv, dimJ, kmax}],
  {d, 0, 12}];
Print["Ordnung, invariant, J-erlaubt, hoechstes k (cos 3k delta):"];
Scan[Print, res];
Print["(i) ungerade Ordnung erlaubt? ", Select[res, OddQ[#[[1]]] && #[[3]] > 0 &]];
Print["(ii) erste Ordnung mit k>=1: ", First[Select[res, #[[4]] >= 1 &]][[1]]];
Print["(iii) erste Ordnung mit k>=2: ", First[Select[res, #[[4]] >= 2 &]][[1]]];
(* H157a: N(W) in der Ebene *)
nw[f_, y1_, y2_] := f^3/(3 Sqrt[3]) - f (y1^2 + y2^2)/(2 Sqrt[3]) + (y1^3 - 3 y1 y2^2)/(3 Sqrt[6]);
dN = Simplify[TrigReduce[nw[phi, r Cos[t], r Sin[t]] - nw[r, phi Cos[t], phi Sin[t]]]];
Print["N(W): Rest = ", Factor[dN]];
Print["N(W): Ebenen mit Rest identisch 0: ", Reduce[ForAll[{phi, r}, dN == 0], t, Reals]];
V155[f_, y1_, y2_] := -mu2 (f^2 + y1^2 + y2^2) + lam (f^4 + (y1^2 + y2^2)^2) + kap f^2 (y1^2 + y2^2);
Print["H155-Form: Rest = ", Simplify[V155[phi, r Cos[t], r Sin[t]] - V155[r, phi Cos[t], phi Sin[t]]]];
(* Skala *)
cs = Cos[2/3];
Print["Lambda/v fuer delta = 2/9 (Einheitskoeffizienten): ", N[(2 cs)^(1/6)/Sqrt[2], 10]];
