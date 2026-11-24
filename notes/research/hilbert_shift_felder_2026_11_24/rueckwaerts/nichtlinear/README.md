# Nichtlineares Ursprungsfeld: Bleibt der Turm skalenfrei? (Erkundung k274, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Ein nichtlineares Ursprungsfeld (ψ̈ = −ω²ψ − λ|ψ|²ψ) führt eine **Skala** ein, nämlich die Kopplung von
Frequenz und Amplitude. Die **Struktur** des Turms ändert es aber nicht. Der Term ist G₂-äquivariant, die Kreisbahnen exp(uΩt)ψ₀ mit
Ω² = ω² + λ|ψ₀|² bleiben bis HS(3) exakte Lösungen, und ab HS(4) brechen sie wie im linearen Fall. Neu ist zweierlei. Bei HS(1)
präzedieren alle echten Ellipsen (Bertrand), nur die Linie (HS(0)) und der Kreis (eine Generation) bleiben geschlossen. Für λ < 0
gibt es eine Amplitudenschwelle ω/√|λ|, oberhalb derer die Rückstellung das Vorzeichen wechselt. Dort kippt das Feld in den
wachsenden, also gespaltenen Fall von k272.

Auftrag (Autor über den Koordinator, 24.11.2026): als zweiter Folgeschritt das nichtlineare Ursprungsfeld. **Erkundung, nicht
blind:** Duffing-Periode (elliptisches Integral), Satz von Bertrand und Apsidenpräzession sind Lehrbuch. Skripte **k274, k274b**.

Werkzeuge: Python (scipy, solve_ivp mit rtol 10⁻¹¹) für Bahnen, Präzession, Residuen und Äquivarianz (k274); Wolfram Language exakt
für die Duffing-Periode (k274b, Übereinstimmung auf 4 Stellen). Qiskit nicht eingesetzt.

## Vorwissen geprüft
k272 (Vorzeichen g, gespaltene Oktonionen), k251 (Skala frei), k253 (Regel ψ̇ = uωψ, L_u² ≠ −1 ab n = 4), k248 (Drei-Mulden-Schwelle,
`licht_vermittler_zeit_2026_11_24/`), I4 (Kondensation mit λ < 0 im T-Bild, gescheitert unter den geltenden Lesarten).

## Ergebnisse
1. **HS(0) (k274 A, k274b):** Bei ω = 1 ist T(A) = 4 K(m)/√(1 + λA²) mit m = λA²/(2(1 + λA²)), für kleine Amplituden
   T ≈ 2π(1 − 3λA²/8). λ = +0,5 verkürzt die Periode (6,27 → 4,93 für A = 0,1 → 1,3), λ = −0,5 verlängert sie (6,30 → 11,18).
   Die Bahn bleibt reell, also a = b und zeitumkehrinvariant. Nur die Frequenz hängt von der Amplitude ab.
2. **Schwelle für λ < 0:** Die Rückstellkraft −ω²ψ − λψ³ wechselt bei |ψ| = ω/√|λ| das Vorzeichen (1,414 für λ = −0,5). Darüber wächst
   das Feld. Mit k272 heißt das: Das Ursprungsfeld ist unterhalb der Schwelle der kompakte Fall (g = −1), oberhalb der gespaltene
   (g = +1). Die Struktur des Turms wird damit **amplitudenabhängig**. Für λ > 0 bleibt jede Amplitude gebunden.
3. **HS(1) (k274 B):** Die Ladung L bleibt erhalten (Drift ≤ 6·10⁻¹¹, Zentralkraft). Linie und Kreis bleiben geschlossen, jede echte
   Ellipse präzediert: je Halbumlauf −0,101 rad (λ = +0,3, a = 1, b = 0,5) bzw. +0,532 rad (λ = −0,3). Linear ist es 0. Der Sinn folgt
   dem Umlaufsinn, denn a ↔ b kehrt L und Präzession gemeinsam um. **Einen Drehsinn wählt die Nichtlinearität nicht** (wie k250). Neu
   ist, dass HS(1) eine dynamische Restdrehung bekommt. Das ist keine geometrische Phase, die erste Holonomie bleibt bei HS(2) (k253).
   Rückwärts gelesen: Nur die beiden Konfigurationen, die k270 als Grenzfälle auszeichnete, bleiben geschlossen, nämlich a = b
   (HS(0), beide C-Bilder gleich) und b = 0 (eine Generation, ein C-Bild).
4. **Kreisbahnen bis HS(3) exakt (k274 C):** exp(uΩt)ψ₀ mit Ω² = ω² + λ|ψ₀|² hat das Residuum 2·10⁻¹⁴, 5·10⁻¹³ und 2·10⁻¹³ für n = 1, 2, 3,
   aber 73 für n = 4. Die Nichtlinearität verschiebt die Grenze nicht: Sie liegt weiter bei 𝕆.
5. **Äquivarianz (k274 D):** Für g = exp(tD) mit einer Derivation D von 𝕆 gilt |gψ| = |ψ| (Abweichung 0) und g(|ψ|²ψ) = |gψ|²gψ
   (4·10⁻¹⁵). Symmetrien, Stabilisatoren (G₂, SU(3)) und Nullteiler sind dieselben wie im linearen Fall.

## Bewertung
- **Skalenfrei? Nein, aber nur in der Zeit.** λ koppelt Amplitude und Frequenz, mit der dimensionslosen Größe λA²/ω². Alles
  Algebraische aus k270–k273 bleibt (N_c = 3, Drehsinn als Konvention, Vorzeichenregel, Generationsfrage).
- **Neu ist eine Ordnungsrolle der Amplitude.** Für λ < 0 entscheidet die Amplitude, ob das Feld im kompakten oder im gespaltenen
  Fall liegt. Das ist eine mögliche dynamische Form der M/T-Grenze und hängt mit I4 zusammen (Schwelle, Kondensation). Das ist Lesart
  und nicht gerechnet. Für einen Vergleich zwischen Frames fehlt die deklarierte Transportregel (Konvention F).
- **Die Präzession bei HS(1)** gibt den Ellipsen eine dynamische Restdrehung. Linie und Kreis sind die einzigen geschlossenen Bahnen,
  also genau die Konfigurationen, die rückwärts gebraucht werden. Dass die Dynamik genau diese beiden auszeichnet, ist
  bemerkenswert, folgt aber direkt aus Bertrand.
- Keine Vorhersage. OP1/OP3/OP5 offen, kein Guard berührt.

## Mögliche nächste Schritte
- Schwelle als Übergang: Bei λ < 0 kippt das Feld an der Amplitude ω/√|λ|. Wie verhält sich die HS(1)-Ladung beim Überschreiten
  (Anschluss an k248, Drei-Mulden-Schwelle)?
- Präzession als Masse: Die Präzessionsrate ist eine Frequenzdifferenz zwischen Radial- und Winkelbewegung. Ob sie sich als
  Massenaufspaltung der Kreisanteile lesen lässt, ist offen und bräuchte eine Vorab-Notiz.

## Dateien
`../k274_nichtlinear.py` (`../k274_out.txt`), `../k274b_duffing.wl` (`../k274b_out.txt`, Wolfram).
