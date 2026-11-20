Clear[r,a,u,z,t,x,y,m,k,w,rho0,s,chi,f,q0,qMiddle,qOutside,g];
g[r_,a_]:=(1-r^2/a^2)^4;
q0=Cancel[Integrate[u (g[u,a]-g[u,2 a]/4),{u,0,r}]/r];
qMiddle=(Integrate[u g[u,a],{u,0,a}]-Integrate[u g[u,2 a]/4,{u,0,r}])/r;
qOutside=FullSimplify[Integrate[u g[u,a],{u,0,a}]-Integrate[u g[u,2 a]/4,{u,0,2 a}],Assumptions->a>0];
coords={t,x,y,z};
c=chi[x,y,z];
f=D[c,{x,2}]+D[c,{y,2}];
j=-D[s[t],t] {D[c,x],D[c,y]};
stress={{rho0[x,y,z]+s[t] f,j[[1]],j[[2]],0},{j[[1]],D[s[t],{t,2}] c,0,0},{j[[2]],0,D[s[t],{t,2}] c,0},{0,0,0,0}};
eta=DiagonalMatrix[{-1,1,1,1}];
nullCovector={-1,0,0,1};
checks={
 qOutside,
 FullSimplify[{Limit[q0,r->0],(q0-qMiddle)/.r->a,qMiddle/.r->2 a},Assumptions->a>0],
 FullSimplify[D[r q0,r]/r-(g[r,a]-g[r,2 a]/4)],
 FullSimplify[D[r qMiddle,r]/r+g[r,2 a]/4],
 FullSimplify[Table[Sum[D[stress[[mu,nu]],coords[[mu]]],{mu,4}],{nu,4}]],
 FullSimplify[nullCovector.stress.nullCovector-stress[[1,1]]],
 FullSimplify[Tr[eta.stress]+stress[[1,1]]-2 D[s[t],{t,2}] c],
 FullSimplify[(m^2+k)/(m^2+k-w^2)-1-w^2/(m^2+k-w^2),Assumptions->m>0&&k>=0&&-m<w<m]
};
Print[checks];
