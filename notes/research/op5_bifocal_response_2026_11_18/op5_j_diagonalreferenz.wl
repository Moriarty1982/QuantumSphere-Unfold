Print["Kernel: ", $Version];
h[w_] := (1 + I w - Exp[I w])/w^2;
a0 = 10000 Pi; j0 = 9999 Pi; u0 = 10001 Pi;
Print["affine integral and two center residuals = ", FullSimplify[{
 Integrate[(1 - d) Exp[I w d], {d, 0, 1}, Assumptions -> w != 0] - h[w],
 h[j0 - u0] - I/(j0 - u0), h[j0 + u0] - I/(j0 + u0)}]];
Print["J forward cancellation residual = ", Together[
 1 - (kap^2 - ka^2)/(2 kap) (1/(kap - kj) + 1/(kap + kj)) -
 (ka^2 - kj^2)/(kap^2 - kj^2)]];
uBand = (2067833848/10^16)/(360329/10^6);
tol = 1/(4 10^6); n0 = u0/a0; mu2 = 1 - (j0/a0)^2; mix = 1/1000;
aMax = a0 (1 + uBand) (1 + tol);
du = Sqrt[(u0 (uBand + tol + uBand tol) + aMax tol)^2 + (aMax tol)^2];
j[e_, l_] := a0 (1 + l) Sqrt[(1 + e)^2 - mu2];
dj = Max[j[uBand, tol] - j0, j0 - j[-uBand, -tol]];
rad = du + dj;
dMinus = u0 - j0 - rad; dPlus = u0 + j0 - rad;
direct = 1/dMinus + rad/dMinus^2 + 1/dPlus + rad/dPlus^2;
num = Sqrt[(n0 - 1 + tol)^2 + tol^2];
rho = num/(n0 + 1 - tol);
images = 2 rho + rho^2;
s = aMax num Sqrt[(n0 + 1 + tol)^2 + tol^2];
cBound = 1/(1 - rho); f0 = (1 + rho)/(1 - rho);
kernel = Max[1/2, (1 + rho)^2/(2 (n0 - tol) (1 - rho^2))];
theta = kernel s (mix^2 + Sqrt[mix^4 + 4 mix^2])/2;
aSecond = (s mix cBound)^2 (direct + images)/4;
aThird = f0 (kernel s mix)^2 (kernel s mix^2);
aTail = f0 theta^4/(1 - theta);
aBound = aSecond + aThird + aTail;
jFirst = s mix^2/2;
gamma = (a0^2 - j0^2) (1 + tol)^2/(dMinus dPlus);
jCombined = jFirst (gamma + (1 + gamma) rho^2/(1 - rho^2));
jRemainder = (s mix)^2 (rad/dMinus^2 + rad/dPlus^2 + images)/
   (4 (n0 - tol) (1 - rho^2)) + (s mix^2)^2/4;
jTail = f0 theta^3/(1 - theta);
jBound = jCombined + jRemainder + jTail;
refBudget = 6234/10^9;
Print["A bounds {order 2, order 3, orders >= 4, total} = ", N[{aSecond, aThird, aTail, aBound}, 13]];
Print["J bounds {combined leading terms, other second order, orders >= 3, total} = ",
 N[{jCombined, jRemainder, jTail, jBound}, 13]];
Print["remaining calibration budget {A only, both diagonals} = ", N[refBudget - {aBound, Max[aBound, jBound]}, 13]];
id = IdentityMatrix[2]; zero = ConstantArray[0, {2, 2}];
sample[e_, l_, dn_, loss_] := Module[{aa, jj, uu, ri, strength, kk, basis, v, gen, prop, rr, tt, tA},
 aa = a0 (1 + e) (1 + l); jj = j[e, l]; uu = aa (n0 + dn + I loss);
 ri = (uu - aa)/(uu + aa);
 strength = (uu^2 - aa^2)/aa;
 kk = DiagonalMatrix[{jj, aa}];
 basis = ArrayFlatten[{{id, id}, {I kk, -I kk}}];
 v = strength {{mix^2, mix}, {mix, 1}};
 gen = ArrayFlatten[{{zero, id}, {-kk.kk - kk.v, zero}}];
 prop = Inverse[N[basis, 60]].MatrixExp[N[gen, 60]].N[basis, 60];
 rr = -LinearSolve[prop[[3 ;; 4, 3 ;; 4]], prop[[3 ;; 4, 1 ;; 2]]];
 tt = DiagonalMatrix[Exp[-I N[{jj, aa}, 60]]].(
   prop[[1 ;; 2, 1 ;; 2]] + prop[[1 ;; 2, 3 ;; 4]].rr);
 tA = Exp[I (uu - aa)] (1 - ri^2)/(1 - ri^2 Exp[2 I uu]);
 {Abs[tt[[2, 2]] - N[tA, 60]], Abs[tt[[1, 1]] - 1]}];
examples = sample @@@ {{0, 0, 0, 0}, {uBand, tol, tol, tol}, {-uBand, -tol, -tol, 0}};
Print["transfer controls {A, J} at center and two band edges = ", N[examples, 12]];
Print["all controls within bounds = ", And @@ Map[(#[[1]] < aBound && #[[2]] < jBound) &, examples]];
Print["sufficient index excursion with both scalar diagonals, center error zero or 2e-6 = ",
  N[((4596/10^9 - 181745/10^11 - #)/aMax &) /@ {0, 2/10^6}, 13]];
