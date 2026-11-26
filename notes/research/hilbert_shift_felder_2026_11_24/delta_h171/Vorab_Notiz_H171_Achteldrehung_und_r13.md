# Vorab-Notiz H171: Ist die Achteldrehung zwischen neutralem und geladenem Feld dieselbe wie Ψ = exp(uπ/4) aus r13 neu?

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Überwiegend nicht blind:** a, b, d stehen analytisch fest und sind von Hand überschlagen. c ist eine
Rechnung in den Sedenionen mit offenem Ausgang (Erwartung angegeben). Anlass: Autor, 26.11.2026, „ja, mach beides“ auf die Frage, ob nach H170 geprüft
werden soll, ob die Achteldrehung dieselbe ist wie exp(uπ/4) aus r13. Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4. Vergeben: H171, k366 (geprüft: frei).

## Vorwissen geprüft
- **r13 neu / k255** (`../r13/README.md`): Ψ = α·1 + β·w⊗n(δ); K = ⅔ genau für β = α, Ψ = (1 + u)/√2 = exp(uπ/4); δ ist die Richtung von u in der
  Kopienebene; O_θ ist nur bei θ = 0°, 60°, 120°, … eine Unteralgebra; δ nicht festgelegt.
- **H149, H156** (`../generationszahl_h138/`): θ = π/4 als Fixpunkt des Frame-Tauschs J (A ↔ B); K = ⅔ nur aus J als Postulat.
- **H158**: Brannen-Form in der Albert-Algebra exakt, δ = Phase der Nebendiagonale.
- **H167 bis H170** (`../delta_h167/` … `../delta_h170/`): c = 1 ⇔ Cσ-Symmetrie (Tausch s ↔ v); −i an der Form = Achteldrehung e^{−iπ/4} am Feld = Drehung
  von δ um π/4; Oktant δ = π/12.
- **H101, r12**: Oktant, masseloses Elektron; ρ² = ½. **H118, H123**: Phase π/4 des Oktant-Tripels.
- Suche nach „zwei Achteldrehungen“, „polar“ zusammen mit „azimut“ und „Koide“ in `notes/`, `wiki/`: kein Vorbefund.

**Suchrichtung:** rückwärts: Ziel sind K = ⅔ und c = 1 aus einer Quelle. Notwendig dafür: Beide Drehungen müssten dieselbe Ebene oder dieselbe Einheit
haben. **Werkzeugwahl:** Python (sympy exakt; numpy mit dem Sedenion-Produkt aus `../k253_cayley_dickson_turm.py` für c); Wolfram unabhängig für a, b, d.
Qiskit nicht geeignet.

## Aufbau (k366, `k366_test_h171.py`; Gegenprobe `k366b_gegenprobe.wl`)
Feld als reeller Dreiervektor n = (A, B cos δ, B sin δ) mit A = a, B = √2 r (Ebenen-Lesart wie H157). Polarwinkel θ: tan θ = B/A. Azimut δ.
Sedenionen: Kopienebene span(e_i, e_{i+8}), i = 1..7; Kopie O_θ wie in k255.

## Hypothesen und Kriterien
- **H171a (exakt): Es sind zwei verschiedene Drehungen.** Die r13-Achteldrehung ist die polare (Ebene Singulett–Dublett, θ = π/4, legt K = ⅔ fest, lässt δ
  frei): K hängt nur von θ ab. Die Achteldrehung aus H170 ist die azimutale (in der Dublettebene, δ ↦ δ + π/4, lässt K fest). Kriterium: K(θ, δ) unabhängig
  von δ; die Lage der Minima des Spin-1-Terms unabhängig von θ; Nullreste.
- **H171b (exakt): Gleiche Form, gleicher Ursprung als Fixachse eines Tauschs.** θ = π/4 ist die Fixachse von J (A ↔ B), χ = π/4 die Fixachse von Cσ (s ↔ v).
  Am Baumpunkt (K = ⅔, Spin-1-Term mit c = 1) ist die Nebendiagonale z = a·(±1 + j)/2 = (a/√2)·exp(jπ/4)·j^m: Betrag 1/√2 (polar) und Phase π/4 (azimutal)
  stecken in einer Zahl; die Gewichte von (A², 2s², 2v²) sind (½, ¼, ¼). Kriterium: Nullreste; Spektrum des Oktant-Zweigs mit Eigenwert 0.
- **H171c (Sedenionen, offen; Erwartung ja):** In der r13-Darstellung wird der Azimut von der Verdopplungseinheit e₈ erzeugt: Für i = 1..7 ist e_i·e₈ oder
  e₈·e_i gleich ±e_{i+8}, mit einheitlichem Vorzeichen je Seite. Die polare Einheit u liegt in einer Kopie, die azimutale ist e₈: zwei verschiedene
  Einheiten. Kriterium: Abweichung < 10⁻¹²; berichtet wird Seite und Vorzeichen. Zusatz (Bericht): Lage der ausgezeichneten Azimute (0, π/12, π/6, π/4, π/3)
  relativ zu den Unteralgebra-Richtungen 0°, 60° (Abgeschlossenheit wie k255 (3)).
- **H171d (exakt, Bericht): Beide zusammen sind keine einzelne Achteldrehung.** Die Zusammensetzung der polaren und der azimutalen Drehung um je π/4 ist eine
  Drehung um den Winkel Θ mit cos Θ = (2√2 − 1)/4 (62,80°); die beiden vertauschen nicht. Kriterium: Nullrest für cos Θ.

## Folge, vorab festgelegt
- a, b bestätigt: Antwort an den Autor: **Nicht dieselbe Drehung, aber dieselbe Regel auf zwei Ebenen.** r13 dreht vom Singulett in die Dublettebene (K = ⅔),
  H170 dreht innerhalb der Dublettebene (Sektorschritt). Gemeinsam ist: eine Achteldrehung als Fixachse eines Tauschs zweier gleich schwerer Anteile. K = ⅔ und
  c = 1 kommen damit **nicht** aus einer einzigen Operation; als Lesart bleibt „dieselbe Regel bei zwei aufeinanderfolgenden Verdopplungen“, das ist keine
  Herleitung.
- c bestätigt: Die beiden Drehungen gehören zu verschiedenen Einheiten (u in der Kopie, e₈ zwischen den Kopien). c nicht bestätigt: berichten, keine Folgerung.
- Kein Vorzeichen wird gesetzt; kein Guard berührt; OP3 und OP4 bleiben offen. Keine neue Datenvorhersage.
