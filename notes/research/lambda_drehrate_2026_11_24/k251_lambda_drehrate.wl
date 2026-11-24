(* k251: Kann Lambda an die Drehrate der Scheibe gekoppelt werden? Erkundung, nicht blind, 24.11.2026.
   Wolfram Language, exakt wo symbolisch. Lief in drei Teilen auf dem MCP-Kernel (zustandslos); Ausgaben in k251_out.txt.
   Konvention: Signatur (+,-,-,-), R_mn = d_l G^l_mn - d_n G^l_ml + G G - G G, Gleichung G_ab + lam g_ab = k T_ab;
   physikalisches Lambda = -lam (kalibriert an de Sitter in Teil 2). *)

(* ---------- Teil 1: Goedel ---------- *)
x0={t,x,y,z};
g={{a^2,0,0,a^2 Exp[x]},{0,-a^2,0,0},{0,0,-a^2,0},{a^2 Exp[x],0,0,a^2 Exp[2x]/2}};
gi=Simplify[Inverse[g]];
Gam=Table[Simplify[1/2 Sum[gi[[l,s]](D[g[[s,m]],x0[[n]]]+D[g[[s,n]],x0[[m]]]-D[g[[m,n]],x0[[s]]]),{s,4}]],{l,4},{m,4},{n,4}];
Ric=Table[Simplify[Sum[D[Gam[[l,m,n]],x0[[l]]],{l,4}]-Sum[D[Gam[[l,m,l]],x0[[n]]],{l,4}]+Sum[Gam[[l,l,s]]Gam[[s,m,n]]-Gam[[l,n,s]]Gam[[s,m,l]],{l,4},{s,4}]],{m,4},{n,4}];
R=Simplify[Sum[gi[[m,n]]Ric[[m,n]],{m,4},{n,4}]];
Ein=Simplify[Ric-R/2 g];
u={1/a,0,0,0}; ul=g.u;
sol=Solve[Thread[Flatten[Ein+lam g-k rho Outer[Times,ul,ul]]==0],{lam,rho}];
Print["Goedel: Ricci-Skalar R = ",R];
Print["Goedel: Loesung ",Simplify[sol]];
du=Table[D[ul[[n]],x0[[m]]]-Sum[Gam[[l,m,n]]ul[[l]],{l,4}],{m,4},{n,4}];
w=Simplify[(du-Transpose[du])/2];
w2=Simplify[1/2 Sum[w[[a1,b1]]w[[c1,d1]]gi[[a1,c1]]gi[[b1,d1]],{a1,4},{b1,4},{c1,4},{d1,4}]];
Print["Goedel: omega^2 = ",w2];
Print["Goedel: Lambda/omega^2 = ",Simplify[(lam/.sol[[1]])/w2]];
Print["Goedel: 8piG rho/omega^2 = ",Simplify[(k rho/.sol[[1]])/w2]];

