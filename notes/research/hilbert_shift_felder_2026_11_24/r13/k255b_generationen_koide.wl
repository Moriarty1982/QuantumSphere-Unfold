(* k255b (Erkundung, nicht blind): drei Generationen als Permutationsdarstellung 1 + 2 von S3 auf V_w = span{1, w(x)f1, w(x)f2};
   Koide exakt. Koordinaten (1, w f1, w f2). Ausgefuehrt ueber den Wolfram-MCP-Kern am 24.11.2026; Ausgabe k255b_out.txt *)
th = {0, 2 Pi/3, 4 Pi/3};
g = Table[{1/Sqrt[3], Sqrt[2/3] Cos[th[[k]]], Sqrt[2/3] Sin[th[[k]]]}, {k, 3}];
Print["Gram der g_k: ", Simplify[g . Transpose[g]]];
Print["Winkel g_k zur reellen Eins: cos^2 = ", Simplify[g[[All, 1]]^2], " (magischer Winkel ArcCos[1/Sqrt[3]] = ", N[ArcCos[1/Sqrt[3]] 180/Pi, 8], " Grad)"];
R = {{1, 0, 0}, {0, Cos[2 Pi/3], -Sin[2 Pi/3]}, {0, Sin[2 Pi/3], Cos[2 Pi/3]}};
Print["psi g_k = g_{k+1}: ", Simplify[(R . #) & /@ g - RotateLeft[g]] // Flatten // Union];
Print["Eigenwerte von psi: ", Eigenvalues[R], " (r13: Phase diag(1, w, wbar) in der Eigenbasis)"];
Psi = {al, be Cos[de], be Sin[de]};
c = Simplify[g . Psi];
Print["Amplituden c_k = ", c];
K = Simplify[Total[c^2]/Total[c]^2, {al > 0, be > 0}];
Print["Koide K = ", K, " ; K = 2/3 genau fuer ", Solve[K == 2/3 && al > 0 && be > 0, be]];
Print["Brannen-Form bei be = al: c_k/(al/Sqrt[3]) = ", Simplify[c/(al/Sqrt[3]) /. be -> al]];
Print["Psi bei be = al normiert: (1 + u)/Sqrt[2] = Exp[u Pi/4], Winkel zur Eins = ", ArcCos[1/Sqrt[2]]];
