# k399: Möbiusband, Band auf der Sphäre, mehrere Bänder, Bänder als Stufen des HS-Turms (Erkundung, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test; Geometrie. Teil 2 (Hopf-Punkt) und Teil 6 sind nachträgliche Beobachtungen. **Anlass:** Bilder
des Autors vom 27.11.2026: beidseitig beschriebenes Band → Möbiusband → höherdimensional; Spinor als Gummischlauch; Band am Äquator maximal
gedehnt, Sphäre maximal entspannt; alle Bänder gleichzeitig auf die Oberfläche; jedes Band eine Stufe des HS-Turms. **Werkzeuge:** Python
(numpy, scipy), bekannte Geometrie.

## 1 Möbiusband und Torus
Ein beidseitig beschriebenes Band, einmal verdrillt und verklebt, ist ein Möbiusband: Vorder- und Rückseite werden eine Fläche, und der Rand
schließt sich erst nach zwei Umläufen (nachgerechnet: nach 4π, nicht nach 2π). Das ist genau der Spinor-Vorzeichenwechsel (erst nach 720°
zurück); Vorder-/Rückseite = ±, passend zur Lesart Rückseite = Dual-Frame T. Gibt man dem Band eine Dicke, wird es ein Volltorus, und seine
Oberfläche ist ein Torus; sein Rand läuft darauf als (2,1)-Kurve (zweimal lang herum, einmal um den Schlauch, nachgerechnet). Die
höherdimensionale Verdrillung ist nicht der Torus, sondern die Kleinsche Flasche (zwei Möbiusbänder am Rand verklebt, nicht orientierbar); der
Torus entsteht ohne Verdrillung.

## 2 Band auf der Sphäre der Feldzustände
Ein Breitenkreis beim Polwinkel θ hat die Länge 2π sin θ; sein Urbild unter der Hopf-Abbildung in S³ ist ein Torus mit Fläche 2π² sin θ (beides
numerisch bestätigt). Beide sind am Äquator (θ = 90°) maximal (Clifford-Torus, Fläche 2π²). „Band maximal gedehnt, Sphäre maximal entspannt“ ist
also der Äquator. Nachträglich: Der Materie-Frame M sitzt bei θ = 57,569° (b_C = 1/γ_L), der Hopf-Punkt der Schleife (b = ½, k395) bei θ = 60°
(sin = √3/2), und das Vektormodell des Spins ½ (cos θ = 1/√3) bei θ = 54,736°. Das sind Einordnungen, kein Befund.

## 3 Ein Band abseits des Äquators
Setzt man die Bandlänge fest (maximal gedehnt), so ist die Bedingung „Weg wieder maximal“ erfüllt, sobald der Breitenkreis des Bands der
längste der Fläche ist, also ihr Äquator. Die Sphäre kann sich dazu einfach so drehen, dass ihre Achse senkrecht zum Band steht (kostet nichts);
hält man die Achse fest, muss sie ihren Mittelpunkt um cos θ verschieben oder den Breitenkreis um 1/sin θ dehnen. **Ein einzelnes Band erzwingt
keine neue Form.** Zahlen entstehen erst, wenn mehrere Bänder gleichzeitig maximal sein wollen.

## 4 Mehrere Bänder gleichzeitig
Je zwei Großkreise schneiden sich in zwei Gegenpunkten; alle Bänder können gleichzeitig maximal lang sein, aber nicht kreuzungsfrei. Mit einer
Abstoßung (Energie Σ 1/sinˢ Winkel, s = 1 und s = 2) ordnen sich gleiche Bänder in die erwarteten symmetrischen Lagen, **unabhängig vom
Abstoßungsgesetz**: 2 Bänder 90°, 3 Bänder 90° (Koordinatenebenen, acht Oktanten), 4 Bänder 70,53° = arccos(⅓) (Würfeldiagonalen), 6 Bänder
63,43° = arccos(1/√5) (Ikosaeder). Für 5 gleiche Bänder gibt es keine solche Lage; die Winkel hängen vom Gesetz ab (59,1°/74,0° bei s = 1,
59,6°/73,0° bei s = 2). Die Zahlen 3 und die Oktanten sind dabei genau die Geometrie, die im Companion schon auftritt.

## 5 Jedes Band eine Stufe des HS-Turms
Gibt man den fünf Bändern R, ℂ, ℍ, 𝕆, 𝕊 ein Gewicht nach ihrer Dimension (1, 2, 4, 8, 16) oder nach deren Wurzel, stellen sich die schweren
Bänder (𝕆, 𝕊) nahezu senkrecht und die leichten ordnen sich danach ein, aber die konkreten Winkel hängen von Gewicht und Abstoßungsgesetz ab
(z. B. RC von 35,6° bei Gewicht = Dimension bis 59,1° bei gleichem Gewicht). **Ohne ein hergeleitetes Gewicht und Abstoßungsgesetz liefert das
Bild keine Zahl.** Das ist die offene Stelle, an der ein späterer Test ansetzen müsste.

## 6 Die Folge Möbius–Torus ist die Folge der Hopf-Faserungen (nachträglich)
Die Stufen mit einer Hopf-Faserung sind genau R, ℂ, ℍ, 𝕆 (Dimension 1, 2, 4, 8; Adams 1960). Das Urbild eines Breitenkreises ist S^{n−1} × Sᶠ
mit Volumen ~ sin^{n−1} θ. Stufe R ist das Möbiusband (Rand läuft zweimal um), Stufe ℂ der Torus über dem Band (Teil 1 und 2). Die Folge
„Möbiusband, Torus, …“ ist also die Folge der Hopf-Faserungen, und sie endet bei 𝕆; 𝕊 (Sedenionen) hat keine Faserung und Nullteiler. Das passt
zum Bild des Autors, ist aber bekannte Topologie, kein neuer Befund.

## Lesart und nächster Schritt
Die Bilder treffen bekannte Geometrie: Möbius = Spinor-Vorzeichen, Band am Äquator = Clifford-Torus, mehrere Bänder = platonische Winkel,
Turmstufen = Hopf-Faserungen. Eine **Zahl** (θ, δ, β_sym) entsteht erst mit zwei Setzungen, die noch fehlen: dem Gewicht je Band und dem
Abstoßungs- oder Spannungsgesetz. Das wäre ein Test mit Vorab-Notiz wert: Gewicht = Dimension des HS-Turms, Spannung aus einer Variationsaufgabe
(Band fest, Fläche minimal), mit dem Kriterium, ob einer der Winkel des Companion (Oktant, 57,569°, θ = 45°) ohne Anpassung herauskommt.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Möbius = Spinor-Vorzeichen, Band = Clifford-Torus, Stufen = Hopf-Faserungen | bekannte Geometrie, nachgerechnet |
| Winkel für 2, 3, 4, 6 gleiche Bänder | hergeleitet (gesetzesunabhängig) |
| Gewicht je Band, Abstoßungsgesetz | **nicht** gesetzt; genau hier fehlt die Eingabe |
| Einordnung der Frames (57,569°, 60°, 54,736°) | nachträglich, kein Befund |

## Grenzen
Starre Großkreise, Punkt-Abstoßung statt echter Spannung einer Fläche; kein Bezug zu Messdaten. OP-Fragen bleiben offen.
