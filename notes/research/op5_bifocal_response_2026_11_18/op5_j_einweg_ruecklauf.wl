Print["Kernel: ", $Version];
cross[z_] := z[[1]] z[[4]]/(z[[2]] z[[3]]);
fwd = {f00, f01, f10, f11}; rev = {b00, b01, b10, b11};
gauge = {lambda00, lambda01, lambda10, lambda11};
echo = fwd rev;
Print["echo factorization, gauge residuals = ", Together[{cross[echo] - cross[fwd] cross[rev],
 cross[(gauge fwd) (rev/gauge)] - cross[echo]}]];
Print["one-way cross ratio changes by arbitrary forward gauge = ", Together[cross[gauge fwd]/cross[fwd] - cross[gauge]]];
Print["reciprocal square residual = ", Together[cross[echo /. Thread[rev -> fwd]] - cross[fwd]^2]];
limit = 5/10^7;
Print["minimum requirements in isolation {round-trip residual, directional asymmetry, length change at 0.360329 eV in m} = ",
 N[{2 limit, 2 limit, limit (1973269804/10^16)/(360329/10^6)}, 12]];
Print["possible allocation {echo log residual, asymmetry log bound, one-way residual} = ",
 N[{4/10^7, 6/10^7, (4/10^7 + 6/10^7)/2}, 12]];
