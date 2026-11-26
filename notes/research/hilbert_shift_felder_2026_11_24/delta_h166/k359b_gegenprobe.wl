(* k359b (H166): unabhaengige Gegenprobe in Wolfram Language. Ausgabe: k359b_out.txt *)
out = {};
pr[x__] := AppendTo[out, StringJoin[ToString /@ {x}]];
me = 51099895000/10^11; mmu = 1056583755/10^7; ratio = 2067682827/10^7; dratio = 46/10^7;
lam[rho_, d_] := Table[1 + 2 rho Cos[d + 2 Pi k/3], {k, {1, 2, 0}}];
(* a *)
ds = d /. FindRoot[lam[1/Sqrt[2], d][[1]]/lam[1/Sqrt[2], d][[2]] == 1/Sqrt[ratio], {d, 2/9}, WorkingPrecision -> 40];
pr["a(i) delta* = ", NumberForm[ds, 16], "; delta* - 2/9 = ", ScientificForm[ds - 2/9, 5]];
l = lam[1/Sqrt[2], ds]; pr["a(i) m_tau = ", NumberForm[N[mmu (l[[3]]/l[[2]])^2, 20], 12]];
r2 = r /. FindRoot[lam[r, 2/9][[1]]/lam[r, 2/9][[2]] == 1/Sqrt[ratio], {r, 7/10}, WorkingPrecision -> 40];
pr["a(ii) K = ", NumberForm[(1 + 2 r2^2)/3, 16], "; m_tau = ", NumberForm[N[mmu (lam[r2, 2/9][[3]]/lam[r2, 2/9][[2]])^2, 20], 12]];
rb = N[(lam[1/Sqrt[2], 2/9][[2]]/lam[1/Sqrt[2], 2/9][[1]])^2, 30];
pr["a(iii) m_mu/m_e = ", NumberForm[rb, 15], "; Abstand = ", NumberForm[N[(rb - ratio)/dratio, 10], 7], " sigma"];
(* b *)
p3 = Simplify[TrigExpand[D[Cos[2 d] + q Cos[3 d], d]]/Sin[d]] /. Sin[d]^2 -> 1 - Cos[d]^2 // Expand;
p3 = Expand[TrigExpand[D[Cos[2 d] + q Cos[3 d], d]]/Sin[d] /. Sin[d]^2 -> 1 - x^2 /. Cos[d] -> x];
p1 = Expand[TrigExpand[D[Cos[2 d] + q Cos[d], d]]/Sin[d] /. Cos[d] -> x];
pr["b: dV/Sin[d], cos 3d: ", InputForm[Simplify[p3]], "; cos d: ", InputForm[Simplify[p1]]];
pr["b: Cos[2/9] in Algebraics: ", Element[Cos[2/9], Algebraics], "; Tan[2/9] in Algebraics: ", Element[Tan[2/9], Algebraics]];
pr["b: noetiges q (cos 3d) bei 2/9 und 2Pi/3 - 2/9: ", NumberForm[N[-4 x/(12 x^2 - 3) /. x -> Cos[2/9], 12], 10], ", ",
   NumberForm[N[-4 x/(12 x^2 - 3) /. x -> Cos[2 Pi/3 - 2/9], 12], 10]];
(* c *)
S = {{0, 1, 0}, {0, 0, 1}, {1, 0, 0}};
Ln = ({{0, 0, 0}, {0, 0, -I}, {0, I, 0}} + {{0, 0, I}, {0, 0, 0}, {-I, 0, 0}} + {{0, -I, 0}, {I, 0, 0}, {0, 0, 0}})/Sqrt[3];
pr["c(i) MatrixExp[I 2Pi/3 Ln] - S = ", Simplify[MatrixExp[I 2 Pi/3 Ln] - S] // Flatten // Union];
W = a IdentityMatrix[3] + (s + I v) S + (s - I v) Transpose[S];
pr["c(ii) W - (a+2s - 3s Ln^2 - Sqrt3 v Ln) = ", Simplify[W - ((a + 2 s) IdentityMatrix[3] - 3 s Ln . Ln - Sqrt[3] v Ln)] // Flatten // Union];
G = DiagonalMatrix[{Exp[I a1], Exp[I a2], Exp[I a3]}]; Wg = G . W . ConjugateTranspose[G] // ComplexExpand;
pr["c(iii) w12 w23 w31 - b^3 = ", FullSimplify[ComplexExpand[Wg[[1, 2]] Wg[[2, 3]] Wg[[3, 1]] - (s + I v)^3]]];
ev = Table[a + 2 r Cos[de + 2 Pi k/3], {k, 0, 2}];
pr["c(iv) Rest = ", FullSimplify[Sqrt[3] (ev[[3]] - ev[[2]])/(2 ev[[1]] - ev[[2]] - ev[[3]]) - Tan[de]]];
(* d *)
eps0 = ArcTanh[5494056410/10^10]; P = RotateRight[IdentityMatrix[3]];
Cm[rho_, d0_] := IdentityMatrix[3] + rho Exp[I d0] P + rho Exp[-I d0] Transpose[P];
fK[C_, e_] := With[{Dm = DiagonalMatrix[{1, 1, Exp[-3 e]}]}, Dm . C . Dm];
fL[C_, e_] := With[{Wm = DiagonalMatrix[{0, 0, -3}]}, C + e (Wm . C + C . Wm)];
kd[M_] := Module[{e = Sort[Re[Eigenvalues[N[M, 30]]]]}, {Total[e^2]/Total[e]^2, ArcTan[Sqrt[3] (e[[2]] - e[[1]])/(2 e[[3]] - e[[2]] - e[[1]])]}];
nset = {0, Pi/12, Pi/6, Pi/4, Pi/3, (3 ArcCos[1 - 1/Sqrt[2]] - Pi)/3};
pr["d: eps0 = ", NumberForm[N[eps0, 15], 11]];
Do[pr["d vorwaerts ", f, " ", sg, ": ", NumberForm[#, 7] & /@ Table[kd[If[f == "K", fK, fL][Cm[1/Sqrt[2], d0], sg eps0]], {d0, nset}]],
   {f, {"K", "lin"}}, {sg, {1, -1}}];
pr["d: K' in Form K geschlossen (rho^2 = 1/2): ", FullSimplify[Tr[fK[Cm[1/Sqrt[2], d0], e] . fK[Cm[1/Sqrt[2], d0], e]]/Tr[fK[Cm[1/Sqrt[2], d0], e]]^2]];
StringRiffle[out, "\n"]
