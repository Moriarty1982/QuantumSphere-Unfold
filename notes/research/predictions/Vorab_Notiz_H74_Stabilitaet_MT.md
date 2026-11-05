# Vorab-Notiz H74: Ist die exakte M–T-Aufhebung der Vakuumenergie stabil gegen eine Kopplung der Sektoren?

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert, nicht blind (Kernaussage analytisch vorab gesehen).**

## Vorwissen geprüft
- `Wirkung_W2_Higgs.md`: Die M–T-Paarung mit F3-Vorzeichen hebt die Higgs-Vakuumenergie bei Photon-Gewichten exakt auf; dafür muss das Tachyonbild dasselbe Spektrum haben wie die Materie.
- H69/H70: exakte Aufhebung von Strom und Energie im Paar (masselos, entkoppelt).
- `analysis/OP5_Neutral_Pair_Dynamics_Result.md`: Ein Frame-Vorzeichen ist keine Quanten-Gewichtung; Stabilität der Kompensation offen.
- Literatur (Vorwissen): Kaplan–Sundrum 2005 (Energieparität, Geisterkopie des Standardmodells), Pais–Uhlenbeck-Oszillator (Stabilität nur bei verschiedenen Frequenzen bzw. in Inseln).

## Analytisch vorab gesehen
Für L = ½φ̇² − ½ω₁²φ² − ½χ̇² + ½ω₂²χ² + εφχ (χ mit F3-Vorzeichen, Gesamt-Lagrangedichte gespiegelt) gilt ẍ = −Mx mit M = [[ω₁², −ε], [ε, ω₂²]] und den Eigenwerten Ω² = (ω₁² + ω₂²)/2 ± √((ω₁² − ω₂²)²/4 − ε²). Komplexe Ω, also exponentielles Wachstum, für ε > |ω₁² − ω₂²|/2. Zum Vergleich: zwei normale Schwinger haben M = [[ω₁², −ε], [−ε, ω₂²]], immer reell.

## Messung (k188)
Numerische Integration (RK4, Schritt 1e-3, Zeit 0–400) je Fall, Anfangsauslenkung 1e-3; gemessen das maximale |φ| relativ zum Anfang. Für jede Feldmode k gilt dasselbe mit ω(k).

## Hypothese H74
- **H74a:** Bei gleichen Frequenzen (ω₁ = ω₂ = 1, exakte Aufhebung) wächst die Lösung für jedes ε ∈ {1e-3, 1e-2, 1e-1} exponentiell, mit Rate ≈ ε/(2ω).
- **H74b:** Bei Verstimmung (ω₂² = 1,1) ist sie für ε < 0,05 beschränkt und wächst für ε > 0,05.
- **H74c (Kontrolle):** Zwei normale Schwinger bleiben für alle ε beschränkt.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | a: Wachstum ≥ 10³ und gemessene Rate innerhalb 10 % von ε/(2ω); b: beschränkt (≤ 10) bzw. wachsend (≥ 10³) wie angegeben; c: beschränkt |
| widerlegt | ein Fall verhält sich umgekehrt |
| ungültig | Energieerhaltung der Gesamtenergie E_φ − E_χ + Kopplung relativ > 1e-6 |

## Grenzen
Klassisch, linear gekoppelt (Konnektor- bzw. Yukawa-artige Mischung). Eine Kopplung nur über die Gravitation ist nichtlinear und hier nicht erfasst. Auf Quantenebene kommt der bekannte Vakuumzerfall in Teilchenpaare positiver und negativer Energie hinzu, der hier nicht gerechnet wird.
