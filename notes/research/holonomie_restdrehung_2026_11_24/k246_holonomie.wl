(* k246, unabhaengige Kontrolle in Wolfram Language (Modell B und C) *)
c[i_]:=Cos[d+2Pi i/3]; r2[i_]:=(1+a c[i])^2;
hol=Simplify[Integrate[TrigReduce[-b Sum[r2[i]c[i],{i,0,2}]/Sum[r2[i],{i,0,2}]],{d,0,2Pi}],a>0];
Print["Modell B Holonomie: ",hol];
k=Simplify[hol/(-2Pi b)]; Print["k(a)=",k,"  Max: ",Maximize[{k,a>0},a]];
L=2Pi; l3=L-l1-l2; m={l1^2,l2^2,l3^2}; g={l1/2,l1+l2/2,l1+l2+l3/2}; w=m/Total[m];
F=Simplify[Sum[D[w[[i]],l1]D[g[[i]],l2]-D[w[[i]],l2]D[g[[i]],l1],{i,3}]];
Print["Modell C F(2pi/3,2pi/3)=",Simplify[F/.{l1->L/3,l2->L/3}]];
q=4+3Sqrt[2]; Print["F Koide=",N[F/.{l1->L q/(q+2),l2->L/(q+2)},12]];
tot=Integrate[F,{l1,0,L},{l2,0,L-l1}]; Print["Fluss Simplex=",FullSimplify[tot]," = ",N[tot,12]];
