(* Pruefung 23.11.2026: metrische Kegelgrenze (../op5_bifocal_response_2026_11_18/OP5_J_Metrische_Kegelgrenze.md) bei luminalen Vermittlern.
   Hauptteil: K = diag(A, 1, 1), V = {{b, j0, jm}, {j0, r0, 0}, {jm, 0, rm}}; Quadrate der Geschwindigkeiten = Eigenwerte von K^(-1/2) V K^(-1/2).
   Polteilung aus der Notiz: A = Z - 2 gm2/3, b = Z ch2 + 2 gm2/3 (rm - al), j0^2 = g02 al^2/2, jm^2 = 2 gm2/3 (rm^2 - rm al + al^2), al = a/q in [0, 1].
   Erkundung, nicht blind (die Notiz zeigt allgemein: bei r_i = 1 muss j_i verschwinden). *)
K = DiagonalMatrix[{A, 1, 1}];
V[b_, j0_, jm_, r0_, rm_] := {{b, j0, jm}, {j0, r0, 0}, {jm, 0, rm}};
Aof[Z_, gm2_] := Z - 2 gm2/3;
bof[Z_, ch2_, gm2_, rm_, al_] := Z ch2 + 2 gm2/3 (rm - al);
j0sq[g02_, al_] := g02 al^2/2;
jmsq[gm2_, rm_, al_] := 2 gm2/3 (rm^2 - rm al + al^2);
speeds[Z_, ch2_, g02_, gm2_, r0_, rm_, al_] := Module[{AA = Aof[Z, gm2], Kh},
   Kh = DiagonalMatrix[{1/Sqrt[AA], 1, 1}];
   Eigenvalues[N[Kh . V[bof[Z, ch2, gm2, rm, al], Sqrt[j0sq[g02, al]], Sqrt[jmsq[gm2, rm, al]], r0, rm] . Kh, 30]]];
Print["Kontrolle Vergleichsmodell (Z=1, c_h^2=r0=rm=1/2, g^2=3/100): max Geschwindigkeit^2 ueber alpha = ",
  Max[Table[Max[speeds[1, 1/2, 3/100, 3/100, 1/2, 1/2, al]], {al, 0, 1, 1/20}]]];
Print["luminal r0 = rm = 1, sonst gleich: max Geschwindigkeit^2 = ", Max[Table[Max[speeds[1, 1/2, 3/100, 3/100, 1, 1, al]], {al, 0, 1, 1/20}]]];
Print["luminal r0 = rm = 1 und c_h^2 = 1 (W2, r33): max Geschwindigkeit^2 = ", Max[Table[Max[speeds[1, 1, 3/100, 3/100, 1, 1, al]], {al, 0, 1, 1/20}]]];
Print["nur masseloser Kanal luminal (r0 = 1, rm = 1/2), c_h^2 = 1/2: max = ", Max[Table[Max[speeds[1, 1/2, 3/100, 3/100, 1, 1/2, al]], {al, 0, 1, 1/20}]]];
Print["nur massiver Kanal luminal (r0 = 1/2, rm = 1), c_h^2 = 1/2: max = ", Max[Table[Max[speeds[1, 1/2, 3/100, 3/100, 1/2, 1, al]], {al, 0, 1, 1/20}]]];
Print["Hauptminor von K - V im luminalen Kanal i: det = -j_i^2; j_m^2 bei rm = 1: ", Simplify[jmsq[gm2, 1, al]], " > 0 fuer alle alpha (Minimum ", Minimize[{jmsq[3/100, 1, al], 0 <= al <= 1}, al], ")"];