(* ---------- Teil 2: Kalibrierung, euklidische Periode, Verduennung, Spintessence, Zahlen ---------- *)
g=DiagonalMatrix[{1,-Exp[2 H t],-Exp[2 H t],-Exp[2 H t]}]; gi=Inverse[g];
Gam=Table[Simplify[1/2 Sum[gi[[l,s]](D[g[[s,m]],x0[[n]]]+D[g[[s,n]],x0[[m]]]-D[g[[m,n]],x0[[s]]]),{s,4}]],{l,4},{m,4},{n,4}];
Ric=Table[Simplify[Sum[D[Gam[[l,m,n]],x0[[l]]],{l,4}]-Sum[D[Gam[[l,m,l]],x0[[n]]],{l,4}]+Sum[Gam[[l,l,s]]Gam[[s,m,n]]-Gam[[l,n,s]]Gam[[s,m,l]],{l,4},{s,4}]],{m,4},{n,4}];
R=Simplify[Sum[gi[[m,n]]Ric[[m,n]],{m,4},{n,4}]]; Ein=Simplify[Ric-R/2 g];
Print["deSitter (beschleunigt, physikalisch Lambda>0): lam = ",Solve[Thread[Flatten[Ein+lam g]==0],lam], "  => physikalisches Lambda = -lam = 3H^2"];
f[r_]:=1-H^2 r^2; kappa=Simplify[Abs[f'[1/H]]/2,H>0];
Print["Oberflaechengravitation kappa = ",kappa,"  Periode von tE = 2Pi/kappa = ",2Pi/kappa];
Print["AdS f(r)=1+r^2/L^2 Nullstellen fuer r>0: ",Reduce[1+r^2/L^2==0&&r>0&&L>0,r,Reals]];
Print["Raychaudhuri-Term 2 omega^2 mit omega ~ a^-2 skaliert wie a^",Exponent[2 (c/a^2)^2,a]," (Lambda: a^0, Strahlung: a^-4)"];
rho=1/2 fd^2+1/2 f2^2 Om^2+V; p=1/2 fd^2+1/2 f2^2 Om^2-V;
Print["w = ",Simplify[p/rho],";  w=-1 genau wenn ",Reduce[(p+rho==0)&&f2>0&&Om>=0&&fd>=0,{Om,fd}]];
Print["Kreisbahn V=m^2 f^2/2: Om=m, fd=0 -> w = ",Simplify[p/rho/.{V->m^2 f2^2/2,Om->m,fd->0}]];
Print["Ladung Q=f^2 Om a^3 erhalten -> Rotationsenergie f^2 Om^2/2 = Q Om/(2 a^3) skaliert wie a^-3 bei festem Om"];
lamObs=1.1056*10^-52; cc=2.99792458*10^8; H0=67.4*1000/(3.0857*10^22);
OmNeed=Sqrt[lamObs cc^2/3];
Print["Omega aus Lambda=3 Omega^2/c^2: ",ScientificForm[OmNeed]," 1/s;  Omega/H0 = ",OmNeed/H0];
Print["Omega fuer Lambda = Omega^2/c^2: ",ScientificForm[Sqrt[lamObs cc^2]]," 1/s; /H0 = ",Sqrt[lamObs cc^2]/H0];
Print["CMB-Schranke (omega/H)_0 < 4.7e-11 -> Lambda_rot/Lambda_obs < ",ScientificForm[2*(4.7*10^-11 H0)^2/(lamObs cc^2)]];
Print["Planck-Frequenz/Omega: ",ScientificForm[1/(5.391*10^-44)/OmNeed],"  ln = ",Log[1/(5.391*10^-44)/OmNeed]];
b2=0.3018466; Print["3(1-beta^2) = ",3(1-b2),"  2Pi/3 = ",N[2Pi/3],"  1-2Pi/9 = ",N[1-2Pi/9],"  Abstand zu beta^2 = ",N[1-2Pi/9]-b2];

(* ---------- Teil 3: Kombination Umlaufsinn s, Drehrate Om, Eigenfrequenz w0, Stringlaenge l ---------- *)
Lg=m/2 (rd^2+r^2 (s Om)^2)-m w0^2 r^2/2;
Print["mitrotierend: rdd = ",Simplify[(D[Lg,r]/m)/.s^2->1],"  (s^2=1: Umlaufsinn faellt heraus)"];
fd2[r_]:=1-Lam r^2/3; Print["dS radial (c=1): rdd = ",Simplify[-1/2 fd2'[r]],"  -> Vergleich: Lam/3 <-> Om^2 - w0^2"];
Print["Lam>0 genau wenn ",Reduce[Om^2-w0^2>0&&Om>0&&w0>0,Om]];
LamExpr=3 (Om^2-w0^2)/c^2/.{Om->rr w0}/.w0->Pi c/l;
Print["Lam = ",Simplify[LamExpr],"  -> Dimension nur ueber l"];
RH=cc/H0; lneed=Sqrt[3 Pi^2/lamObs];
Print["l fuer rr^2-1=1: ",ScientificForm[lneed]," m = ",lneed/RH," Hubble-Radien"];
lP=1.616255*10^-35; Print["l = Planck-Laenge: rr^2-1 = ",ScientificForm[lamObs lP^2/(3 Pi^2)]];
Print["Om^2-w0^2 = ",Expand[(w0+d)^2-w0^2],"  Schwebung (Om-w0)^2 = d^2 >= 0 immer, Vorzeichen nicht waehlbar"];
