(* k378b: Kontrolle der Formeln aus k378 (trigonometrischer Teil und Zahlen) *)
t[p_, g_, f_] := Cos[p]^3 - Cos[p] Sin[p]^2 g - Sin[p]^3 f;
Print[{FullSimplify[t[p, 3, 0] - Cos[3 p]], N[ArcTan[1/Sqrt[2]]], N[p /. FindRoot[t[p, 2, 0.19245], {p, 0.6}]], N[p /. FindRoot[t[p, 1, 0.5443], {p, 0.7}]], N[ArcCot[1]],
 N[ArcCos[-1/(Sqrt[2] #)] - 2 Pi/3 & /@ {1, 1.11506, 1.28952}], N[{-2 Sin[48.114 Degree]^2, -2 Sin[52.207 Degree]^2}]}]
