(* k252 / H125 Stufe A, exakte Kontrolle (Wolfram): Fuer ein Spin-1/2-Dublett mit [Jx,Jy] = i s Jz ist die
   Bargmann-Invariante der Oktant-Projektoren B = Tr(Px Py Pz) = 1/4 + i s/4; s -> -s konjugiert B. *)
sx = PauliMatrix[1]/2; sy = PauliMatrix[2]/2; sz = PauliMatrix[3]/2;
proj[j_] := (IdentityMatrix[2] + 2 j)/2;
Do[
  js = {sx, sy, s sz};
  Print["s = ", s, ": [Jx,Jy] - i s Jz = ", Simplify[js[[1]].js[[2]] - js[[2]].js[[1]] - I s js[[3]]],
   ";  B = Tr(Px Py Pz) = ", Simplify[Tr[proj[js[[1]]].proj[js[[2]]].proj[js[[3]]]]]], {s, {1, -1}}];
Print["Konjugation: B(s=-1) == Conjugate[B(s=+1)]: ",
  Simplify[Tr[proj[sx].proj[sy].proj[-sz]] == Conjugate[Tr[proj[sx].proj[sy].proj[sz]]]]];
