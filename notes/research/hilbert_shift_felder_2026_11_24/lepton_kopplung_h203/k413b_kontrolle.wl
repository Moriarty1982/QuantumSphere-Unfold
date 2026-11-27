(* k413b (H203): Wolfram-Kontrolle der tragenden H184-Regel.
   Farbfrequenz der Mode (i,j) = 2(v'(li)-v'(lj))/(li-lj); reproduziert die Spur-Invarianten.
   Stationaeres Potential v'(l)=(l-l1)(l-l2)(l-l3) -> alle Farbfrequenzen 0
   => die Stationaritaet, die die Leptonen (farblos) bindet, macht die Quarks (Farbe) masselos;
      Quarkmassen kommen aus F4-brechenden U-Termen, die der Lepton-Sektor nicht sieht. *)
rule[v_] := Simplify[2 (v'[li] - v'[lj])/(li - lj)];
Print["Tr W^2 (v=l^2): ", rule[#^2 &], "   (H184: 4)"];
Print["Tr W^3 (v=l^3): ", rule[#^3 &], "   (H184: 6(li+lj))"];
Print["Tr W^4 (v=l^4): ", rule[#^4 &], "   (H184: 8(li^2+li lj+lj^2))"];
vp[l_] := (l - l1)(l - l2)(l - l3);
colorFreq[a_, b_] := Simplify[2 (vp[a] - vp[b])/(a - b)];
Print["stationaer, Paar (l1,l2): ", colorFreq[l1, l2]];
Print["stationaer, Paar (l2,l3): ", colorFreq[l2, l3]];
Print["stationaer, Paar (l1,l3): ", colorFreq[l1, l3]];
