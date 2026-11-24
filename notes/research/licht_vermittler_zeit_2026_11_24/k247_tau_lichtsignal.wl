(* Erkundung 24.11.2026: Zeitrichtung tau ueber ein Lichtsignal; nicht blind. Wolfram Language, exakt. *)
s={PauliMatrix[1],PauliMatrix[2],PauliMatrix[3]};
L[eta_]:={{Cosh[eta],-Sinh[eta],0,0},{-Sinh[eta],Cosh[eta],0,0},{0,0,1,0},{0,0,0,1}};
LT=Simplify[L[I Pi]];
Sp=MatrixExp[-I Pi PauliMatrix[1]/2]//Simplify;
kvec[K_]:=Simplify[{Tr[K],Tr[K.s[[1]]],Tr[K.s[[2]]],Tr[K.s[[3]]]}/2];
Kof[k_]:=k[[1]] IdentityMatrix[2]+k[[2]] s[[1]]+k[[3]] s[[2]]+k[[4]] s[[3]];
k={1,nx,ny,nz};
r1=LT.k; r2=kvec[Sp.Kof[k].ConjugateTranspose[Sp]]; r3=kvec[Sp.Kof[k].Sp];
up={1,0};xp={1,1}/Sqrt[2];yp={1,I}/Sqrt[2];
B[a_,b_,c_]:=(Conjugate[a].b)(Conjugate[b].c)(Conjugate[c].a);
bM=Simplify[B[up,xp,yp]]; bTunit=Simplify[B[Sp.up,Sp.xp,Sp.yp]];
Print["Lambda(i pi) auf k: ",r1];
Print["unitaer S K S^dagger: ",r2];
Print["holomorph S K S: ",r3];
Print["B_M = ",bM," Arg/(pi/4) = ",Arg[bM]/(Pi/4)];
Print["B nach gemeinsamer Abbildung S: ",bTunit," gleich: ",Simplify[bTunit-bM]==0];
Print["umgekehrte Reihenfolge: ",Simplify[B[up,yp,xp]]," = Conjugate: ",Simplify[B[up,yp,xp]-Conjugate[bM]]==0];
