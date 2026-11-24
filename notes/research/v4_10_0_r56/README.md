# v4.10.0-r56: Λ als Eingabe (Negativ-Schluss des OP5-Rests) (Stand 23.11.)

23. November 2026. Autorentscheidung im Projekt-Thread „OP5-Weg entscheiden“: Wahl „Negativ-Schluss (A)“ gegen den Attraktor-Weg
(Entscheidungsvorlage mit Aufwand und Risiken beider Wege vorab im Thread). Die Runde bündelt r03, r05, r06 und v4.9.0-r69/r70 zu einer Aussage über
eine ausdrücklich genannte Klasse 𝒦 und prüft die beiden tragenden Mechanismen mit Wolfram Language. **Erkundung, nicht blind** (Ergebnis stand
analytisch vorher fest), keine H-Nummer, kein Entscheidungskriterium. Skript-Nummer k242.

## Vorwissen geprüft
- `sources/research/parts/v4100-post-release-layers.tex`: r03.5 (unter G2 kein Λ nach dem Urknall, Λ = a·V_min frei), r04 (G1: (a+b)·V_min frei),
  r05.3–r05.5 (OP5 getrennt; Epoche „heute“; H96; H97 widerlegt), r06.3 (Λ als Integrationskonstante bei Dorau–Much), r55.3/r55.4/r55.6.
- `sources/research/parts/v490-post-release-layers.tex`: r69 (kein Weg legt den absoluten Vakuumterm fest; gemeinsamer Versatz unbeobachtbar;
  affiner Zweig löst für jede Konstante; passiver Frame-Wechsel skaliert nur), r70.3 (H48 widerlegt), r70.4.
- `notes/research/v4_10_0_r05/` (Rückschau, Fundstellen, Brückenvorschlag), `predictions/Vorab_Notiz_H96_*`, `Ergebnis_H97_*`.
- `notes/research/op_cross_map_2026_11_23/README.md` (Negativ-Schluss nur Rest von OP5, unabhängig von OP1, Q1, Q2).
- `wiki/Offene-Probleme.md`, gemeinsamer Kern Punkt 4 (Λ als Integrationskonstante als Anforderung).
- `notes/research/v4_10_0_w1/Zurueckgestellte_Ideen.md`: I3 (in beiden Formen gescheitert), I4 (scheitert unter den geltenden Lesarten); kein
  Auslöser führt zu einem anderen Ausweg. Der Attraktor-Weg wird als **I7** zurückgestellt.

**Suchrichtung:** Rückwärts. Ziel „Λ ist in 𝒦 nicht festgelegt“; notwendige Bedingungen: (i) keine Gleichung in 𝒦 wählt die Konstante, (ii) keine
Skala in 𝒦, (iii) die Auslesung H96 legt sie nicht fest. Alle drei werden einzeln geprüft.

**Werkzeugwahl:** Wolfram Language (MCP-Kernel) für die symbolischen Nullreste und die Epochen-Lösung. Qiskit nicht eingesetzt: keine
Quantenschaltung, kein Zustands- oder Messproblem.

| Eintrag | Inhalt |
|---|---|
| r56.1 | Klasse 𝒦: (K1) Frame-Abbildungen und Auslesungen, (K2) W1/W2 unter G1/G2, (K3) semiklassischer Weg (r06), (K4) OP5-Vergleichsmodell mit affinem Zweig, (K5) Markov-Kaskade mit Brücken Γ = εH |
| r56.2 | Die Konstante fällt aus jeder Bewegungsgleichung in 𝒦: V → V + c ändert die Feldgleichung nicht (Differenz 0, exakt) und fügt (ρ, p) = (ac, −ac), w = −1 hinzu; spurfreie Friedmann-Gleichung + Erhaltung: d/dt(H² − κρ/3) = 0 (exakt); K1, K4, K5 aus r69, r05.5 |
| r56.3 | Keine Skala in 𝒦: alle festgelegten Zahlen dimensionslos und von Ordnung eins; Λℓ_P² = 2,85·10⁻¹²² (Planck 2018), −ln = 279,9 |
| r56.4 | Die Auslesung tauscht Λ gegen die Epoche: Ω_M(x) = β² hat für jedes Λ > 0 genau eine Lösung, x*³ = κρ_M0(1 − β²)/(3β²Λ); Λ = 3(1 − β²)H*² = 2,0944603·H*² |
| r56.5 | Folgerung: In 𝒦 ist der Absolutwert von Λ Eingabe, gleichwertig die Epoche „heute“; No-go für den Bestand, nicht für jede Erweiterung. OP5 offen, H96 offen, Attraktor-Weg als I7 zurückgestellt |

## Bilanz der Setzungen
- **Gesetzt:** die Liste 𝒦; Λ oder gleichwertig die Epoche „heute“ (Autorentscheidung 6.11.).
- **Hergeleitet:** r56.2–r56.4.
- **Wohin die offene Wahl wandert:** zur Epoche. Das „warum heute“ ist dieselbe Eingabe wie der Wert von Λ, keine zweite.

## Dateien
- `rounds/v4100_r56_round.tex` (wörtlich an `sources/research/parts/v4100-post-release-layers.tex` angehängt)
- `llm/k242_lambda_input.wl`, `llm/k242_out.txt` (tatsächliche Print-Ausgaben, Nullreste und Warnungen getrennt)

OP1–OP5, C5, C6/T2 offen; kein Guard berührt.
