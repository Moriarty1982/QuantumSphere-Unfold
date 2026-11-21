Print["Kernel: ", $Version];
e0=360329/10^6; hc=1973269804/10^16;
a0=10000 Pi; u0=10001 Pi; j0=9999 Pi;
l0=a0 hc/e0;
u=(2067833848/10^16)/e0;
n0=u0/a0; m2=1-(j0/a0)^2;
mix=1/1000; g0=(u0^2-a0^2) mix/(2 a0);
p=9/10^6;
Print["marker length, illustrative matched lengths full and half harmonic m = ",
 N[{l0,Pi l0/(2 g0),Pi l0/g0},14]];
Print["uniform unmatched conversion probability bound = ", N[4 g0^2/((u0-j0)^2+4 g0^2),14]];
bd=a0 (Abs[n0-a0/j0] u+m2 u^2/(2 ((1-u)^2-m2)^(3/2)));
Print["band mismatch in reference-length units and detuning ratio half harmonic = ", N[{bd,bd/g0},14]];
Print["single-error index tolerances and pulse-area relative tolerance = ",
 N[Join[{2 g0/a0,g0/a0} p/Sqrt[1-p^2],{ArcSin[p]/(Pi/2)}],14]];
rat=(a0/(4 10^6))/(2 g0);
bc=Sqrt[rat^2-1];
Print["loss to twice coupling ratio, maximum transfer amplitude with A loss = ",
 N[{rat,Exp[-rat ArcTanh[bc/rat]/bc]},14]];
Print["transfer peak identity residual = ",
 FullSimplify[Sinh[ArcTanh[beta/r]]-beta,beta>0&&r>0&&r^2-beta^2==1]];

pol[u_] := ChebyshevT[4,4u-2];
moment=Integrate[pol[x],{x,0,1/4}];
tvLower=2 moment/(1/2)-1;
Print["annulus Chebyshev core moment and variation lower bound = ",{moment,tvLower}];
lake=1/100; dd=5/10^7;
Print["monitor residual from J phase error example = ",N[lake Sin[dd/2],15]];
Print["opposite projection average and diagnostic residuals = ", Expand[
 {((1+r)+(1-r))/2-1,((1+r)-(1-r))/2-r}]];

Print["Chebyshev moment lower bounds for total variation (core, support) = ",
 {ChebyshevT[5,2], ChebyshevT[5,5/4], ChebyshevT[5,9/5]}];
ev=5/10^9;
mon=((1+ev)^4+(1+ev)^2-2)/(1-ev)^2;
ee=33346568111499/10^20;
remaining=Sin[6/(8 10^6)]-ee;
Print["pilot-transfer budget and visible-rest acceptance = ",
 N[{mon,(remaining-ee-mon)/(1+mon),(4/10^6) Sin[1/2000]},14]];

cut=Expand[Sum[Binomial[25,i] z^i(1-z)^(25-i),{i,0,12}]];
op[f_] := Expand[xi D[f,{xi,2}]+D[f,xi]];
bernAbs[poly_] := Module[{co=CoefficientList[poly,w],n},n=Length[co]-1;
 Max[Abs[Table[Sum[co[[j+1]] Binomial[k,j]/Binomial[n,j],{j,0,k}],{k,0,n}]]]];
tvBound[aa_,bb_,n_] := Module[{pot,dx=(bb-aa)/n,dp},
 pot=Nest[op,Expand[D[xi^5 (cut/.z->(xi-aa)/(bb-aa)),xi]/5],4]/576;
 dp=D[pot,xi];
 dx Total[Table[bernAbs[Expand[dp/.xi->aa+(i+w)dx]],{i,0,n-1}]]];
Print["gradient variation Bernstein upper (32 cells) = ",
 N[{tvBound[1/4,3/4,32],tvBound[1/4,7/8,32],tvBound[1/10,9/10,32]},14]];
