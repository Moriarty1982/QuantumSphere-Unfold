(* H219 (k432b): unabhaengige Gegenprobe in Wolfram Language.
   Aufzaehlung bis Groesse 5 mit denselben Bausteinen, eigene Deduplizierung (relativ 1e-11);
   kuerzeste Treffer fuer sechs Ziele bis Groesse 5; Werte der gemeldeten Treffer. *)
leaves = N[{1, 2, 3, Pi, Log[2]}, 20];
un = {Sqrt[#] &, #^2 &, 1/# &, 2^(-#) &}; bin = {Plus, Subtract, Times, Divide};
key[v_] := Round[Log[Abs[v]] 10^11]; ok[v_] := NumericQ[v] && Im[v] == 0 && 10^-7 < Abs[v] < 10^7;
seen = Association[]; lev = <||>;
addLevel[s_, cands_] := Module[{out = {}}, Do[If[ok[c], With[{k = key[c]}, If[! KeyExistsQ[seen, k], seen[k] = s; AppendTo[out, c]]]], {c, cands}]; lev[s] = out];
addLevel[1, leaves];
Do[addLevel[s, Join[Flatten[Table[f /@ lev[s - 1], {f, un}]], Flatten[Table[Outer[op, lev[a], lev[s - 1 - a]], {a, 1, s - 2}, {op, bin}]]]], {s, 2, 5}];
Print["verschiedene Werte je Groesse (Wolfram): ", Length /@ Values[lev]];
smin[lo_, hi_] := Module[{r = SelectFirst[Range[5], AnyTrue[lev[#], lo <= # <= hi &] &]}, If[MissingQ[r], "-", r]];
tg = {{"beta_sym", 0.54907, 0.54978}, {"sin2tW", 0.23129 - 8*^-5, 0.23129 + 8*^-5}, {"sin2t12", 0.3088 - 0.0132, 0.3088 + 0.0134},
   {"sin2t23", 0.470 - 0.028, 0.470 + 0.034}, {"|Vub|", 0.00382 - 0.0004, 0.00382 + 0.0004}, {"mmu/mtau", 0.059464 - 8*^-6, 0.059464 + 8*^-6}};
Do[Print[t[[1]], ": s_min (bis 5) = ", smin[t[[2]], t[[3]]]], {t, tg}];
Print["1/(3 ln2)^2 = ", N[1/(3 Log[2])^2, 12], "  1/Pi + (ln2)^4 = ", N[1/Pi + Log[2]^4, 12], "  3 (2^-Sqrt2)^4 = ", N[3 2^(-4 Sqrt[2]), 12],
  "  Sqrt[Pi + 1/3] = ", N[Sqrt[Pi + 1/3], 12]];
