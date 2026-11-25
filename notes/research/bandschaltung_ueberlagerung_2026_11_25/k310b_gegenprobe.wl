(* k310b: independent exact check for H137 (Wolfram Language). Step map from the rule tables, collision counts, H137d reduced states. *)
stepP[{tape_, h_, s_}] := Module[{n = Length[tape], r = tape[[h + 1]]},
  Which[
    s === "halt", {tape, h, s, "halted"},
    r == 1, If[h + 1 < n, {tape, h + 1, "scan", "running"}, {tape, h, s, "boundary"}],
    r == 0, {ReplacePart[tape, h + 1 -> 1], h, "halt", "halted"}]];
stepR[{tape_, h_, s_}] := Which[
    s === "halt", {tape, h, s, "halted"},
    s === "a", {ReplacePart[tape, h + 1 -> 1 - tape[[h + 1]]], h, "b", "running"},
    s === "b", {tape, h, "a", "running"}];
configs[n_, states_] := Flatten[Table[{t, h, s}, {t, Tuples[{0, 1}, n]}, {h, 0, n - 1}, {s, states}], 2];
coll[step_, n_, states_] := Module[{c = configs[n, states]}, {Length[c], Length[DeleteDuplicates[step /@ c]], Length[c] - Length[DeleteDuplicates[step /@ c]]}];
Do[Print["P n=", n, " {domain, image, collisions} = ", coll[stepP, n, {"scan", "halt"}], "  expected collisions n 2^(n-1) = ", n 2^(n - 1)], {n, 2, 3}];
Do[Print["R n=", n, " {domain, image, collisions} = ", coll[stepR, n, {"a", "b", "halt"}]], {n, 2, 3}];
(* H137d: after one R step from tape 0..0, state a, head (|0>+|1>)/Sqrt[2]; basis order: cells (n qubits) x head (n values) *)
Do[
  Module[{dimC = 2^n, psi, rho, rhoCells, s, rho01, pt, neg, img},
   img = stepR /@ {{ConstantArray[0, n], 0, "a"}, {ConstantArray[0, n], 1, "a"}};
   psi = Normal[SparseArray[(FromDigits[Reverse[#[[1]]], 2] n + #[[2]] + 1 -> 1/Sqrt[2]) & /@ img, dimC n]];
   rho = KroneckerProduct[psi, Conjugate[psi]];
   rhoCells = Total[Table[rho[[Range[dimC] n - n + k, Range[dimC] n - n + k]], {k, 1, n}]];
   s = Total[If[# > 0, -# Log2[#], 0] & /@ Eigenvalues[rhoCells]];
   (* cells index = FromDigits[Reverse[tape]] => qubit 0 is lowest bit; trace cells beyond 0,1 *)
   rho01 = Table[Sum[rhoCells[[i + 4 m + 1, j + 4 m + 1]], {m, 0, dimC/4 - 1}], {i, 0, 3}, {j, 0, 3}];
   pt = Table[rho01[[2 Quotient[j, 2] + Mod[i, 2] + 1, 2 Quotient[i, 2] + Mod[j, 2] + 1]], {i, 0, 3}, {j, 0, 3}];
   neg = Total[Select[Eigenvalues[pt], # < 0 &], {1}] // Abs;
   Print["R n=", n, " H137d: S(cells|head,state) = ", Simplify[s], " bits; rho(cell0,cell1) = ", rho01, "; negativity = ", neg]],
  {n, 2, 3}];
