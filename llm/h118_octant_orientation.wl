(* H118: Legt der Bestand die Orientierung des Oktanten fest?  Vorab-Notiz llm/Vorab_Notiz_H118_Oktant_Orientierung.md, Commit 371f14d7. *)
(* Exakte Rechnung auf dem invarianten Dublett chi = (Sqrt[s+], Sqrt[s-]) mit R = sz, T = sx, J_B = sy (r16.7). *)

sx = {{0, 1}, {1, 0}}; sy = {{0, -I}, {I, 0}}; sz = {{1, 0}, {0, -1}};
pole[m_, s_] := Normalize[(First @ Select[Transpose[Eigensystem[m]], #[[1]] == s &])[[2]]];
(* Bloch-Achsen: z = Helizitaet (R), x und y auf dem Aequator (T bzw. J_B) *)
vz[s_] := pole[sz, s]; vx[s_] := pole[sx, s]; vy[s_] := pole[sy, s];
blochVec[v_] := FullSimplify[Re[{Conjugate[v].sx.v, Conjugate[v].sy.v, Conjugate[v].sz.v}]];
bargmann[a_, b_, c_] := FullSimplify[(Conjugate[a].b) (Conjugate[b].c) (Conjugate[c].a)];
phase[a_, b_, c_] := FullSimplify[Arg[bargmann[a, b, c]]];

Print["(0) Pole: Bloch-Vektoren von vz(+1), vx(+1), vy(+1): ", {blochVec[vz[1]], blochVec[vx[1]], blochVec[vy[1]]}];

(* (1) Acht Tripel, beide Umlaufrichtungen; H118a: Phase = tau * eps * Pi/4 mit eps = sz*sx*sy *)
signs = Tuples[{1, -1}, 3];
rows = Table[
   Module[{a = vz[e[[1]]], b = vx[e[[2]]], c = vy[e[[3]]], p1, p2, eps},
    p1 = phase[a, b, c]; p2 = phase[a, c, b]; eps = Times @@ e;
    {e, eps, p1, p2, Simplify[p1 - eps Pi/4], Simplify[p2 + eps Pi/4]}], {e, signs}];
Print["(1) Tripel {sz,sx,sy} | eps | Phase z->x->y | Phase z->y->x | Rest1 | Rest2"];
Scan[Print["    ", #] &, rows];
Print["    H118a: alle Reste null: ", And @@ (#[[5]] === 0 && #[[6]] === 0 & /@ rows)];
Print["    Betrag der Bargmann-Invariante: ", Union[FullSimplify[Abs[bargmann[vz[#[[1]]], vx[#[[2]]], vy[#[[3]]]]]] & /@ signs]];

(* (2) Wirkung von R, T, J_B (unitaer) und von zwei antiunitaeren Abbildungen auf die Phase eines Tripels *)
unit[m_][v_] := m.v;
theta[v_] := (I sy).Conjugate[v];          (* Antipode, Umkehrwalze Theta = i sy K *)
kconj[v_] := Conjugate[v];                 (* z -> conj z: Zeitumkehr der Feldamplituden, siehe (3) *)
maps = {{"R = sz", unit[sz]}, {"T = sx", unit[sx]}, {"J_B = sy", unit[sy]}, {"Theta = i sy K", theta}, {"K (z -> conj z)", kconj}};
Print["(2) Phase z->x->y nach Abbildung, je Tripel (eps zum Vergleich)"];
Scan[Function[mp,
   Module[{ph = Table[phase[mp[[2]][vz[e[[1]]]], mp[[2]][vx[e[[2]]]], mp[[2]][vy[e[[3]]]]], {e, signs}]},
    Print["    ", mp[[1]], ": ", ph, "  erhaelt Vorzeichen: ",
     ph === Table[(Times @@ e) Pi/4, {e, signs}], "  kehrt um: ", ph === Table[-(Times @@ e) Pi/4, {e, signs}]]]], maps];
Print["    Theta^2 = ", theta[theta[{u, w}]] // Simplify, " fuer {u,w} (erwartet -{u,w})"];
Print["    K bildet Pole auf Pole ab: Bloch(K vy(+1)) = ", blochVec[kconj[vy[1]]], ", Bloch(K vx(+1)) = ", blochVec[kconj[vx[1]]],
  ", Bloch(K vz(+1)) = ", blochVec[kconj[vz[1]]]];

(* (3) Feldebene: Zeitumkehr und Paritaet auf s+- = F+-.F+-, F+- = E +- i B (komplexe Amplituden, wie helicity_axis.py) *)
ee = Table[er[k] + I ei[k], {k, 3}]; bb = Table[br[k] + I bi[k], {k, 3}];  (* Real- und Imaginaerteile reell *)
spm[f_, g_] := {(f + I g).(f + I g), (f - I g).(f - I g)};
{sp, sm} = spm[ee, bb];
(* Zeitumkehr: E(t) -> E(-t), B(t) -> -B(-t); fuer E(t) = Re(E e^{-i w t}) heisst das E -> conj E, B -> -conj B *)
{spT, smT} = spm[Conjugate[ee], -Conjugate[bb]];
Print["(3) Zeitumkehr: s+ -> conj s+ ? ", Simplify[ComplexExpand[spT - Conjugate[sp]]] === 0,
  "   s- -> conj s- ? ", Simplify[ComplexExpand[smT - Conjugate[sm]]] === 0];
(* Paritaet: polarer Vektor E -> -E, axialer Vektor B -> B *)
{spP, smP} = spm[-ee, bb];
Print["    Paritaet: s+ -> s- ? ", Simplify[spP - sm] === 0, "   s- -> s+ ? ", Simplify[smP - sp] === 0,
  "   (auf chi also der Tausch der Komponenten = sx, wie die Frame-Abbildung T)"];

(* (4) K5: Dreierzyklus U = diag(conj w3, 1, w3) auf (s+, w, conj s-), r16.9; Overlap <psi|U psi> fuer Gewichte p *)
w3 = Exp[2 Pi I/3];
ov[pm_, p0_, pp_, dir_] := p0 + pm w3^(-dir) + pp w3^dir;
Print["(4) Im<psi|U psi> = ", FullSimplify[ComplexExpand[Im[ov[pm, p0, pp, 1]]], Element[{pm, p0, pp}, Reals]],
  ";  unter U -> U^-1: ", FullSimplify[ComplexExpand[Im[ov[pm, p0, pp, -1]]], Element[{pm, p0, pp}, Reals]],
  ";  unter p+ <-> p-: ", FullSimplify[ComplexExpand[Im[ov[pp, p0, pm, 1]]], Element[{pm, p0, pp}, Reals]]];

(* (5) Plausibilitaet: 200 zufaellige Unitaere erhalten, ihre antiunitaeren Gegenstuecke kehren die Phase um *)
SeedRandom[118];
randU[] := Module[{m = RandomComplex[{-1 - I, 1 + I}, {2, 2}]}, First[QRDecomposition[m]]];
dev = Table[Module[{u = randU[], a = N@vz[1], b = N@vx[1], c = N@vy[1], p0, pu, pk},
    p0 = Arg[(Conjugate[a].b) (Conjugate[b].c) (Conjugate[c].a)];
    pu = Arg[(Conjugate[u.a].(u.b)) (Conjugate[u.b].(u.c)) (Conjugate[u.c].(u.a))];
    pk = Arg[(Conjugate[u.Conjugate[a]].(u.Conjugate[b])) (Conjugate[u.Conjugate[b]].(u.Conjugate[c])) (Conjugate[u.Conjugate[c]].(u.Conjugate[a]))];
    {Abs[pu - p0], Abs[pk + p0]}], {200}];
(* Ausgabe nur der beiden Maxima *)
Print["(5) max |Phase(U) - Phase|, max |Phase(U K) + Phase| ueber 200 Unitaere: ", ScientificForm[Max[#], 3] & /@ Transpose[dev]];
