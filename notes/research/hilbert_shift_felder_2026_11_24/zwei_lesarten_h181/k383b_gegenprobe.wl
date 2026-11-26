(* k383b: unabhaengige Gegenprobe zu k383 (Test H181) in Wolfram Language. Symbolische Reste und Zahlen getrennt. *)
Module[{b, gL, eW, eA, bn = 5494056410/10^10, mZ = 911876/10^4, mh, mw},
 gL = (1 + b^2)/(1 - b^2); eW = ArcTanh[b]; eA = ArcTanh[b^2];
 mh[k_] := 125.20 Sqrt[(16 k^2 - 2.77)/20.42]; mw[c_] := mZ c/Sqrt[1 + c^2];
 Print["W1 cosh 2etaW - gammaL = ", FullSimplify[TrigToExp[Cosh[2 eW]] - gL, 0 < b < 1]];
 Print["W2 exp(2etaA) - gammaL = ", FullSimplify[TrigToExp[Exp[2 eA]] - gL, 0 < b < 1]];
 Print["W3 cosh 2etaA - (gammaL+1/gammaL)/2 = ", FullSimplify[TrigToExp[Cosh[2 eA]] - (gL + 1/gL)/2, 0 < b < 1]];
 Print["W4 tanh^2 etaA = ", FullSimplify[Tanh[eA]^2, 0 < b < 1], "; num ", N[bn^4, 10]];
 Print["W5 mW(W,D) = ", N[mw[gL /. b -> bn], 9], "; mW(A,D) = ", N[mw[(gL + 1/gL)/2 /. b -> bn], 9]];
 Print["W6 mh(kappa=gammaL) = ", mh[N[gL /. b -> bn, 12]], "; mh((gL+1/gL)/2) = ", mh[N[(gL + 1/gL)/2 /. b -> bn, 12]], "; mh(cosh etaW) = ", mh[N[1/Sqrt[1 - bn^2], 12]], "; mh(coth 2etaW) = ", mh[N[(1 + bn^2)/(2 bn), 12]]];
 Print["W7 2etaA = ", N[2 ArcTanh[bn^2], 12], "; etaW = ", N[ArcTanh[bn], 12], "; ln gammaL = ", N[Log[gL /. b -> bn], 12]];
 Print["W8 z mW(A,D) = ", (N[mw[(gL + 1/gL)/2 /. b -> bn]] - 80.3625)/Sqrt[0.0077^2 + 0.0018^2], "; z OmegaM(A,D) DESI/Planck = ", (N[bn^4] - 0.2975)/0.0086, " / ", (N[bn^4] - 0.315)/0.007];
]
