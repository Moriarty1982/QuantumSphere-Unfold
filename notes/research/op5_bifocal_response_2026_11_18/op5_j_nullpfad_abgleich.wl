ClearAll["Global`*"];
Print["kernel version = ", $Version];

identity = IdentityMatrix[2];
left = {{1,1/20},{0,1}};
right = {{1,0},{I/25,1}};
mix = {{3/5,-4/5},{4/5,3/5}};
u = mix.DiagonalMatrix[{1,I}].Transpose[mix];
q = left.u.right;
w = right.left;
Print["cyclic similarity residual = ", Simplify[Inverse[left].q.left-u.w]];
Print["reciprocal endpoint residual = ",
  Simplify[Inverse[left].(left.u.Inverse[left]).left-u]];
nullWithSameFactors = left.right;
Print["same-branch null calibration residual = ",
  Simplify[right.Inverse[nullWithSameFactors].q.Inverse[right]-u]];

h = {{h11,h12},{h21,h22}};
lambda = DiagonalMatrix[{z1,z2}]+h;
Print["Schur product residual = ", Expand[Det[x identity-lambda]-
  ((x-z1-h11)(x-z2-h22)-h12 h21)]];

matchError[amount_] := Module[{val},
  val = Eigenvalues[N[DiagonalMatrix[{1,I}]+{{0,amount},{I amount,0}},45]];
  Max[Min /@ Transpose[Table[Abs[z-z0],{z,val},{z0,{1,I}}]]]
];
Print["direct eigenvalue shifts for zero-diagonal errors 0.01 and 0.001 = ",
  N[matchError /@ {1/100,1/1000},8]];
Print["tenfold mixing amplitude reduction, shift ratio = ",
  N[matchError[1/100]/matchError[1/1000],8]];

radius = Sin[2 Pi 10^8/(16 10^12)];
gap = 2 Sin[1/20];
equalEndpoint = radius/(1+Sqrt[1+radius]);
mixCeiling = 2 radius gap/(Sqrt[radius^2+4 radius gap]+radius);
Print["illustrative chord budget and eigenvalue gap = ", N[{radius,gap},9]];
Print["equal-end norm budget, no noise = ", N[equalEndpoint,8]];
Print["pure zero-diagonal mixing budget, no noise = ", N[mixCeiling,8]];
Print["budget inversion residuals = ",
  FullSimplify[{2 equalEndpoint+equalEndpoint^2-radius,
    mixCeiling^2/(gap-mixCeiling)-radius}]];
