(* k392b: Gegenprobe zu k392 in Wolfram Language. H189a symbolisch, H189b exakt, H189c (Variante 1) im reduzierten Modell
   (Vakuum diagonal, komplexer Eintrag). Ausgabe: k392b_out.txt *)
nn[X_] := Total[Flatten[ComplexExpand[Abs[X]^2]]]; ip[X_, Y_] := Total[Flatten[ComplexExpand[Re[Conjugate[X] Y]]]];
k1[X_, Y_] := nn[X] nn[Y] - ip[X, Y]^2; k2[X_, Y_] := nn[X . Y - Y . X]; k4[X_, Y_] := nn[X . Y] + nn[Y . X] - 2 nn[X] nn[Y];
A = Array[a, {3, 3}]; B = Array[b, {3, 3}]; zero = ConstantArray[0, {3, 3}];
Print["H189a: K1, K2, K4 mit X_x = 0 (allgemeine reelle 3x3-Matrix fuer X_t): ", {k1[A, zero], k2[A, zero], k4[A, zero]}];
d = DiagonalMatrix[{l1, l2, l3}]; B0 = I d;
fl[p_, q_] := Module[{m = ConstantArray[0, {3, 3}]}, m[[p, q]] = x + I y; m[[q, p]] = x - I y; m];
Print["H189c, Variante 1 im reduzierten Modell (Vakuum diagonal, Eintrag (p,q) = x + i y, Norm der Koordinaten x^2 + y^2 = 1):"];
Do[Module[{f = fl[p, q], r = {x^2 -> 1 - y^2}},
  Print["  Paar ", {p, q}, ": g1 = ", Factor[Simplify[k1[B0, f] /. r]], ", g2 = ", Factor[Simplify[k2[B0, f] /. r]], ", g4 = ", Simplify[k4[B0, f] /. r]]], {p, 1, 2}, {q, p + 1, 3}];
Print["  Reste Paar (1,2): ", Simplify[{k1[B0, fl[1, 2]] - (2 (l1^2 + l2^2) + 2 l3^2), k2[B0, fl[1, 2]] - 2 (l1 - l2)^2, k4[B0, fl[1, 2]] - (-2 (l1^2 + l2^2) - 4 l3^2)} /. x^2 -> 1 - y^2]];
Print["H189b: Ansatz d = v Exp[I Om t], I v = I s v in d'' + 2 om I d' - om^2 d + h d = 0: Loesungen Om = ", Om /. Solve[-Om^2 - 2 s om Om - om^2 + h == 0 /. s -> 1, Om], " (s = +1), ", Om /. Solve[-Om^2 - 2 s om Om - om^2 + h == 0 /. s -> -1, Om], " (s = -1)"];
g2v = {11417098, 1057332, 5525570}/10^6; g4v = {-6194301, -9647556, -8158143}/10^6;
Print["Variante 2 (Zahlen aus k392_out.txt): g2 - 3 g4 = ", N[g2v - 3 g4v, 8]];
