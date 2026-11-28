(* H220 (k433b): unabhaengige Gegenprobe in Wolfram Language: Aufzaehlung bis Groesse 4 (= S_max) mit denselben strukturellen
   Bausteinen, Treffer in den 2-sigma-Fenstern, Nachrechnung der gemeldeten Formeln. *)
Fz[g_?NumericQ] := Sum[2^(1 - g Sqrt[k (k + 2)/3]), {k, 1, 400}] - 1;
gL = g /. FindRoot[Fz[g], {g, 186/100}, WorkingPrecision -> 40];
leaves = N[{1, 2, 4, 8, 16, 3, 7, 1/2, 2/3, Sqrt[3/4], Sqrt[2], Sqrt[15/4], Sqrt[6], gL}, 25];
un = {Sqrt[#] &, #^2 &, 1/# &}; bin = {Plus, Subtract, Times, Divide};
key[v_] := Round[Log[Abs[v]] 10^11]; ok[v_] := NumericQ[v] && Im[v] == 0 && 10^-7 < Abs[v] < 10^7;
seen = Association[]; lev = <||>;
addLevel[s_, c_] := Module[{out = {}}, Do[If[ok[x], With[{k = key[x]}, If[! KeyExistsQ[seen, k], seen[k] = s; AppendTo[out, x]]]], {x, c}]; lev[s] = out];
addLevel[1, leaves];
Do[addLevel[s, Join[Flatten[Table[f /@ lev[s - 1], {f, un}]], Flatten[Table[Outer[op, lev[a], lev[s - 1 - a]], {a, 1, s - 2}, {op, bin}]]]], {s, 2, 4}];
Print["gamma_L = ", N[gL, 15], ";  neue Werte je Groesse (Wolfram): ", Length /@ Values[lev]];
inwin[x0_, sig_] := Select[Flatten[Values[lev]], Abs[# - x0] <= 2 sig &];
Print["Treffer bis Groesse 4: mmu/mtau ", inwin[0.059464, 4*^-6], ", sin2tW ", inwin[0.23129, 4*^-5], ", mW/mZ ", inwin[80.3692/91.1880, 0.0133/91.1880], ", 1/alpha ", inwin[137.035999177, 2.1*^-8], ", me/mmu ", inwin[0.51099895/105.6583755, 1.*^-10]];
Print["1/(16+Sqrt[2/3]) = ", N[1/(16 + Sqrt[2/3]), 15], ";  1/7 + Sqrt[2]/16 = ", N[1/7 + Sqrt[2]/16, 15], ";  2/(Sqrt[15/4]+1/3) = ", N[2/(Sqrt[15/4] + 1/3), 15],
  ";  gL/Sqrt[1+gL^2] = ", N[gL/Sqrt[1 + gL^2], 12], ";  16^2/gL = ", N[256/gL, 12]];
