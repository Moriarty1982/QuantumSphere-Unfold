(* Gegenprobe zu qmon.sv und zur kanonischen sqrt(2)-Form in qnorm2.sv (symbolisch, exakt). *)
w = Exp[I Pi/4];
x = a0 + a1 w + a2 w^2 + a3 w^3;
(* 1) |x|^2 = P + sqrt(2) Q *)
norm = FullSimplify[ComplexExpand[x Conjugate[x]], Element[{a0, a1, a2, a3}, Reals]];
pq = a0^2 + a1^2 + a2^2 + a3^2 + Sqrt[2] (a0 a1 + a1 a2 + a2 a3 - a3 a0);
Print["Norm minus P+sqrt2 Q: ", FullSimplify[norm - pq]];
(* 2) x*sqrt(2) in der Basis 1, w, w^2, w^3 *)
y = (a1 - a3) + (a0 + a2) w + (a1 + a3) w^2 + (a2 - a0) w^3;
Print["x sqrt2 minus y: ", FullSimplify[ComplexExpand[x Sqrt[2] - y]]];
(* 3) Teilbarkeitsregel: x/sqrt(2) in Z[w] genau dann, wenn a0=a2, a1=a3 mod 2 (Durchlauf ueber alle Restklassen) *)
ok = And @@ Flatten@Table[
    With[{yy = {b1 - b3, b0 + b2, b1 + b3, b2 - b0}},
     (AllTrue[yy, EvenQ]) == (EvenQ[b0 - b2] && EvenQ[b1 - b3])],
    {b0, 0, 3}, {b1, 0, 3}, {b2, 0, 3}, {b3, 0, 3}];
Print["Teilbarkeitsregel fuer alle Restklassen mod 4: ", ok];
