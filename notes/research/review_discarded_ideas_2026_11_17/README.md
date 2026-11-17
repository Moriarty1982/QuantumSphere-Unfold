# Sichtung: Verworfene Ideen, die an einer später berichtigten Grundannahme hingen (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „Suche bitte das ganze Paper nach Ideen ab, die ich evtl. früher verworfen habe, die aber evtl. nur wegen einer
falschen Grundannahme verworfen wurden.“ Skript `recheck.py`, Ausgabe `run/recheck_stdout.txt`. Keine H-Nummer.

## Vorgehen
1. **Berichtigte Grundannahmen gesammelt** (der Companion sagt selbst, dass eine frühere Aussage falsch war oder fällt): Stichwortsuche in allen
   Teilen unter `sources/research/parts/` (Correction, wrong, withdrawn) und in den Notizen, ergänzt um die Lesart-Korrekturen der letzten Tage.
2. **Verworfene Ideen gesammelt:** alle 35 widerlegten H-Tests (`Ergebnis_H*.md`), die zurückgezogenen Bedingungen im Rundentext (P2, (S2)-Motivation)
   und die zurückgestellten Ideen I1–I4.
3. **Abgleich:** Für jede Verwerfung die tragende Annahme bestimmt und mit Schritt 1 verglichen; wo es eine Überschneidung gab, mit der berichtigten
   Annahme nachgerechnet oder der Stand geprüft.

## Berichtigte Grundannahmen (Auswahl, mit Quelle)

| Nr. | Frühere Annahme | Berichtigt durch |
|---|---|---|
| B1 | z ↦ iz sei die Wick-Drehung | v4.10.0-r07 (z ↦ iz ist die Dualität; Boosts bleiben reell) |
| B2 | Tachyon-Abbildung und Zeitumkehr verwechselt | v4.9.0-r51, r81 |
| B3 | Rollen von β² bei Λ und Ω_M vertauscht | v4.9.0-r67 |
| B4 | historische Λ-Aufhebung als Pflicht des Kerns | v4.10.0-r05, r11.2 (ausgesetzt, Autor 6.11.) |
| B5 | Frame-Lesart von v4.9.0-r38 | v4.10.0-r15 |
| B6 | Frames ohne Typisierung, Geschwindigkeit je Frame 1/√3 | Konvention F (r22), M bei β_sym = tanh η (r63, r68) |
| B7 | P liegt zwischen M und T | Nachtrag 17.11.: nur in der Koordinate x; in Rapidität gemeinsamer Endpunkt |
| B8 | (A): Frame-Abbildungen wirken als dieselbe SU(2) wie die Drehungen | `op1_s1_check_2026_11_16/`: zwei verschiedene SU(2) |
| B9 | Brücke P2 über Unruh-Temperatur | v4.10.0-r10.2 |
| B10 | eine Umkehrwalze; Spiegelung bildet mit der Triole S₃ | `op3_topology_core_2026_11_16/` (mehrere Walzen; Viertelraster D₄ enthält die Kleinsche Gruppe der Frame-Abbildungen) |

## Ergebnis des Abgleichs

### A. Echter Kandidat: H6 (TM1-Lift), Kriterium C
H6 (20.10.) sollte entscheiden, was den TM1-Lift vom Lift mit θ₁₃ = 0 unterscheidet. **Hauptkriterium A** war „die Spiegelung bildet mit der Triole
die kleinste gemeinsame Struktur S₃“; es sprach gegen TM1. **Kriterium C** (die erzeugte Gruppe hat Ordnung 24) sprach für TM1, zählte aber nur als
Hinweis, weil kein modellinterner Grund dafür vorlag. Nachtrag k24: TM1 ⇔ die Gruppe aus Triole und Restspiegelung **enthält die vierelementige
Vorzeichen-Symmetrie der Oktonionen** (24 = 4 · 6).
- **Die tragende Annahme war Minimalität** („kleinste gemeinsame Struktur“). Sie ist empirisch schon in H6 selbst als falsch markiert (θ₁₃ = 0 ist seit
  2012 ausgeschlossen), aber es fehlte ein Grund für die Alternative.
- **Neu seit 16.11. (B10):** Der Bestand hat jetzt eine modellinterne vierelementige Gruppe, die Kleinsche Gruppe der Frame-Abbildungen (R, T, J_B als
  π-Drehungen um drei senkrechte Achsen, r16.7), und der Befund, dass die Frame-Abbildungen im Viertelraster (D₄) liegen, nicht im Triolenraster (D₃).
  Kleinsche Gruppe plus Dreierzyklus erzeugen A₄, mit einer Spiegelung S₄; das ist genau die Ordnung 24 von Kriterium C.
- **Offen und prüfbar:** Ist die Vorzeichen-Symmetrie aus H6 (auf den Oktonionen-Einheiten) das Bild der Frame-Abbildungen (auf χ)? Wenn ja, hat
  Kriterium C seinen modellinternen Grund, und TM1 folgt aus „Triole + Frame-Abbildungen“, nicht aus einer Wahl. Nicht blind gegenüber TM1; als
  Prüfung nur mit Vorab-Notiz, die vorher festlegt, welche Abbildung zwischen beiden Darstellungen zählt.

