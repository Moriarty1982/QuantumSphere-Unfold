(* k369b (Erkundung, 26.11.2026): Wolfram-Gegenrechnung zu k369_abweichung.py.
   Zwei Auswertungen im zustandslosen Kern; Ausgaben in k369b_out.txt. *)

(* --- Auswertung 1: rho-Unabhaengigkeit des Drehwinkels, Zahlen, ungleiche Diagonale --- *)
out = {};
p[s_] := AppendTo[out, s];
m = {{a, b, c}, {b, a, -b}, {c, -b, a}};
ev = Eigenvalues[m] // FullSimplify;
p["Eigenwerte: " <> ToString[ev, InputForm]];
l[k_] := 1 + Sqrt[2] rho Cos[d + 2 Pi k/3];
sol = {a -> 1, c -> l[1] - 1, b2 -> ((l[0] - l[2])^2 - (l[1] - 1)^2)/8};
p["Spur-Kontrolle (soll 0): " <> ToString[FullSimplify[(3 a /. sol) - Sum[l[k], {k, 0, 2}]]]];
p["Summe-Quadrate-Kontrolle (soll 0): " <> ToString[FullSimplify[(3 a^2 + 4 b2 + 2 c^2 /. sol) - Sum[l[k]^2, {k, 0, 2}]]]];
u = {1, 0, -1}/Sqrt[2]; e2 = {0, 1, 0};
blk = FullSimplify[{{u . m . u, u . m . e2}, {e2 . m . u, e2 . m . e2}}];
p["Block: " <> ToString[blk, InputForm]];
t2 = FullSimplify[(8 b2/c^2) /. sol];
p["tan^2(2 phi) = 8 b^2/c^2 = " <> ToString[t2, InputForm]];
p["Differenz zu 3 Tan[d+2Pi/3]^2 - 1 (soll 0): " <> ToString[FullSimplify[t2 - (3 Tan[d + 2 Pi/3]^2 - 1)]]];
p["Ableitung nach rho (soll 0): " <> ToString[FullSimplify[D[t2, rho]]]];
s13obs = 2248/100000; Robs = 30016/1000000;
phiobs = ArcSin[Sqrt[3 s13obs]];
xth = x /. FindRoot[3 Tan[Pi/6 - x + 2 Pi/3]^2 - 1 == Tan[2 phiobs]^2, {x, 0.06}, WorkingPrecision -> 30];
p["x_th = " <> ToString[N[xth, 12]]];
RR[dd_, r_] := Module[{mm = Sort[Table[(1 + Sqrt[2] r Cos[dd + 2 Pi k/3])^2, {k, 0, 2}]]}, (mm[[2]]^2 - mm[[1]]^2)/(mm[[3]]^2 - mm[[1]]^2)];
xR = x /. FindRoot[RR[Pi/6 - x, 1] == Robs, {x, 0.04}, WorkingPrecision -> 30];
p["x_R = " <> ToString[N[xR, 12]]];
rs = r /. FindRoot[RR[Pi/6 - xth, r] == Robs, {r, 0.94}, WorkingPrecision -> 30];
p["rho = " <> ToString[N[rs, 12]] <> ", K_nu = " <> ToString[N[(1 + rs^2)/3, 12]]];
p["x_th/x = " <> ToString[N[xth/(Pi/12 - 0.2222220470731`20), 8]] <> ", x_th/x_R = " <> ToString[N[xth/xR, 8]]];
m3 = {{f, b, c}, {b, dd, -b}, {c, -b, f}};
blk3 = FullSimplify[{{u . m3 . u, u . m3 . e2}, {e2 . m3 . u, e2 . m3 . e2}}];
p["Block ungleiche Diagonale: " <> ToString[blk3, InputForm]];
Do[
 lam = Table[1 + Sqrt[2] Cos[Pi/6 - xx + 2 Pi k/3], {k, 0, 2}];
 lo = SortBy[lam, Abs];
 s3 = FindRoot[{f + c == lo[[1]], (f - c) + dd == lo[[2]] + lo[[3]], (f - c) dd - 2 b^2 == lo[[2]] lo[[3]], Tan[2 phiobs] (dd - f + c) == 2 Sqrt[2] b}, {{f, 0.98}, {dd, 1.03}, {b, 0.23}, {c, -1.18}}, WorkingPrecision -> 25];
 p["x = " <> ToString[N[xx, 8]] <> ": " <> ToString[N[{f, dd, dd - f, b, c} /. s3, 8]]],
 {xx, {Pi/12 - 0.2222220470731`20, xR}}];
StringRiffle[out, "\n"]

(* --- Auswertung 2: x_R mit Klammer (Auswertung 1 lief in die um 4 Pi/3 verschobene Nullstelle) --- *)
Robs = 30016/1000000; s13obs = 2248/100000; phiobs = ArcSin[Sqrt[3 s13obs]];
RR[dd_?NumericQ, r_?NumericQ] := Module[{mm = Sort[Table[(1 + Sqrt[2] r Cos[dd + 2 Pi k/3])^2, {k, 0, 2}]]}, (mm[[2]]^2 - mm[[1]]^2)/(mm[[3]]^2 - mm[[1]]^2)];
xR = x /. FindRoot[RR[Pi/6 - x, 1] == Robs, {x, 4/100, 5/100}, WorkingPrecision -> 30];
xth = x /. FindRoot[3 Tan[Pi/6 - x + 2 Pi/3]^2 - 1 == Tan[2 phiobs]^2, {x, 6/100}, WorkingPrecision -> 30];
xl = Pi/12 - 2222220470731/10^13;
lam = Table[1 + Sqrt[2] Cos[Pi/6 - xR + 2 Pi k/3], {k, 0, 2}]; lo = SortBy[lam, Abs];
s3 = FindRoot[{f + c == lo[[1]], (f - c) + dd == lo[[2]] + lo[[3]], (f - c) dd - 2 b^2 == lo[[2]] lo[[3]], Tan[2 phiobs] (dd - f + c) == 2 Sqrt[2] b}, {{f, 98/100}, {dd, 103/100}, {b, -23/100}, {c, -118/100}}, WorkingPrecision -> 25];
{N[xR, 12], N[xth/xR, 10], N[xth - xR, 10], N[xth/xl, 10], N[{f, dd, dd - f, b, c} /. s3, 8], N[Sin[ArcTan[Sqrt[3 Tan[Pi/6 - xl + 2 Pi/3]^2 - 1]]/2]^2/3, 10]}
