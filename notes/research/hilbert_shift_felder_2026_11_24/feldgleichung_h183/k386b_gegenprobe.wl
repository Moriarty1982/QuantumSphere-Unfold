(* k386b (Test H183, Wolfram exakt): reelle Unterfamilie x0, xU, r = |c|. Jedes invariante Potential bis Grad 4 hat dort die Form unten
   (gerade in xU wegen der Konjugation, symmetrisch in x0 <-> xU wegen J, Farbe nur ueber r^2). Ausgabe k386b_out.txt. *)
v[x0_, xu_, r_] := a1 (x0^2 + xu^2) + a2 r^2 + b1 (x0^2 + xu^2)^2 + b2 x0^2 xu^2 + b3 r^2 (x0^2 + xu^2) + b4 r^4;
vars = {x0, xu, r};
gradv = D[v[x0, xu, r], {vars}]; hessv = D[v[x0, xu, r], {vars, 2}];
sph[pt_] := Module[{x = pt, g, h, lam, p}, g = gradv /. Thread[vars -> x]; h = hessv /. Thread[vars -> x]; lam = x . g/(x . x);
   p = IdentityMatrix[3] - Outer[Times, x, x]/(x . x); {Simplify[p . g], Simplify[p . (h - lam IdentityMatrix[3]) . p]}];
{gL, hL} = sph[{1, 1, 0}/Sqrt[2]];
Print["L: Gradient = ", gL, "; Kruemmung in der Leptonebene (Richtung (1,-1,0)/Sqrt2) = ", Simplify[{1, -1, 0} . hL . {1, -1, 0}/2], "; Richtung Farbe = ", Simplify[hL[[3, 3]]]];
{gD, hD} = sph[{Cos[th], 0, Sin[th]}];
statD = Simplify[gD . {-Sin[th], 0, Cos[th]}];
Print["D: Stationaritaet entlang theta = ", FullSimplify[statD]];
sol = First[Solve[statD == 0, a2]];
kU = FullSimplify[hD[[2, 2]] /. sol]; kTh = FullSimplify[({-Sin[th], 0, Cos[th]} . hD . {-Sin[th], 0, Cos[th]}) /. sol];
kLp = Simplify[{1, -1, 0} . hL . {1, -1, 0}/2]; kLc = FullSimplify[hL[[3, 3]] /. sol];
Print["nach Stationaritaet bei D: Kruemmung D Richtung U = ", kU, "; D Richtung theta = ", kTh, "; L Leptonebene = ", kLp, "; L Richtung Farbe = ", kLc];
Print["Alle vier > 0 mit 0 < th < Pi/2 loesbar? ", Reduce[kU > 0 && kTh > 0 && kLp > 0 && kLc > 0 && 0 < th < Pi/2, {b1, b2, b3, b4, a1, th}, Reals]];
Print["Nur D (Richtung U) > 0: ", Reduce[kU > 0 && 0 < th < Pi/2, {b2, th}, Reals], "; nur L Leptonebene > 0: ", Reduce[kLp > 0, b2, Reals]];
{gP, hP} = sph[{Cos[th]/Sqrt[2], Cos[th]/Sqrt[2], Sin[th]}];
dirP = {-Sin[th]/Sqrt[2], -Sin[th]/Sqrt[2], Cos[th]};
statP = FullSimplify[gP . dirP]; solP = First[Solve[statP == 0, a2]];
kPth = FullSimplify[(dirP . hP . dirP) /. solP]; kLcP = FullSimplify[hL[[3, 3]] /. solP];
Print["D': Kruemmung Richtung theta = ", kPth, "; L Richtung Farbe = ", kLcP];
Print["D' und L zugleich: ", Reduce[kPth > 0 && kLcP > 0 && 0 < th < Pi/2, {b1, b2, b3, b4, th}, Reals]];
