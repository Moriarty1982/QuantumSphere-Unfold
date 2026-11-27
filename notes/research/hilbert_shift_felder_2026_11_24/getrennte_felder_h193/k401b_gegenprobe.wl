(* k401b Gegenprobe H193: exakte stufeneigene Groessen und die Verhaeltnisse der besten stufenfesten Regel. *)
gammaL = 1.8646997646;
casimir[k_] := Sqrt[k (k + 2)/3];
weight[k_] := 2^(1 - gammaL casimir[k]);
dim[k_] := 2^k;

Print["Casimir a_k (k=1..4), exakt: ", Table[casimir[k], {k, 1, 4}]];
Print["Casimir a_k numerisch:        ", N[Table[casimir[k], {k, 1, 4}], 7]];
Print["Gewicht w_k:                  ", N[Table[weight[k], {k, 1, 4}], 7]];
Print["Dimension d_k:                ", Table[dim[k], {k, 1, 4}]];

(* Beobachtete Generationsverhaeltnisse *)
upPDG = {2.16*^-3, 1.2730, 172.4}; downPDG = {4.70*^-3, 93.5*^-3, 4.183};
rat[m_] := {m[[2]]/m[[1]], m[[3]]/m[[2]]};
Print["Up PDG Verhaeltnisse:   ", rat[upPDG]];
Print["Down PDG Verhaeltnisse: ", rat[downPDG]];

(* Beste stufenfeste Regel 2^d (auf) und 1/2^d (ab) *)
S2d = Table[2^dim[k], {k, 1, 3}];
Print["Regel 2^d auf Stufen {1,2,3}: ", S2d, " -> Verhaeltnisse ", {S2d[[2]]/S2d[[1]], S2d[[3]]/S2d[[2]]}];
S2dAb = Table[2^dim[k], {k, 4, 2, -1}];
Print["Regel 2^d ab Stufen {4,3,2}: ", S2dAb, " -> Verhaeltnisse ", {S2dAb[[2]]/S2dAb[[1]], S2dAb[[3]]/S2dAb[[2]]}];

(* Die stufenfesten Verhaeltnisse der einfachen Groessen *)
Print["Dimension-Verhaeltnisse (auf): ", {dim[2]/dim[1], dim[3]/dim[2]}];
Print["Casimir-Verhaeltnisse (auf):   ", N[{casimir[2]/casimir[1], casimir[3]/casimir[2]}, 6]];
Print["Gewicht-Verhaeltnisse (auf):   ", N[{weight[2]/weight[1], weight[3]/weight[2]}, 6]];
