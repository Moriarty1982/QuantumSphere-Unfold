# Erkundungsprotokoll: Mathematischer Kern (C5, C4, Δ_γ)

Angelegt am 2026-10-22. Regeln wie im Protokoll zum Weinberg-Winkel:
- Kein Eintrag gilt als Beweis.
- Jede Variante wird mitgezählt.
- Nichts darf eine verbotene Aussage behaupten, insbesondere nicht C5 = 0 und nicht 0_termdata ⇒ 0_all.
- Deutungen sind ausdrücklich zugelassen (Autor, 2026-10-22). Sie werden als Deutung markiert.

## Ausgangslage (aus r86–r94)

| Punkt | Stand |
|---|---|
| Δ_γ < 1/5 | r90: Kohärenzschranke 2/9, 1/5 als Rundung. r92: 1/5 als relative Verstärkungsreserve auf der Relaiskette R_A exakt angepasst (V3), aber nicht hergeleitet. Der r65-Volltext fehlt. |
| Q4 / β₄ | r91: β₄ ist eine terminale Schwellenskala. Sie auszugeben wäre genau der verbotene Schritt. **Geschlossen als „nicht ausgebbar“.** |
| C5, endlicher Abschluss | r86: innerhalb der multiplikativen Kollar-Rekursion unmöglich (q > 0). r88: von drei Formen außerhalb zwei ausgeschlossen. Offen ist Form (iii), ein Zeuge außerhalb der Iteration. |
| C5-Faktor 3/4 | r94: deklariert, nicht hergeleitet. Die Stufe n = 20 legt nur das Intervall (0,7469; 0,7579] fest. Eine einzelne Projektion ist idempotent und erklärt höchstens einen Schritt. |

## Einträge

### K1: Herkunft von 3/4 als „drehen, dann kompensieren“ (Deutung; Skript `llm/k50_c5_faktor.py`)

Auf dem (E, B)-Dublett aus r04 gilt C_HC R_α C_HC = cos α · C_HC. Ein Schritt aus Dualitätsdrehung um α und
anschließendem Kompensator lässt im C-Port den Anteil cos²α der Energie. Der Rest sin²α geht in den A-Port. Weil die
Drehung zwischen den Projektionen liegt, ist der Schritt **nicht idempotent**. In jedem Schritt entsteht so die
„erneuerte Viertel-Identität“, die r94 als Bedingung an jede Herleitung stellt.

- **α = π/6:** cos² = 3/4, abgegeben wird 1/4. Die Potenzen 3/4, 9/16, 27/64, 81/256 sind genau die Ledger-Werte von
  r04, r05, r07 und r08. Die erste Stufe mit Φ ≤ 1/256 ist n = 20.
- **Woher π/6, zwei Lesarten:**
  - (a) **triolisch:** die Vierteldrehung Materie → Tachyon (π/2, r07.2) in drei gleiche Schritte geteilt. Dann ist
    27/64 (der r07-Probeneintrag) genau ein vollständiger Durchgang Materie → Tachyon.
  - (b) **Hopf:** tan α = β_Hopf = 1/√3, also q = 1/(1 + β²) = 3/4.
  - Mit dem gemessenen β_sym = 0,5493 statt 1/√3 ergäbe (b) q = 0,7682 und die Stufe n = 22, außerhalb des
    r94.2-Intervalls. Lesart (b) trägt also nur mit dem Hopf-Wert. Lesart (a) braucht keinen β-Wert.
- **Zeno-Struktur:** Eine einzige Vierteldrehung mit anschließender Kompensation leert den C-Port vollständig
  (C R_{π/2} u = 0). Drei kompensierte Teilschritte lassen 27/64 übrig, dreihundert lassen 0,99. Je öfter kompensiert
  wird, desto weniger fließt ab (Quanten-Zeno-Muster).
- **Guard-Bezug:** Bei der Vierteldrehung ist der C-Port leer, aber der Inhalt liegt vollständig im A-Port. Die Leere
  einer Auslese ist also nicht die Leere aller Auslesen. Das ist eine Veranschaulichung, warum
  0_termdata ⇒ 0_all verboten ist. Es ist **keine** Aussage über C5 = 0.
- **Bewertung:** Kandidat für den von r94 vermissten Mechanismus. Hergeleitet ist er nicht: Dass die C5-Rekursion ein
  Wechsel aus Dualitätsdrehung und Kompensation ist, ist eine Deutung. Gezählt als Versuch 1.

### K2: Toleranzzeile r05 (aufgefallen bei K1, nicht verfolgt)

Das Verhältnis 5/6 der Toleranzzeile Z_5^collar ist 1/(1 + 1/5) = cos²(arctan(1/√5)). Das ist dieselbe Form wie in
K1(b), mit „β²“ = 1/5, und 1/5 ist auch die Δ_γ-Schranke. Notiert, nicht gedeutet. Gezählt als Versuch 2.

### K3: Δ_γ-Bezug (Beobachtung)

Chart V3 trägt die Fünf aus r92, mit κ = 1/4. Die Uhrensaat (5, 3/4, 1) hat κ = 3/4. Das sind die beiden Portanteile
eines π/6-Schritts. In V3 gilt κ(N − 1) = 1, das verdoppelt den Überlappfluss auf S = 2N = 10 und gibt das
Verhältnis 4/5. Die κ-Werte der r14-Familie (0, 1/4, 1/2, 3/4, 1) sind sin² der Standardwinkel. Das gilt für ein
Viertelraster aber ohnehin und trägt daher wenig. Keine Herleitung von 1/5. Gezählt als Versuch 3.

