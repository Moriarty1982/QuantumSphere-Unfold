(* k362b (H167): unabhaengige Gegenprobe in Wolfram Language. Ausgabe: k362b_out.txt *)
out = {}; pr[x__] := AppendTo[out, StringJoin[ToString /@ {x}]];
S = {{0, 1, 0}, {0, 0, 1}, {1, 0, 0}};
z = (1 + I c) (s + I v); zb = (1 - I c) (s - I v);
W = a IdentityMatrix[3] + z S + zb Transpose[S]; Wc = a IdentityMatrix[3] + zb S + z Transpose[S];
pr["a: Tr(W o sigma W) - (3a^2 + 6[(1-c^2)(s^2-v^2) - 4csv]) = ", Simplify[Tr[W . Wc] - (3 a^2 + 6 ((1 - c^2) (s^2 - v^2) - 4 c s v))]];
sub = {s -> r Cos[d - ArcTan[c]]/Sqrt[1 + c^2], v -> r Sin[d - ArcTan[c]]/Sqrt[1 + c^2]};
pr["a: Re z^2 - r^2 Cos[2d] = ", FullSimplify[(ComplexExpand[Re[z^2]] /. sub) - r^2 Cos[2 d]]];
pr["a: (1+c^2)v^2 - r^2 Sin[d-chi]^2 = ", FullSimplify[((1 + c^2) v^2 /. sub) - r^2 Sin[d - ArcTan[c]]^2]];
mins[al_, alp_, cc_] := Module[{ch = ArcTan[cc], d0}, d0 = (ArcTan[al - alp Cos[2 ch], -alp Sin[2 ch]] + Pi)/2; {d0, d0 + Pi}];
fold[d_] := Module[{m = Mod[d, 2 Pi/3]}, Min[m, 2 Pi/3 - m]];
pr["a: alpha=0, alphap=1, c=1: gefaltet ", FullSimplify[fold /@ mins[0, 1, 1]], "; alphap=-1: ", FullSimplify[fold /@ mins[0, -1, 1]]];
pr["a: alphap=0, alpha=1, c=7/10: gefaltet ", FullSimplify[fold /@ mins[1, 0, 7/10]], "; alpha=-1: ", FullSimplify[fold /@ mins[-1, 0, 7/10]]];
detK[x_] := FullSimplify[Det[IdentityMatrix[3] + (Exp[I x] S + Exp[-I x] Transpose[S])/Sqrt[2]]];
pr["a: det W (K=2/3) = ", detK[x], "; bei Pi/12: ", detK[Pi/12], "; bei Pi/4: ", detK[Pi/4]];
V4 = mu2 (A^2 + B^2) + lam (A^4 + B^4) + kap A^2 B^2 + A^2 B^2 (al Cos[2 d] - alp Cos[2 (d - ch)]);
pr["b: V4(A<->B) - V4 = ", Simplify[(V4 /. {A -> B, B -> A}) - V4], "; V4(-A) - V4 = ", Simplify[(V4 /. A -> -A) - V4], "; V4(d+Pi) - V4 = ", Simplify[(V4 /. d -> d + Pi) - V4]];
pr["b: quadratisch (B^2/2 Cos[2d]) unter Tausch: ", Simplify[(A^2/2 Cos[2 d]) - (B^2/2 Cos[2 d])]];
ds = 2222220470731/10^13;
pr["c: delta - Pi/12 bei rho=1/100 (c=1, Oktant-Zweig): ", N[fold[mins[1/100, 1, 1][[2]]] - Pi/12, 10], " ; -ArcTan[1/100]/2 = ", N[-ArcTan[1/100]/2, 10]];
pr["d: Tan[Pi/6 - 2 delta*] = ", N[Tan[Pi/6 - 2 ds], 12], "; rho-Ziele: ",
  N[Sort[Flatten[Table[With[{dm = sg ds + 2 Pi m/3 + k Pi}, Cos[2 dm]/Sin[2 dm]], {sg, {1, -1}}, {m, 0, 2}, {k, 0, 1}]]] // Union[#, SameTest -> (Abs[#1 - #2] < 10^-9 &)] &, 11]];
pr["d: 1/(4 Pi) = ", N[1/(4 Pi), 10], "; relativ zu rho*: ", N[(1/(4 Pi) - Tan[Pi/6 - 2 ds])/Tan[Pi/6 - 2 ds], 4]];
pr["Kontrolle c: Tan[delta* + Pi/6] = ", N[Tan[ds + Pi/6], 12], "; Cos[Pi/8] = ", N[Cos[Pi/8], 12], "; ArcTan[Cos[Pi/8]] - Pi/6 - delta* = ", N[ArcTan[Cos[Pi/8]] - Pi/6 - ds, 5]];
StringRiffle[out, "\n"]
