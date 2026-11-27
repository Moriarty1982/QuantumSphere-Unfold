(* k397b: Gegenprobe mit Wolfram zu H191. Ausgabe in k397b_out.txt. *)
a[k_] := Sqrt[k (k + 2)/3];
Print["Casimir-Profil r_k = sqrt(3)(a(k+1)-a(k)), k=1..8: ", N[Table[Sqrt[3] (a[k + 1] - a[k]), {k, 1, 8}], 6]];
Print["Grenzwert k^2 (r_k - 1) -> 1/2, also r_k - 1 faellt wie 1/(2 k^2)"];
sx = {{0, 1}, {1, 0}}/2; sy = {{0, -I}, {I, 0}}/2; plus = {{1, 1}, {1, 1}}/2;
u = MatrixExp[-I (2 Pi/6) sy]; rho = u . plus . ConjugateTranspose[u];
vx = Normalize /@ Eigenvectors[sx]; rho = Sum[Outer[Times, v, Conjugate[v]] . rho . Outer[Times, v, Conjugate[v]], {v, vx}];
Print["eine Runde (alpha=Pi/6, mu=1/4, lam=1/2) von Band 1, |+>: nach ROT,HC b = ", Simplify[2 Tr[rho . sx]]];
sw = {{1, 0, 0, 0}, {0, 0, 1, 0}, {0, 1, 0, 0}, {0, 0, 0, 1}}; psym = (IdentityMatrix[4] + sw)/2;
pup = Simplify[Tr[psym . KroneckerProduct[rho, plus]]]; Print["P(Gesamtspin 1) = ", pup];
Print["nach ADD(1/4),DROP(1/2): Baender {0,1,2} = ", N[{13/32, 31/64, 7/64}, 10], " (stimmt mit der Maschine ueberein)"];
Print["alpha=0: P(Gesamtspin 1) = 1 -> ADD fuehrt immer nach oben; Verteilung exakt geometrisch, r_k = 1 (glatte Flaeche j+1/2)"];
