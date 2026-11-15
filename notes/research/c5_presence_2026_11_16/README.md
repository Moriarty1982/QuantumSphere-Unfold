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
