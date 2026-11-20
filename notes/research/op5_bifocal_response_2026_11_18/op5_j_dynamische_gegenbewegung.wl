ClearAll["Global`*"];
Print["kernel version = ", $Version];

(* Formal derivative symbols: k_i for partial_i and dt for partial_t. *)
k = {kx,ky,kz};
base = {b1,b2,b3};
id = IdentityMatrix[3];
laplace = k.k;
elastic = mu laplace id+(lame+mu) Outer[Times,k,k];
a1 = rho1 dt^2 id-elastic;
a2 = rho2 dt^2 id-c elastic;
u = a2.base;
w = -a1.base;
totalMassDisplacement = rho1 u+rho2 w;
inertiaMismatch = rho2-c rho1;
stress[x_] := mu (Outer[Times,k,x]+Outer[Times,x,k])+lame (k.x) id;
spatialStress = -stress[u+c w];
massDensity = -k.totalMassDisplacement;
momentum = dt totalMassDisplacement;
Print["opposed internal force residual = ", Expand[a1.u+a2.w]];
Print["mass displacement residual = ",
  Expand[totalMassDisplacement-inertiaMismatch elastic.base]];
Print["stress displacement residual = ", Expand[u+c w-inertiaMismatch dt^2 base]];
Print["linear conservation residual = ",
  Expand[Join[{dt massDensity+k.momentum}, dt momentum+spatialStress.k]]];
Print["Higgs source longitudinal residual = ",
  Expand[(k.totalMassDisplacement /. Thread[base->k potential])-
    inertiaMismatch (lame+2 mu) laplace^2 potential]];
Print["mechanical source wave-factor residual = ",
  Expand[Join[{massDensity},momentum,Flatten[spatialStress]] /.
    Thread[base->-(dt^2-laplace) base]]+
  Expand[(dt^2-laplace) Join[{massDensity},momentum,Flatten[spatialStress]]]];

radialS = (x^2+y^2)/rad^2;
lapT[f_] := D[f,{x,2}]+D[f,{y,2}];
plateauCore = Nest[lapT,radialS^5-kappa radialS^6,3];
Print["radial six-derivative profile = ",
  Factor[plateauCore/.{y->0,x->rad Sqrt[s]}]];
Print["axis tidal coefficient per longitudinal integral = ",
  Simplify[-D[lapT[-amp mix rad^6 plateauCore/230400],{x,2}]/(2 mass^2)/.{x->0,y->0}]];
azimuthMean = Integrate[D[lapT[plateauCore],{x,2}]/.
  {x->rad Sqrt[s] Cos[t],y->rad Sqrt[s] Sin[t]},{t,0,2 Pi}]/(2 Pi);
Print["averaged tidal ratio on the compact core = ",
  Simplify[azimuthMean/(32 230400/rad^10),s>=0 && rad>0]];
