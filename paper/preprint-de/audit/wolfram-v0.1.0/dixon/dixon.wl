(* Exact Dixon recheck in §2.4 of the published Quantum Sphaera preprint 0.1.0.
   Conventions: Companion f2a4e687, notes/research/op3_frame_bridge_2026_11_15/frame_bridge_commutant.py. *)
ClearAll["Global`*"];
Print["kernel = ", $Version];
qmul[{a1_, b1_, c1_, d1_}, {a2_, b2_, c2_, d2_}] := {
 a1 a2 - b1 b2 - c1 c2 - d1 d2,
 a1 b2 + b1 a2 + c1 d2 - d1 c2,
 a1 c2 - b1 d2 + c1 a2 + d1 b2,
 a1 d2 + b1 c2 - c1 b2 + d1 a2};
qc[v_] := v {1,-1,-1,-1};
omul[x_,y_] := Module[{p=x[[1;;4]], q=x[[5;;8]], r=y[[1;;4]], s=y[[5;;8]]},
 Join[qmul[p,r]-qmul[qc[s],q],qmul[s,p]+qmul[q,qc[r]]]];
unit[n_,i_] := UnitVector[n,i];
mulMat[prod_, n_, j_, side_] := Transpose[Table[
 If[side=="left",prod[unit[n,j],unit[n,k]],prod[unit[n,k],unit[n,j]]],{k,1,n}]];
leftO=Table[mulMat[omul,8,j,"left"],{j,1,8}];
rightO=Table[mulMat[omul,8,j,"right"],{j,1,8}];
leftH=Table[mulMat[qmul,4,j,"left"],{j,1,4}];
rightH=Table[mulMat[qmul,4,j,"right"],{j,1,4}];
i4=IdentityMatrix[4]; i8=IdentityMatrix[8]; i32=IdentityMatrix[32];
comm[a_,b_] := a.b-b.a;
zeroQ[x_] := And@@Flatten[Map[#===0&,x,{-1}]];
matUnits=Table[ArrayReshape[UnitVector[64,j],{8,8}],{j,1,64}];
derivativeResidual[d_] := Join[
  Flatten[Table[d.omul[unit[8,j],unit[8,k]]-
    omul[d.unit[8,j],unit[8,k]]-omul[unit[8,j],d.unit[8,k]],{j,1,8},{k,1,8}]],
  d.unit[8,8]];
derConstraints=Transpose[derivativeResidual /@ matUnits];
colour=ArrayReshape[#,{8,8}]& /@ NullSpace[derConstraints];
Print["octonion derivation dimensions {all, fixing e7} = ",
 {64-MatrixRank[derConstraints[[1;;512]]],Length[colour]}];
colourResidual[b_] := Flatten[Table[comm[a,b],{a,colour}]];
colourBlocks = ArrayReshape[#,{8,8}]& /@
 NullSpace[Transpose[colourResidual /@ matUnits]];
Print["colour commutant dimension on octonion factor = ",Length[colourBlocks]];
l7=leftO[[8]]; r7=rightO[[8]];
qo=i8/2-(I/6) l7-(I/3) r7;
cch=KroneckerProduct[i4,(i8+I l7)/2];
tk=Table[KroneckerProduct[-(I/2)rightH[[j]],i8],{j,2,4}];
tp=(cch.#&) /@ tk;
y2=KroneckerProduct[i4,qo]-i32/2+(i32-cch).tk[[3]];
lor=KroneckerProduct[#,i8]& /@ Rest[leftH];
liftedColour=KroneckerProduct[i4,#]& /@ colour;
all=Join[lor,I lor,tp,{y2},liftedColour];
Print["right quaternion multiplications commute with all left generators = ",
 And@@Flatten[Table[zeroQ[comm[a,b]],{a,Rest[leftH]},{b,rightH}]]];
Print["weak and hypercharge commute with Lorentz and colour = ",
 And@@Flatten[Table[zeroQ[comm[a,b]],{a,Join[tp,{y2}]},{b,Join[lor,I lor,liftedColour]}]]];
Print["weak cyclic brackets residuals vanish = ",
 And@@Table[zeroQ[comm[tp[[j]],tp[[Mod[j,3]+1]]]-I tp[[Mod[j+1,3]+1]]],{j,1,3}]];
candidates=Flatten[Table[KroneckerProduct[h,b],{h,rightH},{b,colourBlocks}],1];
restrictedResidual[b_] := Flatten[Table[comm[a,b],{a,Join[tp,{y2}]}]];
constraint=Transpose[restrictedResidual /@ candidates];
ker=NullSpace[constraint];
solution=(Plus@@MapThread[#1 #2&,{#,candidates}])& /@ ker;
Print["restricted commutant {unknowns, rank, dimension} = ",
 {Length[candidates],MatrixRank[constraint],Length[solution]}];
Print["full linear generator residuals vanish = ",
 And@@Flatten[Table[zeroQ[comm[a,b]],{a,all},{b,solution}]]];
Print["linear commutant mutual brackets vanish = ",
 And@@Flatten[Table[zeroQ[comm[a,b]],{a,solution},{b,solution}]]];
spectrum=Tally[Sort[6 Eigenvalues[y2]]];
Print["hypercharge 6 Y/2 {value, multiplicity} = ",spectrum];
ys=First /@ spectrum;
projectors=Table[Dot@@Table[(6 y2-yj i32)/(yi-yj),{yj,DeleteCases[ys,yi]}],{yi,ys}];
Print["hypercharge spectral projectors {idempotent, orthogonal, sum identity, in commutant} = ",{
 And@@Table[zeroQ[p.p-p],{p,projectors}],
 And@@((zeroQ[#[[1]].#[[2]]]&)/@Subsets[projectors,{2}]),
 zeroQ[Total[projectors]-i32],
 And@@Flatten[Table[zeroQ[comm[a,p]],{a,all},{p,projectors}]]}];
aLor=First[lor];
Print["antilinear obstruction {real rotation, purely imaginary paired boost, invertible rotation} = ",
 {aLor===Conjugate[aLor],Conjugate[I aLor]===-I aLor,MatrixRank[aLor]===32}];
Print["antilinear dimension = 0 (combine AX=XA with AX=-XA and invertible A)"];
Print["RESULT: ",If[Length[colour]===8 && Length[solution]===6 && Length[spectrum]===6,
 "EXACT DIMENSIONS REPRODUCED","CHECK FAILED"]];

