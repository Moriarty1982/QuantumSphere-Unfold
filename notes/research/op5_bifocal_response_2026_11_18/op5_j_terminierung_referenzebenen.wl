Print["Kernel: ", $Version];
uJ = 317/10^5;
hm = 3512/10^9;
direct = 4573/10^12;
second = 2624/10^12;
tail = 3140/10^11;
mixed = direct + second + tail;
scalarFit = 2001/10^11;
budget = 5/10^7;
ref = 4/10^7;
thru = 99/100;
base = thru (1-Exp[-(budget-ref)/4])-scalarFit;
bias[r_] := r uJ/(1-hm);
logBound[r_] := ref -4 Log[1-(scalarFit+bias[r])/thru];
Print["cross reflection, offset, full log error = ", N[{mixed,bias[mixed],logBound[mixed]}, 14]];
Print["coarse full reflection used for cross entry: offset and full log error = ", N[{bias[hm],logBound[hm]}, 14]];
Print["max cross-entry bound with unit termination = ", N[base (1-hm)/uJ, 14]];
Print["illustrative matched-termination limits with coarse reflection = ",N[base/(hm uJ+base hm),14]];
Print["formal J Schur correction residual = ", Together[
 (ra xa+raJ gamma (uj+rja xa)/(1-gamma rjj)) -
 raJ gamma uj/(1-gamma rjj)-(ra+raJ gamma rja/(1-gamma rjj)) xa]];

hbarc = 1973269804/10^16; e0 = 360329/10^6; half100 = 2067833848/10^16;
m2 = e0^2 (1-(9999/10000)^2);
ka[e_] := e/hbarc;
kj[e_] := Sqrt[e^2-m2]/hbarc;
g[e_] := kj[e]-ka[e];
band = {e0-half100,e0+half100};
diff[f_] := (Reverse[f /@ band] - f /@ band)[[1]];
avg[f_] := Mean[f /@ band];
d = 4; aPhase = 2/10^6; rho0 = 1/10^4;
s = d Abs[diff[g]]; delta = 2 ArcSin[rho0]+aPhase;
margin = (s-4 delta)/2;
geo = margin/Abs[{diff[g],avg[g],diff[kj],avg[kj]}];
rhoMax = Sin[(s/4-aPhase)/2];
alpha = Log[1/((1/10^5) (1+1/rhoMax))]/d;
Print["four-m phase, extra contrast allowance, one-at-a-time length errors (m) = ", N[{s,margin,geo},14]];
Print["total relative additive radius and example damping ceiling per m = ", N[{rhoMax,alpha},14]];
Print["mean/difference geometry identity residual = ", Expand[
 kjp (cp+lp)-kap cp - (kjm (cm+lm)-kam cm) -
 ((cp+cm)(kjp-kap-kjm+kam)+(cp-cm)(kjp-kap+kjm-kam)+(lp+lm)(kjp-kjm)+(lp-lm)(kjp+kjm))/2]];

bb = 13/360; cc = -1/360;
shift[c_] := bb ric + 4 cc (ric/2+c);
coeffRic = Coefficient[(shift[weyl]+shift[-weyl])/2,ric];
coeffWeyl = Coefficient[(shift[weyl]-shift[-weyl])/2,weyl];
Print["electron curvature coefficients {Ricci mean, Weyl half difference, ratio} = ",
 {coeffRic,coeffWeyl,coeffWeyl/coeffRic}];
Print["axial recovery and local cancellation residuals = ",
 Expand[{(shift[0] /. ric -> 2 tidal) - (11/180) tidal, shift[weyl] + (-coeffRic ric - coeffWeyl weyl)}]];
