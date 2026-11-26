# Ergebnis H160: Die iterierten Auslesen laufen nicht auf eine Kreisbahn zu, sie laufen in den Kern

**Stand:** 2026-11-26. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H160_Iterierte_Proben_Kreisbahn.md` (Commit b29cc1c, vor dem ersten Lauf).
**Teilweise nicht blind** (Überschlag in der Vorab-Notiz offengelegt). Skripte: `k351_test_h160.py` (numpy/scipy), `k351b_gegenprobe.wl` (Wolfram, NDSolve und
exakt), `k351c_nachtrag_kollapsform.py` (**nachträglich**, ohne Vorab-Kriterium). Ausgaben: `k351_out.txt`, `k351b_out.txt`, `k351c_out.txt`.
Werkzeugwahl: Bahniteration in Python; Wolfram als unabhängige Gegenprobe der Bahnstücke und für die exakten Identitäten. Kein Qiskit (keine Schaltung),
kein HDL/MMA-Vergleich (kein RUN_TAPE-Ablauf). Kein Guard berührt.

## Frage
Idee des Autors (26.11.2026): Zwei Proben am Kern vorbeischicken, am Punkt größter Annäherung anhalten, von dort je eine Probe zum anderen Punkt schicken und so
fortfahren. Vermutung: Die addierten Auslesen erzeugen irgendwann eine stabile Kreisbahn um den Kern.

## Urteil nach den vorab festgelegten Kriterien
| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a Konvergenz auf r∞ > 0 | trägt teilweise | **widerlegt** (Vorhersage falsch) |
| K-b Kreisbahn (e∞ < 10⁻³) | widerlegt | **widerlegt** |
| K-c Anziehung | widerlegt | **widerlegt** |
| Gesamt | trägt teilweise | **widerlegt** |

Meine Vorhersage zu K-a war zu günstig: Ich hatte erwartet, dass in mindestens einer Regel die Mehrheit der Läufe bei r∞ > 0 stehen bleibt. Das geschieht in keiner.

## Zahlen (k351, je 400 Schritte)
| Regel | Läufe | Kollaps | konvergent | anderes |
|---|---|---|---|---|
| E (Energie der Probe bleibt, Hyperbeln) | 48 | 18 (37,5 %) | 7 (14,6 %, alle mit r∞ ≈ 0) | 23 |
| V (feste Geschwindigkeit v₀) | 144 | 140 (97,2 %) | 1 (r∞ = 1,065, e = 3,26) | 3 |
| B (gebunden, feste Energie) | 200 | 200 (100 %) | 0 | 0 |

- Kontrolle der Bahnformel gegen direkte Integration: Abweichung etwa 4·10⁻¹³ (Python), 10⁻¹⁹ (Wolfram, vier Fälle, `k351b`).
- K-b: Es gibt keinen konvergenten Lauf mit Kreisbahn. Der eine konvergente Lauf der Regel V endet auf einer Hyperbel (e = 3,26).
- K-c: Regel E kehrt nach der Störung nur zu r ≈ 0 zurück; in V und B gibt es nichts, wohin zurückzukehren wäre.
- Schwarzschild-Variante (Erkundung, m = 0,01 und 0,05): 40 von 40 Läufen enden im Einfang. Die relativistische Korrektur verstärkt den Sturz.
- Harter Kern mit Radius 0,5 (Erkundung): 40 von 40 Läufen enden mit beiden Auslesepunkten **auf der Oberfläche**. Der Winkel zwischen ihnen hängt vom Start ab
  (0,28° bis 177°, Median 81°). Die Auslesen bleiben also am Kern stehen, aber nicht gegenüber und nicht auf einer Bahn.

## Warum (hergeleitet)
1. Der Punkt größter Annäherung liegt nie weiter außen als der Startpunkt. Die Radien können nur fallen oder stehen bleiben.
2. Stehen bleibt der Radius nur bei tangentialem Start. Die Verbindungslinie zweier verschiedener Punkte kann nicht auf beiden Radien senkrecht stehen:
   (P₂ − P₁)·P₁ + (P₁ − P₂)·P₂ = −|P₁ − P₂|² (exakt, `k351b` Punkt 3). Ein Zustand mit r∞ > 0 verlangt also P₁ = P₂, und dort ist die Zielrichtung nicht mehr erklärt.
3. Die Regel „ziele auf den anderen Punkt“ nimmt jeder Probe Drehimpuls, solange der andere Punkt nicht genau quer liegt. Eine Kreisbahn braucht Drehimpuls.
   Das Verfahren ist deshalb eine Bremse, kein Stabilisator.

## Nachträglich gefunden (k351c, nach Kenntnis des Ergebnisses; kein Test)
- **Winkel bleibt, Radius schrumpft geometrisch.** Im skalenfreien Grenzfall nahe am Kern (v² = 2/r, Parabeln) und für gleiche Radien gilt exakt:
  P₁′ = cos²(Δ/2)·P₂ und P₂′ = cos²(Δ/2)·P₁, mit Δ dem Winkel zwischen den zwei Auslesepunkten. Die Punkte tauschen ihre Strahlen, der Winkel Δ bleibt erhalten,
  der Radius wird je Schritt mit cos²(Δ/2) multipliziert (Wolfram exakt, `k351b` Punkt 2; numerisch 179 Winkel, Rest 10⁻¹⁴).
  Für ungleiche Radien gilt dieses einfache Gesetz **nicht** (Abweichung im Median 57 %, `k351c` Abschnitt 1); dort friert nur der Winkel ein.
- **Kein gemeinsamer Endwinkel.** In Regel B friert Δ ein (Änderung zuletzt etwa 10⁻⁹ Grad), aber bei Werten zwischen 1,2° und 177,6°, je nach Start.
- **Die „Kreisbahn“ als Grenzfall.** cos²(Δ/2) → 1 für Δ → 0: Liegen die zwei Punkte fast aufeinander, schrumpft der Radius fast nicht mehr.
  Im symmetrischen Lauf der Regel E geschieht genau das, aber beides zugleich: r·n → 0,4997 und Δ²·n → 3,997 (Radius ∼ 1/(2n), Winkel ∼ 2/√n). Die Punkte laufen
  zusammen **und** nach innen; der Kollaps wird langsam (algebraisch statt geometrisch), bleibt aber ein Kollaps.
- Neu eingeteilt: Regel E 19 Läufe noch in Bewegung, 18 Kollaps, 9 laufen gegen null, 2 zusammengelaufen bei r ≈ 10⁻⁶. Regel V 140 Kollaps, 4 zusammengelaufen
  bei r∞ ≈ 1,07 bis 1,15 (alle v₀ = 2, b₁ = 4, Hyperbeln). Diese vier sind die einzigen Endzustände mit r∞ > 0, und sie sind keine Kreisbahnen und bilden ein Kontinuum.

## Was von der Idee bleibt
- Als Aussage über Bahnen: nichts. Ohne eine Regel, die Drehimpuls erhält oder zuführt, gibt es keinen Kreis.
- Als Aussage über die Auslesen: zwei Dinge. Erstens friert der **Winkel** zwischen den zwei Auslesen ein, während die Skala verschwindet; was übrig bleibt, ist
  eine Richtung, kein Radius. Zweitens hält ein Kern mit Ausdehnung die Auslesen auf seiner Oberfläche fest, mit einem Winkel, der vom Start abhängt. Das ist die
  Ausgangslage von H161 (zwei Punkte auf einer Kugel, die nicht gegenüberliegen).
- Was eine Kreisbahn liefern könnte (nicht gerechnet, Vorschlag): eine Zielregel mit festem Vorhaltewinkel statt gerader Zielrichtung. Das wäre eine zusätzliche
  Setzung und ein neuer Test.

## Grenzen
Übersetzung gesetzt (gerade Zielrichtung, Punktmasse, drei Geschwindigkeitsregeln, Ebene). Klassische Bahnen, keine Wellen. Keine Größe des Companion geht ein;
eine Zuordnung zu Kern, Frames oder HC wird nicht behauptet. Die Schwarzschild-Variante benutzt die flache Zielgeometrie in Schwarzschild-Koordinaten (Setzung).
OP1 bis OP5 bleiben offen.
