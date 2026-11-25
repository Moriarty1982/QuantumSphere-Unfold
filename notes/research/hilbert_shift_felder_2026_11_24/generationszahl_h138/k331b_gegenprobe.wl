(* k331b (Test H148, Wolfram exakt): theta* der Gram-Auslesung, Eigenwerte dort; K der Amplituden-Auslesung (r13/k255) signiert;
   Betragsquadrate fuer den komplexen Ladungszustand. Ausgabe k331b_out.txt. *)
a[t_] := Cos[t]^2 - Sin[t]^2/2;
ts = ArcSin[Sqrt[2/3 (1 - 1/Sqrt[2])]];
Print["a(t*)^2: ", FullSimplify[a[ts]^2], "; t* in Grad: ", N[ts/Degree, 10]];
G = {{1, a[ts], a[ts]}, {a[ts], 1, a[ts]}, {a[ts], a[ts], 1}};
Print["Eigenwerte bei t*: ", FullSimplify[Eigenvalues[G]], "; K: ", FullSimplify[Total[Eigenvalues[G]^2]/Total[Eigenvalues[G]]^2]];
g = {{1/Sqrt[3], Sqrt[2/3], 0}, {1/Sqrt[3], -Sqrt[2/3]/2, Sqrt[2]/2}, {1/Sqrt[3], -Sqrt[2/3]/2, -Sqrt[2]/2}};
c = g . {Cos[th], Sin[th] Cos[d], Sin[th] Sin[d]};
Print["Gram der g_k: ", Simplify[g . Transpose[g]]];
Print["K signiert: ", FullSimplify[Total[c^2]/Total[c]^2]];
Print["Komplexer Zustand: |c|^2 bei th = Pi/4: ", FullSimplify[ComplexExpand[Abs[g . {1/Sqrt[2], I Cos[d]/Sqrt[2], I Sin[d]/Sqrt[2]}]^2]]];
