(* k352b: Gegenprobe zu H161 in Wolfram Language, exakt (unabhaengig von k352).
   Ausgefuehrt am 26.11.2026 ueber den Wolfram-Kernel; Ausgabe in k352b_out.txt. Die K-c-Zeile steht korrigiert in k351b (Punkt 4). *)
px = PauliMatrix[1]; py = PauliMatrix[2]; pz = PauliMatrix[3]; id = IdentityMatrix[2];
P = <|"I" -> id, "X" -> px, "Y" -> py, "Z" -> pz|>;
k[s_] := KroneckerProduct[P[StringTake[s, 1]], P[StringTake[s, {2}]]];
Print["K-a: X.Z + I Y = ", px . pz + I py, " ;  Z.X - I Y = ", pz . px - I py];
Print["K-b: (XX).(ZZ) + YY = ", k["XX"] . k["ZZ"] + k["YY"] // Flatten // Union];
bell = <|"Phi+" -> {1, 0, 0, 1}/Sqrt[2], "Phi-" -> {1, 0, 0, -1}/Sqrt[2], "Psi+" -> {0, 1, 1, 0}/Sqrt[2], "Psi-" -> {0, 1, -1, 0}/Sqrt[2]|>;
Do[Print["   ", b, ": <XX>, <ZZ>, <YY> = ", Table[bell[b] . k[s] . bell[b], {s, {"XX", "ZZ", "YY"}}]], {b, Keys[bell]}];
sq = {{"XI", "IX", "XX"}, {"IZ", "ZI", "ZZ"}, {"XZ", "ZX", "YY"}};
sgn[l_] := (Dot @@ (k /@ l))[[1, 1]];
rows = sgn /@ sq; cols = sgn /@ Transpose[sq];
Print["K-d: Vorzeichen Zeilen ", rows, " Spalten ", cols, " ; Produkte sind Vielfache der Eins: ", And @@ (DiagonalMatrixQ[Dot @@ (k /@ #)] & /@ Join[sq, Transpose[sq]])];
cnt = Table[Module[{v = Partition[2 IntegerDigits[n, 2, 9] - 1, 3]}, Count[Join[Times @@@ v - rows, Times @@@ Transpose[v] - cols], 0]], {n, 0, 511}];
Print["   512 Belegungen: Maximum erfuellter Pruefungen ", Max[cnt], " , Anzahl mit Maximum ", Count[cnt, Max[cnt]], " , Verteilung ", Sort[Tally[cnt]]];
Print["K-e: symmetrischer Fall exakt"];
g = 1/Sqrt[1 - b^2];
boost[{e_, x_, y_, z_}] := {g (e - b z), x, y, g (z - b e)};
l1 = boost[{1, Sin[t/2], 0, Cos[t/2]}]; l2 = boost[{1, -Sin[t/2], 0, Cos[t/2]}];
Print["   n_z' = ", FullSimplify[l1[[4]]/l1[[1]]], " ; Null bei beta = ", Solve[l1[[4]] == 0, b]];
l1b = FullSimplify[l1 /. b -> Cos[t/2], 0 < t < Pi]; l2b = FullSimplify[l2 /. b -> Cos[t/2], 0 < t < Pi];
Print["   bei beta = Cos[t/2]: l1' = ", l1b, " , l2' = ", l2b];
Print["   M^2 = (l1+l2)^2 = ", FullSimplify[(2)^2 - (2 Cos[t/2])^2], " = 2(1 - Cos[t]) : ", FullSimplify[4 - 4 Cos[t/2]^2 - 2 (1 - Cos[t])], " ; E1' - M/2 = ", FullSimplify[l1b[[1]] - Sqrt[2 (1 - Cos[t])]/2, 0 < t < Pi]];
psi[th_, ph_] := {Cos[th/2], Exp[I ph] Sin[th/2]};
Print["   |<psi1|psi2>|^2 - Cos[t/2]^2 = ", FullSimplify[Abs[Conjugate[psi[t/2, 0]] . psi[t/2, Pi]]^2 - Cos[t/2]^2, 0 < t < Pi]];
eta = ArcTanh[Cos[t/2]]; A = DiagonalMatrix[{Exp[-eta/2], Exp[eta/2]}];
Print["   Det A = ", FullSimplify[Det[A]], " ; Ueberlapp der abgebildeten Spinoren = ", FullSimplify[Conjugate[A . psi[t/2, 0]] . (A . psi[t/2, Pi]), 0 < t < Pi]];
Print["   Kreistreue: stereographisch w = Tan[th/2] E^(I ph) -> w E^eta (Streckung, Moebius), bildet Kreise auf Kreise ab"];
Print["   Zahl: beta = beta_sym => theta = ", N[2 ArcCos[0.5494] 180/Pi], " Grad"];
