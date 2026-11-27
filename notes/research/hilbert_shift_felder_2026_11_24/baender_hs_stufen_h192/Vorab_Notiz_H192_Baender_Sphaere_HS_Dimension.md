# Vorab-Notiz H192: Bänder als Stufen des HS-Turms auf der Sphäre, Gewicht nach Dimension, Spannungsgesetz — kommt ein Winkel des Companion heraus?

**Stand:** 2026-11-27, vor der Rechnung festgelegt und vor dem ersten Lauf committet. Auftrag des Autors vom 27.11.2026, 08:55 UTC („ja“ zu dem
Vorschlag aus k399: Bänder auf der Sphäre mit Gewicht nach HS-Dimension und einem Spannungsgesetz, mit Vorab-Notiz). Zugleich die vom Autor
gewählte Richtung „Lesart wechseln“ für die Quarkmassen nach H190 (HS-Stufe statt Farbschwingung). Skripte **k400** (Python: numpy, scipy für die
Minimierung) und **k400b** (Wolfram: die symmetrischen Grenzfälle exakt). Werkzeugwahl: numerische Minimierung in Python, exakte Winkel der
symmetrischen Lagen in Wolfram. Kein HDL/MMA-Vergleich (keine endliche Guard-Suche). Kein Guard berührt.

## Vorwissen geprüft
- **k399 (27.11.):** Gleiche Bänder ordnen sich in platonische Winkel, gesetzesunabhängig (2→90°, 3→90°, 4→70,53° = arccos ⅓, 6→63,43° =
  arccos 1/√5); für 5 gleiche Bänder keine solche Lage, Winkel gesetzesabhängig. Mit Gewicht nach Dimension hingen die Winkel von Gewicht **und**
  Gesetz ab (RC von 35,6° bis 59,1°). Genau das ist die offene Stelle, die H192 testet.
- **r69:** Namen R, M, T, P. **r70:** Materie-Frame M bei b_C = 1/γ_L, Polwinkel 57,569°. **k245:** Hopf-Punkt θ = 60°.
- **H178, k380, k384, H180 (26.11.):** J ist Spiegelung nur in der farblosen Ebene; 𝕊 (HS4) hat unter Farbe vier Sektoren; θ = 45° ist der
  Fixpunkt des Frame-Tauschs; Koide-Winkel π/4. **Oktant/Oktantschritt** (r29, Companion 5.9): die drei Koordinatenebenen, acht Oktanten.
- **Companion-Winkel, die als Ziel zählen:** Oktant 90°; Materie-Frame M 57,569°; magischer Winkel 54,7356° (arccos 1/√3, Raumdiagonale);
  Hopf-Punkt 60°; θ = 45° (Koide, Fixpunkt); Würfel 70,5288° (arccos ⅓); Ikosaeder 63,4349° (arccos 1/√5).
- 𝕊 (Sedenionen) hat keine Hopf-Faserung (Adams 1960) und Nullteiler.

## Modell (gesetzt)
Fünf Bänder = Großkreise auf der Einheitssphäre, eines je Stufe R, ℂ, ℍ, 𝕆, 𝕊. Jedes Band ist durch seinen Normalenvektor n_i ∈ S² gegeben;
der Winkel θ_ij zwischen zwei Bändern ist der Winkel zwischen ihren Normalen. **Gewicht w_i = Dimension der Stufe = (1, 2, 4, 8, 16)** (ohne
freien Parameter). **Spannungsgesetz:** Energie E = Σ_{i<j} w_i w_j / sin θ_ij (zwei Großkreise kreuzen sich; die Kreuzungsdichte und damit die
Abstoßung geht wie 1/sin des Winkels). Minimiert wird über die Lagen der Normalen; die Gesamtdrehung ist frei (nur die Winkel zählen). Vielfache
Startlagen (≥ 200), bester Wert gewinnt.

Gesetzt sind: die Zuordnung Stufe → ein Band auf **einer** gemeinsamen S², das Gewicht = Dimension, das Gesetz 1/sin. Nichts davon ist hergeleitet.
Kein Winkel wird eingegeben.

