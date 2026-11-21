Print["Kernel: ", $Version];
dd={{daa,daj},{dja,djj}};
Print["directional cross-entry identity residual = ",
 Expand[{1,beta}.dd.{alpha,1}-daj-(alpha daa+beta djj+alpha beta dja)]];
portGain = 254/10^5; absoluteGoal=2/10^7;
Print["additive readout ceilings {both weak directions, calibrated A detector} = ",
 N[absoluteGoal {portGain^2,portGain},13]];
leak = 4/10^4; add = 1/10^7;
Print["reflection and transmission directional certificates {reflection rest, max readback for 1e-6, transmission rest} = ",
 N[{add+(2 leak+leak^2)/10^4,1/10^6-add-(2 leak+leak^2)/10^4,
    add+2 leak+leak^2},13]];
Print["singular-port kernel leaves readout invariant = ",
 Expand[{{1,0}}.({{d11,d12},{d21,d22}}+{{0,eta},{0,0}}).{{1},{0}}-
 {{1,0}}.{{d11,d12},{d21,d22}}.{{1},{0}}]];

hbarc = 1973269804/10^16; e0 = 360329/10^6; half = 2067833848/10^16;
m2=e0^2(1-(9999/10000)^2);
g[e_] := (Sqrt[e^2-m2]-e)/hbarc;
signal = 4(g[e0+half]-g[e0-half]);
rawBound=Sin[signal/16];
jBound=Sin[(signal/2-4/10^6)/4];
Print["4-m phase contrast and radius ceilings {equal raw, calibrated A} = ",
 N[{signal,rawBound,jBound},14]];
aa = {mAJ11,mAJ12,mAJ21,mAJ22}; swap={1,-1,-1,1};
Print["stationary reference cancellation residual = ", Expand[
 swap.(aa+{r1,r2,r1,r2})-swap.aa]];

moment[n_] := Integrate[
 ((b+rr Cos[t])^2-(rr Sin[t])^2) ((b+rr Cos[t])^2+(rr Sin[t])^2)^n,
 {t,0,2 Pi}]/(2 Pi);
pred={b^2,b^2(b^2+3 rr^2),b^2(b^4+8 b^2 rr^2+6 rr^4)};
Print["finite circular spot angular residuals = ", Expand[Table[moment[n],{n,0,2}]-pred]];
ff[s_] := a0+a1(s+3 mm2)+qq(s^2+8 s mm2+6 mm4);
Print["spot profile determinant and second difference residuals = ", Expand[{
 Det[{{s1,s1 ff[s1]},{s2,s2 ff[s2]}}]-s1 s2(ff[s2]-ff[s1]),
 ff[3 h]-2 ff[2 h]+ff[h]-2 qq h^2}]];

jRaw = 1/10^4;
aRaw = Sin[signal/8-ArcSin[jRaw]];
phaseReserve = signal/2-4 ArcSin[jRaw]-4/10^6;
Print["direct A radius with J=1e-4, reference group-delay allowance in s, equal mirror return loss dB = ",
 N[{aRaw,phaseReserve/(2 Pi 10^8),-10 Log[10,rawBound]},14]];
Print["length and frequency reference cancellation residual = ",
 Expand[swap.{l1+r1,l1+r2,l2+r1,l2+r2}]];
xs = {h,2 h,3 h};
contrast = {3,-3,1};
Print["three-spot contrast residuals = ", Expand[{contrast.xs,contrast.(# ff[#]& /@ xs)-6 qq h^3}]];
