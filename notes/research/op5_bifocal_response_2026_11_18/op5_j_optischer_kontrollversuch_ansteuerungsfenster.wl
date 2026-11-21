Print["Kernel: ", $Version];
yy[x_] := t+r x+c2 x^2+c3 x^3+c4 x^4;
Print["three-load even closure and five-load odd closure residuals = ", Expand[
 {yy[a]+yy[-a]-2 yy[0]-(2 c2 a^2+2 c4 a^4),
 ((yy[2a]-yy[-2a])/(4a)-(yy[a]-yy[-a])/(2a))-3 c3 a^2}]];
Print["affine contamination invisible in both closures =",Expand[
 {(t0+t1 a)+(t0-t1 a)-2t0, (4a t1)/(4a)-(2a t1)/(2a)}]];
bd=2001/10^11+3/10^8+4/10^8;
Print["A-only direct witness per-state radius and cross-quotient log bound =", N[{bd,-4 Log[1-bd/(99/100)]},15]];
Print["illustrative affine-null closure noise radius = ",N[4(2/10^8),10]];

hf=360329/10^6; hc=1973269804/10^16; band=10^8; eq=25/10^10;
Print["delay and single optical path ceilings = ", N[{eq/(2 Pi band),eq hc/hf},15]];
Print["phase contrast decomposition residual = ", Expand[
 (fc+df/2) dp-(fc-df/2) dm- (df(dp+dm)/2+fc(dp-dm))]];
pt=9/10^6; bound=1791/10^10; earlier=141250470956826/10^21;
tolx=(bound-earlier)/(pt+bound);
Print["complex load error and one-way phase ceilings = ", N[{tolx,ArcSin[tolx/2]},15]];

Print["rest-to-rest time acceleration coefficient residual = ",
 Integrate[t,{t,0,tt/2}]+Integrate[tt-t,{t,tt/2,tt}]-tt^2/4];
Print["relative b4 product transfer identity residual = ",
 Expand[(1+ek)(1+ep)-1-(ek+(1+ek)ep)]];