## Vorhergesagte Zuordnung (vorab, nicht blind)
Rationale: Die schweren Stufen tragen die Quarks (𝕊 trägt vier Sektoren, k380), die leichten die Leptonen. Erwartung aus der Symmetrie:
- Die zwei schwersten Bänder 𝕆–𝕊 stehen am steilsten, nahe 90° (Oktant).
- Das Paar ℂ–ℍ (die „Lepton-Stufen“) trägt am ehesten den Materie-Frame-Winkel 57,569° oder den magischen Winkel 54,736°.

## Aussagen und Kriterien
- **H192a (nicht blind, Kontrolle):** Bei gleichem Gewicht (alle w_i = 1) reproduziert die Minimierung die platonischen Winkel aus k399.
  Bestätigt, wenn die Winkel für die symmetrischen Teilmengen auf < 0,1° mit arccos-Werten übereinstimmen.
- **H192b (Test):** Mit Gewicht = Dimension und Gesetz 1/sin trägt ein **vorab benanntes** Paar einen Companion-Winkel aus der Liste oben (außer
  dem trivialen 90°) auf **±1°**, ohne angepassten Parameter. **Bestätigt**, wenn 𝕆–𝕊 ≈ 90° **und** ℂ–ℍ einen der Winkel 57,569° oder 54,736°
  trifft. **Teilweise**, wenn nur die 90°/Oktant-Struktur herauskommt, die anderen Winkel aber keinen Companion-Wert treffen. **Widerlegt**, wenn
  auch 𝕆–𝕊 nicht nahe 90° liegt.
- **H192c (Robustheit, Bericht):** Dasselbe mit Gewicht = √Dimension und mit Gesetz 1/sin² (vier Kombinationen). Berichtet wird, ob die
  Winkel von Gewicht und Gesetz abhängen. Hängt das Ergebnis von H192b von dieser Wahl ab, ist H192b höchstens „teilweise“.

Zufallstreffer: Sieben Zielwinkel mit Fenster ±1° decken rund 14° von 90° ab, also etwa 16 %. Ein einzelner Treffer unter zehn Paaren ist deshalb
nicht aussagekräftig; H192b verlangt zwei **vorab benannte** Paare gleichzeitig, das senkt die Zufallsquote auf wenige Prozent.

## Vorab offengelegt (Erwartung)
Ich erwarte **H192b teilweise**: Die 90°/Oktant-Struktur der schweren Bänder dürfte aus der Symmetrie folgen, aber der konkrete Winkel ℂ–ℍ hängt
nach k399 von Gewicht und Gesetz ab und trifft vermutlich keinen Companion-Wert ohne Anpassung. Das wäre der ehrliche Ausgang: Geometrie plus
Dimensionsgewicht liefert die Oktant-Struktur, aber nicht die kleinen Winkel. Ein überraschendes „bestätigt“ wäre ein echter Hinweis.

## Bilanz der Setzungen (vor der Rechnung)
| Größe | Status |
|---|---|
| Zuordnung Stufe → ein Band auf gemeinsamer S² | gesetzt |
| Gewicht = Dimension (1,2,4,8,16) | gesetzt, ohne freien Parameter |
| Spannungsgesetz 1/sin θ | gesetzt (die Weggabelung, die den Wert trägt; deshalb H192c) |
| vorhergesagte Paare (𝕆–𝕊, ℂ–ℍ) | vorab benannt |
| Zielwinkel | aus Companion/Frames, nicht eingegeben |

## Grenzen
Starre Großkreise auf **einer** S²; keine echte Fläche mit Spannung, keine Dynamik. Kein Bezug zu Messdaten (der Test fragt nach einem Winkel,
nicht nach einer Masse). Bei „teilweise“ oder „widerlegt“ ist die Lesart „Quarks auf eigener HS-Stufe, Winkel aus Geometrie“ in dieser einfachen
Form erledigt; die nächste Weggabelung (getrennte Felder statt Geometrie) käme dann zurück an den Autor. Nächste frei: H193, k401.
