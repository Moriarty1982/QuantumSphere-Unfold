Print["Kernel: ", $Version];
deltaLeft = lambda tRL tLR/(1 - rL lambda);
Print["left load identity residual = ", Together[deltaLeft - tRL lambda (tLR + rL tLR lambda/(1-rL lambda))]];
r = 3512/10^9; cross = 38597/10^12;
lam = 2/10^7; left = lam/(1-r lam);
loaded = r+left; alpha = 1/10; mix = 1/100;
crossExt = 1/10^6 + cross + 2 mix r + left + alpha loaded^2/(1-alpha loaded);
diagExt = 1/10^4 + loaded/(1-alpha loaded);
tErr = 2001/10^11;
logErr = 4/10^7 - 4 Log[1 - (tErr+crossExt (33/10^4)/(1-diagExt))/(99/100)];
Print["loaded front increment and outer cross, outer diagonal, full log error = ", N[{left,crossExt,diagExt,logErr},15]];
Print["fixture example passes = ", logErr < 5/10^7];
Print["scalar fixture inverse and sensitivity residuals = ", Together[
 {z/(1+z a) /. z -> rr/(1-a rr),
  zz/(1+zz a)-z/(1+z a)-(zz-z)/((1+zz a)(1+z a))} - {rr,0}]];

id = IdentityMatrix[2]; aa={{1/10,I/20},{1/25,0}};
rr2={{1/20,1/50},{I/25,1/15}}; err={{0,1/1000},{0,0}};
zz2 = rr2.Inverse[id-aa.rr2]; zh = zz2+err;
rh = Inverse[id+zh.aa].zh;
Print["noncommuting inverse and propagation residuals = ", Map[Together,{
 Inverse[id+zz2.aa].zz2-rr2, rh-rr2-Inverse[id+zh.aa].err.(id-aa.rr2)}, {3}]];

p[i_,f_] := h[f]+g[f](len[i]+c[i,f])+j[f] ell[i,f];
dc[f_] := c[1,f]-c[0,f]; de[f_] := ell[1,f]-ell[0,f];
Print["two-length chromatic cancellation residual = ", Expand[
 p[1,1]+p[0,0]-p[0,1]-p[1,0]-(len[1]-len[0])(g[1]-g[0])-
 (g[1] dc[1]-g[0] dc[0]+j[1] de[1]-j[0] de[0])]];
Print["two-path pilot correction residual = ", Together[
 (kj/kref) kref (c0+ell0) - (ka/kref) kref c0 - ((kj-ka)c0+kj ell0)]];
xy = {xx,yy}; radvar=(xx^2+yy^2)/radius^2; profile=radvar^2-kappa radvar^3;
lap = Total[D[profile,{#,2}]& /@ xy];
screen = FullSimplify[radius^4 Table[D[lap,qi,qj],{qi,xy},{qj,xy}]/32,radius>0];
screenRef = (1-(9/2) kappa radvar) id - 9 kappa Outer[Times,xy,xy]/radius^2;
Print["screen and pure Weyl ring residuals = ", FullSimplify[{
 screen-screenRef, (screen/.{xx->radius/(3 Sqrt[kappa]),yy->0})-DiagonalMatrix[{-1/2,1/2}]},
 radius>0&&kappa>0]];

pot[s_] := 16 b4/radius^2 (s-9 kappa s^2)-b2 (s^2-4 kappa s^3)+
 b0 radius^2/36 (s^3-(9/4) kappa s^4);
f[s_] := Derivative[2][pot][s];
Print["ordinary Weyl separation and second difference residuals = ", Expand[{
 Det[{{s1,s1 f[s1]},{s2,s2 f[s2]}}]-s1 s2 (f[s2]-f[s1]),
 f[3 step]-2 f[2 step]+f[step]+(3/2)b0 kappa radius^2 step^2}]];
