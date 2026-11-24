(* k271 (Erkundung, nicht blind, 24.11.2026): unabhaengige Wolfram-Kontrolle zu k270 Teil C und zur HS(0)-Gleichung.
   Turm-Modell: Sektoren k = 0..N_c, Q = k/N_c, Vielfachheit Binomial[N_c,k]; gerade k links (schwaches Dublett, Y/2 = Q+s),
   ungerade k rechts (Y/2 = Q+s+-1/2). Ausgabe je N_c: Loesung von Tr Y = 0 und {Tr Y, Tr Y^3, SU(2)^2U(1), Zahl der Dubletts} bei s=-1/2.
   SU(N_c)^2U(1) nur in k270 (Python/sympy). Ausgefuehrt ueber den Wolfram-MCP-Kernel. *)
ev[k_] := (1 + (-1)^k)/2; od[k_] := (1 - (-1)^k)/2;
f[m_, s_] := Module[{q = If[m == 0, 0 &, (#/m) &]},
 {Sum[Binomial[m, k] 2 (q[k] + s), {k, 0, m}],
  Sum[Binomial[m, k] (ev[k] 2 (q[k] + s)^3 + od[k] ((q[k] + s + 1/2)^3 + (q[k] + s - 1/2)^3)), {k, 0, m}],
  Sum[Binomial[m, k] ev[k] (q[k] + s), {k, 0, m}],
  Sum[Binomial[m, k] ev[k], {k, 0, m}]}];
{Table[{m, Solve[f[m, s][[1]] == 0, s], f[m, -1/2]}, {m, 1, 7}], Solve[1/2 + 1/(2 n) == (n - 1)/n, n],
 Table[{g, DSolveValue[{p''[t] == g w^2 p[t], p[0] == 1, p'[0] == 0}, p[t], t]}, {g, {-1, 0, 1}}]}
