ClearAll[masks, result, rows, counts];
masks = Tuples[{0, 1}, 2];
result[p_] := Switch[p, {1, 0}, "+45", {0, 1}, "-45", {0, 0}, "blocked", {1, 1}, "ambiguous"];
rows = Flatten[Table[{a, b, a b, result[a b]}, {a, masks}, {b, masks}], 1];
Print["Wolfram: ", $Version];
Print["Rows {first, second, persistent, outcome}:"];
Scan[Print[InputForm[#]] &, rows];
Print["Counts: ", InputForm[Counts[Last /@ rows]]];
Print["Second-mask intervention from same initial mask: ",
  result /@ ({1, 1} # & /@ {{1, 0}, {0, 1}})];
Print["No re-entry: ", AllTrue[rows, And @@ Thread[#[[3]] <= #[[1]]] &]];
Print["Symmetric masks: ", result /@ {{0, 0}, {1, 1}}];
