(* k454b (Test H238): unabhaengige Wolfram-Gegenprobe. Produkt wie k253/k321/k453 (g = -1 an jeder Wand).
   Symbolisch in t: L(t) = Summe |P_perp(u_a u_b)|^2 ; Koide-Identitaet; Werte bei den Brannen-Phasen. *)
cj[x_] := Join[{First[x]}, -Rest[x]];
ml[x_, y_] := If[Length[x] == 1, x y,
  Module[{h = Length[x]/2, a, b, c, d},
   a = x[[;; h]]; b = x[[h + 1 ;;]]; c = y[[;; h]]; d = y[[h + 1 ;;]];
   Join[ml[a, c] - ml[cj[d], b], ml[d, a] + ml[b, cj[c]]]]];
e[i_] := UnitVector[16, i + 1];
u[t_] := Table[Cos[t] e[i] + Sin[t] e[8 + i], {i, 1, 7}];
leak[t_] := Module[{uu = u[t], B, P},
   B = Join[{e[0]}, uu]; P = Transpose[B] . B;
   Total[Flatten[Table[With[{p = ml[a, b]}, (p - P . p) . (p - P . p)], {a, uu}, {b, uu}]]]];
Ls = Simplify[TrigReduce[leak[t]]];
Print["L(t) symbolisch = ", Ls];
Print["L(t) - 42 Sin[3t]^2 = ", Simplify[TrigReduce[Ls - 42 Sin[3 t]^2]]];
Print["Nullstellen in [0,Pi): ", Solve[Ls == 0 && 0 <= t < Pi, t]];
Print["L''(t) an 0, 2Pi/3, 4Pi/3: ", Simplify[D[Ls, {t, 2}] /. t -> #] & /@ {0, 2 Pi/3, 4 Pi/3}];
(* Teil B: Koide *)
a[k_, w_, th_] := 1 + w Cos[th - 2 Pi k/3];
K[w_, th_] := Sum[a[k, w, th]^2, {k, 0, 2}]/Sum[a[k, w, th], {k, 0, 2}]^2;
Print["K(w,th) = ", Simplify[TrigReduce[K[w, th]]]];
Print["K = 2/3 geloest nach w>0: ", Solve[Simplify[K[w, th]] == 2/3 && w > 0, w]];
(* Teil C *)
Do[Print["delta = ", d, ": L/max = Sin[3 delta]^2 = ", N[Sin[3 d]^2, 12], " ; fold-Winkel (Grad) = ",
   N[Mod[3 d, Pi]/3/Degree, 8], " ; direkt leak/42 = ", N[leak[d]/42, 12]], {d, {2222220/10^7, 48399/10^5}}];
