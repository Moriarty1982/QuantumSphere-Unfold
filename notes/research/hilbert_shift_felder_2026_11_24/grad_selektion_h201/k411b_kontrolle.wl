(* k411b (H201): unabhaengige Wolfram-Kontrolle der Grad-Zerlegung.
   Stimmt exakt mit sympy (k411_test_h201.py) ueberein: B (gerade l_k^2) erst Grad 5,
   D (ungerade l_k^2) schon Grad 4 -> verschiedene Grade, keine Grad-Selektion moeglich. *)
Clear[e1, e2, lk, s, pr];
hcomp[m_] := hcomp[m] = Which[m == 0, 1, m == 1, e1, True, Expand[e1 hcomp[m-1] - e2 hcomp[m-2]]];
subVac = {e1 -> 3 - lk, e2 -> 3/2 - lk (3 - lk)};
Print["ladungsGERADE F4-Kruemmung 2n*H[n-2] auf Vakuum (l_k, l_k^2):"];
Do[Module[{cur = Expand[(2 n hcomp[n-2]) /. subVac]},
   Print["  Grad ", n, ": A(l_k)=", Coefficient[cur, lk, 1], "  B(l_k^2)=", Coefficient[cur, lk, 2]]],
  {n, 2, 6}];
subSym = {s -> 3 - lk, pr -> 3/2 - 3 lk + lk^2};
odd = {"c1" -> 2/3, "c2" -> (1/3) s, "c4/c5" -> (1/3)(s^2 - 2 pr),
       "c7/c9" -> (1/6) s^2, "c11" -> (1/2)(s^2 - 2 pr) + (1/3) pr};
Print["ladungsUNGERADE H186-Kruemmungen (Grad 4) auf Vakuum (l_k, l_k^2):"];
Do[Module[{red = Expand[(odd[[i, 2]]) /. subSym]},
   Print["  ", odd[[i, 1]], ": C(l_k)=", Coefficient[red, lk, 1], "  D(l_k^2)=", Coefficient[red, lk, 2]]],
  {i, Length[odd]}];
