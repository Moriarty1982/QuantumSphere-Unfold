ClearAll["Global`*"];
Print["kernel version = ", $Version];

energy = y h density;
source = -D[energy,h];
pressure = density D[energy,density]-energy;
Print["dust source and pressure = ", {source,pressure}];
Print["fixed-radius energy-source residual = ",
  Simplify[D[energy,density]+h D[source,density]]];
Print["source linearization for compression = ",
  Simplify[D[source,density] (-n0 strain)]];
materialEnergy = ee[h,density];
Print["pressure-response identity residual = ",
  Simplify[D[density D[materialEnergy,density]-materialEnergy,h]-
    density D[materialEnergy,h,density]+D[materialEnergy,h]]];

radialU = Integrate[x j[x],{x,0,r}]/(y n0 r);
Print["radial divergence source residual = ",
  FullSimplify[y n0 D[r radialU,r]/r-j[r],r>0]];
lap[expr_] := Total[D[expr,{#,2}]& /@ {x,yc,z}];
lapTransverse[expr_] := D[expr,{x,2}]+D[expr,{yc,2}];
quad = z^2-(x^2+yc^2)/2;
Print["quadrupole Laplacian and transverse bi-Laplacian = ",
  {lap[quad],lapTransverse[lapTransverse[quad]]}];
driveOnQuad = (z0 omega0^2 (mass^2 quad-rm lap[quad])-
  alpha lap[mass^2 quad-rm lap[quad]]-
  2 gm^2 lapTransverse[lapTransverse[quad]]/3)/mass^2;
Print["quadrupole drive residual = ", Simplify[driveOnQuad-z0 omega0^2 quad]];
moments = Table[Integrate[s^k,{s,0,1}],{k,2,4}];
Print["sharp-disk illustrative moments and weighted residual = ",
  {moments,moments[[2]]-moments[[2]] moments[[3]]/moments[[1]]}];