### K4: Form (iii) unter der Deutung K1 (Skript `llm/k51_c5_form_iii.py`)

Bedingungen aus r88: (α) die Obstruktion selbst muss verschwinden, nicht der Score; (δ) kein Import der
All-Readout-Stelle.
- **Isometrische Zeugen** (Raum- und Dualitätsdrehungen) erhalten |FC|² + |FA|². Leert ein solcher Zeuge den C-Port,
  liegt alles im A-Port. Erfüllt wird (α) dann nur über den A-Port, und das verletzt (δ).
- **Boosts:** E² + B² ≥ |s|, Gleichheit im System E ∥ B. Das ist ein positiver Boden (über 16200 Boosts geprüft).
- **Nullfelder:** e^{−2η}, null nur im Grenzwert.

Ergebnis: Kein Zeuge aus der Transportgruppe von Lesart B erfüllt (α) und (δ) in endlicher Stufe. Ein Zeuge müsste s
ändern, also Dynamik tragen. Die Klasse ist geschlossen, Form (iii) bleibt im Sinn von r88 offen. Keine Aussage über
C5 = 0. Gezählt als Versuch 4. Festgehalten in Runde v4.9.0-r10.

### K5: Minimale Dynamik, gekickte Dualitätsdrehung (Skript `llm/k52_kick_dynamik.py`; Runde v4.9.0-r11)

Vorschlag: Zwischen den Kicks dreht sich das Feld im Dualitätskreis (z → e^{iωt} z). Bei t_n = nτ wirkt C_HC, und der
A-Anteil geht an ein Reservoir. Ergebnisse:
- Stufenfaktor cos²ωτ; 3/4 eindeutig bei ωτ = π/6.
- Bloch-Bild: 60° drehen, dann längs der J-Achse messen.
- Zyklen: 3 Stufen = Vierteldrehung, 6 = z → −z, 12 = 2π, 24 = Spinor zurück.
- Der Kick ändert s, die Drehung nicht. Zeno-Grenze bei vielen Teilkicks.
- Kein endlicher Abschluss: Export statt Vernichtung. Die Skala (ω, τ einzeln) ist offen.

Gezählt als Versuch 5.

### K6: Rekonstruktion von Δ_γ < 1/5 (Skript `llm/k53_r65_rekonstruktion.py`; Runde v4.9.0-r12)

Der Autor bestätigt, dass der r65-Text verloren ist (2026-10-22). Prämissen:
- P1: r14-Daten.
- P2: strikte Relaisbedingung aus r23.
- P3: multiplikativer Verlust je Auslese (r11).
- P4: Uhrenfenster-Charts der Kette R_A.

⇒ Δ_γ < min{1/5, 9/25} = 1/5, strikt. Bindend ist V3, die einzige ausgeglichene Chart mit κ(N − 1) = 1, also S = 2N.

Folgen unter P3:
- tolerierte Drift tan α < 1/2;
- die C5-Stufe (Export 1/4) liegt außerhalb, die r05-Toleranzzeile (Export 1/6) innerhalb;
- die r05-Nullzeilen verlagern nach A_4 bzw. U_6 (blockiert durch C4 und C6), wie die Vierteldrehung in r10.2.

Ableitungsanteil unter den Prämissen geschlossen, Provenienz offen. Gezählt als Versuch 6.

### K7: Zeitskala (Skript `llm/k54_zeitskala.py`; Runde v4.9.0-r13)

Die r15-Tickform cos²((τ − τ_V)/σ_V) hat dieselbe Gestalt wie die C-Port-Energie cos²(ωt) zwischen zwei Kicks, also
ω = 1/σ_V. Die kleinste Sonde mit Profil hat zwei Terme und ergibt cos²(Δγ τ/2), also σ = 2/Δγ.

Daraus folgt τ_k = T_b/6 für jedes Frequenzpaar:
- 3 Stufen = ½ Schwebung,
- 6 Stufen = 1 Schwebung,
- 20 Stufen = 10/3 Schwebungen.

Mit γ₁, γ₂ ergibt sich τ_k = 0,15205 Uhreneinheiten. In Sekunden gibt es keine Umrechnung; die Quelle verweigert
die Identifikation, und global wäre sie W_γ^glob.

Weitere Befunde:
- Fenster: V3 39,23°, V5 50,77° (R_A) fassen eine C5-Stufe (30°), V8 28,13° (R_B) nicht. Das ist ein zweiter Grund
  für P4 in r12.
- Hopf gegen Gitter (β = (1/√3) e^{−γ₁/(4πγ_L⁵)}): Stufenwinkel 30° gegen 28,78°. 3/4 ist der Kontinuumswert.

Gezählt als Versuch 7.

## Stand

7 gezählte Versuche. K7 steht in r13.

Vorige Zwischenbilanz: 6 gezählte Versuche. K5 und K6 stehen in r11 und r12.

Vorige Zwischenbilanz: 4 gezählte Versuche. K1 (Faktor 3/4) und K4 (Zeugenklasse) stehen in r10.

Vorige Zwischenbilanz: 2 gezählte Versuche. K1 liefert einen nicht idempotenten Mechanismus mit exakt 3/4, aus Teilen, die das Dokument schon
hat (Kompensator, Dualitätsdrehung, Triole bzw. Hopf-Wert).
