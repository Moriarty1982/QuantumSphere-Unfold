Clear[q,n,mu,r0,c,t,s,rr,tension,m,w,r1,r2];
radius=Sqrt[r0^2-2 q s[t]/(n mu)];
tension=c/radius^2-mu D[radius,{t,2}];
virial=n/2 (mu D[radius,t]^2+c/radius-tension radius);
assume=n>0&&mu>0&&q>0&&r0>0&&c>0&&r0^2>2 q s[t]/(n mu);
checks={
 FullSimplify[mu D[radius,{t,2}]-(c/radius^2-tension),Assumptions->assume],
 FullSimplify[virial+q D[s[t],{t,2}]/2,Assumptions->assume],
 FullSimplify[D[mu D[radius,t]^2/2+c/radius+tension radius,t]-radius D[tension,t],Assumptions->assume],
 FullSimplify[D[Cosh[m w rr/2],rr]>0,Assumptions->m>0&&rr>0&&w!=0&&Element[w,Reals]],
 FullSimplify[2 c/r2-2 c/r1>0,Assumptions->c>0&&0<r2<r1]
};
Print[checks];
