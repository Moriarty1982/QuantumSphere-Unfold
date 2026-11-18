# Direkte Quelle für den Randdipol

Analytische Erkundung gemäß [Vorab-Notiz](Quellkopplung_Vorab.md), Commit ee629dc7c7410e9b70932cf447865f4181ff5098. q ist der signierte geometrische Dipol, Q die erhaltene M/T-Differenz des Paarmodells, hier als fester Steuerparameter. Beide sind unter M/T-Tausch ungerade. Ihre physikalische Zuordnung bleibt eine Eingabe.

Im angesetzten Potential V=K q²/2−gQq+C Q²/2+λq⁴/4 (λ>0) ist q* durch Kq+λq³=gQ bestimmt.

- K>0: Eindeutiges Minimum. q*=(g/K)Q−(λ/K)(g/K)³Q³+O(Q⁵). V_min=(C−g²/K)Q²/2+(λ/4)(g/K)⁴Q⁴+O(Q⁶). Für g≠0 folgt also eine signierte lineare Antwort, aber keine generische quadratische Auslöschung. Bei C=g²/K ist der gesamte quadratische Teil K(q−gQ/K)²/2. Der Tausch erlaubt sämtliche drei ursprünglichen quadratischen Terme und erzwingt diese Relation nicht.
- K=0, g≠0: q*=sgn(gQ)|gQ/λ|^(1/3). V_min=C Q²/2−(3/4)λ^(−1/3)|gQ|^(4/3). Ein linearer äußerer Quellterm an der quartisch weichen Kreisgeometrie bewahrt weder die lineare Auslesung noch die quartische Energie in Q. Der Befund ist eine subtrahierte minimale Zusatzenergie im Modell, keine negative absolute Energieaussage.

Wenn Q als erhaltene homogene Eigendichte wirkt und die Energie bei Expansion nur über Q variiert, gilt p_add=Q dV_min/dQ−V_min. Ein Q²-Anteil liefert denselben quadratischen Druckbeitrag. Der quartische Anteil bei der Quadratbedingung liefert einen Druck in vierter Ordnung; er ist nicht exakt drucklos. Im weichen Fall hat der 4/3-Leitterm einen Druck derselben Ordnung.

Für OP5 ist die nächste strukturelle Bedingung damit scharf: Eine unabhängige Grenzflächenwirkung müsste die Koeffizienten der linearen Antwort gemeinsam aus demselben Residuum bestimmen oder eine andere Kopplung liefern. Der bloße M/T-Tausch oder das geometrische Fehlen eines q²-Terms reicht dafür nicht. Die Paarerhaltung bleibt ein Modellbefund. OP5 und H96 bleiben offen.
