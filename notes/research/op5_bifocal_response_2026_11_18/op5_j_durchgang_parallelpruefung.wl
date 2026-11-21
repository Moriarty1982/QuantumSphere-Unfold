Print["Kernel: ", $Version];
sol[x1_, x2_, y1_, y2_] := (x2 y1 - x1 y2)/(x2 - x1);
Print["intercept residual = ", Together[sol[x1,x2,t + r x1,t + r x2] - t]];
Print["perturbed intercept identity residual = ", Together[
 sol[x1 + dx1,x2 + dx2,t + r x1 + dy1,t + r x2 + dy2] - t -
 ((x2 + dx2) (dy1 - r dx1) - (x1 + dx1) (dy2 - r dx2))/(x2 + dx2 - x1 - dx1)]];
amp = 2/100;
noiseX = 1/10^8; noiseY = 1/10^8;
minThrough = 99/100;
bound = 2 (amp + noiseX) (noiseY + noiseX)/(2 amp - 2 noiseX);
crossBudget = -4 Log[1 - bound/minThrough];
refBudget = 4/10^7;
Print["intercept, log-cross error, with reference-plane budget = ", N[{bound, crossBudget, crossBudget + refBudget}, 14]];
Print["illustrative through control meets previous 5e-7 budget = ",
 N[crossBudget + refBudget, 45] <= 5/10^7];

sig[n_] := scale z^n;
ev[n_] := 2^-n - I 4^-n;
Print["single mode closure residual = ", Expand[sig[0] sig[2] - sig[1]^2]];
Print["evanescent mixture {two ratios, closure} = ", Together[{ev[1]/ev[0], ev[2]/ev[1], ev[0] ev[2] - ev[1]^2}]];
ke = {{e0, couplingE},{couplingE, e1}};
kb = {{b0, couplingB},{couplingB, b1}};
basis = {{1, u},{v, 1}};
split[x_] := Tr[x]^2 - 4 Det[x];
Print["kinetic discriminant {basis, proportional, tensor} residuals = ", Together[{
 split[Inverse[Transpose[basis].ke.basis].(Transpose[basis].kb.basis)] - split[Inverse[ke].kb],
 split[Inverse[ke].(lambda ke)],
 split[Inverse[DiagonalMatrix[{z0+delta,1}]].DiagonalMatrix[{z0-delta,1}]] - 4 delta^2/(z0+delta)^2}]];
Print["tensor index first derivative at zero = ", FullSimplify[D[Sqrt[(z0+delta)/(z0-delta)],delta] /. delta -> 0,z0>0]];
