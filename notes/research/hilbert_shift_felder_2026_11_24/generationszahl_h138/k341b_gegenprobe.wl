(* k341b (H158): Gegenprobe. a, b, e symbolisch; c ueber reelle Monome in (phi, s1..s3, v1..v3) mit expliziten V4-Vorzeichen,
   Einschraenkung auf den Zirkulantensektor, Fourier-Zerlegung in delta, J-Schnitt U[a,m] ∩ U[m,a]. *)
S = {{0, 1, 0}, {0, 0, 1}, {1, 0, 0}};
W = a IdentityMatrix[3] + (s + I v) S + (s - I v) Transpose[S];
Print["P W P^T - W = ", Simplify[S . W . Transpose[S] - W]];
Print["Eigenwerte - Brannen: ", Chop[Sort[Eigenvalues[N[W /. {a -> 1, s -> r Cos[d], v -> r Sin[d]} /. {r -> 7/10, d -> 2/9}]]] -
   Sort[N[Table[1 + 2 (7/10) Cos[2/9 + 2 Pi k/3], {k, 0, 2}]]]]];
Print["det W - (a^3 - 3 a r^2 + 2 r^3 Cos[3 d]) = ", Simplify[Det[W /. {s -> r Cos[d], v -> r Sin[d]}] - (a^3 - 3 a r^2 + 2 r^3 Cos[3 d])]];
Print["K - 2/3 bei r^2 = a^2/2: ", Simplify[(Tr[W . W]/Tr[W]^2 /. {s -> r Cos[d], v -> r Sin[d]} /. r -> a/Sqrt[2]) - 2/3]];
Print["H158e Rest: ", Simplify[ComplexExpand[Re[((1 + I c) (s + I v))^2]] - ((1 - c^2) (s^2 - v^2) - 4 c s v)]];
(* c *)
flips = {{1, -1, -1}, {-1, 1, -1}, {-1, -1, 1}}; (* Vorzeichen der Nebendiagonalen (12),(23),(31) unter diag(1,-1,-1) usw.: je zwei wechseln *)
harm[i_, j_] := Module[{e = TrigReduce[Cos[d]^i Sin[d]^j] /. {Cos[k_. d] :> cc[k], Sin[k_. d] :> ss[k]}},
   Prepend[Flatten[Table[{Coefficient[e, cc[n]], Coefficient[e, ss[n]]}, {n, 1, 8}]], e /. {cc[_] -> 0, ss[_] -> 0}]];
U[m_] := U[m] = Module[{exps, ok, vecs},
   exps = Flatten[Permutations /@ IntegerPartitions[m, {6}, Range[0, m]], 1];
   ok = Select[exps, Function[ex, AllTrue[flips, Function[f, EvenQ[Total[Pick[ex[[1 ;; 3]] + ex[[4 ;; 6]], f, -1]]]]]]];
   vecs = Union[harm[Total[#[[1 ;; 3]]], Total[#[[4 ;; 6]]]] & /@ ok];
   If[vecs === {}, {}, Select[RowReduce[vecs], # . # != 0 &]]];
inter[A_, B_] := If[A === {} || B === {}, {}, Module[{ns = NullSpace[Transpose[Join[A, -B]]]}, If[ns === {}, {}, Select[RowReduce[(#[[1 ;; Length[A]]] . A) & /@ ns], # . # != 0 &]]]];
names = Prepend[Flatten[Table[{"cos" <> ToString[n], "sin" <> ToString[n]}, {n, 1, 8}]], "1"];
Do[Module[{dim = 0, hs = {}},
   Do[With[{m = D - aa}, If[aa <= m,
       With[{X = If[aa == m, U[m], inter[U[m], U[aa]]]},
        If[X =!= {}, dim += Length[X]; hs = Union[hs, Flatten[Position[Total[Abs[X]], _?(# != 0 &)]]]]]]], {aa, 0, D}];
   Print["Ordnung ", D, ": J-erlaubt Dimension ", dim, ", Harmonische: ", names[[hs]]]], {D, 0, 8}];
d0 = 0.2222217;
Print["noetiges beta/alpha, Zweig 2Pi/3 - delta (I6): ", With[{x = 2 Pi/3 - d0}, -2 (3/4) Sin[2 x]/(3 (27 (1/6)^(3/2) 2 (1/12)^(3/2)) Sin[3 x])], "; 3 Sqrt[3] = ", N[3 Sqrt[3]]];
