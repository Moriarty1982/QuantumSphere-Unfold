(* k262b (Erkundung, nicht blind, 25.11.2026): exakte Kontrolle der TM1-Klasse aus k262, Lesart B.
   T erzeugt die Z3 der geladenen Leptonen, A ist die ungerade Z2 der Neutrinos (beide aus k262_out.txt). *)
T = {{0, 0, 1}, {-1, 0, 0}, {0, -1, 0}};
A = {{0, 0, -1}, {0, 1, 0}, {-1, 0, 0}};
Print["T^3 = 1: ", MatrixPower[T, 3] == IdentityMatrix[3], "; A^2 = 1: ", A.A == IdentityMatrix[3], "; det A = ", Det[A]];
(* allgemeine reelle symmetrische Massenform mit A^T m A = m *)
m0 = {{a, b, c}, {b, d, e}, {c, e, f}};
sol = Solve[Thread[Flatten[Transpose[A].m0.A - m0] == 0], {b, c, d, e, f, a}][[1]];
m = m0 /. sol;
Print["m (reell, A-invariant): ", m, "; freie Parameter: ", Variables[m]];
(* Eigenbasis von T: Spalten von Ue *)
es = Eigensystem[T];
Ue = Transpose[Normalize /@ es[[2]]];
Print["Eigenwerte von T: ", es[[1]]];
Print["Ue unitaer: ", FullSimplify[ConjugateTranspose[Ue].Ue] == IdentityMatrix[3]];
(* feste Spalte: Eigenvektor von A zum einfachen Eigenwert *)
ea = Eigensystem[A];
Print["Eigenwerte von A: ", ea[[1]]];
w = Normalize[First[Select[Transpose[{ea[[1]], ea[[2]]}], Count[ea[[1]], #[[1]]] == 1 &]][[2]]];
Print["einfacher Eigenvektor w = ", w, "; m.w proportional w: ", Simplify[Cross[m.w, w]] == {0, 0, 0}];
col = FullSimplify[Abs[ConjugateTranspose[Ue].w]^2];
Print["|U_alpha1|^2 = ", col];
(* mu-tau-Spiegelung: m' = Ue^T m Ue erfuellt P^T m' P = Conjugate[m'] fuer eine Vertauschung P mit Phasen *)
mp = FullSimplify[Transpose[Ue].m.Ue];
X = FullSimplify[ConjugateTranspose[Ue].Conjugate[Ue]];
Print["X = Ue^dagger Ue^* = ", X, "  (Betraege: ", FullSimplify[Abs[X]], ")"];
Print["X^T m' X - Conjugate[m'] = ", FullSimplify[ComplexExpand[Transpose[X].mp.X - Conjugate[mp]], Assumptions -> Element[Variables[m], Reals]]];
(* Zahlenbeispiel: Winkel *)
vars = Variables[m]; numr = Thread[vars -> Take[{1, 17/10, 3/10, 1/5}, Length[vars]]];
mn = N[m /. numr, 30]; {vals, vecs} = Eigensystem[mn];
U = N[ConjugateTranspose[Ue], 30].Transpose[vecs]; P = Abs[U]^2;
Print["Zahlenbeispiel ", numr, ": |U|^2 = ", N[P, 8]];
