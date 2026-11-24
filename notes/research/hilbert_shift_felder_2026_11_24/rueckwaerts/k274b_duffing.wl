(* k274b (Erkundung, nicht blind, 24.11.2026): exakte Duffing-Periode zu k274 Teil A, w = 1, Wolfram-MCP-Kernel.
   T(lam, A) = 4/Sqrt[1 + lam A^2] EllipticK[m], m = lam A^2/(2(1 + lam A^2)). *)
T[lam_, A_] := 4/Sqrt[1 + lam A^2] EllipticK[lam A^2/(2 (1 + lam A^2))];
{Table[{lam, Table[N[T[lam, A], 6], {A, {0.1, 0.5, 1.0, 1.3}}]}, {lam, {0.5, -0.5}}],
 Series[T[lam, A], {A, 0, 2}] // Normal // Simplify,
 Solve[D[-(psi^2/2 + lam psi^4/4), psi] == 0 && psi > 0, psi]}
