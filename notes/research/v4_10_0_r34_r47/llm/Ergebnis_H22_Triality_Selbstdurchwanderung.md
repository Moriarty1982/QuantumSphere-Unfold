# Ergebnis H22: Die Triality-Form ist die Spin(8)-Triality, Farbe liegt in ihrer Fixgruppe, die Struktur hat keine ausgezeichnete Periode

Vorab-Notiz: `Vorab_Notiz_H22_Triality_Selbstdurchwanderung.md`, Commit ed74608 (2026-10-23 19:25 MESZ), vor der Rechnung.
Skript `k78_test_h22.py`, Ausgabe `k78_out.txt`. Kriterium unverändert; eine Nachkontrolle zu H22d nach der Auswertung ist im Skript
als solche gekennzeichnet.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H22a Triality-Form | **bestätigt** | Symmetrie-Algebra der Tripel dim 28; alle drei Projektionen auf so(8) bijektiv; die drei Platz-Darstellungen paarweise nicht äquivalent (Verflechtungsraum 0), jede irreduzibel. t = Re((xy)z) ist die Spin(8)-Triality-Form |
| H22b äußerer Automorphismus | **bestätigt** | τ bildet die Algebra auf sich ab und permutiert die drei Darstellungen zyklisch; da sie nicht äquivalent sind, ist τ äußer: die Triality selbst |
| H22c Fixgruppe | **bestätigt** | τ-feste Elemente (A, A, A): Dimension 14, gleich den Derivationen von 𝕆 (G₂); mit A e₇ = 0: Dimension 8 (SU(3)_c) |
| H22d vier Plätze (schwach) | **bestätigt**, aber **ohne Aussagekraft** | Keine einzelne Klammerung von Re(xyzw) ist zyklisch invariant. *Nachkontrolle:* Die fünf Klammerungen bilden zwei Klassen, die Verschiebung tauscht sie, und ihre Summe ist zyklisch invariant. Ein Verbot eines vierten Platzes folgt daraus nicht |
| H22e Perioden | **bestätigt** | τ, ρ, T, R erzeugen S₃ × D₄ (Ordnung 48); Elementordnungen {1, 2, 3, 4, 6, 12} (Anzahlen 1, 23, 2, 8, 10, 4) |

## Einordnung

1. **Die von H21 verlangte zweite Dreierstruktur existiert, und sie ist die Triality.** Die drei Plätze von 𝕆³ tragen die drei
   inäquivalenten 8-dimensionalen Darstellungen von Spin(8) (Vektor, zwei Spinoren). Die Verschiebung der Plätze ist der äußere
   Triality-Automorphismus. Was sie festlässt, ist G₂ ⊃ SU(3)_c.
   - In der Lesart: **Generation ist, was die Durchwanderung vertauscht; Farbe ist, was sie festlässt.** Farbe und Generation sind
     damit Fixgruppe und Bahn derselben Bewegung, nicht mehr dasselbe Objekt (vgl. H21).
   - Das passt zur Autorabsicht „die Triole ist eine andere Darstellung der Sphäre“: Die drei Plätze sind drei Darstellungen
     desselben 𝕆 ≅ ℝ⁸.
   - **Nicht** gezeigt ist, dass die drei Plätze physikalisch die Generationen *sind*.
2. **Genau drei?** Das starke Argument ist bekannte Mathematik: Spin(8) hat genau drei 8-dimensionale irreduzible Darstellungen,
   Out(Spin(8)) = S₃. H22a ist damit verträglich, beweist es aber nicht. Es verbietet einen vierten Platz mit einer *neuen*
   8-dimensionalen Darstellung, aber keine Wiederholung einer der drei. Der eigene Test H22d trägt nichts bei: Es gibt eine
   zyklisch invariante Form auf vier Plätzen. Test 2 der Bestandsaufnahme ist damit zur Hälfte beantwortet: Die Triality ist der
   Träger, das Verbot einer vierten Generation folgt aus der Struktur nicht zwingend.
3. **Perioden (Autorhinweis, nicht auf 3 festlegen):** Die Struktur aus Plätzen und ℂ-Faktor hat keine ausgezeichnete Periode.
   - Periode 2 haben ρ, T, J_B und der Orbit-Scan-Wechsel A ↔ B.
   - Periode 3 hat die Triality, Periode 4 die Dualitätsdrehung R.
   - Ihre Kombinationen haben die Perioden 6 und 12.
   - Lesart zur Selbstdurchwanderung: Welche Periode ein Readout sieht, ist eine Wahl der Untergruppe, also des Zooms bzw. des Frames.
4. **Mehrere Triolen im Korpus** (aus dem Text, nicht gerechnet). Das Wort „Triole“ benennt mindestens drei verschiedene Strukturen:
   - **Frame-Triole** M/P/T (Originalarbeit, `thm:spring`): ℤ₂ (M ↔ T) mit Fixpunkt P, Amplituden 1 : 1 : 3, keine 120°.
   - **Kern-Triole** K₁, K₂, K₃ mit 120° (ℤ₃): in 𝕆 eine Farbdrehung (H21).
   - **Platz-Triole** von 𝕆³: die Triality (H22).

   Die Verwechslungen aus r13, r34–r36 entstehen, wenn diese Triolen gleichgesetzt werden. Nach der Autorabsicht sind es
   Darstellungen derselben Sphäre auf verschiedenen Ebenen.
