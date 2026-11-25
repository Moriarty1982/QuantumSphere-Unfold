(* k261b (Test H131, Kontrolle iv): CP-Abbildungen X in der Basis der geladenen Leptonen (T diagonal) und die allgemeine Majorana-Matrix
   mit S^T m S = m und X^T m X = m*, exakt. Vertreter: T zyklisch, S = diag(1,-1,-1), X1, X2 mit X X* = 1 und X3, X4 mit X X* = S (aus k261). *)
w = Exp[2 Pi I/3];
T = {{0, 1, 0}, {0, 0, 1}, {1, 0, 0}}; S = DiagonalMatrix[{1, -1, -1}];
U = Transpose[{{1, 1, 1}, {1, w, w^2}, {1, w^2, w}}]/Sqrt[3];
Print["U unitaer: ", FullSimplify[ConjugateTranspose[U] . U] == IdentityMatrix[3], "; U^+ T U = ", FullSimplify[ConjugateTranspose[U] . T . U] // ComplexExpand // FullSimplify];
xs = <|"X1 (X X* = 1)" -> {{1, 0, 0}, {0, 0, -1}, {0, -1, 0}}, "X2 (X X* = 1)" -> {{-1, 0, 0}, {0, 0, 1}, {0, 1, 0}}, "X3 (X X* = S)" -> {{-1, 0, 0}, {0, 0, -1}, {0, 1, 0}}, "X4 (X X* = S)" -> {{-1, 0, 0}, {0, 0, 1}, {0, -1, 0}}|>;
Do[With[{x = xs[k]}, Print[k, ": X S == S X ", x . S == S . x, "; X.X = ", x . x, "; X' = U^+ X U* = ", InputForm[FullSimplify[ComplexExpand[ConjugateTranspose[U] . x . Conjugate[U]]]]]], {k, Keys[xs]}];
m = {{a + I a2, b + I b2, c + I c2}, {b + I b2, e + I e2, f + I f2}, {c + I c2, f + I f2, g + I g2}};
vars = {a, a2, b, b2, c, c2, e, e2, f, f2, g, g2};
sol[x_] := Solve[Thread[Flatten[ComplexExpand[{Re[#], Im[#]} & /@ Flatten[Join[Transpose[S] . m . S - m, Transpose[x] . m . x - ComplexExpand[Conjugate[m]]]]]] == 0], vars];
Do[With[{mm = m /. First[sol[xs[k]]]}, Print[k, ": m_nu = ", InputForm[mm], "; m' = U^T m U = ", InputForm[FullSimplify[ComplexExpand[Transpose[U] . mm . U]]],
   "; Eigenwerte von m^+ m: ", InputForm[FullSimplify[Eigenvalues[ComplexExpand[ConjugateTranspose[mm] . mm]], Element[vars, Reals]]]]], {k, {"X1 (X X* = 1)", "X3 (X X* = S)"}}];
