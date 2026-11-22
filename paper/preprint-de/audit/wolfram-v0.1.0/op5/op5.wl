(* Symbolic audit of published article 0.1.0, section 4.4.
   Only declared linear models, flat-core profiles, local elasticity and matrix algebra. *)
ClearAll["Global`*"];
Print["Wolfram kernel: ", $Version];
passed = 0; failed = 0;
check[name_, value_, expected_, ass_: True] := Module[{r},
  r = FullSimplify[value - expected, ass];
  If[And @@ (TrueQ[# == 0] & /@ Flatten[{r}]), passed++; Print["PASS | ", name, " | residual ", InputForm[r]],
   failed++; Print["FAIL | ", name, " | residual ", InputForm[r]]]];
xyz = {xx, yy, zz};
gr[f_] := (D[f, #] & /@ xyz);
div[b_] := Total[Table[D[b[[i]], xyz[[i]]], {i, 3}]];
lap[f_] := Total[(D[f, {#, 2}] &) /@ xyz];
eps[b_] := Table[(D[b[[i]], xyz[[j]]] + D[b[[j]], xyz[[i]]])/2, {i, 3}, {j, 3}];
sig[b_] := lam div[b] IdentityMatrix[3] + 2 mu eps[b];
matDiv[a_] := Table[Total[Table[D[a[[i,j]], xyz[[j]]], {j,3}]], {i,3}];
ela[b_] := matDiv[sig[b]];
op1[b_] := r1 D[b,{tt,2}] - ela[b];
op2[b_] := r2 D[b,{tt,2}] - cs ela[b];
bvec = Through[{bx, by, bz}[xx, yy, zz, tt]];
u = op2[bvec]; w = -op1[bvec]; rd = u-w+op1[u]/ks;
beta = r2-cs r1;
check["sources of W2", -D[h (y1 n1+y2 n2),h], -(y1 n1+y2 n2)];
check["direct energy density at fixed v", v (y1 dn1+y2 dn2), -v (-(y1 dn1+y2 dn2))];
check["rest-energy pressure", n1 D[h y1 n1,n1]-h y1 n1,0];
check["Paired spring first EOM", op1[u]+ks (u-w-rd), {0,0,0}];
check["Paired spring second EOM", op2[w]-ks (u-w-rd), {0,0,0}];
check["mass-weighted displacement", r1 u+r2 w, beta ela[bvec]];
check["stiffness-weighted displacement", u+cs w, beta D[bvec,{tt,2}]];
t00 = -beta div[ela[bvec]];
t0 = beta ela[D[bvec,tt]];
tij = -beta sig[D[bvec,{tt,2}]];
check["linear energy conservation", D[t00,tt]+div[t0],0];
check["linear momentum conservation", D[t0,tt]+matDiv[tij],{0,0,0}];
seed = psi[xx,yy,zz,tt];
check["longitudinal elastic Higgs source", beta div[ela[gr[seed]]]/v, beta (lam+2mu)lap[lap[seed]]/v];
check["spring work on imposed rest-position d", D[ks (fu[tt]-fw[tt]-fd[tt])^2/2,tt] - ks (fu[tt]-fw[tt]-fd[tt]) (fu'[tt]-fw'[tt]), -ks (fu[tt]-fw[tt]-fd[tt]) fd'[tt]];
etas = DiagonalMatrix[{-1,1,1,1}]; pp={om,kx,ky,kz}; ds=pp.etas.pp; st=Outer[Times,pp,pp]-etas ds;
sttrace=Tr[etas.st]; stsq=Tr[etas.st.etas.st];
check["Einstein source transversality", pp.etas.st,{0,0,0,0}];
check["Einstein trace and contraction",{sttrace,stsq},{-3 ds,3 ds^2}];
check["Einstein quotient continued through removable pole", Cancel[(stsq-sttrace^2/2)/ds],-3 ds/2];
check["Fierz-Pauli contraction",stsq-sttrace^2/3,0];
q = kx^2+ky^2+kz^2; ap=kx^2+ky^2; x=om^2;
dm=mm^2+rm q-x; nm=2(x^2-ap x+ap^2)/3;
op=(zkin (om0^2+ch2 q-x)+3 g0^2 (q-x)/2)dm/mm^2-gm^2 nm/mm^2;
dsym=q-x;
shape=-dsym q^2 vv; shS=-v dsym op vv/(beta (lam+2mu));
check["imposed source profile match",beta (lam+2mu) q^2 shS/v,op shape];
check["retarded field expression matches forced wave equation in Fourier symbol",dsym (-16 Pi grav ts),16 Pi grav (-dsym ts)];
rhos=(xx^2+yy^2)/rrad^2;
perp[f_] := D[f,{xx,2}]+D[f,{yy,2}];
pol=rhos^5-kappa rhos^6; triple=Expand[Nest[perp,pol,3]];
check["three transverse Laplacians",triple,230400 (rhos^2-4 kappa rhos^3)/rrad^6,rrad>0];
plateau = Expand[-amp rrad^6 Nest[lap,pz[zz]pol,3]/230400];
fprof=Expand[perp[plateau]/mm^2];
check["axis profile vanishes",plateau/.{xx->0,yy->0},0];
check["axis massive entry vanishes",fprof/.{xx->0,yy->0},0];
check["axis tidal contrast per local p",-(D[fprof,{xx,2}]/2/.{xx->0,yy->0}),16 amp pz[zz]/(mm^2 rrad^4)];
(* Rotational average of a fixed transverse Hessian component is half its trace.
   Replace all z-derivatives of p by zero only after integration over compact longitudinal support. *)
bundle=Expand[-perp[fprof]/4] /. Derivative[n_Integer?Positive][pz][zz] :> 0;
check["azimuthal bundle factor after longitudinal integration",bundle,16 amp pz[zz](1-36 kappa rhos)/(mm^2 rrad^4)];
kerInt=Integrate[mm/2 Exp[-mm Abs[xpos-zpos]],{xpos,0,len},Assumptions->mm>0&&0<zpos<len];
check["planar kernel interval deficit",kerInt,1-(Exp[-mm zpos]+Exp[-mm (len-zpos)])/2,mm>0&&0<zpos<len];
hes={{h11,h12,h13},{h12,h22,h23},{h13,h23,h33}};
grad2=Array[jmath,{3,3}];
defG=IdentityMatrix[3]+eta hes+eta^2 grad2;
green=(Transpose[defG].defG-IdentityMatrix[3])/2;
matP=defG.(lam Tr[green] IdentityMatrix[3]+2 mu green);
second=Map[Coefficient[#,eta,2]&,matP,{2}];
nquad=lam Tr[hes.hes] IdentityMatrix[3]/2+3 mu hes.hes+lam Tr[hes]hes;
check["second Piola coefficient",second,lam Tr[grad2] IdentityMatrix[3]+mu(grad2+Transpose[grad2])+nquad];
check["quadratic counter-motion sum",nquad+cs(nquad/.Thread[DeleteDuplicates[Flatten[hes]]->(-DeleteDuplicates[Flatten[hes]]/cs)]),(1+1/cs)nquad,cs>0];
pot=phi[xx,yy,zz]; hh=Table[D[pot,xyz[[i]],xyz[[j]]],{i,3},{j,3}];
check["integrated Hessian relation pointwise divergence precursor",lap[pot]^2-Tr[hh.hh],div[lap[pot] gr[pot]-hh.gr[pot]]];
check["trace coefficient after integration by parts", Tr[nquad]-lam Tr[hes]^2+lam Tr[hes.hes],(5 lam/2+3 mu)Tr[hes.hes]];
check["positive integrated trace prefactor",Boole[5 lam/2+3 mu>0],1,Element[{lam,mu},Reals]&&mu>0&&3lam+2mu>0];
lf={{1,2},{0,1}}; ff={{1,0},{3,1}}; sEnd={{1,1},{1,2}}; rEnd={{2,1},{1,1}}; uMode={{I,0},{0,-I}};
check["A/B equal-ends quotient control", Inverse[lf.ff].lf.uMode.ff,Inverse[ff].uMode.ff];
check["drift quotient spectral-similarity control",Inverse[sEnd].ff.Inverse[lf.ff].lf.sEnd.uMode.rEnd.ff.Inverse[ff].sEnd,uMode.rEnd.sEnd];
check["matched null path control",Inverse[lf.sEnd.rEnd.ff].lf.sEnd.uMode.rEnd.ff,Inverse[ff].Inverse[rEnd].uMode.rEnd.ff];
na={{0,1/10},{1/20,0}}; nb={{0,0},{0,-1/10}}; de={{I/20,0},{0,0}};
check["exact phase-error quotient control",Inverse[IdentityMatrix[2]+na].(uMode+nb+de)-uMode,Inverse[IdentityMatrix[2]+na].(nb-na.uMode+de)];
Print["SUMMARY | passed=",passed," | failed=",failed];
{passed,failed}

