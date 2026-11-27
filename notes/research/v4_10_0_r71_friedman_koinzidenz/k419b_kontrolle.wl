(* k419b (Runde v4.10.0-r71): unabhaengige Kontrolle des Koinzidenzindex (Wolfram Language).
   Bestaetigt die Python-Werte aus k419 auf demselben Strom (seed 71): globaler IC und
   mittlerer Spalten-IC bei L=7 (die versteckte Periode). Der Strom ist hier eingebettet,
   weil der Evaluator keinen Dateizugriff hat; er ist mit k419s make_stream(seed=71) identisch. *)

s = {2,0,2,1,1,2,1,2,0,2,1,1,2,0,3,0,2,0,1,2,0,2,0,2,1,1,2,0,2,0,2,1,1,2,1,2,0,2,1,1,2,0,2,0,2,0,1,2,0,2,0,2,1,0,2,0,2,0,2,1,1,2,2,2,0,2,1,0,3,0,2,0,2,1,1,2,0,2,1,2,1,1,2,0,2,0,2,1,1,3,0,2,0,0,1,1,2,3,2,0,2,1,3,2,0,2,0,2,1,1,2,0,2,0,0,1,1,1,0,2,0,2,3,1,2,0,2,0,2,1,1,0,0,2,0,3,1,1,3,0,2,0,2,1,1,2,1,2,0,2,1,1,2,0,2,0,2,1,1,2,0,2,2,2,1,3,2,0,2,0,2,1,1,2,0,2,0,2,1,1,2,0,2,0,2,1,1,2,0,2,0,2,1,1,2,0,2,0,2,1,1,2,0,2,2,2,1,1,2,0,2,0,2,1,1,2,0,2,0,2,1,2,2,0,2,0,2,1,1,2,0,2,1,2,1,1,3,0,2,0,1,1,1,2,2,2,0,2,1,1,2,0,1,2,2,1,1,2,0,2,0,2,0,2,1,0,2,0,2,1,1,2,2,2,0,2,1,3,2,0,2,1,0,1,1,2,0,1,1,2,1,1,2,3,2,0,2,1,1,2,2,2,0,2,1,1,2,2,2,0,2,1,0,1,0,2,0,2,1,1,3,1,2,0,3,1,1,2,0,2,0,2,1,1,2,0,2,0,2,1,1,2,0,3,0,2,1,1,2,3,2,0,2,1,1,2,0,2,0,1,2,1,2,0,2,0,2,1,2,2,3,2,0,2,2,1,2,0,2,0,2,1,1,3,0,2,0,2,1,1,2,3,2,0,2,1,3,1,0,2,0,2,1,1,2,0,2,0,3,1,1,2,0,0,0,2,1,2,2,0};

Print["len = ", Length[s], "  counts = ", {#, Count[s, #]} & /@ {0, 1, 2, 3}];
icOf[sym_] := Module[{nn = Length[sym]},
  If[nn < 2, 0., Total[(# (# - 1)) & /@ (Length /@ GatherBy[sym, Identity])]/(nn (nn - 1))]];
Print["global IC = ", N[icOf[s], 6], "  (Python 0.31357)"];
colICs = Table[icOf[s[[i ;; ;; 7]]], {i, 1, 7}];
Print["mittlerer Spalten-IC(7) = ", N[Mean[colICs], 6], "  (Python 0.73374)"];
Print["Spalten-IC bei L=6,7,8 = ", N[Mean[Table[icOf[s[[i ;; ;; #]]], {i, 1, #}]], 5] & /@ {6, 7, 8}];
Print["Zufalls-IC 1/c = ", N[1/Length[Union[s]], 6]];
