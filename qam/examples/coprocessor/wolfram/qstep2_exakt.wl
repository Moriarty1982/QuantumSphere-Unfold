w=(1+I)/Sqrt[2];id=IdentityMatrix[2];
g1["x"]={{0,1},{1,0}};g1["z"]=DiagonalMatrix[{1,-1}];g1["s"]=DiagonalMatrix[{1,I}];g1["sdg"]=DiagonalMatrix[{1,-I}];
g1["t"]=DiagonalMatrix[{1,w}];g1["tdg"]=DiagonalMatrix[{1,Conjugate[w]}];g1["h"]={{1,1},{1,-1}}/Sqrt[2];g1["nop"]=id;
(* Index i = b0 + 2 b1, Qubit 0 = niederwertiges Bit: KroneckerProduct[U1,U0] *)
op[{"cx",t_}]:=Module[{m=ConstantArray[0,{4,4}]},Do[With[{c=BitAnd[i,If[t==1,1,2]]!=0},m[[If[c,BitXor[i,If[t==1,2,1]],i]+1,i+1]]=1],{i,0,3}];m];
op[{n_,0}]:=KroneckerProduct[id,g1[n]];op[{n_,1}]:=KroneckerProduct[g1[n],id];
data={{1,{{"h",0},{"cx",1}},1,{1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0}},{2,{{"h",0},{"t",0},{"h",0}},2,{1,1,0,0,1,-1,0,0,0,0,0,0,0,0,0,0}},{5,{{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0},{"h",0},{"t",0}},12,{-27,15,19,21,-27,-27,21,-21,0,0,0,0,0,0,0,0}},{9,{{"x",1},{"x",1},{"h",1},{"tdg",0},{"x",1},{"nop",1},{"tdg",0},{"h",1},{"s",0}},0,{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}},{10,{{"nop",0},{"nop",0},{"tdg",0},{"tdg",0},{"cx",0},{"h",1},{"cx",0},{"t",0},{"s",1},{"sdg",0},{"tdg",0},{"z",1},{"x",1},{"cx",1},{"cx",0},{"sdg",1},{"h",1},{"nop",1},{"s",1},{"tdg",0},{"t",1}},2,{0,0,1,0,0,-1,0,0,0,1,0,0,-1,0,0,0}},{11,{{"h",0},{"z",1},{"t",1},{"nop",1},{"nop",1},{"tdg",0}},1,{1,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0}}};
Do[{n,gs,k,c}=d;psi=Fold[Expand[op[#2].#1]&,{1,0,0,0},gs];
hdl=Table[Sum[c[[4 i+j+1]] w^j,{j,0,3}]/Sqrt[2]^k,{i,0,3}];
Print["Fall ",n,": Gatter ",Length[gs],", k ",k,", exakte Differenz ",Expand[ComplexExpand[psi-hdl]]],{d,data}]
