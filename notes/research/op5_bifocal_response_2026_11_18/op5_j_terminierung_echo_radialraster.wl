Print["Kernel: ", $Version];
rr[g_] := rA + t12 t21 g/(1-rJ g);
odd = Together[(rr[gam]-rr[-gam])/(2 gam)];
p[g_] := (rr[g]-rr[0])/g;
Print["switched J-endpoint and exact two-load product residuals = ", Together[{
 odd - t12 t21/(1-(rJ gam)^2),
 2 p[gam] p[-gam]/(p[gam]+p[-gam])-t12 t21}]];
t0=3/1000; loadAbs=1/2; returnMax=1/10; reflErr=5/10^8;
bound=t0^2 (returnMax loadAbs)^2/(1-(returnMax loadAbs)^2)+reflErr/loadAbs;
Print["reciprocal product example {bias and noise, one percent complex root allowance} = ",
 N[{bound,t0^2 (1-(99/100)^2)},14]];

extrap = Together[(1/(1-aa uu)-aa/(1-uu))/(1-aa)];
Print["attenuated unmarked echo extrapolation residual = ",
 Together[extrap-1+aa uu^2/((1-uu)(1-aa uu))]];
aa0=1/10; uu0=1/1000; epsilon=1/10^7;
da=1/10000;
echoBound=aa0 uu0^2/((1-uu0)(1-aa0 uu0)) + epsilon (1+aa0)/(1-aa0) +
 uu0 da/((1-aa0)(1-aa0 uu0)(1-(aa0+da) uu0));
Print["attenuated example relative echo bound and eight-read phase bound = ",
 N[{echoBound,8 ArcSin[echoBound]},14]];
fk[x_] := x (1-Log[x]);
ring[a_,b_] := (b^2-a^2)/4-a b Log[b/a]/2;
Print["Lipschitz ring kernel derivative and axis limit residuals = ",
 {FullSimplify[D[ring[a,b],b]-((b-a)-a Log[b/a])/2,0<a<b],
  Integrate[(b-u)/2,{u,0,b}]-b^2/4}];
r0[a_,b_] := If[a==0,b^2/4,ring[a,b]];
grid[n_,p_] := N[Table[(i/n)^p,{i,0,n}],40];
cost[g_] := Total[MapThread[r0,{Most[g],Rest[g]}]];
Print["8-ring Lipschitz costs {uniform area, graded} = ",
 N[{cost[grid[8,1]],cost[grid[8,3/2]]},14]];

Print["crossing of normalized ring target 0.001 {uniform N=22,23; graded N=16,17} = ",
 N[{cost[grid[22,1]],cost[grid[23,1]],cost[grid[16,3/2]],cost[grid[17,3/2]]},14]];
