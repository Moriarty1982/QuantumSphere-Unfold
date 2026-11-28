(* k436b: unabhaengige Wolfram-Gegenprobe zu k436 (Erkundung). Aufruf: wolframscript -file k436b_gegenprobe.wl > k436b_out.txt *)
nn = ph^3 - 3 ph r^2 + 2 r^3 Cos[3 d];
circ = {{ph, r Exp[I d], r Exp[-I d]}, {r Exp[-I d], ph, r Exp[I d]}, {r Exp[I d], r Exp[-I d], ph}};
Print["1) det(Zirkulante) - N = ", Simplify[ExpToTrig[Det[circ]] - nn]];
Print["1) N^2 Fourier: ", Collect[TrigReduce[Expand[nn^2]], {Cos[3 d], Cos[6 d]}, Factor]];
f6 = c1 (ph^6 + r^6) + c2 (ph^2 r^4 + ph^4 r^2) + c3 (ph^2 r^4 + ph^4 r^2) Cos[2 d] + c4 ph^3 r^3 Cos[d] + b3 ph^3 r^3 Cos[3 d];
Print["2) F6(phi;-c4,-b3) - F6(-phi;c4,b3) = ", Simplify[(f6 /. {c4 -> -c4, b3 -> -b3}) - (f6 /. ph -> -ph)]];
dv[d0_, o0_] := Simplify[TrigExpand[(b3 Cos[3 (d0 + p)] + c4 Cos[d0 + p]) - (b3 Cos[3 (o0 + p)] + c4 Cos[o0 + p])]];
xl = Pi/12 - 0.2222220470731;
Print["3) Im: ", dv[5 Pi/4, Pi/4], " ; bei x_lepton: ", N[dv[5 Pi/4, Pi/4] /. p -> xl]];
Print["3) Re: ", dv[Pi/2, 3 Pi/2], " ; bei x_lepton: ", N[dv[Pi/2, 3 Pi/2] /. p -> xl]];
Print["3) Keilgrenzen beta3/c4: Re ", N[Sin[xl]/Sin[3 xl], 6], ", Im ", N[Cos[Pi/4 + xl]/Cos[Pi/4 - 3 xl], 6]];
Print["3) Keilanteil: ", N[(Pi - (ArcTan[N[Sin[xl]/Sin[3 xl]]^-1 ] - ArcTan[N[Cos[Pi/4 - 3 xl]/Cos[Pi/4 + xl]]]))/(2 Pi), 5]];
