ClearAll["Global`*"];
Print["kernel version = ", $Version];

lap[expr_] := D[expr,{x,2}]+D[expr,{y,2}];
radiusSquared = (x^2+y^2)/rad^2;
shape = radiusSquared^2-kappa radiusSquared^3;
axis = {x->0,y->0};
Print["axis profile, Laplacian and transverse Hessians = ",
  Simplify[{shape,lap[shape],D[lap[shape],{x,2}],D[lap[shape],{y,2}],
    D[lap[shape],x,y]}/.axis]];
Print["axis integrated tidal coefficient per unit longitudinal integral = ",
  Simplify[-D[lap[-amp scale shape/mass^2],{x,2}]/2/.axis]];
Print["azimuthal mean Hessian = ",
  Simplify[Integrate[D[lap[shape],{x,2}]/.{x->rad Sqrt[s] Cos[theta],
    y->rad Sqrt[s] Sin[theta]},{theta,0,2 Pi}]/(2 Pi), s>=0 && rad>0]];
Print["transverse integral moment residual = ",
  Simplify[moment2-kappa moment3/.kappa->moment2/moment3,moment3>0]];

(* Plateau-only illustrative cutoff. The construction in the note uses a smooth cutoff. *)
Print["sharp-disk moment ratio for cutoff s<=1 = ",
  Integrate[s^2,{s,0,1}]/Integrate[s^3,{s,0,1}]];
leftTail = Integrate[mass Exp[-mass (xp-z)]/2,{z,-Infinity,0},
  Assumptions->mass>0 && 0<xp<len];
rightTail = Integrate[mass Exp[-mass (z-xp)]/2,{z,len,Infinity},
  Assumptions->mass>0 && 0<xp<len];
inside = Integrate[mass Exp[-mass (xp-z)]/2,{z,0,xp},
  Assumptions->mass>0 && 0<xp<len]+
  Integrate[mass Exp[-mass (z-xp)]/2,{z,xp,len},
  Assumptions->mass>0 && 0<xp<len];
Print["planar column and exterior-tail residual = ",
  FullSimplify[inside+leftTail+rightTail-1,mass>0 && 0<xp<len]];
