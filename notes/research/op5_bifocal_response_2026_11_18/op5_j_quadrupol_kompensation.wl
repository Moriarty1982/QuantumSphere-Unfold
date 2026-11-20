ClearAll["Global`*"];
Print["kernel version = ", $Version];

lapT[e_] := D[e,{x,2}]+D[e,{y,2}];
lap[e_] := lapT[e]+D[e,{z,2}];
sxy = (x^2+y^2)/rad^2;
seed = -amp mix rad^2 p[z] (sxy^3-kappa sxy^4)/36;
deltaH = lap[seed];
axis = {x->0,y->0};
Print["axis profile and transverse Laplacian = ",
  FullSimplify[{deltaH,lapT[deltaH]}/.axis]];
Print["axis tidal term per polarization = ",
  FullSimplify[-D[lapT[deltaH],{x,2}]/(2 mass^2)/.axis]];
Print["integrated transverse-only mean Hessian factor = ",
  FullSimplify[(Integrate[D[lapT[lapT[seed]],{x,2}]/.
    {x->rad Sqrt[s] Cos[t],y->rad Sqrt[s] Sin[t]},{t,0,2 Pi}]/(2 Pi))/
    (-32 amp mix p[z]/rad^4),s>=0 && rad>0]];
Print["seed moment compensation residual = ",
  Simplify[mm3-kappa mm4/.kappa->mm3/mm4,mm4>0]];

op[e_] := (zz omega0^2 e-alpha lap[e])-rm/mass^2 lap[zz omega0^2 e-alpha lap[e]]-
  2 gm^2/(3 mass^2) lapT[lapT[e]];
Print["static operator and Laplacian commutator = ",
  Expand[op[lap[f[x,y,z]]]-lap[op[f[x,y,z]]]]];
quadrupole = z^2-(x^2+y^2)/2;
hexadecapole = z^4-3 z^2 (x^2+y^2)+3 (x^2+y^2)^2/8;
Print["adjoint direct-source quadrupole and degree-four residual = ",
  Expand[{lap[op[quadrupole]],lap[op[hexadecapole]]}]];

(* Finite differentiability comparison only. The construction uses a smooth cutoff. *)
cut = (1-s)^10;
kExample = Integrate[cut s^3,{s,0,1}]/Integrate[cut s^4,{s,0,1}];
seedExample = cut (s^3-kExample s^4);
deltaRadial = D[s D[seedExample,s],s];
Print["finite smoothness example moment ratio and two radial moments = ",
  {kExample,Integrate[deltaRadial,{s,0,1}],Integrate[s deltaRadial,{s,0,1}]}];
