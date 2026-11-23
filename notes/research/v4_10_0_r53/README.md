# v4.10.0-r53: Zählregeln als Dimensionsformel und Frame-Austausch für C5 (OP1, C5) (Stand 23.11.)

23. November 2026. Auftrag des Autors: „148 und 149 prüfen“, danach „Runde r53 anlegen“. Die Runde übernimmt die Erkundung
`../openai_148_149_fulltext_2026_11_23/` in den Companion (Quelle für die Ergänzungen in Physik-Paper und Preprint 5.6). Erkundung, nicht
blind, keine H-Nummer. Grundlage: OpenAI-Familien 148 und 149 (openai/math @ 4eaee875, unbegutachtet, Lean-Formalisierungen laut Sammlung,
von uns nicht geprüft).

| Eintrag | Inhalt |
|---|---|
| r53.1 | Zählgleichung in natürlichen Einheiten r_j = e^{−2π√(j(j+1))} = Moran-Gleichung; mit Gibbs-Gewichten H(p)/χ = γ exakt; für endliche Abschneidungen ohne exakte Überlappung dim_H μ = γ nach 148; in T-Einheiten (D > 1) nicht anwendbar |
| r53.2 | Gewicht 2 von M braucht zwei verschiedene Abbildungen für \|j, ±j⟩; zusammengelegt oder nur einer zugelassen: γ₁ = 0,161586; T: Dimension 0; gespiegelte Kopien mit eigenem Zentrum zählen voll, um dasselbe Zentrum gespiegelte überlappen in längeren Verkettungen |
| r53.3 | Zwei Kontraktionen vertauschen genau bei gleichem Fixpunkt; Reihenfolge-Unabhängigkeit aller Verkettungen kollabiert den Attraktor auf einen Punkt |
| r53.4 | Lesart: Gewicht 2 verlangt eine Auslese, die beide Orientierungen unterscheidet, ohne eine auszuwählen (H118, Q1); U2 und T-Regel nicht hergeleitet |
| r53.5 | Frame-Austausch als schwach reversibles Massenwirkungsnetz: C5_M ≥ ε > 0 für alle Zeiten (149); C5_M → 0 nur einseitig wie die Kragenrekursion |
| r53.6 | klassisch: keine endliche Null in Massenwirkungsnetzen; endliche Null braucht nicht-Lipschitz-Dynamik oder Vorzeichenwechsel; bei S = N² ist ein Nulldurchgang eine doppelte Nullstelle |
| r53.7 | Form (iii) von C5: es bleiben nicht-Lipschitz-Dynamik am Nullpunkt (im Bestand nicht bekannt) oder Vorzeichenwechsel (für den Score gescheitert, r21.12); Netzmodell ist eine Setzung |

Rechnungen und Ausgaben: `../openai_148_149_fulltext_2026_11_23/` (`op1_148_moran_overlap.wl`, `c5_149_exchange.wl`, je mit `_stdout.txt`).
Runde als Datei: `rounds/v4100_r53_round.tex`.

OP1–OP5, C5, C6/T2 offen; kein Guard berührt.
