ClearAll["Global`*"];
mp = 1836152673426/10^9;
mmu = 2067682827/10^7;
recoil[m_] := 4 m/(mp + m);
reduced[m_] := m mp/(mp + m);
direction[m_, shift_] := {-1 + recoil[m] + shift, 1};
inverseAngleCondition[u_, v_] := (Sqrt[u] + Sqrt[v])^2/Abs[u-v];
balancedCondition[shift_] := Module[{s},
  s = SingularValueList[Normalize /@ N[{direction[1, shift], direction[mmu, shift]}, 30], Tolerance -> 0];
  First[s]/Last[s]
];
residual = FullSimplify[
  Det[{{-1 + epsilonE + eta, 1}, {-1 + epsilonMu + eta, 1}}] -
  (epsilonE - epsilonMu)
];
massFactor = reduced[mmu]/reduced[1];
polarRatio = massFactor^-3;
report[label_, value_] := Print[label, " = ", NumberForm[N[value], 9]];
Print["common charge-shift determinant residual = ", residual];
report["electronic recoil", recoil[1]];
report["muonic recoil", recoil[mmu]];
report["normalized condition at unit coupling and zero shift", balancedCondition[0]];
report["best normalized condition at zero shift", inverseAngleCondition[1-recoil[1], 1-recoil[mmu]]];
report["normalized condition at unit coupling and lepton null", balancedCondition[1]];
report["best normalized condition at lepton null", inverseAngleCondition[recoil[1], recoil[mmu]]];
report["reduced mass ratio", massFactor];
report["static electric polarizability ratio", polarRatio];
report["common half-gap electric polarizability ratio lower bound", (3/4) polarRatio];
report["common half-gap electric polarizability ratio upper bound", (4/3) polarRatio];
report["electronic Coulomb gap [eV], using 13.605693123 eV", (3/4) (13605693123/10^9) reduced[1]];
