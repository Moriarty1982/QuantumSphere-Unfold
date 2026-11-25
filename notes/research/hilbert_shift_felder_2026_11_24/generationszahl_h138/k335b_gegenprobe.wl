(* k335b (H152): Gegenprobe in Wolfram Language zu k335_erweiterter_ansatz.py (Wolfram-Cloud-Kernel, ein Aufruf):
   beta-Funktionen des erweiterten Ansatzes ueber SolveAlways, delta-Abhaengigkeit auf der Kugel, Massen bei delta = 0 und pi/3. *)
f = {p, y1, y2, c0, c1, c2, c3};
B = y1^2 + y2^2; Q = c0^2 + c1^2 + c2^2 + c3^2; C3 = y1^3 - 3 y1 y2^2;
bas = {p^4, p^2 B, B^2, p C3, p^2 Q, B Q, Q^2};
V = {lA, ka, lB, xi, kC, kBC, lC} . bas;
H = D[V, {f, 2}]; rhs = Expand[Tr[H . H]/2];
sol = First@SolveAlways[rhs == Array[bb, 7] . bas, f];
Print["beta: ", Thread[{"lA", "ka", "lB", "xi", "kC", "kBC", "lC"} -> Factor[Array[bb, 7] /. sol]]];
Vs = V /. {p -> Cos[t], y1 -> Sin[t] Cos[d], y2 -> Sin[t] Sin[d], c0 -> 0, c1 -> 0, c2 -> 0, c3 -> 0};
Print["delta-Abhaengigkeit auf der Kugel: ", Simplify[Vs - (Vs /. d -> Pi/6)]];
ck[t_, d_] := Table[Cos[t]/Sqrt[3] + Sqrt[2/3] Sin[t] Cos[d - 2 Pi k/3], {k, 0, 2}];
Print["Massen bei delta = 0: ", Simplify[ck[t, 0]^2], " ; bei delta = pi/3: ", Simplify[ck[t, Pi/3]^2]];
