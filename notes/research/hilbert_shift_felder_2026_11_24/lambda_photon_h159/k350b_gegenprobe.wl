(* k350b: Gegenprobe zu k350 (Test H159) in Wolfram Language, Quaternionen als 2x2-Matrizen.
   Aufruf: wolframscript -file k350b_gegenprobe.wl > k350b_out.txt *)
gl = 186444/100000; muM = (gl - 1)/(gl + 1);
(* 1 Tausch J: z -> I Conjugate[z] *)
z[p_, q_] := p Exp[I ph] + q Exp[-I ph];
jz = ComplexExpand[I Conjugate[z[ar + I ai, br + I bi]]];
Print["P1 J z - z(I conj b, I conj a): ", FullSimplify[jz - z[I (br - I bi), I (ar - I ai)], Element[{ar, ai, br, bi, ph}, Reals]]];
ca = ((ar + I ai) + I (br - I bi))/2; cb = ((br + I bi) + I (ar - I ai))/2;
Print["P2 |C a|^2 - |C b|^2: ", Simplify[ComplexExpand[ca Conjugate[ca] - cb Conjugate[cb]]],
  " ; Rang von C: ", MatrixRank[D[ComplexExpand[{Re[ca], Im[ca], Re[cb], Im[cb]}], {{ar, ai, br, bi}}]],
  " ; Im(E^(-I Pi/4) C z): ", FullSimplify[ComplexExpand[Im[Exp[-I Pi/4] z[ca, cb]]], Element[{ar, ai, br, bi, ph}, Reals]]];
(* 2 Stroeme auf der Loesung *)
e = {IdentityMatrix[2], {{I, 0}, {0, -I}}, {{0, 1}, {-1, 0}}, {{0, I}, {I, 0}}};
q[v_] := v . e; cj[M_] := ConjugateTranspose[M];
comp[M_] := ComplexExpand[{Re[M[[1, 1]]], Im[M[[1, 1]]], Re[M[[1, 2]]], Im[M[[1, 2]]]}];
psi = q[{a Cos[w t], a Sin[w t], b Cos[w t], b Sin[w t]}];
Jt = Simplify[comp[ComplexExpand[cj[psi]] . D[psi, t]], Element[{a, b, w, t}, Reals]];
Print["P3 J_t: ", InputForm[Jt], " ; unter a <-> b: J_i -> ", InputForm[Simplify[Jt[[2]] /. {a -> b, b -> a}]], " ; bei a = b: ", InputForm[Jt /. b -> a]];
(* 3 Suche nach K^5 *)
K = (1 + mu)/(1 - mu);
terms = {a^2 + b^2, a^2 - b^2, 2 a b, (a^2 - b^2)^2, (a + b)^2, (a - b)^2, (b^2 - a^2)^2, (a^2 - b^2)^2/(a^2 + b^2)};
stM = {{a -> f/Sqrt[1 + mu^2], b -> mu f/Sqrt[1 + mu^2]}, {b -> mu a}, {a -> f/Sqrt[1 - mu^2], b -> mu f/Sqrt[1 - mu^2]}};
stP = {{a -> f/Sqrt[2], b -> f/Sqrt[2]}, {b -> a}};
stR = {{a -> f, b -> 0}, {b -> 0}, {a -> f, b -> 0}};
ratios = Join[Flatten[Table[Simplify[(tm /. stP[[n]])/(tm /. stM[[n]])], {tm, terms}, {n, 2}]],
   Flatten[Table[Simplify[(tm /. stR[[n]])/(tm /. stM[[n]])], {tm, terms}, {n, 3}]]];
Print["P4 Anzahl Verhaeltnisse: ", Length[ratios], " ; gleich K^5 oder K^-5 als Identitaet: ",
  Count[ratios, r_ /; (Simplify[r - K^5] === 0 || Simplify[r - K^-5] === 0)], " ; gamma_L^5 = ", N[gl^5, 6]];
