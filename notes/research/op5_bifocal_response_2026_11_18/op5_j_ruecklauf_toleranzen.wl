Print["Kernel: ", $Version];
energy = 360329/10^6;
bandHalf = 2067833848/10^16;
u = bandHalf/energy;
a0 = 10000 Pi; j0 = 9999 Pi; u0 = 10001 Pi;
n0 = u0/a0; mu2 = 1 - (j0/a0)^2;
x = 1/1000;
epsilon = 981742885/10^14;
returnLimit = (epsilon/2)/(1 + epsilon/2);
prop[e_] := Sqrt[(1 + e)^2 - mu2]/Sqrt[1 - mu2];
Print["center checks (J phase, A phase, three integral numerators) = ",
  FullSimplify[{a0 Sqrt[1 - mu2] - j0, u0 - a0 - Pi,
    Exp[2 I j0] - 1, Exp[I (j0 + u0)] - 1, Exp[I (j0 - u0)] - 1}]];
Print["J rest energy eV = ", N[energy Sqrt[mu2], 12]];
Print["J slope relative to proportional model = ", N[1/(1 - mu2), 15]];
Print["J-only band phase excursion (massive, proportional) = ",
  N[{j0 Max[prop[u] - 1, 1 - prop[-u]], j0 u}, 13]];
bounds[thickness_, index_, loss_] := Module[
  {aMax, phase, absorp, du, dj, num, rho, s, ratio, d, f, b, direct, image, kern, theta,
   f0, minwave, bJJ, bPlus, bMinus, base, first, second, tail, refl},
  aMax = a0 (1 + u) (1 + thickness);
  phase = u0 (u + thickness + u thickness) + aMax index;
  absorp = aMax loss;
  du = Sqrt[phase^2 + absorp^2];
  dj = j0 Max[(1 + thickness) prop[u] - 1, 1 - (1 - thickness) prop[-u]];
  num = Sqrt[(n0 - 1 + index)^2 + loss^2];
  rho = num/(n0 + 1 - index);
  s = aMax num Sqrt[(n0 + 1 + index)^2 + loss^2];
  ratio = 1/(n0 - index);
  d = s (x^2 + Sqrt[x^4 + 4 x^2])/2;
  f = 1/(1 - rho); b = f rho;
  direct = Max[1/2, ratio/(2 (1 - rho^2))];
  image = ratio (2 rho + rho^2)/(2 (1 - rho^2));
  kern = Max[1/2, ratio (1 + rho)^2/(2 (1 - rho^2))];
  theta = kern d; f0 = (1 + rho)/(1 - rho);
  minwave = Min[j0 - dj, u0 - du];
  bJJ = dj/(j0 - dj);
  bPlus = (dj + du)/(j0 + u0 - dj - du);
  bMinus = (dj + du)/(u0 - j0 - dj - du);
  base = 2 rho du/(1 - rho^2);
  first = s (x^2 bJJ + x f (bPlus + rho bMinus))/2;
  second = d^2 (f^2 direct/minwave + (f^2 image + (2 f b + b^2) kern)/2);
  tail = f0 theta^3/(1 - theta);
  refl = base + first + second + tail;
  {phase, absorp, du, dj, rho, theta, base, first, second, tail, refl, refl/(1 - refl),
    aMax (index + thickness/(10000 (1 + thickness)) + u/(10000 (1 + u))), 1 - Exp[-absorp]}
];
t = 1/(4 10^6);
box = bounds[t, t, t];
Print["box: Re U radius, Im U max, complex U radius, J radius, rho, theta = ", N[box[[1 ;; 6]], 13]];
Print["box: scalar, first, second, higher, total R, return = ", N[box[[7 ;; 12]], 13]];
Print["box: A transmission phase drift bound and fractional amplitude loss = ", N[box[[13 ;; 14]], 13]];
Print["half-budget reflection threshold = ", N[returnLimit, 13]];
Print["common tolerance 4.4e-7, 4.6e-7 reflection bounds = ",
  N[Table[bounds[v, v, v][[11]], {v, {44/10^8, 46/10^8}}], 13]];
Print["thickness m and absolute box error nm = ", N[{
  a0 (1973269804/10^16)/energy, 10^9 t a0 (1973269804/10^16)/energy}, 13]];
Print["box inside reflection threshold = ", N[box[[11]], 40] < N[returnLimit, 40]];
