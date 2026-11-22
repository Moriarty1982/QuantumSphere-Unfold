(* W1 + Holst: Wirkung der Frame-Abbildungen auf den Barbero-Immirzi-Parameter. Methoden-Notiz Commit 1e9a5e2a. Erkundung, nicht blind. *)
eta4 = DiagonalMatrix[{1, -1, -1, -1}];
eps4 = Array[Signature[{##}] &, {4, 4, 4, 4}, 0];       (* eps_{0123} = +1, untere Indizes *)
up[X_] := eta4.X.eta4;                                   (* Bivektor mit oberen Indizes *)
hodge[X_] := Table[1/2 Sum[eps4[[a + 1, b + 1, c + 1, d + 1]] up[X][[c + 1, d + 1]], {c, 0, 3}, {d, 0, 3}], {a, 0, 3}, {b, 0, 3}];
ip[X_, Y_] := 1/2 Total[Flatten[X up[Y]]];               (* <X,Y> = 1/2 X_ab Y^ab *)
biv[s_] := Module[{m = Table[0, {4}, {4}]}, Do[m[[i, j]] = s[i, j]; m[[j, i]] = -s[i, j], {i, 1, 4}, {j, i + 1, 4}]; m];
S = biv[sg]; R = biv[rr];

Print["(1) Hodge^2 = -1 auf Bivektoren: ", Simplify[hodge[hodge[S]] + S] === Table[0, {4}, {4}]];
Print["    <*S,*R> = -<S,R>: ", Simplify[ip[hodge[S], hodge[R]] + ip[S, R]] === 0, ";  <S,*R> = <*S,R>: ", Simplify[ip[S, hodge[R]] - ip[hodge[S], R]] === 0];

lag[A_, B_, X_, Y_] := A ip[hodge[X], Y] + B ip[X, Y];  (* L = A <*Sigma,R> + B <Sigma,R>; W1: A = -1/(2 kappa); Holst: B/A = 1/gamma *)
(* Koeffizienten (a, b) einer Form f[X, Y] = a <*X,Y> + b <X,Y>, bestimmt an zwei festen rationalen Bivektorpaaren und an einem dritten geprueft *)
SeedRandom[22]; rb[] := Module[{r = RandomInteger[{-5, 5}, {4, 4}]}, biv[r[[#1, #2]] &]];   (* jeder Eintrag einmal gezogen *)
pairs = Table[{rb[], rb[]}, {3}];
coef[f_] := Module[{a, b, sol},
   sol = Solve[Table[f @@ pairs[[k]] == a ip[hodge[pairs[[k, 1]]], pairs[[k, 2]]] + b ip[pairs[[k, 1]], pairs[[k, 2]]], {k, 2}], {a, b}];
   {a, b} = {a, b} /. First[sol];
   If[Simplify[f @@ pairs[[3]] - (a ip[hodge[pairs[[3, 1]]], pairs[[3, 2]]] + b ip[pairs[[3, 1]], pairs[[3, 2]]])] =!= 0, Print["    Warnung: Form nicht von der Gestalt a<*X,Y> + b<X,Y>"]];
   {a, b}];

(* (2) Lorentz: reelle Boosts und komplexer Boost mit Rapiditaet eta + i Pi/2 auf Sigma und R zugleich *)
boost[x_] := {{Cosh[x], Sinh[x], 0, 0}, {Sinh[x], Cosh[x], 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
rot[x_] := {{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, Cos[x], -Sin[x]}, {0, 0, Sin[x], Cos[x]}};
act[L_, X_] := Transpose[Inverse[L]].X.Inverse[L];        (* untere Indizes *)
Do[Module[{L = tr[[2]], d},
   d = Simplify[lag[A, B, act[L, S], act[L, R]] - lag[A, B, S, R]];
   Print["(2) ", tr[[1]], ": L invariant: ", d === 0]],
  {tr, {{"Boost x", boost[x]}, {"Drehung y", rot[y]}, {"komplexer Boost eta + i Pi/2", boost[et + I Pi/2]}}}];

(* (3) Dualitaetsdrehung: D1 nur auf R, D2 auf Sigma und R *)
dual[t_, X_] := Cos[t] X + Sin[t] hodge[X];
{a1, b1} = Simplify[coef[Function[{X, Y}, lag[A, B, X, dual[t, Y]]]]];
{a2, b2} = Simplify[coef[Function[{X, Y}, lag[A, B, dual[t, X], dual[t, Y]]]]];
Print["(3) D1: A' = ", a1, ",  B' = ", b1];
Print["    D2: A' = ", a2, ",  B' = ", b2];
(* mit B/A = 1/gamma = Cot[al], al = ArcTan[gamma] *)
g1 = Simplify[a1/b1 /. B -> A Cot[al], 0 < al < Pi/2]; g2 = Simplify[a2/b2 /. B -> A Cot[al], 0 < al < Pi/2];
Print["    gamma' (D1) = ", g1, " ;  Kontrolle Tan[al + t]: ", Simplify[g1 - Tan[al + t]] === 0];
Print["    gamma' (D2) = ", g2, " ;  Kontrolle Tan[al + 2 t]: ", Simplify[TrigExpand[g2 - Tan[al + 2 t]]] === 0];
(* Flaechenquant a ~ kappa gamma = -1/(2 B) wegen A = -1/(2 kappa) *)
q1 = Simplify[(B/b1) /. B -> A Cot[al]]; q2 = Simplify[(B/b2) /. B -> A Cot[al]];
Print["    a'/a (D1) = ", q1, " ;  (D2) = ", q2];

(* (4) Vorab festgelegte Auswertung *)
gM = 0.237533; gT = 0.127384; gL = 1.864700; etaS = ArcTanh[0.5494];
alM = ArcTan[gM];
Print["(4) eta = ", NumberForm[etaS, 7], ", alpha_M = ArcTan[gamma_M] = ", NumberForm[alM, 7]];
thetas = {{"Pi/4", Pi/4}, {"Pi/2 (J_B)", Pi/2}, {"i Pi/2", I Pi/2}, {"eta", etaS}, {"2 eta", 2 etaS}};
Do[Module[{t0 = th[[2]], gp1, gp2, ap1, ap2},
   gp1 = N[Tan[alM + t0]]; gp2 = N[Tan[alM + 2 t0]];
   ap1 = N[Cos[alM]/Cos[alM + t0]]; ap2 = N[Cos[alM]/Cos[alM + 2 t0]];
   Print["    theta = ", th[[1]], ": gamma'(D1) = ", gp1, ", gamma'(D2) = ", gp2, ", a'/a(D1) = ", ap1, ", a'/a(D2) = ", ap2];
   Print["        rel. Abweichung gamma' von gamma_T: ", N[{Abs[gp1/gT - 1], Abs[gp2/gT - 1]}], ";  a'/a von 1/gamma_L: ", N[{Abs[ap1 gL - 1], Abs[ap2 gL - 1]}]]],
  {th, thetas}];
tstar1 = ArcTan[gT] - alM;
Print["(5) theta* mit gamma_M -> gamma_T: D1 ", NumberForm[tstar1, 7], ", D2 ", NumberForm[tstar1/2, 7],
  ";  a'/a dort: ", NumberForm[Cos[alM]/Cos[alM + tstar1], 7]];
