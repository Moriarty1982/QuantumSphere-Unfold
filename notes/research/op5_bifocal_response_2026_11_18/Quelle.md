# Rückwärtssuche: Welche native Größe könnte der Randdipol auslesen?

Analytische Erkundung gemäß [Vorab-Notiz](Quelle_Vorab.md), Commit 509dedecf59350ebdd3024541254ba1ae683f992. Der Randdipol ist im festen orientierten Chart unter Fokustausch ungerade. Eine direkte Identifikation ohne weitere Vorzeichenstruktur braucht eine ungerade, erhaltene Größe und eine eigene Abbildung auf die Chartachse.

## Freies Maxwell-Feld (r07/r11)

Unter der für dieses Feld erklärten Abbildung M→T, z=E+iB↦iz, bleibt die Maxwell-Energie-Impuls-Auslesung invariant. Sie liefert kein Vorzeichen. Re S=E²−B², S=z·z, wechselt das Vorzeichen, ist aber selbst räumlich integriert kein allgemeiner Erhaltungssatz.

Exakte Gegenprobe in Einheiten c=1 und auf einer periodischen x-Richtung: E=E₀ cos(kx)cos(kt) e_y und B=E₀ sin(kx)sin(kt) e_z. Die Divergenzen sind null, ∂_t B=−curl E und ∂_t E=curl B gelten durch direkte Ableitung. Im Mittel über eine räumliche Periode gilt ⟨u⟩=E₀²/4, aber ⟨Re S⟩=(E₀²/2)cos(2kt). Energie bleibt bei Null-Randfluss konstant, die dualitätsungerade Invariante ändert sich sogar im Vorzeichen. Das widerlegt ihre allgemeine Erhaltung und keine spezifische Randabbildung.

## Die übrigen bereits vorhandenen Kandidaten

- W1 besitzt einen erhaltenen Eichstrom j_J mit internem Dixon-Generator J=iL_e7. Seine Vorzeichen unterscheiden interne +/−-Ladungssektoren der Weyl-Komponenten innerhalb derselben Ablage. Die geprüfte W1-Wirkung wird in M aufgestellt. Es gibt dort keine Zuordnung dieser Vorzeichen zu den beiden Brennpunkten unter der Maxwell-Vierteldrehung. Interne Ladungszerlegung ist keine Frame-Zerlegung.
- H69 beschreibt unter seiner Lesart ein sich neutralisierendes M–T-Paar. Das liefert keinen von null verschiedenen allgemein erhaltenen Überschuss.
- k193 besitzt sein eigenes Erhaltungsdatum im skalaren Modell. Es hat keine hergeleitete Fokustausch- oder Randauslesungsregel.

Damit ist der direkteste freie Feldkandidat ausgeschieden. Die vorhandenen Erhaltungssätze liefern unter ihren jeweiligen Guards noch keine signierte physikalische Größe mit nachgewiesener Randabbildung. Eine echte M–T-Grenzflächenwirkung mit spezifizierter Symmetrie ist eine fehlende Eingabe, kein weiterer Rasterparameter. OP5 und H96 bleiben offen.