### B. Nachgerechnet, bleibt widerlegt
- **H13 (Wigner-Holonomie):** Damals Geschwindigkeit 1/√3 je Frame (B6). Mit der Geschwindigkeit des Frames M (β_sym = 0,5494): Wigner-Winkel 25,48°
  statt 28,56°, cos δ = 0,9027, z = −4,9 statt −7,9. **Weiter widerlegt.** f(+) bräuchte v = 0,486; das ist kein Wert des Bestands.
- **H73 (Zustandsgleichung der Bezugszustände):** Damals Gewichte des Materie-Frames (Frage B3/B6). Mit vertauschten Gewichten (Tachyon-Frame):
  w = −1,104, |w + 1| = 0,104 > 0,05. **Weiter widerlegt;** exakt −1 nur bei β² = ⅓ (nachträglich, schon in H73 vermerkt).

### C. Verwerfung hing an einer Testannahme, nicht an der Physik
- **H62, H63 (Lorentz-Symmetrie des Symbols):** Die Ergebnisnotiz H63 hält selbst fest, dass Invarianztests bei festem Hintergrund kein kovariantes von
  einem nicht kovarianten Modell unterscheiden (Takabayasi: Stabilisator eines generischen Spinors trivial). „Das Modell ist nicht lorentzkovariant“
  ist daraus **nicht** gefolgert und sollte auch nicht so gelesen werden; die Frage ist offen, nicht verneint.
- **H61 (Spin der sechs Moden):** verworfen unter der „naiven“ Zuordnung I₃ ⊗ Spin ½, die die Notiz selbst für vermutlich falsch hält. Die verlangte
  Nacharbeit (Stabilisator des Symbols bestimmen, dann Spin ablesen) steht im Repo nicht; die Frage ist offen.

### D. Schwacher Kandidat: P2 (Energiebedingung der Zählregel)
P2 wurde in r10.2 zurückgenommen, weil ein Beobachter in T dasselbe thermische Vakuum sieht (über r07.2, also B1 schon berichtigt). Die Arbeiten vom
17.11. geben die Zählregeln als Übergangsfrequenzen in Einheiten der Hawking-Temperatur (ω_T = ln 2 · T_H, ω_M = γ_L ln 2 · T_H,
`op1_readout_frequency_2026_11_17/`). Das ist der Sache nach eine Energiebedingung, nur nicht über die Unruh-Brücke von r09.2. Eine Rücknahme der
Rücknahme folgt daraus nicht; es ist ein Hinweis, P2 in dieser Form neu zu formulieren.

### E. Geprüft, keine Abhängigkeit von einer berichtigten Annahme
H1, H5, H14–H18, H34, H38, H40, H43, H44, H48–H50, H68, H83, H95, H97, H101, H103–H111 (Gründe jeweils rechnerisch oder an Daten, nicht an einer der
Annahmen B1–B10). **H85** wurde wegen vertauschter Rollen von C und D verworfen, aber schon als H86 aufgegriffen. **I3** (Λ als Folge der dunklen
Materie) ist mit festen Gewichten und dynamisch (H95) gescheitert; die Gründe (Positivität, Feinabstimmung) hängen nicht an B1–B4.

## Ergebnis in einem Satz
Von den verworfenen Ideen hängt nur eine erkennbar an einer inzwischen überholten Grundannahme: **H6, Kriterium C** (TM1 aus Triole plus
Vorzeichen-Symmetrie), weil der Bestand seit 16.11. eine modellinterne Vierergruppe hat; H13 und H73 bleiben nachgerechnet widerlegt, H61–H63 sind offen
statt verneint, P2 verdient eine Neufassung. OP1–OP5, C5, C6/T2 offen.

## Nachtrag (17.11.2026): Kandidat H6 geprüft, trägt nicht
Beim Aufsetzen der Vorab-Notiz zeigte sich, dass die Gleichsetzung der Vorzeichen-Symmetrie mit den Frame-Abbildungen analytisch ausgeschlossen ist (die
Vorzeichen-Elemente halten span(1, e₇) fest, auf das die Frame-Abbildungen unter φ wirken), ebenso mit der Familien-su(2) (sie vertauschen mit ihr).
Die Behauptung in Abschnitt A, die Kleinsche Gruppe der Frame-Abbildungen liefere den fehlenden Grund, ist damit **zurückgenommen**: Es ist dasselbe
Muster (Vierergruppe plus Dreierzyklus, A₄/S₄) auf zwei verschiedenen Räumen, keine Gleichsetzung. Einzelheiten:
`../op4_h6_criterion_c_2026_11_17/`. Die Sichtung hat damit keinen verworfenen Gedanken gefunden, der an einer überholten Annahme hängt und jetzt trägt.
