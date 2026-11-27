# Ergebnis H193: Getrennte Felder je HS-Stufe tragen die Quarkmassen nicht (Test, k401, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H193_Getrennte_Felder_je_HS_Stufe.md`, Commit 74ecdb6,
vor der Rechnung). H193a ist nicht blind (Kontrolle, der Größenabstand ist analytisch vorhersehbar), H193c ein Bericht.
**Werkzeuge:** Python (numpy, scipy) für die Rastersuche über Regeln, Zuordnungen und σ-Abstände; Wolfram Language für die exakten
stufeneigenen Größen und Verhältnisse (`k401b_gegenprobe.wl`, `k401b_out.txt`), bestätigt Python exakt. Qiskit nicht nötig (keine
Schaltung). Die Coprozessor-Maschine (Baustufe 2) ist hier nicht das richtige Werkzeug: H193 ist ein Zahlen-Fit über feste Regeln,
kein Bandlauf mit Drehung/Messung. **Anlass:** „ja" des Autors (27.11., 09:03) zur zweiten Gabel nach H192.

## Modell
Quark-Masse m = Einheit · S(Stufe) · Sektorfaktor. Drei Generationen eines Sektors auf drei aufsteigenden HS-Stufen
(HS(1..4) = ℂ, ℍ, 𝕆, 𝕊; Dimension 2, 4, 8, 16). Prüfstein sind die zwei dimensionslosen Generationsverhältnisse je Sektor
(die Einheit fällt heraus). Lesart (i) stufenfest: S folgt einer festen Regel aus einer stufeneigenen Größe, kein Fit je Feld.
Lesart (ii) frei: S je Stufe eine freie Zahl.

## Ergebnis

**H193a (nicht blind, Kontrolle).** Die beobachteten Generationsverhältnisse sind groß und zwischen den Sektoren ungleich:

| | g2/g1 | g3/g2 |
|---|---|---|
| Up (PDG) | 589 | 135 |
| Down (PDG) | 19,9 | 44,7 |

Die stufeneigenen Verhältnisse sind dagegen klein: Dimension je Schritt Faktor 2; Casimir a_{k+1}/a_k = 1,63 bzw. 1,37;
Gewicht 2^(1−γ_L a_k) fällt je Schritt um Faktor ≈ 0,44–0,46. Der Größenabstand (Faktor 1–2 gegen 20–589) ist genau wie vorab
angesagt: ein bis drei Größenordnungen.

**H193b (Test): widerlegt.** Über die vorab festgelegte Kandidatenliste (16 Regeln × 4 Zuordnungen), Lesart (i):
- Beste stufenfeste Regel je Sektor nach **Verhältnis**-Abstand: Up `1/2^d` auf Stufen (4,3,2) → Modellverhältnisse [256, 16] vs.
  [589, 135], max Faktor **8,5×** daneben; Down `2^d` auf (1,2,3) → [4, 16] vs. [19,9, 44,7], max Faktor **5,0×** daneben.
- Eine **gemeinsame** Regel für beide Sektoren (je Sektor nur eine Gesamteinheit gefittet, dieselbe Stufenzuordnung): bester
  Fall `1/2^d` → **Up 217,5σ, Down 190,6σ**. Kriterium „bestätigt" (beide < 3σ): **nein**.
- Bester Einzelsektor-σ-Abstand einer stufenfesten Regel überhaupt: Up 217,5σ, Down 153,8σ. Kein Sektor kommt unter 3σ.

Damit ist weder „bestätigt" (beide < 3σ) noch „teilweise" (ein Sektor < 3σ) erfüllt: **widerlegt** — der vorab offengelegte
erwartete Ausgang.

**H193c (Bericht, Parameterzählung).** Lesart (ii): drei freie Skalen je Sektor treffen drei Massen exakt (Residuum 0). Sechs
freie Zahlen für sechs Massen — die Trennung in getrennte Felder ist in dieser Lesart **inhaltsleer**. Die Trennung trägt nur,
wenn die Stufe die Skala festlegt, und genau das scheitert in H193b.

**Kontrolle.** 2000 erfundene Massensätze gleicher Größenordnung durch dasselbe Raster: ein Sektor < 3σ (frei gefittete Einheit)
in **0,7 %** der Fälle, beide Sektoren < 3σ in **0,0 %**. Die echten Daten liegen bei 154–218σ, also weit außerhalb selbst dieser
seltenen Zufallstreffer. Das Modell ist nicht knapp daneben, sondern strukturell falsch.

## Lesart
Getrennte Felder je HS-Stufe erzeugen die Quark-Hierarchie **nicht aus sich heraus**. Entweder legt die Stufe die Skala fest —
dann sind die Verhältnisse (Faktor 1–2, höchstens 16 bei einer exponentiellen Regel) um das 5- bis 300-fache zu klein, und eine
Regel kann die ungleichen Up- und Down-Verhältnisse ohnehin nicht zugleich tragen (derselbe **Up-≠-Down-Widerstand** wie
H184–H190). Oder jedes Feld bekommt seine eigene freie Skala — dann ist das Modell eine Tautologie mit sechs Knöpfen für sechs
Massen. Die bloße Trennung kauft nichts.

Damit sind nach „Lesart wechseln" beide benannten Gabeln geprüft: **gemeinsame Geometrie** (H192, teilweise: Oktant ja, kleine
Winkel angepasst) und **getrennte Felder** (H193, widerlegt). Die Lesart „Quarks auf eigener HS-Stufe" trägt die Sektorstruktur
(welche Stufe, welche Dimension — das war H178–H182), aber keine Massenquelle, die die Generationsverhältnisse festlegt. Das
Bild ist das von H190: Mechanismus und Zuordnung stimmen, die **Skala der Verhältnisse** fehlt weiter. Das zweite kleine
Verhältnis je Sektor hat bisher kein Weg erzeugt.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Zuordnung Generation → drei aufsteigende HS-Stufen | gesetzt (vorab, feste Liste) |
| Stufeneigene Skala S(Stufe) aus Dimension/Casimir/Gewicht | geprüft, kein Fit je Feld — trägt nicht |
| Generationsverhältnisse (beobachtet) | nicht eingegeben; Prüfstein |
| exakte Massen bei freier Skala je Stufe (Lesart ii) | angepasst (Parameter = Daten, inhaltsleer) |
| Up ≠ Down bei einer gemeinsamen Regel | nicht trennbar (wie H184–H190) |

## Grenzen
Fester Satz von Regeln und Zuordnungen, keine kontinuierliche Funktionensuche (die wäre ein verkappter Fit). Keine Dynamik, nur
Skalenzuordnung. OP3/OP4 (Quarkmassen) bleiben offen. Nächste frei: H194, k402.
