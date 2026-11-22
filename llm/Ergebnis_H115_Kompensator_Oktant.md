# H115: Kompensator und Nullrichtung des flachen Oktanten

22. November 2026. Nicht blind nach [Vorab-Notiz](Vorab_Notiz_H115_Kompensator_Oktant.md), Commit aceae41cf27e40cabfde58b6e2b4cfa5ae669fe9. [Wolfram-Skript](h115_hc_octant.wl) und [tatsächliche Ausgabe](h115_hc_octant.txt).

## H115a: Der vorhandene direkte Kompensator hat Rang null

In der konstruierten [Generationenkopplung](../sources/research/parts/generation-coupling.tex) gilt für die geschlossenen Zustände mit Einbettung \(S\) ausdrücklich \(JS=-S\). Folglich gilt \(CS=(S+JS)/2=0\). Der dortige Closure-Projektor \(P_{C_7}\) ist ein anderer Operator. Die direkte Rang-fünf-Behauptung ist widerlegt.

Bei einer komplexlinearen Involution hat das Bild von \(C\) geraden reellen Rang. Bei einer antiunitären Involution auf einem invarianten komplexen Dreiraum paart Multiplikation mit \(i\) die reellen Eigenräume zu \(+1\) und \(-1\). Ihr Rang ist drei, wie die Konjugationskontrolle zeigt. Die vorhandene [reelle Abstiegskonstruktion](../sources/research/parts/hc-mass-identification.tex) erfordert eine \(J\)-invariante Kernbedingung. Sie liefert keine Ausrichtung auf die Oktant-Nullgerade.

## H115b: Die gewünschte Halbierung existiert als reelle Projektion

Die drei Oktantstrahlen \(+x,+y,+z\) werden als Spalten in \(V\) angeordnet. Ihr zyklisches Überlappungsprodukt ist \((1+i)/4\) und hat Phase \(\pi/4\). Wolfram bestätigt die komplexe Nullgerade
\[
 L=\mathbb C u,\qquad u=(-i,1,-(1-i)/\sqrt2),\qquad Vu=0.
\]
Reell hat \(L\) die orthogonalen Richtungen \(n\) und \(in\). Für eine von ihnen sei \(P_n\) der reell-orthogonale Linienprojektor. Die Spiegelung \(J_n=I-2P_n\) liefert \(C_n=(I+J_n)/2=I-P_n\) mit reellem Rang fünf. Für die reelle Form \(D\) der Oktant-Auslese gilt \(DC_n=D\), weil die entfernte Richtung ohnehin im Kern liegt. Die Wahl \(in\) liefert dieselben Ränge und dieselbe Endauslese. Multiplikation mit \(i\) vertauscht die beiden Rang-fünf-Projektoren. Damit ist die bedingte Kette \(6\to5\to4\) bestätigt. Die Gram-Geometrie bestimmt die komplexe Nullgerade, aber keine ihrer reellen Richtungen.

## Ergänzende Einbettungskontrolle

Eine ambient antiunitäre Projektion kann Rang fünf liefern, wenn der eingebettete komplexe Dreiraum unter der Konjugation nicht invariant ist. Im Vergleich \(\mathbb C^5\) mit gewöhnlicher Konjugation verwende die drei Spalten \((e_1+i e_2)/\sqrt2,(e_3+i e_4)/\sqrt2,e_5\). Die Realteilauslese liefert reellen Rang fünf und verwirft nur die imaginäre Koordinate der dritten Spalte. Durch eine angepasste Basis im Eingangsraum kann diese dritte Spalte der Oktant-Nullgeraden entsprechen. Diese Einbettung erfüllt die bisherige Bedingung \(JS=-S\) nicht.

Für eine native Realisierung braucht es eine Einbettung oder Kopplung, die aus dem vorhandenen \(J\) die Phasenrichtung auf \(L\) festlegt. Auf einem einzelnen geladenen komplexen Sektor würde ein Projektor, der mit der kontinuierlichen Phasensymmetrie kommutiert, nur geraden reellen Rang erlauben. Der Vergleich liefert keine solche Einbettung, keine Zeitentwicklung und keine Herleitung der Photon-Endpunkt-Zuordnung aus H114. Wolfram prüfte alle Matrixresiduen exakt. Eine Quantenschaltung war nicht Teil der Prüfung.
