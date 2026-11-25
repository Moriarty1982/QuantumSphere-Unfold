(* k281b (Erkundung, nicht blind): ein Element W = Z_v(a) + Z_S(b) in H3(C); Hoehe des Z3-Vakuums aus k278 im vollen Raum. *)
re = Element[{a, b, s, v, r}, Reals];
Print["det (s,v) -> (Re w, Im w), w = (1 + I b) s + (-a + I) v: ", Det[{{1, -a}, {b, 1}}]];
H[d_, z_] := {{d[[1]], z[[3]], Conjugate[z[[2]]]}, {Conjugate[z[[3]]], d[[2]], z[[1]]}, {z[[2]], Conjugate[z[[1]]], d[[3]]}};
Z = ComplexExpand[H[{0, 0, 0}, (-a + I) {r, r, r}]];
q = Simplify[ComplexExpand[Tr[Z . Z]], re]; n = Simplify[ComplexExpand[Det[Z]], re];
ratio = FullSimplify[n/q^(3/2), r > 0 && Element[a, Reals]];
Print["Z3-Vakuum v = r(1,1,1): N/(Tr Z^2)^(3/2) = ", ratio];
Print["  mal Sqrt[54] = ", FullSimplify[Sqrt[54] ratio, Element[a, Reals]], "; = 1 bei a = ", Solve[(3 a - a^3)^2 == (1 + a^2)^3, a, Reals]];
Print["Bahn (3 psi psi^+ - 1)/Sqrt6: Eigenwerte*Sqrt6 = ", Eigenvalues[3 Outer[Times, {1, 0, 0}, {1, 0, 0}] - IdentityMatrix[3]], ", det = ",
  Det[DiagonalMatrix[{2, -1, -1}]/Sqrt[6]], " = 1/Sqrt[54]: ", Det[DiagonalMatrix[{2, -1, -1}]/Sqrt[6]] == 1/Sqrt[54]];
