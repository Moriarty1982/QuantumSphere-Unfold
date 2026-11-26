(* k374b (Erkundung k374, 26.11.2026): unabhaengige Nachrechnung der kleinsten CKM-Brechung (Frobenius-Norm des nicht zirkulanten Anteils). Ausgabe in k374b_out.txt. *)
T = {{0, 0, 1}, {-1, 0, 0}, {0, -1, 0}}; T2 = T . T; w = Exp[2 Pi I/3];
ev[t_] := Normalize[First[NullSpace[T - t IdentityMatrix[3]]]];
F = N[Transpose[{ev[1], ev[w], ev[Conjugate[w]]}], 30];
std[s12_, s23_, s13_, d_] := Module[{c12 = Sqrt[1 - s12^2], c23 = Sqrt[1 - s23^2], c13 = Sqrt[1 - s13^2], e = Exp[I d]}, {{c12 c13, s12 c13, s13/e}, {-s12 c23 - c12 s23 s13 e, c12 c23 - s12 s23 s13 e, s23 c13}, {s12 s23 - c12 c23 s13 e, -c12 s23 - s12 c23 s13 e, c23 c13}}];
lam[m_] := Module[{s = N[Sqrt[m], 30]}, Sort[s/(Total[s]/3)]];
ld = lam[{154/10000, 306/1000, 1630/100}]; lu = lam[{704/100000, 356/100, 967}];
V = N[std[225/1000, 418/10000, 373/100000, 114/100], 30];
nc[M_] := M - (M + T . M . Transpose[T] + T2 . M . Transpose[T2])/3;
nd[a_?NumericQ, b_?NumericQ] := Module[{U = F . DiagonalMatrix[{1, Exp[I a], Exp[I b]}] . V}, Norm[nc[U . DiagonalMatrix[ld] . ConjugateTranspose[U]], "Frobenius"]];
nu[a_?NumericQ, b_?NumericQ] := Module[{U = F . DiagonalMatrix[{1, Exp[I a], Exp[I b]}] . ConjugateTranspose[V]}, Norm[nc[U . DiagonalMatrix[lu] . ConjugateTranspose[U]], "Frobenius"]];
{NMinimize[nd[a, b], {{a, 0, 2 Pi}, {b, 0, 2 Pi}}, Method -> "DifferentialEvolution"][[1]], NMinimize[nu[a, b], {{a, 0, 2 Pi}, {b, 0, 2 Pi}}, Method -> "DifferentialEvolution"][[1]], N[ld, 6], N[lu, 6]}
