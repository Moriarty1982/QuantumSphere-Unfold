# Erkundung: Die Dorau–Much-Kette im Tachyon-Frame (Gravitation und Dualitätsdrehung)

**7. November 2026. Status: Erkundung, nicht blind (Ergebnis analytisch vor der Rechnung klar), numerisch kontrolliert (k217).**
Anlass: Autorfrage, ob der Companion die Herleitung von Dorau–Much (PRL 136, 091602, arXiv:2510.24491) intern abbilden und damit die
allgemeine Relativitätstheorie selbst zeigen kann. Geplant war ein vorab festgelegter Test H98 („im T-Frame dieselbe Einstein-Gleichung“).
Bei der Vorwissen-Suche stellte sich heraus, dass das Ergebnis analytisch feststeht. Nach der Regel „nicht blind = offen sagen“ ist es deshalb
eine Erkundung; **H98 ist nicht vergeben.**

## Vorwissen geprüft
- v4.8.0-r06.3: z ↦ iz bildet s ↦ −s ab, erhält den Nullkegel; tauscht die beiden massiven Typen, Photon fix.
- **v4.8.0-r20.1: z ↦ iz vertauscht mit jedem Element von SO(3,ℂ)** (der eigentlichen Lorentzgruppe auf z = E + iB).
- v4.9.0-r02: z = E + iB, s = E² − B² + 2iE·B; z ↦ −z = C = PT.
- v4.9.0-r28: die Tachyon-Abbildung von Konvention F ist die Dualitätsdrehung z ↦ iz.
- v4.9.0-r40: bilinearer Vergleich wechselt unter z ↦ iz das Vorzeichen (m² ↦ −m²), hermitescher Vergleich ist frame-blind.
- r64, r67: unter der Zähl-Lesart ist die Gravitation frame-unabhängig (bisher als Lesart, nicht als Satz).
- r81–r84, H71, H77, H79: Tachyonbild einer Wirkung; mit Masse tachyonisch (H71); zweite Lesart: T-Anteil als Gewicht auf S_M (H79).
- v4.10.0-r06.5 und `Erkundung_Dorau_Much_relative_Entropie.md` (d): dort steht, unter z ↦ iz werde die Rapidität imaginär und der Boost
  eine Drehung.

## Korrektur zu v4.10.0-r06.5
Die Aussage in r06.5 (und Punkt (d) der Dorau–Much-Erkundung) ist **falsch**. z ↦ iz ist eine Drehung im Feldraum (E ↦ −B, B ↦ E), keine
Abbildung der Raumzeit. Nach v4.8.0-r20.1 vertauscht sie mit allen Lorentz-Transformationen; der Boost bleibt ein Boost, seine Rapidität
bleibt reell. Die in r06.5 gestellte Frage („ist z ↦ iz die Wick-Rotation von thm:artqft?“) ist damit beantwortet: **nein**, die beiden wirken
auf verschiedene Dinge (Feldraum gegen Zeitkoordinate). Die Korrektur gehört in die nächste Runde (append-only, r06 bleibt unverändert).

## Ergebnis
**Satz (Erkundung).** Für das freie Maxwell-Feld liefert die Dorau–Much-Kette im Tachyon-Frame dieselbe Einstein-Gleichung wie im
Materie-Frame: gleiches G, gleiches Vorzeichen, gleiche Eingaben.

Begründung:
1. Die Dualitätsdrehung U_α ist eine Symmetrie des freien Maxwell-Felds (Erhaltungsgröße: Helizität), lokal (wirkt punktweise auf F),
   lässt das Vakuum fest und bildet die Algebra des Rindler-Keils auf sich ab.
2. Sie vertauscht mit dem Boost (r20.1), also mit der Modulargruppe des Vakuums (Bisognano–Wichmann).
3. Die relative Entropie ist unter einem solchen Automorphismus invariant: S_rel(ω₀‖ω_φ) = S_rel(ω₀∘U‖ω_φ∘U) = S_rel(ω₀‖ω_{Uφ}).
4. Der Energie-Impuls-Tensor ist hermitesch in z und daher dualitätsinvariant; der Energiefluss T_ab ξ^a ξ^b ändert sich nicht.
   Was das Vorzeichen wechselt, sind die bilinearen Invarianten s = z·z: Lagrangedichte (E² − B²)/2 und E·B (r06.3, r40).

Numerische Kontrolle `llm/k217_dualitaet_gravitation.py` (2000 zufällige Felder und Boosts; Ausgabe `llm/k217_out.txt`): Vertauschung,
Invarianz des Tensors und des Nullflusses jeweils exakt 0; Vorzeichenwechsel von E² − B² und E·B exakt; Negativkontrolle (nicht-unitäre
Skalierung (1 + 0,3i)z) ändert den Tensor um O(1).

**Lesart.** Gravitation koppelt an den hermiteschen Tensor; die Frames unterscheiden sich in den bilinearen Invarianten. Deshalb ist die
Gravitation (für das Maxwell-Feld) frame-blind. Das macht die bisherige Lesart aus r64 („Gravitation selbst frame-unabhängig“) für diesen
Fall zu einem Satz. Neue Physik ist es nicht: Dualitätsinvarianz des Maxwell-Tensors ist Lehrbuchwissen.

## Zutatenkarte (QAM)
`llm/qam_dorau_much_companion.tex` (Export `.qam`), geprüft mit `qam.sty`: keine Meldung. Ergebnis des Exports:
- einsteinM: conditional, Eingaben {loclin, arealaw}
- einsteinT: conditional, Eingaben {loclin, arealaw}; Vergleich nach Abbildung D zulässig.

**Bilanz:** Die interne Fassung trägt **dieselben Eingaben wie Dorau–Much**. Gewinn 1 (Frame-Unabhängigkeit als Satz) ist erreicht, für das
Maxwell-Feld. Gewinn 2 (Vorfaktor ¼ aus dem Companion) ist nicht erreicht: das Flächengesetz bleibt Eingabe. Zum Vergleich die Prüfung des
Papers selbst: `llm/qam_dorau_much_paper.tex` (drei Meldungen: Beförderung, Eingabe als Ergebnis, Frame-Vermischung in der Lesart des
Companion).

## Grenzen
- Nur das freie Maxwell-Feld. Für massive Felder ist das Tachyonbild der Wirkung tachyonisch (H71); ein tachyonisches Feld hat keinen
  stabilen Hadamard-Grundzustand, die Voraussetzungen der Kette fehlen. Unter der zweiten Lesart (r84, H79) ist der T-Anteil ein Gewicht auf
  der M-Wirkung; ob und mit welchem Faktor er dann in den Fluss eingeht, ist nicht untersucht.
- Wechselwirkende Felder: Dualität ist dort im Allgemeinen keine Symmetrie.
- Das Flächengesetz bleibt gesetzt (r06.2).

## Nächste mögliche Schritte
1. Korrektur zu r06.5 und dieses Ergebnis als Runde v4.10.0-r07.
2. Massive Felder unter der zweiten Lesart: welcher Fluss geht bei Gewichten a, b in die Kette ein? (Achtung: Entscheidung Photon-Gewichte
   für die Gravitation, r05.)
3. Gewinn 2 bleibt die eigentliche offene Front: den Vorfaktor des Flächengesetzes aus den Frame-Zählungen ohne Anpassung begründen.
