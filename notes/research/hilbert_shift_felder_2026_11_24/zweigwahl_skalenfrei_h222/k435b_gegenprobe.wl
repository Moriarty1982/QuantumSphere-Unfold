(* k435b (H222): unabhaengige Wolfram-Gegenprobe zu k435.
   d) symbolisch: det Y, D3-Invarianz von cos 3d, niedrigste invariante Mode
   a/b) Zweige nach Drehung exakt, Wahl max cos 3d;  c) R am verworfenen Zweig;  e) q = -eps
   Aufruf: wolframscript -file k435b_gegenprobe.wl > k435b_out.txt *)
detY = Simplify[TrigReduce[Product[1 + a Cos[d + 2 Pi k/3], {k, 0, 2}]]];
Print["d(i) det Y/mu^3 = ", detY, ";  Differenz zu 1-3a^2/4+a^3/4 Cos[3d]: ", Simplify[detY - (1 - 3 a^2/4 + a^3/4 Cos[3 d])]];
Print["d(ii) cos3(-d)-cos3d = ", Simplify[Cos[-3 d] - Cos[3 d]], ";  cos3(d+2Pi/3)-cos3d = ", Simplify[Cos[3 (d + 2 Pi/3)] - Cos[3 d]],
  ";  cos3(d+Pi/3)+cos3d = ", Simplify[Cos[3 (d + Pi/3)] + Cos[3 d]]];
inv = Select[Range[1, 6], Function[n, Simplify[Cos[n (d + 2 Pi/3)] - Cos[n d]] === 0]];
Print["d(iii) Moden cos(n d), n=1..6, invariant unter d->d+2Pi/3 (cos ist reflexionsgerade): n = ", inv, "  (sin n d: reflexionsungerade, faellt weg)"];
xl = Pi/12 - 0.2222220470731`30;
br[ap_, chi_] := Module[{s = Solve[{D[-ap Cos[2 (d - chi)], d] == 0, 0 <= d < 2 Pi}, d], dd},
   dd = d /. s; Select[dd, (D[-ap Cos[2 (x - chi)], {x, 2}] /. x -> #) > 0 &]];
fold[x_] := With[{y = Mod[x, 2 Pi/3]}, Min[y, 2 Pi/3 - y]];
Do[Module[{bi = Union[N[fold /@ br[1, Pi/4 + ph], 20]], bn = Union[N[fold /@ br[-1, ph], 20]]},
   Print["a/b) phi=", N[ph, 6], ": Im-Zweige ", N[bi, 9], " cos3d ", N[Cos[3 bi], 6], " -> Wahl ", N[First@MaximalBy[bi, Cos[3 #] &], 9],
    " (Ziel ", N[Pi/12 - ph, 9], ");  Re-Zweige ", N[bn, 9], " cos3d ", N[Cos[3 bn], 6], " -> Wahl ", N[First@MaximalBy[bn, Cos[3 #] &], 9],
    " (Ziel ", N[Pi/6 - ph, 9], ")"]], {ph, {1/100, xl, 6/100}}];
dm21 = 7.537*^-5; s21 = 0.097*^-5; dm31 = 2.511*^-3; s31 = 0.0205*^-3; rObs = dm21/dm31; sR = rObs Sqrt[(s21/dm21)^2 + (s31/dm31)^2];
rNO[dd_] := Module[{m = Sort[N[Table[(1 + Sqrt[2] Cos[dd + 2 Pi k/3])^2, {k, 0, 2}], 20]]}, (m[[2]]^2 - m[[1]]^2)/(m[[3]]^2 - m[[1]]^2)];
Print["c) gewaehlt pi/6-x: R_NO = ", NumberForm[rNO[Pi/6 - xl], 7], " (", NumberForm[(rNO[Pi/6 - xl] - rObs)/sR, 3], " sigma);  verworfen pi/6+x: R_NO = ",
  NumberForm[rNO[Pi/6 + xl], 7], " (", NumberForm[(rNO[Pi/6 + xl] - rObs)/sR, 3], " sigma)"];
Do[Module[{fi, fn},
   fi = FindMinimum[-Cos[2 (d - Pi/4 - xl)] - eps Cos[3 d], {d, 7 Pi/12 + 0.05 + 2 Pi/3}, WorkingPrecision -> 30, AccuracyGoal -> 20];
   fn = FindMinimum[Cos[2 (d - xl)] - eps Cos[3 d], {d, Pi/2 + 0.05}, WorkingPrecision -> 30, AccuracyGoal -> 20];
   Print["e) eps=", ScientificForm[N[eps], 2], ": Im Minimum gefaltet ", NumberForm[fold[d /. fi[[2]]], 12], " Abstand ", ScientificForm[N[Abs[fold[d /. fi[[2]]] - (Pi/12 - xl)]], 3],
    ";  Re Minimum gefaltet ", NumberForm[fold[d /. fn[[2]]], 12], " Abstand ", ScientificForm[N[Abs[fold[d /. fn[[2]]] - (Pi/6 - xl)]], 3]]], {eps, {10^-2, 10^-4, 10^-6}}];
Print["e) Wahl im Grenzfall: V(Zweig 1) - V(Zweig 2) = -q (cos3d1 - cos3d2); Im: cos3(5Pi/4+p) - cos3(Pi/4+p) = ", Simplify[Cos[3 (5 Pi/4 + p)] - Cos[3 (Pi/4 + p)]], ";  Re: cos3(Pi/2+p) - cos3(3Pi/2+p) = ", Simplify[Cos[3 (Pi/2 + p)] - Cos[3 (3 Pi/2 + p)]]];
