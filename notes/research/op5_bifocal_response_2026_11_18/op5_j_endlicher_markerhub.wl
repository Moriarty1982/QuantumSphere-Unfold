ClearAll["Global`*"];
Print["Kernel: ", $Version];
left[z_] := Exp[-I kap z] + ri Exp[I kap z];
right[z_] := left[ell - z];
wr = left[z] D[right[z], z] - D[left[z], z] right[z];
Print["Green Wronskian residual: ", FullSimplify[
 wr - 2 I kap Exp[-I kap ell] (1 - ri^2 Exp[2 I kap ell])]];
Print["Outgoing Robin residuals: ", FullSimplify[
 {((D[left[z], z] + I k left[z]) /. z -> 0),
   ((D[right[z], z] - I k right[z]) /. z -> ell)} /.
   ri -> (kap - k)/(kap + k)]];
qMat = {{x^2, x}, {x, 0}};
Print["Perturbation eigenvalue polynomial residual: ",
 Expand[Det[qMat - z IdentityMatrix[2]] - (z^2 - x^2 z - x^2)]];

(* Exact scalar reference at the center, then a high-precision full transfer comparison. *)
ka = 10000 Pi; kj = 9999 Pi; kap0 = 10001 Pi; mix = 1/1000;
indexR = (kap0 - ka)/(kap0 + ka);
strength = (kap0^2 - ka^2)/ka;
greenBound = Max[1/2, ka (1 + indexR)^2/(2 kap0 (1 - indexR^2))];
incidentBound = Max[1, (1 - indexR)/(1 - indexR)];
beta = greenBound strength (mix^2 + Sqrt[mix^4 + 4 mix^2])/2;
diagBound = incidentBound (greenBound strength mix^2 + 2 beta^2/(1 - beta));
allBound = incidentBound beta/(1 - beta);
Print["Example {Neumann parameter, diagonal contrast error bound, reflection error bound}: ",
 N[{beta, diagBound, allBound}, 10]];
kk = DiagonalMatrix[{kj, ka}]; id = IdentityMatrix[2]; zero = ConstantArray[0, {2, 2}];
basis = ArrayFlatten[{{id, id}, {I kk, -I kk}}];
v = strength {{mix^2, mix}, {mix, 1}};
gen = ArrayFlatten[{{zero, id}, {-kk.kk - kk.v, zero}}];
prop = Inverse[N[basis, 55]].MatrixExp[N[gen, 55]].N[basis, 55];
reflected = -LinearSolve[prop[[3 ;; 4, 3 ;; 4]], prop[[3 ;; 4, 1 ;; 2]]];
transmitted = DiagonalMatrix[Exp[-I {kj, ka}]].(
 prop[[1 ;; 2, 1 ;; 2]] + prop[[1 ;; 2, 3 ;; 4]].reflected);
Print["Full transfer at the example frequency {diagonal contrast error, reflected norm}: ",
 N[{Abs[transmitted[[1, 1]] - transmitted[[2, 2]] - 2], Norm[reflected, 2]}, 9]];
Print["Both example bounds hold: ",
 {Abs[transmitted[[1, 1]] - transmitted[[2, 2]] - 2] < diagBound, Norm[reflected, 2] < allBound}];
uBand = (2067833848/10^16)/(360329/10^6);
bandBeta = beta (1 + uBand);
bandDiag = incidentBound (greenBound strength mix^2 (1 + uBand) +
  2 bandBeta^2/(1 - bandBeta));
Print["Illustrative 100 MHz band {contrast lower bound, reflection upper bound}: ",
 N[{2 Cos[Pi uBand/2] - 2 indexR^2/(1 - indexR^2) - bandDiag,
  2 indexR kap0 uBand/(1 - indexR^2) + incidentBound bandBeta/(1 - bandBeta)}, 10]];
