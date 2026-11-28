(* H215 (k428b): unabhaengige Gegenprobe in Wolfram Language.
   beta_sym neu aus der Zaehlregel (Summe bis k = 400, Rest < 1e-120), Zaehlung N fuer Woerter der Laenge <= 3
   mit eigenem Gitter im Fenster (201 Teile, Nullstellen auf dem Gitter mitgezaehlt) und FindRoot. *)
Fz[g_?NumericQ] := Sum[2^(1 - g Sqrt[k (k + 2)/3]), {k, 1, 400}] - 1;
gL = g /. FindRoot[Fz[g], {g, 186/100}, WorkingPrecision -> 40];
beta = Sqrt[(gL - 1)/(gL + 1)]; b0 = N[beta];
Print["gamma_L = ", N[gL, 20], "   beta_sym = ", N[beta, 20]];
ops = <|"H" -> (1 - 2 # (1 - #) &), "S" -> (#^2 &), "R" -> (Sqrt[#] &), "C" -> (1 - # &),
   "A" -> (2 #/(1 + #^2) &), "W" -> (#/(1 + Sqrt[1 - #^2]) &), "G" -> ((1 - #^2)/(1 + #^2) &),
   "D" -> (2 # Sqrt[1 - #^2] &), "E" -> (2^(1 - (1 + #^2)/(1 - #^2)) &)|>;
words = Flatten[Table[StringJoin /@ Tuples[Keys[ops], len], {len, 1, 3}]];
fun[w_] := Composition @@ (ops /@ Characters[w]);
rel = 0.00065;
attractIn[w_, x0_] := Quiet@Module[{f = fun[w], xs, ds, roots},
  xs = Subdivide[x0 (1 - rel), x0 (1 + rel), 201]; ds = (f /@ xs) - xs;
  If[Max[Abs[ds]] < 10^-12, Return[False]];
  roots = Table[If[ds[[i]] ds[[i + 1]] <= 0, x /. FindRoot[f[x] - x, {x, xs[[i]], xs[[i + 1]]}], Nothing], {i, Length[xs] - 1}];
  AnyTrue[roots, Abs[f'[#]] < 1 &]];
hitsB = Select[DeleteCases[words, "E"], attractIn[#, b0] &];
Print["Woerter Laenge <= 3: ", Length[words]];
Print["N(beta_sym), Laenge <= 3, ohne E: ", Length[hitsB], "  ", hitsB];
h2 = Select[words, attractIn[#, 0.5] &]; h3 = Select[words, attractIn[#, 1/3.] &];
Print["N(1/2), Laenge <= 3: ", Length[h2], " ", Take[h2, UpTo[12]]];
Print["N(1/3), Laenge <= 3: ", Length[h3], " ", h3];
xE = x /. FindRoot[ops["E"][x] == x, {x, 55/100}, WorkingPrecision -> 30];
Print["Fixpunkt von E: ", N[xE, 15], "  Abstand zu beta_sym: ", N[xE - beta, 5], "  E'(x*) = ", N[ops["E"]'[xE], 6]];
