# Vorab-Notiz H75: Ist die M–T-Paarung stabil, wenn die Sektoren nur über die Gravitation gekoppelt sind?

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert, nicht blind (a, b analytisch vorab gesehen; c bekanntes Ergebnis von Bondi 1957).**

## Vorwissen geprüft
- H74 (`Ergebnis_H74_Stabilitaet_MT.md`): Bei direkter linearer Kopplung ist die exakte Paarung instabil (Rate ε/2ω). Offen blieb die Kopplung nur über die Gravitation.
- `Wirkung_W2_Higgs.md`: Kaplan–Sundrum (Energieparität) setzen auf eine Kopplung nur über die Gravitation.
- Literatur (Vorwissen, nicht nachgeschlagen): Bondi 1957, ein Paar aus positiver und negativer Masse beschleunigt gemeinsam unbegrenzt (Durchgehen, „runaway“) bei erhaltener Energie und erhaltenem Impuls.

## Aufbau (k189), Newtonscher Grenzfall, klassisch
- Zwei drucklose Flüssigkeiten: Materie (Dichte ρ_A > 0) und Tachyon-Sektor mit F3-Vorzeichen (träge und schwere Masse negativ, Dichte −ρ_B). Beide fallen im selben Potential gleich (a = −∇Φ), die Quelle ist ∇²Φ = 4πG(ρ_A δ_A − ρ_B δ_B).
- Lineare Störungen: ẍ = 4πG N x mit x = (δ_A, δ_B) und N = [[ρ_A, −ρ_B], [ρ_A, −ρ_B]]. Analytisch: Spur ρ_A − ρ_B, Determinante 0. Bei ρ_A = ρ_B ist N nilpotent (N² = 0).
- Gewichte: Photon (ρ_A = ρ_B) und Materie (ρ_B/ρ_A = x = β_sym²). Kontrolle: zwei normale Flüssigkeiten, N = [[ρ_A, ρ_B], [ρ_A, ρ_B]].
- Nichtlinear: zwei Punktmassen +m und −m im Abstand d, ruhend, 1D-Integration.

## Hypothese H75
- **H75a:** Bei Photon-Gewichten wächst keine Störung exponentiell; die relative Mode δ_A − δ_B wächst höchstens linear in t (Jordan-Block).
- **H75b:** Bei Materie-Gewichten gibt es genau eine exponentiell wachsende Mode mit Rate √(4πG(ρ_A − ρ_B)), also die gewöhnliche Jeans-Instabilität mit der effektiven Dichte ρ_A(1 − x); die Kontrolle mit zwei normalen Flüssigkeiten wächst mit √(4πG(ρ_A + ρ_B)).
- **H75c (bekannt):** Das Punktpaar ±m beschleunigt gemeinsam mit konstanter Beschleunigung Gm/d², bei konstantem Abstand, erhaltener Energie und erhaltenem Impuls.

## Entscheidung
| Teil | bestätigt | widerlegt |
|---|---|---|
| a | max. Wachstum über t = 0…50 (Einheiten 4πGρ_A = 1) ≤ linear: |δ(t)|/t beschränkt, kein Exponent > 1e-6 | exponentielles Wachstum |
| b | gemessene Rate innerhalb 1 % der vorhergesagten | Abweichung > 5 % |
| c | Abstand konstant auf 1e-9, Beschleunigung konstant auf 1e-9 | Abweichung > 1e-6 |

## Grenzen
Newtonscher, linearer bzw. Zwei-Körper-Grenzfall, klassisch. Die Expansion, relativistische Effekte und vor allem der quantenmechanische Vakuumzerfall in Paare positiver und negativer Energie über Gravitonen (das Hauptproblem bei Kaplan–Sundrum) sind nicht erfasst.
