(* k444b: Wolfram-Gegenprobe zu H230 (Symmetriepunkt pi/8 in den Materie-Frame). Teil B exakt (30 Stellen), Teil A Form K ueber die Eigenwerte von DCD.
   Aufruf: wolframscript -file k444b_gegenprobe.wl > k444b_out.txt *)
beta = 0.549405640974529`30; gl = 1.864699764609373`30; e0 = ArcTanh[beta]; b2 = Tanh[2 e0];
x = Pi/12 - 2222220470731/10^13; sig = 78/10^8;
Print["cosh 2e0 - gamma_L = ", N[Cosh[2 e0] - gl, 5], ", tanh 2e0 = ", N[b2, 10]];
ab[b_, s_][t_] := ArcCos[(Cos[t] - s b)/(1 - s b Cos[t])];
tm[k_][t_] := ArcTan[k Tan[t]];
maps = {{"Ab -beta", ab[beta, 1]}, {"Ab +beta", ab[beta, -1]}, {"Ab -tanh2e", ab[b2, 1]}, {"Ab +tanh2e", ab[b2, -1]},
   {"tan/cosh e0", tm[1/Cosh[e0]]}, {"tan*cosh e0", tm[Cosh[e0]]}, {"tan/gL", tm[1/gl]}, {"tan*gL", tm[gl]},
   {"tan*beta", tm[beta]}, {"tan/beta", tm[1/beta]}, {"tan*tanh2e", tm[b2]}, {"tan/tanh2e", tm[1/b2]}};
c = Flatten[Table[{m[[1]], n, N[m[[2]][n Pi/8]/n, 12]}, {m, maps}, {n, 1, 3}], 1];
c = SortBy[c, Abs[#[[3]] - N[x, 15]] &];
Do[Print["B: ", r[[1]], " n=", r[[2]], ": phi' = ", r[[3]], "  Abstand ", N[(r[[3]] - x)/sig, 6], " sigma"], {r, Take[c, 5]}];
Print["B: Spannweite ", Min[c[[All, 3]]], " .. ", Max[c[[All, 3]]], ", Anzahl ", Length[c]];
pm = RotateRight[IdentityMatrix[3], {1, 0}];
cm[d0_] := IdentityMatrix[3] + (1/Sqrt[2]) Exp[I d0] pm + (1/Sqrt[2]) Exp[-I d0] Transpose[pm];
dm[e_] := DiagonalMatrix[Exp[e {0, 0, -3}]];
kd[m_] := Module[{ev = Sort[Re@Eigenvalues[N[(m + ConjugateTranspose[m])/2, 20]]]}, {Total[ev^2]/Total[ev]^2, ArcTan[Sqrt[3] (ev[[2]] - ev[[1]])/(2 ev[[3]] - ev[[2]] - ev[[1]])]}];
Do[Print["A: Form K, eps = ", s, ": Im ", N[kd[dm[s e0].cm[Pi/12 - Pi/8].dm[s e0]], 7], "  Re ", N[kd[dm[s e0].cm[Pi/6 - Pi/8].dm[s e0]], 7]], {s, {1, -1, 2, -2}}];
Print["A: Datenphase delta*_Im = ", N[Pi/12 - x, 10]];
