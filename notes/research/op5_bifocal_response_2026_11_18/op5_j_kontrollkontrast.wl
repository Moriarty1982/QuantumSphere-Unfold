Clear[z,r,a,l,s,m,m0,q,x,y,u];
plan=FullSimplify[Integrate[m Exp[-m (s-z)]/2,{z,0,s}]+Integrate[m Exp[-m (z-s)]/2,{z,s,l}],Assumptions->m>0&&0<s<l];
axial=Integrate[(1-u^2)^4,{u,-1,1}];
area=Integrate[2 Pi r (1-r^2/a^2)^4,{r,0,a},Assumptions->a>0];
trans=FullSimplify[area-(area/.a->2 a)/4,Assumptions->a>0];
atAxis=3 axial/4;
detune=FullSimplify[m^2/(q+m^2) (1+q/m0^2)-m^2/m0^2-(1-m^2/m0^2)m^2/(q+m^2),Assumptions->m>0&&m0>0&&q>=0];
beamLower=FullSimplify[((1-1/4)^4-1/4) axial];
boundary=Table[D[(1-u^2)^4,{u,j}]/.u->1,{j,0,3}];
{plan,axial,area,trans,atAxis,beamLower,detune,boundary}