Print["P5 Exponenten log(r)/log(gamma_L) der endlichen positiven Verhaeltnisse: ",
  Sort[DeleteDuplicates[Round[Select[N[Log[Select[ratios /. mu -> muM, NumericQ[#] && # > 0 &]]/Log[gl]], NumericQ], 0.0001]]]];
(* 4a Fassung F bei mu -> 1 *)
x = {x0, x1, x2, x3}; v = {v0, v1, v2, v3};
J = Simplify[comp[ComplexExpand[cj[q[x]]] . q[v]], Element[Join[x, v], Reals]];
tau = 2 m/(1 - m^2);
PF = (J[[3]]^2 + J[[4]]^2 - tau^2 J[[2]]^2)^2/(x . x)^2;
Print["P6 Limit von P/tau^4 bei mu -> 1 minus J_i^4/N^2: ", Simplify[Limit[PF/tau^4, m -> 1] - J[[2]]^4/(x . x)^2]];
PP = J[[2]]^4/(x . x)^2;
lrot[u_, y_] := Simplify[comp[q[u] . q[y]], Element[Join[x, v], Reals]];
rrot[u_, y_] := Simplify[comp[q[y] . q[u]], Element[Join[x, v], Reals]];
dL[u_] := Simplify[D[PP, {x}] . lrot[u, x] + D[PP, {v}] . lrot[u, v]];
Print["P7 Aenderung von J_i^4/N^2 links um i, j, k: ", {dL[{0, 1, 0, 0}], dL[{0, 0, 1, 0}], dL[{0, 0, 0, 1}]}, " ; rechts um i: ",
  Simplify[D[PP, {x}] . rrot[{0, 1, 0, 0}, x] + D[PP, {v}] . rrot[{0, 1, 0, 0}, v]]];
Print["P8 Kosten b = (1 + d) a: J_i^4/N^2 = ", InputForm[Normal[Series[Jt[[2]]^4/(a^2 + b^2)^2 /. b -> (1 + d) a, {d, 0, 4}]]],
  " ; J_i^2/N = ", InputForm[Normal[Series[Jt[[2]]^2/(a^2 + b^2) /. b -> (1 + d) a, {d, 0, 2}]]]];
c2 = Simplify[D[((Jt[[3]]^2 + Jt[[4]]^2 - tau^2 Jt[[2]]^2)^2/(a^2 + b^2)^2/tau^4) /. b -> (m + d) a, {d, 2}]/2 /. d -> 0];
Print["P9 umskalierte Fassung F, Koeffizient von d^2: ", InputForm[Factor[c2]], " ; bei mu = 1: ", c2 /. m -> 1, " ; bei mu_M (a = w = 1): ", N[c2 /. {m -> muM, a -> 1, w -> 1}, 7]];
(* 4b H132 Stufe A *)
psi0 = q[{f Cos[th], 0, f Sin[th], 0}];
DA = gL L e[[2]] . psi0 - gR R psi0 . e[[2]];
MA = Simplify[D[ComplexExpand[Det[DA]]/2, {{L, R}, 2}]];
Print["P10 Massenmatrix: ", InputForm[MA], " ; det: ", InputForm[Simplify[Det[MA]]], " ; Eigenwerte bei 45 Grad: ", InputForm[Eigenvalues[MA /. th -> Pi/4]],
  " ; det bei th = 0: ", Simplify[Det[MA] /. th -> 0]];
(* 4c J-symmetrisches HC-Potential *)
V[A_, B_, m0_] := eta (B - m0^2 A)^2;
Print["P11 V(A,B) - V(B,A): ", InputForm[Factor[V[A, B, m0] - V[B, A, m0]]]];
VM = Simplify[V[f^2/(1 + mu^2), f^2 mu^2/(1 + mu^2), 1]];
Print["P12 mu0 = 1: V(P) = ", V[f^2/2, f^2/2, 1], " ; V(M) = ", InputForm[Factor[VM]], " ; V(T) - V(M) = ", Simplify[V[f^2 mu^2/(1 + mu^2), f^2/(1 + mu^2), 1] - VM], " ; V(R) = ", V[f^2, 0, 1]];
c2M = ((1 - mu^2)/(1 + mu^2))^2;
Print["P13 cos^2(2 th) bei mu_M: ", N[c2M /. mu -> muM, 7], " ; 1 - mu_M: ", N[1 - muM, 7], " ; reelle Loesungen von cos^2(2 th) = 1 - mu: ",
  N[mu /. Solve[c2M == 1 - mu && mu >= 0, mu, Reals], 6], " ; cos(2 th) in K: ", InputForm[Simplify[(1 - mu^2)/(1 + mu^2) /. mu -> (k - 1)/(k + 1)]]];
Print["P14 mu0 = mu_M: V(P)/V(R) = ", InputForm[Factor[V[f^2/2, f^2/2, m0]/V[f^2, 0, m0]]], " = ", N[(1 - muM^2)^2/(4 muM^4), 6]];
hs = D[V[x0^2 + x1^2, x2^2 + x3^2, 1], {x, 2}] /. {x0 -> f/Sqrt[2], x1 -> 0, x2 -> f/Sqrt[2], x3 -> 0};
Print["P15 Massenquadrate am Vakuum A = B: ", InputForm[Eigenvalues[hs]]];
