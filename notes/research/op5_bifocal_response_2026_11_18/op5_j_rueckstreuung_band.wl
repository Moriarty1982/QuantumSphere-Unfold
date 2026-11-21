ClearAll["Global`*"];
Print["Kernel: ", $Version];
ri = (kap - k)/(kap + k);
p = Exp[2 I kap ell];
f[z_] := (1 - ri) (Exp[I kap z] + ri Exp[I kap (2 ell - z)])/(1 - ri^2 p);
boundary[z_] := (1 + ri) (Exp[I kap z] + ri Exp[I kap (2 ell - z)])/(2 I kap (1 - ri^2 p));
Print["Weighted boundary Green kernel residual: ", FullSimplify[k boundary[z] - f[z]/(2 I)]];
int[a_] := (Exp[I a ell] - 1)/(I a);
Print["First return conversion integrand residual: ", FullSimplify[
 D[(1 - ri) ( (Exp[I (kj + kap) z] - 1)/(I (kj + kap)) +
  ri p (Exp[I (kj - kap) z] - 1)/(I (kj - kap)) )/(1 - ri^2 p), z]
  - Exp[I kj z] f[z]]];
Print["Central sum and difference integral residuals: ",
 FullSimplify[{int[kj + kap], int[kj - kap], int[2 kj]} /.
   {ell -> 1, kj -> 9999 Pi, kap -> 10001 Pi}]];
(* Same illustrative nondispersive band as the preceding exploration. *)
ka0 = 10000 Pi; kj0 = 9999 Pi; kap0 = 10001 Pi;
r0 = 1/20001; x = 1/1000; u = (2067833848/10^16)/(360329/10^6);
strengthMax = ((kap0^2 - ka0^2)/ka0) (1 + u);
dmax = strengthMax x^2;
cmax = strengthMax x;
eMax = strengthMax (x^2 + Sqrt[x^4 + 4 x^2])/2;
a = 1/(1 + r0); b = a r0;
cdir = Max[1/2, ka0/(2 kap0 (1 - r0^2))];
cimg = ka0 (2 r0 + r0^2)/(2 kap0 (1 - r0^2));
cTotal = 1/2; theta = cTotal eMax;
rRef = 2 r0 kap0 u/(1 - r0^2);
firstBound = u (dmax + cmax)/(2 (1 - u));
secondBound = cdir eMax^2/((1 - u) kj0) +
  eMax^2 (cimg + (2 r0 + r0^2) cTotal)/2;
lastBound = theta^3/(1 - theta);
total = rRef + firstBound + secondBound + lastBound;
Print["Uniform band contributions {reference, first, second, tail, total}: ",
 N[{rRef, firstBound, secondBound, lastBound, total}, 10]];
Print["Return rest bound at unit return norm: ", N[total/(1 - total), 10]];
