(* k405b: Gegenprobe mit Wolfram Language (exakt). Ausgabe in k405b_out.txt *)
Print["k405b Teil D: Schleife L3 in c = 2b - 1"]; f3[b_] := 1 - 2 b (1 - b);
Print["2 f3((1+c)/2) - 1 - c^2 = ", Simplify[2 f3[(1 + c)/2] - 1 - c^2]];
Print["n-fache Schleife: c_n - c^(2^n) fuer n = 1..5: ", Table[Simplify[2 Nest[f3, (1 + c)/2, n] - 1 - c^(2^n)], {n, 1, 5}]];
Print["Zahl der Vorgaenger nach n Schritten (Grad von c_n): ", Table[Exponent[Expand[2 Nest[f3, (1 + c)/2, n] - 1], c], {n, 0, 5}]];
Print["k405b Teil B: Cl(1,1)"]; e = {{0, -1}, {1, 0}}; f = {{0, 1}, {1, 0}}; id = IdentityMatrix[2];
Print["e.e = ", e . e, "; f.f = ", f . f, "; e.f + f.e = ", e . f + f . e, "; Rang {1,e,f,ef} = ", MatrixRank[Flatten /@ {id, e, f, e . f}]];
Print["MatrixExp[t f] = ", Simplify[ExpToTrig[MatrixExp[t f]]]];
ep = (id + f)/2; em = (id - f)/2; Print["e+.e+ - e+ = ", ep . ep - ep, "; e+.e- = ", ep . em];
Print["(p e+ + q e-) als a + b f: a = (p+q)/2, b = (p-q)/2, Norm a^2 - b^2 = ", Simplify[((p + q)/2)^2 - ((p - q)/2)^2]];
Print["k405b Teil C: Zaehlregel"];
Print["glatt: Sum 2^(1 - 2 (k+1)/2) = ", Sum[2^(1 - 2 (k + 1)/2), {k, 1, Infinity}], "; p_k = ", Table[2^(1 - 2 (k + 1)/2), {k, 1, 5}]];
gL = g /. FindRoot[Sum[2^(1 - g Sqrt[k (k + 2)/3]), {k, 1, 600}] == 1, {g, 1.8}, WorkingPrecision -> 30];
bs = Sqrt[(gL - 1)/(gL + 1)]; Print["gamma_L = ", N[gL, 15], "; beta_sym = ", N[bs, 15]];
Print["log2 p_k (Casimir), k = 1..6: ", Table[N[1 - gL Sqrt[k (k + 2)/3], 8], {k, 1, 6}]];
Print["phi_M = ln(1/beta_sym) = ", N[Log[1/bs], 10], "; artanh beta_sym = ", N[ArcTanh[bs], 10]];
Print["k405b Teil E: q-Zahlen"]; qi[n_, q_] := (q^n - 1)/(q - 1);
Print["[n]_2, n = -2..4: ", Table[qi[n, 2], {n, -2, 4}], "; Grenzwert q -> 1: ", Table[Limit[qi[n, q], q -> 1], {n, -2, 4}]];
gl[n_, q_] := Product[q^n - q^i, {i, 0, n - 1}]; Print["Limit |GL_n(F_q)|/(q-1)^n, n = 1..5: ", Table[Limit[gl[n, q]/(q - 1)^n, q -> 1], {n, 1, 5}]];
