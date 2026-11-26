(* k339b (H156): unabhaengige Gegenprobe in Wolfram Language (Vorab-Notiz fdac350). *)
lu = {{0, -1}, {1, 0}}; cj = {{1, 0}, {0, -1}}; jj = {{0, 1}, {1, 0}};
Print["J = L_U . Konjugation: ", jj == lu.cj];
grp[gens_] := FixedPoint[Union[#, Flatten[Table[g.h, {g, #}, {h, gens}], 1]] &, {IdentityMatrix[2]}];
inv[g_, deg_] := Module[{mons = Table[f^a w^(deg - a), {a, 0, deg}], avg}, avg = Table[Expand[Total[(m /. Thread[{f, w} -> #.{f, w}]) & /@ g]/Length[g]], {m, mons}];
   DeleteCases[RowReduce[Table[Coefficient[Coefficient[a, f, e], w, deg - e], {a, avg}, {e, 0, deg}]], {0 ..}].Table[f^e w^(deg - e), {e, 0, deg}]];
Do[With[{g = grp[gs[[2]]]}, Print[gs[[1]], " (Ordnung ", Length[g], "): quadratisch ", inv[g, 2], "; quartisch ", inv[g, 4],
    "; schiebt theta bei pi/4: ", Select[inv[g, 4], (D[# /. {f -> Cos[t], w -> Sin[t]}, t] /. t -> Pi/4) != 0 &]]], {gs, {{"Z4", {lu}}, {"Z2 J", {jj}}, {"D4", {lu, cj}}}}];
bet[nB_] := Module[{ys = Array[uu, nB], af, bf, vf, hh, rr}, af = f^2; bf = Total[ys^2]; vf = mA af + mB bf + lA af^2 + ka af bf + lB bf^2;
   hh = D[vf, {Join[{f}, ys], 2}]; rr = Expand[Tr[hh.hh]/2];
   {Coefficient[rr, f, 2] /. Thread[Join[{f}, ys] -> 0], Coefficient[rr, uu[1], 2] /. Thread[Join[{f}, ys] -> 0], Coefficient[rr, f, 4] /. Thread[ys -> 0], Coefficient[Coefficient[rr, f, 2], uu[1], 2] /. Thread[Drop[ys, 1] -> 0], Coefficient[rr, uu[1], 4] /. Thread[Join[{f}, Drop[ys, 1]] -> 0]}];
Do[Module[{b = bet[nB], fl, sub, dsm, drl, dm0, dl0, ds, dr},
   sub = {mA -> m + e dm/2, mB -> m - e dm/2, lA -> l + e dl/2, ka -> k, lB -> l - e dl/2};
   fl = -b /. sub; ds = (fl[[1]] - fl[[2]]) m - e dm (fl[[1]] + fl[[2]])/2; ds = ds/m^2; dr = ((fl[[3]] - fl[[5]]) l - e dl (fl[[3]] + fl[[5]])/2)/l^2;
   Print["n_B=", nB, ": Quelle ", Simplify[{ds, dr} /. e -> 0], "; Matrix (s, r): ", Simplify[{{D[ds, e, dm] m, D[ds, e, dl] l}, {D[dr, e, dm] m, D[dr, e, dl] l}} /. e -> 0]]], {nB, {1, 2}}];
jc[z_] := I Conjugate[z];
Print["J(1)J(1) = ", jc[1] jc[1], ", J(1) = ", jc[1], "; |J(z)|^2-|z|^2 = ", ComplexExpand[Abs[jc[a + I b]]^2 - Abs[a + I b]^2], "; J(zw)-J(z)conj(w) = ", ComplexExpand[jc[(a + I b) (c + I d)] - jc[a + I b] Conjugate[c + I d]]];
