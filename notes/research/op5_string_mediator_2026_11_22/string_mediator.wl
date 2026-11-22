(* Weg C: gespannter String als Vermittler. Methoden-Notiz Commit 7ecb9fce. Erkundung, nicht blind. *)
(* Grundmode X^i = q^i s(sigma)/Sqrt[T0], s = Sqrt[2/L] Sin[Pi sigma/L], w1 = Pi/L. Kopplung an eta (Annahme S2: T = T0 (1 + tau eta/v)):
   L_int/eta = -(tau/v) Sqrt[T0] c1 I k.q + (tau/(2 v)) (k_i k_j q^i q^j + qdot^2 - w1^2 q^2),  c1 = Int s = 2 Sqrt[2 L]/Pi.
   H_int = -L_int (erste Ordnung, qdot -> p). Residuum je Energie E: R(E) = Sum_n 2 E |<n|H_int/eta|0>|^2. *)
Print["Normierung: Int s^2 = ", Integrate[(Sqrt[2/L] Sin[Pi s/L])^2, {s, 0, L}, Assumptions -> L > 0],
  ", Int s'^2 = ", Integrate[(D[Sqrt[2/L] Sin[Pi s/L], s])^2, {s, 0, L}, Assumptions -> L > 0],
  ", Int s = ", Integrate[Sqrt[2/L] Sin[Pi s/L], {s, 0, L}, Assumptions -> L > 0],
  ", Int s_2 (Mode 2) = ", Integrate[Sqrt[2/L] Sin[2 Pi s/L], {s, 0, L}, Assumptions -> L > 0]];
nmax = 3; dim = nmax + 1;
a1 = SparseArray[Table[{n, n + 1} -> Sqrt[n], {n, 1, nmax}], {dim, dim}] // Normal;
id = IdentityMatrix[dim];
ax = KroneckerProduct[a1, id]; ay = KroneckerProduct[id, a1];
q[a_] := (a + ConjugateTranspose[a])/Sqrt[2 w1];
pp[a_] := I Sqrt[w1/2] (ConjugateTranspose[a] - a);
qx = q[ax]; qy = q[ay]; px = pp[ax]; py = pp[ay];
idx[nx_, ny_] := nx dim + ny + 1;
vac = UnitVector[dim^2, idx[0, 0]];
Lint = -(tau/v) Sqrt[T0] c1 I (k1 qx + k2 qy) + (tau/(2 v)) (k1^2 qx.qx + 2 k1 k2 qx.qy + k2^2 qy.qy + px.px + py.py - w1^2 (qx.qx + qy.qy));
H = -Lint;
amp[nx_, ny_] := Simplify[Conjugate[UnitVector[dim^2, idx[nx, ny]]].H.vac, {w1 > 0, tau > 0, v > 0, T0 > 0, c1 > 0, Element[{k1, k2}, Reals]}];
one = {amp[1, 0], amp[0, 1]};
two = {amp[2, 0], amp[1, 1], amp[0, 2]};
R1 = Simplify[2 w1 Total[Abs[one]^2] /. Abs[z_]^2 :> z Conjugate[z], {w1 > 0, Element[{k1, k2, tau, v, T0, c1}, Reals]}];
R2 = Simplify[2 (2 w1) Total[ComplexExpand[Abs[two]^2]], {w1 > 0}];
R1a = Simplify[R1 /. k2 -> Sqrt[a - k1^2]];
R2a = Simplify[Expand[R2] /. k2 -> Sqrt[a - k1^2], a >= 0];
Print["(1) Ein-Quanten-Amplituden: ", one, ";  Residuum bei w1: ", R1a];
Print["    Zwei-Quanten-Amplituden: ", Simplify[two]];
Print["(2) Residuum bei 2 w1: ", Factor[R2a]];
R2x = Simplify[R2a /. w1 -> Sqrt[x]/2, x > 0];
Print["    am Pol x = 4 w1^2: ", Expand[R2x], " = ", Factor[R2x]];
Nm = 2/3 (x^2 - a x + a^2);
lam = Simplify[Coefficient[Expand[R2x], a, 2]/(2/3)];
Print["    skaliert auf den a^2-Koeffizienten von N_m: R2/lambda = ", Expand[R2x/lam], ";  Differenz zu N_m: ", Simplify[R2x/lam - Nm]];
Print["(4) in der Familie von r36.3: Koeffizienten (x^2, a x, a^2) = ", {Coefficient[Expand[R2x/lam], x, 2], Coefficient[Coefficient[Expand[R2x/lam], x, 1], a, 1], Coefficient[Expand[R2x/lam], a, 2]}];
