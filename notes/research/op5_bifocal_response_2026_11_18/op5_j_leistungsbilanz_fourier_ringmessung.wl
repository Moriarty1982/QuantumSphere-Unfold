Print["Kernel: ", $Version];
saa={{a,b},{c,d}}; sja={{e,f},{g,h}};
id=IdentityMatrix[2];
full=Join[saa,sja];
loss=id-ConjugateTranspose[full].full;
Print["power closure operator residual = ", Expand[
 id-ConjugateTranspose[saa].saa-ConjugateTranspose[sja].sja-loss]];
swap={{0,1},{1,0}};
Print["hidden-side mixing leaves the A deficit Gram residual = ", Expand[
 ConjugateTranspose[swap.sja].(swap.sja)-ConjugateTranspose[sja].sja]];
Print["one-percent amplitude power error allowances for amplitudes 0.003 and 1e-6 = ",
 N[(#^2-(99 #/100)^2)& /@ {3/1000,1/10^6},14]];
Print["illustrative scalar power nonidentifiability residual = ",
 Expand[(p+shift)+(bath-shift)-(p+bath)]];

w=(-1+I Sqrt[3])/2;
obs[z_,y_] := d0+d20 z^2+d50 z^5+d02 y^2+d05 y^5+d11 z y;
dft[p_,q_] := Total[Flatten[Table[Expand[w^Mod[-p i-q j,3] obs[w^i,w^j]],{i,0,2},{j,0,2}]]]/9;
Print["3x3 Fourier alias identities residuals = ",
 FullSimplify[{dft[0,0]-d0,dft[2,0]-d20-d50,dft[0,2]-d02-d05,dft[1,1]-d11}]];
tt=2/1000;
Print["mean echo and second-tag alias bounds at total radius 0.002 = ",
 N[{tt^3,tt^5}/(1-tt),14]];
f[u_] := u(1-Log[u]);
Print["radial log-kernel antiderivative residual = ", Expand[D[f[u],u]+Log[u]]];
Print["missing central 1 percent area log-kernel weight = ", N[f[1/100],14]];

qNum=72112379361105/10^16;
m3[q_] := (8q^3/(1-8q^3)-2q^3/(1+q^3))/3;
Print["3x3 symmetric exact-majorant limit check = ",N[8 ArcSin[m3[qNum]],14]];

Print["last 10 percent of radius log-kernel weight = ", N[f[1]-f[81/100],14]];
Print["centered log-kernel norms and common-bias cancellation = ",
 {2 f[1/2]-f[1], 2 (f[1/E]-1/E), 1-1}];
