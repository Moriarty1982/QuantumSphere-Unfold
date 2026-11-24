(* k243 Teil A: Fixpunkte der rueckgekoppelten Kaskade (r05.5) mit Gamma = eps H, flach, ohne Strahlung. N = ln a *)
eq = D[om[n], n] == (1 - om[n]) (b2 eps - 3 om[n]);
(* Herleitung: d ln rho_M/dN = -3 + b2 eps (1-om)/om ; d ln rho/dN = -3 om *)
lhs = om (-3 + b2 eps (1 - om)/om) - om (-3 om);
Print["(A1) dOmega/dN aus den Bilanzen = ", Factor[Simplify[lhs]]];
fp = Solve[(1 - o) (b2 eps - 3 o) == 0, o];
Print["(A2) Fixpunkte: ", fp];
Print["(A3) Stabilitaet (Ableitung) bei o=1: ", Simplify[D[(1 - o) (b2 eps - 3 o), o] /. o -> 1], ", bei o=b2 eps/3: ", Simplify[D[(1 - o) (b2 eps - 3 o), o] /. o -> b2 eps/3]];
Print["(A4) Attraktor = beta^2 genau fuer eps = ", Solve[b2 eps/3 == b2, eps]];
Print["(A5) w_eff am Attraktor (eps=3): -1 + Omega = ", -1 + b2 /. b2 -> 0.3018465583, "; Wechselwirkung delta = eps b2 = ", 3*0.3018465583];
sol = DSolve[{D[om[n], n] == 3 (1 - om[n]) (b2 - om[n]), om[0] == o0}, om[n], n];
Print["(A6) Bahn Omega_M(N) fuer eps=3: ", Simplify[sol]];
