(* k434b (H221): unabhaengige Wolfram-Gegenprobe zu k434 (Teile a-d).
   Aufruf: wolframscript -file k434b_gegenprobe.wl > k434b_out.txt *)
v[d_, a_, ap_, chi_, q_] := a Cos[2 d] - ap Cos[2 (d - chi)] + q Cos[3 d];
fold[d_] := Module[{m = Mod[d, 2 Pi/3]}, Min[m, 2 Pi/3 - m]];
dstar = 0.2222220470731; xnu = 0.043359; sxnu = 0.002128;
qS = q /. FindRoot[(D[v[d, 0, 1, Pi/4, q], d] /. d -> 5 Pi/4 + (Pi/12 - dstar)) == 0, {q, -0.08}, WorkingPrecision -> 20];
Print["Weg S geladen: q/alphap = ", NumberForm[qS, 10]];
Do[sol = FindMinimum[v[d, 0, -1, 0, s Abs[qS]], {d, Pi/2 - s 0.05}, WorkingPrecision -> 20];
 dm = d /. sol[[2]]; xp = N[Pi/6 - fold[dm]];
 Print["b) q_nu = ", s, "|q|: Minimum ", NumberForm[N[fold[dm]], 10], "  x_nu,pred = ", NumberForm[xp, 8], "  z = ", NumberForm[(xp - xnu)/sxnu, 4]], {s, {-1, 1}}];
Print["a) neutral Weg K: V = ", Simplify[v[d, a, -1, 0, 0]], " -> Minimum bei pi/2 fuer 1+a>0, x_nu,pred = 0"];
Print["d) geladen: dV/dd bei d = Pi/4+phi+Pi: ", Simplify[D[v[d, 0, 1, Pi/4 + phi, 0], d] /. d -> Pi/4 + phi + Pi], "  zweite Ableitung: ", Simplify[D[v[d, 0, 1, Pi/4 + phi, 0], {d, 2}] /. d -> Pi/4 + phi + Pi]];
Print["d) neutral: dV/dd bei d = Pi/2 + phi: ", Simplify[D[v[d, 0, -1, phi, 0], d] /. d -> Pi/2 + phi], "  zweite Ableitung: ", Simplify[D[v[d, 0, -1, phi, 0], {d, 2}] /. d -> Pi/2 + phi]];
xl = Pi/12 - 2222220470731/10^13; xnuE = 43359/10^6;
Do[{sa, sq} = s;
 fit = Quiet@FindRoot[{(D[v[d1, a, 1, Pi/4, q], d1] /. d1 -> 5 Pi/4 + xl) == 0, (D[v[d2, sa a, -1, 0, sq q], d2] /. d2 -> Pi/2 + xnuE) == 0}, {{a, 0.025}, {q, -0.058}}, WorkingPrecision -> 25];
 {av, qv} = {a, q} /. fit;
 ge = NMinimize[{v[d, av, 1, Pi/4, qv], 0 <= d <= 2 Pi}, d, WorkingPrecision -> 25];
 gn = NMinimize[{v[d, sa av, -1, 0, sq qv], 0 <= d <= 2 Pi}, d, WorkingPrecision -> 25];
 Print["c) s_a=", sa, " s_q=", sq, ": alpha=", NumberForm[av, 6], " q=", NumberForm[qv, 6],
  "  global geladen fold=", NumberForm[fold[d /. ge[[2]]], 8], " (Ziel ", NumberForm[N[Pi/12 - xl], 8], ")",
  "  global neutral fold=", NumberForm[fold[d /. gn[[2]]], 8], " (Ziel ", NumberForm[N[Pi/6 - xnuE], 8], ")"],
 {s, {{1, 1}, {-1, 1}}}];
