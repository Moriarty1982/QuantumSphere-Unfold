(* k381b: Gegenprobe zu r70 (Wolfram Language, exakt).  Kugel der Feldzustaende, HC, Gewichte gegen Amplituden. *)
out = {};
p[s__] := AppendTo[out, StringJoin[ToString /@ {s}]];
ev = {e1, e2, e3}; bv = {b1, b2, b3};
st[ee_, bb_] := Module[{u = (ee.ee + bb.bb)/2}, {ee.bb/u, (ee.ee - bb.bb)/(2 u), Cross[ee, bb].Cross[ee, bb]/u^2, u}];
{bC, bS, b3q, u} = st[ev, bv];
p["W1 bC^2+bS^2+|ExB|^2/u^2-1 = ", Simplify[bC^2 + bS^2 + b3q - 1]];
v = {0, 0, Tanh[h]}; g = Cosh[h]; e0 = {q, 0, 0}; b0 = {q, 0, 0};
ep = g (e0 + Cross[v, b0]); bp = g (b0 - Cross[v, e0]);
{c, s, t, up} = st[ep, bp];
p["W2 Schub von R (E=B): bC-Sech[2h] = ", FullSimplify[c - Sech[2 h]], " ; bS = ", FullSimplify[s], " ; b3^2-Tanh[2h]^2 = ", FullSimplify[t - Tanh[2 h]^2]];
p["W3 p+ bei h=ArcTanh[be] minus 1/(1+be^2) = ", FullSimplify[((1 + c)/2 /. h -> ArcTanh[be]) - 1/(1 + be^2), 0 < be < 1]];
ec = (ev + bv)/2; {cc, cs, c3, uc} = st[ec, ec];
p["W4 HC-Bild: bC = ", Simplify[cc], ", bS = ", Simplify[cs], ", b3^2 = ", Simplify[c3], " ; Anteil-(1+bC)/2 = ", Simplify[uc/u - (1 + bC)/2]];
ea = (ev - bv)/2; {ac, as, a3, ua} = st[ea, -ea];
p["W5 Partner: bC = ", Simplify[ac], " ; Anteil-(1-bC)/2 = ", Simplify[ua/u - (1 - bC)/2]];
p["W6 Cos[2 ArcTan[be]]-(1-be^2)/(1+be^2) = ", FullSimplify[Cos[2 ArcTan[be]] - (1 - be^2)/(1 + be^2)]];
ht[m_] := (1 - m^2)/(1 + m^2); kk[m_] := (1 + m)/(1 - m);
p["W7 Gewichte 1:x, b/a=be: Hoehe-(1-x)/(1+x) = ", Simplify[ht[be] - (1 - be^2)/(1 + be^2)], " ; K-Exp[2 ArcTanh[be]] = ", FullSimplify[kk[be] - Exp[2 ArcTanh[be]], 0 < be < 1]];
p["W8 b/a=x=be^2: K-gammaL = ", Simplify[kk[be^2] - (1 + be^2)/(1 - be^2)], " ; Hoehe-Sech[2 ArcTanh[be^2]] = ", FullSimplify[ht[be^2] - Sech[2 ArcTanh[be^2]], 0 < be < 1]];
p["W9 1/cos(2 theta), tan(theta)=m: bei m=x: (gL+1/gL)/2-(1+x^2)/(1-x^2) = ", Simplify[((1 + be^2)/(1 - be^2) + (1 - be^2)/(1 + be^2))/2 - (1 + be^4)/(1 - be^4)], " ; bei m=be: 1/ht[be]-gammaL = ", Simplify[1/ht[be] - (1 + be^2)/(1 - be^2)]];
bn = 5494056410/10^10; x = bn^2; gL = (1 + x)/(1 - x);
row[m_] := StringJoin["B/A=", ToString[N[m^2, 6]], " Anteil=", ToString[N[m^2/(1 + m^2), 6]], " lamB/lamA=", ToString[N[1/m^4, 6]], " mH2/(eta f^2)=8 mu^2=", ToString[N[8 m^2, 6]], " ms2/mH2/eta=", ToString[N[m^2/Pi^2, 6]], " Winkel=", ToString[N[ArcCos[ht[m]]/Degree, 6]], " K=", ToString[N[kk[m], 6]], " 1/cos2theta=", ToString[N[1/ht[m], 6]], " m+^2,m-^2/(g^2 f^2)=", ToString[N[2/(1 + m^2), 6]], ",", ToString[N[2 m^2/(1 + m^2), 6]]];
p["W10 b/a=beta_sym: ", row[bn]];
p["W11 b/a=x:        ", row[x]];
p["W12 gamma_L=", N[gL, 7], " x=", N[x, 7], " eps=", N[ArcTanh[bn], 7], " Quadratur-Ellipse der Dublette bei M: Achsen 1/beta=", N[1/bn, 6]];
StringRiffle[out, "\n"]
