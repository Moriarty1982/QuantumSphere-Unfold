# H113: Farbauslese des Generationsrasters

22. November 2026. Exakter, nicht blinder Test nach [Vorab-Notiz](Vorab_Notiz_H113_Farbauslese_Generationsraster.md), Commit df52d76518aa08fa9498f289cb033d00335e8aad. [Wolfram-Skript](h113_dixon_color_raster.wl) und [Laufausgabe](h113_dixon_color_raster.txt).

## Rechnung

Der Modellraum ist \(G\otimes(A_0\oplus A_c)\) mit drei farbtrivialen Generationsrichtungen, \(A_0\) der komplexen Linie aus \(1,e_7\) und \(A_c\) dem Farbtriplet mit den Spalten \(e_4,e_5,e_6\). Für \(z=(-1+i\sqrt3)/2\) wirkt das nichttriviale Farbzentrum auf \(G\otimes A_c\) als \(zI\). Jede farbäquivariante lineare Auslese \(T\) in ein Singulett erfüllt dort \(zT=T\). Daraus folgt \(T=0\), auch auf den drei Diagonalplätzen. Der zentrale Operator minus Identität hat auf dem farbigen Block Rang neun, auf dessen Diagonale Rang drei und auf der Restspalte Rang null. Sein Fixraum ist genau die Restspalte, da die volle Farbgruppe \(A_0\) invariant lässt. Eine Auslese des Restblocks kann daher Rang drei haben. **H113 ist für das festgelegte Raster widerlegt.**

Die zyklische Farbpermutation hat Determinante eins und verschiebt bei festen Zeilen den dreidimensionalen Diagonalraum in einen dazu orthogonalen Raum. Insbesondere bleibt das Muster der drei einzelnen Diagonalplätze unter Farbe nicht erhalten. Ein farbtrivialer Zusatzfaktor ändert auch im vollen Dixon-Raum den Zentrenfaktor \(z\) auf diesem Sektor nicht.

## Kontrolle mit dualem Farbindex

In \(\bar{\mathbf3}\otimes\mathbf3\simeq\operatorname{End}(\mathbf3)\) wirkt Farbe durch Konjugation. Die Spur ist invariant und bildet die drei Diagonaleinheiten auf dieselbe Zahl \(1\) ab. Der lineare Ausleser hat Rang eins. Auf Zustandsseite ist die Identitätsmatrix die einzige farbinvariante Richtung bis auf Skalierung, wie aus dem Kommutanten der irreduziblen Darstellung folgt. Mit einem **zusätzlichen unabhängigen** Generationsindex ergibt die Spur je Zeile Rang drei. Wenn schon die Zeile als dualer Farbindex dient, fällt sie als unveränderliche Generationskoordinate weg. Die Rechnung setzt den dualen Tensorindex als Vergleich ein. Sie weist ihn für die vorhandenen Rasterplätze nicht nach.

## Die Restspalte mit schwacher Verdopplung

In der [H26-Zuordnung](../notes/research/v4_10_0_r34_r47/llm/Ergebnis_H26_Verteilung_H_Faktor.md) liegt Farbe auf dem Oktonionfaktor und die schwache Dublettwirkung auf dem Quaternionfaktor. Unter den dort gewählten Ladungen liefert die eine farbneutrale Spalte dann pro Generation das linksseitige Paar \((\nu,\ell)\). Der farbige Block liefert Up- und Down-artige Komponenten jeweils mit allen drei Farben. Mit dem schwachen Zweierfaktor sind es im Vergleichsraum 24 komplexe interne Richtungen, davon sechs farbneutral. [H27](../notes/research/v4_10_0_r34_r47/llm/Ergebnis_H27_MM_Kompensator_Chiralitaet.md) betrachtet die chiralen Partner unter zusätzlichen Setzungen. Die Generationeneinbettung und die Massen folgen aus dieser Farbprüfung noch nicht.

Der erste Wolfram-Lauf meldete inkompatible Tensorformen, weil das Kroneckerprodukt der zwei Listen einen Rang-2-Tensor beließ. Nach expliziter Vektorisierung verlief der Lauf ohne Meldungen. Die Kriterien blieben unverändert. Wolfram prüfte exakte Matrizenränge und Residuen. Eine Quantenschaltung war nicht Teil dieses Tests.
