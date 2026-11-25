(* k329b (Test H146, Wolfram exakt): Gram-Auslesung auf den Kopien. Lepton-Ueberlappung (1 + v.v')/2, Farb-Ueberlappung v.v'.
   Ausgabe k329b_out.txt. *)
f = {{1, 0}, {-1/2, Sqrt[3]/2}, {-1/2, -Sqrt[3]/2}};
vv = Flatten[Table[Flatten[Outer[Times, f[[a]], f[[b]]]], {a, 3}, {b, 3}], 1];
gl[idx_] := Table[(1 + vv[[i]] . vv[[j]])/2, {i, idx}, {j, idx}];
gc[idx_] := Table[vv[[i]] . vv[[j]], {i, idx}, {j, idx}];
kk[l_] := Total[l^2]/Total[l]^2;
Print["Sedenion-Tripel [1,2,3]: Lepton ", Sort[Eigenvalues[gl[{1, 2, 3}]]], ", K ", kk[Eigenvalues[gl[{1, 2, 3}]]], "; Farbe ", Sort[Eigenvalues[gc[{1, 2, 3}]]], ", K ", kk[Eigenvalues[gc[{1, 2, 3}]]]];
Print["Max K drei Kopien: Lepton ", Max[Table[kk[Eigenvalues[gl[t]]], {t, Subsets[Range[9], {3}]}]], ", Farbe ", Max[Table[kk[Eigenvalues[gc[t]]], {t, Subsets[Range[9], {3}]}]]];
q = {1, 2, 6, 9};
el = Eigensystem[gl[q]]; ec = Eigensystem[gc[q]];
Print["H142-Auswahl [1,2,6,9]: Lepton ", el, "; Farbe ", ec];
Print["K der drei massiven: Lepton ", kk[DeleteCases[el[[1]], 0]], ", Farbe ", kk[DeleteCases[ec[[1]], 0]]];
