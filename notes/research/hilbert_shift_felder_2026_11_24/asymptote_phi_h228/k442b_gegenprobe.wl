(* k442b: Wolfram-Gegenprobe zu H228 (phi als Asymptote).
   Teil B: Fluss du/dt = -k Sin[3u] mit DSolve/NDSolve, geschlossene Form, t_x/tau, Uhren.
   Teil A: unabhaengige Zaehlung der anziehenden Fixpunkte fuer alle Woerter der Laenge <= 3.
   Aufruf: wolframscript -file k442b_gegenprobe.wl > k442b_out.txt *)

x = Pi/12 - 2222220470731/10^13; sig = 78/10^8;
gl = g /. FindRoot[NSum[2^(1 - g Sqrt[k (k + 2)/3]), {k, 1, Infinity}, WorkingPrecision -> 40] == 1, {g, 186/100}, WorkingPrecision -> 30];
beta = Sqrt[(gl - 1)/(gl + 1)];
Print["gamma_L = ", N[gl, 18], "  beta_sym = ", N[beta, 18], "  x = ", N[x, 12]];

(* Teil B *)
S[p_] := Abs[Cos[Pi/4 - 3 p]] + Abs[Sin[3 p]];
Print["S = 2 Cos[pi/8] Cos[3(phi-pi/8)] auf (0, pi/4), Stichproben-Max-Abw.: ",
  Max@Table[Abs[S[p] - 2 Cos[Pi/8] Cos[3 (p - Pi/8)]], {p, 1/100, 78/100, 1/100}] // N];
sol = DSolve[{u'[t] == -kk Sin[3 u[t]], u[0] == Pi/8}, u[t], t];
Print["DSolve (u = pi/8 - phi, u0 = pi/8): ", Simplify[sol, kk > 0 && t > 0]];
closed[T_] := Pi/8 - 2/3 ArcTan[Tan[3 Pi/16] Exp[-T]];
num = NDSolve[{u'[s] == -(1/3) Sin[3 u[s]], u[0] == Pi/8}, u, {s, 0, 2}, WorkingPrecision -> 30, AccuracyGoal -> 25, PrecisionGoal -> 25];
Print["NDSolve vs geschlossene Form (Einheit tau = 1/(3k)), max |Abw.| auf [0,2]: ",
  N[Max@Table[Abs[(Pi/8 - (u[s] /. num[[1]])) - closed[s]], {s, 0, 2, 1/10}], 3]];
tx = -Log[Tan[3/2 (Pi/8 - x)]/Tan[3 Pi/16]];
Print["t_x/tau = ", N[tx, 12], "   sigma_t = ", N[-Log[Tan[3/2 (Pi/8 - x - sig)]/Tan[3 Pi/16]] - tx, 4]];
clocks = {{"1", 1}, {"1/2", 1/2}, {"1/3", 1/3}, {"1/8", 1/8}, {"ln 2", Log[2]}, {"artanh beta", ArcTanh[beta]},
   {"beta", beta}, {"beta^2", beta^2}, {"1/gamma", 1/gl}, {"1/gamma^2", 1/gl^2}, {"pi/24 (nachtraeglich)", Pi/24}};
Do[Print["  t*/tau = ", c[[1]], ": phi = ", N[closed[c[[2]]], 10], "  Abstand ", N[(closed[c[[2]]] - x)/sig, 6], " sigma"], {c, clocks}];

(* Teil A (so ausgefuehrt: Faltung listenfaehig, Gitter als Ganzes durch die Woerter) *)
xn = N[x]; gn = N[gl, 18]; bn = Sqrt[(gn - 1)/(gn + 1)];
fold[y_] := With[{z = Mod[y, N[Pi/2]]}, z + (N[Pi/2] - 2 z) UnitStep[z - N[Pi/4]]];
ops = <|"h" -> (#/2 &), "d" -> (fold[2 #] &), "s" -> (#/3 &), "t" -> (fold[3 #] &), "X" -> (N[Pi/4] - # &),
   "Y" -> (fold[N[Pi/12] - #] &), "Z" -> (fold[N[Pi/6] - #] &), "B" -> (ArcTan[bn Tan[#]] &),
   "U" -> (fold[ArcTan[Tan[#]/bn]] &), "G" -> (ArcTan[Tan[#]/gn] &)|>;
names = Keys[ops];
grid = N[Subdivide[0, Pi/4, 6000]]; hh = grid[[2]] - grid[[1]];
fixA[w_] := Module[{y, d, idx, pts},
   y = Fold[ops[#2][#1] &, grid, Reverse[w]]; d = y - grid;
   If[Count[Abs[d], v_ /; v < 10^-12] > 0.01 Length[d], Return[$Failed]];
   idx = Flatten@Position[Sign[Most[d]] Sign[Rest[d]], -1];
   pts = Table[{grid[[i]] - d[[i]] hh/(d[[i + 1]] - d[[i]]), (y[[i + 1]] - y[[i]])/hh}, {i, idx}];
   Select[pts, Abs[#[[2]]] < 1 - 10^-9 && 10^-6 < #[[1]] < N[Pi/4] - 10^-6 &]];
words = Flatten[Table[Tuples[names, L], {L, 1, 3}], 1];
res = {}; deg = 0;
Do[With[{f = fixA[w]}, If[f === $Failed, deg++, res = Join[res, {StringJoin[w], #[[1]]} & /@ f]]], {w, words}];
Print["Woerter Laenge <= 3: ", Length[words], ", identitaetsartig ", deg, ", anziehende Fixpunkte ", Length[res], "  (Python: 335)"];
near = First@SortBy[res, Abs[#[[2]] - xn] &];
Print["naechster Fixpunkt zu x: ", near, "  Abstand ", Abs[near[[2]] - xn], "  (Python: GsY 0.0397459, 1.69e-4)"];
Print["N_c(x) fuer Laenge <= 3: ", Count[res, r_ /; Abs[r[[2]] - xn] <= 10^-3 xn], "  (Python: 0)"];
