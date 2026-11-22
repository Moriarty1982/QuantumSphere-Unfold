ClearAll[x, y, z, orderedProduct, overlaps, normalized, a, b, c, cycles, increments];
x = {1, 1}/Sqrt[2];
y = {1, I}/Sqrt[2];
z = {1, 0};
orderedProduct[{u_, v_, w_}] := (Conjugate[u].v) (Conjugate[v].w) (Conjugate[w].u);
overlaps[points_] := FullSimplify[(Abs[Conjugate[#[[1]]].#[[2]]]^2 &) /@
  Partition[Append[points, First[points]], 2, 1]];
normalized[t_] := FullSimplify[t/Abs[t]];
Print["Wolfram: ", $Version];
Print["Pairwise overlap squares, forward and reverse: ",
  InputForm[overlaps /@ {{x, y, z}, {x, z, y}}]];
Print["Normalized ordered products, forward and reverse: ",
  InputForm[normalized /@ (orderedProduct /@ {{x, y, z}, {x, z, y}})]];
Print["Bargmann phases in units of Pi/4: ",
  FullSimplify[(4 Arg[orderedProduct[#]]/Pi &) /@ {{x, y, z}, {x, z, y}}]];
Print["Independent rephasings: ordered product residual: ",
  FullSimplify[orderedProduct[{Exp[I a] x, Exp[I b] y, Exp[I c] z}] -
    orderedProduct[{x, y, z}], Element[{a, b, c}, Reals]]];
cycles = Mod[#, 8] & /@ {Range[0, 7], -Range[0, 7]};
increments[q_] := Mod[Differences[Append[q, First[q]]], 8];
Print["Equal sorted accumulated phases: ", Sort /@ cycles];
Print["Distinct signed-step classes modulo 8: ", Union[increments[#]] & /@ cycles];
