(* k412b (H202): unabhaengige Wolfram-Kontrolle des Rangs der Struktur-Abbildung.
   Stimmt mit numpy (k412_test_h202.py) ueberein: Rang 4 (Block gerade 2 + ungerade 2)
   -> alle vier Koeffizienten (A,B,C,D) unabhaengig -> D/B frei. *)
coup = {
  {-6, 0, 0, 0}, {-24, 0, 0, 0}, {-60, -30, 0, 0}, {-108, -234, 0, 0},   (* g3,g4,g5,g6 *)
  {0, 0, -1/3, 0}, {0, 0, 0, -1/3}, {0, 0, -1, 1/6}, {0, 0, -1, -1/6}};  (* c2,c4/c5,c7/c9,c11 *)
M = Transpose[coup];
even = Select[coup, #[[3]] == 0 && #[[4]] == 0 &][[All, {1, 2}]];
odd  = Select[coup, #[[1]] == 0 && #[[2]] == 0 &][[All, {3, 4}]];
Print["Rang volle Abbildung 4x8 = ", MatrixRank[M]];
Print["Rang (A,B)-Block (gerade) = ", MatrixRank[Transpose[even]]];
Print["Rang (C,D)-Block (ungerade) = ", MatrixRank[Transpose[odd]]];
