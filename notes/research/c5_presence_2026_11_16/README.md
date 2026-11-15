# C5 (B3): Liegen Felder mit Nullaugenblick vor?

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind** (die Kernaussagen folgen analytisch), ohne Kriterium, keine
H-Nummer. Auftrag des Autors: „weiter“ nach der Neufassung von C5 (Runde r21, PR #147, noch nicht gemergt); laut Übergabe ist (B3)
der nächste Schritt. **Die Aussage C5 = 0 wird nicht gemacht; C5 bleibt offen.** Skript `presence.py`, Ausgabe
`run/presence_stdout.txt`.

## Frage
r20.1 fand Nullaugenblicke nur für eine Familie von Kodimension 1 der Amplituden in einem Punkt. (B3) aus r21.7 fragt, warum solche
Felder vorliegen sollten. **Suchrichtung:** rückwärts, von der Bedingung zu den Feldklassen, die sie erfüllen.

## Vorwissen geprüft
- **r20.1, r20.3:** Nullaugenblicke existieren (Kodimension 1); sie brauchen beide Helizitäten; reine Helizität hat keine.
- **r21.6:** Bleibende Null nur für s₊ = s₋ = w = 0, also z. B. für eine einzelne ebene Welle.
- **r21.8:** zwei Klassen; P als Vertreter der lichtartigen Klasse.
- Im Repo keine Vorbefunde zu Überlagerungen ebener Wellen, stehenden Wellen oder linearer Polarisation im C5-Zusammenhang
  (Suche in `notes/research/predictions/`, `notes/research/v4_10_0_*`, `c5_*`, `op3_*`, `analysis/`).
- **Literatur (nachträglich gefunden, nicht vorab):** Die Nullstellen von F·F mit F = E + iB heißen **Riemann–Silberstein-Wirbel**.
  G. Kaiser, „Helicity, polarization, and Riemann–Silberstein vortices“ (2003, math-ph/0309010), definiert sie als Flächen in der
  Raumzeit mit F·F = 0; I. Białynicki-Birula und Z. Białynicka-Birula, „Vortex lines of the electromagnetic field“ (2003,
  physics/0305012), führen sie als Wirbellinien. **Der Nullaugenblick aus r20 ist also ein Punkt auf einem bekannten Objekt.** Neu
  ist nur seine Rolle als C5-Kandidat.

## Ergebnisse
1. **Bedingung (exakt).** Ein Nullaugenblick liegt genau dann vor, wenn die quadratische Gleichung s̄₋x² + 2wx + s₊ = 0 eine Wurzel
   auf dem Einheitskreis hat. Gleichwertig: Der Punkt −2w e^{−iγ} mit γ = (arg s₊ − arg s₋)/2 liegt auf der Ellipse mit den Halbachsen
   |s₊| + |s₋| und ||s₊| − |s₋||. Ob der Ursprung innerhalb der Ellipse liegt, entscheidet die Zahl der Wurzeln im Einheitskreis
   (innen genau dann, wenn 0 oder 2 Wurzeln innen liegen; 400 von 400 Feldern stimmen). Beim Beispiel aus r20.1 liegt eine Wurzel
   exakt auf dem Kreis.
2. **Eine ebene Welle:** s(t) = 0 für alle t, bei jeder Polarisation. Das ist die bleibende Null von r21.6 und kein Nullaugenblick.
3. **Zwei ebene Wellen gleicher Frequenz.** Dort ist s(t) = 2 z₁(t)·z₂(t).
   - Ist eine der beiden Wellen **linear polarisiert**, so verschwindet sie zweimal je Periode. Dann ist das Feld gleich der anderen
     Welle, also lichtartig und ≠ 0: **ein Nullaugenblick in jedem Punkt des Raums** (300 von 300 Punkten, für linear + linear,
     linear + elliptisch, linear + zirkular).
   - Sind beide elliptisch oder zirkular, gibt es Nullaugenblicke nur auf einer Fläche (0 von 300 Zufallspunkten).
4. **Linear heißt gleiche Helizitätsgewichte (½, ½).** Eine ebene Welle hat genau dann eine zeitliche Nullstelle, wenn sie linear
   polarisiert ist, also beide Helizitäten gleich stark trägt. Das passt zu r20.3.
5. **Allgemeines Feld (sechs elliptische Wellen):** Das Vorzeichen der Ellipsenbedingung wechselt im Raum vielfach (42 % der
   Gitterpunkte innen, 3167 Wechsel auf einem 31³-Gitter). Die Punkte mit Nullaugenblick bilden also **Flächen im Raum**. An
   Punkten dieser Fläche ist s zur Wurzelzeit null (|s|/2u ≤ 1,2·10⁻¹⁵) bei Feld ≠ 0.

## Was daraus für (B3) folgt
- **„Nicht generisch“ war eine Aussage über einen Punkt, nicht über ein Feld.** Kodimension 1 der Amplituden in einem Punkt heißt
  Kodimension 1 im Raum. Jedes generische monochromatische Feld, das nicht überall reine Helizität hat, trägt Flächen mit
  Nullaugenblicken; in der Raumzeit sind es die Riemann–Silberstein-Wirbel.
- **Es gibt eine native Klasse, in der Nullaugenblicke überall vorliegen:** Überlagerungen, in denen eine Teilwelle linear polarisiert
  ist, also gleiche Helizitätsgewichte hat. Das ist der helizitätsneutrale Fall, der in Lesart B dem Äquator der Helizitätsachse
  entspricht (r16.2(b)). Ob „helizitätsneutral“ im Bestand eine ausgezeichnete Rolle hat, die das Vorliegen begründet, ist nicht
  geprüft.
- **(B3) ist damit verschoben, nicht geschlossen.** Die Frage „warum gerade solche Felder“ entfällt in ihrer alten Form: Solche Punkte
  liegen in fast jedem Feld vor. Offen bleibt, warum der Zeuge an einem solchen Punkt liegen sollte; das ist eine Frage der Auswahl
  des Punktes, nicht des Feldes.

## Was das nicht ist
- Keine C5-Entladung. (B1), die Lesart „Obstruktion = Boden“ (r10), bleibt eine Lesart.
- Der Nullaugenblick ist ein bekanntes Objekt der Literatur; der Befund ist keine Neuheit der Physik, nur eine Einordnung im Projekt.
- Nur freie, monochromatische Felder in Lesart B. Für polychromatische Felder ist s(t) kein trigonometrisches Polynom zweiten Grades;
  die Flächenaussage (Kodimension 1 im Raum) bleibt plausibel, ist aber nicht gerechnet.

## Nachtrag 16.11.2026: Hat „helizitätsneutral“ eine ausgezeichnete Rolle?
Auftrag des Autors: „weiter“. Offener Punkt aus dieser Notiz: Ob lineare Polarisation (gleiche Helizitätsgewichte, b_y = 0) im
Bestand eine ausgezeichnete Rolle hat. **Erkundung, nicht blind.** Skript `helicity_neutral.py`, Ausgabe
`run/helicity_neutral_stdout.txt`.

### Fundstellen
- **v4.10.0-r16.2(a):** Die Tachyon-Abbildung R erhält b_y, T und J_B kehren es um (wie die Chiralität in v4.9.0-r51.1(a)).
- **v4.10.0-r16.3(b):** Auf dem invarianten Dublett χ erhält R das Helizitätsvorzeichen, T und J_B kehren es um.
- **v4.10.0-r16.2(d):** Für allgemeine komplexe Amplituden ändert sich b_y unter Boosts.
- **v4.10.0-r18.1 (Warnung):** „Majorana heißt gleiche Helizitätsanteile“ wurde als Neutrino-Prinzip geprüft und ist durch Daten
  ausgeschlossen (R = 0 gegen beobachtet 0,0298). Das betrifft Neutrinos, nicht Felder, zeigt aber, dass gleiche Helizitätsanteile
  als Prinzip schon einmal gescheitert sind.

### Ergebnisse
1. **Die einzige Helizität, die alle drei Frame-Abbildungen erhalten, ist b_y = 0.** R lässt b_y fest, T und J_B kehren es um
   (nachgerechnet: 0,2622 ↦ 0,2622, −0,2622, −0,2622). Die Menge b_y = 0 ist also die einzige Helizitätsstufe, die kein Frame
   verschiebt.
2. **Für eine ebene Welle ist diese Neutralität beobachterunabhängig.** Beide Helizitätsanteile einer ebenen Welle erhalten unter
   einem Boost denselben Doppler-Faktor; eine linear polarisierte Welle bleibt linear (500 Boosts, |b_y| = 0), eine elliptische behält
   ihr b_y (Abweichung ≤ 3·10⁻¹⁶). Für allgemeine Amplituden in einem Punkt gilt das nicht (Median der Änderung 0,14), wie r16.2(d).

### Einordnung
- **Ja, eine ausgezeichnete Rolle gibt es:** Helizitätsneutral ist die frame-invariante Helizitätsstufe, und für Teilwellen ist sie
  Lorentz-invariant. Zusammen mit r21.11 heißt das: Eine Teilwelle, die kein Frame nach Helizität unterscheidet, erzeugt
  Nullaugenblicke an jedem Punkt des Raums.
- **Was das nicht ist:** Keine Begründung, dass eine solche Teilwelle vorliegt. Frame-Invarianz einer Menge ist kein Prinzip, das
  einen Zustand auswählt; dafür bräuchte es eine Setzung wie „der Zeuge trägt keine Helizität, die ein Frame unterscheidet“. Diese
  Setzung wird hier nicht gemacht.
- **Nicht verwechseln:** Die Scheibe von r04 (b_y = 0) beschreibt das augenblickliche reelle Feld (r05.2(a)); dort ist b_y immer 0.
  Die Neutralität hier betrifft die Amplituden einer Teilwelle (r05.2(b)), also die zeitgemittelte Helizität. Das sind zwei Ebenen.
- C5 bleibt offen; (B1) bleibt eine Lesart.
