(* Symbolic identities in the variable-coefficient OP5 estimate. *)
ClearAll["Global`*"];
Print["Kernel: ", $Version];

grad = Array[g, {3, 3}];
sym = (grad + Transpose[grad])/2;
iso = mu Tr[sym.sym] + lam Tr[grad]^2/2;
nullTerm = mu (Tr[grad]^2 - Tr[grad.grad])/2;
positiveForm = (mu Total[Flatten[grad]^2] + (lam + mu) Tr[grad]^2)/2;
Print["Elastic null-Lagrangian coercivity residual: ",
  Expand[iso + nullTerm - positiveForm]];
coords = {x, y, z};
field = {u1[x, y, z], u2[x, y, z], u3[x, y, z]};
jac = Table[D[field[[i]], coords[[j]]], {i, 3}, {j, 3}];
nullStress = Map[D[nullTerm, #] &, grad, {2}] /. Thread[Flatten[grad] -> Flatten[jac]];
Print["Null-Lagrangian force residual: ", Simplify[Div[#, coords] & /@ nullStress]];

fluid = {{0, n0}, {kap/(n0 m0), 0}};
fluidWeight = DiagonalMatrix[{kap/n0, n0 m0}];
Print["Acoustic symmetrizer residual: ",
  Simplify[fluidWeight.fluid - Transpose[fluidWeight.fluid]]];

(* Two arbitrary coupled fields and one frozen derivative direction. *)
mat = {{m11, m12}, {m12, m22}};
stiff = {{k11, k12}, {k12, k22}};
mixed = Array[b, {2, 2}];
zero = ConstantArray[0, {2, 2}];
coefT = ArrayFlatten[{{mat, zero}, {zero, stiff}}];
coefX = ArrayFlatten[{{mixed + Transpose[mixed], -stiff}, {-stiff, zero}}];
Print["First-order time and space symmetry residuals: ",
  Expand[{coefT - Transpose[coefT], coefX - Transpose[coefX]}]];

(* Energy identity for variable symmetric matrices and arbitrary solution. *)
symTime = {{a[t, x], b0[t, x]}, {b0[t, x], c[t, x]}};
symSpace = {{d0[t, x], e0[t, x]}, {e0[t, x], f[t, x]}};
lower = Array[p, {2, 2}];
state = {p1[t, x], p2[t, x]};
forced = symTime.D[state, t] + symSpace.D[state, x] + lower.state;
Print["Variable energy identity residual: ", Expand[
  D[state.symTime.state, t] + D[state.symSpace.state, x] -
  state.(D[symTime, t] + D[symSpace, x] - lower - Transpose[lower]).state -
  2 state.forced]];

(* Fixed-time radial derivatives of the shifted light-cone kernel. *)
radius = Sqrt[coords.coords];
direction = coords/radius;
radialKernel = source[t - radius]/radius;
unit = IdentityMatrix[3];
dyad = Outer[Times, direction, direction];
spatialHessian = Table[D[radialKernel, coords[[i]], coords[[j]]], {i, 3}, {j, 3}];
expectedHessian = source''[t - radius] dyad/radius +
  (3 dyad - unit) (source'[t - radius]/radius^2 + source[t - radius]/radius^3);
Print["Retarded spatial gradient residual: ", Simplify[
  Grad[radialKernel, coords] +
  direction (source'[t - radius]/radius + source[t - radius]/radius^2)]];
Print["Retarded spatial Hessian residual: ", FullSimplify[spatialHessian - expectedHessian]];
Print["Radial dyad and trace-free angular norm spectra: ",
  Simplify[{Eigenvalues[dyad], Eigenvalues[3 dyad - unit]}, coords.coords > 0]];
