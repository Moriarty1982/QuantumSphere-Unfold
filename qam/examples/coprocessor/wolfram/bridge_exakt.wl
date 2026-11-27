(* Erzeugt von bridge_check.py: exakte Gegenprobe der Bruecke. Je Fall die Gatterfolge (aus OpenQASM)
   und der exakte HDL-Zustand; Wolfram rechnet den Zustand mit Kronecker-Matrizen nach. *)
w=(1+I)/Sqrt[2];id=IdentityMatrix[2];
g1["x"]={{0,1},{1,0}};g1["z"]=DiagonalMatrix[{1,-1}];g1["s"]=DiagonalMatrix[{1,I}];g1["sdg"]=DiagonalMatrix[{1,-I}];
g1["t"]=DiagonalMatrix[{1,w}];g1["tdg"]=DiagonalMatrix[{1,Conjugate[w]}];g1["h"]={{1,1},{1,-1}}/Sqrt[2];g1["nop"]=id;
op[{"cx",t_}]:=Module[{m=ConstantArray[0,{4,4}]},Do[With[{c=BitAnd[i,If[t==1,1,2]]!=0},m[[If[c,BitXor[i,If[t==1,2,1]],i]+1,i+1]]=1],{i,0,3}];m];
op[{n_,0}]:=KroneckerProduct[id,g1[n]];op[{n_,1}]:=KroneckerProduct[g1[n],id];
data={
  {0,{{"z",1},{"nop",0},{"cx",0},{"t",0},{"cx",0},{"nop",0},{"tdg",1},{"x",0},{"x",1},{"nop",0},{"s",0}},With[{w = (1 + I)/Sqrt[2]}, {(0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 1 w^2 + 0 w^3)/Sqrt[2]^0}]},
  {1,{{"tdg",0},{"s",0},{"cx",0},{"sdg",1},{"z",0},{"sdg",0},{"x",0},{"t",0},{"cx",0},{"nop",0},{"h",1},{"t",1},{"h",1},{"sdg",0},{"z",0},{"x",1},{"cx",1},{"t",1},{"sdg",0}},With[{w = (1 + I)/Sqrt[2]}, {(0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^2, (0 + 1 w + 1 w^2 + 0 w^3)/Sqrt[2]^2, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^2, (0 + 0 w + 1 w^2 + -1 w^3)/Sqrt[2]^2}]},
  {2,{{"cx",1},{"z",1},{"z",1},{"tdg",0}},With[{w = (1 + I)/Sqrt[2]}, {(1 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0}]},
  {3,{{"x",1},{"t",1},{"h",1},{"x",0},{"sdg",1},{"x",0},{"sdg",1},{"sdg",1},{"t",0},{"h",1},{"z",0},{"h",0},{"s",1},{"z",0},{"tdg",1},{"h",0},{"z",1},{"tdg",1},{"z",1},{"cx",1},{"tdg",1},{"tdg",0}},With[{w = (1 + I)/Sqrt[2]}, {(0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^2, (1 + 0 w + 1 w^2 + 0 w^3)/Sqrt[2]^2, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^2, (0 + -1 w + 0 w^2 + -1 w^3)/Sqrt[2]^2}]},
  {4,{{"x",0},{"z",0},{"s",0},{"h",0},{"sdg",1}},With[{w = (1 + I)/Sqrt[2]}, {(0 + 0 w + -1 w^2 + 0 w^3)/Sqrt[2]^1, (0 + 0 w + 1 w^2 + 0 w^3)/Sqrt[2]^1, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^1, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^1}]},
  {5,{{"z",1}},With[{w = (1 + I)/Sqrt[2]}, {(1 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0}]},
  {6,{{"t",1},{"z",0},{"h",1},{"tdg",1},{"tdg",0},{"h",1},{"nop",0},{"x",0},{"h",0},{"x",1},{"nop",0},{"nop",0},{"cx",0},{"t",0},{"x",0},{"tdg",0},{"sdg",1},{"t",1}},With[{w = (1 + I)/Sqrt[2]}, {(1 + -1 w + 0 w^2 + 0 w^3)/Sqrt[2]^3, (0 + 0 w + 1 w^2 + -1 w^3)/Sqrt[2]^3, (1 + 0 w + 0 w^2 + -1 w^3)/Sqrt[2]^3, (0 + 1 w + 1 w^2 + 0 w^3)/Sqrt[2]^3}]},
  {7,{{"x",1},{"h",1},{"h",1},{"x",0}},With[{w = (1 + I)/Sqrt[2]}, {(0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (0 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0, (1 + 0 w + 0 w^2 + 0 w^3)/Sqrt[2]^0}]}
};
Do[{n,gs,hdl}=d;psi=Fold[Expand[op[#2].#1]&,{1,0,0,0},gs];
 Print["Fall ",n,": Gatter ",Length[gs],", exakte Differenz ",Expand[ComplexExpand[psi-hdl]]],{d,data}]
