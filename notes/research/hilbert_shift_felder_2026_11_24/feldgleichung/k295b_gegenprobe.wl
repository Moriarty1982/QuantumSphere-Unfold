(* k295b (Erkundung, nicht blind): Gegenprobe zu k295 in Wolfram Language.
   psi = psi1 + chi j, psi1 = x0 + I x1, chi = x2 + I x3, A = N(psi1), B = N(chi).
   Aufruf: wolframscript -file k295b_gegenprobe.wl > k295b_out.txt *)
vars = {x0, x1, x2, x3}; A = x0^2 + x1^2; B = x2^2 + x3^2;
(* V1: Einschraenkung des Potentials der vollen Norm auf chi = 0 *)
Print["V1 lambda (N - f^2)^2 bei chi = 0: ", Factor[lam (A + B - f^2)^2 /. {x2 -> 0, x3 -> 0}],
  " ; Koeffizient von A: ", Coefficient[Expand[lam (a + b - f^2)^2 /. b -> 0], a, 1]];
(* V2: Zaehlung der zulaessigen Terme ueber die Erzeuger der Drehungen *)
mons = Select[Flatten[Table[x0^p x1^q x2^r x3^s, {p, 0, 4}, {q, 0, 4}, {r, 0, 4}, {s, 0, 4}]],
   MemberQ[{2, 4}, Total[Exponent[#, vars]]] && EvenQ[Exponent[#, x2] + Exponent[#, x3]] && (# /. {x2 -> 0, x3 -> 0}) === 0 &];
cs = Array[c, Length[mons]]; P = cs . mons;
gL[F_] := -x1 D[F, x0] + x0 D[F, x1] - x3 D[F, x2] + x2 D[F, x3];   (* psi -> e^{i al} psi *)
gR[F_] := -x1 D[F, x0] + x0 D[F, x1] + x3 D[F, x2] - x2 D[F, x3];   (* psi -> psi e^{i be} *)
nullDim[gens_] := Length[mons] - MatrixRank[Normal[CoefficientArrays[
      Flatten[(CoefficientRules[Expand[#[P]], vars][[All, 2]]) & /@ gens], cs][[2]]]];
Print["V2 Monome: ", Length[mons], " ; invariant links und rechts: ", nullDim[{gL, gR}], " ; nur links: ", nullDim[{gL}]];
Print["   B, A B, B^2 invariant (Nullreste): ", Expand[{gL[B], gR[B], gL[A B], gR[A B], gL[B^2], gR[B^2]}]];
z = (x0 + I x1) (x2 - I x3);
Print["   Re und Im von (psi1 conj(chi))^2: links ", Simplify[{gL[ComplexExpand[Re[z^2]]], gL[ComplexExpand[Im[z^2]]]}],
  " , rechts ", Simplify[{gR[ComplexExpand[Re[z^2]]], gR[ComplexExpand[Im[z^2]]]}] =!= {0, 0}];
(* V3: Vakuum *)
V = lA a^2 + ka a b + lB b^2 + m2 b;
sol = First[Solve[{D[V, a] == 0, D[V, b] == 0}, {a, b}]];
Print["V3 stationaer: ", Simplify[sol], " ; A/B = ", Simplify[a/b /. sol], " ; f^2 = ", Factor[a + b /. sol], " ; V = ", Factor[V /. sol]];
bR = First[Solve[D[V /. a -> 0, b] == 0, b]];
Print["   Rand A = 0: ", bR, " ; V = ", Simplify[V /. a -> 0 /. bR], " ; dV/dA = ", Simplify[D[V, a] /. a -> 0 /. bR],
  " ; dV/dB bei A = B = 0: ", D[V, b] /. {a -> 0, b -> 0}];
(* V4: Massen aus der Hesse-Matrix in den vier reellen Komponenten *)
Vx = V /. {a -> A, b -> B}; H = D[Vx, {vars, 2}];
Print["V4 Rand A = 0, chi = (b0, 0): Hesse-Eigenwerte ", Simplify[Eigenvalues[H /. {x0 -> 0, x1 -> 0, x3 -> 0, x2 -> Sqrt[-m2/(2 lB)]}]]];
Vr = V /. {a -> r1^2, b -> r2^2}; Hr = D[Vr, {{r1, r2}, 2}] /. {r1 -> Sqrt[a], r2 -> Sqrt[b]} /. sol;
Print["   innen, Radialmoden (2x2): Determinante ", Factor[Simplify[Det[Hr]]], " ; Spur ", Factor[Simplify[Tr[Hr]]]];
Print["   Beispiel lA = lB = 1, ka = -1, m2 = -1: A, B = ", {a, b} /. sol /. {lA -> 1, lB -> 1, ka -> -1, m2 -> -1},
  " ; Eigenwerte ", Eigenvalues[Hr /. {lA -> 1, lB -> 1, ka -> -1, m2 -> -1}]];
(* V5: Loesung im Anhang psi1 = a0 e^{i p1}, chi = b0 e^{i p2} mit lichtartigen Phasen *)
p1 = k t - k x; p2 = -(kp t - kp y);
f = {a0 Cos[p1], a0 Sin[p1], b0 Cos[p2], b0 Sin[p2]};
eom = Simplify[(D[f, {t, 2}] - D[f, {x, 2}] - D[f, {y, 2}]) + (D[Vx, {vars}] /. Thread[vars -> f])];
Print["V5 Reste der Feldgleichung, geteilt durch das Feld: ", Simplify[eom/f]];
(* V6: Instabilitaet von chi = 0 *)
Print["V6 d^2 V / d chi^2 bei chi = 0: ", Simplify[D[Vx, {x2, 2}] /. {x2 -> 0, x3 -> 0} /. x0^2 + x1^2 -> Aa],
  " => omega^2 = q^2 + 2 (mu2 + kappa A)"];
